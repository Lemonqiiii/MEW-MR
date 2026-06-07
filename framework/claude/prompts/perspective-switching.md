# Perspective-Switching Rules

> **用途**: Agent 4 Pre-Pass 1 — 在稿件自然锚点插入多视角锚点段落
> **原则**: 每个视角 2-4 句，基于稿件数据，不发明场景

---

## Mandatory Perspective Switches

| ID | Perspective | Trigger Location | Depth | Purpose |
|----|------------|-----------------|-------|---------|
| **P1** | Front-line Clinician | 每个主要干预的证据总结之后 | 2-3 句 | "What does this mean at 3 AM in the NICU?" |
| **P2** | Family / Caregiver | 神经发育结局数据之后 | 2-3 句 | "For parents asking 'What will my child's life be like?'" |
| **P3** | LMIC Clinician | 首次提到资源密集干预时 | 2-3 句 | "In settings without [resource]..." |
| **P4** | Policy Maker / Funder | Discussion 中，Future Directions 之前 | 3-4 句 | "The investment case for closing this evidence gap" |
| **P5** | Researcher | Knowledge Gaps 章节 | 3-4 句 | "Methodological priorities for the next generation of studies" |

---

## Per-Perspective Instructions

### P1: Front-line Clinician

**Trigger**: 每个主要干预章节的证据总结段落后（通常在章节倒数第二段）
**Format**: 
> **Clinical Perspective**: [What the evidence means for bedside decisions. What the clinician CAN act on. What decisions remain in uncertainty.]
**Example**:
> **Clinical Perspective**: For the clinician managing a 26-week infant with worsening respiratory status, the evidence supports volume-targeted ventilation over pressure-limited modes to reduce BPD (NNT ≈ [X]). However, whether this choice affects the child's lung function at age 10 — or their quality of life at age 30 — is unknown. The decision today is evidence-based; its lifelong consequences are uncharted.

### P2: Family / Caregiver

**Trigger**: 神经发育/长期结局数据段落后
**Format**: 
> **Family Context**: [Plain-language summary of what the evidence means for families. What parents can reasonably expect. What remains uncertain.]
**Example**:
> **Family Context**: For parents of an extremely preterm infant, the available evidence provides partial reassurance: a single course of antenatal corticosteroids does not appear to increase the risk of cerebral palsy or cognitive impairment in childhood. However, data on how these children function in school, their social relationships, and their quality of life as adults are largely absent — questions that matter deeply to families making decisions in the NICU today.

### P3: LMIC Clinician

**Trigger**: 首次提到资源密集干预（设备依赖/昂贵药物/需要专业培训）
**Format**:
> **Global Health Context**: [How this evidence translates — or fails to translate — to resource-limited settings.]
**Example**:
> **Global Health Context**: The evidence supporting LISA comes predominantly from well-resourced European NICUs with established CPAP infrastructure and experienced operators. In settings where CPAP availability is limited or surfactant costs are prohibitive, the risk-benefit calculus may differ substantially. The evidence gaps described above — already severe in high-income settings — are magnified in LMIC contexts where both the interventions and the follow-up infrastructure are scarcer.

### P4: Policy Maker / Funder

**Trigger**: Discussion 章节中，"Future Directions" 或 "Research Priorities" 小节之前
**Format**:
> **Policy Perspective**: [The investment case. What closing evidence gaps would cost vs. what inaction costs.]
**Constraint**: 不发明经济数据。如果没有成本-效果数据，坦率说明。

### P5: Researcher

**Trigger**: Knowledge Gaps 章节中的研究方法论讨论
**Format**:
> **Research Priority**: [Specific, actionable methodological recommendation. Study design. Endpoints. Population.]

---

## Insertion Rules

| Rule | Description |
|------|-------------|
| **R1: Length** | 每个视角 2-4 句，不超过 80 词 |
| **R2: Register** | 保持学术语域——临床/政策语言，不是随意语言 |
| **R3: Data Grounding** | 必须基于稿件中已存在的数据。不发明具体患者场景或统计数据 |
| **R4: Tagging** | 每条视角插入用 `<!-- PERSPECTIVE:P[N] -->` 标记 |
| **R5: Placement** | 在自然段落边界插入——不打断句子或段落流 |
| **R6: Skipping** | 如果Trigger Positions没有足够数据来支撑一个视角 → 跳过该位置，在报告中记录原因 |

---

## Quality Check

Agent 4 Pre-Pass 1 完成后:
- 计数: N 个视角尝试 / N 个Trigger Positions = 覆盖百分比
- 目标: ≥80%
- 如果 <80% → 报告哪些Trigger Positions无法满足、原因是什么
