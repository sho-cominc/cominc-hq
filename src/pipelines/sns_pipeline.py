"""SNS Content Pipeline — reads ideas from Notion, generates multi-platform drafts via Cat.

Usage:
    python run.py --pipeline sns              # Process unprocessed ideas
    python run.py --pipeline sns-schedule     # Generate weekly posting schedule
    python run.py --pipeline sns-factcheck    # Run Hana fact-check on drafts
    python run.py --pipeline sns-publish      # Publish approved/ready posts to Threads
    python run.py --pipeline sns-auto         # Scheduled auto-post (for cron)
    python run.py --pipeline sns-series       # Post next item from threads_intro_series.json
"""

import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

from src.agents.base import load_prompt, get_agent_mcp, TOOLS_WEB
from src.pipelines.sns_prompts import (
    FETCH_IDEAS_PROMPT,
    GENERATE_DRAFTS_PROMPT,
    WRITE_DRAFTS_PROMPT,
    SCHEDULE_PROMPT,
    HANA_FACTCHECK_PROMPT,
    THREADS_PUBLISH_PROMPT,
    THREADS_UPDATE_STATUS_PROMPT,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
STRATEGY_FILE = Path(__file__).parent.parent.parent / "data" / "marketing" / "sns_strategy_v1.md"

# Agent key → prompt file mapping (mirrors AGENT_REGISTRY in orchestrator.py)
_PROMPT_FILE_MAP = {
    "cat": "marketing",
    "hana": "hana",
    "webber": "web_director",
}

# Threads intro series data file
THREADS_SERIES_FILE = Path(__file__).parent.parent.parent / "data" / "content" / "threads_intro_series.json"

# JST timezone (UTC+9)
JST = timezone(timedelta(hours=9))

# Scheduled posting times (JST hours)
SCHEDULED_POST_TIMES = [8, 19, 20]

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
    stderr_lines: list[str] = []

    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            system_prompt=system_prompt,
            allowed_tools=TOOLS_WEB,
            mcp_servers=get_agent_mcp(agent_name),
            permission_mode="bypassPermissions",
            max_turns=30,
            stderr=lambda line: stderr_lines.append(line),
        ),
    ):
        if isinstance(message, ResultMessage):
            response_parts.append(message.result)

    if not response_parts and stderr_lines:
        print(f"   ⚠️  Agent stderr ({agent_name}):")
        for line in stderr_lines[-10:]:
            print(f"      {line}")

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
    """Full pipeline: fetch ideas -> Cat generates drafts -> write to Notion -> Sho reviews."""
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

    # Stage 2 + 3: For each idea, generate → write
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

        draft_count = len(drafts_data.get("drafts", []))
        skipped = drafts_data.get("skip_platforms", [])
        quality_note = drafts_data.get("quality_note", "")
        print(f"   ✅ {draft_count} draft(s) generated.")
        if skipped:
            print(f"   ✂️  Skipped: {skipped}")
        if quality_note and quality_note != "all passed":
            print(f"   📝 Cat QA: {quality_note}")

        # --- Stage 3: Write drafts to Notion (Status=draft → Sho reviews) ---
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
    print("   → Sho: SNS Queue の draft を確認して approved に変えてね。")


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


# ---------------------------------------------------------------------------
# Stage 4: Hana fact-check gate
# ---------------------------------------------------------------------------
FACTCHECK_FETCH_PROMPT = """\
Query the Notion database "SNS Queue" for all items where Status = "draft".

For each item, return:
- page_id
- title
- platform
- content (full body text)
- author (if available)

Return ONLY valid JSON array. No additional commentary.
"""


