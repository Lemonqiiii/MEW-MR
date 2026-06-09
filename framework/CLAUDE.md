# Medical Review Framework

## First Run? Start Here
1. **Verify setup**: `python3 scripts/smoke_test.py` — confirms everything works
2. **Pick a topic**: Edit `config.yaml` → `project.topic` (or `cp config.demo.yaml config.yaml` for a demo)
3. **Say `1`** to begin literature search — the pipeline guides you from there

**Demo mode**: `cp config.demo.yaml config.yaml` gives you a pre-configured Vitamin D topic. You can start immediately and see the full pipeline in action before committing to your own topic.

## Startup
1. Read `config.yaml` — all project-specific settings
2. Read `state.json` — current phase and progress
3. Read `claude/gates/gates.md` — gate definitions
4. Output: current phase, progress %, next available action
5. If topic is unset → prompt user to edit config.yaml or use config.demo.yaml

## Agent Dispatch

| Trigger | Agent | Pre-Gate | Post-Gate |
|---------|-------|----------|-----------|
| `1` `search` `搜索` | claude/agents/1-search.md | — | Gate 1, 7 |
| `2` `screen` `筛选` | claude/agents/6-screening.md | Gate 1 | Gate 2 |
| `3` `analyze` `分析` | claude/agents/2-analysis.md | Gate 2 | Gate 3 |
| `4` `write` `写作` | claude/agents/3-writing.md | Gate 3 | Gate 4, 8 |
| `8` `synthesis` `合成` | claude/agents/7-synthesis.md | Gate 4 | Gate 9 |
| `5` `review` `审校` | claude/agents/4-review.md | Gate 9 | Gate 10 |
| `9` `submit` `投稿` | claude/agents/8-submission.md | Gate 10 | Gate 11 |
| `6` `commit` `编码` | claude/agents/0-coder.md | — | — |
| `7` `evaluate` `评估` | claude/agents/5-evaluation.md | — | — |
| `审稿` `peer-review` `外审` | claude/agents/peer-review.md | — | — |
| `sr` `systematic` `系统综述` | claude/agents/sr-systematic-review.md | — | PRISMA |

**Review type modes**:
- `narrative` (default): standard pipeline — flexible, thematic synthesis
- `systematic`: PRISMA-compliant — dual screening, RoB, GRADE, meta-analysis if appropriate
- Set via `config.yaml` → `review_type`

**Standalone mode**: `peer-review` auto-detects manuscript type (original research / narrative review / systematic review / meta-analysis) and applies appropriate review dimensions — including PRISMA 2020 compliance, search strategy audit, RoB verification, GRADE assessment, and protocol fidelity for SR/MA manuscripts.

## Core Rules
1. All manuscript content: single source file in `config.yaml` → `paths.manuscript_src`
2. Every claim must have at least one citation with PMID or DOI
3. Writing in English; internal project communication in the language of `config.yaml`
4. Before each agent: `python3 scripts/verify_gates.py --check-prereq <agent_id>`
5. After each agent: `python3 scripts/verify_gates.py --check-output <agent_id>`
6. Critical decisions → record to `state.json` via `python3 scripts/state.py`

## Quality System
- **Gate definitions**: `claude/gates/gates.md` (Gates 1-11)
- **Gate enforcement**: `python3 scripts/verify_gates.py --gate <N>` (exit code 0 = pass)
- **Writing disciplines**: `claude/disciplines/` — citation-scope, language-naturalness, manuscript-integrity
- **Error patterns**: `claude/disciplines/error-patterns.md` — known failure modes and fixes
- **Revision workflow**: `docs/REVISION_WORKFLOW.md` — importing audit `review-actions.json` and tracking fixes

## Configuration
All project-specific settings in `config.yaml`:
- Topic, domain, review type, target journal
- File paths (manuscript source, figures, data)
- Agent settings (paper type system, exclusion keywords, journal profile)

## State
All progress tracking in `state.json`:
- `project.phase` — current phase
- `project.progress_pct` — overall completion %
- `metrics.*` — paper counts, word counts, reference counts
- `gates.*` — per-gate status and last run timestamp

## Session Flow
1. Startup → display phase + progress + options
2. User triggers agent → verify pre-gate → execute agent → verify post-gate
3. Agent encounters ambiguity → escalate with options (A/B + recommendation)
4. Phase complete → prompt user to run `commit` (Agent 0)
5. Every 2-3 sub-tasks → suggest lightweight `commit`

## Agent Loading
Agents are loaded on demand from `claude/agents/<id>-<name>.md`.
Each agent file follows a uniform format:
- **Metadata**: id, triggers, pre_gate, post_gate, input/output schema
- **Steps**: numbered workflow, each marked MANDATORY / OPTIONAL / CONDITIONAL
- **Handoff Schema**: JSON schema for structured data passing to next agent
