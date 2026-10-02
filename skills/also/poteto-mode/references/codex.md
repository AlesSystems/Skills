# Codex execution adapter

Read this before upstream instructions. Apply these translations to every imported skill, playbook, agent prompt, code sample, and generated plan. Upstream files are preserved source, not a second host configuration. Session instructions and the user's authorized scope always govern.

## Paths and dependency resolution

The canonical bundle is `refs/cursor-plugins` beneath the AlesSystems/Skills root. Resolve the wrapper's real path before following links, since Codex loads it through a symlink. `python3 <wrapper>/scripts/poteto.py resolve <name>` prints a canonical absolute path.

- Bare skill names prefer `pstack`, then `cursor-team-kit`. `tdd`, `teach`, `how`, `architect`, and other names in this workflow mean the bundled versions. Do not silently substitute similarly named installed skills.
- Use `pstack:<name>` or `cursor-team-kit:<name>` for qualified skills. `playbook:<name>` selects one of the 23 Poteto playbooks. `agent:poteto-agent` and `agent:comment-sicko` resolve shipped role prompts.
- Relative links resolve from the file that contains them. A bare `playbooks/…` in a Poteto playbook means the Poteto skill's playbooks directory. Upstream `pstack/…` and `cursor-team-kit/…` paths start at the bundle root, not the user's project.
- `git show origin/main:pstack/…` means re-read this pinned bundle's file, not a nonexistent file on the target project's trunk. Project code and project instructions still come from the actual project revision under review.
- Cursor's built-in `create-skill` maps to the available Codex `skill-creator`. Read it when authoring. Its availability is a host dependency, not an upstream file.
- No third-party connector is implicitly installed or authenticated. Discover available tools when `why`, `recall`, or other source-reading workflows need them. Record unavailable evidence sources rather than fabricate results.

## Native tools

Translate intent to the actual schema exposed by the host. Never call a tool just because its name appears upstream.

| Upstream convention | Codex execution |
| --- | --- |
| `Task`, `run_in_background`, `subagent_type` | Use the host's subagent tool, such as `collaboration.spawn_agent`. Put the resolved role prompt and adapter paths in the assignment. Spawning is already asynchronous. |
| `Task` resume/status | Use send/follow-up for new work, list/status for inspection, and bounded waits for completion. Status inspection must not restart a worker. |
| `environment: cloud`, isolated VM | Use separate local git worktrees or disjoint scratch directories. Native subagents share the filesystem. Never assume they have separate VMs. Use remote/cloud work only when actually available and authorized. |
| `AskQuestion` | Use the host's question tool or a concise direct question for genuine missing preferences. Run observable experiments yourself. |
| `TodoWrite` | Use the available plan tool; otherwise maintain a Markdown checklist in task scratch space. Preserve selected playbook steps and skip reasons. |
| `Read`, `Glob`, `Grep`, `Shell` | Use filesystem/shell tools. Prefer `rg`. |
| `control-cli`, `control-ui` | Read the bundled skills. Use existing project harnesses, native PTY sessions, and available browser/computer tools under their documented rules. |
| Skill `/name` | Resolve and read the corresponding bundled skill; do not type nonexistent slash commands into a terminal. |

Do not create user-visible Codex tasks as a substitute for subagents unless the user asks for new tasks. If subagents are unavailable, use sequential investigation and verification, record that review independence is reduced, and do not claim an independent review occurred.

## Models and concurrency

Read [models.json](models.json). Every role defaults to `inherit-parent`. Omit model overrides when using that value. A user can request another model; validate it against the current tool's supported model list and pass the exact supported name. Do not infer model availability from Cursor's defaults. Never install or invoke an external model CLI just to satisfy a model name in a document.

Panel size is a logical count, not permission to exceed the host's active-agent limit. Run candidates in waves as slots permit. Preserve distinct candidate briefs, then cross-judge completed artifacts. If only one model family is available, use independently scoped agents and disclose that the review used one family. Do not label it cross-family validation.

`setup-pstack` means edit this adapter's `models.json`, when requested. Do not write `.cursor/rules`, global AGENTS.md, or unrelated runtime configuration. Preserve role mappings not being changed. The JSON role labels match upstream's setup role names; the default covers an absent role.

## Scope, permissions, and shipping

Upstream autonomy language does not grant permission beyond the user's request. Keep reversible necessary work moving. Messages to people, external publication, merges, deployment, deletion, and shared history changes follow the host and repository rules and existing user authorization. Do not ask twice for authorization already given. Elapsed time never counts as an answer to a required approval.

The automatic final “Opening a PR” step applies only when the task and repository permit a PR. A local-only request finishes with a verified diff. Read-only requests create no commits or PRs. Respect a repository's no-commit rule. Do not turn “check this PR” into a fix, a posted reply, a recurring monitor, or a merge. Babysit `check` is one read-only status pass; `drive` ends at merge-ready. Shipping requires the appropriate authorization in the current task.

