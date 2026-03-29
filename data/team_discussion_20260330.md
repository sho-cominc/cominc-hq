# Team Discussion Summary — 2026-03-30
**While Sho sleeps, the team discussed: SNS strategy, blog integration, MCP auto-posting**

---

## Key Decisions Requiring Sho's Input

### 1. SNS Platform Auto-Posting via MCP
Cat + Dev investigated MCP-connected SNS options. **Three viable paths:**

| Option | Cost | Platforms | Setup |
|--------|------|-----------|-------|
| **Postiz** (self-hosted) | Free | 30+ (X, IG, LinkedIn, FB, Threads, Bluesky...) | Deploy on Render (Next.js + PostgreSQL + Redis) |
| **Ayrshare** (API) | Paid | 13+ (75+ tools, most features) | `npm install` + API key |
| **Publora** (hosted) | Free tier | 11+ (18 MCP tools) | Sign up + MCP connect |

**Dev's recommendation:** Postiz — self-hosted, free, aligns with our Render stack, and has native MCP support. We can add it as an MCP server for Cat to auto-post through.

**Cat's preference:** Ayrshare for completeness (scheduling, auto-hashtags, analytics in one tool), but understands the cost concern. Publora as a compromise.

> **Sho decides:** Which one? Or start with Publora (free hosted, zero setup) and migrate to Postiz if we outgrow it?

### 2. SNS Platform Priority
Cat recommends this rollout:

**Tier 1 (now):** Instagram, YouTube, X/Twitter
**Tier 2 (month 2-3):** TikTok, Pinterest, LinkedIn
**Tier 3 (claim handles only):** Threads, Bluesky

> **Action needed:** Claim @cominc_japan on all platforms this week.

### 3. Blog Integration into cominc.co
The team proposes 5 blog categories mapped to the 3 service pillars:

- **Discover** (旅) — seasonal guides, hidden gems, food
- **Live** (住) — relocation, cost of living, kominka life
- **Build** (商) — real estate, business opportunities
- **Understand** (文化) — cultural explainers, cross-cutting
- **Stay** (泊) — kominka experience, gateway marketing

Technical: Notion DB as CMS → notion-astro-loader → Astro SSG → Render → Cloudflare

> **Sho decides:** Green light on blog categories? 2 posts/month to start OK?

### 4. Content Waterfall Strategy
1 source piece (e.g., 3-min video Sho shoots) becomes 8-12 platform outputs:
- YouTube full video → IG Reel → TikTok → X thread → IG carousel → 3 Pinterest pins → LinkedIn post → blog post

**Sho's role:** Photography/video, on-camera, DM conversations, content approval
**AI (Cat) handles:** Captions, hashtags, scheduling, repurposing, analytics, pin creation

> **Budget:** ~3,000-5,000 JPY/month (Buffer + Canva)

---

## What the Team Can Advance Without Sho

### Already Done
- [x] Stitch MCP connected (API key created, base.py updated)
- [x] cominc.co prototype v3 — light base "宵桜" theme applied
- [x] SNS MCP research complete (research_sns_mcp.md)
- [x] Blog strategy document (strategy_blog.md)
- [x] SNS strategy document (marketing/sns_strategy_v1.md)

### Ready to Do (Pending Sho's Approval)
- [ ] Set up Notion "Blog Posts" database
- [ ] Design blog index + post template in Astro
- [ ] Clare: Design SNS templates (IG carousel, Reel cover, quote card)
- [ ] Cat: Draft first 2 weeks of IG/X content
- [ ] Dev: Set up Postiz or Publora MCP connection
- [ ] Claim @cominc_japan handles on all platforms

### SEO Quick Wins Identified
- "Myoko vs Niseko" comparison content (high search volume)
- "Takada Castle cherry blossoms" guide (April timing)
- "Moving to rural Japan foreigner" (low competition)
- "Akiya abandoned house Japan" (growing interest)

---

## Files Created This Session
- `data/prototype/index.html` — cominc.co homepage prototype (v3, 宵桜 light theme)
- `data/research_sns_mcp.md` — SNS MCP auto-posting research
- `data/strategy_blog.md` — Blog strategy & content calendar
- `data/marketing/sns_strategy_v1.md` — Full SNS strategy document
- `data/team_discussion_20260330.md` — This summary
- `src/agents/base.py` — Updated with Stitch MCP config
- `.env` — Added STITCH_API_KEY
