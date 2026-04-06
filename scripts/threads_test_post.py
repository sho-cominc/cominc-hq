#!/usr/bin/env python3
"""
Threads API Test Post — ComInc.

Dry-run script that shows what a test post would look like
without actually publishing anything.

Usage:
    python scripts/threads_test_post.py
    python scripts/threads_test_post.py --publish   # Actually post it
"""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ENV_PATH = SCRIPT_DIR.parent / ".env"
GRAPH_BASE = "https://graph.threads.net"

TEST_MESSAGE = "Hello from ComInc. \U0001f3d4\ufe0f"  # 🏔️

# ---------------------------------------------------------------------------
# .env loader
# ---------------------------------------------------------------------------

def load_env(path: Path) -> dict:
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


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

try:
    import requests as _requests

    def http_post(url, params):
        resp = _requests.post(url, data=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

except ImportError:
    import urllib.parse
    import urllib.request

    def http_post(url, params):
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(url, data=data, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            import json as _json
            return _json.loads(resp.read().decode())


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    publish = "--publish" in sys.argv

    print("=" * 60)
    print("  Threads API Test Post — ComInc.")
    print("=" * 60)

    env = load_env(ENV_PATH)
    access_token = env.get("THREADS_ACCESS_TOKEN")
    user_id = env.get("THREADS_USER_ID")

    if not access_token:
        print(f"\nERROR: THREADS_ACCESS_TOKEN not found in {ENV_PATH}")
        print("Run threads_auth.py first to obtain a token.")
        sys.exit(1)

    if not user_id:
        print(f"\nERROR: THREADS_USER_ID not found in {ENV_PATH}")
        print("Run threads_auth.py first to obtain your user ID.")
        sys.exit(1)

    print(f"\n  User ID: {user_id}")
    print(f"  Token:   {access_token[:12]}...{access_token[-4:]}")
    print(f"  Message: {TEST_MESSAGE}")

    # --- Step 1: Create media container ---
    create_url = f"{GRAPH_BASE}/v1.0/{user_id}/threads"
    create_params = {
        "media_type": "TEXT",
        "text": TEST_MESSAGE,
        "access_token": access_token,
    }

    print("\n" + "-" * 60)
    print("STEP 1 — Create media container")
    print(f"  POST {create_url}")
    print(f"  Params: {json.dumps({k: v if k != 'access_token' else '***' for k, v in create_params.items()}, indent=4)}")

    # --- Step 2: Publish ---
    publish_url = f"{GRAPH_BASE}/v1.0/{user_id}/threads_publish"
    print("\nSTEP 2 — Publish the container")
    print(f"  POST {publish_url}")
    print(f"  Params: {json.dumps({'creation_id': '<container_id from step 1>', 'access_token': '***'}, indent=4)}")
    print("-" * 60)

    if not publish:
        print("\n  DRY RUN — No request was sent.")
        print("  To actually publish, run:  python scripts/threads_test_post.py --publish")
        print()
        return

    # Actually publish
    print("\n  Publishing for real...")

    try:
        # Step 1: create container
        print("  Creating media container...")
        result1 = http_post(create_url, create_params)
        container_id = result1.get("id")
        if not container_id:
            print(f"  ERROR: No container ID returned: {result1}")
            sys.exit(1)
        print(f"  Container ID: {container_id}")

        # Step 2: publish
        print("  Publishing...")
        result2 = http_post(publish_url, {
            "creation_id": container_id,
            "access_token": access_token,
        })
        post_id = result2.get("id")
        print(f"  Post ID: {post_id}")
        print(f"\n  SUCCESS! Post published.")
        print(f"  View at: https://www.threads.net/post/{post_id}")

    except Exception as e:
        print(f"\n  ERROR: {e}")
        sys.exit(1)

    print()


if __name__ == "__main__":
    main()
