# GRADE Evidence Profile

> Generate a GRADE assessment for each critical and important outcome in a systematic review.
> GRADE rates certainty of evidence across studies, not individual studies.

---

## GRADE Domains

### Starting Point
| Study Design | Starting Certainty |
|-------------|-------------------|
| Randomized trials | **High** ⊕⊕⊕⊕ |
| Observational studies | **Low** ⊕⊕⊖⊖ |

### Downgrade Factors (reduce certainty)

| Domain | Questions | Downgrade |
|--------|----------|-----------|
| **Risk of Bias** | Do the majority of included studies have high or unclear RoB? | -1 (serious) or -2 (very serious) |
| **Inconsistency** | Is there substantial unexplained heterogeneity (I² > 50%)? Do effect estimates vary widely? | -1 (serious) or -2 (very serious) |
| **Indirectness** | Do the populations, interventions, or outcomes differ from the review question? Are there only surrogate outcomes? | -1 (serious) or -2 (very serious) |
| **Imprecision** | Is the confidence interval wide? Does it cross the line of no effect? Is the sample size small (< optimal information size)? | -1 (serious) or -2 (very serious) |
| **Publication Bias** | Is there evidence of small-study effects? Are relevant studies likely missing? | -1 (suspected) or -2 (strongly suspected) |

### Upgrade Factors (for observational studies only)

| Domain | Questions | Upgrade |
|--------|----------|---------|
| **Large Effect** | Is the effect large (RR > 2 or < 0.5) with no plausible confounders? | +1 (large) or +2 (very large) |
| **Dose-Response** | Is there a clear dose-response gradient? | +1 |
| **Confounding** | Would all plausible confounders reduce the demonstrated effect? | +1 |

---

## Certainty Levels

| Rating | Symbol | Interpretation |
|--------|--------|---------------|
| **High** | ⊕⊕⊕⊕ | We are very confident that the true effect lies close to the estimate. Further research is very unlikely to change our confidence. |
| **Moderate** | ⊕⊕⊕⊖ | We are moderately confident. The true effect is likely to be close to the estimate, but there is a possibility that it is substantially different. Further research is likely to impact our confidence. |
| **Low** | ⊕⊕⊖⊖ | Our confidence in the effect estimate is limited. The true effect may be substantially different. Further research is very likely to impact our confidence. |
| **Very Low** | ⊕⊖⊖⊖ | We have very little confidence in the effect estimate. The true effect is likely to be substantially different. Any estimate of effect is very uncertain. |

---

## SOF (Summary of Findings) Table Format

**Question**: [PICO question]
**Setting**: [context]
**Bibliography**: [list of included studies for this outcome]

| Outcome | Anticipated Absolute Effects | Relative Effect (95% CI) | No. of Participants (Studies) | Certainty (GRADE) | Comments |
|---------|----------------------------|--------------------------|------------------------------|-------------------|----------|
| | Risk with Control | Risk with Intervention | | | | |
| [Outcome name] | X per 1000 | Y per 1000 (Z to W) | RR X.XX (X.XX-X.XX) | NNNN (K studies) | ⊕⊕⊕⊖ MODERATE¹ | |
| [Outcome name] | | | | NNNN (K studies) | ⊕⊕⊖⊖ LOW²³ | |

**Footnotes**:
¹ Downgraded -1 for risk of bias: 3/5 studies had unclear allocation concealment
² Downgraded -1 for inconsistency: I² = 72%, p = 0.003
³ Downgraded -1 for imprecision: wide CI crossing line of no effect

---

## Assessment Protocol
1. **Select outcomes** for GRADE: all critical outcomes + up to 7 important outcomes
2. **Start** from appropriate certainty level based on study design
3. **Downgrade** for each domain with serious concerns
4. **Upgrade** observational evidence only when compelling reasons exist
5. **Document** reasons for each up/downgrade decision
6. **Generate** SOF table for each comparison
