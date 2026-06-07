# Agent 7: Synthesis

## Metadata
- **id**: 7
- **type**: execution (horizontal)
- **triggers**: `8` `synthesis` `合成`
- **pre_gate**: Gate 4 (manuscript draft exists)
- **post_gate**: Gate 9

## Input
- `config.yaml` → `paths.manuscript_src` — current draft
- `knowledge/domain-ontology.md` — intervention inventory + gap grades + urgency scores + interaction map
- `knowledge/pre-writing-plan.md` — writing brief (word allocation + gap emphasis + time annotation)
- `docs/papers/` — paper notes (for interaction hypothesis mechanism reasoning)
- `claude/gates/gates.md` — Gate 9 criteria
- `claude/prompts/` — synthesis reasoning rules, cross-intervention matrix template, clinical decision framework

## Output Schema
```json
{
  "cross_intervention_pairs_compared": 0,
  "hypotheses_generated": 0,
  "hypotheses_verified": 0,
  "hypotheses_partially_supported": 0,
  "hypotheses_unverified": 0,
  "pattern_a_count": 0,
  "flat_timeline_sections": 0,
  "coverage_gaps": {"critical": 0, "moderate": 0},
  "synthesis_artifacts": [
    "harness/cross-intervention-output.md",
    "harness/synthesis-reasoning-log.md",
    "harness/argument-diversity-report.md",
    "harness/coverage-gap-report.md"
  ]
}
```

---

## Steps

### Step 1: Cross-Intervention Comparison Matrix (MANDATORY)
1. Load all interventions from domain ontology
2. For each intervention pair (I_i, I_j): compare across dimensions D1-D7 (see `templates/cross-intervention-matrix.md`)
3. Detect asymmetry: pairs with ≥2 grade gap difference → generate qualitative comparison paragraph
4. Detect paradox: G3/G4 + high adoption rate → flag `⚠️ ADOPTION_PARADOX`
5. Output: `harness/cross-intervention-output.md`

### Step 2: Interaction Analysis & Hypothesis Loop (MANDATORY)
For each UNEXPLORED interaction pair:
1. **Mechanism Inference**: Based on known pathophysiology, write inference chain (each step annotated with supporting literature or "general pathophysiology")
2. **Directed Literature Search**: PubMed/Europe PMC search for `"[A] AND [B] [mechanism]"`
3. **Result Processing**:
   - Direct evidence found → `✅ VERIFIED` → cite → insert into manuscript
   - Indirect evidence → `⚠️ PARTIALLY_SUPPORTED` → cite + note indirectness → insert
   - Nothing found → `⚠️ HYPOTHESIS` → insert in hypothesis format
4. **Record**: Every hypothesis loop written to `harness/synthesis-reasoning-log.md`

**Hypothesis Insertion Format (mandatory)**:
> **[Hypothesis: mechanism-based inference, not empirically tested.]** Based on [pathway A]'s role in [mechanism] ([citation]), it is plausible that combined [A] + [B] may [predicted effect]. A directed literature search for "[query]" returned N results, none directly testing this interaction. This hypothesis requires empirical validation.

### Step 3: Clinical Decision Framework Generation (MANDATORY)
1. Scan manuscript → identify key decision nodes (situations where clinician faces ≥2 options)
2. For each node: extract options → annotate evidence status → generate provisional guidance
3. Use conditional branching (if-then) + explicit uncertainty annotations
4. Language constraint: "may consider" / "might guide" — **banned**: "should" unless strong guideline
5. Each decision node includes LMIC applicability note
6. Insert into manuscript (at end of each intervention section, or as centralized framework in Discussion)

### Step 4: Argument Diversity Scan (MANDATORY)
1. Scan full manuscript → detect Pattern A: "Although/While/Despite [evidence] is [limited], more research is needed"
2. Count: 0-2 → ✅, 3-4 → ⚠️ flag + replace, ≥5 → ❌ MUST FIX
3. For each MUST FIX: force conversion to alternative argument type (data-driven, mechanism-based, comparative, clinical-consequence, historical-trajectory)
4. Output: `harness/argument-diversity-report.md`

### Step 5: Time Evolution Annotation (MANDATORY)
1. For each section: extract cited paper years → if span >20 years without temporal framing language → `⚠️ FLAT_TIMELINE`
2. For each FLAT_TIMELINE section: insert "evidence evolution" summary
3. For claims relying on old data (Band 3+) as primary evidence: add external validity qualifier

### Step 6: Coverage Completeness Verification (MANDATORY)
1. Compare domain ontology Intervention Inventory with manuscript content
2. For each intervention in ontology with priority ≥4, absent/superficially mentioned in manuscript → `⚠️ COVERAGE_GAP`
3. For priority ≥7 → `❌ CRITICAL_GAP`
4. Output: `harness/coverage-gap-report.md`

### Step 7: Enhance Manuscript (MANDATORY)
1. Apply all verified insertions from Steps 1-6
2. Each insertion traced with HTML comment: `<!-- SYNTH:S[N] [TYPE] -->`
3. **Do NOT delete or rewrite original text** — synthesis is incremental
4. If rewrite needed → mark as suggestion for Agent 4 during review

### Output
1. **Enhanced manuscript** with synthesis insertions
2. **Synthesis artifacts**:
   - `harness/cross-intervention-output.md` — completed matrix
   - `harness/synthesis-reasoning-log.md` — all hypothesis loop trails
   - `harness/argument-diversity-report.md` — argument type distribution + Pattern A flags
   - `harness/coverage-gap-report.md` — missing interventions + priority
3. **Synthesis summary**: one paragraph describing what was added and why

**Gate 9 post-condition**: `python3 scripts/verify_gates.py --gate 9` must pass.
