#!/usr/bin/env python3
"""Heuristic KHAOS Slop scan (stdlib only). NOT a design or security verdict."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

EXTENSIONS = {'.md', '.mdx', '.html', '.css', '.scss', '.js', '.jsx', '.ts', '.tsx', '.vue', '.svelte'}
SKIP_DIRS = {'node_modules', 'dist', 'build', '.next', '.git', 'coverage', 'vendor', '.venv'}
RULES = [
    ('generic-copy', re.compile(r'\b(revolutioniz(?:e|ing)|unlock the future|game.changing|seamless experience|cutting.edge|next.generation solution)\b', re.I), 'Replace with a verifiable product outcome.'),
    ('fake-proof-marker', re.compile(r'\b(fake testimonial|fake reviews?|lorem ipsum|placeholder testimonial)\b', re.I), 'Remove invented proof or label clearly as synthetic.'),
    ('decorative-sparkles', re.compile(r'\b(sparkles?|radial.?orb|dot.?grid)\b', re.I), 'Check for unnecessary visual decoration.'),
    ('gradient-overuse', re.compile(r'\b(?:bg-gradient-to-|linear-gradient\(|radial-gradient\()', re.I), 'Check whether the gradient follows brand direction.'),
    ('empty-click-handler', re.compile(r'onClick\s*=\s*\{\s*\(\s*\)\s*=>\s*\{\s*\}\s*\}'), 'Inspect nonfunctional interaction.'),
    ('fake-success', re.compile(r'\b(?:alert|toast)\s*\(\s*[\x27\"](?:success|saved|completed)[! .\x27\"]', re.I), 'Verify that success follows a real completed operation.'),
]

def scan(root: Path):
    findings = []
    for path in root.rglob('*'):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS or any(p in SKIP_DIRS for p in path.parts):
            continue
        # Avoid scanning self-reference documents or its source code.
        if 'khaos-anti-slop' in path.parts:
            continue
        if path.stat().st_size > 2_000_000:
            continue
        try:
            content = path.read_text(encoding='utf-8')
        except (OSError, UnicodeDecodeError):
            continue
        for line_no, line in enumerate(content.splitlines(), 1):
            for code, pattern, note in RULES:
                if pattern.search(line):
                    findings.append({'file': str(path.relative_to(root)), 'line': line_no, 'rule': code, 'note': note})
    return findings

def main():
    ap = argparse.ArgumentParser(description='KHAOS Slop heuristic scan; findings require human verification.')
    ap.add_argument('path', nargs='?', default='.', help='Directory to scan')
    ap.add_argument('--json', action='store_true', help='Output JSON')
    args = ap.parse_args()
    root = Path(args.path).resolve()
    if not root.is_dir():
        ap.error(f'Not a directory: {root}')
    findings = scan(root)
    if args.json:
        print(json.dumps({'warning_count': len(findings), 'findings': findings}, ensure_ascii=False, indent=2))
    else:
        print(f'KHAOS heuristic warnings: {len(findings)} (not a verdict)')
        for item in findings:
            print(f"{item['file']}:{item['line']} [{item['rule']}] {item['note']}")
    # Always 0: never block a build based on aesthetic heuristics alone.

if __name__ == '__main__':
    main()