async def run_sns_factcheck() -> None:
    """Hana reviews all 'draft' items in SNS Queue for factual accuracy."""
    print("\n🔍 SNS Fact-Check Pipeline (Hana) starting...\n")

    # Fetch drafts from Notion
    print("📥 Fetching drafts with Status = 'draft'...")
    drafts_response = await _call_agent("hana", FACTCHECK_FETCH_PROMPT)
    drafts = _extract_json(drafts_response)

    if not drafts or (isinstance(drafts, list) and len(drafts) == 0):
        print("✅ No drafts to review. Pipeline complete.")
        return

    if isinstance(drafts, dict):
        drafts = [drafts]

    print(f"   Found {len(drafts)} draft(s) to review.\n")

    passed_count = 0
    failed_count = 0

    for i, draft in enumerate(drafts, 1):
        title = draft.get("title", "untitled")
        page_id = draft.get("page_id", "unknown")
        platform = draft.get("platform", "unknown")
        content = draft.get("content", "")
        author = draft.get("author", "unknown")

        print(f"🔎 Reviewing [{i}/{len(drafts)}]: {title}")

        prompt = HANA_FACTCHECK_PROMPT.format(
            page_id=page_id,
            platform=platform,
            author=author,
            content=content,
            current_date=date.today().isoformat(),
        )
        response = await _call_agent("hana", prompt)
        result = _extract_json(response)

        if result and result.get("passed"):
            passed_count += 1
            print(f"   ✅ PASSED: {result.get('notes', '')}")
        else:
            failed_count += 1
            issues = result.get("issues", []) if result else ["Could not parse review"]
            print(f"   ❌ NEEDS REVISION: {issues}")

    print(f"\n🎉 Fact-check complete. Passed: {passed_count}, Needs revision: {failed_count}")


# ---------------------------------------------------------------------------
# Stage 5: Publish to Threads
# ---------------------------------------------------------------------------
FETCH_READY_PROMPT = """\
Query the Notion database "SNS Queue" for all items where Status = "approved" OR Status = "ready".
Filter to platform = "threads" if available, otherwise return all.

For each item, return:
- page_id
- title
- content (full body text)
- scheduled_date (if available)
- scheduled_time (if available)

Return ONLY valid JSON array. No additional commentary.
"""


async def run_sns_publish_threads() -> None:
    """Publish approved/ready posts to Threads via MCP."""
    print("\n📤 Threads Publish Pipeline starting...\n")

    # Fetch approved/ready items
    print("📥 Fetching posts ready for publishing...")
    ready_response = await _call_agent("cat", FETCH_READY_PROMPT)
    posts = _extract_json(ready_response)

    if not posts or (isinstance(posts, list) and len(posts) == 0):
        print("✅ No posts ready to publish. Pipeline complete.")
        return

    if isinstance(posts, dict):
        posts = [posts]

    print(f"   Found {len(posts)} post(s) ready to publish.\n")

    published = 0
    failed = 0

    for i, post in enumerate(posts, 1):
        title = post.get("title", "untitled")
        page_id = post.get("page_id", "unknown")
        content = post.get("content", "")

        print(f"📤 Publishing [{i}/{len(posts)}]: {title}")

        # Publish via Threads MCP
        publish_prompt = THREADS_PUBLISH_PROMPT.format(content=content)
        response = await _call_agent("cat", publish_prompt)
        result = _extract_json(response)

        if result and result.get("success"):
            post_id = result.get("post_id", "unknown")
            print(f"   ✅ Published! Post ID: {post_id}")

            # Update Notion status to "published"
            update_prompt = THREADS_UPDATE_STATUS_PROMPT.format(
                page_id=page_id,
                publish_date=date.today().isoformat(),
                post_id=post_id,
            )
            await _call_agent("cat", update_prompt)
            published += 1
        else:
            error = result.get("error", "Unknown error") if result else "Could not parse response"
            print(f"   ❌ Failed: {error}")
            failed += 1

    print(f"\n🎉 Publish complete. Published: {published}, Failed: {failed}")


# ---------------------------------------------------------------------------
# Threads intro series — post from local JSON file
# ---------------------------------------------------------------------------
def _load_series() -> list[dict]:
    """Load the threads intro series JSON file."""
    if THREADS_SERIES_FILE.exists():
        return json.loads(THREADS_SERIES_FILE.read_text(encoding="utf-8"))
    return []


