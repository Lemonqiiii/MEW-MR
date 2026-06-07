# Risk of Bias Assessment

> Apply to every included study in a systematic review.
> Select the appropriate tool based on study design (see `templates/paper-types/systematic-review.md`).

---

## Cochrane RoB 2 (for Randomized Trials)

### Domain 1: Bias arising from the randomization process
| Question | Judgment |
|----------|----------|
| Was the allocation sequence random? | Y / PY / PN / N / NI |
| Was the allocation sequence concealed until participants were enrolled and assigned to interventions? | Y / PY / PN / N / NI |
| Did baseline differences between intervention groups suggest a problem with the randomization process? | Y / PY / PN / N / NI |
| **Domain risk** | **Low / Some concerns / High** |

### Domain 2: Bias due to deviations from intended interventions
| Question | Judgment |
|----------|----------|
| Were participants aware of their assigned intervention during the trial? | Y / PY / PN / N / NI |
| Were carers and people delivering the interventions aware of participants' assigned intervention? | Y / PY / PN / N / NI |
| Were there deviations from the intended intervention beyond what would be expected in usual practice? | Y / PY / PN / N / NI |
| Was an appropriate analysis used to estimate the effect of assignment to intervention? | Y / PY / PN / N / NI |
| **Domain risk** | **Low / Some concerns / High** |

### Domain 3: Bias due to missing outcome data
| Question | Judgment |
|----------|----------|
| Were data for this outcome available for all, or nearly all, participants randomized? | Y / PY / PN / N / NI |
| Is there evidence that the result was not biased by missing outcome data? | Y / PY / PN / N / NI |
| **Domain risk** | **Low / Some concerns / High** |

### Domain 4: Bias in measurement of the outcome
| Question | Judgment |
|----------|----------|
| Was the method of measuring the outcome appropriate? | Y / PY / PN / N / NI |
| Could measurement of the outcome have differed between intervention groups? | Y / PY / PN / N / NI |
| Were outcome assessors aware of the intervention received by study participants? | Y / PY / PN / N / NI |
| **Domain risk** | **Low / Some concerns / High** |

### Domain 5: Bias in selection of the reported result
| Question | Judgment |
|----------|----------|
| Were the data that produced this result analyzed in accordance with a pre-specified analysis plan? | Y / PY / PN / N / NI |
| Is the numerical result likely to have been selected from multiple eligible outcome measurements or analyses? | Y / PY / PN / N / NI |
| **Domain risk** | **Low / Some concerns / High** |

### Overall Risk of Bias
- **Low**: All domains low risk
- **Some concerns**: At least one domain with some concerns, no high risk
- **High**: At least one domain high risk, or multiple domains with some concerns

---

## ROBINS-I (for Non-Randomized Intervention Studies)

| Domain | Key Questions | Judgment |
|--------|--------------|----------|
| **1. Confounding** | Were all important confounders identified and controlled? | Low / Moderate / Serious / Critical / NI |
| **2. Selection of participants** | Was selection into the study based on characteristics observed after intervention start? | |
| **3. Classification of interventions** | Were intervention groups clearly defined and recorded? | |
| **4. Deviations from intended interventions** | Were there deviations from intended interventions beyond usual practice? | |
| **5. Missing data** | Were outcome data available for all or nearly all participants? | |
| **6. Measurement of outcomes** | Were outcome measures influenced by knowledge of the intervention? | |
| **7. Selection of the reported result** | Was the reported result selected from multiple analyses? | |
| **Overall** | | **Low / Moderate / Serious / Critical / NI** |

---

## Newcastle-Ottawa Scale (for Cohort and Case-Control)

### Cohort Studies (max 9 stars)
| Category | Item | Stars |
|----------|------|-------|
| **Selection** | Representativeness of exposed cohort | * |
| | Selection of non-exposed cohort | * |
| | Ascertainment of exposure | * |
| | Demonstration outcome not present at start | * |
| **Comparability** | Comparability of cohorts (design/analysis) | ** |
| **Outcome** | Assessment of outcome | * |
| | Follow-up long enough | * |
| | Adequacy of follow-up | * |

### Rating: Good (7-9) / Fair (4-6) / Poor (≤3)

---

## Summary Table Format

Generate a RoB summary for all included studies:

| Study | Design | RoB Tool | D1 | D2 | D3 | D4 | D5 | Overall |
|-------|--------|----------|----|----|----|----|----|---------|
| Author Year | RCT | RoB 2 | Low | Low | Concerns | Low | Low | **Some concerns** |
| Author Year | Cohort | NOS | — | — | — | — | — | **7/9 (Good)** |

### Study-Level Judgment Rules
- If overall RoB is **High** → flag `HIGH_RISK`, consider sensitivity analysis excluding this study
- If overall RoB is **Some concerns** → flag `SOME_CONCERNS`, note in limitations
- Do NOT exclude high-RoB studies without reporting them (PRISMA requires accounting)
