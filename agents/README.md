# Agent Definitions (backup)

This folder is a **git backup** of the 12 Claude Code subagent definitions (`~/.claude/agents/*.md`).

The definitions are **generic**: they work on any project. ComInc.-specific rules live in **`../playbook/`**. Generic agents find it through the root `CLAUDE.md` of the Arai Supabase folder.

## What is the source of truth

| Location | Role |
|---|---|
| `~/.claude/agents/*.md` (`C:\Users\shota\.claude\agents\`) | **Source of truth.** The only copy Claude Code reads. Edit here. |
| `cominc-agents/agents/*.md` (this folder) | Backup of the above (git history, restore on a new PC). **Don't edit here.** |
| `cominc-agents/playbook/*.md` | ComInc.-specific rules per role (premises, banned wording, checklists, brand, where facts live). |
| `cominc-agents/src/prompts/*.md` | Something else: the prompts the Python agent system (`run.py`) reads. |

Neither the definitions nor the playbook hold moving facts (prices, status, dates, stack versions). Those live in Claude Code memory or Notion.

The second half of each definition is shared by all 12 files: "Before you start", "Handling facts", "Report format" and "Team & collaboration rules". Keep it identical across all 12.

Changes go through Hana's retrospective procedure (`hana.md`):
- general ways of working → the definitions
- ComInc.-specific rules → the playbook
- facts → memory

## Agents (12)
- `ottar` orchestrator
- `hana` secretary, fact-check, retrospectives
- `fin` finance
- `law` legal
- `webber` web director
- `clare` creative
- `yuri` UX/UI
- `dev` developer
- `cat` marketing
- `prod` content producer
- `kai` local guide
- `min` lodging operations

## Sync: local → GitHub (after editing `~/.claude/agents`)

```bash
cd "C:/Users/shota/Arai Supabase/cominc-agents"
cp /c/Users/shota/.claude/agents/*.md agents/
# backup matches (no output = OK)
for f in agents/*.md; do b=$(basename "$f"); [ "$b" = README.md ] || cmp -s "$f" "/c/Users/shota/.claude/agents/$b" || echo "DIFF $b"; done
# shared block identical across all 12 (exactly one line = OK; also check it is not the empty-string hash d41d8cd9...)
for f in /c/Users/shota/.claude/agents/*.md; do sed -n '/^## Before you start/,$p' "$f" | md5sum; done | sort -u
git add agents/ playbook/
git commit -m "agents: <what changed>"
# push only after Sho agrees
```

## Restore to a new machine

```bash
git clone https://github.com/sho-cominc/cominc-hq.git
cp cominc-hq/agents/*.md ~/.claude/agents/ && rm ~/.claude/agents/README.md
```
