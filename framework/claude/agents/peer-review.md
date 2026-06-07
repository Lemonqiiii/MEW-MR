# Agent: Standalone Peer Review

## Metadata
- **id**: peer-review
- **type**: execution (horizontal, standalone)
- **triggers**: `peer-review` `审稿` `外审` `review-manuscript`
- **pre_gate**: none
- **post_gate**: none

## Purpose
Perform a structured peer review of an external manuscript. Automatically detects manuscript type (original research, narrative review, systematic review/meta-analysis) and applies the appropriate review dimensions.

## Input
- Manuscript file path
- `templates/peer-review-report.md` — report template
- `templates/peer-review-sr-report.md` — SR-specific report template
- `claude/disciplines/` — review standards
- `claude/prompts/` — review enhancement prompts
- `templates/rob-assessment.md` — RoB reference
- `templates/grade-profile.md` — GRADE reference

## Output Schema
```json
{
  "manuscript": "path",
  "review_report_path": "manuscript/peer_review_report.md",
  "manuscript_type": "original | narrative_review | systematic_review | meta_analysis",
  "total_issues": 0,
  "must_fix": 0,
  "recommendation": "accept | minor_revision | major_revision | reject",
  "dimensions": {
    "scientific_validity": {"score": 0, "issues": 0},
    "methodology": {"score": 0, "issues": 0},
    "data_interpretation": {"score": 0, "issues": 0},
    "novelty_impact": {"score": 0, "issues": 0},
    "presentation": {"score": 0, "issues": 0},
    "sr_dimensions": null_or_SR_object
  }
}
```

---

## Steps

### Step 0: Load and Classify Manuscript (MANDATORY)
1. Accept manuscript path from user, or prompt
2. Read the manuscript
3. **Auto-detect manuscript type** by scanning title, abstract, and methods:
   - Contains "systematic review" / "meta-analysis" / PRISMA citation → **SR/MA**
   - Contains "review" but no systematic methodology → **Narrative Review**
   - Otherwise → **Original Research**
4. Set `manuscript_type` — this determines which subsequent steps apply

---

## Universal Steps (all manuscript types)

### Step 1: Scientific Validity (MANDATORY)
1. **Research Question**: Clearly stated? Answerable with presented data?
2. **Literature Context**: Accurate representation of prior work?
3. **Internal Logic**: Conclusions follow from data? Unsupported leaps?
4. **Claim Verification**: Cross-check 5-8 key claims against cited references
5. Apply `claude/disciplines/citation-scope.md`

### Step 2: Methodology (MANDATORY)
1. **Design**: Appropriate for the question?
2. **Population/Sample**: Described? Size adequate? Selection bias?
3. **Methods**: Sufficiently detailed for reproducibility?
4. **Statistics**: Appropriate tests? Multiple comparison correction?
5. **Controls**: Present and appropriate? (for experimental studies)

### Step 3: Data Interpretation (MANDATORY)
1. **Results**: Clear, complete? Selective reporting?
2. **Statistical Claims**: P-values, CIs, effect sizes correctly interpreted?
3. **Overstatement**: Claims exceeding data support?
4. **Negative Claims**: Apply `claude/prompts/negative-claim-detection.md`
5. **Statistical Translation**: Apply `claude/prompts/data-translation.md`

### Step 4: Novelty & Impact (MANDATORY)
1. **Novelty**: Meaningful advance? Specific contribution?
2. **Relevance**: Who is affected? Practice change implications?
3. **Generalizability**: Applicable populations/settings?
4. **Limitations**: Honestly acknowledged? Unstated limitations?

### Step 5: Presentation (MANDATORY)
1. **Structure**: Journal conventions? Sections logical?
2. **Clarity**: Accessible? Jargon appropriate?
3. **Language**: Apply `claude/disciplines/language-naturalness.md`
4. **Figures/Tables**: Clear, labeled, stand-alone understandable?
5. **References**: Format, recency, key omissions?

---

## Systematic Review / Meta-Analysis Specific Steps
> These activate when manuscript_type is "systematic_review" or "meta_analysis"

### Step SR-1: PRISMA 2020 Compliance (MANDATORY for SR/MA)
Audit against PRISMA 2020 checklist (27 items):

#### Title & Abstract (Items 1-2)
| # | Check | Pass/Fail | Note |
|---|-------|-----------|------|
| 1 | Title identifies report as systematic review/meta-analysis | | |
| 2 | Abstract follows PRISMA structured format | | |

#### Methods (Items 3-12)
| # | Check | Pass/Fail | Note |
|---|-------|-----------|------|
| 3 | Rationale stated | | |
| 4 | Explicit eligibility criteria (PICO + study designs) | | |
| 5 | Information sources (databases, registers, date last searched) | | |
| 6 | Complete search strategy for ≥1 database | | |
| 7 | Selection process (screening methods, independent reviewers) | | |
| 8 | Data extraction methods (form, pilot, independent extraction) | | |
| 9 | Data items extracted (all outcomes, variables) | | |
| 10 | Risk of bias assessment tool and method | | |
| 11 | Effect measures (RR, OR, MD, etc.) | | |
| 12 | Synthesis methods (meta-analysis model, heterogeneity, sensitivity, publication bias, certainty) | | |

