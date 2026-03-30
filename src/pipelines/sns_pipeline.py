"""SNS Content Pipeline — reads ideas from Notion, generates multi-platform drafts via Cat.

Usage:
    python run.py --pipeline sns           # Process unprocessed ideas
    python run.py --pipeline sns-schedule  # Generate weekly posting schedule
"""

import json
import re
from datetime import date, timedelta
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

from src.agents.base import load_prompt, get_agent_mcp, TOOLS_WEB
from src.pipelines.sns_prompts import (
    FETCH_IDEAS_PROMPT,
    GENERATE_DRAFTS_PROMPT,
    REVIEW_DRAFTS_PROMPT,
    WRITE_DRAFTS_PROMPT,
    SCHEDULE_PROMPT,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
STRATEGY_FILE = Path(__file__).parent.parent.parent / "data" / "marketing" / "sns_strategy_v1.md"

# Agent key → prompt file mapping (mirrors AGENT_REGISTRY in orchestrator.py)
_PROMPT_FILE_MAP = {
    "cat": "marketing",
    "webber": "web_director",
}

# Season mapping (month -> context string)
_SEASONS = {
    1: "Deep winter / powder season",
    2: "Peak ski + snow festivals",
    3: "Late season skiing, spring hints",
    4: "Cherry blossoms (Takada Castle)",
    5: "Green season begins, rice planting",
    6: "Rainy season, hydrangea",
    7: "Summer festivals, hiking",
    8: "Obon, peak domestic tourism",
    9: "Early autumn, rice harvest",
    10: "Peak autumn foliage",
    11: "Late autumn, ski season preview",
    12: "Ski season opens, year-end",
}


def _get_season_context() -> str:
    """Return current season context string."""
    return _SEASONS.get(date.today().month, "")


def _load_strategy_excerpt() -> str:
    """Load SNS strategy doc. Returns content or fallback message."""
    if STRATEGY_FILE.exists():
        content = STRATEGY_FILE.read_text(encoding="utf-8")
        # Extract sections most relevant for draft generation
        sections = []
        current: list[str] = []
        for line in content.split("\n"):
            if line.startswith("## ") and current:
                sections.append("\n".join(current))
                current = []
            current.append(line)
        if current:
            sections.append("\n".join(current))

        relevant = [s for s in sections if any(
            kw in s[:100] for kw in ("CONTENT PILLARS", "BRAND VOICE", "PLATFORM SELECTION")
        )]
        return "\n\n---\n\n".join(relevant) if relevant else content[:5000]
    return "No strategy file found. Use general best practices for tourism SNS content."


async def _call_agent(agent_name: str, prompt: str) -> str:
    """Send a prompt to a named agent and collect the full text response."""
    prompt_file = _PROMPT_FILE_MAP.get(agent_name, agent_name)
    system_prompt = load_prompt(prompt_file)
    response_parts: list[str] = []

    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            system_prompt=system_prompt,
            allowed_tools=TOOLS_WEB,
            mcp_servers=get_agent_mcp(agent_name),
            permission_mode="auto",
            max_turns=30,
        ),
    ):
        if isinstance(message, ResultMessage):
            response_parts.append(message.result)

    return "\n".join(response_parts)


