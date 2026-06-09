#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Cross-reference consistency check across all project files."""
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROJECT_ROOT = r'E:\medical-review'

scan_files = [
    'CLAUDE.md', 'AGENTS.md',
    'memory/agent-specializations.md', 'harness/quality-gate.md',
    'harness/safety-policy.md', 'harness/test-scenarios.md',
    'harness/consistency-benchmarks.md', 'harness/search-screening-protocol.md',
    'harness/review-revision-protocol.md',
    'memory/MEMORY.md', 'memory/workflow-evolution.md',
    'features/FEATURE_LIST.md', '.codex/hooks.json',
]

def read_file(fname):
    fpath = os.path.join(PROJECT_ROOT, fname)
    if not os.path.exists(fpath):
        return None
    with open(fpath, 'r', encoding='utf-8') as f:
        return f.read()

all_pass = True
def ok(msg):
    print(f'  ✅ {msg}')
def fail(msg):
    global all_pass
    all_pass = False
    print(f'  ❌ {msg}')

# =====================================================
# CHECK 1: All referenced files exist
# =====================================================
print('=' * 60)
print('CHECK 1: File path references')
print('=' * 60)
for fname in scan_files:
    content = read_file(fname)
    if content is None:
        fail(f'FILE MISSING: {fname}')
        continue
    refs = set(re.findall(r'`([a-zA-Z0-9_/.\-]+\.[a-z]{2,4})`', content))
    refs |= set(re.findall(
        r'(?<![`\w])(?:scripts|harness|memory|docs|manuscript|knowledge|features|archive|progress)/[a-zA-Z0-9_/.\-]+\.[a-z]{2,4}',
        content))
    for ref in refs:
        if ref.startswith('http'):
            continue
        ref_path = os.path.join(PROJECT_ROOT, ref)
        if not os.path.exists(ref_path):
            # Some might be template/example paths
            if any(ref.startswith(p) for p in ['docs/papers/', 'archive/']):
                continue
            fail(f'{fname} -> {ref} (NOT FOUND)')

# =====================================================
# CHECK 2: Agent numbering consistency
# =====================================================
print()
print('=' * 60)
print('CHECK 2: Agent numbering consistency')
print('=' * 60)

claude = read_file('CLAUDE.md') or ''
agents_md = read_file('AGENTS.md') or ''
agent_spec = read_file('memory/agent-specializations.md') or ''

claude_agents = set(re.findall(r'Agent\s+(\d+)', claude))
extra = claude_agents - {'0','1','2','3','4','5'}
if extra:
    fail(f'CLAUDE.md refs non-existent Agents: {extra}')
else:
    ok(f'CLAUDE.md only refs Agents 0-5: {sorted(claude_agents, key=int)}')

# Check AGENTS.md command table
cmd_start = agents_md.find('| `1`')
cmd_end = agents_md.find('| `gen`', cmd_start) if cmd_start > 0 else -1
cmd_table = agents_md[cmd_start:cmd_end+200] if cmd_start > 0 and cmd_end > 0 else ''
bad_agents_in_cmd = []
for a in ['6', '7', '8']:
    if f'Agent {a}' in cmd_table:
        bad_agents_in_cmd.append(a)
if bad_agents_in_cmd:
    fail(f'AGENTS.md command table still refs Agent {bad_agents_in_cmd}')
else:
    ok('AGENTS.md command table clean (no Agent 6/7/8)')

# Check agent-specializations has consolidation notices
if 'Agent 6' in agent_spec and '已合并' in agent_spec:
    ok('Agent 6 section has consolidation notice')
if 'Agent 7' in agent_spec and '已合并' in agent_spec:
    ok('Agent 7 section has consolidation notice')
if 'Agent 8' in agent_spec and '保留为脚本' in agent_spec:
    ok('Agent 8 section has script-only notice')

# =====================================================
# CHECK 3: Gate tier consistency
# =====================================================
print()
print('=' * 60)
print('CHECK 3: Gate tier consistency')
print('=' * 60)

gates_md = read_file('harness/quality-gate.md') or ''
core_count = len(re.findall(r'🔵 CORE', gates_md))
enh_count = len(re.findall(r'🟢 ENHANCED', gates_md))
ok(f'CORE gates: {core_count} (expected 7)') if core_count == 7 else fail(f'CORE: {core_count} != 7')
ok(f'ENHANCED gates: {enh_count} (expected 5)') if enh_count == 5 else fail(f'ENHANCED: {enh_count} != 5')

if '分级制度' in gates_md:
    ok('Gate tiering table present')
else:
    fail('Gate tiering table missing')

if '🔵 CORE' in claude:
    ok('CLAUDE.md mentions CORE gate labels')

# =====================================================
# CHECK 4: Old hardcoded references
# =====================================================
print()
print('=' * 60)
print('CHECK 4: Old project hardcoded references')
print('=' * 60)

old_patterns = [
    (r'jitc_submission\.md', 'jitc_submission.md path'),
    (r'\bJITC\b', 'JITC journal name'),
    (r'\bLUSC\b', 'LUSC topic (not in archive)'),
    (r'Pediatric Research', 'Pediatric Research (not as historical)'),
    (r'screening_final_\d+\.json', 'old screening JSON'),
    (r'pubmed_merged_all\.json', 'old pubmed merge JSON'),
]
safe_keywords = ['禁止', 'do not', '旧', '历史', '归档', 'archive', 'hardcod',
                 'default to', '上一轮', '历史项目', '示例', 'example',
                 '上一轮:', '旧项目', '已归档']

