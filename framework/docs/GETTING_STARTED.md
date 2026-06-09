# Getting Started (5 Minutes)

## Prerequisites
- Python 3.10+
- Claude Code (or any LLM-powered coding assistant)
- Git

## Step 1: Install

```bash
git clone <your-repo-url> medical-review
cd medical-review
pip install -r scripts/requirements.txt
```

## Step 2: Configure

Edit `config.yaml`:

```yaml
project:
  topic: "Your Review Topic"
  domain: "your-field"
  review_type: "narrative"     # narrative | systematic | meta-analysis
  target_journal: "Target Journal Name"
```

That's it. All paths are relative to the project root — no hardcoded paths to fix.

## Step 3: Start Your First Review

Open Claude Code in the project directory:

```
claude
```

The framework auto-loads and presents your current state. Say `1` or `search` to begin literature search.

## The Agent Flow

```
1 (search) → 2 (screen) → 3 (analyze) → 4 (write) → 8 (synthesis) → 5 (review) → 9 (submit)
```

At each step:
- **Before** an agent runs, its pre-gate is verified automatically
- **After** an agent completes, its post-gate is checked
- Say `6` (commit) to save progress

## Understanding the Structure

```
├── config.yaml              # YOUR settings — edit this
├── state.json               # Progress tracking — auto-managed
├── claude/
│   ├── CLAUDE.md            # Orchestrator (auto-loaded each session)
│   ├── agents/              # 11 agent definition files
│   ├── disciplines/         # Writing rules and error patterns
│   ├── gates/               # Quality gate definitions
│   └── prompts/             # Review enhancement prompts
├── scripts/                 # Python tools (all read from config.yaml)
├── templates/               # Domain templates and paper classification systems
└── docs/                    # This documentation
```

## Next Steps
- Read `WORKFLOW.md` for the full workflow
- Read `CONFIG.md` for all configuration options
- Check `example/` for a sample project setup
