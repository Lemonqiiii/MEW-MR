# Revision Map — jitc_submission.md R4

This file maps each review finding to its resolution in the manuscript. Used by review agents to verify fixes without full re-read.

**Format:** `review_item_id | line | grep-anchor | status`

---

## R4 Fixes

### MF-NEW (Must Fix)

```
MF-NEW-1 | L194 | "Schmidt et al., JAMA 2012 [41]" | ✅
MF-NEW-1 | L196 | "Doyle et al., JAMA Pediatrics 2017 [42]" | ✅
MF-NEW-1 | L200 | "11-year CAP follow-up [42]" | ✅
MF-NEW-1 | L218 | "beyond 11 years of age [42]" | ✅
MF-NEW-1 | L220 | "82% follow-up at 5 years [41]" | ✅
MF-NEW-1 | L220 | "pulmonary function at 11 years [42]" | ✅
MF-NEW-1 | L22  | "11-year follow-up [41,42]" (Key Messages) | ✅
MF-NEW-1 | L636 | "41. Schmidt B..." new reference | ✅
MF-NEW-1 | L638 | "42. Doyle LW..." new reference | ✅
MF-NEW-2 | L52  | "informed by a structured literature search" (condensed §1.1) | ✅
MF-NEW-2 | L58  | "detailed account...provided in the **Methods** section" | ✅
MF-NEW-3 | L503 | "[3,20]" (ACS 30yr safety evidence) | ✅
MF-NEW-3 | L503 | "[39,41,42]" (caffeine 11yr follow-up) | ✅
MF-NEW-3 | L505 | "[14,15]" (early vs late PCS) | ✅
MF-NEW-3 | L507 | "[5]" (VTV NNT ~7) | ✅
MF-NEW-3 | L507 | "[16]" (LISA NNT ~6) | ✅
MF-NEW-3 | L509 | "[17,37]" (O2 targets 90-94%) | ✅
```

### NC-NEW (Numerical/Consistency)

```
NC-NEW-1 | L151 | "point-estimate NNH ~50" (late PCS CP) | ✅
```

### CA-NEW (Critical Qualifiers)

```
CA-NEW-2 | L149 | "The Cochrane cutoff for 'early'" (Notably removed) | ✅
CA-NEW-2 | L354 | "The Caffeine for Apnea of Prematurity" (Notably removed) | ✅
CA-NEW-3 | L507 | "suggesting that novel long-term harms are unlikely though unproven" | ✅
```

### SI-NEW (Suggested Improvements)

```
SI-NEW-5 | L477 | "(see Section 4 for the full caffeine evidence synthesis)" | ✅
```

---

## R3 Fixes (verified intact)

### MF (Must Fix)

```
MF-1 | L351 | "0.86 standard deviations below term-born peers (95% CI 0.78–0.94)" | ✅
MF-2 | L117 | "secondary outcome in the IPD meta-analysis" | ✅
MF-3 | L146 | "GRADE certainty for this outcome is high (2021 Cochrane update)" | ✅
MF-4 | L41  | "contextual comparator (Section 4)" | ✅
MF-5 | L534 | References populated — 40 entries with PMIDs | ✅
```

## NC (Numerical/Consistency)

```
NC-1 | L5   | "42.5% of cited references, 17 of 40" (Abstract) | ✅
NC-1 | L448 | "42.5% of the cited references (17 of 40)" (§11.7) | ✅
NC-2 | L47  | "551 articles were excluded" | ✅
NC-3 | L369 | "1.4% (8 of 590)" (§10) | ✅
NC-3 | L9   | "1.4% (8 of 590)" (Impact Statement) | ✅
NC-3 | L494 | "1.4% (8 of 590)" (§12) | ✅
NC-4 | L127 | "in their fifties" (§2.5 body) | ✅
NC-4 | L130 | "in their fifties" (Clinical Perspective) | ✅
```

## CA (Critical Qualifiers)

```
CA-1 | L225 | "last search: January 2017; ...newer ventilation modes may alter" | ✅
CA-2 | L146 | "limited predictor of school-age motor function and cerebral palsy diagnosis" | ✅
CA-3 | L105 | "New trials in LMIC settings [e.g., WHO ACTION] may alter the generalizability" | ✅
```

## SI (Suggested Improvements)

```
SI-1 | L486 | "### What We Know" sub-heading | ✅
SI-1 | L490 | "### What We Don't Know" sub-heading | ✅
SI-1 | L510 | "### Call to Action" sub-heading | ✅
SI-2 | L248 | "**Clinical Perspective**: The ventilation evidence base..." | ✅
SI-3 | L440 | "Evidence gap severity grades: **G0** = no gap..." (no harness/ ref) | ✅
SI-4 | L213 | "(See Section 11.9 for a discussion of caffeine as a potential confounder...)" | ✅
SI-5 | L117 | "ARR ~6%, NNT ~17" (repeat ACS RDS) | ✅
SI-5 | L240 | "near-null effect translates to a very large NNT" (HFOV) | ✅
```

## AX (Additional fixes from full review)

```
AX-1 | L187 | "borderline statistical significance given the upper CI bound of 0.92" | ✅
AX-2 | L316 | "has not been evaluated in trials with long-term follow-up" | ✅
AX-3 | L342 | "This pathway is complicated by the fact that the same intervention can have opposing..." | ✅
AX-4 | L419 | "**Research Perspective**: The evidence gaps identified..." | ✅
AX-5 | L219 | "no randomized trial has followed children beyond hospital discharge" | ✅
```

## Verification Command

```bash
grep -n -f <(awk -F'|' '{print $3}' REVISION_MAP.md | grep '✅' | sed 's/^ *//;s/ *$//') jitc_submission.md
```

**Last updated:** 2026-06-06 R3