def _extract_json(response: str) -> dict | list | None:
    """Extract JSON from LLM response text.

    Tries in order:
    1. Raw JSON parse of entire response
    2. JSON block between ```json and ```
    3. First { ... } or [ ... ] block
    """
    # Try raw parse
    try:
        return json.loads(response)
    except (json.JSONDecodeError, TypeError):
        pass

    # Try ```json ... ``` block
    match = re.search(r"```json\s*\n(.*?)\n```", response, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass

    # Try first JSON object or array
    for pattern in (r"\{[\s\S]*\}", r"\[[\s\S]*\]"):
        match = re.search(pattern, response)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass

    return None


# ---------------------------------------------------------------------------
# Pipeline stages
# ---------------------------------------------------------------------------
async def run_sns_pipeline() -> None:
    """Full pipeline: fetch ideas -> generate drafts -> Webber review -> write to Notion."""
    print("\n🐱 SNS Content Pipeline v1 starting...\n")

    # Stage 1: Fetch unprocessed ideas from Notion
    print("📥 Stage 1: Fetching unprocessed ideas from Notion...")
    ideas_response = await _call_agent("cat", FETCH_IDEAS_PROMPT)
    ideas = _extract_json(ideas_response)

    if not ideas or (isinstance(ideas, list) and len(ideas) == 0):
        print("✅ No unprocessed ideas found. Pipeline complete.")
        return

    if isinstance(ideas, dict):
        ideas = [ideas]

    print(f"   Found {len(ideas)} unprocessed idea(s).\n")

    # Load strategy context once (DRY — shared across all ideas and agents)
    strategy_excerpt = _load_strategy_excerpt()
    season_context = _get_season_context()

    # Stage 2 + 2.5 + 3: For each idea, generate → review → write
    for i, idea in enumerate(ideas, 1):
        title = idea.get("title", "untitled")
        page_id = idea.get("page_id", "unknown")
        content = idea.get("content", idea.get("title", ""))

        # --- Stage 2: Cat generates drafts ---
        print(f"✏️  Stage 2: Cat generating drafts for [{i}/{len(ideas)}]: {title}")

        draft_prompt = GENERATE_DRAFTS_PROMPT.format(
            memo_content=content,
            current_date=date.today().isoformat(),
            sns_strategy_excerpt=strategy_excerpt,
            season_context=season_context,
            page_id=page_id,
        )
        drafts_response = await _call_agent("cat", draft_prompt)
        drafts_data = _extract_json(drafts_response)

        if not drafts_data:
            print(f"   ⚠️  Could not parse drafts for: {title}. Skipping.")
            continue

        # --- Stage 2.5: Webber reviews drafts ---
        print(f"🔍 Stage 2.5: Webber reviewing drafts...")

        review_prompt = REVIEW_DRAFTS_PROMPT.format(
            memo_title=title,
            drafts_json=json.dumps(
                drafts_data.get("drafts", []),
                ensure_ascii=False,
                indent=2,
            ),
            sns_strategy_excerpt=strategy_excerpt,
            source_idea_id=page_id,
            content_pillar=drafts_data.get("content_pillar", "unseen_japan"),
            seasonal_score=drafts_data.get("seasonal_relevance_score", 5),
            suggested_timing=drafts_data.get("suggested_timing", ""),
        )
        review_response = await _call_agent("webber", review_prompt)
        reviewed_data = _extract_json(review_response)

        if reviewed_data:
            # Filter out cut drafts
            all_reviewed = reviewed_data.get("drafts", [])
            approved_drafts = [d for d in all_reviewed if d.get("status") != "cut"]
            cut_count = len(all_reviewed) - len(approved_drafts)

            if not approved_drafts:
                print(f"   ✂️  Webber cut all drafts for: {title}. Skipping.")
                continue

            # Replace drafts with reviewed versions
            drafts_data["drafts"] = approved_drafts
            review_summary = reviewed_data.get("review_summary", "")
            print(f"   ✅ {len(approved_drafts)} approved, {cut_count} cut.")
            if review_summary:
                print(f"   📝 Webber: {review_summary}")
        else:
            print(f"   ⚠️  Could not parse Webber's review. Using Cat's original drafts.")

        # --- Stage 3: Write approved drafts to Notion ---
        print(f"📤 Stage 3: Writing drafts to SNS Queue...")

        write_prompt = WRITE_DRAFTS_PROMPT.format(
            content_pillar=drafts_data.get("content_pillar", "unseen_japan"),
            seasonal_score=drafts_data.get("seasonal_relevance_score", 5),
            suggested_timing=drafts_data.get("suggested_timing", ""),
            source_idea_id=page_id,
            drafts_json=json.dumps(
                drafts_data.get("drafts", []),
                ensure_ascii=False,
                indent=2,
            ),
        )
        await _call_agent("cat", write_prompt)
        print(f"   ✅ Done: {title}\n")

    print("🎉 SNS Pipeline complete. Check Notion SNS Queue for drafts.")


async def run_sns_scheduling() -> None:
    """Review approved drafts and generate a weekly posting schedule."""
    print("\n📅 SNS Scheduling starting...\n")

    today = date.today()
    week_start = today - timedelta(days=today.weekday())

    prompt = SCHEDULE_PROMPT.format(
        current_date=today.isoformat(),
        season_context=_get_season_context(),
        week_start=week_start.isoformat(),
    )

    print("Analyzing approved drafts and generating schedule...")
    response = await _call_agent("cat", prompt)
    print(response)
    print("\n✅ Schedule generated. Check Notion for the weekly plan.")
