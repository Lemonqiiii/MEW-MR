# Argument Diversity Report — NRDS Life-Course Review — 2026-06-06

> **Built by**: Agent 7 Step 4
> **Principle**: Pattern A ("推断不是证据→需要更多研究") detected, counted, and flagged for conversion

---

## Pattern A Detection

**Detection Rule** (simplified for manual scan):
Match sentences containing ALL of:
- Evidence limitation word (limited, incomplete, scarce, lacking, absent, insufficient)
- "More/further research/studies/data/follow-up is needed/required/warranted"
- Without a specific, actionable research recommendation

### Pattern A Instances Found: **11**

| # | Location | Text Snippet | Status |
|---|---------|-------------|--------|
| 1 | §2.5 | "the studies designed to detect those consequences have not been conducted" | ⚠️ REPLACE → Type E (Clinical-Consequence) |
| 2 | §3.4 | "Whether the cerebral palsy signal... represents the full extent of neurological harm... cannot be determined" | ⚠️ REPLACE → Type C (Mechanism) |
| 3 | §4.1 | "inference is not evidence, and the chain of causation... has not been empirically tested" | ⚠️ REPLACE → Type D (Comparative) |
| 4 | §4.4 | "Without follow-up that extends into school age and beyond, we cannot know..." | ⚠️ REPLACE → Type E (Clinical-Consequence) |
| 5 | §5.1 | "plausibility, again, is not evidence" | ⚠️ REPLACE → Type D (Comparative) |
| 6 | §5.2 | "the earliest LISA-treated cohort is now approaching adolescence — and we know nothing" | ✅ KEEP (specific, vivid framing — not generic gap-statement) |
| 7 | §5.3 | "The enthusiasm for combination therapy is understandable. The absence of safety data... is concerning." | ⚠️ REPLACE → Type C (Mechanism) |
| 8 | §6.2 | "We do not know whether the oxygen saturation maintained during the first weeks of life influences the trajectory of lung function at age 15" | ⚠️ REPLACE → Type E (Clinical-Consequence) |
| 9 | §8.3 | "the neurodevelopmental consequences... cannot be quantified from existing data" | ⚠️ REPLACE → Type D (Comparative) |
| 10 | §9.1 | "the tools we use to measure quality of life... were not designed for this population" | ✅ KEEP (specific methodological critique — not generic gap-statement) |
| 11 | §11 | "the distinction between 'probable' and 'proven' matters" | ⚠️ REPLACE → Type B (Data-Based) |

### Count Summary
- Total Pattern A: **11**
- KEEP (acceptable specificity): 2 (#6, #10)
- MUST REPLACE: **9**

---

## Recommended Argument Type Distribution (vs Actual)

| Type | Required Min | Estimated Actual | Status |
|------|-------------|-----------------|--------|
| A: Gap-Statement | ≤2 | 11 → target 2 | ❌ OVERUSE |
| B: Data-Based | ≥5 | ~3 | ⚠️ BELOW MINIMUM |
| C: Mechanism-Based | ≥3 | ~2 | ⚠️ BELOW MINIMUM |
| D: Comparative | ≥3 | ~1 | ⚠️ BELOW MINIMUM |
| E: Clinical-Consequence | ≥2 | ~1 | ⚠️ BELOW MINIMUM |
| F: Historical-Trajectory | ≥1 | ~1 | ✅ |

---

## Replacement Suggestions

| Instance | Replace With | Suggested Conversion |
|----------|-------------|---------------------|
| #1 (§2.5) | Type E (Clinical-Consequence) | "If a clinician in 2026 administers ACS to a woman at 28 weeks, she is making a decision whose consequences for that child at age 50 are completely unknown — not because the effect doesn't exist, but because the studies were never funded." |
| #3 (§4.1) | Type D (Comparative) | "The evidence for VTV's short-term superiority over PLV is as strong as any in neonatology — yet the evidence for whether this choice matters at age 10 is as absent as LISA's entire follow-up literature. The contrast between short-term certainty and long-term ignorance is the central finding of this review." |
| #5 (§5.1) | Type D (Comparative) | "Compare: ACS has follow-up on 1.2 million children. Surfactant preparation choice has zero follow-up beyond discharge. Both are decisions neonatologists make every day. One is made with data; the other is made in the dark." |
| #11 (§11) | Type B (Data-Based) | "Of 590 papers in our systematic search, 8 addressed quality of life. Of 35 cited references, none reported adult pulmonary function. These are not gaps — they are a void." |

---

## Section-Level Diversity Check

| Section | B (Data) | C (Mechanism) | D (Comparative) | E (Clinical) | F (Historical) | Meets Minimum? |
|---------|----------|---------------|-----------------|-------------|----------------|---------------|
| §2 ACS | ✅ | ❌ MISSING | ❌ MISSING | ✅ | ✅ | ❌ |
| §3 Postnatal CS | ✅ | ✅ | ❌ MISSING | ❌ MISSING | — | ❌ |
| §4 Ventilation | ✅ | ✅ | ✅ | ❌ MISSING | — | ⚠️ |
| §5 Surfactant | ✅ | ❌ MISSING | ❌ MISSING | ❌ MISSING | — | ❌ |
| §6 Oxygen | ✅ | ✅ | ❌ MISSING | ❌ MISSING | — | ❌ |
| §7 BPD | ✅ | ✅ | ✅ | ❌ MISSING | ✅ | ⚠️ |
| §8 Neuro | ✅ | ❌ MISSING | ❌ MISSING | ❌ MISSING | — | ❌ |
| §9 QoL | ✅ | ❌ MISSING | ❌ MISSING | ❌ MISSING | — | ❌ |
| §10 Gaps | ❌ MISSING | ❌ MISSING | ❌ MISSING | ❌ MISSING | — | ❌ |
| §11 Conclusions | ❌ MISSING | ❌ MISSING | ❌ MISSING | ❌ MISSING | — | ❌ |

**Overall**: 0/10 sections meet full diversity minimum. This is a structural deficiency requiring substantive revision.

---

## MUST FIX Items (Consolidated)

1. **Reduce Pattern A from 11 → 2**: Keep #6 and #10; convert 9 others to B/C/D/E/F types
2. **Add ≥2 more Data-Based arguments (Type B)**: Convert Pattern A instances using ARR/NNT data
3. **Add ≥1 more Mechanism-Based argument (Type C)**: §2 and §5 currently missing
4. **Add ≥2 more Comparative arguments (Type D)**: Leverage cross-intervention matrix findings
5. **Add ≥1 more Clinical-Consequence argument (Type E)**: §3, §4, §5, §6 currently missing
6. **§10 and §11 critically under-diversified**: Conclusions must include data-based closing argument
