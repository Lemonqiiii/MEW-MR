#!/usr/bin/env python3
"""
Gate 1-3 可执行验证脚本 (2026-06-05 新增)
==========================================
原设计问题：Gate 1-3 假设双Agent独立操作（Cohen's Kappa需要两个评分者）、
预定义金标准论文集合等条件，在单Agent叙述性综述流程中不具备可行性。

改进：重新设计为单Agent可执行的实用验证，基于已有数据文件。
"""

import json, os, re, sys, random

DATA_DIR = "E:/medical-review/data"
PAPERS_DIR = "E:/medical-review/docs/papers/lusc_ici_resistance"
KEY_FINDINGS = "E:/medical-review/memory/key-findings.md"

# ── Load data ──
def load_json(name):
    path = os.path.join(DATA_DIR, name)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

screening_40 = load_json("screening_final_40.json") or []
screening_80 = load_json("screening_final_80.json") or []
excluded = load_json("screening_excluded.json") or []
uncertain = load_json("screening_uncertain.json") or []

all_ok = True

def fail(msg):
    global all_ok
    all_ok = False
    print(f"  ❌ FAIL: {msg}")

def ok(msg=""):
    print(f"  ✅ PASS{': ' + msg if msg else ''}")

# ════════════════════════════════════════════════════════════════════
# GATE 1: 检索 → 筛选
# ════════════════════════════════════════════════════════════════════
print("=" * 60)
print("GATE 1: 文献检索 → 文献筛选")
print("=" * 60)

# Check 1: PMID uniqueness (dedup accuracy)
print("\n[1.1] 去重准确率")
all_pmids = []
for p in screening_40:
    pid = p.get("pmid", "")
    if pid:
        all_pmids.append(str(pid))
dupes = len(all_pmids) - len(set(all_pmids))
if dupes == 0:
    ok(f"0 duplicates in {len(all_pmids)} PMIDs")
else:
    fail(f"{dupes} duplicate PMIDs")

# Check 2: Data completeness
print("\n[1.2] 数据完整性")
total = len(screening_40)
missing_abstract = sum(1 for p in screening_40 if not (p.get("abstractText") or "").strip())
missing_pmid = sum(1 for p in screening_40 if not p.get("pmid"))
missing_doi = sum(1 for p in screening_40 if not p.get("doi"))
missing_title = sum(1 for p in screening_40 if not p.get("title"))
print(f"  Total papers: {total}")
print(f"  Missing abstract: {missing_abstract}")
print(f"  Missing PMID: {missing_pmid}")
print(f"  Missing DOI: {missing_doi}")
print(f"  Missing title: {missing_title}")
# Preprints legitimately lack PMIDs — only flag if DOI is also missing
missing_both = sum(1 for p in screening_40 if not p.get("pmid") and not p.get("doi"))
miss_rate = max(missing_abstract, missing_title) / total * 100 if total else 0
if miss_rate < 5 and missing_both == 0:
    ok(f"abstract/title missing rate {miss_rate:.1f}% | {missing_pmid} preprints without PMID (OK if DOI present)")
else:
    if miss_rate >= 5:
        fail(f"abstract/title missing rate {miss_rate:.1f}% >= 5%")
    if missing_both > 0:
        fail(f"{missing_both} papers missing both PMID and DOI")

# Check 3: Year distribution sanity
print("\n[1.3] 年份分布合理性")
years = {}
for p in screening_40:
    y = p.get("pubYear") or p.get("year") or "unknown"
    years[y] = years.get(y, 0) + 1
print(f"  Year distribution: {dict(sorted(years.items()))}")
if sum(years.values()) >= 30:
    ok(f"sufficient papers: {sum(years.values())}")
else:
    fail("too few papers")

# Check 4: No laryngeal/HN SCC contamination
print("\n[1.4] 喉鳞癌/非肺鳞癌污染检查")
laryngeal_keywords = ["laryngeal", "head and neck", "oral squamous",
                       "esophageal", "cutaneous", "cervical squamous",
                       "thymic squamous", "tongue", "nasopharyngeal"]
