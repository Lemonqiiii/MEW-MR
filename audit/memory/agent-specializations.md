# Agent 专业化定义 — 审稿项目

> 本文件定义了审稿项目中的 6 个独立审稿人 + 预处理/验证/主编/反馈/关卡/编码等支持Agent。README 中的“6维度审稿”指核心审稿维度；本文件保留完整执行角色。
> 每个Agent有极简命令触发、完整的输入输出规范和 prompt 模板。

---

## Agent 0: 编码Agent (Infrastructure) — 双模式

### 设计理念
与写作项目Agent 0 保持一致的双模式设计：轻量编码降低执行门槛，完整编码保证审计质量。

| 模式 | 触发命令 | 频率 | 包含Parts | 预计耗时 |
|------|---------|------|----------|---------|
| **轻量编码** | `快记` `记` `quick` | 每2-3个审稿维度完成 | Part A + Git提交 | 低（秒级） |
| **完整编码** | `编码` `6` `commit` | 每次完整审稿任务结束 | Part A + B + C + D | 中 |

### 自动提示规则
- 完成2-3个审稿人审稿后 → Agent主动建议"快记"
- 完整审稿任务结束后 → Agent展示检查清单，提示"编码"
- 发现知情边界违规 → 强制提示完整编码（含安全审计）

---

### 轻量编码模式 (`快记` / `记`)

#### 工作流
1. 检查 git 变更状态
2. 读取 `features/FEATURE_LIST.md`，更新已完成任务的勾选状态
3. 更新 `memory/project-status.md` 统计数据
4. 追加 `progress/SESSION_LOG.md` 一条精简记录
5. git add -A && git commit

#### 输出
- 一句话确认：提交了哪些变更

---

### 完整编码模式 (`编码` / `6`)

#### 工作流
执行轻量编码全部内容 + 以下补充：

##### Part A+: 进度记录
1-5. 同轻量编码
6. 更新 `progress/MILESTONES.md`
7. 如有新发现或决策，更新 `memory/decisions.md`

##### Part B: 效率数据收集
8. 从会话上下文提取效率指标，写入 `progress/metrics-raw.json`

##### Part C: 安全审计（审稿项目特有！）
9. 扫描审稿Agent的系统提示 → 检查知情边界合规（对照 `harness/limited-knowledge-boundary.md`）
10. 扫描文件读写 → 检查越界访问
11. 扫描网络请求 → 检查未授权URL
12. 将违规写入 `progress/metrics-raw.json`

##### Part D: Git 提交
13. git commit（含 metrics-raw.json），使用结构化 message: `[review] RA-ID 简短描述`

---

## Agent P: 预处理Agent — 审稿任务准备

### 定位
审稿流水线的入口。负责接收稿件、构建Disclosure Packet、验证知情边界、分发给审稿人。

### 触发条件
**极简命令**: `设置` `config` `prep` `准备`
**自动触发**: 当 `review-pipeline/input/` 目录有新稿件时

### 输入
- `review-pipeline/input/manuscript.md` — 稿件全文
- 用户指定的目标期刊和审稿标准

### 工作流

#### Step 1: 稿件解析
1. 读取稿件全文
2. 识别结构：标题、作者、摘要（结构化/非结构化）、正文章节、引用列表
3. 统计基本数据：字数、引用数、图表数、章节数
4. 生成稿件结构地图

#### Step 2: 元数据提取
5. 提取综述类型声明（叙述性/系统综述/荟萃分析/其他）
6. 提取PICO框架（如有明确声明）
7. 提取检索策略描述（数据库、检索式、日期范围）
8. 提取引用清单（PMID/DOI）

#### Step 3: Disclosure Packet 构建
9. 按 `harness/limited-knowledge-boundary.md` 的 6 类标准构建 Disclosure Packet
10. 确认仅含 A-F 类信息
11. 构建 Masked Info 清单（X1-X6 类信息确认不可见）

