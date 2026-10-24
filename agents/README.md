# ComInc. Agent Definitions (backup)

This folder is a **git backup** of the Claude Code subagent definitions for ComInc.'s 12-member AI team.

## どれが正か

| 場所 | 役割 |
|---|---|
| `~/.claude/agents/*.md`（`C:\Users\shota\.claude\agents\`） | **正。** Claude Code が実際に読むのはここだけ。編集はここで行う |
| `cominc-agents/agents/*.md`（このフォルダ） | 上のバックアップ（git で履歴を残す・新しい PC に戻すため）。**直接編集しない** |
| `cominc-agents/src/prompts/*.md` | 別物。Python のエージェントシステム（`run.py`）が読むプロンプト |

定義ファイルには**役割と進め方だけ**を書く。料金・申請状況・日付・スタックなどの動く情報はメモリ（`~/.claude/projects/C--Users-shota-Arai-Supabase/memory/`）か Notion に書き、定義からはそこを読ませる。各ファイルの後半（「作業前に必ず読むもの」「事実の扱い」「報告の書式」「協働ルール」）は12名共通で、変えるときは全員を同じ内容にする。定義の見直しは Hana の振り返り手順で行う（`hana.md` 参照）。

## Agents (12)

### CEO Orchestration
- `ottar.md` — CEO Orchestrator, routes multi-specialist tasks

### Admin
- `hana.md` — Secretary, Notion, fact-check & review, retrospectives
- `fin.md` — Finance, P&L, pricing break-even, tax, subsidies & loan
- `law.md` — Legal & compliance, 民泊法, 旅行業法, 景表法, contracts

### Web Production
- `webber.md` — Web Director, architecture, technical review
- `clare.md` — Creative Designer, brand visuals, photos
- `yuri.md` — UX/UI Designer, IA
- `dev.md` — Web Developer, Astro + Cloudflare

### Marketing
- `cat.md` — Marketing, copy/SEO/SNS writing
- `prod.md` — Content Producer, pipeline & arc design

### Operations
- `kai.md` — Guide, Walk & Blend self-guided routes, local knowledge
- `min.md` — Minpaku, Cominca-stay. operations & Airbnb

## Sync: local → GitHub（`~/.claude/agents` を編集したあと）

```bash
cd "C:/Users/shota/Arai Supabase/cominc-agents"
cp /c/Users/shota/.claude/agents/*.md agents/
# 一致確認（何も出なければOK）
for f in agents/*.md; do b=$(basename "$f"); [ "$b" = README.md ] || cmp -s "$f" "/c/Users/shota/.claude/agents/$b" || echo "DIFF $b"; done
# 共通ブロックが12名で同じか（1行だけ出ればOK）
for f in /c/Users/shota/.claude/agents/*.md; do sed -n '/^## 作業前に必ず読むもの/,$p' "$f" | md5sum; done | sort -u
git add agents/
git commit -m "agents: <what changed>"
# push は Sho の了承後
```

## Restore to a new machine

```bash
git clone https://github.com/sho-cominc/cominc-hq.git
cd cominc-hq
cp agents/*.md ~/.claude/agents/
rm ~/.claude/agents/README.md
```
