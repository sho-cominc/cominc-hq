# Agent definitions — the repo is the source of truth (since 2026-11-28)

The 12 subagent definitions live in **this repository**: `.claude/agents/*.md`. Edit them here, from any device, then commit and push.

| Where you work | How it gets the definitions |
|---|---|
| claude.ai/code (browser, mobile app) on `sho-cominc/cominc-hq` | Reads `.claude/agents/` from the pushed repo. Nothing to set up |
| Local `claude` CLI on a PC | `~/.claude/agents` is a **link (junction) to this folder**, so every local folder sees the same files. Run `git pull` to get changes made elsewhere |

Related:
- `playbook/` — ComInc.-specific rules per role, learning notes (`playbook/learning/`), team roster (`playbook/team-roster.md`)
- `src/prompts/*.md` — something else: the prompts the Python agent system (`run.py`) reads

Each definition = role body + shared blocks ("Before you start", "Handling facts", "Report format", "会社の方針（ComInc.）", "Team & collaboration rules"). The shared blocks must be identical in all 12. Changes go through Hana's retrospective procedure: ways of working → definitions, ComInc.-specific rules → playbook, facts → memory.

## After editing a definition

```bash
# shared block identical across all 12 (exactly one line, not the empty hash d41d8cd9...)
for f in .claude/agents/*.md; do sed -n '/^## Before you start/,$p' "$f" | md5sum; done | sort -u
git add .claude/agents/ playbook/
git commit -m "agents: <what changed>"
git push   # other devices only see what is pushed
```

## One-time setup on each Windows PC (PowerShell, no admin needed)

```powershell
$repo = "C:\Users\shota\Arai Supabase\cominc-agents"   # the local clone of sho-cominc/cominc-hq
cd $repo; git pull

# 1. If the old local folder has edits the repo lacks, find them first (no output = nothing to rescue)
Get-ChildItem "$HOME\.claude\agents\*.md" | ForEach-Object {
  $r = Join-Path "$repo\.claude\agents" $_.Name
  if (-not (Test-Path $r) -or (Get-FileHash $_).Hash -ne (Get-FileHash $r).Hash) { "DIFF $($_.Name)" }
}
# If anything prints DIFF: compare, copy what should be kept into the repo, commit and push, then continue.

# 2. Keep the old folder as a backup and replace it with a link to the repo
Rename-Item "$HOME\.claude\agents" "agents-backup-2026-11-28"
New-Item -ItemType Junction -Path "$HOME\.claude\agents" -Target "$repo\.claude\agents"

# 3. Check: should list the 12 files
Get-ChildItem "$HOME\.claude\agents"
```

On a new PC: `git clone https://github.com/sho-cominc/cominc-hq.git "C:\Users\shota\Arai Supabase\cominc-agents"`, then run step 2 (skip the rename if `~/.claude/agents` does not exist).

## Limits
- A cloud session opened on **another** repository (e.g. a client site) does not load these agents. Start ComInc. work from `cominc-hq`, or later package the agents as a plugin.
- On a PC, edits are not shared until you commit and push; changes from elsewhere arrive only after `git pull`.
