---
name: hardware-test-report
description: Write one Raspberry Pi physical test for the person with the board, and require their structured result. Use before asking someone to run a binary, watch an LED, or check a sensor on a Pi.
---

# Hardware test report

Read [raspberry-pi](../raspberry-pi/SKILL.md). If `Board`, `Connections`, or `Pin numbering` is `unknown`, do not issue a test. Ask for those fields first.

Issue one test. Use `HWT-001` for the first test in a project. Increment the number for each later test in that project.

## Test

```text
TEST HWT-NNN

Setup:
<one circuit, using names from the hardware record>

Run:
<command>

Expected:
<observable result>

Check:
[ ] program starts
[ ] <observable on>
[ ] <observable off>
[ ] timing matches Expected
[ ] no errors

Return every field in the report below.
```

Replace each placeholder from the hardware record and the part record. Remove a check that does not apply to this test. Do not add a pin, a resistor value, or a time interval that those records do not state.

## Report

The person with the board returns this block. Leave a field empty when they did not observe it. Do not write `Observed` yourself.

```text
Commit:
Board:
OS:
Connections:
Command:
Expected:
Observed:
stdout:
stderr:
dmesg:
Physical checks:
```

`Commit` is the git revision they built. `Physical checks` copies the checklist, with each box marked.

The returned block is the only physical evidence. A host test does not fill `Observed`. If `Observed` does not match `Expected`, use [hardware-debug](../hardware-debug/SKILL.md). Do not edit the program before that skill names the failed layer.
