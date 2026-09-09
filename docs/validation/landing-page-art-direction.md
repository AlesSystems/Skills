# First-version validation

Date: 2026-09-09

## Scenario

Plan a neighborhood grocery homepage with a store-visit goal, a directions CTA, Turkish/English content, static Next.js output, existing green branding, and real shop photographs. Keep the shared header/footer. Two reference descriptions supply food photography, left-aligned copy, and compact store information. Produce a brief and wireframes without implementation.

## Observed results

- Baseline without the skill: produced a plausible brief, but included “Open today · until 20:00” without a supplied closing time, vague font guidance, and only a desktop diagram.
- Independent run with the skill: labeled unavailable reference evidence, kept business details as placeholders, proposed specific colors/type/spacing, provided both wireframes and bilingual draft copy, preserved page scope, and did not implement.
- Missing-context scenario: asked one focused opening question about the offering and visitor action, with a recommendation, rather than inventing a business.
- Review found one inconsistency: prose placed the mobile visit card immediately after the CTA, while the diagram placed the photograph between them. The skill now explicitly requires a block-by-block comparison of prose and diagrams. That wording change has not received another independent behavioral run.

## Mechanical checks

- Skill-creator `quick_validate.py`: passed.
- Codex UI metadata: parsed successfully; short-description length and skill invocation in the default prompt checked.
- `git diff --check`: passed.

## Limits

These are small text-only smoke tests, not proof of repeatable design quality. No real reference websites were inspected during the simulation, and no rendered design was evaluated. The Esmer Market trial with the user's references remains the next practical evaluation. No website files or runtime skill installations were changed.