#### Results (Items 13-20)
| # | Check | Pass/Fail | Note |
|---|-------|-----------|------|
| 13 | Study selection flow with numbers (PRISMA flowchart) | | |
| 14 | Study characteristics table | | |
| 15 | Risk of bias results per study | | |
| 16 | Results of each outcome with effect estimates and CIs | | |
| 17 | Results of syntheses (forest plots, heterogeneity) | | |
| 18 | Reporting bias assessment | | |
| 19 | Certainty of evidence (GRADE or equivalent) | | |

#### Discussion (Items 20-27)
| # | Check | Pass/Fail | Note |
|---|-------|-----------|------|
| 20 | Summary of evidence with limitations | | |
| 22 | Certainty of evidence discussion | | |
| 23 | Implications for practice/policy | | |
| 24 | Implications for research | | |
| 25 | Registration (PROSPERO ID or equivalent) | | |
| 26 | Protocol availability | | |
| 27 | Funding and competing interests | | |

**PRISMA compliance score**: X/27 items

### Step SR-2: Search Strategy Audit (MANDATORY for SR/MA)
1. **Database coverage**: PubMed alone is insufficient — minimum: PubMed + Embase + Cochrane
2. **Search reproducibility**: Is the full search string provided for at least one database?
3. **Date restriction**: Search date ≤12 months before submission? Re-run indicated?
4. **Grey literature**: Conference abstracts, trial registries, dissertations included?
5. **Language restriction**: If English-only, acknowledged as limitation?
6. **Search filter validation**: Are validated filters used (e.g., Cochrane RCT filter)?
7. **Missing databases**: Note any key databases not searched

### Step SR-3: Screening & Selection Audit (MANDATORY for SR/MA)
1. **Dual screening**: Was screening performed independently by ≥2 reviewers?
2. **Inter-rater reliability**: Is Cohen's Kappa reported? (target >0.6)
3. **Conflict resolution**: Is the process described?
4. **PRISMA flowchart**: Are the numbers consistent? (initial → dedup → screened → full-text → included + excluded with reasons)
5. **Excluded studies**: Are reasons provided? Is there a table of excluded studies with reasons for key borderline cases?

### Step SR-4: Risk of Bias Audit (MANDATORY for SR/MA)
1. **Tool selection**: Is the RoB tool appropriate? (RCT → RoB 2; NRS → ROBINS-I; Cohort → NOS)
2. **Domain-level reporting**: Are individual domain judgments reported, not just overall?
3. **Dual assessment**: Two reviewers independently?
4. **Integration**: Are RoB results used in synthesis (sensitivity analysis excluding high-RoB)?
5. **Missing assessments**: Any included study without RoB assessment?

### Step SR-5: Synthesis Audit (MANDATORY for SR/MA)
#### If Meta-Analysis was performed:
1. **Model choice**: Fixed vs random-effects justified? (I² reported?)
2. **Heterogeneity**: I² values reported and interpreted?
3. **Forest plots**: Effect estimates + CIs + weights clearly displayed?
4. **Publication bias**: Funnel plot + Egger's test if ≥10 studies?
5. **Sensitivity analyses**: Leave-one-out? Excluding high-RoB? Subgroup analyses?
6. **Software**: Analysis software and version reported?
7. **Double-counting**: Any control group counted twice across comparisons?

#### If Narrative Synthesis only:
1. **SWiM compliance**: Synthesis Without Meta-analysis guidelines followed?
2. **Vote-counting avoided**: Not simply counting "positive" vs "negative" studies?
3. **Structured reporting**: Organized by outcome, not by study?

### Step SR-6: GRADE / Certainty Audit (MANDATORY for SR/MA)
1. **GRADE performed**: For all critical outcomes? For all important outcomes?
2. **SoF table**: Summary of Findings table with absolute effects?
3. **Downgrade documentation**: Each domain decision justified?
4. **GRADE-Conclusion consistency**: Do conclusions match the certainty ratings?
   - "X is effective" with ⊕⊖⊖⊖ Very Low certainty → **MUST FIX**
5. **Certainty-language matching**:
   | GRADE | Appropriate Language |
   |-------|---------------------|
   | High | "is effective" / "reduces" |
   | Moderate | "probably reduces" / "likely effective" |
   | Low | "may reduce" / "might be effective" |
   | Very Low | "the evidence is uncertain" / "we are uncertain whether" |

### Step SR-7: Protocol Fidelity (MANDATORY for SR/MA)
1. **Registration**: PROSPERO or equivalent? ID provided?
2. **Protocol deviations**: Any differences between protocol and review? Documented and justified?
3. **Unregistered**: If no registration, flagged as significant limitation
4. **Outcome switching**: Are outcomes in the review consistent with the protocol?

---

## Report Generation

### Step 6: Generate Peer Review Report (MANDATORY)

Use `templates/peer-review-report.md` for all manuscript types.
For SR/MA manuscripts, **append** the SR-specific dimension table and PRISMA audit.

### Step 7: Save Report (MANDATORY)
Write to `manuscript/peer_review_report.md` (or user-specified path).
