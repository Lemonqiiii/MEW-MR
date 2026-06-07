# Quick-Start Guide

This guide gets you from zero to a working review-writing pipeline in ~5 minutes.

## Prerequisites

- **Python 3.10+** — `python3 --version`
- **Claude Code** — the CLI tool from Anthropic (`claude --version`)
- **pip** — `pip3 --version`

## Setup (First Time)

```bash
# 1. Install Python dependencies
pip install -r scripts/requirements.txt

# 2. Edit config.yaml — set your topic, domain, and target journal
#    Open config.yaml in any editor:
#      - project.topic: "Your Review Topic"
#      - project.domain: "your, keywords"
#      - project.target_journal: "Target Journal"
#    See config.example.yaml for all options.

# 3. Start Claude Code
claude
```

## First Session

When Claude Code starts, it will:
1. Read your config.yaml and state.json
2. Show: current phase, progress %, available actions
3. Wait for your command

**Say `1` or `search` to begin the literature search.**

## Agent Pipeline

```
Search(1) → Screen(2) → Analyze(3) → Write(4) → Synthesis(8) → Review(5) → Submit(9)
```

| Say | What Happens |
|-----|-------------|
| `1` / `search` | Literature search — PubMed, Semantic Scholar, Europe PMC |
| `2` / `screen` | Screen results — apply inclusion/exclusion, classify paper types |
| `3` / `analyze` | Deep reading — structured note-taking for included papers |
| `4` / `write` | Draft manuscript — generate Word (.docx) from markdown |
| `8` / `synthesis` | Cross-intervention synthesis — generate figures and hypotheses |
| `5` / `review` | Self-review — fact-check, language scan, citation compliance |
| `9` / `submit` | Submission prep — cleanup, format, compliance checks |
| `6` / `commit` | Save progress — git commit with structured message |

## Quality Gates

11 automated gates protect the pipeline. Before and after each agent, Claude runs:

```bash
python3 scripts/verify_gates.py --check-prereq <agent_id>
python3 scripts/verify_gates.py --check-output <agent_id>
```

Run all gates manually at any time:

```bash
python3 scripts/verify_gates.py --all
```

## Useful Scripts

```bash
# Check manuscript structure before generating Word
python3 scripts/audit_manuscript.py manuscript/submission.md

# Generate Word document
python3 scripts/gen_word.py

# Check current project state
python3 scripts/state.py get project

# List all gates
python3 scripts/verify_gates.py --list

# Generate peer review template (for external review)
python3 scripts/peer_review.py manuscript/submission.md
```

## Project Structure

```
├── config.yaml           # YOUR settings — edit this first
├── state.json            # Progress tracking (auto-updated)
├── CLAUDE.md             # Orchestrator (loaded by Claude Code)
├── claude/
│   ├── agents/           # 9 specialized agent definitions
│   ├── disciplines/      # Writing rules and error patterns
│   └── gates/            # Gate definitions (Gates 1-11)
├── scripts/              # Python verification + generation tools
├── manuscript/           # Your manuscript lives here
├── data/                 # Search results and screening data
└── docs/                 # Papers, methods, figures
```

## Need Help?

### Common Issues

| Problem | Solution |
|---------|----------|
| "WebFetch blocked" during search | Use WebSearch or Semantic Scholar API as fallback — Agent 1 will suggest alternatives |
| All 11 gates show FAIL | **This is normal!** Gates check for artifacts that don't exist yet. Run Agent 1 first, then gates will pass one by one. |
| `gen_word.py` says "file not found" | You need a manuscript first. Complete Agents 1→2→3, or create a test file at `manuscript/submission.md` |
| `audit_manuscript.py` crashes | Pass a manuscript path: `python3 scripts/audit_manuscript.py manuscript/submission.md` |
| "No module named yaml" | `pip install -r scripts/requirements.txt` |
| Topic not configured warning | `cp config.demo.yaml config.yaml` for a demo topic, or edit config.yaml |

### Full Documentation

- **Why this exists**: [WHY.md](WHY.md) — motivation and capabilities
- **Full workflow**: [docs/WORKFLOW.md](docs/WORKFLOW.md) — phase-by-phase walkthrough
- **All config options**: [docs/CONFIG.md](docs/CONFIG.md) — every config.yaml setting
- **Agent definitions**: `claude/agents/` — each agent's steps and handoff schema

### Still Stuck?

1. Run `python3 scripts/smoke_test.py` to verify your setup
2. Check the demo config: `config.demo.yaml` has a working example
3. Open an issue on GitHub
