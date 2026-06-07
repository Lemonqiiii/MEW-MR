# Agent 5: Quality Evaluation

## Metadata
- **id**: 5
- **type**: infrastructure (vertical)
- **triggers**: `7` `evaluate` `评估` `评`
- **pre_gate**: none (can run independently)
- **post_gate**: none

## Input
- `state.json` — metrics collected by Agent 0
- `git diff` / `git log` — current Phase changes
- `claude/gates/gates.md` — gate definitions and pass criteria
- `claude/disciplines/error-patterns.md` — known error patterns

## Output Schema
```json
{
  "phase": "phase_name",
  "composite_score": 85.5,
  "dimensions": {
    "success_rate": {"score": 90, "weight": 0.35},
    "efficiency": {"score": 75, "weight": 0.10},
    "robustness": {"score": 80, "weight": 0.20},
    "safety": {"score": 95, "weight": 0.15},
    "consistency": {"score": 85, "weight": 0.20}
  },
  "improvement_items": ["item1", "item2"],
  "report_path": "harness/reports/phase-N-report.md"
}
```

---

## Steps

### Step 1: L2 Success Rate Assessment (MANDATORY)
1. Read collected metrics
2. For each L1_PASS task, call **Agent 4** to score output on L2 business quality (1-5 scale)
3. Combine L1 + L2 for final success rate

### Step 2: Efficiency Analysis (MANDATORY)
1. Read efficiency metrics (wall time, tool calls, tokens)
2. Compare against historical baselines
3. Flag items deviating >2σ from baseline
4. Flag monotonically worsening trends

### Step 3: Robustness Testing (CONDITIONAL — Phase end)
1. Select test scenarios for current Phase (L1-L5, 1-2 each)
2. For each scenario: construct task, send to target agent, observe behavior
3. Score behavioral patterns: ✅ / ⚠️ / ❌
4. Record results: `harness/reports/robustness-phase-N.md`

### Step 4: Safety Review (MANDATORY)
1. Read safety audit data
2. Investigate MEDIUM severity items for false positives
3. Confirm and notify user on CRITICAL/HIGH
4. Generate safety trend analysis

### Step 5: Consistency Testing (CONDITIONAL — Phase end)
1. Select consistency benchmarks for current Phase
2. Run each benchmark 2× (independent agent calls)
3. Compare behavioral paths (tool call sequence edit distance)
4. Call **Agent 4** to compare semantic outputs
5. Record: `harness/reports/consistency-phase-N.md`

### Step 6: Generate Comprehensive Report (MANDATORY)
1. Aggregate five-dimension scores
2. Calculate Phase composite:
   ```
   Composite = Success×0.35 + Efficiency×0.10 + Robustness×0.20 + Safety×0.15 + Consistency×0.20
   ```
3. Write: `harness/reports/phase-N-report.md`
4. Append summary to evaluation log
5. Extract improvement items → feedback to user

### Output
- `harness/reports/phase-N-report.md` — comprehensive evaluation
- `harness/reports/robustness-phase-N.md` — robustness test details
- `harness/reports/consistency-phase-N.md` — consistency test details
- Improvement items list
