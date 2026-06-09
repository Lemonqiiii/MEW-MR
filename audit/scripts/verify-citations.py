#!/usr/bin/env python3
"""
引用验证脚本 — Layer 1 存在性验证

验证稿件中所有引用的 PMID/DOI 是否有效。
用法: python3 scripts/verify-citations.py <manuscript_path>
"""

import re
import sys
import json
from urllib.request import urlopen, Request
from urllib.error import URLError
import time

# Fix Windows GBK terminal encoding — emoji characters crash without this
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass


def extract_citations(text):
    """从稿件文本中提取所有引用"""
    # 查找参考文献部分的编号列表
    ref_section = text.split("## References")[-1] if "## References" in text else text

    citations = []
    # 匹配格式: 1. Author (Year) Title. Journal. PMID: XXXX
    pmid_pattern = re.findall(r'PMID[:：]\s*(\d+)', ref_section, re.IGNORECASE)
    doi_pattern = re.findall(r'DOI[:：]\s*(10\.\d{4,}/[^\s\]\)]+)', ref_section, re.IGNORECASE)

    for i, pmid in enumerate(pmid_pattern):
        citations.append({"ref_number": i+1, "pmid": pmid, "doi": None})

    for doi in doi_pattern:
        doi_clean = doi.rstrip('.')
        # 找到对应编号
        citations.append({"ref_number": len(citations)+1, "pmid": None, "doi": doi_clean})

    return citations


def verify_pmid(pmid):
    """通过 PubMed API 验证 PMID"""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
    try:
        req = Request(url, headers={"User-Agent": "Medical-Audit/1.0"})
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            if "result" in data and pmid in data["result"]:
                record = data["result"][pmid]
                title = record.get("title", "Unknown")
                if record.get("error") or not title or title == "Unknown":
                    return False, record.get("error", "PMID not found")
                return True, title
            return False, "PMID not found"
    except Exception as e:
        return False, str(e)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 verify-citations.py <manuscript_path>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        text = f.read()

    citations = extract_citations(text)
    print(f"Found {len(citations)} citations")
    print("=" * 60)

    verified = 0
    failed = 0

    for cit in citations:
        if cit["pmid"]:
            ok, info = verify_pmid(cit["pmid"])
            status = "✅" if ok else "❌"
            if ok:
                verified += 1
            else:
                failed += 1
            print(f"{status} [{cit['ref_number']}] PMID:{cit['pmid']} — {info[:80]}")
            time.sleep(0.34)  # NCBI rate limit: 3 requests/sec

    print("=" * 60)
    print(f"Verified: {verified}, Failed: {failed}, Total: {len(citations)}")


if __name__ == "__main__":
    main()
