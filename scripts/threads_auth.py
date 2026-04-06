#!/usr/bin/env python3
"""
Threads API OAuth Token Generator for ComInc.

Walks through the full OAuth flow:
1. Opens authorization URL in browser
2. Runs local HTTPS server to catch the redirect
3. Exchanges auth code for short-lived token
4. Exchanges short-lived token for long-lived token (60 days)
5. Saves tokens to .env
"""

import http.server
import json
import os
import re
import ssl
import subprocess
import sys
import threading
import urllib.parse
import webbrowser
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REDIRECT_URI = "https://localhost:8080/callback"
SCOPES = "threads_basic,threads_content_publish,threads_read_replies,threads_manage_replies,threads_manage_insights"
GRAPH_BASE = "https://graph.threads.net"

SCRIPT_DIR = Path(__file__).resolve().parent
ENV_PATH = SCRIPT_DIR.parent / ".env"

# ---------------------------------------------------------------------------
# .env helpers
# ---------------------------------------------------------------------------

def load_env(path: Path) -> dict:
    """Read a .env file into a dict (simple KEY=VALUE format)."""
    env = {}
    if not path.exists():
        return env
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                env[key.strip()] = value.strip()
    return env


def save_env(path: Path, updates: dict):
    """Update (or append) keys in a .env file."""
    lines = []
    existing_keys = set()

    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and "=" in stripped:
            key = stripped.split("=", 1)[0].strip()
            if key in updates:
                new_lines.append(f"{key}={updates[key]}\n")
                existing_keys.add(key)
                continue
        new_lines.append(line)

    # Append any keys that weren't already in the file
    for key, value in updates.items():
        if key not in existing_keys:
            new_lines.append(f"{key}={value}\n")

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


# ---------------------------------------------------------------------------
# HTTP(S) helpers — requests or urllib fallback
# ---------------------------------------------------------------------------

try:
    import requests as _requests

    def http_post(url, params):
        resp = _requests.post(url, data=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def http_get(url, params):
        resp = _requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

except ImportError:
    import urllib.request

    def _fetch(req):
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())

    def http_post(url, params):
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(url, data=data, method="POST")
        return _fetch(req)

    def http_get(url, params):
        qs = urllib.parse.urlencode(params)
        req = urllib.request.Request(f"{url}?{qs}", method="GET")
        return _fetch(req)


# ---------------------------------------------------------------------------
# Self-signed cert for the local HTTPS callback server
# ---------------------------------------------------------------------------

def _generate_self_signed_cert(cert_path: Path, key_path: Path):
    """Generate a self-signed cert using openssl CLI (available on most systems)."""
    subprocess.run(
        [
            "openssl", "req", "-x509", "-newkey", "rsa:2048",
            "-keyout", str(key_path),
            "-out", str(cert_path),
            "-days", "1",
            "-nodes",
            "-subj", "/CN=localhost",
        ],
        check=True,
        capture_output=True,
    )


# ---------------------------------------------------------------------------
# Local callback server
# ---------------------------------------------------------------------------

auth_code_result = {"code": None, "error": None}
server_ready = threading.Event()


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    """Handles the OAuth redirect callback."""

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == "/callback":
            if "code" in params:
                auth_code_result["code"] = params["code"][0]
                self._respond(200, "Authorization successful! You can close this tab and return to the terminal.")
            elif "error" in params:
                auth_code_result["error"] = params.get("error_description", params["error"])[0]
                self._respond(400, f"Authorization failed: {auth_code_result['error']}")
            else:
                auth_code_result["error"] = "No code in callback"
                self._respond(400, "No authorization code received.")
        else:
            self._respond(404, "Not found")

    def _respond(self, status, message):
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        html = f"<html><body><h2>{message}</h2></body></html>"
        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        # Suppress noisy server logs
        pass


def run_callback_server(cert_path: Path, key_path: Path):
    """Start an HTTPS server on port 8080 and wait for the callback."""
    server = http.server.HTTPServer(("localhost", 8080), CallbackHandler)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(str(cert_path), str(key_path))
    server.socket = ctx.wrap_socket(server.socket, server_side=True)

    server_ready.set()
    # Handle requests until we get a code or error
    while auth_code_result["code"] is None and auth_code_result["error"] is None:
        server.handle_request()
    server.server_close()


# ---------------------------------------------------------------------------
# Token exchange
# ---------------------------------------------------------------------------

def exchange_code_for_short_token(app_id, app_secret, code):
    """Exchange authorization code for a short-lived token."""
    print("\n[2/4] Exchanging auth code for short-lived token...")
    data = http_post(f"{GRAPH_BASE}/oauth/access_token", {
        "client_id": app_id,
        "client_secret": app_secret,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
        "code": code,
    })
    if "access_token" not in data:
        raise RuntimeError(f"Failed to get short-lived token: {data}")
    print("    Short-lived token obtained.")
    return data["access_token"], data.get("user_id")


