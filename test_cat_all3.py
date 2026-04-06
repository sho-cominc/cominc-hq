"""Test: Cat generates drafts for all 3 SNS Ideas. No Notion MCP — text in, JSON out."""
import sys
import json
import anyio
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage
from src.agents.base import load_prompt, TOOLS_BASE

OUTPUT_DIR = Path(__file__).parent

IDEAS = [
    {
        "page_id": "333860170c1781c9bacfe7e24c8d1a27",
        "title": "ありのままが最高のコンテンツ",
        "content": "僕が興味あるのは背伸びした地方ではない。ありのままの生活、ありのままの食事、ありのままの住処。それこそが最高のコンテンツであると思う。",
        "tags": ["unseen_japan", "kominka_life"],
    },
    {
        "page_id": "333860170c17815e9809ef1949ebf3ab",
        "title": "大人は言い訳をしてはいけない",
        "content": "僕は負けず嫌いだ。日本が世界と戦えないとも思いたくない。世界をリードするために変わってほしいと願うことも多くある。変わらなければいけないのはいつも大人だ。大人は言い訳をしてはいけない。なぜならば、社会を作ったのは大人達だ。",
        "tags": ["the_bridge"],
    },
    {
        "page_id": "333860170c17813dae50c77c49c3d668",
        "title": "ギャップの根源は成長を止めること",
        "content": "子供は生まれてから社会に出るまで、能動的に学び、必然的に成長しているわけだ。だが大人はそうではない。残念ながら多くの人たちが学びを止め、成長を止めてしまう。それこそがギャップの根源だと思う。僕は成長を止めた人とはギャップを感じる。感じているのはジェネレーションギャップではない。",
        "tags": ["the_bridge"],
    },
]

PROMPT_TEMPLATE = """You are drafting SNS content for ComInc. based on a raw idea from Sho.

## Raw Idea
{title}

{content}

## Today's Date
2026-04-01

## Seasonal Context
Current season: Cherry blossoms (Takada Castle)

---

## 2-Layer Strategy
ComInc. SNS operates on two layers. Sho doesn't sell tourism - he sells himself. Takada is the stage.
Layer 1 - Sho's thoughts & perspective (X/Twitter): Japanese society's absurdities seen from a foreigner's eye. AI in practice. 20 years abroad -> why is Japan like this? Entrepreneurship philosophy. Anti-groupthink.
Layer 2 - ComInc. services & place (Instagram): Takada castle town, kominka, experiences. Unseen Japan through the eyes of someone who lives there.
The audience flow: This person is interesting -> I want to visit where they live.

---

For this idea, generate drafts for the following v1 platforms ONLY:
- X (Twitter): English only - Layer 1 voice
- Instagram: English AND Japanese - Layer 2 voice

### Rules
- X (EN): Sharp, opinionated, hook-first. Sho's voice - like a well-traveled friend with a hot take. Max 280 chars per tweet. If a thread, each segment under 280. Minimal hashtags (0-2).
- Instagram (EN): Visual storytelling. Caption 50-300 words. Hashtags 10-15 (in first comment). Include visual_direction.
- Instagram (JP): Natural Japanese - NOT machine-translated. Include Japanese hashtags.
- Decide which content pillar this maps to
- Score seasonal relevance 1-10
- Include a CTA in every draft

### Quality Gate (self-review before output)
Before returning ANY draft, check:
1. Brand voice - Does this sound like Sho? First-person, warm, slightly irreverent. NOT corporate.
2. 2-Layer alignment - X = Sho thoughts (Layer 1). Instagram = place/experience (Layer 2).
3. CTA - Every draft has a natural call-to-action.
4. Platform fit - X under 280 chars? IG caption 50-300 words?
5. Would Sho actually post this? If no, rewrite or drop it.

Return ONLY valid JSON, no markdown fences, no commentary:
{{
  "source_idea_id": "{page_id}",
  "content_pillar": "<pillar_name>",
  "seasonal_relevance_score": 8,
  "drafts": [
    {{
      "platform": "x_twitter",
      "language": "en",
      "content": "<tweet text>",
      "thread_count": 1
    }},
    {{
      "platform": "instagram",
      "language": "en",
      "content": "<caption>",
      "hashtags": ["#tag1"],
      "format_suggestion": "carousel",
      "visual_direction": "<direction>"
    }},
    {{
      "platform": "instagram",
      "language": "jp",
      "content": "<JP caption>",
      "hashtags": ["#tag1"],
      "format_suggestion": "carousel",
      "visual_direction": "<direction>"
    }}
  ],
  "suggested_post_order": ["x_twitter_en", "instagram_en", "instagram_jp"],
  "suggested_timing": "<reasoning>",
  "skip_platforms": [],
  "quality_note": "<note>"
}}
"""


async def generate_for_idea(idea: dict, system_prompt: str) -> dict | None:
    prompt = PROMPT_TEMPLATE.format(**idea)
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

    raw = "\n".join(parts)

    # Try to extract JSON
    import re
    # Try raw parse
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        pass
    # Try ```json block
    match = re.search(r"```json\s*\n(.*?)\n```", raw, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    # Try first { ... }
    match = re.search(r"\{[\s\S]*\}", raw)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass

    # Save raw for debugging
    debug_file = OUTPUT_DIR / f"debug_{idea['page_id'][:8]}.txt"
    debug_file.write_text(raw, encoding="utf-8")
    return None


async def main():
    system_prompt = load_prompt("marketing")
    results = []

    for i, idea in enumerate(IDEAS):
        sys.stdout.buffer.write(f"[{i+1}/3] Generating: {idea['title']}...\n".encode("utf-8"))
        sys.stdout.flush()

        result = await generate_for_idea(idea, system_prompt)
        if result:
            results.append(result)
            sys.stdout.buffer.write(f"  OK: {len(result.get('drafts', []))} drafts\n".encode("utf-8"))
        else:
            sys.stdout.buffer.write(f"  FAIL: could not parse\n".encode("utf-8"))
        sys.stdout.flush()

    output_file = OUTPUT_DIR / "test_cat_all3_output.json"
    output_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    sys.stdout.buffer.write(f"\nDone. {len(results)}/3 ideas processed. Output: test_cat_all3_output.json\n".encode("utf-8"))


if __name__ == "__main__":
    anyio.run(main)
