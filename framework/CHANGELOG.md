# Changelog

## v1.0.0 (2026-06-07)

### Framework Architecture
- CLAUDE.md split from 497 lines (26KB) to 62 lines — thin orchestrator pattern
- 9 agent definitions as independent files (67-177 lines each)
- 3 writing discipline files: citation-scope, language-naturalness, manuscript-integrity
- Centralized error pattern library

### Configuration
- Single `config.yaml` — no hardcoded paths in any script
- `config.example.yaml` for new users
- All 9 Python scripts read from config_loader

### Quality System
- 11 executable gates via `scripts/verify_gates.py`
- CLI: `--all`, `--gate N`, `--phase`, `--check-prereq`, `--check-output`
- Gate status tracked in `state.json`

### State Management
- `state.json` replaces `memory/` directory
- `scripts/state.py` with `get`, `set`, `gate` commands
- Structured JSON with project phase, metrics, gate status, decisions

### Domain Templates
- A-J paper classification system as standalone template
- 9 domain templates (ontology, paper notes, evidence grading, etc.)
- 5 review enhancement prompts

### Documentation
- GETTING_STARTED.md (5-minute onboarding)
- WORKFLOW.md (full phase-by-phase guide)
- CONFIG.md (all configuration options)
- Clean README with structure overview

### Distribution
- MIT License
- setup.sh for one-command initialization
- requirements.txt with all Python dependencies
- .gitignore excluding run records, pycache, OS files
