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

- **Project**: ComInc. (cominc.co) — Sho Shimizu の個人事業。上越市高田の城下町が拠点
- **Founder**: Shotaro Shimizu (Sho) — bilingual EN/JP。高田の城下町中心部の古民家に住む（farmhouse・田舎ではない）
- **事業**: Cominca-stay.（家主居住型の民泊）、Walk & Blend（宿泊者向けセルフガイド街歩き）、日本企業向け BtoB（海外展開支援・JPサイト）
- **Tagline**: "What you need is somebody who understands you."

## 最新の状況・日付・料金はここに書かない

進捗・予定・料金・申請状況は動く情報なので、このファイルには置かない（置くと必ず古くなる）。次を見ること:
- Claude Code のメモリ `C:\Users\shota\.claude\projects\C--Users-shota-Arai-Supabase\memory\MEMORY.md` と本文（事実の正。数字は本文から取る）
- Notion の Sho's Notes（最終更新日を確認。古ければメモリを優先）
- エージェント定義の正は `~/.claude/agents/*.md`（このリポの `agents/` はバックアップ。`agents/README.md` 参照）

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
`ottar` (orchestrator) · `hana` (secretary) · `fin` (finance) · `law` (legal) · `webber` (web director) · `dev` (developer) · `clare` (creative) · `yuri` (UX) · `cat` (marketing) · `prod` (content producer) · `kai` (guide) · `min` (minpaku)

### Dev servers (.claude/launch.json)
- `cominc-agents` → port 3000 (Python agent system)
- `cominc-website` → port 8000 (static HTML mockup)

---

## Notion Workspace
All plans live in **ComInc. HQ** on Notion:
- 💰 Monetization Plan (EN)
- 📑 事業計画書・財務予測 2026 (JP) — ready for subsidy applications
- 🏠 Airbnb 出品パッケージ — 掲載文・ハウスルール（料金・チェックインは最新版の子ページとメモリで確認）
- 📣 Marketing Sprint Week 1 — Instagram content calendar
- 🌐 全体俯瞰レポート — Hana's overview of everything

---

## Important context
- Sho's git identity is set: `Shotaro Shimizu <sho@myokojoetsu.com>`
- Python is installed at `C:/Users/reservation_agent03/AppData/Local/Programs/Python/Python312/`
- joetsuexplorer.com appears to be offline — check before any web tasks involving it

---

## 🖥️ 環境と会話履歴の保存先

Sho は複数のデバイスから Claude Code を使う（PC A / PC B / Mobile App）。repo は 1 つ（`sho-cominc/cominc-hq`）だが、**会話履歴がどこに保存されるかは環境ごとに違う**。混乱したらここを見ること。

| 環境 | 会話履歴の保存先 | 他デバイスと共有 |
|---|---|---|
| **claude.ai/code（ブラウザ / Web / モバイルアプリ）** | Anthropic アカウント側にクラウド保存 | ✅ 同じアカウントでログインした全デバイスで共有される。**これが推奨** |
| **ローカル `claude` CLI** | `~/.claude/projects/<hash>/*.jsonl`（そのマシンのみ） | ❌ 他デバイスからは見えない。新規セッションはここで始めないこと |
| **Git リポジトリ** | コード本体の変更 + `project-memory/` のマークダウン | ✅ 全デバイスで共有。ただし会話の jsonl は repo には入らない |

**運用ルール**：
- 新しい作業を始めるときは、どの PC からでも **ブラウザで `claude.ai/code` を開く**（ローカル CLI は使わない）
- エージェントの成果物（試算・下書き・振り返り）は `project-memory/` に日付つきで残す。確定した事実はメモリに書く（`project-memory/README.md` 参照）
- 日々の会話ログを自動で commit するような仕掛けは入れていない（Notion の「Sho's Notes」と役割が重複するため）

---

Good luck. The plan is solid. 🏔️
