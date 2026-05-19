# ComInc. Agent Definitions

This folder contains the Claude Code subagent definitions for ComInc.'s 12-member AI team.

## What this is

These are the same files that live at `~/.claude/agents/` on Sho's machine. Backing them up here lets us:
- Restore them on a new PC by copying back to `~/.claude/agents/`
- Track changes via git history
- Share / review via PRs

## Agents (12)

### CEO Orchestration
- `ottar.md` — CEO Orchestrator, routes tasks to specialists

### Admin
- `hana.md` — Secretary, Notion single-source-of-truth, review & scoring
- `fin.md` — Finance, P&L, tax, subsidies
- `law.md` — Legal & compliance, 民泊法, contracts

### Web Production
- `webber.md` — Web Director, architecture
- `clare.md` — Creative Designer, brand visuals
- `yuri.md` — UX/UI Designer, IA
- `dev.md` — Web Developer, Astro + Cloudflare

### Marketing
- `cat.md` — Marketing, SEO/SNS writing/copy
- `prod.md` — Content Producer, pipeline & arc design

### Operations
- `kai.md` — Guide, tour planning
- `min.md` — Minpaku, kominka operations

## Restore to a new machine

```bash
# Clone this repo
git clone https://github.com/sho-cominc/cominc-hq.git
cd cominc-hq

# Copy agent definitions to Claude Code's user-global folder
cp agents/*.md ~/.claude/agents/
# (Windows) cp agents/*.md "$env:USERPROFILE/.claude/agents/"
```

## Sync from local → GitHub

Whenever you edit `~/.claude/agents/*.md`:

```bash
cd "C:/Users/shota/Arai Supabase/cominc-agents"
cp /c/Users/shota/.claude/agents/*.md agents/
git add agents/
git commit -m "agents: <what changed>"
git push
```

## Status

- **Current scope**: ComInc.-specific (古民家民泊, cominc.co, 上越市 context embedded)
- **Future refactor (Option B)**: Split into generic role definitions (user-global) + ComInc. overlays (project-scoped) so the same skills can be reused across other projects (Indian Curry, BKC, etc.)
