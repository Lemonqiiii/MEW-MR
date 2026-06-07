# Agent 4: Review

## Metadata
- **id**: 4
- **type**: execution (horizontal)
- **triggers**: `5` `review` `审校` `审` `核查`
- **pre_gate**: Gate 9 (if synthesis was run)
- **post_gate**: Gate 10

## Input
- `config.yaml` → `paths.manuscript_src` — manuscript to review (single source of truth)
- `docs/papers/` — paper notes (for cross-verifying citations + paper type labels + citation scope labels)
- `state.json` — key decisions (for consistency checking)
- `claude/disciplines/` — all three discipline files
- `claude/prompts/` — review enhancement prompts

## Output Schema
```json
{
  "review_round": "R1",
  "must_fix_count": 0,
  "nice_to_have_count": 0,
  "citation_accuracy_pct": 0,
  "naturalness_score": {"passing": 0, "total": 0, "pct": 0},
  "citation_scope_violations": 0,
  "perspective_coverage_pct": 0,
  "data_translation": {"total_rr": 0, "translated": 0, "baseline_unknown": 0},
  "pattern_a_final_count": 0,
  "cochrane_analyzed": 0,
  "cochrane_qualifiers_added": 0,
  "cochrane_concentration_pct": 0
}
```

---

## Enhanced Review Passes (Module C)

Execute these before/after the main review workflow.

### Pre-Pass 1: Perspective Switching (MANDATORY)
1. Read `claude/prompts/perspective-switching.md`
2. Scan manuscript for trigger positions: after each major intervention evidence summary → P1 Clinician; neurodevelopmental outcomes → P2 Family; resource-intensive interventions → P3 LMIC
3. At each trigger: draft 2-4 sentence perspective paragraph → verify based on manuscript data → insert with `<!-- PERSPECTIVE:P[N] -->` tag
4. Report: N perspectives inserted / N trigger positions = XX% coverage

### Pre-Pass 2: Data Translation (MANDATORY)
1. Read `claude/prompts/data-translation.md`
2. Scan manuscript for all RR/HR/OR values
3. For each: extract baseline risk from cited paper → compute ARR + NNT/NNH → insert translation
4. If baseline risk unavailable → annotate `⚠️ BASELINE_RISK_UNKNOWN`
5. Report: N RR values, N translated, N baseline unknown

### Post-Pass 3: Argument Diversity (MANDATORY)
1. Read `claude/prompts/argument-diversity-enforcement.md`
2. Verify Agent 7 Step 4 results (if synthesis was run)
3. Directly detect residual Pattern A
4. For MUST FIX: force conversion or deletion
5. Check argument type distribution → flag missing types
6. Report: Pattern A final count, argument type distribution

### Post-Pass 4: Mandatory Critique (MANDATORY)
1. Read `claude/prompts/critical-absorption.md`
2. Identify Cochrane reviews cited ≥2 times
3. For each: check GRADE → CI width → trial overlap → version currency → population applicability
4. For each issue found → insert critical qualifier
5. Calculate Cochrane concentration → if >60% trigger COCHRANE_MONOCULTURE warning
6. Report: N Cochrane reviews analyzed, N critical qualifiers inserted, Cochrane concentration XX%

---

## Main Review Steps

### Step 1: Fact Checking (MANDATORY)
Verify each citation accurately reflects the original paper. Cross-check against paper notes.

### Step 1.5: Absolute Negative Claim Detection (MANDATORY)
1. Scan manuscript for all absolute negative claims ("no data", "absent", "zero", "never been studied", etc.)
2. Two-phase verification:
   - **Phase A**: Check cited literature — does the cited paper actually support the "no data" claim?
   - **Phase B**: Reverse-check — search the full reference pool for evidence contradicting the negative claim
3. Flag MUST FIX contradictions (claim says "no data" but cited paper contains relevant data)
4. Rules in `claude/prompts/negative-claim-detection.md`

### Step 2: Logic Review (MANDATORY)
Check paragraph transitions, argument chain completeness.

### Step 3: Language Polish (MANDATORY)
Grammar, spelling, academic expression norms.

### Step 4: Citation Completeness (MANDATORY)
Every claim has literature support.

### Step 5: Consistency Check (MANDATORY)
Terminology usage, abbreviation definitions, number formatting.

### Step 6: Naturalness Scan (MANDATORY)
Apply all 6 anti-patterns from `claude/disciplines/language-naturalness.md`. Calculate paragraph pass rate.

### Step 7: Citation Scope Compliance (MANDATORY)
Verify against `claude/disciplines/citation-scope.md`:
- Mechanism claims use types A/B/C as primary?
- Any type G (review) used as primary citation?
- Any type I (case report) solely supporting a general claim?
- Any type E (bioinformatics) used for causal mechanism claims?
- Violations → MUST FIX

### Step 8: Output Review Report (MANDATORY)

**Report format**:
```markdown
## Review Report — [Section] — YYYY-MM-DD

### Must Fix
| # | Location | Issue Type | Description | Suggested Fix |
|---|----------|-----------|-------------|---------------|

### Nice to Have
| # | Location | Improvement | Suggestion |
|---|----------|------------|------------|

### Statistics
- Total issues: X
- Must Fix: X
- Nice to Have: X
- Citation accuracy: X%
- Naturalness: X/X paragraphs pass (XX%) — target ≥80%
- Citation scope compliance: X violations (MUST FIX)
- Perspective switching: N/N trigger positions (XX%) — target ≥80%
- Data translation: N RR values, N translated to ARR/NNT, N baseline unknown
- Argument diversity: Pattern A final count: N — target ≤2
- Mandatory critique: N Cochrane analyzed, N qualifiers inserted, concentration: XX%
```

**Gate 10 post-condition**: `python3 scripts/verify_gates.py --gate 10` must pass.
