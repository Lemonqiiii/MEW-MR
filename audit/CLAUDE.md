# 医学综述审稿项目 (Medical Review Audit)

## 项目身份
- **目标**: 对医学/生物学综述论文进行多维度专业审稿，输出结构化改进建议
- **定位**: 与写作项目独立运行，写审分离（通过文件接口通信）
- **领域**: 随审稿任务变化，由稿件与 Disclosure Packet 决定
- **当前审稿任务**: 以 `memory/active-review.md` 与 `review-pipeline/input/` 为准
- **上一轮**: 无（首篇审稿）

## 交互原则

### 启动行为
**每次会话开始时**，自动执行：
1. 读取 `memory/project-status.md` — 了解当前审稿任务阶段
2. 读取 `features/FEATURE_LIST.md` — 找到第一个未完成任务
3. 读取 `memory/active-review.md` — 了解当前审稿任务的上下文
4. 用**一句话**告诉用户当前状态，然后用**简洁的选项列表**告诉用户接下来可以做什么

示例:
```
📋 审稿待命 | 当前任务: 等待 `review-pipeline/input/` 中的稿件

你可以这样说:
  审稿           → 一键全流程审稿（6审稿人并行 + 主编综合）
  审稿 方法学    → 仅方法学维度审稿
  审稿 临床      → 仅临床维度审稿
  审稿 逻辑      → 仅逻辑与论证维度审稿
  审稿 统计      → 仅统计/数据维度审稿
  审稿 覆盖      → 仅文献覆盖维度审稿
  审稿 结构      → 仅结构与叙事维度审稿
  审稿 方法学 临床 统计  → 按需多维度审稿（空格分隔）
  验证           → 逐条引用验证
  综合           → 主编综合（需先完成至少2个维度审稿）
  状态           → 查看详细项目状态
  编码           → 保存当前进度
  帮助           → 查看所有可用命令
```

### 命令极简化

| 用户说 | Agent 理解为 | 触发 |
|--------|------------|------|
| `审稿` `review` `r` | 一键完整审稿 | Workflow 全流程 |
| `审稿 方法学` `r clinical` | 单个维度审稿 | Agent R1-R6 按需 |
| `审稿 方法学 临床 统计` | 多维度并行审稿 | Agent R1-R6 按需组合 |
| `验证` `verify` `v` | 逐条引用验证 | Agent V 验证Agent |
| `综合` `synthesize` `syn` | 主编综合 | Agent M 主编Agent |
| `编码` `6` `commit` | 完整编码 | Agent 0 编码Agent |
| `快记` `记` `quick` | 轻量编码 | Agent 0 轻量模式 |
| `状态` `进度` | 查看项目状态 | 展示当前状态 |
| `帮助` `?` `help` | 显示命令 | 展示帮助 |
| `教训` `lesson` | 记录流程缺陷 | 根因分析 → 修改项目文件 |
| `设置` `config` | 配置目标期刊和审稿标准 | Agent P 预处理Agent |

### 确认规则
- 用户输入简略指令时 → **先一句话确认理解**，再执行
- 禁止在确认前执行任何写操作或网络请求
- 确认格式: `理解为: [你要做什么]。确认吗？`

## 核心规则
1. **写审分离**: 审稿项目不知道写作项目的内部决策、质量关卡结果、Agent分工和修改历史
2. **有限知情**: 审稿人仅通过 Disclosure Packet 获取必要信息（见 `harness/limited-knowledge-boundary.md`）
3. 所有审稿意见必须附带**具体文本位置**（章节+段落号+原文引用）
4. 所有批评意见必须附带**改进建议**（非仅指出问题）
5. 审稿报告使用**中文**写作（方便写作项目理解和执行），但指出的问题和引用原文使用**英文**
6. 关键决策记录到 `memory/decisions.md`
7. 审稿人之间在审稿阶段**不互相通信**（保证独立性），仅在主编综合阶段汇总

## 审稿流程

### 完整流程（一键触发 `审稿`）

```
稿件提交 → Agent P预处理 → 6审稿人并行审稿 → 关卡复查 → 
引用验证 → 主编综合 → 输出报告
```

### 按需流程（单维度触发 `审稿 <维度>`）

```
用户选择维度 → 对应Agent激活 → 单维度审稿报告 → 可选: 综合
```

## Tier 2 资源（按需加载）
- **项目状态**: `memory/project-status.md`
- **当前审稿**: `memory/active-review.md`
- **Agent定义**: `memory/agent-specializations.md` — Agent 0/M/P/R1-R6/G/V/F 完整定义
- **功能清单**: `features/FEATURE_LIST.md`
- **审稿人角色**: `harness/reviewer-profiles.md` — 6个审稿人完整角色定义
- **质量关卡**: `harness/quality-gate.md` — GA1-GA8 关卡定义

## Tier 3 资源（主动检索）
- **有限知情边界**: `harness/limited-knowledge-boundary.md` — 知情/屏蔽量化标准
- **验证协议**: `harness/verification-protocol.md` — 引用验证协议
- **步骤间复查**: `harness/inter-step-checklist.md` — 关卡Agent复查清单
- **度量定义**: `harness/metrics.md` — 审稿质量度量
- **安全策略**: `harness/safety-policy.md` — 越权检测规则
- **AI缺陷库**: `knowledge/common-ai-defects.md` — AI写作10大缺陷检测模式
- **统计模式**: `knowledge/statistical-patterns.md` — 常见统计错误
- **审稿标准**: `knowledge/review-standards.md` — 各类型综述审稿标准
- **期刊标准**: `knowledge/journal-requirements.md` — 目标期刊审稿要求
- **评估日志**: `harness/eval-log.md` — 评估日志模板

## 编码Agent执行协议

### 轻量编码 (`快记` / `记`)
- 更新 FEATURE_LIST.md 任务状态
- 更新 project-status.md 统计数据
- 追加 SESSION_LOG.md
- git add -A && git commit

### 完整编码 (`编码` / `6`)
- 轻量编码全部内容
- 效率数据收集（wall_time、tool_calls、token消耗）
- 安全审计（对照 safety-policy.md）
- MILESTONES.md 更新
- 结构化 commit message: `[phase] 简短描述`

## 与写作项目的协作协议

### 审稿触发
写作项目 Agent 8（投稿Agent）生成审稿包 → 放入 `review-pipeline/input/`

### 审稿反馈
审稿项目输出 → 写作项目 Agent 4（审校Agent）解析 `review-actions.json` → 逐条执行修复

### 复核闭环
修复后重新提交 → 审稿项目仅验证上次问题是否修复（不需完整重审）

---

*最后更新: 2026-06-06*
*当前版本: v1.0 — 项目初始化*
