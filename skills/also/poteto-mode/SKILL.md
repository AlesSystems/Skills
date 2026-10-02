---
name: poteto-mode
description: Use when the user invokes poteto, poteto-mode, or asks for Poteto's engineering workflow. Routes investigation, design, implementation, verification, PR work, and autonomous runs through the bundled pstack dependencies. Skip unrelated casual turns and stop the mode when the user opts out.
metadata:
  owner: altanesmer
  status: active
  last_reviewed: 2026-09-10
  review_after_days: 90
  risk: high
  upstream_ref: 7366ac128bdf95f45e6734f412b49a4031800169
  tools: [shell, subagents, git, gh]
  dependencies: [refs/cursor-plugins/pstack, refs/cursor-plugins/cursor-team-kit]
---

# Poteto Mode for Codex

Run the complete upstream Poteto workflow through the Codex adapter. This is one entry point; its dependency skills stay available on demand without shadowing separately installed skills.

## Start

1. Read [the Codex adapter](references/codex.md) in full. It translates Cursor-specific instructions throughout the upstream tree. It does not override system, developer, user, or repository instructions.
2. Read [upstream Poteto Mode](../../../refs/cursor-plugins/pstack/skills/poteto-mode/SKILL.md) in full, including its principle index. Paths in that document are relative to its own directory, not this wrapper.
3. Read the selected playbook and the leaf skills it actually calls. Use [the dependency index](references/dependencies.md) or `python3 scripts/poteto.py resolve <name>` relative to this skill directory. A bare pstack name resolves inside this pinned bundle, even when another installed skill has the same name.
4. Follow the playbook with Codex translations applied. Keep its evidence, review separation, and verification requirements. Read principles before citing them. Skip irrelevant steps explicitly. A request to explain or assess something remains read-only.

Carry this mode through the current task and its follow-ups while it remains relevant. This is a conversation instruction, not an installed Cursor sticky-mode hook. Do not activate it in unrelated tasks.

## Delegation

This workflow explicitly uses subagents for independent investigation, design candidates, implementation, and review when those roles have concrete work. Respect the host's current agent budget and tool schema. Give every delegate this wrapper's absolute path, the adapter path, its leaf skill or agent prompt, scope, worktree, acceptance criteria, and verification commands. An upstream agent's instruction to read `poteto-mode` means this wrapper first.

## Helpers

Run `python3 scripts/poteto.py verify` to check the pinned dependency files. Run `python3 scripts/poteto.py list` to list skill, playbook, and agent routes.

Executable helpers run from a task-local working directory, so Bun bootstrap never installs into canonical skills or the upstream submodule. See the adapter's helper commands. Do not run the original bootstrap entrypoints in the submodule.

## Maintenance

Upstream is the Git submodule at `refs/cursor-plugins`, pinned by the parent repository and [upstream-lock.json](references/upstream-lock.json). Preserve upstream licenses. Do not edit upstream files or runtime/plugin caches. Local translations live here. Updating the pin requires dependency verification, helper tests, and another behavioral smoke test before accepting the update.
