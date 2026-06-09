# Adapter Guide

MEW-MR is written for Claude Code, but most of the repository is plain Markdown plus Python scripts. This guide explains what works in each environment.

## Claude Code

This is the primary path.

```bash
cd framework
pip install -r scripts/requirements.txt
python3 scripts/smoke_test.py
cp config.demo.yaml config.yaml
claude
```

Claude Code reads `CLAUDE.md`, loads agent definitions from `claude/agents/`, and uses the gate scripts in `scripts/`.

## Windows PowerShell

Use `python` and `Copy-Item` instead of `python3` and `cp`:

```powershell
cd framework
pip install -r scripts/requirements.txt
python scripts/smoke_test.py
Copy-Item config.demo.yaml config.yaml
claude
```

If the terminal shows encoding errors, run Python with UTF-8 mode:

```powershell
python -X utf8 scripts/smoke_test.py
```

## Other LLM Coding Agents

Use the same files as instructions:

- `framework/CLAUDE.md` for the writing pipeline
- `framework/claude/agents/*.md` for individual agent behavior
- `audit/CLAUDE.md` for the independent review pipeline
- `audit/memory/agent-specializations.md` for reviewer roles and workflow

Ask the agent to read the relevant entry file first, then run the Python gate scripts before and after each phase.

## Scripts Only

Without an LLM, you can still use:

- `framework/scripts/smoke_test.py`
- `framework/scripts/verify_gates.py`
- `framework/scripts/gen_word.py`
- `audit/scripts/check-structure.py`
- `audit/scripts/gen-review-pack.py`
- `audit/scripts/verify-citations.py`

The scripts check structure, citations, gates, and Word generation. They do not independently perform literature search, screening judgment, evidence synthesis, or peer-review reasoning.
