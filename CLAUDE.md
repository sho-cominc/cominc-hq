# CLAUDE.md — ComInc. Project Handoff Note

Hey Claude 👋 — before anything else, read this:

## 🔴 Step 1: Check Sho's Notes in Notion FIRST

**Always start every session by reading this page:**
👉 [📝 Sho's Notes](https://www.notion.so/334860170c1781949710cc1db811afc4)

This is the live handoff memo. Sho writes what he needs, what he's thinking, and where things left off.
It's updated from any device — more current than this file.
**Read it before doing anything. It overrides any assumptions below.**

---

Here's the static context that doesn't change often:

---

## Who & What

- **Project**: ComInc. (cominc.co) — Inbound tourism business based in Joetsu, Niigata, Japan
- **Founder**: Shotaro Shimizu (Sho) — bilingual EN/JP, based in a 130-year-old kominka farmhouse
- **Core offer**: Guided tours + kominka Airbnb stay + experiences (ski, cherry blossoms, sake, hiking)
- **Tagline**: "What you need is somebody who understands you."

---

## Current Status (as of 2026-03-30)

- Sho is **still working full-time** — available days in April: 1, 6, 12, 16, 24, 28 only
- **Minpaku (民泊) registration**: application in progress, awaiting permit number
- **Airbnb listing**: fully drafted in Notion, ready to publish the moment permit number arrives
- **cominc.co**: under construction (Astro 4.x + Cloudflare Pages)
- **joetsuexplorer.com**: existing sub-brand, running in parallel
- **NZ bank funds**: pending documents → will be transferred to business account on arrival
- **Subsidy meeting**: booked for 4/6 at 14:00

## Key upcoming dates (April)
- **4/1** — Kominka photo shoot (Airbnb) + strategic meeting with Kawano-san (hotel owner x4) & former boss
- **4/6** — Subsidy consultation meeting 14:00 + Instagram first post
- **4/12** — City hall (minpaku permit) + Airbnb listing go-live
- **4/16** — 7:00 見積もり・丸山さん訪問
- **4/24** — Chamber of Commerce + 小規模事業者持続化補助金 application
- **4/28** — Subsidy docs final submission + IT導入補助金 consultation

---

## Dev Setup

```bash
# Install dependencies (first time only)
cd cominc-hq
python -m pip install -e .

# Copy and fill in your API key
cp .env.example .env
# → Add ANTHROPIC_API_KEY=sk-ant-...

# Start the agent system
python run.py

# Or run a specific agent
python run.py --agent fin "your task"
```

### Available agents
`hana` (secretary) · `fin` (finance) · `law` (legal) · `webber` (web director) · `dev` (developer) · `cat` (marketing) · `kai` (guide) · `min` (minpaku) · `yuri` (UX) · `clare` (creative)

### Dev servers (.claude/launch.json)
- `cominc-agents` → port 3000 (Python agent system)
- `cominc-website` → port 8000 (static HTML mockup)

---

## Notion Workspace
All plans live in **ComInc. HQ** on Notion:
- 💰 Monetization Plan (EN)
- 📑 事業計画書・財務予測 2026 (JP) — ready for subsidy applications
- 🏠 Airbnb 出品パッケージ — listing copy in EN/JP, pricing, house rules, check-in guide
- 📣 Marketing Sprint Week 1 — Instagram content calendar
- 🌐 全体俯瞰レポート — Hana's overview of everything

---

## Important context
- Kawano-san (4/1 meeting) = local hotel owner x4, potential key partner — handle with care
- Sho's git identity is set: `Shotaro Shimizu <sho@myokojoetsu.com>`
- Python is installed at `C:/Users/reservation_agent03/AppData/Local/Programs/Python/Python312/`
- joetsuexplorer.com appears to be offline — check before any web tasks involving it

---

Good luck. The plan is solid. 🏔️
