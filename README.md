# Ales Skills

Reusable skills maintained in [AlesSystems/Skills](https://github.com/AlesSystems/Skills).

## Available skills

| Skill | Purpose |
| --- | --- |
| [landing-page-art-direction](skills/landing-page-art-direction/SKILL.md) | Turn project context and reference ideas into one original design brief and desktop/mobile wireframes, before implementation. |
| [software-idea-discovery](https://github.com/tutoria-hub/agent-library/blob/main/skills/software-idea-discovery/SKILL.md) | Interview the developer, research their preferred market, identify underserved needs, and assess differentiated software opportunities with future scenarios and validation experiments. |
| [product-demo-js](https://github.com/tutoria-hub/agent-library/blob/main/skills/product-demo-js/SKILL.md) | Create editable Remotion product demos with JavaScript, real screenshots, licensed music, and rendered-media checks. |
| `3d-ui-design` (publication pending) | Design, implement, and critique interactive 3D web interfaces, including model sourcing, scene integration, accessibility, and browser verification. |

`software-idea-discovery`, `product-demo-js`, and `3d-ui-design` are maintained in the separate, private [agent library](https://github.com/tutoria-hub/agent-library); access to that repository is required to read their instructions. `3d-ui-design` currently lives at `skills/3d-ui-design/SKILL.md` in the local library checkout; its GitHub link will be added after publication.

The [Frame product demo example](examples/product-demo-js/README.md) provides an editable Remotion walkthrough, local screenshot captures, a pinned dependency lockfile, and rendered-media checks. Obtain the documented music track from its official provider before rendering; raw music and generated output are excluded from Git.

## Use

Point your agent at the skill’s `SKILL.md`, or invoke `$landing-page-art-direction`, `$software-idea-discovery`, `$product-demo-js`, or `$3d-ui-design` after making the corresponding skill available in your agent’s skill environment.

Example request:

> Use landing-page-art-direction to plan the Esmer Market homepage only. The main goal is store visits. Keep the shared header, footer, and other pages unchanged. Inspect the existing project and use these reference websites for ideas, not copying: [add links]. Ask up to three questions, one at a time, only for missing decisions. Finish with a brief and simple desktop/mobile wireframes; do not implement yet.

Keep each project’s brand choices, reference collection, and resulting brief in that project. This repository contains the reusable method. The skill requires no other skills or specific browser provider; it records limitations when references cannot be inspected.

Adding a skill here does not install it into an agent runtime. The existing third-party agent library remains separate.
