# Owned skill migration — 2026-10-02

The user selected AlesSystems/Skills as the default owned skill library and
requested transfer and rollback of their contributions to tutoria-hub/agent-library.
The source scope is merged PRs [23](https://github.com/tutoria-hub/agent-library/pull/23)
and [24](https://github.com/tutoria-hub/agent-library/pull/24), authored by AltanEsmer.
The [plan](plan.md) defines completion; [manifest.json](manifest.json) records the
source hashes, destination preservation hashes, and dependency pins.

## Acceptance evidence before publication

- `python3 work/poteto/skills-migration/verify.py`: 236 exact source files,
  25 unchanged destination files, the canonical Impeccable link, and two exact
  dependency pins pass. Five documentation/catalog adaptations are listed explicitly.
- All seven catalog skills pass the bundled Codex skill validator.
- `python3 tests/test_diagram_design.py`: resource links and Mermaid edge regressions pass.
- Diagram `self_check.py`: all 148 `assets/example-*.html` files pass.
- Poteto `verify`: 68 skills, 187 fingerprinted files, and 95 routes match the pin.
- Prepared Poteto toolkit: 58 Bun tests and four Python integration tests pass.
- Both watch-pr and the authored GitHub frontier adapter/tests pass TypeScript checking.
- Both upstream submodule working trees are clean and use independent object stores.
- Source revert commits `4a85bda` and `56426c8` restore the exact tree of `27f5191`,
  the first parent of PR 23. `git diff --exit-code 835d3db^1 HEAD` is empty.
- Source `bin/library validate --strict` passes with 54 catalog entries.
- The source worktree library suite runs 67 tests: 63 pass, four fail. Two failures
  concern unchanged baseline `grok-build-mini` contracts; two compare machine
  loader aliases against this temporary worktree. Primary-checkout checks follow
  reconciliation. Unrelated source contracts/provider wiring are not repaired here.

## Limits and retained source material

This transfers existing methods and assets; it does not claim a fresh browser
execution of the 3D skill or a new live research/Remotion run. Existing destination
examples and their acceptance records remain unchanged. Original import evidence
is preserved and labeled historical; unavailable source-only CLI commands are
removed from current installation instructions.

Transferred diagram examples retain original CRLF bytes. With `cr-at-eol`,
Git's whitespace check still reports two inherited lines in
`example-queue-animated.html:298` and `references/onboarding.md:84`; both hashes
match the source. Checks pass for other paths. These lines are preserved to
avoid mixing formatting changes into a faithful move.

Publication, main-branch reconciliation, and native loader/default-guidance
checks follow independent review. Only the six direct owned loader links are
retargeted; unrelated sources, provider settings, and worktrees are preserved.
