# Medical Review Framework

> **New here?** Start with [WHY.md](WHY.md) — what this does, why it's useful, and what you can build with it.

An AI-assisted framework for writing high-quality medical and biological review papers. Built on Claude Code with structured agent workflows, automated quality gates, and extensible domain templates.

## Quick Start

```bash
git clone <repo-url> medical-review
cd medical-review
pip install -r scripts/requirements.txt
# Edit config.yaml with your topic and target journal
claude
```

Say `1` or `search` to begin.

**5-minute guide**: [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md)

## How It Works

8 specialized agents collaborate through a structured pipeline:

```
Search → Screen → Analyze → Write → Synthesize → Review → Submit
```

Each agent has defined inputs, outputs, and quality gates. Gates are **enforced by executable scripts**, not honor system.

## Key Features

- **11 automated quality gates** — `python3 scripts/verify_gates.py --all`
- **Paper type classification** (A-J) with citation scope rules
- **Language naturalness scanning** (6 anti-pattern detection)
- **Domain ontology construction** with evidence gap grading (G0-G4)
- **Cross-intervention synthesis** with hypothesis generation
- **Statistical translation** (RR→ARR/NNT)
- **Configurable** — single `config.yaml`, no hardcoded paths

## Structure

```
├── config.yaml              # Project configuration
├── state.json               # Progress tracking
├── claude/
│   ├── CLAUDE.md            # Orchestrator
│   ├── agents/              # 9 agent definitions
│   ├── disciplines/         # Writing rules
│   ├── gates/               # Quality gates
│   └── prompts/             # Review enhancement prompts
├── scripts/                 # Python tools
├── templates/               # Domain templates & paper type systems
└── docs/                    # Documentation
```

## Documentation

| Document | Content |
|----------|---------|
| [Getting Started](docs/GETTING_STARTED.md) | 5-minute setup |
| [Workflow Guide](docs/WORKFLOW.md) | Full phase-by-phase walkthrough |
| [Configuration](docs/CONFIG.md) | All config.yaml options |

## Requirements

- Python 3.10+
- Claude Code (or compatible LLM coding assistant)
- `pip install -r scripts/requirements.txt`

## License

MIT — see [LICENSE](LICENSE)