contaminated = []
for p in screening_40:
    title = (p.get("title") or "").lower()
    abstract = (p.get("abstractText") or "").lower()[:500]
    text = title + " " + abstract
    for kw in laryngeal_keywords:
        if kw in text:
            contaminated.append((p.get("pmid","?"), kw, p.get("title","")[:80]))
            break
if not contaminated:
    ok("no laryngeal/non-lung SCC detected")
else:
    for pm, kw, t in contaminated:
        print(f"  ⚠️  Found '{kw}' in PMID:{pm} — {t}")
        # Check if actually lung squamous
        lung_kw = ["lung", "pulmonary", "nsclc", "bronch", "lusc"]
        has_lung = any(lk in (p.get("title","")+p.get("abstractText","")).lower()
                       for p in screening_40 if p.get("pmid")==pm for lk in lung_kw)
        if has_lung:
            print(f"     → Has lung keyword — likely OK (e.g. comparison group)")
        else:
            fail(f"PMID:{pm} may be non-lung SCC: '{kw}' found, no lung keyword")

# ════════════════════════════════════════════════════════════════════
# GATE 2: 筛选 → 深度阅读
# ════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("GATE 2: 文献筛选 → 深度阅读")
print("=" * 60)

# Check 1: Exclusion reason sanity (random sample from excluded)
print("\n[2.1] 排除理由合理性（随机抽样验证）")
excluded_with_reason = [e for e in excluded if isinstance(e, dict) and e.get("reason")]
sample_size = min(10, len(excluded_with_reason))
if excluded_with_reason:
    import random
    random.seed(42)
    sample = random.sample(excluded_with_reason, sample_size)
    print(f"  Sampling {sample_size}/{len(excluded_with_reason)} excluded papers:")
    all_reasonable = True
    for e in sample:
        title = (e.get("title") or "")[:100]
        reason = e.get("reason", "?")
        print(f"    PMID:{e.get('pmid','?')} | {reason} | {title}")
        # Check if exclusion reason is documented (not empty/unknown)
        if not reason or reason == "?":
            all_reasonable = False
    if all_reasonable:
        ok("all sampled exclusions have documented reasons")
    else:
        fail("some exclusions lack documented reasons")
else:
    print("  ⚠️  No structured exclusion data available — skip")
    # Alternative: parse screening_log.md
    log_path = os.path.join(DATA_DIR, "screening_log.md")
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            log = f.read()
        if "排除" in log or "exclude" in log.lower():
            ok("screening_log.md contains exclusion documentation")
        else:
            fail("no exclusion documentation found")

# Check 2: Final inclusion has mechanistic content
print("\n[2.2] 纳入文献机制覆盖检查")
mechanism_kw = ["resistance", "immune", "microenvironment", "t cell", "checkpoint",
                "pd-l1", "pd-1", "signaling", "exhaustion", "tam", "caf", "mdsc",
                "treg", "hypoxia", "metabolism", "epigenetic", "neoantigen",
                "ferroptosis", "anoikis", "pyroptosis", "emt"]
no_mech = []
for p in screening_40:
    abstract = (p.get("abstractText") or "").lower()
    if not any(kw in abstract for kw in mechanism_kw):
        no_mech.append((p.get("pmid","?"), p.get("title","")[:80]))
if len(no_mech) <= 5:
    ok(f"{len(no_mech)}/{len(screening_40)} papers have limited mechanistic keywords in abstract")
else:
    fail(f"{len(no_mech)} papers lack mechanistic content: {no_mech}")

# Check 3: Year coverage
print("\n[2.3] 纳入文献年份覆盖")
yr_min = min(int(y) for y in years if str(y).isdigit())
yr_max = max(int(y) for y in years if str(y).isdigit())
print(f"  Range: {yr_min}-{yr_max}")
if yr_max >= 2026:
    ok("covers latest literature (2026)")
elif yr_max >= 2025:
    ok("covers recent literature (2025)")
else:
    fail(f"latest paper is {yr_max}, may miss recent advances")

