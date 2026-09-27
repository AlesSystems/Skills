# Ales Skills

Reusable skills maintained in [AlesSystems/Skills](https://github.com/AlesSystems/Skills).

## Available skills

| Skill | Purpose |
| --- | --- |
| [landing-page-art-direction](skills/landing-page-art-direction/SKILL.md) | Turn project context and reference ideas into one original design brief and desktop/mobile wireframes, before implementation. |
| [raspberry-pi](skills/raspberry-pi/SKILL.md) | Record the Pi board, OS, pin numbering, voltage, and wiring before any hardware step. |
| [embedded-c](skills/embedded-c/SKILL.md) | Write the Pi program in C, with checked errors and the warning flags in the skill. |
| [datasheet-research](skills/datasheet-research/SKILL.md) | Fill a part record from the manufacturer datasheet, or leave the field unknown. |
| [gpio-safety-review](skills/gpio-safety-review/SKILL.md) | Block wiring and GPIO execution while voltage, current, or idle state is unknown. |
| [hardware-debug](skills/hardware-debug/SKILL.md) | Diagnose a Pi failure in layers before changing code. |
| [hardware-test-report](skills/hardware-test-report/SKILL.md) | Issue one physical test and require a structured result from the person with the board. |

The hardware skills do not assume a Pi model, a pin map, or a GPIO library. I2C, SPI, UART, deploy, and hardware-in-the-loop skills stay out until a hardware record names the board and the parts.

## Use

Point your agent at the skill’s `SKILL.md`, or invoke `$landing-page-art-direction` after making it available in your agent’s skill environment.

Example request:

> Use landing-page-art-direction to plan the Esmer Market homepage only. The main goal is store visits. Keep the shared header, footer, and other pages unchanged. Inspect the existing project and use these reference websites for ideas, not copying: [add links]. Ask up to three questions, one at a time, only for missing decisions. Finish with a brief and simple desktop/mobile wireframes; do not implement yet.

Keep each project’s brand choices, reference collection, and resulting brief in that project. This repository contains the reusable method. The skill requires no other skills or specific browser provider; it records limitations when references cannot be inspected.

Adding a skill here does not install it into an agent runtime. The existing third-party agent library remains separate.
