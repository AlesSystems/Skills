---
name: raspberry-pi
description: Record the Raspberry Pi board, OS, pin numbering, logic voltage, and wiring before any GPIO, bus, or deploy work. Use when the user mentions a Raspberry Pi, Pi GPIO, or hardware on a Pi and the board revision or OS is unknown or unverified.
---

# Raspberry Pi

Collect a hardware record before you choose a pin, a library, a voltage, or a deploy step. Stop at the record. Do not write the application in this skill.

## When to run

Run this skill when the task touches a Raspberry Pi and any of these are missing, or only remembered from an earlier chat.

- Board model and revision
- Operating system and kernel
- Pin numbering scheme
- Logic voltage
- Wired parts, and the header pins they use

If the person with the board can see it, ask for the missing fields. If nobody can observe the board, stop. Leave each missing field as `unknown`.

## Hardware record

Write this block. Fill a field only from what you observed or what the user stated in this task. Copy every other field as `unknown`. Do not infer a model, a 40-pin header, BCM numbering, 3.3 V logic, or a GPIO library from the words "Raspberry Pi".

```text
Board:
Revision:
OS:
Kernel:
User:
Pin numbering:
Logic voltage:
Power:
Connections:
Ground shared:
GPIO library:
```

Set `Pin numbering` to `BCM`, `physical`, `wiringPi`, or `unknown`. Set `Ground shared` to `yes`, `no`, or `unknown`. When a datasheet or a measurement in this task shows 3.3 volts, write `Logic voltage` as `3.3 V`. Do not write that value from the words "Raspberry Pi" alone. In `Connections`, name each wire the person with the board can see, including ground. Leave `GPIO library` as `unknown` until this project already uses one, or the user names one.

## Stop

Stop when the record is written. If `Board`, `Pin numbering`, `Logic voltage`, or `Connections` is `unknown`, do not pick a pin, do not name a GPIO library, and do not tell anyone to power a circuit.

Do not start another skill unless the user asked for that work. Safety review is [gpio-safety-review](../gpio-safety-review/SKILL.md). C for the Pi is [embedded-c](../embedded-c/SKILL.md).
