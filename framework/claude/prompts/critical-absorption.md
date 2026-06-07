# Critical Absorption Rules (Enforced Cochrane Skepticism)

> **用途**: Agent 4 Post-Pass 4 — 对高度依赖的系统综述信源进行强制批判
> **原则**: 学术写作的本质是对信源的批判性对话。引用不能替代思考。

---

## Mandatory Critical Checks

对在稿件中被引用 ≥2 次的每个 Cochrane 综述/系统综述，逐条执行以下检查：

### Check 1: GRADE Certainty Reflection

| Issue | Detection | Required Action |
|-------|-----------|----------------|
| Manuscript states finding as definitive but GRADE is "moderate" or "low" | Compare manuscript language vs Cochrane GRADE rating | Add: "(GRADE [rating] certainty; the true effect may differ substantially from the point estimate)" |
| Manuscript states finding as definitive but GRADE is "very low" | Compare | Add strong caveat: "(GRADE very low certainty; the evidence is insufficient to draw firm conclusions)" |
| GRADE rating not mentioned in manuscript when it exists in the review | Text search for "GRADE", "certainty", "quality of evidence" | Insert GRADE rating at first mention of each Cochrane finding |

### Check 2: Type II Error Risk (Wide Confidence Intervals)

| Issue | Detection | Required Action |
|-------|-----------|----------------|
| "No significant difference" with wide CI that doesn't exclude clinically important effect | Check CI bounds vs MCID (minimal clinically important difference) | Add: "(though the confidence interval [range] does not exclude a clinically meaningful effect; this 'absence of evidence' should not be interpreted as 'evidence of absence')" |
| "No significant difference" but sample size is small (<200 total) | Check Cochrane Characteristics of included studies for total N | Add: "(based on [N] participants; the study may have been underpowered to detect clinically important differences)" |

### Check 3: Trial Overlap Between Reviews

| Issue | Detection | Required Action |
|-------|-----------|----------------|
| Two cited Cochrane reviews share ≥30% of included trials | Compare included trial lists (from Cochrane "Characteristics of included studies") | Add: "[Review A] and [Review B] share [N] of [M] included trials; their conclusions are not fully independent." |
| Manuscript treats overlapping reviews as independent confirmatory evidence | Detection: consecutive sentences cite different reviews for same claim | Add independence caveat |

### Check 4: Review Currency

| Issue | Detection | Required Action |
|-------|-----------|----------------|
| Cited Cochrane review has search date >5 years old | Check review Methods section for "Search date" or "Date of search" | Add: "(last search: [date]; newer evidence may alter these conclusions)" |
| A newer version of the same Cochrane review exists | Check Cochrane Library for "New search for studies" or updated versions | Flag: ⚠️ OUTDATED_REVIEW — suggest citing newer version |

### Check 5: Population Applicability

| Issue | Detection | Required Action |
|-------|-----------|----------------|
| Review includes trials from era with substantially different standard of care | Compare trial enrollment years vs current practice era | Add: "(the included trials date from [era], when standard care differed; the applicability of these findings to contemporary practice requires interpretation)" |
| Review population is narrower than manuscript's claimed scope | Compare review PICO vs manuscript topic | Add limitation: "This review focused on [narrower population]; its generalizability to [broader population discussed in manuscript] is uncertain." |

---

## Cochrane Concentration Detection

### Calculation
```
Cochrane_concentration = (number of Cochrane citations) / (total citations) × 100%
```

### Thresholds

| Concentration | Label | Required Response |
|--------------|-------|------------------|
| <30% | ✅ Normal | No action required |
| 30–60% | ⚠️ ELEVATED | Verify at least 40% of non-Cochrane citations are primary research (not other reviews) |
| >60% | ⚠️ COCHRANE_MONOCULTURE | Must add ≥3 critical caveats about Cochrane review limitations + must cite ≥5 primary research papers |

---

## Critical Caveat Insertion Rules

### Per-Review Caveat Limit
- 每篇 Cochrane 综述 1-3 条批判性限定语（不是为加而加——只在实际识别到局限性时添加）

### Placement
- 第一条提到该 Cochrane 综述时 → 立即插入 GRADE/时效限定语
- "无显著差异"声明处 → 插入 CI 宽度/检验效能限定语
- 如果有试验重叠 → 在提到第二篇综述时插入重叠限定语

### Format
批判性限定语的语气是学术对话，不是攻击:
> **Good**: "This conclusion is based on GRADE moderate-certainty evidence [citation]; the true effect may change with further research."
> **Bad**: "This Cochrane review is flawed and cannot be trusted."

---

## Critical Absorption Report Format

Agent 4 Post-Pass 4 完成后，在审校报告统计区追加:

```markdown
### Critical Absorption Statistics
- Cochrane reviews cited ≥2 times: N
- Critical caveats inserted: N
  - GRADE certainty caveats: N
  - CI width / Type II error caveats: N
  - Trial overlap caveats: N
  - Currency caveats: N
  - Population applicability caveats: N
- Cochrane concentration: XX% ([status])
- No Cochrane reviews cited ≥2 times without critical engagement: ✅ / ❌
```