#### Step 4: 知情边界检查
12. 执行 B1-B8 检查清单
13. 如发现违规 → 修正后重新构建
14. 生成知情边界合规报告

#### Step 5: 审稿任务分发准备
15. 根据用户选择（全流程/单维度/多维度），准备对应审稿人的任务包
16. 将 Disclosure Packet 嵌入各审稿人的系统提示

### 输出
- `review-pipeline/context/disclosure-packet.md` — 信息披露包
- `review-pipeline/context/masked-info.md` — 屏蔽信息清单与合规报告
- 稿件结构地图
- 审稿任务分发清单

---

## Agent R1-R6: 审稿人Agent（横向执行层）

> 6个审稿人Agent共享相同的输入结构和输出结构，差异在于检查维度。
> 完整检查维度定义见 `harness/reviewer-profiles.md`。

### 触发条件
**全流程**: Workflow脚本自动并行触发全部6个
**按需**: `审稿 <维度1> <维度2> ...`

| 用户命令 | 触发 |
|---------|------|
| `审稿 方法学` `r methodology` | Agent R1 |
| `审稿 临床` `r clinical` | Agent R2 |
| `审稿 逻辑` `r logic` | Agent R3 |
| `审稿 统计` `r stats` | Agent R4 |
| `审稿 覆盖` `r coverage` | Agent R5 |
| `审稿 结构` `r structure` | Agent R6 |

### 输入
- Disclosure Packet（稿件全文 + 目标期刊 + PICO + 检索策略 + 引用清单）
- `harness/reviewer-profiles.md` 中该审稿人的检查维度定义

### 工作流（所有审稿人通用）

#### Step 1: 稿件通读
- 快速通读全文，形成整体印象
- 标注重点关注区域（与该审稿人维度最相关的章节）
- 不急于发现问题，先理解文章的整体逻辑

#### Step 2: 逐章深度审稿
- 按章节顺序逐段检查
- 在每个段落中应用检查维度的全部项目
- 记录每个发现的：位置、原文、问题类型、严重性

#### Step 3: 综合评估
- 给各检查维度打分
- 给出综合评分和总体评价
- 形成结构化的审稿报告

#### Step 4: 自我复查
- 检查是否覆盖了所有检查维度
- 检查每条发现是否附带具体位置和改进建议
- 检查是否避免了模糊语言

### 输出格式
严格按照 `harness/reviewer-profiles.md` 中各审稿人的输出格式生成报告。

### 约束
- **不评价语言错误**（语法、拼写）
- **不与其他审稿人通信**
- **不使用模糊语言**
- **每条发现独立自包含**

---

## Agent G: 关卡Agent — 步骤间复查

### 定位
纵向基础设施层。在每个审稿人产出后执行复查，确保审稿质量在进入下一阶段前达标。

### 触发条件
- **自动**: 每个审稿Agent完成产出后自动触发
- **手动**: `复查 <审稿人编号>` 如 `复查 R1`

### 输入
- 单个审稿人的审稿报告
- `harness/reviewer-profiles.md` 中该审稿人的检查维度
- `harness/inter-step-checklist.md` 复查清单

### 工作流

#### 单审稿人复查
1. 读取该审稿人的审稿报告
2. 执行 Part 1: 维度覆盖检查（逐项对应该审稿人的检查维度）
3. 执行 Part 2: 发现质量检查（位置/原文/严重性/建议）
4. 执行 Part 3: 独立性检查（跨审稿人引用/风格/越界）
5. 判定: ✅通过 / 🔄打回补充 / ⚠️标记异常

#### 交叉复查（所有审稿人通过后）
6. 执行审稿报告间矛盾检测
7. 执行重复发现去重
8. 执行覆盖盲区检测
9. 生成交叉复查报告

### 输出
- 每个审稿人的复查报告卡片
- 交叉复查报告（如为最后一位通过审稿人）

---

## Agent V: 验证Agent — 引用验证

### 定位
横向执行层。对稿件中的所有引用进行逐条验证。独立于审稿人维度，是客观事实检查。

