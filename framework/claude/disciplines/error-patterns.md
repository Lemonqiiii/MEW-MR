# Error Pattern Library

> Universal error patterns encountered during AI-assisted medical review writing.
> Domain-specific exclusion rules belong in `templates/paper-types/<system>.md`, not here.

## Reasoning & Writing Errors

### Citation Grafting (引用嫁接)
- **Pattern**: Training-data knowledge + mismatched citation
- **Detection**: Claim keywords vs. cited abstract keywords match rate <30%
- **Fix**: Revert claim; find proper citation or remove claim entirely

### Elegant Vacuity (优雅空洞)
- **Pattern**: "Although/While/Despite [evidence] is [limited], more research is needed" repeated ≥5 times
- **Detection**: Agent 7 Step 4 scans for Pattern A across full manuscript
- **Fix**: Convert to alternative argument types — data-driven, mechanism-based, comparative, clinical-consequence, or historical-trajectory arguments

### Silence Blindness (沉默失明)
- **Pattern**: Manuscript systematically omits clinically important interventions without acknowledgment
- **Detection**: Domain ontology vs. manuscript coverage comparison (Agent 7 Step 6)
- **Fix**: Add scope limitations paragraph; include high-priority missing interventions

### Cochrane Worship (Cochrane崇拜)
- **Pattern**: Cochrane reviews cited without critical discussion
- **Detection**: Cochrane concentration >60% OR ≥2 Cochrane citations with zero critical qualifiers (Agent 4 Post-Pass 4)
- **Fix**: Add GRADE quality notes, CI width discussion, trial overlap analysis, version timeliness check

### Missing Statistical Translation (统计翻译缺失)
- **Pattern**: RR/HR/OR values reported without ARR/NNT translation
- **Detection**: Agent 4 Pre-Pass 2 scans for all RR/HR/OR values
- **Fix**: Add ARR + NNT/NNH; if baseline risk unknown, mark `⚠️ BASELINE_RISK_UNKNOWN`

### Single Perspective (视角单一)
- **Pattern**: Entire review maintains only abstract reviewer perspective
- **Detection**: Agent 4 Pre-Pass 1 checks for ≥3 perspective types (clinician, patient/family, LMIC, policymaker, researcher)
- **Fix**: Insert perspective paragraphs at trigger points

### Absolute Negative Claim Contradiction (绝对否定声称矛盾)
- **Pattern**: "No data exists" / "never been studied" claims contradicted by cited literature content
- **Detection**: Agent 4 Step 1.5 two-phase verification (cited-literature check + reference-pool reverse check)
- **Fix**: Replace absolute claims with qualified statements matching actual evidence

### Mixed Metric Reporting (度量混用)
- **Pattern**: OR, HR, RR mixed in the same sentence without explaining metric differences
- **Detection**: Agent 4 Step 5
- **Fix**: Add note explaining why metrics differ (study design, adjustment, etc.)

## Process & Structural Errors

### Step Skipping (Step跳过)
- **Pattern**: Agent skips a mandatory gate step
- **Detection**: Steps marked `MANDATORY` in agent definitions
- **Fix**: Agent definitions mark gatekeeping steps as unskippable; verify with `scripts/verify_gates.py`

### Reference Scope Overreach (引用越权)
- **Pattern**: Type E paper used for causal claim OR type G review used as primary citation
- **Detection**: Gate 6 — citation scope compliance check
- **Fix**: Replace primary citation with appropriate type OR add qualifying language

### Numbering Drift (编号漂移)
- **Pattern**: After deleting figure/table, manual renumbering introduces errors
- **Detection**: Automated self-check in `gen_word.py`
- **Fix**: Automated renumbering; self-check verifies body refs match actual figures/tables

### Range Omission (范围遗漏)
- **Pattern**: `[8-10]` not matched by regex, only `[8]` extracted
- **Detection**: Expand all ranges before comparison
- **Fix**: Reference parsing handles `[N]`, `[N,M]`, `[N-M]` formats

### Compression Loss (压缩丢失)
- **Pattern**: Token-saving compression truncates paragraphs
- **Fix**: Always parse from source file, not from compressed context

### Reference Section Corruption (编辑破坏引用段)
- **Pattern**: Incremental edits duplicate `## References` section
- **Fix**: Use `scripts/rebuild_refs.py` to batch-rebuild reference section
