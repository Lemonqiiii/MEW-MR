# Agent 0: Coder (Infrastructure)

## Metadata
- **id**: 0
- **type**: infrastructure
- **triggers**: `6` `commit` `编码` `快记` `记`
- **modes**: lightweight (`快记`), full (`编码`)
- **pre_gate**: none
- **post_gate**: none

## Input
- Git status (current changes)
- `state.json` — current progress data
- `config.yaml` — project configuration

## Output Schema
```json
{
  "mode": "lightweight | full",
  "updated_tasks": ["task_id"],
  "new_phase": "phase_name or null",
  "commit_hash": "abc123",
  "commit_message": "[phase] description"
}
```

---

## Lightweight Mode (`快记`)

### Trigger
- User says `快记`, `记`, `quick`
- Agent proactively suggests after 2-3 sub-tasks completed

### Steps

#### Step 1: Check Git Status (MANDATORY)
Check current git changes.

#### Step 2: Update Task List (MANDATORY)
1. Read existing task list
2. Mark completed tasks as done
3. If new sub-tasks discovered, add them

#### Step 3: Update State (MANDATORY)
```bash
python3 scripts/state.py set project.progress_pct <value>
python3 scripts/state.py set project.last_updated "<timestamp>"
python3 scripts/state.py set metrics.words_written <value>
```

#### Step 4: Append Session Log (MANDATORY)
Append one line to session log with: date + completed items + next steps + blockers.

#### Step 5: Git Commit (MANDATORY)
```bash
git add -A
git commit -m "[phase] brief description of changes"
```

### Skipped in Lightweight Mode
- Efficiency data collection (full mode only)
- Security audit (full mode only)
- Milestone updates (full mode only)

---

## Full Mode (`编码`)

### Trigger
- User says `编码`, `6`, `commit`
- Agent proactively suggests at Phase completion

### Steps (includes all lightweight steps plus:)

#### Step F1: Milestone Update (MANDATORY)
Mark current phase milestone as complete with date.

#### Step F2: Efficiency Data Collection (MANDATORY)
Extract from session: wall time, tool call counts, token usage → write to metrics file.

#### Step F3: Security Audit (MANDATORY)
1. Scan session operations against `claude/disciplines/error-patterns.md`
2. Flag any violations
3. Write audit results

#### Step F4: Full Git Commit (MANDATORY)
Include all metrics and audit results in structured commit message.

### Output
- Table summarizing what was updated
- Efficiency metrics summary
- Security audit summary (if violations)
- Suggested next task
