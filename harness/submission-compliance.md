# Agent 8 Submission Compliance Rules

> **用途**: Agent 8 三阶段工作流的详细操作规范
> **定位**: 基础设施层 — Agent 5（评估）之后、gen_word_full.py 之前
> **原则**: 将内部审计产物转换为投稿就绪稿件。清理编辑标记但保留实质内容。

---

## Stage 1: Cleanup — 编辑标记处理

### 1.1 HTML Comment Stripping

| Comment Type | Pattern | Action |
|-------------|---------|--------|
| Perspective markers | `<!-- PERSPECTIVE:P[N] -->` | **Delete** — perspective text has been integrated, comment no longer needed |
| Synthesis step markers | `<!-- SYNTH:S[N] [TYPE] -->` | **Delete** — synthesis logic is documented in harness logs |
| Post-pass markers | `<!-- SYNTH:POST-PASS4 COCHRANE_CAVEAT -->` | **Delete** — caveat is embedded in text |
| Coverage gap markers | `<!-- SYNTH:S6 COVERAGE_GAP -->` | **Extract then delete** — text content following the marker is preserved; marker itself is removed |
| Scope limitation markers | `<!-- SCOPE_LIMITATION -->` | **Extract then delete** — same as above |

**Rule**: All `<!-- ... -->` constructs must be removed from the manuscript before submission. NO exceptions.

### 1.2 Placeholder Detection

Scan for patterns indicating incomplete sections:
- `[To be completed]`
- `[TBD]`
- `[待完成]`
- `[Author list to be added]`
- `[Funding source to be added]`

**Any match → ❌ MUST FIX**: Section must be completed before submission.

### 1.3 Duplicate Word Detection

Scan for repeated word patterns:
- `are, are` / `is, is` / `the the` / `and and`
- Any word repeated consecutively at word boundary with optional comma/space

**Any match → ❌ MUST FIX**: Typo must be corrected.

### 1.4 Internal Reference Detection

Scan for internal reference artifacts:
- `[ref: ...]` — internal cross-reference format
- `PMID: [N]` where N is not a valid PMID (e.g., `PMID: 41915392` → verify via PubMed)
- `[citation needed]` / `[insert ref]`

**Match → ⚠️ WARNING**: Flag for verification. May indicate incomplete citation.

---

## Stage 2: Transform — 合成产物转化为投稿文本

### 2.1 Coverage Gap → Scope Limitations

**Input**: `harness/coverage-gap-report.md`
**Output**: Scope limitations paragraph for Discussion or Introduction

**Template**:
```
This review focused on [declared scope from active-focus.md]. Several clinically important interventions that intersect with neonatal respiratory management were beyond our scope, including:

- **[Intervention 1]** ([brief justification of clinical relevance])
- **[Intervention 2]** ([brief justification])

Their exclusion should be considered when interpreting the generalizability of our findings. In particular, [most critical gap] deserves acknowledgment because [reason].
```

**Required**: All CRITICAL_GAP interventions (priority ≥7) must be mentioned in this paragraph.

### 2.2 Synthesis Findings → Submission-Ready Citations

**Input**: `harness/synthesis-reasoning-log.md`
**Process**:
- For each ✅ VERIFIED entry: Check if the finding is cited in the manuscript reference list
- If YES → ✅ INCORPORATED
- If NO → ⚠️ UNINCORPORATED_FINDING: flag for author review
- For each ⚠️ PARTIALLY_SUPPORTED entry: Include in Discussion if clinically significant
- For each ⚠️ HYPOTHESIS entry: Optionally include in Discussion as "Emerging Hypothesis" with explicit caveat

### 2.3 Argument Diversity Warning

**Input**: `harness/argument-diversity-report.md`
**Process**: If Pattern A count ≥5 → generate warning for final author review. Note: Pattern A content is substantive, not a technical marker — Agent 4 should have already addressed most instances. Agent 8 only raises a final flag.

