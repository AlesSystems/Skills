---
name: datasheet-research
description: Build a part record from the manufacturer datasheet before a Raspberry Pi circuit uses that part. Use when adding a sensor, chip, module, LED, motor, or other part, or when voltage, current, pinout, timing, or a register map is needed.
---

# Datasheet research

Build one part record for each new component. Prefer the manufacturer datasheet. A tutorial, a forum post, or a blog does not fill a field. If you cannot open the official document, write the URL that failed and leave the missing fields as `unknown`. Do not copy ratings from memory.

## Identify the part

Require the manufacturer and the exact part number printed on the device, or stated by the user. A family name is not enough when the package or the breakout board can change the pinout. If the package or the breakout board is unknown, stop and ask the person who can see the part.

## Part record

```text
Manufacturer:
Part number:
Package or board:
Datasheet URL:
Datasheet date or revision:
Supply voltage operating range:
Absolute maximum voltage:
Absolute maximum current:
Logic voltage:
Pinout:
Protocol:
Timing:
Register map:
Init sequence:
Known failure conditions:
```

Copy a number or a pin name only from the datasheet you opened in this task. Mark a field `unknown` when that datasheet does not state it.

## Stop

Stop when the part record is written. Do not design the circuit while `Absolute maximum voltage`, `Absolute maximum current`, or `Pinout` is `unknown`. [gpio-safety-review](../gpio-safety-review/SKILL.md) reads this record. Do not start that review unless the user asked for it.
