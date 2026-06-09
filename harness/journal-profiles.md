# Journal Profiles — Format Requirements

> **用途**: Agent 8 Stage 3 合规检查的目标期刊格式参数
> **更新**: 新期刊投稿时追加

---

## Pediatric Research (Springer Nature)

| Parameter | Requirement |
|-----------|------------|
| **Running title** | ≤50 characters |
| **Abstract** | Unstructured, ≤200 words |
| **Word limit** | No strict limit for reviews; typically 4,000–8,000 words |
| **Reference format** | Vancouver (numbered) |
| **Reference limit** | No strict limit |
| **Figures/Tables** | Separate files or embedded; ≤8 combined typically |
| **AI disclosure** | Required — Springer Nature policy: disclose in Methods or Acknowledgements |
| **Author Contributions** | CRediT taxonomy |
| **Data Availability** | Required |
| **Impact Statement** | Not typically required; check current guidelines |
| **PRISMA** | Required for systematic reviews; not for narrative reviews |
| **PROSPERO registration** | Not required for narrative reviews |

---

## JAMA Pediatrics

| Parameter | Requirement |
|-----------|------------|
| **Running title** | ≤60 characters |
| **Abstract** | Structured (Importance, Objective, Design, Results, Conclusions), ≤350 words |
| **Word limit** | 3,000–5,000 words for reviews |
| **Reference format** | Vancouver (numbered) |
| **Reference limit** | Typically ≤70 |
| **AI disclosure** | Required — JAMA policy: must disclose in Methods and Acknowledgements |
| **Author Contributions** | Required |
| **Data Availability** | Required |

---

## Neonatology (Karger)

| Parameter | Requirement |
|-----------|------------|
| **Running title** | ≤60 characters |
| **Abstract** | Unstructured preferred, ≤250 words |
| **Word limit** | Review: typically 5,000–8,000 words |
| **Reference format** | Vancouver (numbered) |
| **Reference limit** | No strict limit |
| **AI disclosure** | Recommended — check current Karger policy |

---

## Archives of Disease in Childhood - Fetal and Neonatal Edition (BMJ)

| Parameter | Requirement |
|-----------|------------|
| **Running title** | ≤50 characters |
| **Abstract** | Unstructured, ≤250 words |
| **Word limit** | Review: typically 3,000–5,000 words |
| **Reference format** | Vancouver (numbered) |
| **Reference limit** | ≤60 |
| **AI disclosure** | Required — BMJ policy: disclose in Methods |
| **PRISMA** | Required for systematic reviews |

---

## Seminars in Perinatology (Elsevier)

| Parameter | Requirement |
|-----------|------------|
| **Running title** | ≤50 characters |
| **Abstract** | Unstructured, ≤200 words |
| **Word limit** | Review: 4,000–6,000 words (invited reviews) |
| **Reference format** | Vancouver (numbered) |
| **Reference limit** | Typically ≤75 |
| **AI disclosure** | Recommended |

---

## Journal of Perinatology (Springer Nature)

| Parameter | Requirement |
|-----------|------------|
| **Running title** | ≤50 characters |
| **Abstract** | Unstructured, ≤250 words |
| **Word limit** | Review: typically 4,000–6,000 words |
| **Reference format** | Vancouver (numbered) |
| **Reference limit** | No strict limit |
| **AI disclosure** | Required — Springer Nature policy |

---

## General Compliance Rules (All Journals)

| Rule | Detection Method |
|------|-----------------|
| Author Contributions completed | Scan for `[To be completed]`, `[TBD]` |
| Funding statement complete | Scan for `[To be completed]`, empty section |
| No duplicate words (typos) | Regex: `\b(\w+),\s+\1\b` |
| No HTML comments | Regex: `<!--.*?-->` |
| Figures referenced in text exist as files | Cross-check `Figure N` in text vs files in figures directory |
| Reference numbers sequential | Verify `[N]` references are consecutive and unique |
