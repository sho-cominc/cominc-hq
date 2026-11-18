# Agent definitions — where they live and how to sync

The 12 subagent definitions exist in two places with **identical content**:

| Location | Who reads it |
|---|---|
| `~/.claude/agents/*.md` (`C:\Users\shota\.claude\agents\`) | Local Claude Code on Sho's PC, in every folder. **Edit here.** |
| `cominc-agents/.claude/agents/*.md` (this repo) | **Cloud sessions** (claude.ai/code) on the `sho-cominc/cominc-hq` repo, which load agents from the repo's `.claude/agents/`. Also serves as the git backup. **Don't edit here; copy from the local folder.** |

Related:
- `cominc-agents/playbook/` — ComInc.-specific rules per role
- `cominc-agents/src/prompts/*.md` — something else: the prompts the Python agent system (`run.py`) reads

Each definition = role body + shared blocks ("Before you start", "Handling facts", "Report format", "会社の方針（ComInc.）", "Team & collaboration rules"). The shared blocks must be identical in all 12. Changes go through Hana's retrospective procedure: ways of working → definitions, ComInc.-specific rules → playbook, facts → memory.

## Sync after editing `~/.claude/agents`

```bash
cd "C:/Users/shota/Arai Supabase/cominc-agents"
cp /c/Users/shota/.claude/agents/*.md .claude/agents/
# copies match (no output = OK)
for f in .claude/agents/*.md; do cmp -s "$f" "/c/Users/shota/.claude/agents/$(basename "$f")" || echo "DIFF $f"; done
# shared block identical across all 12 (exactly one line, not the empty hash d41d8cd9...)
for f in .claude/agents/*.md; do sed -n '/^## Before you start/,$p' "$f" | md5sum; done | sort -u
git add .claude/agents/ playbook/
git commit -m "agents: <what changed>"
git push   # cloud sessions only see what is pushed
```

## Restore on a new PC

```bash
git clone https://github.com/sho-cominc/cominc-hq.git
mkdir -p ~/.claude/agents && cp cominc-hq/.claude/agents/*.md ~/.claude/agents/
```