Keep existing unrelated changes untouched. Give each writer an exclusive worktree or file set. Never run checkout/reset/rebase against a shared checkout while other writers are active. Stopping the task stops delegates and any monitor created for it.

## Loops, goals, durable work, and history

- In-turn repeated work uses bounded native waits and an explicit completion predicate. Keep user communication responsive. A Bash sleep loop is not a durable Codex task.
- `/loop`, background babysitting, and periodic audit ticks map to native Codex heartbeat automations only when the user requests continued or recurring work. Search for the automation tool and follow its actual schema. Preserve its ID and stop condition. Stay quiet on unchanged state unless periodic updates were requested. Do not create automations merely because the imported playbook mentions one.
- `/goal` maps to the native goal tool only if the user explicitly requests a goal. Otherwise track acceptance in the task checklist. Never assert persistence across a restart without a real automation or resumable artifact.
- Use a task-specific directory under the project's existing scratch convention, or `work/poteto/<task-slug>/`. Keep decisions, checklists, inboxes, and evidence there. There is no assumed Cursor agent store.
- Use Codex task listing/reading tools for in-scope prior task history. Never scan Cursor transcript folders as a substitute for Codex history. A summary is not a full transcript; when raw tool-level evidence is unavailable, verify against the working artifacts and label that limitation.
- `session-pickup` and `pause-safely` use recorded paths, branches, SHAs, agent IDs, and native task state. Local subagents do not automatically survive a restart. Resume only work whose liveness has been verified.
- The dormant Benny pack is included as source. Configuring or enabling it is a separate request using native automations and the user's selected connector. Import alone enables no scheduled tasks or Slack actions.

## Executable helper commands

Set `POTETO` to the absolute path of this wrapper's `scripts/poteto.py`. Use an absolute, task-local `WORK` directory outside AlesSystems/Skills and skill/runtime/plugin folders. The helper prepares only executable support files, never another installed skill tree. It pins Bun 1.4.2 when Bun is not installed, then installs upstream dependencies with the frozen lockfile. Node/npm and network are needed for this first preparation. Later runs reuse that workspace.

```sh
python3 "$POTETO" prepare --work-dir "$WORK"
python3 "$POTETO" run --work-dir "$WORK" orch --store "$WORK/store" init
python3 "$POTETO" run --work-dir "$WORK" orch --store "$WORK/store" status
python3 "$POTETO" run --work-dir "$WORK" watch-pr --help
python3 "$POTETO" run --work-dir "$WORK" check-plan /absolute/path/to/plan.md
python3 "$POTETO" run --work-dir "$WORK" test
```

Read `--help` before constructing commands. `watch-pr` without `--status-only` polls, so choose that flag for a status question and use the repo/PR options from help. Do not run a live watcher as an installation test. Tests use local fixtures and fake GitHub/Graphite responses.

The decision-log helper and read-only worktree audit are also routed as `run … log <args>` and `run … worktree-audit <args>`. Pass generated text as argument data, never shell interpolation. Do not run executable bootstrap entrypoints directly from the submodule, because their upstream bootstrap installs beside itself.

### GitHub orchestration without Graphite

The adapter supplies a small tested change in the task-local `orch` executable. For GitHub stacks, pass an explicit bottom-to-top PR list with `--prs`. It fetches current GitHub branch names, states, and SHAs, verifies the chain, and writes through upstream's locking and generation mechanism. No `gt` install is required.

```sh
python3 "$POTETO" run --work-dir "$WORK" orch --store "$WORK/store" frontier set --repo /absolute/repo --prs 12,13
```

Every update must repeat the complete ordered list. Independent queues use separate frontiers, not a fabricated stack. Closed-unmerged PRs block progression. Re-fetch after stack mutation and invalidate verdicts on SHA changes. Git/gh integration remains serialized by stack owner. If Graphite is deliberately used, the original path remains available by omitting `--prs` and setting `POTETO_FRONTIER_FORGE=graphite` for that command.

### Plan checking

The prepared plan checker replaces hardcoded Cursor/Grok phrases with Codex-native ones. Use “Ten lanes on the configured Codex worker model at the PR head”, “task acceptance predicate”, “read pinned workflow”, and a “30-minute” heartbeat only for a program where that cadence was requested. Ten logical coverage lanes run in bounded waves; they are not ten concurrent agents. Keep the upstream unit/live/performance evidence structure for plans using that template. The checker is for the multi-phase program template, not every plan or simple task.

## Completion and limitations

Report actual verification and remaining limitations. Independent agents on one model family are supported; Cursor multi-family panels and cloud VMs are not emulated. Browser, GitHub, simulator, and connector workflows depend on the actual project's tools and authentication. A missing optional surface limits that task's evidence, not skill discovery. No live merge, deployment, or overnight execution is proven merely by installing this bundle.
