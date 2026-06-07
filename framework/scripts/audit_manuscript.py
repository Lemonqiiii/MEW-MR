#!/usr/bin/env python3
"""Audit manuscript structural integrity — run before gen_word.py."""
import re, sys, os
from config_loader import load_config, find_project_root

if len(sys.argv) > 1 and sys.argv[1] in ('--help', '-h'):
    print("Usage: python3 audit_manuscript.py [manuscript_path]")
    print("  Validates structural integrity of a review manuscript.")
    print("  If no path given, reads from config.yaml paths.manuscript_src.")
    sys.exit(0)

_config = load_config()
_default_src = str(find_project_root() / _config["paths"]["manuscript_src"])
SRC = sys.argv[1] if len(sys.argv) > 1 else _default_src

with open(SRC, 'r', encoding='utf-8') as f:
    text = f.read()

errors = []
warnings = []

# Split body/references
parts = text.split('## References')
body = parts[0]
refs = parts[1] if len(parts) > 1 else ''

# 1. Has title?
if not re.match(r'^# ', text):
    errors.append("Missing top-level title (# Title)")

# 2. Has Abstract?
if '## Abstract' not in body:
    errors.append("Missing ## Abstract section")

# 3. Has References?
if '## References' not in text:
    errors.append("Missing ## References section")

# 4. Only one References section
ref_count = text.count('## References')
if ref_count > 1:
    errors.append(f"Duplicate ## References sections ({ref_count} found)")

# 5. Section numbering sequential
sections = re.findall(r'^## (\d+)\.', body, re.MULTILINE)
if sections:
    nums = [int(s) for s in sections]
    expected = list(range(1, max(nums) + 1))
    if nums != expected:
        errors.append(f"Non-sequential sections: found {nums}, expected {expected}")

# 6. Citation integrity
cited = set()
for m in re.finditer(r'\[([\d,\-]+)\]', body):
    for part in m.group(1).split(','):
        part = part.strip()
        if '-' in part:
            a, b = part.split('-')
            cited.update(range(int(a), int(b) + 1))
        else:
            cited.add(int(part))

listed = set()
for m in re.finditer(r'^(\d+)\.', refs, re.MULTILINE):
    listed.add(int(m.group(1)))

missing = cited - listed
unused = listed - cited
if missing:
    errors.append(f"References cited but not listed: {sorted(missing)}")
if unused:
    warnings.append(f"References listed but not cited: {sorted(unused)}")

# 7. Word count
words = len(re.findall(r'\b\w+\b', body))
if words < 3000:
    warnings.append(f"Low word count: {words}")
elif words > 15000:
    warnings.append(f"High word count: {words}")

# 8. Abstract has no figure references
abstract_section = body.split('## 1.')[0] if '## 1.' in body else body
if re.search(r'Figure\s+\d+', abstract_section):
    errors.append("Abstract contains figure reference — move to body text")

# 9. Duplicate paragraphs
paras = [p.strip() for p in body.split('\n\n') if len(p.strip()) > 80]
seen = set()
dups = 0
for p in paras:
    key = p[:80]
    if key in seen:
        dups += 1
    seen.add(key)
if dups > 0:
    warnings.append(f"{dups} potential duplicate paragraphs")

# 10. Orphaned HRs
hr_count = len(re.findall(r'^\-\-\-$', text, re.MULTILINE))
# Rough check: sections * 1 + references * 1 = expected HRs
expected_hrs = len(sections) + 1
if abs(hr_count - expected_hrs) > 3:
    warnings.append(f"Orphaned --- separators: {hr_count} found, ~{expected_hrs} expected")

# Report
print(f"Audit: {SRC}")
print(f"  Sections: {len(sections)} ({' → '.join(sections[:5])}{'...' if len(sections)>5 else ''})")
print(f"  Words: {words}")
print(f"  References: {len(listed)} listed / {len(cited)} cited")

if errors:
    print(f"\n  ERRORS ({len(errors)}):")
    for e in errors:
        print(f"    - {e}")
if warnings:
    print(f"\n  WARNINGS ({len(warnings)}):")
    for w in warnings:
        print(f"    - {w}")

if not errors:
    print(f"\n  PASSED")
else:
    print(f"\n  FAILED — fix errors before generating Word")

sys.exit(len(errors))
