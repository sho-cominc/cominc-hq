"""CEO Orchestrator — ComInc. multi-agent system entry point."""

from claude_agent_sdk import AgentDefinition

from src.agents.base import (
    load_prompt,
    get_mcp_servers,
    get_agent_mcp,
    TOOLS_BASE,
    TOOLS_WRITE,
    TOOLS_WEB,
    TOOLS_DEV,
)


# ---------------------------------------------------------------------------
# Agent registry — single source of truth for all 11 agents
# ---------------------------------------------------------------------------
AGENT_REGISTRY: list[dict] = [
    # ── 管理部門 / Admin ──
    {
        "key": "hana",
        "prompt_file": "secretary",
        "description": "秘書・Notion管理。全提案のユーザー目線レビュー＆スコアリング。カレンダー管理、日次/週次サマリー。",
        "tools": TOOLS_WEB,
    },
    {
        "key": "fin",
        "prompt_file": "finance",
        "description": "経理。P&L管理、青色申告準備、補助金追跡、収支アラート。",
        "tools": TOOLS_WRITE,
    },
    {
        "key": "law",
        "prompt_file": "legal",
        "description": "法務・コンプライアンス。民泊法、旅行業法、税務、契約書、許認可。",
        "tools": TOOLS_WEB,
    },
    # ── Web制作部 / Web Production ──
    {
        "key": "webber",
        "prompt_file": "web_director",
        "description": "Web制作ディレクター。技術選定、サイト設計、品質管理、チーム統括。",
        "tools": [*TOOLS_BASE, "WebFetch"],
    },
    {
        "key": "clare",
        "prompt_file": "creative_designer",
        "description": "クリエイティブデザイナー。ビジュアル、ブランディング、Figma制作。",
        "tools": TOOLS_WRITE,
    },
    {
        "key": "yuri",
        "prompt_file": "ux_designer",
        "description": "UX/UIデザイナー。情報設計、ワイヤーフレーム、ユーザビリティ。",
        "tools": TOOLS_WRITE,
    },
    {
        "key": "dev",
        "prompt_file": "web_developer",
        "description": "Web開発者。コーディング、デプロイ、パフォーマンス最適化。",
        "tools": TOOLS_DEV,
    },
    {
        "key": "cat",
        "prompt_file": "marketing",
        "description": "マーケティング。SEO、SNS、広告戦略、KPI分析、コンテンツマーケ。",
        "tools": TOOLS_WEB,
    },
    # ── 事業部門 / Operations ──
    {
        "key": "kai",
        "prompt_file": "guide",
        "description": "体験ガイド。旅程設計、ゲスト対応、予約管理。",
        "tools": TOOLS_WRITE,
    },
    {
        "key": "min",
        "prompt_file": "minpaku",
        "description": "民泊管理。ゲスト対応、チェックイン管理、清掃手配、価格調整。",
        "tools": TOOLS_WRITE,
    },
]


def build_agent_definitions() -> dict[str, AgentDefinition]:
    """Build all specialist agent definitions from the registry."""
    return {
        entry["key"]: AgentDefinition(
            description=entry["description"],
            prompt=load_prompt(entry["prompt_file"]),
            tools=entry["tools"],
        )
        for entry in AGENT_REGISTRY
    }


def get_orchestrator_config() -> dict:
    """Return the full orchestrator configuration."""
    return {
        "system_prompt": load_prompt("orchestrator"),
        "agents": build_agent_definitions(),
        "mcp_servers": get_mcp_servers(
            "notion", "gmail", "google-calendar", "github", "figma",
        ),
        "allowed_tools": [
            "Read", "Write", "Glob", "Grep",
            "WebSearch", "WebFetch", "Agent",
        ],
        "max_turns": 50,
    }
