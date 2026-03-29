"""Base configuration shared across all ComInc. agents."""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
KNOWLEDGE_DIR = PROJECT_ROOT / "data" / "knowledge"
PROMPTS_DIR = PROJECT_ROOT / "src" / "prompts"


def load_prompt(agent_name: str) -> str:
    """Load system prompt for a given agent from the prompts directory."""
    prompt_file = PROMPTS_DIR / f"{agent_name}.md"
    if prompt_file.exists():
        return prompt_file.read_text(encoding="utf-8")
    raise FileNotFoundError(f"Prompt file not found: {prompt_file}")


def load_knowledge(filename: str) -> str:
    """Load a knowledge base file."""
    knowledge_file = KNOWLEDGE_DIR / filename
    if knowledge_file.exists():
        return knowledge_file.read_text(encoding="utf-8")
    raise FileNotFoundError(f"Knowledge file not found: {knowledge_file}")


# ---------------------------------------------------------------------------
# MCP server configurations — single source of truth
# ---------------------------------------------------------------------------
MCP_SERVERS = {
    "notion": {
        "command": "npx",
        "args": ["-y", "@anthropic-ai/notion-mcp"],
    },
    "gmail": {
        "command": "npx",
        "args": ["-y", "@anthropic-ai/gmail-mcp"],
    },
    "google-calendar": {
        "command": "npx",
        "args": ["-y", "@anthropic-ai/google-calendar-mcp"],
    },
    "github": {
        "command": "npx",
        "args": ["-y", "@anthropic-ai/github-mcp"],
    },
    "figma": {
        "command": "npx",
        "args": ["-y", "@anthropic-ai/figma-mcp"],
    },
    "stitch": {
        "url": "https://stitch.googleapis.com/mcp",
        "headers": {"X-Goog-Api-Key": os.environ.get("STITCH_API_KEY", "")},
    },
}


def get_mcp_servers(*names: str) -> dict:
    """Return a subset of MCP server configs by name."""
    return {name: MCP_SERVERS[name] for name in names if name in MCP_SERVERS}


# ---------------------------------------------------------------------------
# Shared tool presets — DRY: define once, reuse in orchestrator.py
# ---------------------------------------------------------------------------
TOOLS_BASE = ["Read", "Glob", "Grep"]
TOOLS_WRITE = [*TOOLS_BASE, "Write"]
TOOLS_WEB = [*TOOLS_WRITE, "WebSearch", "WebFetch"]
TOOLS_DEV = [*TOOLS_WRITE, "Edit", "Bash"]


# ---------------------------------------------------------------------------
# Agent → MCP mapping — which agents get which MCP servers
# ---------------------------------------------------------------------------
AGENT_MCP = {
    "hana":   ("notion", "gmail", "google-calendar"),
    "fin":    ("notion",),
    "law":    ("notion",),
    "webber": ("notion", "figma", "github", "stitch"),
    "clare":  ("notion", "figma", "stitch"),
    "yuri":   ("notion", "figma", "stitch"),
    "dev":    ("notion", "github", "figma", "stitch"),
    "cat":    ("notion",),
    "kai":    ("notion", "gmail", "google-calendar"),
    "min":    ("notion", "gmail", "google-calendar"),
}


def get_agent_mcp(agent_name: str) -> dict:
    """Return MCP server configs for a specific agent."""
    servers = AGENT_MCP.get(agent_name, ())
    return get_mcp_servers(*servers)
