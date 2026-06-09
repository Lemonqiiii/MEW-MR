# Safety Policy — 安全策略与越权检测规则

## 允许范围 (Allowlist)

### 文件系统
| 操作 | 允许路径 | 说明 |
|------|---------|------|
| Read | `E:\medical-review\**` | 项目内全部可读 |
| Read | `C:\Users\think.LAPTOP-BGJDS780\.claude\**` | Claude Code 配置（需读取原生 memory） |
| Read | `/e/medical-review/**` | Unix 路径形式 |
| Write/Edit | `E:\medical-review\**` | 仅项目内可写 |
| Write/Edit | `C:\Users\think.LAPTOP-BGJDS780\.claude\projects\E--medical-review\**` | 原生 memory 可写 |

### 网络
| 域名 | 用途 |
|------|------|
| `pubmed.ncbi.nlm.nih.gov` | PubMed 检索 |
| `pmc.ncbi.nlm.nih.gov` | PMC 全文 |
| `europepmc.org` | Europe PMC |
| `api.semanticscholar.org` | Semantic Scholar API |
| `www.semanticscholar.org` | Semantic Scholar 网页 |
| `link.springer.com` | Springer 文献 |
| `ncbi.nlm.nih.gov` | NCBI E-utilities |
| `ebi.ac.uk` | EBI 服务 |

### 命令
| 命令模式 | 用途 |
|---------|------|
| `git *` | 版本控制 |
| `python *` | Python 脚本 |
| `python scripts/process_integrity_check.py` | Gate 0 流程完整性检查 |
| `python scripts/harness_architecture_check.py` | Harness 架构检查 |
| `python scripts/audit_manuscript.py *` | 当前稿件审计 |
| `rg *` | 项目内文本搜索 |
| `Get-Content *` | PowerShell 文件读取 |
| `Get-ChildItem *` | PowerShell 文件枚举 |
| `pip *` | Python 包管理 |
| `mkdir -p /e/medical-review/**` | 创建项目目录 |
| `find /e/medical-review/**` | 文件搜索 |

---

## 越权检测规则

### 规则 1: 文件越界检测

编码Agent 扫描本次会话所有 Read/Write/Edit 操作的目标路径：

```python
# 伪代码逻辑
ALLOWED_READ = ["E:\\medical-review\\", "C:\\Users\\think.LAPTOP-BGJDS780\\.claude\\", "/e/medical-review/"]
ALLOWED_WRITE = ["E:\\medical-review\\", "C:\\Users\\think.LAPTOP-BGJDS780\\.claude\\projects\\E--medical-review\\"]

for op in session_operations:
    if op.type in ("Read", "Write", "Edit"):
        path = op.target_path
        if op.type in ("Write", "Edit"):
            if not any(path.startswith(p) for p in ALLOWED_WRITE):
                violations.append({
                    "severity": "HIGH",
                    "type": "OUT_OF_SCOPE_WRITE",
                    "path": path,
                    "operation": op
                })
        elif op.type == "Read":
            if not any(path.startswith(p) for p in ALLOWED_READ):
                violations.append({
                    "severity": "MEDIUM",
                    "type": "OUT_OF_SCOPE_READ",
                    "path": path,
                    "operation": op
                })
```

### 规则 2: 网络越界检测

```python
ALLOWED_DOMAINS = [
    "pubmed.ncbi.nlm.nih.gov", "pmc.ncbi.nlm.nih.gov",
    "europepmc.org", "api.semanticscholar.org", "www.semanticscholar.org",
    "link.springer.com", "ncbi.nlm.nih.gov", "ebi.ac.uk"
]

for op in session_operations:
    if op.type == "WebFetch":
        domain = extract_domain(op.url)
        if not any(domain == d or domain.endswith("." + d) for d in ALLOWED_DOMAINS):
            violations.append({
                "severity": "MEDIUM",
                "type": "UNAUTHORIZED_DOMAIN",
                "url": op.url,
                "domain": domain
            })
```

### 规则 3: 命令越界检测

```python
ALLOWED_COMMANDS = [
    "git *",
    "python scripts/process_integrity_check.py",
    "python scripts/harness_architecture_check.py",
    "python scripts/audit_manuscript.py *",
    "python *",
    "rg *",
    "Get-Content *",
    "Get-ChildItem *",
    "pip *",
    "mkdir -p /e/medical-review/**",
    "find /e/medical-review/**"
]

for op in session_operations:
    if op.type == "Bash":
        if not any(match_pattern(op.command, p) for p in ALLOWED_COMMANDS):
            violations.append({
                "severity": "LOW",
                "type": "UNRECOGNIZED_COMMAND",
                "command": op.command
            })
```

