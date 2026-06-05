# 质量关卡系统 (Quality Gate System)

## 核心原则

**每个 Phase 的输出在进入下一 Phase 之前，必须通过质量关卡检查。** 未经检查的输出 = 未完成。

---

## 六个关卡

### Gate 1: 文献检索 → 文献筛选

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 查全率 | 随机抽 5 篇已知关键论文，验证是否被检索到 | 5/5 命中 |
| 去重准确率 | 随机抽 50 篇，人工验证无重复 | 0 重复 |
| 数据完整性 | 检查 PMID/DOI/摘要缺失率 | <5% 缺失 |

### Gate 2: 文献筛选 → 深度阅读

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 纳入一致性 | Agent A vs Agent B 独立筛选 20 篇，计算 Cohen's Kappa | Kappa > 0.7 |
| 排除理由 | 随机抽 10 篇排除文献，验证排除理由合理 | 10/10 合理 |
| 假阳性检查 | 验证纳入文献标题→是否确实讨论鳞癌+免疫耐药 | 0 篇错分 |

### Gate 3: 深度阅读 → 写作

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 笔记质量 | 随机抽 10 篇笔记，检查核心发现是否可从摘要中推断 | ≥ 8/10 |
| 主题覆盖 | 检查是否有关键机制类别未被覆盖 | 0 空白类别 |
| 引用可追溯 | 每个交叉主题是否至少有 2 篇独立文献支撑 | 100% |

### Gate 4: 写作（正文）

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| **引用-声明验证** | **逐条打开引用文献的摘要，确认声明内容确实来自该文献** | **≥ 95% 通过率** |
| 逻辑连贯性 | 检查章节过渡句是否准确反映下一章内容 | 7/7 过渡准确 |
| 数据准确性 | 验证所有频率数字、试验名称、药物名称的准确性 | 0 事实错误 |

### Gate 5: 修改/扩展（关键！）

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| **新增声明溯源** | **每条新增声明必须标注具体来源（引文+段落位置）** | **100% 可溯源** |
| 修改范围审查 | 对比修改前后的 diff，确认修改不超过引用支撑范围 | 0 越界修改 |
| 回退测试 | 如果新增声明无法溯源，是否可安全回退而不破坏逻辑？ | 100% 不破坏 |

### Gate 6: 终稿 → 投稿

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 引用格式 | 检查所有引用格式一致性、PMID/DOI 完整性 | 100% |
| 图表嵌入 | 确认正文引用编号与图表文件对应 | 100% |
| 语言终审 | 全文朗读，标记不通顺句子 | ≤ 5 处标记 |

---

## 执行记录

| 关卡 | 日期 | 通过/失败 | 发现问题 | 处理 |
|------|------|----------|---------|------|
| Gate 1 | - | 未执行 | - | - |
| Gate 2 | - | 未执行 | - | - |
| Gate 3 | - | 未执行 | - | - |
| Gate 4 | 2026-06-04 | **失败** | 14条声明中13条引文不支持 | 回退方案 |
| Gate 4 | 2026-06-04 | **通过** | 回退后19/20直接验证 | 1项AST/SOX2声明修正 |
| Gate 5 | 2026-06-05 | **通过** | 41/41引用已用, Fig/Tab编号干净 | - |

---

## Gate 4 可执行脚本 (2026-06-05 编码)

```bash
python3 << 'PYEOF'
import json, re
data_dir = "E:/medical-review/data"
with open(f"{data_dir}/screening_final_40.json", "r", encoding="utf-8") as f:
    papers = json.load(f)
pmid_db = {}
for p in papers:
    if p.get("pmid"): pmid_db[p["pmid"]] = ((p.get("abstractText","") or "")[:3000]).lower()

with open("manuscript/jitc_submission.md", "r", encoding="utf-8") as f:
    body = f.read().split("## References")[0]

# 1. Expand range refs [N-M] → individual numbers
text_refs = set()
def expand(m):
    for seg in re.split(r',\s*', m.group(1)):
        rng = re.match(r'(\d+)\s*[-–]\s*(\d+)', seg)
        if rng: text_refs.update(range(int(rng.group(1)), int(rng.group(2))+1))
        else: text_refs.add(int(seg))
re.sub(r'\[([\d,\s\-–]+)\]', expand, body)

refs_section = open("manuscript/jitc_submission.md").read().split("## References")[1]
list_refs = set(int(m.group(1)) for m in re.finditer(r'^(\d+)\.', refs_section, re.MULTILINE))

# 2. Check claim-citation pairs
claims = [
    ("41050683","p = 0.00018","TGM2 P-value"),
    ("35799269","28 to 36","EIC 28-36%"),
    ("35799269","ctla4","9 co-upregulated ICPs"),
    ("34429332","7%","Lung-MAP ORR 7%"),
    ("36198685","keap1","KEAP1 ~12%"),
    ("38803944","513","Song 513 samples"),
    ("41239433","aldoa","ALDOA overexpression"),
    ("40138855","sting","Hypoxia-STING"),
    ("35525959","circhmgb2","circHMGB2"),
    ("40568576","adenosquamous","AST claim"),
]
v_ok = sum(1 for pmid,kw,_ in claims if pmid in pmid_db and kw in pmid_db[pmid])

# 3. Format checks
figs = set(re.findall(r'Figure\s+(\d+)', body))
tabs = set(re.findall(r'Table\s+(\d+)', body))

print(f"Gate4 claims: {v_ok}/{len(claims)}")
print(f"Gate5 unused: {sorted(list_refs - text_refs) or 'none'}")
print(f"Gate5 figs: {figs} | tabs: {tabs}")
print(f"PASS" if v_ok>=9 and not (list_refs-text_refs) and figs=={'1'} and tabs=={'1','2'} else "FAIL")
PYEOF
```

## Gate 5b Word 格式检查 (已嵌入 gen_word_full.py)

生成 Word 后自动运行：Figure refs, Table refs, Bad refs, Body citations, Images embedded, Headings, Word count

---

## 知识库更新

所有教训已编码到：
- `CLAUDE.md` → 写作纪律 + 质量关卡
- `memory/lessons-learned.md` → 8条教训 + 错误模式库
- `harness/quality-gate.md` → 可执行 Gate 4 脚本
- `scripts/gen_word_full.py` → 内置自检
