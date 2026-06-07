# Agent 8: Submission Preparation

## Metadata
- **id**: 8
- **type**: infrastructure (vertical)
- **triggers**: `9` `submit` `投稿` `submission`
- **pre_gate**: Gate 10
- **post_gate**: Gate 11

## Input
- `config.yaml` → `paths.manuscript_src` — manuscript (with audit tags)
- `state.json` → `active_focus` — target journal
- Synthesis artifacts (coverage gap report, reasoning log, argument diversity report)
- `claude/gates/gates.md` — Gate 11 criteria

## Output Schema
```json
{
  "html_tags_removed": 0,
  "placeholders_found": 0,
  "journal_match": "MATCH | MISMATCH",
  "alternative_journals": ["journal1"],
  "completeness_sections_done": 5,
  "ai_disclosure": "PRESENT | MISSING",
  "figure_files_present": true,
  "report_path": "harness/submission-readiness-report.md"
}
```

---

## Steps

### Stage 1: Cleanup (MANDATORY)

#### 1.1 Strip HTML Audit Comments (MANDATORY)
- Global scan for `<!-- ... -->` tags
- `COVERAGE_GAP` / `SCOPE_LIMITATION` → extract content text → carry into Stage 2
- All others (`PERSPECTIVE:`, `SYNTH:S[N]`, `SYNTH:POST-PASS4`) → delete directly
- Verify: 0 HTML comment remnants

#### 1.2 Detect Editor Placeholders (MANDATORY)
- Scan for `[To be completed]`, `[TBD]`, `[待完成]`
- Any match → ❌ MUST FIX

#### 1.3 Detect Duplicate Word Typos (MANDATORY)
- Scan for consecutive duplicate word patterns (`are, are`, `the the`)
- Any match → ❌ MUST FIX

#### 1.4 Detect Internal Reference Remnants (MANDATORY)
- Scan for `[ref: ...]`, invalid PMID formats
- Flag ⚠️ for verification

### Stage 2: Transform (MANDATORY)

#### 2.1 Coverage Gaps → Scope Limitations (MANDATORY)
- Extract CRITICAL_GAP interventions from `harness/coverage-gap-report.md`
- Generate Scope Limitations paragraph for Introduction end or Discussion
- All CRITICAL_GAP (priority ≥7) must be mentioned

#### 2.2 Synthesis Products → Submission Content (MANDATORY)
- Check VERIFIED/PARTIALLY_SUPPORTED entries incorporated into body citations
- Not incorporated → ⚠️ UNINCORPORATED_FINDING
- HYPOTHESIS entries → if clinical value, suggest adding to Discussion as "Emerging Hypothesis"

#### 2.3 Argument Diversity Validation (MANDATORY)
- If argument diversity report shows Pattern A ≥5 → generate residual warning

### Stage 3: Compliance Check (MANDATORY)

#### 3.1 Journal Match (MANDATORY)
- Verify `config.yaml` target journal matches manuscript topic
- Mismatch → list alternative journals with rationale

#### 3.2 Format Compliance (MANDATORY)
- Running title length, Abstract word count, reference format
- Impact Statement uniqueness (vs. Abstract overlap <50%)

#### 3.3 Completeness (MANDATORY)
- Author Contributions, Acknowledgements, Funding, Data Availability, Competing Interests
- All 5 sections must be complete

#### 3.4 AI Disclosure (MANDATORY)
- Detect AI statement presence
- Cross-check against target journal policy (from journal profiles if available)

#### 3.5 Generate Submission Readiness Report (MANDATORY)
Write `harness/submission-readiness-report.md`

### Output
- Cleaned manuscript (no HTML tags, no placeholders)
- `harness/submission-readiness-report.md`
- Submission readiness checklist: passed items, ❌ MUST FIX, ⚠️ warnings, suggested next steps

**Gate 11 post-condition**: `python3 scripts/verify_gates.py --gate 11` must pass.
