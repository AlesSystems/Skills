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

## Completed publication and loader checks

- Independent destination review: PASS, no findings, patch ID
  `bc41a65f822837c3230f698aed206efebb1d0533`.
- Independent source review: PASS+NOTES, no actionable findings, patch ID
  `bfff131e21d90f3ea3400f12bd88c08912dcdeba`.
- Destination [PR 4](https://github.com/AlesSystems/Skills/pull/4) merged first,
  preserving workstream commits `7bde407`, `45612d7`, and `a2264c8`.
  Merge: `85bba444fa850b363dcf62d5c51637a6eb87adfe`.
- Source [PR 25](https://github.com/tutoria-hub/agent-library/pull/25) merged next,
  preserving both revert commits. Merge:
  `aeba1b37503fb2af935f297a3c91034785bc54a2`.
- Both primary checkouts are on their reconciled main branches. The source main
  tree and primary working tree exactly equal the pre-contribution baseline.
- The primary destination passes the migration verifier and Poteto fingerprints.
  Its submodules match both pins, have independent objects, and remain clean.
- Impeccable's ignored bundle was rebuilt in the destination from its pinned
  transformer. Both canonical loading adapters run successfully and idempotently.
- All six owned Codex links resolve to the primary destination. All 67 unrelated
  Codex links retain their original targets.
- The source doctor exposed two stale Claude links to removed imported skills.
  Those existing Poteto/Impeccable links now resolve to the destination;
  all 57 other Claude links retain their original targets. Source doctor passes
  with 55/55 baseline links and strict validation passes with 54 catalog entries.
- The final primary source suite passes 64/67 tests. Two remaining failures
  are the unchanged baseline `grok-build-mini` contracts; the third test expects
  a lowercase `origin/main` report even though the baseline CLI skips Cursor
  Origin checks on this GitHub-only checkout. The source doctor itself passes.
- Global Codex guidance and the destination README/AGENTS name AlesSystems/Skills
  as the default owned library. No provider settings or plugin caches changed.
- The existing Pi hardware worktree remains clean at `973e97f`.

Restart Codex to load the source and loader changes. Historical branches and PRs
remain available; the rollback preserves shared history rather than erasing it.