def exchange_for_long_token(app_secret, short_token):
    """Exchange short-lived token for a long-lived token (60 days)."""
    print("[3/4] Exchanging for long-lived token (60 days)...")
    data = http_get(f"{GRAPH_BASE}/access_token", {
        "grant_type": "th_exchange_token",
        "client_secret": app_secret,
        "access_token": short_token,
    })
    if "access_token" not in data:
        raise RuntimeError(f"Failed to get long-lived token: {data}")
    expires_in = data.get("expires_in", 5184000)
    days = expires_in // 86400
    print(f"    Long-lived token obtained (expires in {days} days).")
    return data["access_token"]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("  Threads API OAuth Token Generator — ComInc.")
    print("=" * 60)

    # 1. Load env
    env = load_env(ENV_PATH)
    app_id = env.get("THREADS_APP_ID")
    app_secret = env.get("THREADS_APP_SECRET")

    if not app_id or not app_secret:
        print(f"\nERROR: THREADS_APP_ID and/or THREADS_APP_SECRET not found in {ENV_PATH}")
        print("Please add them to your .env file first.")
        sys.exit(1)

    print(f"\n  App ID:     {app_id}")
    print(f"  App Secret: {app_secret[:8]}...{app_secret[-4:]}")
    print(f"  .env path:  {ENV_PATH}")

    # 2. Generate self-signed cert for localhost HTTPS
    cert_dir = SCRIPT_DIR / ".certs"
    cert_dir.mkdir(exist_ok=True)
    cert_path = cert_dir / "localhost.crt"
    key_path = cert_dir / "localhost.key"

    print("\nGenerating self-signed certificate for localhost HTTPS...")
    try:
        _generate_self_signed_cert(cert_path, key_path)
    except FileNotFoundError:
        print("\nERROR: 'openssl' command not found.")
        print("Please install OpenSSL or Git Bash (which includes it).")
        print("Alternatively, on Windows you can install it via: winget install ShiningLight.OpenSSL")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"\nERROR: Failed to generate self-signed cert: {e}")
        sys.exit(1)

    # 3. Start callback server in background
    server_thread = threading.Thread(
        target=run_callback_server,
        args=(cert_path, key_path),
        daemon=True,
    )
    server_thread.start()
    server_ready.wait(timeout=5)

    # 4. Build authorization URL and open in browser
    auth_url = (
        f"https://threads.net/oauth/authorize"
        f"?client_id={app_id}"
        f"&redirect_uri={urllib.parse.quote(REDIRECT_URI, safe='')}"
        f"&scope={urllib.parse.quote(SCOPES, safe='')}"
        f"&response_type=code"
    )

    print("\n" + "-" * 60)
    print("[1/4] Opening authorization URL in your browser...")
    print("\nIf the browser doesn't open, copy this URL manually:\n")
    print(f"  {auth_url}\n")
    print("NOTE: Your browser will warn about the self-signed certificate.")
    print("      This is expected — click 'Advanced' > 'Proceed' to continue.")
    print("-" * 60)

    webbrowser.open(auth_url)

    # 5. Wait for callback
    print("\nWaiting for authorization callback on https://localhost:8080/callback ...")
    server_thread.join(timeout=300)  # 5 minute timeout

    if auth_code_result["error"]:
        print(f"\nERROR: {auth_code_result['error']}")
        sys.exit(1)

    if not auth_code_result["code"]:
        print("\nERROR: Timed out waiting for authorization callback (5 min).")
        sys.exit(1)

    code = auth_code_result["code"]
    print(f"\n    Authorization code received: {code[:10]}...")

    # 6. Exchange for tokens
    try:
        short_token, user_id = exchange_code_for_short_token(app_id, app_secret, code)
        long_token = exchange_for_long_token(app_secret, short_token)
    except Exception as e:
        print(f"\nERROR during token exchange: {e}")
        sys.exit(1)

    # 7. If user_id wasn't in the token response, fetch it
    if not user_id:
        print("    Fetching user ID...")
        try:
            me = http_get(f"{GRAPH_BASE}/me", {"access_token": long_token})
            user_id = me.get("id")
        except Exception:
            print("    WARNING: Could not fetch user ID. You may need to set THREADS_USER_ID manually.")

    # 8. Save to .env
    print("[4/4] Saving tokens to .env...")
    updates = {"THREADS_ACCESS_TOKEN": long_token}
    if user_id:
        updates["THREADS_USER_ID"] = str(user_id)
    save_env(ENV_PATH, updates)

    # 9. Cleanup certs
    try:
        cert_path.unlink(missing_ok=True)
        key_path.unlink(missing_ok=True)
        cert_dir.rmdir()
    except OSError:
        pass

    # Done!
    print("\n" + "=" * 60)
    print("  SUCCESS!")
    print("=" * 60)
    print(f"\n  THREADS_ACCESS_TOKEN saved to {ENV_PATH}")
    if user_id:
        print(f"  THREADS_USER_ID:     {user_id}")
    print(f"\n  Token is valid for ~60 days.")
    print("  Run this script again before it expires to refresh.")
    print()


if __name__ == "__main__":
    main()
