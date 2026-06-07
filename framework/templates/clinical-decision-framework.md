# Clinical Decision Framework Template

> **用途**: Agent 7 Step 3 — 从稿件中提取关键决策节点，生成条件分支决策框架
> **原则**: 基于文献中没有超出边界的内容。所有不确定性显式标注。

---

## Framework Structure

### 1. Decision Nodes

对每个关键临床决策点：

| Field | Description |
|-------|-------------|
| **Decision** | 临床医生面对的具体选择 |
| **Context** | 做出该决策的临床情境 (胎龄、临床状态、可用资源) |
| **Options** | 可用干预选项列表 |
| **Known** | 每个选项的已知证据 (短期 + 远期) |
| **Unknown** | 每个选项的未知 (证据空白) |
| **Provisional Guidance** | 基于现有最佳证据的暂定指导 |
| **Uncertainty Level** | HIGH / MODERATE / LOW |

---

### 2. Decision Node Template

```markdown
### Decision Node [N]: [Decision Name]

**Clinical Context**: [Population, clinical state, setting]

**Available Options**:
| Option | Short-term Evidence | Long-term Evidence | Gap Grade | Key Unknown |
|--------|-------------------|-------------------|-----------|-------------|
| A | [summary + citation] | [summary or "none"] | G[0-4] | [specific unknown] |
| B | [summary + citation] | [summary or "none"] | G[0-4] | [specific unknown] |

**Provisional Guidance** (Uncertainty Level: [HIGH/MODERATE/LOW]):
- In the current state of evidence, clinicians may consider [Option X] when [conditions], and [Option Y] when [different conditions].
- **[IMPORTANT]**: This guidance is provisional. It is based on the best available evidence as of [date]. It should NOT be interpreted as a clinical practice guideline. It reflects the synthesis of published literature and does not substitute for clinical judgment.

**Patient/Family Communication Points**:
- When discussing this decision with families, clinicians might explain that [plain-language summary of what is known and unknown].
```

---

### 3. Mandatory Rules

#### R1: Evidence Bounds
- 指南中的每个 if-then 分支必须对应文献中存在的最少证据
- 如果某分支路径无文献支撑 → 必须显式说明: "No direct evidence exists for this specific scenario. The suggestion is extrapolated from [source population/context] and should be applied with caution."

#### R2: Uncertainty Language
| 不确定性等级 | 语言 | 示例 |
|------------|------|------|
| HIGH | "may consider," "might guide," "could inform," "is not yet established" | "Clinicians may consider LISA for spontaneously breathing preterm infants, though long-term safety data are absent." |
| MODERATE | "evidence suggests," "currently available data indicate," "appears to" | "Available evidence suggests VTV over PLV for reducing BPD, though whether this translates to improved adult lung function is unstudied." |
| LOW | "established evidence supports," "guidelines recommend," "should" (仅当有 strong guideline recommendation 且有高级别证据) | "Established evidence supports ACS administration to women at risk of preterm birth between 24-34 weeks." |

#### R3: No False Certainty
- ❌ 不要将不同选项的"证据缺失"等同于"选项无差异"
- ❌ 不要暗示选择 A 比选 B 更安全，除非有直接的安全性比较数据
- ❌ 不要用一般性病理生理学原理代替特定干预的数据

#### R4: LMIC Applicability Note
- 对每个 Decision Node，如果选项涉及资源/设备/培训依赖 → 添加 LMIC 注释:
  - "In settings without access to [resource], the available options are [limited set]. The evidence gaps described above are magnified in this context because [reasons]."

---

### 4. Decision Node Identification Heuristics

从稿件中识别决策节点：

1. 扫描每个干预在稿件中被讨论为"选项"的段落——即临床医生需要选择的情境
2. 如果一个干预段落的开篇是类似 "When managing..." / "The choice of..." / "Clinicians must decide..." 的措辞 → 这是一个决策节点
3. 如果一个段落讨论了 ≥2 个替代方案并对它们设置了相对关系 → 这是一个决策节点
4. 如果一个段落的结论是指出"数据缺失意味着医生必须在没有充分证据的情况下做出选择" → 这是一个**关键**决策节点

---

### 5. Framework Placement in Manuscript

生成的决策框架可以插入以下位置：
- **方案 A (推荐)**: 在每个主要干预章节末尾，作为一个 150-250 字的 "Clinical Decision Context" 框
- **方案 B**: 在 Discussion 中作为一个集中的 "Clinical Decision Framework" 独立小节
- 由 Agent 7 根据稿件结构和长度决定（长稿 → 方案 A；短稿 → 方案 B）
