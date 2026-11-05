---
name: khaos-anti-slop
description: >-
  KHAOS Anti Slop: quality skill for hackathon and production work. Use when
  generating, modifying or reviewing UI/UX, frontend, backend, APIs, ML integrations,
  pitch copy and demos. Prevent generic AI-template design, fake functionality,
  speculative abstractions, inefficient algorithms and unverifiable claims.
metadata:
  author: KHAOS / VCA team
  version: "1.1.0"
---

# KHAOS Anti Slop

Design with intent. Code with restraint. Write like you mean it. Prove what works.

## Objective and precedence

Produce a *specific, functional, understandable* result, not polished-looking filler.
The explicit product brief, real constraints, accessibility, security and user intent
outrank stylistic preferences. Do not blindly prohibit a font, icon, color, shadow or
layout: flag *unjustified defaults and repetitive combinations*. Do not invent facts.

**Use this skill in two passes:** once *before implementation* to prevent default-template
choices, then *after implementation* to review the real artifact. For design tasks
read [references/visual-red-flags.md](references/visual-red-flags.md). For code tasks
read [references/code-performance.md](references/code-performance.md). For writing tasks
read [references/writing-humanizer.md](references/writing-humanizer.md). For test prompts
read [references/evaluation.md](references/evaluation.md).

## 0. Understand the task (do not code yet)

- State in one sentence: **user + problem + observable outcome**.
- Identify the existing stack, conventions, assets and data sources. Inspect relevant
  files and the flow actually affected before changing code.
- Decide the **one complete end-to-end path** to deliver. Drop work not needed for it.
- Label data/integrations as REAL, SYNTHETIC, MOCKED or UNVERIFIED where applicable.
- If no design reference exists, select a clear editorial/product direction and explain
  one reason for each major choice (hierarchy, typography, layout and color).

## 1. The KHAOS/Ponytail-inspired ladder (smallest safe solution)

Use the minimalist *reasoning*, not Ponytail's source code or proprietary identity:

1. **Don't build it** if the requested outcome does not require it (YAGNI).
2. **Reuse existing code** and project patterns, without duplicating a subsystem.
3. **Use native platform/stdlib** features before adding a dependency.
4. **Use an existing compatible dependency** before inventing a library or wrapper.
5. **Add the smallest justified code** for real behavior, with clear boundaries.
6. **Keep essentials**: input validation, errors, authorization, data safety,
   keyboard access and useful tests are not optional optimizations.
7. **Stop once verified**. No unrelated refactors, speculative configuration,
   factories with a single caller or abstractions for hypothetical future needs.

If the new abstraction or dependency is necessary, explain *which current requirement*
justifies it. Do not optimize for line count at the cost of clarity.

## 2. UI/UX: recognizable, intentional, usable

- Start from *content and tasks*, not from a generic "AI startup landing page" template.
- Establish a compact visual system: type hierarchy, grid/spacing, palette, interactive
  states and mobile breakpoints. Reuse the project's real brand assets.
- Avoid the **30 recurrent visual/content signatures** collected from the team's
  screenshots by default. They are individually classified in
  [references/visual-red-flags.md](references/visual-red-flags.md): most are warnings,
  not prohibitions; fake testimonials and deceptive claims are hard failures.
- Extra community red flags: generic centered hero without substance, unrelated stock
  imagery, cards with no story, faint text/low contrast, decorative metrics, copy that
  says nothing, unusable mobile navigation, inconsistent page hierarchy.
- Icons: use only when they clarify meaning; Lucide is acceptable when justified.
  Three cards, a gradient, rounded corners or purple *can be correct* for the brand.
- Every CTA must do something real or be clearly disabled/labeled as a prototype.
- Every screen should include sensible loading, empty, error and success feedback
  where appropriate. Skeleton loaders are *one option*, not a universal requirement.
- Show real product screens or an honestly labeled demonstrator, not a static facsimile.
- If terms/privacy policies are legally needed, implement appropriate links/content;
  don't fabricate legal assurances or pretend a placeholder is compliant.
- Inspect actual mobile and desktop output, not only source code.

## 3. Code: simplicity, performance, correctness