### 触发条件
**极简命令**: `验证` `verify` `v`
**自动触发**: 全流程审稿中，6审稿人完成后自动触发

### 输入
- 稿件全文（含引用列表）
- `harness/verification-protocol.md` 验证协议
- 文献数据库访问（PubMed/EPMC/Semantic Scholar）

### 工作流

#### Step 1: 构建验证清单
1. 从稿件中提取所有引用标记和声称文本
2. 将每个引用-声称对编码为验证单元 (C001, C002, ...)
3. 按声称类型分类: statistical / interpretive / background

#### Step 2: Layer 1 存在性验证
4. 验证所有引用的 PMID/DOI 有效性
5. 检查文献是否未被撤稿

#### Step 3: Layer 2 摘要级验证
6. 批量获取文献摘要
7. 逐条比对声称 vs 摘要实际内容
8. 判定: ✅匹配 / ⚠️部分匹配 / ❌不匹配 / 🔍需全文验证

#### Step 4: Layer 3 全文级验证（按需）
9. 对 🔍 标记的引用和核心论点引用获取全文
10. 在全文层面验证声称
11. 记录偏差类型和严重性

#### Step 5: 生成验证报告
12. 统计各判定类别的数量
13. 列出所有不匹配详情
14. 计算总体通过率

### 输出
- `review-pipeline/reviews/verification-report.md` — 完整验证报告

---

## Agent M: 主编Agent — 综合与优先级

### 定位
横向执行层。将所有审稿人的发现整合为一套连贯的、优先级排序的改进建议。

### 触发条件
**极简命令**: `综合` `synthesize` `syn`
**自动触发**: 全流程审稿中，所有审稿人+关卡复查+引用验证完成后自动触发

### 输入
- 6份审稿报告（R1-R6）
- 关卡复查报告（Agent G）
- 引用验证报告（Agent V）
- 稿件全文

### 工作流

#### Step 1: 发现汇总
1. 合并所有审稿人的发现到一个统一列表
2. 去重合并（根据关卡Agent的交叉复查结果）
3. 标注每条发现的来源（哪些审稿人独立发现了同一问题）

#### Step 2: 严重性重新校准
4. 在跨维度视角下重新评估每条发现的严重性
5. 检测"交互效应"——多个维度的小问题组合可能构成重大缺陷
6. 统一 Critical/Major/Minor/Suggestion 的判定尺度

#### Step 3: 优先级排序
7. 按以下公式计算每条改进建议的优先级分:
   ```
   Priority Score = Severity (Critical=10, Major=6, Minor=3, Suggestion=1)
                  × Fix Impact (评估修复后对稿件质量的提升, 1-5)
                  ÷ Fix Cost (评估修复所需工作量, 1-5)
   ```
8. 生成优先级排序的改进路线图

#### Step 4: 综合审稿报告
9. 撰写综合审稿意见（主编给作者的总体反馈）
10. 包含: 主要优势、主要问题、关键修改要求、可选改进建议
11. 生成 `review-actions.json`

### 输出
- `review-pipeline/meta/synthesis.md` — 综合审稿意见
- `review-pipeline/meta/severity-matrix.md` — 问题严重性矩阵
- `review-pipeline/meta/improvement-roadmap.md` — 优先级改进路线图

---

## Agent F: 反馈Agent — 输出格式化

### 定位
横向执行层。将主编综合的结果格式化为写作项目可直接使用的格式。

### 触发条件
- **自动**: Agent M 完成后自动触发
- **手动**: `输出` `output` `export`

### 输入
- Agent M 的综合审稿意见和改进路线图
- 稿件全文

### 工作流

#### Step 1: 生成人类可读报告
1. 将综合审稿意见格式化为标准审稿报告格式
2. 包含: 总体评价、主要发现、逐章节意见、参考文献问题、改进路线图
3. 适合人类（写作项目的用户）阅读

