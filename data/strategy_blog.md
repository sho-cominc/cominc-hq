# ComInc. Blog Strategy (2026-03-30)

## Content Categories (5 pillars)

### A: "Discover" (旅 — Tourism)
- Seasonal guides, activity deep-dives, food stories, hidden gems, practical tips, guest stories

### B: "Live" (住 — Relocation)
- Rural Japan life, relocation guides, kominka culture, Sho's perspective, community integration

### C: "Build" (商 — Business & Real Estate)
- Real estate primers (w/ ES Hasegawa), akiya opportunities, business climate, subsidies/grants

### D: "Understand" (文化 — Cultural Translation)
- Cultural explainers, language tips, festivals, bilingual life — serves ALL audiences

### E: "Stay" (泊 — Kominka Experience)
- Property updates, guest stories, seasonal ambiance — gateway marketing

## SEO Strategy

### Primary Keyword Clusters
**Tourism (highest volume):**
- "Myoko travel guide", "Joetsu things to do", "Myoko ski vs Niseko", "Takada Castle cherry blossoms", "kominka stay Japan", "Japan snow country experience"

**Relocation (lower volume, higher intent):**
- "moving to rural Japan foreigner", "cost of living Niigata", "akiya abandoned house Japan", "digital nomad rural Japan"

**Real Estate/Business (lowest volume, highest conversion):**
- "buying property Niigata Japan", "starting business rural Japan", "Japan government subsidies rural relocation"

### Technical SEO
- Pillar + Cluster model: 5 pillar pages, cluster posts link back
- Structured data: Article, Breadcrumb, FAQ schemas
- hreflang for /en/blog/ and /ja/blog/
- URL: `/en/blog/[category]/[slug]`
- Refresh seasonal posts annually

## Content Calendar

| Month | Focus | Category |
|-------|-------|----------|
| Jan | Powder guide, onsen, winter food | 旅 + 文化 |
| Feb | Snow festivals, cherry blossom preview | 旅 |
| Mar | Season transition, relocation refresh | 旅 + 住 |
| Apr | Takada Castle guide (flagship) | 旅 + 文化 |
| May | Hiking, rice planting, spring life | 旅 + 住 |
| Jun | Sake breweries, indoor activities | 旅 + 文化 |
| Jul | Mountain guides, summer festivals | 旅 |
| Aug | Festival explainers, family guides | 旅 + 文化 |
| Sep | Harvest, food tours, real estate update | 旅 + 商 |
| Oct | Autumn colors, ski preview | 旅 |
| Nov | Sake season, akiya opportunities | 文化 + 商 + 住 |
| Dec | Ski opening, winter kominka stay | 旅 + 泊 |

**Cadence:** 2 posts/month min, 4 target. 60% seasonal, 40% evergreen.

## Technical Implementation

### Notion Database: "Blog Posts"
Properties: Title, Title_JA, Slug, Category (discover/live/build/understand/stay), Tags, Season, Pillar (旅/住/商), Status, Publish Date, Featured Image, SEO Title, SEO Description, Primary Keyword, Related Posts (relation), CTA Pillar, Locale (en/ja/both)

### Astro Routes
```
/en/blog/                    — Index (filterable)
/en/blog/[category]/         — Category archive
/en/blog/[category]/[slug]   — Post
/ja/blog/                    — Japanese mirror
```

### Build Pipeline
Notion edit → Status: Published → GitHub Action/webhook → Render rebuild → Cloudflare CDN

## Blog Design (Matching Prototype Style)

### Index Page
- Seasonal hero photo, Cormorant Garamond headline, kanji watermark 物語
- Asymmetric masonry grid (NOT uniform), featured post spans 2 cols
- Pill-style category filters, sakura accent on active
- "Load more" button (not infinite scroll — SEO)

### Post Page
- Cinematic full-bleed hero image
- ~700px reading column, Cormorant Garamond for H2/H3
- Pull-quotes with sakura-pink left border
- Images break out to full-width
- Sticky sidebar TOC + contextual CTA
- Post footer: related posts + pillar CTA + newsletter signup

## Cross-Linking Strategy

### Pillar CTAs (bottom of every post)
| Pillar | CTA | Links To |
|--------|-----|----------|
| 旅 | "Experience this with a local guide" | joetsuexplorer.com |
| 住 | "Thinking about making this home?" | /relocation or contact |
| 商 | "See the opportunity? Let's talk." | /consultation or contact |

### Cross-pillar Discovery
- Tourism → "Some visitors never leave..." → 住 content
- Relocation → "Before you move, come visit" → 旅 content
- Business → "See the lifestyle behind the opportunity" → 泊 content

## Implementation Phases

**Phase 1 (Month 1-2):** Notion DB, Astro templates, 3 cornerstone posts (1 per pillar), RSS, SEO basics
**Phase 2 (Month 3-4):** Category pages, filtering, 2 post/month cadence, Mailchimp newsletter
**Phase 3 (Month 5-6):** Bilingual /ja/, scroll animations, cross-link CTAs, backlink outreach
