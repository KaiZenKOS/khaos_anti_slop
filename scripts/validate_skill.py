#!/usr/bin/env python3
"""Validate local KHAOS skill packaging without optional dependencies."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = (root / 'SKILL.md').read_text(encoding='utf-8')
flags = (root / 'references' / 'visual-red-flags.md').read_text(encoding='utf-8')
assert skill.startswith('---\n'), 'Missing YAML frontmatter'
front = skill.split('---', 2)[1]
assert re.search(r'(?m)^name:\s*khaos-anti-slop\s*$', front), 'Skill name missing or incorrect'
assert re.search(r'(?m)^description:', front), 'Missing description'
assert (root.name == 'khaos-anti-slop'), 'Directory and skill name must match'
for relative in ('references/visual-red-flags.md', 'references/code-performance.md', 'references/writing-humanizer.md', 'references/evaluation.md'):
    assert (root / relative).exists(), f'Missing reference: {relative}'
for n in range(1, 31):
    assert re.search(rf'(?m)^\|\s*{n}\s*\|', flags), f'Missing screenshot red flag {n}'
assert 'O(n)' in skill and 'O(n log n)' in skill and 'O(n²)' in skill
assert 'Hard fail' in skill and 'Ponytail' in skill and 'writing-humanizer' in skill
print('PASS: metadata, name, 30 flags, references, complexity and safety gate.')