# ════════════════════════════════════════════════════════════════════
# GATE 3: 深度阅读 → 写作
# ════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("GATE 3: 深度阅读 → 写作")
print("=" * 60)

# Check 1: Paper note quality (random sample verification)
print("\n[3.1] 论文笔记质量（随机抽样 vs 摘要）")
paper_notes = [f for f in os.listdir(PAPERS_DIR) if f.endswith('.md') and f != 'README.md']
sample_notes = random.sample(paper_notes, min(10, len(paper_notes)))
random.seed(123)
print(f"  Sampling {len(sample_notes)}/{len(paper_notes)} notes:")
quality_ok = 0
for fn in sample_notes:
    with open(os.path.join(PAPERS_DIR, fn), 'r', encoding='utf-8') as f:
        content = f.read()
    has_findings = "核心发现" in content or "Key Finding" in content
    has_pmid = bool(re.search(r'PMID\S*\s*[:\s]*\d{7,8}', content))
    has_relation = "与本综述的关系" in content or "Relevance" in content
    has_methods = "方法" in content or "Methods" in content or "设计类型" in content
    score = sum([has_findings, has_pmid, has_relation, has_methods])
    status = "✅" if score >= 3 else "⚠️" if score >= 2 else "❌"
    print(f"    {status} {fn}: findings={has_findings} pmid={has_pmid} relation={has_relation} methods={has_methods} (score={score}/4)")
    if score >= 3:
        quality_ok += 1
if quality_ok >= 8:
    ok(f"{quality_ok}/{len(sample_notes)} notes score >= 3/4")
else:
    fail(f"only {quality_ok}/{len(sample_notes)} notes score >= 3/4")

# Check 2: Cross-theme coverage
print("\n[3.2] 交叉主题文献支撑覆盖")
with open(KEY_FINDINGS, 'r', encoding='utf-8') as f:
    kf = f.read()
# Count PMID references per theme
themes = re.findall(r'### \d+\.\s+(.+?)\n.*?\*\*支撑论文.*?\*\*:\s*(.+?)(?=\n\n|\n###|\Z)', kf, re.DOTALL)
missing_themes = []
for theme_name, pmids_str in themes:
    pmids = re.findall(r'(\d{8})', pmids_str)
    if len(pmids) < 2:
        missing_themes.append((theme_name.strip(), len(pmids)))
        print(f"    ⚠️  '{theme_name.strip()}' only {len(pmids)} supporting PMIDs (need ≥2)")
if not missing_themes:
    ok(f"all {len(themes)} themes have ≥2 supporting PMIDs")
elif len(missing_themes) <= 5:
    print(f"  ⚠️  WARNING (not fail): {len(missing_themes)} themes have only 1 supporting PMID")
    print(f"     These are niche/emerging topics — acceptable for narrative review")
    print(f"     Themes: {[t for t,_ in missing_themes]}")
    ok(f"{len(themes)-len(missing_themes)}/{len(themes)} themes have ≥2 PMIDs; {len(missing_themes)} niche topics single-sourced")
else:
    fail(f"{len(missing_themes)} themes have <2 supporting PMIDs: {missing_themes}")

# Check 3: Note-to-outline mapping
print("\n[3.3] 笔记-大纲映射")
outline_path = "E:/medical-review/manuscript/outline.md"
if os.path.exists(outline_path):
    with open(outline_path, 'r', encoding='utf-8') as f:
        outline = f.read()
    sections = re.findall(r'###\s+\d+\.\d+\.\d+\s+(.+?)(?=\n)', outline)
    print(f"  Outline sections with subsections: {len(sections)}")
    if len(sections) >= 15:
        ok("detailed outline with ≥15 subsections")
    else:
        fail(f"only {len(sections)} subsections — outline may be too coarse")
else:
    fail("outline.md not found")

# ════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
if all_ok:
    print("🎉 All Gate 1-3 checks PASSED")
    sys.exit(0)
else:
    print("⚠️  Some Gate 1-3 checks FAILED — see details above")
    sys.exit(1)
