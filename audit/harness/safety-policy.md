# 安全策略与越权检测规则

> 审稿项目的安全策略。编码Agent Part C 依据本文件执行安全审计。

---

## 一、知情边界安全

### 规则 S1: 审稿Agent隔离

```
禁止: 审稿Agent的系统提示中包含写作项目的内部信息
检测: 扫描R1-R6的prompt是否包含被屏蔽关键词
关键词库: 
  - CLAUDE.md (写作项目的)
  - Agent 0-8
  - Gate 1-11
  - domain-ontology
  - evidence-gap-grading
  - cross-intervention-matrix
  - workflow-evolution
  - metrics-raw
  - project-status (写作项目路径)
  - memory/agent-specializations (写作项目)
```

### 规则 S2: 文件系统隔离

```
允许: 审稿Agent读取 review-pipeline/input/ 和 review-pipeline/context/
允许: 审稿Agent写入 review-pipeline/reviews/
允许: Agent V读取文献数据库（PubMed/EPMC等外部API）
禁止: 审稿Agent读取写作项目下的任何文件（仅限审稿包输入）
禁止: 审稿Agent写入写作项目下的任何文件（仅限审稿报告输出）
例外: Agent P可以读取写作项目输出的审稿包（仅限约定的输入路径）
```

### 规则 S3: 输出净化

```
禁止: review-actions.json 中包含:
  - 可执行代码或脚本
  - 对写作项目文件的直接路径引用
  - 对写作Agent的调用指令
  - API密钥或密码
格式约束: review-actions.json 仅含结构化数据，不含自然语言指令
```

---

## 二、外部访问安全

### 规则 S4: 网络请求限制

```
允许: PubMed E-utilities API (eutils.ncbi.nlm.nih.gov)
允许: Europe PMC API (www.ebi.ac.uk/europepmc)
允许: DOI解析 (dx.doi.org)
允许: Semantic Scholar API (api.semanticscholar.org)
需确认: 任何其他外部URL
禁止: 访问付费/登录墙后的内容（需用户手动授权）
```

### 规则 S5: 数据最小化

```
原则: 审稿过程中获取的文献全文/摘要仅用于本次审稿
禁止: 将文献摘要/全文存入项目的非预期位置
禁止: 在公网上发布审稿内容
存储: 文献缓存仅存储在 review-pipeline/input/cache/
```

---

## 三、审计流程

### 编码Agent Part C 审计步骤

```
1. 扫描本次会话中所有Agent的系统提示
   → 检查是否包含禁止关键词
   
2. 扫描所有文件读写操作
   → 检查是否有越界读写
   
3. 扫描所有网络请求
   → 检查是否有未授权的URL
   
4. 扫描输出文件
   → 检查是否有敏感信息泄露
   
5. 生成审计报告
   → 写入 progress/metrics-raw.json 的 safety 部分
```

### 违规处理

| 级别 | 处理 |
|------|------|
| **临界** | 记录到 metrics-raw.json，提示用户注意 |
| **严重** | 立即通知用户，建议回退相关操作 |
| **致命** | 终止审稿，要求重新设计知情边界 |