### 规则 4: 配置篡改检测

```python
SENSITIVE_FILES = [
    "CLAUDE.md",
    ".claude/settings.json",
    ".claude/settings.local.json",
    "memory/agent-specializations.md"
]

for op in session_operations:
    if op.type in ("Write", "Edit"):
        for sf in SENSITIVE_FILES:
            if op.target_path.endswith(sf):
                # 检查是否是用户明确请求的修改
                if not user_explicitly_requested(op):
                    violations.append({
                        "severity": "HIGH",
                        "type": "CONFIG_TAMPERING",
                        "path": op.target_path,
                        "note": "Agent self-modified configuration without user request"
                    })
```

### 规则 5: 信息泄露检测

```python
SECRET_PATTERNS = [
    r"sk-[a-f0-9]{32,}",          # API key 模式
    r"Bearer [a-f0-9\-]{20,}",    # Bearer token
    r"Authorization:.*[Kk]ey",    # Auth header
]

for op in session_operations:
    if op.type == "WebFetch":
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, op.url):
                violations.append({
                    "severity": "CRITICAL",
                    "type": "CREDENTIAL_LEAK",
                    "url": op.url,
                    "pattern": pattern
                })
```

### 规则 6: 模型/API Provenance 缺失检测

关键产物包括筛选日志、证据表、稿件正文、审校报告、投稿报告。若产物由 AI/API 辅助生成，必须记录模型/API 来源、输入来源、输出路径和人工核查状态。

```python
CRITICAL_OUTPUTS = [
    "docs/search-results/screening-decisions.csv",
    "data/**/evidence_table.*",
    "manuscript/*.md",
    "harness/reports/*.md",
    "harness/submission-readiness-report.md",
]

for output in generated_outputs:
    if matches_any(output.path, CRITICAL_OUTPUTS):
        if output.ai_assisted and not output.has_provenance:
            violations.append({
                "severity": "MEDIUM",
                "type": "MISSING_AI_PROVENANCE",
                "path": output.path
            })
```

### 规则 7: 旧项目写入脚本检测

任何会写文件的脚本，如果包含历史稿件名、历史主题名或内置长篇正文，必须被视为 legacy unsafe，除非它明确接受当前项目输入/输出路径。

```python
LEGACY_TOKENS = ["jitc_submission.md", "LUSC", "JITC", "screening_final_40.json"]

for script in scripts:
    if script.writes_files and any(tok in script.text for tok in LEGACY_TOKENS):
        if not script.requires_explicit_paths:
            violations.append({
                "severity": "HIGH",
                "type": "LEGACY_WRITE_SCRIPT",
                "path": script.path
            })
```

---

## 审计报告格式

编码Agent 在 `progress/metrics-raw.json` 的 `safety` 字段中记录：

```json
{
  "safety": {
    "total_operations": 25,
    "violations": [
      {
        "severity": "MEDIUM",
        "type": "OUT_OF_SCOPE_READ",
        "path": "C:\\Users\\think\\Documents\\notes.txt",
        "timestamp": "2026-06-04T15:30:00",
        "context": "Agent read user's Documents folder without authorization"
      }
    ],
        "summary": {
            "critical": 0,
            "high": 0,
            "medium": 1,
            "low": 0
        },
        "provenance": {
            "critical_outputs_checked": 4,
            "missing_ai_provenance": 0
        }
  }
}
```

### 评估Agent复核

评估Agent 读取 violations 后：
1. 对 CRITICAL → 立即通知用户
2. 对 HIGH → 在评估报告中标注
3. 对 MEDIUM → 检查是否为误报（如系统文件正常访问）
4. 对 LOW → 趋势监控，如果某种 LOW 频繁出现则升级

---

## 紧急响应流程

```
CRITICAL 级别违规
    │
    ├─ 1. 编码Agent 立即标记
    ├─ 2. 评估Agent 在下次运行时确认
    ├─ 3. 用户收到通知
    ├─ 4. 对应 API key 应立即轮换
    └─ 5. 复盘报告写入 harness/reports/incident-YYYY-MM-DD.md
```
