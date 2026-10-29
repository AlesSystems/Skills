---
name: hardware-debug
description: Diagnose a Raspberry Pi hardware failure in layers before changing code. Use when a program builds but the LED, sensor, bus, or pin does not match the expected physical result.
---

# Hardware debug

Do not edit the program as the first action. Name the last layer that has evidence, then the first layer that does not.

Read the latest report from [hardware-test-report](../hardware-test-report/SKILL.md) before you change a hypothesis. If no report exists, ask for one and stop.

## Layers

Walk in this order. Stop at the first layer that lacks evidence.

1. Build. The compiler finished, and the binary path is the one that was run.
2. Program execution. The process started, and the report includes stdout and stderr.
3. Operating system and permissions. The user can open the device node, and the report includes `dmesg`.
4. GPIO and device configuration. The hardware record from [raspberry-pi](../raspberry-pi/SKILL.md) names the pin numbering and the GPIO library. The report names the device node the program opened, or the program opens none.
5. Electrical connection. `Connections` matches what the person with the board checked, including ground.
6. Component functionality. A part record from [datasheet-research](../datasheet-research/SKILL.md) covers this component, and the person with the board observed the part itself.
7. Application logic. Only this layer may justify a code change.

## Change the code

Edit the program only when layer 7 is the first layer without evidence, or when the report shows that every lower layer passed. State the failed layer and the report fields that support that claim.

A clean compile does not pass layer 5 or layer 6.
