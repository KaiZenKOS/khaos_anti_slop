# KHAOS Anti Slop

**An agent skill for work that holds up outside the chat.**

AI can build a page in minutes. That doesn't mean the page has a point, the code
is worth keeping, or the demo works. KHAOS Anti Slop reviews what agents ship:
**intentional interfaces, lean code, honest product claims and writing with a voice.**

It started as a quality checklist for a six-person hackathon team. It's now a small,
portable skill you can use in your own projects.

## What it checks

| Area | What KHAOS looks for |
| --- | --- |
| **UI & UX** | Template layouts, empty decoration, inaccessible states, weak hierarchy, missing real demos |
| **Code** | Premature abstractions, dependencies for simple jobs, unrelated refactors, missing error handling |
| **Performance** | Accidental quadratic loops, N+1 requests, repeated scans; time *and* memory trade-offs |
| **Writing** | Generic AI-sounding prose, exaggerated claims, repetitive rhythm, loss of the author's voice |
| **Trust** | Invented testimonials, misleading mocks, fake metrics, unchecked security assumptions |

A gradient isn't a crime. Neither is Lucide, Inter or a three-column layout. They're
problems when they're used because the agent had no better reason. The 30 visual
patterns collected by the team are **review prompts, not arbitrary bans**.

## Install

Clone this repository into a skill directory your agent scans. Keep the
folder name `khaos-anti-slop` and retain `references/`. For a shared team
project, install globally or copy the contents into the project; do not
accidentally commit a nested `.git` directory.

**Claude Code** (global installation):

```bash
git clone https://github.com/OWNER/khaos-anti-slop.git ~/.claude/skills/khaos-anti-slop
```

**Codex:**

```bash
git clone https://github.com/OWNER/khaos-anti-slop.git ~/.agents/skills/khaos-anti-slop
```

**GitHub Copilot with Agent Skills support** (project-scoped, copy contents
rather than creating a nested Git repository):

```bash
git clone https://github.com/OWNER/khaos-anti-slop.git /tmp/khaos-anti-slop
mkdir -p .github/skills/khaos-anti-slop
cp -R /tmp/khaos-anti-slop/SKILL.md /tmp/khaos-anti-slop/references /tmp/khaos-anti-slop/scripts .github/skills/khaos-anti-slop/
```

Replace `OWNER` with the actual GitHub account or organization **after publishing**.
Skill discovery depends on the tool/version. For agents without skills support, point
it at `SKILL.md` explicitly; these instructions alone do not modify any project.

## How to use it

Ask an agent that has the skill installed:

```text
Use KHAOS Anti Slop to review this project. Inspect the actual implementation,
not just screenshots. Identify the five highest-impact issues, distinguish real
bugs from subjective style concerns, and make the smallest safe changes.
Keep existing brand choices. Explain relevant Big-O trade-offs. Verify the main
user path and tell me what you could not test.
```

For writing:

```text
Use KHAOS Anti Slop to edit this README. Keep the facts and technical details;
remove generic AI phrasing, make it easier to read, and preserve my voice.
```

**Humanizer is built into the writing review** via [`references/writing-humanizer.md`](references/writing-humanizer.md).
You can also use a separate Humanizer skill if you install and review it yourself.
No external service or AI detector is required.

## Run the optional local checks

Python 3, standard library only:

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/audit_slop.py path/to/another/project
```

The scanner reports **heuristic warnings**, not a score for code quality, a
security audit or a reliable AI-authorship test. It doesn't automatically change
source files or block commits.

## What's in the repository

```text
SKILL.md
references/
  visual-red-flags.md      # 30 visual patterns, with exceptions
  code-performance.md     # simplicity, Big-O and resource trade-offs
  writing-humanizer.md    # editing, clarity and voice
  evaluation.md           # 9 comparison prompts
scripts/
  audit_slop.py           # optional heuristic scanner
  validate_skill.py       # packaging and coverage checks
tests/
  test_audit.py
```

## How to judge whether it helps

Give two runs of the **same agent** the same task and repository snapshot: one
without KHAOS, one with it. Compare the artifacts and test results, not how
confident the agent sounds. The evaluation guide includes nine prompts, including
cases where a supposedly "AI-looking" design choice is actually justified.

## Credits and scope

KHAOS Anti Slop is an independent skill. It borrows **ideas**, not source files,
from [Ponytail](https://github.com/DietrichGebert/ponytail) (keep solutions small),
[Humanizer](https://github.com/blader/humanizer) and
[Humanizer by hannsxpeter](https://github.com/hannsxpeter/humanizer)
(preserve meaning and individual voice), plus the team's visual references and
community design discussions. These are **not bundled dependencies** or
endorsements. This repo does not claim to identify whether a person or model
wrote a text.

## Licence

MIT. Contributions and practical test cases are welcome.

---

<details><summary>En français</summary>

KHAOS Anti Slop est un skill pour agents de développement. Il repère les
interfaces génériques, les fonctionnalités factices, le code inutilement complexe,
les coûts algorithmiques évitables et les textes qui sonnent creux. Il ne bannit
pas une couleur ou une bibliothèque par principe. Il cherche les choix sans raison,
les promesses sans preuve et les problèmes d'usage réels.

</details>
