# Full Workflow Guide

## Phase Overview

```
Planning → Literature Search → Screening → Deep Reading → Writing → Synthesis → Review → Submission
```

Each phase has entry gates (must pass before entering) and exit gates (must pass before moving on).

## Phase 1: Planning

**Goal**: Define review topic, PICO framework, target journal.

**Actions**:
1. Edit `state.json` → `active_focus` with your PICO
2. Edit `config.yaml` → `project` with topic and target journal
3. Say `commit` to save

**Output**: Configured project ready for search.

---

## Phase 2: Literature Search (Agent 1)

**Trigger**: `1` or `search`

**What it does**:
1. Database assessment (PubMed, Semantic Scholar, Europe PMC + optional Embase/Cochrane/CNKI)
2. Tier 1 automated search
3. Generates Tier 2 manual search checklist (for VPN databases)
4. Five-layer comprehensiveness validation
5. Full-text access triage
6. Domain ontology construction (Gate 7)

**Post-gate**: Gate 1 (search quality), Gate 7 (domain ontology)

**Key files**:
- `data/pubmed_search_results.json` — search output
- `knowledge/domain-ontology.md` — intervention inventory
- `docs/search-results/handoff.md` — structured handoff to screening

---

## Phase 3: Screening (Agent 6)

**Trigger**: `2` or `screen`

**What it does**:
1. Round 0: Paper type classification (A-J)
2. Round 1: Title/abstract screening (PICO + type conditions)
3. Round 2: Full-text screening + citation scope assignment
4. Type distribution health checks

**Pre-gate**: Gate 1
**Post-gate**: Gate 2

**Key files**:
- `data/screening_final_included.json` — final inclusion list with type labels
- `data/screening_excluded.json` — excluded papers with reasons

---

## Phase 4: Deep Reading (Agent 2)

**Trigger**: `3` or `analyze`

**What it does**:
1. Fetches paper metadata and full text
2. Confirms paper type from screening handoff
3. Structured extraction following `templates/paper-note.md`
4. Writes notes to `docs/papers/`

**Pre-gate**: Gate 2
**Post-gate**: Gate 3

---

## Phase 5: Writing (Agent 3)

**Trigger**: `4` or `write`

**What it does**:
1. Pre-writing planning (Steps 0a-0f): priority-weighted allocation, gap-to-emphasis mapping, time annotation
2. Loads writing brief and paper notes
3. Writes sections following citation scope rules and language naturalness discipline
4. Runs `gen_word.py` to generate formatted output
5. Self-checks Gates 4, 5, 6

**Pre-gate**: Gate 3
**Post-gate**: Gate 4, Gate 8

**Key files**:
- `manuscript/submission.md` — single source of truth (markdown)
- `manuscript/output.docx` — formatted Word output
- `knowledge/pre-writing-plan.md` — writing brief

---

## Phase 6: Synthesis (Agent 7)

**Trigger**: `8` or `synthesis`

**What it does**:
1. Cross-intervention comparison matrix
2. Interaction analysis and hypothesis generation
3. Clinical decision framework generation
4. Argument diversity scan (Pattern A detection)
5. Time evolution annotation
6. Coverage completeness verification

**Pre-gate**: Gate 4
**Post-gate**: Gate 9

---

## Phase 7: Review (Agent 4)

**Trigger**: `5` or `review`

**What it does**:
1. Enhanced passes: perspective switching, data translation (RR→NNT)
2. Fact checking, logic review, language polish
3. Naturalness scan (6 anti-patterns)
4. Citation scope compliance
5. Post-passes: argument diversity verification, Cochrane critique

**Pre-gate**: Gate 9 (if synthesis was run)
**Post-gate**: Gate 10

---

## Phase 8: Submission (Agent 8)

**Trigger**: `9` or `submit`

**What it does**:
1. Cleanup: strip HTML audit tags, detect placeholders
2. Transform: coverage gaps → scope limitations, synthesis → submission content
3. Compliance: journal match, format compliance, AI disclosure
4. Generate submission readiness report

**Pre-gate**: Gate 10
**Post-gate**: Gate 11

---

## Quality System

### Gate Enforcement

```bash
# Check if an agent can run
python3 scripts/verify_gates.py --check-prereq 3

# Verify an agent's output
python3 scripts/verify_gates.py --check-output 3

# Run a specific gate
python3 scripts/verify_gates.py --gate 4

# Run all gates
python3 scripts/verify_gates.py --all
```

### Writing Disciplines
- **Citation scope**: `claude/disciplines/citation-scope.md`
- **Language naturalness**: `claude/disciplines/language-naturalness.md`
- **Manuscript integrity**: `claude/disciplines/manuscript-integrity.md`
- **Error patterns**: `claude/disciplines/error-patterns.md`

### State Management

```bash
# View current state
python3 scripts/state.py

# Update progress
python3 scripts/state.py set project.phase "writing"
python3 scripts/state.py set metrics.words_written 5000

# Mark gate status
python3 scripts/state.py gate 4 pass
```
