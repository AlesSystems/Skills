---
name: gpio-safety-review
description: Block Raspberry Pi wiring and GPIO execution until voltage, current, pin map, and safe idle state are known. Use before asking someone to connect a pin, power a load, or run a program that drives GPIO.
---

# GPIO safety review

Read [raspberry-pi](../raspberry-pi/SKILL.md) and use its hardware record. For each part in `Connections` that is not a wire or the Pi, read the part record. If that record does not exist, build it with [datasheet-research](../datasheet-research/SKILL.md) before you answer the checks.

Run this review before any step that asks the person with the board to wire a pin, apply power, or run a program that changes a GPIO.

## Checks

Answer each line `pass`, `fail`, or `unknown`. Use the hardware record and the part records only. `unknown` means those records do not say. Do not fill a line from a tutorial or from memory.

```text
3.3 V logic?
Correct GPIO numbering?
Current limits respected?
Correct resistor?
Motor or relay driver required?
Flyback diode required?
Common ground?
Safe startup state?
Safe shutdown state?
```

`3.3 V logic?` is `pass` only when `Logic voltage` in the hardware record is `3.3 V` and every part record's `Logic voltage` is `3.3 V`. Any other stated voltage is `fail`. Do not assume 3.3 V when a field is `unknown`.

`Correct GPIO numbering?` is `pass` only when every pin name in the program uses the record's `Pin numbering`.

`Current limits respected?` is `pass` only when each GPIO current is inside the limits in the part records.

`Correct resistor?` is `pass` when the fitted resistor matches the part record, or when that record requires no resistor and none is fitted.

`Motor or relay driver required?` is `pass` when `Connections` has no motor, relay, or solenoid, or when that load has a driver in the records. It is `fail` when a bare GPIO drives that load.

`Flyback diode required?` is `pass` when no inductive load is connected, or when the part record's diode is present. It is `fail` when an inductive load is missing a diode the part record requires.

`Common ground?` is `pass` only when `Ground shared` is `yes`.

`Safe startup state?` and `Safe shutdown state?` are `pass` only when the records name the idle level of every driven pin for that event.

## Block

Stop the physical step when any line is `fail` or `unknown`.

A `fail` on the driver line or the flyback line blocks the step even when the program compiles. Tell the person with the board not to connect that load.

Do not propose a pin number, a resistor value, or a voltage in this review. Put those facts in the hardware record or the part record after someone reads the board and the datasheet.
