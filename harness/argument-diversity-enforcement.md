# Argument Diversity Enforcement

> **用途**: Agent 7 Step 4 (合成视角扫描) + Agent 4 Post-Pass 3 (审校验证)
> **原则**: "优雅空洞"——同一论证动作以不同措辞重复——可被精确检测和被强制转换

---

## Argument Type Taxonomy

| Type | Definition | Linguistic Markers | Function |
|------|-----------|-------------------|----------|
| **A: Gap-Statement** ("优雅空洞") | "Evidence is limited → more research needed" | "Although/While/Despite [evidence], [limitation], further research is needed" | Identifies a gap but adds no new information beyond the gap itself |
| **B: Data-Based** | Conclusion driven by specific numbers | Specific effect sizes, ARR/NNT, statistical comparisons | Grounds abstraction in quantifiable fact |
| **C: Mechanism-Based** | Uses pathophysiology to explain or predict | "Because [pathway], [intervention] may [effect]" | Connects observation to biological understanding |
| **D: Comparative** | Contrasts two interventions, eras, or populations | Structure: "While A does X, B does Y. This difference matters because..." | Generates insight through juxtaposition |
| **E: Clinical-Consequence** | Translates finding to patient impact | "For the clinician/patient, this means..." | Answers "so what?" at the human level |
| **F: Historical-Trajectory** | Shows how understanding evolved over time | "Since [era], our understanding has shifted from X to Y..." | Contextualizes current evidence within intellectual history |

---

## Pattern A Detection Rule (Executable)

```
Pattern: (Although|While|Despite)
         .{0,100} (evidence|data|studies|literature|trial|RCT)
         .{0,100} (limited|incomplete|scarce|lacking|absent|insufficient|few|sparse)
         .{0,200} (more|further|additional)
         .{0,50} (research|studies|trials|data|follow-up|investigation)
         .{0,50} (needed|required|necessary|warranted|urgently|essential)
```

**Classification**: Any sentence matching this pattern AND not containing a specific, actionable research recommendation (e.g., "A phase III trial comparing X vs Y with follow-up to age 10") is Pattern A.

---

## Required Argument Type Distribution

| Argument Type | Minimum Per Major Section | Minimum Per Manuscript |
|--------------|--------------------------|----------------------|
| A: Gap-Statement | 0 | ≤2 |
| B: Data-Based | ≥1 | ≥5 |
| C: Mechanism-Based | ≥1 | ≥3 |
| D: Comparative | ≥1 | ≥3 |
| E: Clinical-Consequence | ≥1 | ≥2 |
| F: Historical-Trajectory | — | ≥1 |

---

## Handling Pattern A Overuse

| Count | Action |
|-------|--------|
| 0–2 | ✅ PASS — 可接受 |
| 3–4 | ⚠️ WARNING — 第 3+ 次必须替换为 B/C/D/E/F 中的一种 |
| ≥5 | ❌ MUST FIX — 第 3+ 次强制转换。无法转换的，合并为一个集中的 "Limitations of the Evidence Base" 段落 |

### Replacement Strategy

对每个需替换的 Pattern A 实例:
1. 识别该处具体在讨论什么证据空白
2. 从替代类型中选择最合适的一个:
   - 可否用具体数字替换？ → B (Data-Based)
   - 可否用病理生理解释？ → C (Mechanism-Based)
   - 可否与其他干预对比？ → D (Comparative)
   - 可否描述临床后果？ → E (Clinical-Consequence)
   - 可否追溯历史演变？ → F (Historical-Trajectory)
3. 如果都无法做到 → 删除该句，将其空白描述合并到 "Limitations" 段落

### Consolidation Rule

如果全文有 ≥5 个独立的 Pattern A 实例:
- 收集所有具体的空白描述
- 在 Discussion 末尾生成一个 "**Evidence Gaps Summary**" 表
- 各章节删除各自的 Pattern A，替换为: "Specific evidence gaps for [this intervention] are summarized in Section [X]."
- 目标: 空白被承认但不被重复

---

## Argument Diversity Report Format

`harness/argument-diversity-report.md`:

```markdown
# Argument Diversity Report — [Manuscript] — YYYY-MM-DD

## Pattern Distribution
| Type | Count | % |
|------|-------|---|
| A: Gap-Statement | N | X% |
| B: Data-Based | N | X% |
| C: Mechanism-Based | N | X% |
| D: Comparative | N | X% |
| E: Clinical-Consequence | N | X% |
| F: Historical-Trajectory | N | X% |

## Pattern A Instances
| # | Location | Full Match | Status |
|---|---------|-----------|--------|
| 1 | §X, ¶Y | "...limited, more research..." | ✅ KEEP |
| 2 | §X, ¶Y | "...absent, further studies..." | ✅ KEEP |
| 3 | §X, ¶Y | "...scarce, more data needed..." | ⚠️ REPLACE → Type D |
| 4 | ... | ... | ⚠️ REPLACE → Type B |

## Section-Level Diversity Check
| Section | B | C | D | E | F | Meets Minimum? |
|---------|---|---|---|---|---|---------------|
| §2 | ✅ | ✅ | ❌ MISSING | ✅ | — | ❌ |
| §3 | ✅ | ✅ | ✅ | ❌ MISSING | — | ❌ |
...

## MUST FIX Items
[List of specific conversion recommendations]
```
