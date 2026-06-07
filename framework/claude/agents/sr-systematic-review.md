# Agent: Systematic Review Orchestrator

## Metadata
- **id**: sr
- **type**: execution (horizontal) — orchestrates SR-specific workflow
- **triggers**: `sr` `systematic` `系统综述` `meta`
- **pre_gate**: none
- **post_gate**: PRISMA compliance, GRADE completeness

## Purpose
Orchestrates a PRISMA-compliant systematic review (with or without meta-analysis).
Activates when `config.yaml` → `review_type` is "systematic" or "meta-analysis".
Adds SR-specific steps between the standard pipeline agents.

## Differences from Narrative Review

| Step | Narrative Review | Systematic Review |
|------|-----------------|-------------------|
| Protocol | Optional | **Required** — PROSPERO registration |
| Search | 3-4 databases | **Mandatory**: PubMed + Embase + Cochrane + CT.gov minimum |
| Search documentation | Brief | **Full search strategies** for each database (supplementary) |
| Screening | Single reviewer | **Dual independent** screening + conflict resolution |
| PRISMA | Not required | **Required** — complete flowchart with exact numbers |
| RoB Assessment | Not required | **Required** — every included study |
| Data Extraction | Free-form notes | **Structured forms** — dual extraction + reconciliation |
| Synthesis | Thematic | **GRADE assessment** + meta-analysis if appropriate |
| Reporting | Standard | **PRISMA 2020 checklist** + PRISMA flowchart |

---

## Steps

### Step 0: Protocol Registration (MANDATORY)
1. Check if a PROSPERO registration exists for this topic
2. If not: guide user through protocol development
3. Protocol elements:
   - PICO (Population, Intervention, Comparison, Outcome)
   - Inclusion/exclusion criteria
   - Search strategy (at least one database)
   - Data extraction plan
   - Risk of bias assessment plan
   - Synthesis plan (meta-analysis or narrative)
