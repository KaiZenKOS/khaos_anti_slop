# Writing that does not sound manufactured

This is an editing checklist, not an AI-authorship detector. It does not promise to
make text indistinguishable from human writing. A writer's own voice outranks these
heuristics. Use it for READMEs, documentation, UI labels, landing pages and pitches.

## Pass 1 — Keep the substance

Before rewriting, identify the intended reader, what they need to know, and which
claims are demonstrably true. Preserve names, facts, quantities, scope, technical
terminology and citations. Never make up numbers, users, clients, research or
benchmarks to make a sentence feel concrete. Keep honest uncertainty.

## Pass 2 — Remove the tells, not the personality

Challenge these *patterns when overused*, never as blanket bans:

- Empty openings: "In today's fast-paced world", "In the ever-evolving landscape".
- Inflated language: "revolutionary", "game-changing", "next-gen", "unlock the power".
- Artificial contrasts: "It's not X, it's Y" / "Ce n'est pas X, c'est Y".
- Empty claims: "seamless", "robust", "innovative" without specific evidence.
- Identical sentence lengths, uniformly polished paragraphs and forced three-part lists.
- Repetitive em dashes, bolding and colons used as a substitute for clear structure.
- Overly cheerful intros and mechanical sign-offs or recap conclusions.
- Generic metaphors (journey, ecosystem, magic) when an exact noun exists.
- Fake authority: invented testimonials, unsourced statistics or claims of compliance.
- Sloppy French or literal translations that ignore normal idioms and context.

Do not penalize natural uses of these words or punctuation. You are editing a text,
not classifying its author.

## Pass 3 — Give the text a point of view

- Lead with what the tool *does*, not how ambitious it sounds.
- Use tangible verbs and examples. Prefer "flags duplicate events" over
  "revolutionizes workflow management".
- Vary rhythm when it helps reading; do not force quirky phrasing or artificial mistakes.
- Keep appropriate technical detail in docs, without drowning the reader in jargon.
- Match the requested voice: precise/technical, direct, warm, editorial, etc.
- Maintain consistent naming and terminology across README, interface and docs.
- If a short sentence works, stop. A concise explanation is better than padding.

## Pass 4 — Integrity check

Re-read the edited version against the original. Confirm that no feature, result,
compatibility promise, benchmark, quote or attribution has appeared from nowhere.
If it has, cut it. Preserve valid nuance, user-authored phrasing and sourced claims.

## Before/after examples

**EN, before:** "Unlock the future of seamless AI-powered development with our
revolutionary, next-generation solution."

**EN, after:** "A review skill that catches generic UI, unnecessary code and claims
your demo cannot back up."

**FR, before:** "Révolutionnez votre productivité grâce à notre solution innovante
et intuitive qui repousse les limites du possible."

**FR, after:** "Un skill de revue pour repérer les interfaces génériques, le code
superflu et les démonstrations qui promettent plus qu'elles ne font."

## If an external Humanizer skill is available

An optional dedicated editing pass can be done with `blader/humanizer` or
`hannsxpeter/humanizer`, provided the actual installed skill is reviewed and its
instructions do not conflict with the user's brief. **KHAOS has no external runtime
dependency** and doesn't bundle, impersonate or auto-install either project.

References and inspiration (not copied source):
- https://github.com/blader/humanizer
- https://github.com/hannsxpeter/humanizer
- https://github.com/ameenmo/humanize-skill
