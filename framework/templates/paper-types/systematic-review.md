# Paper Classification for Systematic Reviews

> Use this classification when `config.yaml` → `review_type` is "systematic" or "meta-analysis".
> Unlike the A-J system (designed for mechanism/biomarker reviews), this system classifies
> papers by study design — which is the primary axis for systematic review inclusion.

---

## Study Design Classification

### Experimental
| Code | Design | Definition | Key Features |
|------|--------|-----------|-------------|
| **RCT** | Randomized Controlled Trial | Prospective, random allocation to intervention/control | Randomization method, blinding, allocation concealment |
| **cRCT** | Cluster RCT | Randomization by group/cluster | Clustering accounted for in analysis |
| **Quasi** | Quasi-Experimental | Intervention with non-random control | Before-after, interrupted time series, controlled but not randomized |

### Observational — Analytical
| Code | Design | Definition | Key Features |
|------|--------|-----------|-------------|
| **Cohort** | Cohort Study | Follows exposed/unexposed groups over time | Prospective or retrospective, incidence data |
| **CC** | Case-Control | Compares cases to controls retrospectively | Odds ratios, rare outcomes |
| **CSS** | Cross-Sectional | Snapshot at one time point | Prevalence data, no temporality |
| **Nested** | Nested Case-Control | Case-control within a defined cohort | Reduced selection bias vs standard CC |

### Observational — Descriptive
| Code | Design | Definition | Key Features |
|------|--------|-----------|-------------|
| **CS** | Case Series | Multiple cases, no comparison group | Hypothesis-generating only |
| **CR** | Case Report | Single case | Lowest evidence level |
| **Eco** | Ecological | Population-level data | Ecological fallacy risk |

### Secondary Research
| Code | Design | Definition | Key Features |
|------|--------|-----------|-------------|
| **SR** | Systematic Review | Explicit methodology, comprehensive search | PRISMA-compliant |
| **MA** | Meta-Analysis | Statistical pooling of primary studies | Effect sizes, heterogeneity, forest plots |
| **NMA** | Network Meta-Analysis | Indirect comparisons across interventions | Mixed-treatment comparisons |
| **NR** | Narrative Review | Non-systematic expert review | Background only — not primary evidence |

### Other
| Code | Design | Definition |
|------|--------|-----------|
| **Guide** | Clinical Practice Guideline | Evidence-based recommendations |
| **Proto** | Study Protocol | Published protocol for planned study |
| **Reg** | Registry Record | Trial registration entry (e.g., ClinicalTrials.gov) |

---

## Evidence Hierarchy (for inclusion decisions)

```
Level 1: SR/MA of RCTs → highest quality for intervention questions
Level 2: Individual RCTs
Level 3: SR/MA of observational studies
Level 4: Cohort studies
Level 5: Case-control studies
Level 6: Cross-sectional studies
Level 7: Case series/reports
Level 8: Expert opinion/narrative reviews
```

---

## Study Design Filter (for search strategies)

When searching, apply validated filters:

**RCT filter (Cochrane highly sensitive)**:
```
(randomized controlled trial[pt] OR controlled clinical trial[pt] OR 
 randomized[tiab] OR placebo[tiab] OR randomly[tiab] OR trial[tiab] OR groups[tiab])
NOT (animals[mh] NOT humans[mh])
```

**Observational filter**:
```
(cohort[tiab] OR case-control[tiab] OR cross-sectional[tiab] OR 
 longitudinal[tiab] OR prospective[tiab] OR retrospective[tiab] OR 
 observational[tiab] OR follow-up[tiab])
```

---

## Quality Assessment Mapping

| Study Design | Recommended RoB Tool |
|-------------|---------------------|
| RCT | Cochrane RoB 2 |
| Cluster RCT | Cochrane RoB 2 (cluster variant) |
| Non-randomized intervention | ROBINS-I |
| Cohort | ROBINS-I or Newcastle-Ottawa Scale |
| Case-Control | Newcastle-Ottawa Scale |
| Cross-Sectional | JBI Checklist or adapted NOS |
| Case Series | JBI Checklist |
| Systematic Review | AMSTAR 2 or ROBIS |