---

## Stage 3: Compliance — 期刊合规检查

### 3.1 Journal-Topic Match Verification

1. Load target journal from `memory/active-focus.md`
2. Load manuscript topic from `manuscript/outline.md` or abstract
3. Verify match:
   - Topic outside journal scope → ❌ MISMATCH
   - Neonatal/perinatal journal + neonatal topic → ✅ MATCH
   - Pediatric journal + pediatric/neonatal topic → ✅ MATCH
4. If MISMATCH → suggest 3-5 appropriate journals based on topic

**Suggested journal list for neonatal respiratory topics**:
- *Pediatric Research*
- *Neonatology*
- *JAMA Pediatrics*
- *Archives of Disease in Childhood - Fetal and Neonatal Edition*
- *Seminars in Perinatology*
- *Journal of Perinatology*
- *Pediatric Pulmonology*

### 3.2 Format Compliance

| Check | Method | Pediatric Research Standard |
|-------|--------|---------------------------|
| Running title length | Count characters | ≤50 characters |
| Abstract word count | Count words | Structured ≤250; unstructured ≤200 |
| Reference format | Verify consistent style | Vancouver (numbered) |
| Impact Statement uniqueness | Compare with Abstract | <50% overlap in content |

### 3.3 Completeness

| Section | Status | Action if Missing |
|---------|--------|------------------|
| Author Contributions | Must be completed per CRediT taxonomy | ❌ MUST FIX |
| Acknowledgements | Must be completed | ❌ MUST FIX |
| Funding | Must include grant numbers if applicable; or "No funding received" | ❌ MUST FIX |
| Data Availability Statement | Must exist | ❌ MUST FIX |
| Competing Interests | Must exist | ❌ MUST FIX |
| Figure/Table files | Each referenced figure/table must have a file | ❌ MUST FIX |

### 3.4 AI Disclosure

**Detection**: Scan manuscript for AI use declaration keywords:
- "artificial intelligence" / "AI-assisted" / "language model" / "LLM" / "large language model" / "generative AI"

**If absent**: Check target journal policy:

| Journal | Policy | Required Language |
|---------|--------|------------------|
| JAMA / JAMA Network | Required | "AI was used for [specific tasks]. All AI-generated content was reviewed and verified by the authors." |
| BMJ | Required | Must disclose in Methods or Acknowledgements |
| Cochrane | Required | AI tools must be acknowledged; cannot be listed as authors |
| Pediatric Research (Springer Nature) | Required | Must disclose in Methods or Acknowledgements per Springer Nature AI policy |
| Most others (post-2024) | Recommended | Check journal-specific author guidelines |

**If policy requires disclosure and none found → ⚠️ MISSING_AI_DISCLOSURE**

### 3.5 Submission Readiness Report

**Output**: `harness/submission-readiness-report.md`

```markdown
# Submission Readiness Report — [Manuscript] — YYYY-MM-DD

## Stage 1: Cleanup
- HTML comments stripped: N
- Placeholders found: N (all MUST FIX)
- Duplicate words found: N (all MUST FIX)

## Stage 2: Transform
- Coverage gaps addressed: N/N CRITICAL_GAPs mentioned
- Unincorporated synthesis findings: N
- Argument diversity warning: [YES/NO]

## Stage 3: Compliance
- Journal match: [MATCH/MISMATCH] — [journal name]
- Running title: [N] chars ([PASS/FAIL])
- Abstract word count: [N] words ([PASS/FAIL])
- Reference format: [PASS/FAIL]
- Impact Statement uniqueness: [N]% overlap ([PASS/FAIL])
- Completeness: [N]/[N] sections completed
- AI disclosure: [PRESENT/MISSING] — [policy guidance]

## MUST FIX Before Submission
[list of all ❌ items]

## Warnings
[list of all ⚠️ items]

## Recommended Next Steps
[prioritized action list]
```