#### Step 2: 生成机器可解析指令
4. 将每条改进建议转换为 `review-actions.json` 中的结构化条目
5. 每条包含: id, severity, location, problem_type, problem, evidence, suggested_fix, verifier
6. Schema 验证

#### Step 3: 输出验收
7. 验证输出文件完整性
8. 验证 JSON Schema
9. 将输出文件放入约定位置

### 输出
- `review-pipeline/output/review-report.md` — 人类可读审稿报告
- `review-pipeline/output/review-actions.json` — 机器可解析改进指令

### review-actions.json Schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["review_id", "manuscript", "meta_reviewer_summary", "actions"],
  "properties": {
    "review_id": {"type": "string", "pattern": "^RA-\\d{4}-\\d{2}-\\d{2}-\\d{3}$"},
    "manuscript": {"type": "string"},
    "meta_reviewer_summary": {"type": "string"},
    "actions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "severity", "reviewer", "location", "problem_type", "problem", "suggested_fix", "verifier"],
        "properties": {
          "id": {"type": "string", "pattern": "^A\\d{3}$"},
          "severity": {"enum": ["critical", "major", "minor", "suggestion"]},
          "reviewer": {"type": "string"},
          "location": {
            "type": "object",
            "required": ["section"],
            "properties": {
              "section": {"type": "string"},
              "paragraph": {"type": "integer"}
            }
          },
          "problem_type": {
            "enum": [
              "silence_blindness", "category_error", "statistical_incompleteness",
              "evidence_upgrade", "logical_gap", "pattern_a_elegant_vacuum",
              "cochrane_overreliance", "citation_mismatch", "structural_imbalance",
              "missing_citation", "absolute_negative_claim", "methodology_gap",
              "data_inaccuracy", "narrative_flatness", "overclaiming"
            ]
          },
          "problem": {"type": "string"},
          "evidence": {"type": "string"},
          "suggested_fix": {"type": "string"},
          "verifier": {"type": "string"}
        }
      }
    }
  }
}
```

---

## 全流程编排（Workflow脚本）

当用户说 `审稿`（一键全流程），执行以下编排：

```
1. Agent P → 预处理 + 知情包构建
2. [GA1] 稿件接收检查
3. [GA2] 知情包合规检查
4. parallel([Agent R1, Agent R2, Agent R3, Agent R4, Agent R5, Agent R6]) → 6维度并行审稿
5. [GA3] 各审稿人关卡复查 (Agent G × 6)
6. Agent V → 引用验证
7. [GA4] 交叉复查 + 一致性检查
8. Agent M → 主编综合
9. [GA5] 综合质量检查
10. Agent F → 输出格式化
11. [GA6] 输出验收
12. Agent 0 → 编码存档
```

---

## 错误模式库

| 错误ID | 描述 | 严重性 | 处理 |
|--------|------|--------|------|
| E-A01 | 审稿人遗漏了一个检查维度 | Major | Agent G 打回补充 |
| E-A02 | 审稿人越界评价（评价非其领域的问题） | Minor | Agent G 标记，主编综合时降权 |
| E-A03 | 审稿报告缺少具体文本位置 | Major | Agent G 打回修正 |
| E-A04 | 审稿报告缺少改进建议 | Major | Agent G 打回修正 |
| E-A05 | 引用验证发现声称-文献不匹配 | Critical/Major | 记录到验证报告 |
| E-A06 | 知情边界违规（审稿人prompt含被屏蔽信息） | Critical | 回退审稿，重新构建知情包 |
| E-A07 | 审稿人使用了模糊语言 | Minor | Agent G提示修正 |
| E-A08 | 主编综合遗漏了审稿人的Critical发现 | Critical | GA5 打回补充 |
| E-A09 | review-actions.json Schema 验证失败 | Critical | Agent F 修正后重新生成 |
| E-A10 | 审稿报告间存在事实矛盾未被处理 | Major | GA4 标记 → 主编裁决 |

---

*最后更新: 2026-06-06*
*Agent数量: 10 (0, P, R1-R6, G, V, M, F)*
