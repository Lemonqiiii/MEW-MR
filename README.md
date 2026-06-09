# MEW-MR: Medical Writing & Medical Review

> **👉 First time here?** Go straight to **[GETTING_STARTED.md](GETTING_STARTED.md)** — a step-by-step guide from download to working output.
>
> **⚡ One-liner (paste into terminal or Claude Code):**
> ```bash
> git clone https://github.com/Lemonqiiii/MEW-MR.git && cd MEW-MR/framework && pip install -q -r scripts/requirements.txt && python3 scripts/smoke_test.py && cp config.demo.yaml config.yaml && echo "Done. Run: claude"
> ```

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
│  9 pipeline agents  │     │  6 reviewers + V/M/F │
│  11 quality gates   │     │  Cross-reviewer      │
│  Word generation    │     │  convergence         │
└─────────────────────┘     └─────────────────────┘
```

## What's Inside

| Directory | What | Start Here |
|-----------|------|------------|
| `framework/` | Review-writing pipeline | [WHY.md](framework/WHY.md) · [QUICKSTART.md](framework/QUICKSTART.md) |
| `audit/` | Independent peer-review system | [WHY.md](audit/WHY.md) · [README.md](audit/README.md) |
| `docs/` | Platform and tool adapters | [ADAPTERS.md](docs/ADAPTERS.md) |

## How They Work Together

1. **Write** — Use `framework/` to search literature, screen papers, draft a manuscript
2. **Audit** — Place the manuscript in `audit/review-pipeline/input/`, run the 6-dimension review
3. **Revise** — Apply the structured feedback (`review-actions.json`) back in `framework/`
4. **Repeat** — Re-audit until all gates pass

The two projects operate independently — they share only a manuscript file and a review report. This deliberate separation ensures the reviewer isn't blind to what the writer missed.

## Quick Start

For a full walkthrough, use [GETTING_STARTED.md](GETTING_STARTED.md). The shortest local demo path is:

```bash
cd framework
pip install -r scripts/requirements.txt
python3 scripts/smoke_test.py          # verify setup
cp config.demo.yaml config.yaml        # Demo topic: Vitamin D & respiratory infections
claude                                 # Say "1" to test the full pipeline
```

Windows PowerShell:

```powershell
cd framework
pip install -r scripts/requirements.txt
python scripts/smoke_test.py
Copy-Item config.demo.yaml config.yaml
claude
```

Audit demo:

```bash
cd audit
python3 scripts/check-structure.py review-pipeline/input/DEMO-MANUSCRIPT.md
python3 scripts/verify-citations.py review-pipeline/input/DEMO-MANUSCRIPT.md
```

## Requirements

- Python 3.10+
- Claude Code for the full agent workflow
- `pip install -r framework/scripts/requirements.txt` (audit uses stdlib only)

Python scripts can still be used without Claude Code. See [docs/ADAPTERS.md](docs/ADAPTERS.md) for Claude Code, other LLM coding agents, Windows PowerShell, and scripts-only usage.

## Safety Note

MEW-MR is an AI-assisted writing and review framework. It does not replace author responsibility, clinician review, statistician review, journal requirements, or primary-source verification. Medical claims, effect estimates, and citations must be checked by qualified humans before submission or clinical use.

## License

MIT — see [framework/LICENSE](framework/LICENSE) and [audit/LICENSE](audit/LICENSE)
