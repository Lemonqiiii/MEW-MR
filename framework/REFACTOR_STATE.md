# 重构状态追踪

> 自驱动重构流程：每步开始前读取本文件 → 找到第一个未完成任务 → 执行 → 验证 → 编码更新 → 循环

## 重构 Phases

### Phase 1: 拆分 CLAUDE.md
- [x] 1.1 创建新目录结构（claude/, scripts/, templates/, docs/）
- [x] 1.2 从原 CLAUDE.md 提取"写作纪律"到 claude/disciplines/
- [x] 1.3 从原 CLAUDE.md 提取"错误模式库"到 claude/disciplines/
- [x] 1.4 从原 CLAUDE.md 提取"质量门禁定义"到 claude/gates/
- [x] 1.5 从原 CLAUDE.md 提取"交互原则+命令表"到 CLAUDE.md（精简版）
- [x] 1.6 拆分 agent-specializations.md → claude/agents/ 下 9 个独立文件
- [x] 1.7 验证：`wc -l claude/CLAUDE.md` ≤ 120 行
- [x] 1.8 Git commit: Phase 1 完成

### Phase 2: 配置外提
- [x] 2.1 创建 config.yaml（从原 CLAUDE.md + agent-specializations.md 提取所有硬编码配置）
- [x] 2.2 修改所有 Python 脚本改为从 config.yaml 读取路径
- [x] 2.3 验证：`grep -rn "E:/medical-review" scripts/` 返回 0
- [x] 2.4 Git commit: Phase 2 完成

### Phase 3: Gate 代码化
- [x] 3.1 创建 scripts/verify_gates.py（统一 Gate runner）
- [x] 3.2 实现 Gate 1-6 为独立 Python 函数
- [x] 3.3 实现 Gate 7-11 为独立 Python 函数
- [x] 3.4 验证：`python3 scripts/verify_gates.py --all` 语法正确
- [x] 3.5 Git commit: Phase 3 完成

### Phase 4: Agent 定义结构化
- [x] 4.1 统一 Agent 文件格式（Metadata + Steps + Handoff Schema）
- [x] 4.2 每个 Agent 标注 pre_gate / post_gate
- [x] 4.3 每个 Step 标注 MANDATORY / OPTIONAL / CONDITIONAL
- [x] 4.4 验证：所有 Agent 文件格式一致
- [x] 4.5 Git commit: Phase 4 完成

### Phase 5: 状态管理结构化
- [x] 5.1 创建 state.json schema
- [x] 5.2 创建 scripts/state.py（读写 state.json）
- [x] 5.3 Agent 定义中所有 "读取 memory/xxx" 改为 "读取 state.json"
- [x] 5.4 验证：state.json 合法 JSON + Schema 完整
- [x] 5.5 Git commit: Phase 5 完成

### Phase 6: 领域模板可插拔
- [x] 6.1 从 Agent 6 定义中提取 A-J 分类体系 → templates/paper-types/default-a-j.md
- [x] 6.2 从 Agent 6 定义中提取排除规则 → config.yaml exclusion_keywords
- [x] 6.3 从 Agent 4/CLAUDE.md 中提取 LUSC 特定规则 → 标记为领域模板
- [x] 6.4 验证：diff 原定义 vs 模板文件内容一致
- [x] 6.5 Git commit: Phase 6 完成

### Phase 7: 国际化和文档
- [x] 7.1 所有 claude/ 文件从中文 -> 英文
- [x] 7.2 所有 scripts/ 注释和 docstring -> 英文
- [x] 7.3 创建 docs/GETTING_STARTED.md
- [x] 7.4 创建 docs/WORKFLOW.md
- [x] 7.5 创建 docs/CONFIG.md
- [x] 7.6 更新 README.md
- [x] 7.7 Git commit: Phase 7 完成

### Phase 8: 依赖和分发
- [x] 8.1 创建 requirements.txt
- [x] 8.2 创建 config.example.yaml
- [x] 8.3 创建 setup.sh / setup.ps1
- [x] 8.4 创建 .gitignore（不含运行记录，含框架文件）
- [x] 8.5 创建 LICENSE
- [x] 8.6 验证：clean clone + setup + smoke test 全部通过
- [x] 8.7 Git commit: Phase 8 完成

## 工作协议
1. **每步开始前**：读取本文件，找到第一个 `[ ]` 任务
2. **执行**：完成该任务（不跳过，不合并未关联的任务）
3. **验证**：运行该步骤的验证命令，失败则修复后重试
4. **编码**：git add + git commit（结构化 message: `[Phase N.M] 描述`）
5. **更新**：将本文件中对应任务标记为 `[x]`
6. **循环**：回到步骤 1
