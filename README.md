# Ales Skills

The default library for our own reusable skills is [AlesSystems/Skills](https://github.com/AlesSystems/Skills). Create and maintain new owned skills here.

## Available skills

| Skill | Purpose |
| --- | --- |
| [landing-page-art-direction](skills/landing-page-art-direction/SKILL.md) | Turn project context and reference ideas into one original design brief and desktop/mobile wireframes, before implementation. |
| [software-idea-discovery](skills/software-idea-discovery/SKILL.md) | Interview the developer, research their preferred market, identify underserved needs, and assess differentiated software opportunities with future scenarios and validation experiments. |
| [product-demo-js](skills/product-demo-js/SKILL.md) | Create editable Remotion product demos with JavaScript, real screenshots, licensed music, and rendered-media checks. |
| [3d-ui-design](skills/3d-ui-design/SKILL.md) | Design, implement, and critique interactive 3D web interfaces, including model sourcing, scene integration, accessibility, and browser verification. |
| [diagram-design](skills/diagram-design/SKILL.md) | Create and verify architecture diagrams, charts, and other visual explanations with the retained templates and parser tools. |
| [poteto-mode](skills/also/poteto-mode/SKILL.md) | Run the pinned Poteto workflow through the Codex adapter, with its dependency skills resolved on demand. |
| [impeccable](docs/impeccable-codex.md) | Build and use the pinned Impeccable Codex design workflow. |

The migrated skills, adapters, dependency pins, and licenses live in this repository. The [migration record](work/poteto/skills-migration/plan.md) and its executable checks document the transfer.

The [Frame product demo example](examples/product-demo-js/README.md) provides an editable Remotion walkthrough, local screenshot captures, a pinned dependency lockfile, and rendered-media checks. Obtain the documented music track from its official provider before rendering; raw music and generated output are excluded from Git.

## Use

Point your agent at the skill's `SKILL.md`, or invoke its name after making it available in your agent's skill environment. Keep native Codex entries as symlinks to this checkout. Restart Codex after changing those entries.

Initialize the pinned dependencies with `git submodule update --init --recursive`. Follow [Poteto setup](docs/poteto-codex.md) and [Impeccable setup](docs/impeccable-codex.md) for those workflows. Their dependencies remain in this repository rather than separate installed skill copies.

Example request:

> Use landing-page-art-direction to plan the Esmer Market homepage only. The main goal is store visits. Keep the shared header, footer, and other pages unchanged. Inspect the existing project and use these reference websites for ideas, not copying: [add links]. Ask up to three questions, one at a time, only for missing decisions. Finish with a brief and simple desktop/mobile wireframes; do not implement yet.

Keep each project’s brand choices, reference collection, and resulting brief in that project. This repository contains the reusable method. The landing-page-art-direction skill requires no other skills or specific browser provider; it records limitations when references cannot be inspected.

Adding a skill here does not install it into an agent runtime. Keep unrelated library and plugin sources separate. They are not the default home for new owned skills.
