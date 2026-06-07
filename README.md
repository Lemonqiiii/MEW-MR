# MEW-MR: Medical Writing & Medical Review

> **👉 First time here?** Go straight to **[GETTING_STARTED.md](GETTING_STARTED.md)** — a step-by-step guide from download to working output. Every command copy-pasteable.

An AI-assisted system for writing and peer-reviewing high-quality medical review papers.

```
┌─────────────────────┐     ┌─────────────────────┐
│     framework/       │     │       audit/         │
│                     │     │                      │
│  Search → Screen    │     │  6-dimension review  │
│  → Analyze → Write  │────→│  → Citation verify   │
│  → Synthesize →     │     │  → Editor synthesis  │
│  Review → Submit    │←────│  → Structured report │
│                     │     │                      │
│  9 agents           │     │  8 agents            │
│  11 quality gates   │     │  Cross-reviewer      │
│  Word generation    │     │  convergence         │
└─────────────────────┘     └─────────────────────┘
```

## What's Inside

| Directory | What | Start Here |
|-----------|------|------------|
| `framework/` | Review-writing pipeline | [WHY.md](framework/WHY.md) · [QUICKSTART.md](framework/QUICKSTART.md) |
| `audit/` | Independent peer-review system | [WHY.md](audit/WHY.md) · [README.md](audit/README.md) |

## How They Work Together

1. **Write** — Use `framework/` to search literature, screen papers, draft a manuscript
2. **Audit** — Place the manuscript in `audit/review-pipeline/input/`, run the 6-dimension review
3. **Revise** — Apply the structured feedback (`review-actions.json`) back in `framework/`
4. **Repeat** — Re-audit until all gates pass

The two projects operate independently — they share only a manuscript file and a review report. This deliberate separation ensures the reviewer isn't blind to what the writer missed.

## Quick Start

### First Time? Run This
```bash
cd framework
pip install -r scripts/requirements.txt
python3 scripts/smoke_test.py          # 34 checks — verify everything works
cp config.demo.yaml config.yaml        # Demo topic: Vitamin D & respiratory infections
claude                                 # Say "1" to test the full pipeline
```

### Framework (Writing)
```bash
cd framework
# 1. Verify setup
python3 scripts/smoke_test.py
# 2. Configure your topic (or use demo)
cp config.demo.yaml config.yaml
# 3. Start writing
claude
# Say "1" to begin literature search
```

### Audit (Reviewing)
```bash
cd audit
# Demo manuscript ships with the repo — test immediately:
python3 scripts/check-structure.py review-pipeline/input/DEMO-MANUSCRIPT.md
python3 scripts/verify-citations.py review-pipeline/input/DEMO-MANUSCRIPT.md
# Full 6-dimension review:
claude
# Say "审稿" or "peer-review"
```

## Requirements

- Python 3.10+
- Claude Code
- `pip install -r framework/scripts/requirements.txt` (audit uses stdlib only)

## License

MIT — see [framework/LICENSE](framework/LICENSE) and [audit/LICENSE](audit/LICENSE)
