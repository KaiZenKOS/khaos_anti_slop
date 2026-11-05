# Contributing

Please open a focused issue or pull request with a reproducible example. If a
rule flags legitimate design or code, include that case too. False positives matter.

- Keep the skill portable and its instructions short enough to use.
- Do not add rules that ban a font, color, framework or punctuation mark outright.
- Treat any scanner output as a **warning**, not a definitive judgment.
- Do not add unverified performance numbers, invented UX research or testimonials.
- Add a concrete evaluation prompt for behavioral changes; run the Python checks.
- Cite external projects for inspiration. Don't paste third-party skill content in
  without checking its licence and attribution requirements.

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```
