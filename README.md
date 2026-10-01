# Ales Skills

Reusable skills maintained in [AlesSystems/Skills](https://github.com/AlesSystems/Skills).

## Available skills

| Skill | Purpose |
| --- | --- |
| [landing-page-art-direction](skills/landing-page-art-direction/SKILL.md) | Turn project context and reference ideas into one original design brief and desktop/mobile wireframes, before implementation. |

The [Frame product demo example](examples/product-demo-js/README.md) provides an editable Remotion walkthrough, local screenshot captures, a pinned dependency lockfile, and rendered-media checks. Obtain the documented music track from its official provider before rendering; raw music and generated output are excluded from Git.

## Use

Point your agent at the skill’s `SKILL.md`, or invoke `$landing-page-art-direction` after making it available in your agent’s skill environment.

Example request:

> Use landing-page-art-direction to plan the Esmer Market homepage only. The main goal is store visits. Keep the shared header, footer, and other pages unchanged. Inspect the existing project and use these reference websites for ideas, not copying: [add links]. Ask up to three questions, one at a time, only for missing decisions. Finish with a brief and simple desktop/mobile wireframes; do not implement yet.

Keep each project’s brand choices, reference collection, and resulting brief in that project. This repository contains the reusable method. The skill requires no other skills or specific browser provider; it records limitations when references cannot be inspected.

Adding a skill here does not install it into an agent runtime. The existing third-party agent library remains separate.