found_any = False
for fname in ['CLAUDE.md', 'AGENTS.md', 'memory/agent-specializations.md',
              'harness/quality-gate.md', 'features/FEATURE_LIST.md']:
    content = read_file(fname) or ''
    for pattern, label in old_patterns:
        for m in re.finditer(pattern, content):
            # Check context: 3 lines before and after
            start = max(0, m.start() - 200)
            end = min(len(content), m.end() + 200)
            ctx = content[start:end].lower()
            if any(kw in ctx for kw in safe_keywords):
                continue  # OK - in ban/historical context
            found_any = True
            line_no = content[:m.start()].count('\n') + 1
            fail(f'{fname}:{line_no}: {label} in non-safe context')

if not found_any:
    ok('No problematic old references in core files')

# =====================================================
# CHECK 5: Referenced scripts exist
# =====================================================
print()
print('=' * 60)
print('CHECK 5: Referenced scripts exist')
print('=' * 60)

all_text = claude + '\n' + agents_md + '\n' + gates_md
script_refs = set(re.findall(r'scripts/[a-zA-Z_]+\.py', all_text))
for s in sorted(script_refs):
    spath = os.path.join(PROJECT_ROOT, s)
    if os.path.exists(spath):
        ok(f'{s}')
    else:
        fail(f'{s} MISSING')

# =====================================================
# CHECK 6: Memory file consistency
# =====================================================
print()
print('=' * 60)
print('CHECK 6: Memory file integrity')
print('=' * 60)

memory_md = read_file('memory/MEMORY.md') or ''
# Check MEMORY.md has reasonable entries
mem_entries = re.findall(r'\[.+\]\(.+\.md\)', memory_md)
ok(f'MEMORY.md has {len(mem_entries)} memory entries')

# Check each referenced memory file exists
for entry in mem_entries:
    mem_file = re.search(r'\((.+\.md)\)', entry)
    if mem_file:
        fname = mem_file.group(1)
        # Resolve relative to memory/ directory
        if not fname.startswith('memory/'):
            fname = 'memory/' + fname
        fpath = os.path.join(PROJECT_ROOT, fname)
        if os.path.exists(fpath):
            pass  # ok
        else:
            fail(f'MEMORY.md -> {fname} not found')

# Check project-status.md and active-focus.md exist
for mem_f in ['memory/project-status.md', 'memory/active-focus.md']:
    fpath = os.path.join(PROJECT_ROOT, mem_f)
    if os.path.exists(fpath):
        ok(f'{mem_f} exists')
    else:
        fail(f'{mem_f} MISSING - required for project routing')

# =====================================================
# CHECK 7: CLAUDE.md startup order completeness
# =====================================================
print()
print('=' * 60)
print('CHECK 7: CLAUDE.md startup completeness')
print('=' * 60)

required_sections = [
    ('启动顺序', 'startup order'),
    ('项目路由', 'routing rule'),
    ('核心规则', 'core rules'),
    ('引用铁律', 'citation iron law'),
    ('写作纪律', 'writing discipline'),
    ('引用范围纪律', 'citation scope'),
    ('自然度', 'naturalness'),
    ('Gate 体系', 'gate system'),
    ('命令速查', 'command reference'),
]
for section, _ in required_sections:
    if section in claude:
        ok(f'Section present: {section}')
    else:
        fail(f'Section missing: {section}')

# =====================================================
# CHECK 8: harness/ directory structure
# =====================================================
print()
print('=' * 60)
print('CHECK 8: harness directory structure')
print('=' * 60)

harness_dir = os.path.join(PROJECT_ROOT, 'harness')
harness_files = os.listdir(harness_dir)

# Protocols (should be in harness/)
protocols = ['architecture.md', 'quality-gate.md', 'safety-policy.md',
             'search-screening-protocol.md', 'review-revision-protocol.md',
             'test-scenarios.md', 'consistency-benchmarks.md',
             'metrics.md', 'submission-compliance.md',
             'critical-absorption.md', 'argument-diversity-enforcement.md',
             'cross-intervention-matrix.md', 'clinical-decision-framework.md',
             'data-translation.md', 'evidence-gap-grading.md',
             'negative-claim-detection.md', 'perspective-switching.md',
             'priority-scoring.md', 'time-annotation.md',
             'synthesis-reasoning.md', 'journal-profiles.md',
             'remediation-plan.md', 'README.md']
reports_dir = os.path.join(harness_dir, 'reports')
reports_files = os.listdir(reports_dir) if os.path.exists(reports_dir) else []

for proto in protocols:
    if proto in harness_files:
        pass  # ok
    else:
        fail(f'Protocol missing from harness/: {proto}')

ok(f'harness/ has {len(harness_files)} entries')
ok(f'harness/reports/ has {len(reports_files)} entries')

print()
print('=' * 60)
if all_pass:
    print('RESULT: ALL CHECKS PASSED')
else:
    print('RESULT: SOME CHECKS FAILED — see above')
print('=' * 60)
