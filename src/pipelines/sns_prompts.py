"""Prompt templates for the SNS content pipeline stages."""

# ---------------------------------------------------------------------------
# Shared constants (DRY — used by both generate and review prompts)
# ---------------------------------------------------------------------------
TWO_LAYER_STRATEGY = """\
ComInc. SNS operates on two layers. Sho doesn't sell tourism — he sells himself. Takada is the stage.

**Layer 1 — Sho's thoughts & perspective (X/Twitter):**
Japanese society's absurdities seen from a foreigner's eye. AI in practice. 20 years abroad → why is Japan like this? Entrepreneurship philosophy. Anti-groupthink.

**Layer 2 — ComInc. services & place (Instagram):**
Takada castle town, kominka, experiences. "Unseen Japan" through the eyes of someone who lives there.

The audience flow: "This person is interesting" → "I want to visit where they live."\
"""

PLATFORM_RULES = """\
- **X (EN)**: Sharp, opinionated, hook-first. Sho's voice — like a well-traveled friend with a hot take. Max 280 chars per tweet. If a thread, each segment under 280. Minimal hashtags (0-2, only if truly relevant).
- **Instagram (EN)**: Visual storytelling. Caption 50-300 words. Hashtags 10-15 (note: place in first comment). Include a specific, actionable visual_direction.
- **Instagram (JP)**: Natural Japanese — NOT machine-translated. Include Japanese discovery hashtags (#上越 #高田 #古民家 #雪国 etc).\
"""

# ---------------------------------------------------------------------------
# Stage 1: Fetch unprocessed ideas from Notion
# ---------------------------------------------------------------------------
FETCH_IDEAS_PROMPT = """\
Search the Notion database "SNS Ideas" for all items where Status = "unprocessed".

For each item, return the following as a JSON array:
- page_id (the Notion page URL or ID)
- title
- content (full body text of the page)
- tags (if any)
- source (voice_memo, observation, article, thought, photo)
- created_date

Return ONLY valid JSON. No additional commentary.

Example format:
```json
[
  {
    "page_id": "abc123",
    "title": "Saw amazing sunset at Takada",
    "content": "The sunset over Takada Castle was incredible today...",
    "tags": ["unseen_japan", "seasonal"],
    "source": "observation",
    "created_date": "2026-03-30"
  }
]
```
"""

# ---------------------------------------------------------------------------
# Stage 2: Generate platform-specific drafts from a raw idea
# ---------------------------------------------------------------------------
GENERATE_DRAFTS_PROMPT = """\
You are drafting SNS content for ComInc. based on a raw idea from Sho.

## Raw Idea
{memo_content}

## Today's Date
{current_date}

## Strategy Reference
{sns_strategy_excerpt}

## Seasonal Context
Current season: {season_context}

---

## 2-Layer Strategy
""" + TWO_LAYER_STRATEGY + """

---

For this idea, generate drafts for the following v1 platforms ONLY:
- **X (Twitter)**: English only — Layer 1 voice
- **Instagram**: English AND Japanese — Layer 2 voice

Do NOT generate Threads, LinkedIn, YouTube, or TikTok drafts yet.

### Rules
""" + PLATFORM_RULES + """
- Decide which content pillar this maps to
- Score seasonal relevance 1-10
- Suggest posting order and timing
- Include a CTA in every draft (follow, visit cominc.co, DM, save, share, etc.)

### Quality Gate (self-review before output)
You are a professional marketer. Before returning ANY draft, check:
1. **Brand voice** — Does this sound like Sho? First-person, warm, slightly irreverent. NOT corporate, NOT tourist-board generic, NOT try-hard.
2. **2-Layer alignment** — X = Sho's thoughts (Layer 1). Instagram = place/experience (Layer 2). If a draft is on the wrong layer, rewrite it.
3. **CTA** — Every draft has a natural call-to-action. No exceptions.
4. **Platform fit** — X under 280 chars? IG caption 50-300 words? Hashtag counts correct?
5. **"Would Sho actually post this?"** — If no, rewrite or drop it entirely. Set that platform to skip_platforms with a reason.
Better to output 1 strong draft than 3 mediocre ones. Be ruthless with yourself.

### Output Format (return ONLY valid JSON):
```json
{{
  "source_idea_id": "{page_id}",
  "content_pillar": "<pillar_name>",
  "seasonal_relevance_score": 8,
  "drafts": [
    {{
      "platform": "x_twitter",
      "language": "en",
      "content": "<tweet or thread text>",
      "thread_count": 1
    }},
    {{
      "platform": "instagram",
      "language": "en",
      "content": "<caption text>",
      "hashtags": ["#tag1", "#tag2"],
      "format_suggestion": "reel",
      "visual_direction": "<what the photo/video should show>"
    }},
    {{
      "platform": "instagram",
      "language": "jp",
      "content": "<caption text in Japanese>",
      "hashtags": ["#tag1", "#tag2"],
      "format_suggestion": "reel",
      "visual_direction": "<same as EN>"
    }}
  ],
  "suggested_post_order": ["x_twitter_en", "instagram_en", "instagram_jp"],
  "suggested_timing": "<reasoning about when to post>",
  "skip_platforms": [],
  "quality_note": "<brief note on what was cut or rewritten during self-review, or 'all passed'>"
}}
```
"""

# ---------------------------------------------------------------------------
# Stage 3: Write drafts to Notion SNS Queue
# ---------------------------------------------------------------------------
WRITE_DRAFTS_PROMPT = """\
Create pages in the Notion database "SNS Queue" for each draft below.

For each entry, set these properties:
- Title: [platform] | [language] | [first 30 chars of content]
- Platform: (instagram / x_twitter)
- Language: (en / jp)
- Content Pillar: {content_pillar}
- Status: "draft"
- Seasonal Score: {seasonal_score}
- Suggested Timing: {suggested_timing}
- Draft Content: put the full draft text in the page body

Also update the source idea page (in "SNS Ideas" database) with page_id = {source_idea_id}:
- Set Status to "processed"

Here are the drafts to create:
{drafts_json}
"""

# ---------------------------------------------------------------------------
# Stage 4: Scheduling recommendation (runs separately)
# ---------------------------------------------------------------------------
SCHEDULE_PROMPT = """\
Review the Notion "SNS Queue" database. Look at all items with Status = "approved".

Based on:
- Content pillar distribution targets (35% Unseen Japan, 25% Bridge, 20% Powder & Peaks, 15% Kominka Life, 5% Community Intel)
- Weekly posting cadence (Mon: X thread + IG Reel, Wed: IG Carousel, Fri: X take + IG Reel)
- Current date: {current_date}, season: {season_context}
- Platform algorithm best practices
- What has recently been posted (Status = "published")

Produce a 7-day posting schedule. For each post, specify:
- Date and suggested time
- Platform
- Language
- Content title
- Reasoning for the ordering

Create this schedule as a new Notion page titled "SNS Schedule — Week of {week_start}" under ComInc. HQ.
"""
