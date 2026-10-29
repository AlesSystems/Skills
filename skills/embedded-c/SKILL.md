---
name: embedded-c
description: Write and review C for a Raspberry Pi host program. Require fixed-width types, checked errors, and the warning flags in this skill. Use when the program that touches the Pi is written in C, including GPIO, I2C, SPI, or UART access.
---

# Embedded C

Write the Pi program in C. Read [raspberry-pi](../raspberry-pi/SKILL.md) first. If `Board` or `GPIO library` in the hardware record is `unknown`, do not call GPIO, I2C, SPI, or UART. You may still write C that does not touch hardware.

## Types and errors

Use `stdint.h` names such as `uint32_t` for sizes and for device register values. Check every library call and every syscall result. Return that error to the caller. After a failed `open`, `read`, `write`, or `ioctl`, keep `errno` available to the caller.

Initialize every pointer before use. Close or free each resource on the success path and on the error path. Mark a device register `volatile` only when the program reads or writes a memory-mapped register. Do not mark an ordinary variable `volatile` so two threads can share it. Use an atomic or a mutex when more than one thread reads and writes the same variable.

## Build

If `gcc` or `clang` is installed on the machine that builds the program, compile with all of these flags.

```bash
-Wall -Wextra -Wpedantic -Wconversion -Wshadow
```

Run AddressSanitizer and UndefinedBehaviorSanitizer when the program can run without the Pi. Skip both sanitizers when the binary must run on the Pi and that toolchain has no sanitizer runtime. Say that you skipped them.

Run `clang-tidy` and `cppcheck` when those tools are installed. If a tool is missing, say so. Do not install a GPIO library to make the build pass.

## Stop

Do not add a hardware call that the hardware record does not name. Do not claim the binary works on the Pi. A clean host build is a host result. The physical result comes from [hardware-test-report](../hardware-test-report/SKILL.md).