- Require each non-trivial algorithm or endpoint to declare the input size `n` (and
  other parameters if necessary), expected load and **time/space complexity**.
- **Aim for O(n) or better when the problem permits it.** Never claim O(n) is a
  universal rule: comparison sorting is typically O(n log n); graph traversals may
  be O(V+E); necessary pairwise comparisons may be O(n²). Optimize based on sizes,
  constraints and measured hotspots, not as a reflex.
- Review accidental O(n²): `find`/`includes`/`filter` nested inside a `map`/loop,
  repeated scans for joins, repeated parsing, client-side N+1 network/database calls.
  Consider `Map`/`Set`, batched queries or an index where justified.
- State the time **and** memory tradeoff before changing a data structure.
- No invented endpoints, test results, model accuracies, performance numbers or
  successful integrations. No fake API responses passed off as live data.
- Preserve security: validate at trust boundaries, keep secrets out of code/client,
  authorize side effects server-side, and consider idempotence for retries.
- Change only relevant files, avoid unexplained huge diffs, remove unused code and
  dependencies, and write a small test for risky branches/parsers/loops/security.
- For ML: distinguish training from inference; document dataset provenance, model
  version, hardware assumptions and evaluated metrics, and never fake evaluation.

## 4. Writing: humanizer pass + honest product copy

Reject vague claims without observable evidence: "revolutionary", "next-gen",
"seamless", "game-changing", "AI-powered" used without concrete explanation.
Avoid repetitive rhetoric: "It's not X, it's Y" as a default template; em dashes
as filler; fake counters, fake company logos, invented pricing logic, fake reviews,
invented traction, inaccessible "live" dashboards, sham testimonials and metrics.

Write: **who -> what friction -> actual action -> verifiable output -> limit**.
A hackathon mock is legitimate when prominently labeled *demo/synthetic*.

When drafting or reviewing READMEs, landing-page copy, documentation, pitches or UI
microcopy, apply the standalone [writing-humanizer guide](references/writing-humanizer.md).
Edit for specificity, correct facts and a recognizable voice, *not* to defeat an
AI detector. Preserve terms, citations and the writer's deliberate style; remove
mechanical repetition, fake enthusiasm and empty contrast formulas. If a factual
claim lacks evidence, remove it or explicitly qualify it. Do not invent case
studies or promises to make a paragraph sound more convincing.

## 5. Verification gate — mandatory before saying "done"

1. **Functionality:** run/inspect the *real* critical path; errors and edge case.
2. **Design:** assess distinctiveness, hierarchy, consistency and small-screen state.
3. **Performance:** note relevant Big-O; verify with an input-sized test or benchmark
   if scale matters. Never claim a measured speedup without a real measurement.
4. **Safety and honesty:** no credential leakage, fabricated evidence, misleading mocks.
5. **Scope:** any new dependency, file or abstraction without clear benefit?
6. **Communication:** enumerate what was tested versus not tested; humanize public-facing copy without changing its meaning.

### Score (0, 1, 2 each; target >= 10/12)

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Product specificity | Generic | Some context | Clear user/problem/outcome |
| Functional behavior | Static/fake | Partial | Critical flow tested |
| Visual/writing intent | Template/cliche | Some decisions | Coherent and differentiated |
| Simplicity | Speculative bloat | Some waste | Smallest safe implementation |
| Algorithmic fit | Ignored/wasteful | Reasoned only | Complexity justified and relevant hotspot checked |
| Honesty & verification | Claims untested | Limits noted | Checks and limitations explicit |

**Hard fail even with 10/12:** fabricated social proof, secrets in output,
misrepresented mocks, a core CTA that pretends to work, an unreviewed critical
security change. Score only after actual inspection, not from intention.

## 6. Response format for each implementation/review

Keep it brief, useful and verifiable:

- **Built / changed:** specific files and observable behavior.
- **Why this approach:** one design choice + reuse/new dependency justification.
- **Complexity:** relevant time/space Big-O, or "not performance-sensitive" with reason.
- **Verified:** exact commands/browser states/results; say "not run" if not run.
- **Synthetic/limits:** demo data, missing integrations, assumptions and next risk.
- **Intentionally skipped:** work deferred because it was not necessary now.

If the user requests only code, keep this footer compact and outside the code.