def _save_series(series: list[dict]) -> None:
    """Save updated series back to the JSON file."""
    THREADS_SERIES_FILE.write_text(
        json.dumps(series, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _get_next_ready_post(series: list[dict]) -> dict | None:
    """Find the next 'ready' post whose scheduled time has passed."""
    now = datetime.now(JST)
    for post in series:
        if post["status"] != "ready":
            continue
        scheduled = datetime.fromisoformat(
            f"{post['scheduled_date']}T{post['scheduled_time']}:00+09:00"
        )
        if now >= scheduled:
            return post
    return None


def _get_due_post_for_time(series: list[dict]) -> dict | None:
    """Find a post that is due at the current scheduled time window.

    Checks if current JST hour matches one of SCHEDULED_POST_TIMES and there is
    a ready post scheduled for today at that hour.
    """
    now = datetime.now(JST)
    current_hour = now.hour

    if current_hour not in SCHEDULED_POST_TIMES:
        return None

    today_str = now.strftime("%Y-%m-%d")
    target_time = f"{current_hour:02d}:00"

    for post in series:
        if post["status"] != "ready":
            continue
        if post["scheduled_date"] == today_str and post["scheduled_time"] == target_time:
            return post
    return None


async def run_threads_series_post() -> None:
    """Post the next due item from the threads intro series.

    This function can be called manually or by a cron/scheduled task.
    It finds the next 'ready' post whose scheduled_date/time has passed,
    publishes it to Threads, and updates the JSON file status.
    """
    print("\n🧵 Threads Intro Series — Posting next item...\n")

    series = _load_series()
    if not series:
        print("❌ Could not load threads_intro_series.json")
        return

    post = _get_next_ready_post(series)
    if not post:
        print("✅ No posts due for publishing right now.")
        remaining = [p for p in series if p["status"] == "ready"]
        if remaining:
            next_post = remaining[0]
            print(f"   Next scheduled: Post {next_post['post_number']} ({next_post['author']}) "
                  f"at {next_post['scheduled_date']} {next_post['scheduled_time']} JST")
        else:
            print("   All posts in the series have been published!")
        return

    print(f"📤 Publishing Post {post['post_number']} by {post['author']}...")
    print(f"   Scheduled: {post['scheduled_date']} {post['scheduled_time']} JST")
    print(f"   Content preview: {post['content'][:60]}...")

    # Publish via Threads MCP through Cat agent
    publish_prompt = THREADS_PUBLISH_PROMPT.format(content=post["content"])
    response = await _call_agent("cat", publish_prompt)
    result = _extract_json(response)

    if result and result.get("success"):
        post_id = result.get("post_id", "unknown")
        print(f"   ✅ Published! Post ID: {post_id}")

        # Update series JSON status
        post["status"] = "published"
        post["published_at"] = datetime.now(JST).isoformat()
        post["threads_post_id"] = post_id
        _save_series(series)
        print(f"   ✅ Series file updated.")
    else:
        error = result.get("error", "Unknown error") if result else "Could not parse response"
        print(f"   ❌ Failed to publish: {error}")
        post["status"] = "failed"
        post["error"] = error
        _save_series(series)


# ---------------------------------------------------------------------------
# Scheduled auto-post — designed to be called by cron at 8:00, 19:00, 20:00 JST
# ---------------------------------------------------------------------------
async def run_sns_autopost() -> None:
    """Auto-post handler for scheduled execution.

    Checks both:
    1. Threads intro series (local JSON) for due posts
    2. Notion SNS Queue for approved/ready items

    Designed to be triggered by cron or Windows Task Scheduler at:
      - 08:00 JST
      - 19:00 JST
      - 20:00 JST

    Example crontab (Linux/Mac):
      0 8,19,20 * * * cd /path/to/cominc-agents && python run.py --pipeline sns-auto

    Example schtasks (Windows):
      schtasks /create /tn "ComInc SNS AutoPost" /tr "python run.py --pipeline sns-auto" ^
        /sc daily /st 08:00 /ru SYSTEM
      (repeat for 19:00 and 20:00)
    """
    now = datetime.now(JST)
    print(f"\n⏰ SNS Auto-Post triggered at {now.strftime('%Y-%m-%d %H:%M')} JST\n")

    # Priority 1: Check threads intro series for a post due right now
    series = _load_series()
    due_post = _get_due_post_for_time(series) if series else None

    if due_post:
        print(f"🧵 Found series post due: Post {due_post['post_number']} by {due_post['author']}")
        await run_threads_series_post()
    else:
        # Priority 2: Check for any past-due series posts
        overdue = _get_next_ready_post(series) if series else None
        if overdue:
            print(f"🧵 Found overdue series post: Post {overdue['post_number']} by {overdue['author']}")
            await run_threads_series_post()
        else:
            # Priority 3: Publish from Notion SNS Queue
            print("📋 No series posts due. Checking Notion SNS Queue...")
            await run_sns_publish_threads()

    print(f"\n⏰ Auto-post cycle complete.")