4. Register at PROSPERO (https://www.crd.york.ac.uk/prospero/)
5. Record registration ID in `state.json`

### Step 1: Systematic Search (MANDATORY — delegates to Agent 1 with SR parameters)
Execute Agent 1 but with systematic review rigor:

1. **Mandatory databases**: PubMed, Embase, Cochrane CENTRAL (minimum)
2. **Recommended**: Web of Science, Scopus, ClinicalTrials.gov, WHO ICTRP
3. **Grey literature**: ProQuest Dissertations, conference proceedings, preprint servers
4. **Search strategy documentation**: Save complete search string for each database
5. **De-duplication**: Document dedup method and numbers
6. **Search update**: Re-run search before final analysis if >6 months since original search

**Output**: `docs/search-results/search-strategies.md` with complete, reproducible search strings

### Step 2: Dual Screening Setup (MANDATORY)
Configure dual-screening before starting Agent 6:

1. **Screening tool**: Use Rayyan, Covidence, or Excel-based screening form
2. **Pilot test**: Both reviewers screen the same 50 records → calculate agreement
3. **Cohen's Kappa**: Calculate inter-rater reliability (target κ > 0.6)
4. **Conflict resolution**: Define process for disagreements (discussion → third reviewer)
5. **Blinding**: Reviewers should be blinded to each other's decisions during screening

After Agent 6 completes, document:
- Number of conflicts
- Resolution method
- Final κ statistic

### Step 3: Risk of Bias Assessment (MANDATORY — after Agent 2)
For every included study:

1. Select appropriate RoB tool per `templates/rob-assessment.md`:
   - RCTs → Cochrane RoB 2
   - Non-randomized → ROBINS-I
   - Cohort/Case-Control → Newcastle-Ottawa Scale
2. **Dual assessment**: Two reviewers independently assess RoB
3. Generate RoB summary table and traffic-light plot
4. Record each study's overall RoB in data extraction

### Step 4: Structured Data Extraction (MANDATORY — after RoB)
For every included study:

1. Use `templates/data-extraction.md` form
2. **Dual extraction**: Two reviewers extract independently
3. **Reconciliation**: Compare, resolve discrepancies
4. **Missing data**: Contact study authors (document attempts)
5. Pilot test extraction form on 3-5 studies first

### Step 5: Synthesis Decision (MANDATORY — before Agent 7)
Determine synthesis approach:

#### Meta-Analysis Decision Tree
```
Are the studies sufficiently homogeneous?
  ├── NO → Narrative synthesis only (with GRADE)
  └── YES:
      ├── ≥3 studies with same outcome? → Fixed or random-effects MA
      ├── ≥10 studies? → MA + funnel plot + Egger's test
      ├── Only 2 studies? → Consider whether MA is informative
      └── High I² (>75%)? → Explore subgroup/sensitivity; if unexplained → narrative
```

If meta-analysis is appropriate:
1. Select model (fixed-effect if I² < 50%; random-effects if I² ≥ 50%)
2. Choose outcome metric (RR/OR for dichotomous; MD/SMD for continuous)
3. Run meta-analysis
4. Generate forest plot
5. Assess publication bias (funnel plot + Egger's test if ≥10 studies)
6. Sensitivity analyses (excluding high-RoB studies, leave-one-out)

If narrative synthesis only:
1. Use GRADE without meta-analytic pooling
2. Follow SWiM (Synthesis Without Meta-analysis) guidelines

### Step 6: GRADE Assessment (MANDATORY — after synthesis)
For each critical and important outcome:

1. Use `templates/grade-profile.md`
2. Start from appropriate certainty level (RCTs = High; Observational = Low)
3. Downgrade/upgrade per GRADE domains
4. Generate Summary of Findings (SoF) table
5. Include in manuscript

### Step 7: PRISMA 2020 Compliance (MANDATORY — before Agent 8)
1. Generate PRISMA flowchart: `python3 scripts/prisma_flowchart.py --markdown`
2. Complete PRISMA 2020 checklist (27 items)
3. Include checklist as supplementary material
4. Verify:
   - Abstract includes PRISMA-structured summary
   - Methods includes: protocol registration, search strategy, screening process, RoB tool, synthesis methods, GRADE
   - Results includes: study selection flow, study characteristics, RoB results, synthesis results
   - Discussion includes: limitations, certainty of evidence (GRADE), implications

### Step 8: PRISMA Abstract (MANDATORY)
Structure abstract per PRISMA 2020:

```markdown
## Abstract

**Background**: [1-2 sentences]

**Methods**:
- **Eligibility criteria**: [PICO + study designs]
- **Information sources**: [databases searched + last search date]
- **Risk of bias**: [tool(s) used]
- **Synthesis methods**: [meta-analysis methods or narrative synthesis approach]
- **Registration**: [PROSPERO ID]

**Results**:
- **Included studies**: [N studies, N participants]
- **Synthesis results**: [key findings with effect estimates and GRADE ratings]
- **Limitations**: [key RoB concerns, heterogeneity]

**Conclusions**: [1-2 sentences, matched to evidence certainty]

**Funding**: [source]
**Registration**: [PROSPERO CRD4202XXXXXXXX]
```

---

## Handoff Schema
```json
{
  "review_type": "systematic",
  "protocol_registration": "CRD4202XXXXXXXX",
  "databases_searched": ["PubMed", "Embase", "Cochrane CENTRAL", ...],
  "search_date": "YYYY-MM-DD",
  "dual_screening": {
    "kappa": 0.75,
    "conflicts": 23,
    "resolution": "discussion + third reviewer"
  },
  "rob_summary": {
    "tool": "RoB 2",
    "low_risk": 5,
    "some_concerns": 8,
    "high_risk": 2
  },
  "synthesis": {
    "type": "meta-analysis",
    "model": "random-effects",
    "outcomes_pooled": 3,
    "i_squared_range": "32-68%"
  },
  "grade": {
    "high": 1,
    "moderate": 2,
    "low": 1,
    "very_low": 0
  },
  "prisma_flowchart_ready": true,
  "prisma_checklist_complete": true
}
```
