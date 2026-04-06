"""Hana reviews SNS Queue drafts and decides which to approve."""
import sys
import json
import anyio
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage
from src.agents.base import load_prompt, TOOLS_BASE

OUTPUT_FILE = Path(__file__).parent / "test_hana_review_output.json"
DRAFTS_FILE = Path(__file__).parent / "test_cat_all3_output.json"

PROMPT = """You are Hana, Secretary of ComInc., reviewing SNS draft content on behalf of Sho (CEO).

Your job: decide which drafts to APPROVE for posting and which to HOLD or CUT.

## Your Review Criteria (as Sho's proxy)
1. **Does this sound like Sho?** — You know him well. He's direct, warm, slightly irreverent. NOT corporate, NOT generic tourism.
2. **Would this embarrass ComInc.?** — Check for anything that could be misread, too aggressive, or off-brand.
3. **Is the quality high enough?** — Better to post nothing than something mediocre.
4. **Timing** — Consider the seasonal score and suggested timing. Prioritize high-score, time-sensitive content.
5. **Balance** — Don't approve 9 posts at once. Select the strongest 3-6 for this week's batch.

## 2-Layer Strategy
- X (Layer 1): Sho's thoughts, philosophy, hot takes — EN only
- Instagram (Layer 2): Place, experience, visual storytelling — EN + JP
- The flow: "This person is interesting" → "I want to visit where they live"

## Drafts to Review
{drafts_json}

## Instructions
Review each draft. Return ONLY valid JSON:
```json
{{
  "review_summary": "<1-2 sentence overall assessment>",
  "approved": [
    {{
      "source_idea_id": "<id>",
      "platform": "<platform>",
      "language": "<lang>",
      "title_snippet": "<first 30 chars>",
      "reason": "<why approved>"
    }}
  ],
  "held": [
    {{
      "source_idea_id": "<id>",
      "platform": "<platform>",
      "language": "<lang>",
      "title_snippet": "<first 30 chars>",
      "reason": "<why held — what needs fixing or why to wait>"
    }}
  ],
  "suggested_post_order": ["<list of approved titles in recommended posting order>"],
  "note_to_sho": "<any note Hana wants to leave for Sho>"
}}
```
"""


async def main():
    system_prompt = load_prompt("secretary")
    drafts_data = json.loads(DRAFTS_FILE.read_text(encoding="utf-8"))

    prompt = PROMPT.format(
        drafts_json=json.dumps(drafts_data, ensure_ascii=False, indent=2)
    )

    parts: list[str] = []
    async for msg in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            system_prompt=system_prompt,
            allowed_tools=TOOLS_BASE,
            permission_mode="bypassPermissions",
            max_turns=5,
        ),
    ):
        if isinstance(msg, ResultMessage):
            parts.append(msg.result)

    result = "\n".join(parts)
    OUTPUT_FILE.write_text(result, encoding="utf-8")
    sys.stdout.buffer.write(b"Done. Output: test_hana_review_output.json\n")


if __name__ == "__main__":
    anyio.run(main)
