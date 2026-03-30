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
  "skip_platforms": []
}}
```
"""

# ---------------------------------------------------------------------------
# Stage 2.5: Webber reviews drafts for quality
# ---------------------------------------------------------------------------
REVIEW_DRAFTS_PROMPT = """\
You are reviewing SNS content drafts as Webber, Web Director of ComInc.

Your job is quality control. Review each draft and either approve (with edits) or cut it entirely.

## Review Criteria

### 1. Brand Voice Consistency
- Tone: warm, knowledgeable, slightly irreverent. Like a well-traveled friend who lives there.
- First-person always ("I" / "we"), never third-person ("ComInc. offers...")
- NOT: corporate, overly polished, tourist-board generic, try-hard cool
- Emoji: minimal (one at most per caption, never a wall)
- This is Sho's voice. If it doesn't sound like a real person who lives in rural Japan, cut it.

### 2. 2-Layer Strategy Alignment
""" + TWO_LAYER_STRATEGY + """
- If a draft puts place/experience content on X or thought/philosophy content on Instagram, rewrite it to fit or cut it.

### 3. CTA Check
- Every draft MUST include a call-to-action (follow, visit cominc.co, DM, save, share, link in bio, etc.)
- CTA should feel natural, not forced.

### 4. Platform-Specific Optimization
""" + PLATFORM_RULES + """

### 5. Quality Gate
- If a draft is mediocre, generic, or doesn't meet criteria — CUT IT. Better to post nothing than weak content.
- Be ruthless.

## Source Idea
{memo_title}

## Drafts to Review
{drafts_json}

## Strategy Reference
{sns_strategy_excerpt}

---

Return ONLY valid JSON:
```json
{{
  "source_idea_id": "{source_idea_id}",
  "content_pillar": "{content_pillar}",
  "seasonal_relevance_score": {seasonal_score},
  "review_summary": "<1-2 sentence summary of review>",
  "drafts": [
    {{
      "platform": "x_twitter",
      "language": "en",
      "status": "approved",
      "content": "<final content — edited if needed>",
      "edits_made": "<what was changed, or 'none'>",
      "thread_count": 1
    }},
    {{
      "platform": "instagram",
      "language": "en",
      "status": "approved",
      "content": "<final caption>",
      "hashtags": ["#tag1"],
      "format_suggestion": "reel",
      "visual_direction": "<specific direction>",
      "edits_made": "<what was changed, or 'none'>"
    }},
    {{
      "platform": "instagram",
      "language": "jp",
      "status": "approved",
      "content": "<final caption in Japanese>",
      "hashtags": ["#tag1"],
      "format_suggestion": "reel",
      "visual_direction": "<same as EN>",
      "edits_made": "<what was changed, or 'none'>"
    }}
  ],
  "suggested_timing": "{suggested_timing}"
}}
```

For cut drafts, set status to "cut" and include "cut_reason".
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
