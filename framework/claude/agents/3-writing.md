# Agent 3: Writing

## Metadata
- **id**: 3
- **type**: execution (horizontal)
- **triggers**: `4` `write` `写作` `写` `draft`
- **pre_gate**: Gate 3
- **post_gate**: Gate 4, Gate 8

## Input
- `manuscript/outline.md` — review outline
- Paper notes in `docs/papers/` (with paper type and citation scope labels)
- `state.json` → `active_focus` — writing direction and scope
- `knowledge/domain-ontology.md` — intervention inventory + gap grades + urgency scores + interaction map (if built)
- `knowledge/pre-writing-plan.md` — writing brief (if built)

## Output Schema
```json
{
  "section_written": "§N Title",
  "word_count_added": 500,
  "citations_used": ["PMID1", "PMID2"],
  "citation_scope_self_check": {
    "type_e_for_causal": 0,
    "type_g_as_primary": 0,
    "type_i_sole_support": 0
  },
  "gates_passed": ["Gate 4", "Gate 8"]
}
```

---

## Pre-Writing Planning (Module D)

These steps execute **before any writing begins**. They use the domain ontology to drive word allocation, gap emphasis, and evidence time annotation.

### Step 0a: Load Domain Knowledge (MANDATORY — CONDITIONAL: only if domain ontology exists)
1. Read `knowledge/domain-ontology.md`
2. Read `claude/gates/gates.md` → Gate 7 criteria
3. Read `templates/time-annotation.md` (evidence decay rules)
4. Output: "Loaded domain ontology with N interventions"

### Step 0b: Priority-Weighted Section Allocation (MANDATORY — CONDITIONAL: only if domain ontology exists)
1. For each outline section's corresponding intervention:
   - Extract Composite Urgency score from domain ontology
   - Assign Priority Tier: Deep (≥7.0) / Standard (4.0–6.9) / Brief (<4.0)
   - Calculate target word count: `target = base × (urgency / avg_urgency)`
2. **Validate**:
   - Total target ≈ manuscript word budget?
   - Any priority ≥7 intervention assigned Brief? → ❌ ERROR
   - Any priority <4 intervention assigned Deep? → ⚠️ WARNING
3. Output: Priority-Weighted Section Allocation table

### Step 0c: Gap-to-Emphasis Mapping (MANDATORY — CONDITIONAL: only if domain ontology exists)
1. For each intervention:
   - **G3-G4** (severe/null gap): **Lead with the gap** — narrative centers on what's missing
     - Template: "[Intervention] is [widely/rapidly] used for [population], yet there is [G3/G4: no meaningful long-term follow-up data]. The [stakes] consequences of this knowledge gap are..."
   - **G0-G1** (data sufficient): **Efficient summary** — defer to Cochrane/meta-analyses, push forward
     - Template: "Multiple RCTs with follow-up to [horizon] have established that... Remaining uncertainties include [specific gaps]."
2. Output: Gap-to-Emphasis Mapping table

### Step 0d: Evidence Time Annotation (MANDATORY — CONDITIONAL: only if domain ontology exists)
1. For each planned citation:
   - Extract publication year + study type
   - Calculate chronological age → effective age (apply decay factor + age-accelerating multipliers)
   - Assign Band 0-4
2. For Band 2+ citations: plan qualifier language ("data from [era], applicability uncertain")
3. If latest primary data for an intervention >10 years: flag `⚠️ FIELD_STAGNANT`
4. If Band 2+ is sole evidence for a claim: flag `⚠️ AGING_EVIDENCE_SOLE_SOURCE`
5. Output: Time Annotation Schedule

### Step 0e: Domain Ontology Coverage Check (MANDATORY — CONDITIONAL: only if domain ontology exists)
1. Compare outline sections with domain ontology Intervention Inventory
2. If ontology has priority ≥5 intervention not in outline → `⚠️ WARNING: potentially missing topic`
3. If outline has topic not in ontology → add to ontology, mark `⚠️ DISCOVERED_LATE`
4. Generate coverage report: N interventions in ontology, N covered in outline, N missing
5. Output: Coverage Report

### Step 0f: Write Pre-Writing Brief (MANDATORY — CONDITIONAL: only if domain ontology exists)
1. Compile all Step 0a-0e outputs into `knowledge/pre-writing-plan.md`
2. Contains: allocation table + gap-emphasis mapping + time annotation schedule + coverage report
3. This file is the **writing brief** that Steps 1-N must follow

**Gate 8 post-condition**: `python3 scripts/verify_gates.py --gate 8` must pass.

---

## Writing Steps

### Step 1: Load Writing Brief (MANDATORY)
Read `knowledge/pre-writing-plan.md` if it exists; otherwise use `manuscript/outline.md` directly.

### Step 2: Load Relevant Paper Notes (MANDATORY)
Retrieve paper notes matching the target section's topic from `docs/papers/`.

### Step 3: Verify Paper Types (MANDATORY)
Confirm each paper's type code (A-J) and citation scope labels from Screening Agent Handoff.

### Step 4: Write Section (MANDATORY)
Academic review writing standards:
- **Logical flow**: Background → Current State → Advances → Controversies → Outlook
- **Citation management**: Every sentence from literature must note PMID/DOI
- **Citation scope matching**: Verify claim type vs. paper type:
  - Mechanism claim → must be supported by types A/B/C (not E)
  - Clinical association → can be supported by D/E/F/H
  - Background statement → can use type G as auxiliary
  - Case report (type I) → cannot solely support general claims
- **Thematic synthesis**: Avoid simple "A found X, B found Y" lists — write thematic synthesis
- **Language discipline**: See `claude/disciplines/language-naturalness.md` (6 anti-patterns)
- **Citation discipline**: See `claude/disciplines/citation-scope.md`
- **Manuscript integrity**: See `claude/disciplines/manuscript-integrity.md`

### Step 5: Write to Source File (MANDATORY)
Write draft to the file specified in `config.yaml` → `paths.manuscript_src` (single source of truth).

### Step 6: Run Generator (MANDATORY)
```bash
python3 scripts/gen_word.py
```

### Step 7: Self-Check Gates (MANDATORY)
```bash
python3 scripts/verify_gates.py --gate 4
python3 scripts/verify_gates.py --gate 5
python3 scripts/verify_gates.py --gate 6
```

### Output
- Written paragraphs in the manuscript source file
- Generated Word document (8 self-checks must all pass)
- Cited PMID list with type codes
- Citation scope compliance self-check table (claim type × citation type cross-reference)

### Writing Style Requirements
- Academic formal but not obscure
- Active voice preferred, avoid excessive passive
- No "Interestingly", "It is worth noting that" (see empty intensifiers in language-naturalness.md)
- Data statements must be precise: "increased by 34% (95% CI: 28-40%, p<0.001)" not "significantly increased"
- **Language variance**: At least 1 short sentence (<12 words) per paragraph
- Full naturalness spec: See `claude/disciplines/language-naturalness.md`
