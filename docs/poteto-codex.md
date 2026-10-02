# Poteto Mode in Codex

Invoke `$poteto-mode <task>` after restarting Codex. To call a dependency through the same adapter, say `$poteto-mode use arena to compare these designs`, or name another bundled workflow. Only the entry point is exposed globally; dependency names do not replace existing installed skills.

## Source and installation

- Canonical entry point: `skills/also/poteto-mode/SKILL.md`.
- Codex loading link: `~/.codex/skills/poteto-mode` points at the canonical entry point directory.
- Source: `refs/cursor-plugins`, a Git submodule from `https://github.com/cursor/plugins`.
- Pin: `7366ac128bdf95f45e6734f412b49a4031800169`.
- Imported workflow versions: pstack 0.15.1 and cursor-team-kit 1.2.0.
- Dependency coverage: 47 pstack skills, 18 cursor-team-kit skills, three dormant Benny automation skills, 23 Poteto playbooks, and four agent prompts. All 187 files in the two plugin directories are fingerprinted.
- The entire upstream repository is present as a submodule, but other plugins are not exposed or installed. The two dependency directories are the verified workflow boundary.

The source remains upstream-owned. The wrapper and adapter are locally maintained by Altan. Licenses and author attribution are retained in the submodule. No copies are installed into runtime/plugin caches.

After cloning this library on another machine, initialize the pinned source and add the one loading link:

```sh
git submodule update --init refs/cursor-plugins
python3 skills/also/poteto-mode/scripts/poteto.py verify
python3 adapters/codex/link-poteto.py --dry-run
python3 adapters/codex/link-poteto.py
```

The link helper is deliberately scoped to Poteto Mode. It does not prune or replace other skills. This library revision no longer supplies the old `Codex-sync` command.

## Codex adaptations

The adapter translates native delegation and agent roles, model selection, bounded concurrency, tool lookup, transcript access, task scratch paths, goals, heartbeat automations, and local-only completion. Cursor cloud agents become local isolated worktrees when appropriate. Host authorization and repository rules remain authoritative.

The executable adapter adds a GitHub CLI frontier path so orchestration does not require Graphite. It retains upstream locking, generation tracking, and verification ledgers. The plan checker accepts Codex terminology. Worktree audit no longer searches Cursor history by default.

Runtime dependencies are prepared in a task-local working directory, separate from canonical skills. The first preparation needs Node/npm and network if Bun is absent. Bun 1.4.2 is pinned for the fallback installation. Upstream runtime dependencies use its frozen lockfile. No monitor, background automation, or external connector is enabled by installation.

## Models and practical limits

All roles inherit the selected Codex model. Panels use independent agents within the host's actual concurrency limit. This preserves review separation but is not cross-family review. Available models may be configured in `skills/also/poteto-mode/references/models.json` after validating the current host's model names.

Cursor-specific cloud VM placement, Claude/Grok model access, and sticky-mode UI metadata are not reproduced. Multi-turn behavior comes from the task's instructions; durable scheduling requires native Codex automation requested by the user. Live GitHub, UI, simulator, and connector work still requires the relevant project's tools and authentication.

## Verification

Runnable checks in this repository:

```sh
git diff --check
python3 skills/also/poteto-mode/scripts/poteto.py verify
python3 adapters/codex/link-poteto.py
python3 skills/also/poteto-mode/scripts/poteto.py run --work-dir <task-scratch> test
python3 skills/also/poteto-mode/scripts/poteto.py run --work-dir <task-scratch> typecheck
python3 skills/also/poteto-mode/tests/test_adapter.py --work-dir <task-scratch> -v
```

The source toolkit plus GitHub frontier tests passed 58 tests. Four Python integration checks passed, covering skill resolution, canonical-directory protection, real orchestration CLI behavior with fake GitHub responses, and decision-log argument handling. The GitHub adapter and tests also passed strict TypeScript checking. The helper's `typecheck` command covers `watch-pr`; from the prepared scripts directory, also run the installed TypeScript CLI with `--noEmit --strict --skipLibCheck --target esnext --module esnext --moduleResolution bundler --allowImportingTsExtensions --types bun-types orch/github-frontier.ts orch/github-frontier.test.ts` to cover the authored orchestration adapter. The plan checker accepted the translated upstream program template and rejected the same template with a missing coverage lane. The Codex link is idempotent, and all wrapper Markdown links resolve.

The bundled skill-creator validator passed using the system Python with PyYAML. The upstream submodule stayed clean.

An independent agent also executed the installed workflow against a disposable Python bug fixture. It loaded the pinned dependencies, used bounded subagents for investigation and implementation, added a regression assertion, captured `1 != 1.5` before the fix, changed one division operator, reviewed the delegated change, and reran the public call and all three tests successfully. The parent reran the three tests independently. The fixture had no Git history and used standard-library unittest; those environment limits were disclosed without creating external work.

## Original import evidence

The original import in tutoria-hub/agent-library passed strict catalog validation
with 45 entries. Its doctor retained a pre-existing agents-alias failure.
Those `bin/library` commands belong to the original repository and are not
available here. No live merge, external message, deployment, or overnight run
was used as an installation test.

Current transfer checks are recorded in
[the migration evidence](../work/poteto/skills-migration/acceptance.md).
