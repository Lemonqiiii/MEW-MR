# Agent Dispatch Reference

This file is a compact dispatch reference for files under `claude/`. The main Claude Code entry point is `../CLAUDE.md` (`framework/CLAUDE.md`). If the two files conflict, follow `../CLAUDE.md`.

## Agent Dispatch

| Trigger | Agent | Pre-Gate | Post-Gate |
|---------|-------|----------|-----------|
| `1` `search` `搜索` | `claude/agents/1-search.md` | — | Gate 1, 7 |
| `2` `screen` `筛选` | `claude/agents/6-screening.md` | Gate 1 | Gate 2 |
| `3` `analyze` `分析` | `claude/agents/2-analysis.md` | Gate 2 | Gate 3 |
| `4` `write` `写作` | `claude/agents/3-writing.md` | Gate 3 | Gate 4, 8 |
| `8` `synthesis` `合成` | `claude/agents/7-synthesis.md` | Gate 4 | Gate 9 |
| `5` `review` `审校` | `claude/agents/4-review.md` | Gate 9 | Gate 10 |
| `9` `submit` `投稿` | `claude/agents/8-submission.md` | Gate 10 | Gate 11 |
| `6` `commit` `编码` | `claude/agents/0-coder.md` | — | — |
| `7` `evaluate` `评估` | `claude/agents/5-evaluation.md` | — | — |
| `审稿` `peer-review` `外审` | `claude/agents/peer-review.md` | — | — |
| `sr` `systematic` `系统综述` | `claude/agents/sr-systematic-review.md` | — | PRISMA |

## Review Type Modes

- `narrative`: standard flexible pipeline.
- `systematic`: PRISMA-compliant workflow with dual screening, RoB, GRADE, and meta-analysis checks where appropriate.
- `meta-analysis`: systematic-review workflow plus quantitative synthesis planning.

Set the mode in `config.yaml` under `project.review_type`.

## Loading Rules

- Load agents on demand from `claude/agents/<id>-<name>.md`.
- Before each agent, run or respect `python3 scripts/verify_gates.py --check-prereq <agent_id>`.
- After each agent, run or respect `python3 scripts/verify_gates.py --check-output <agent_id>`.
- For revision imports from the audit project, see `docs/REVISION_WORKFLOW.md`.
