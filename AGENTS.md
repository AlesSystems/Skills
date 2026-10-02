# Ales Skills

`https://github.com/AlesSystems/Skills` is the default source of truth for our own
skills. The primary local checkout is `~/Desktop/Ales/Skills`. New owned skills,
their resources, and their maintenance changes belong here.

Check `git remote get-url origin` before a push or PR. Owned skill changes target
`AlesSystems/Skills`. Other libraries and plugin caches are separate sources.
Read them when needed, but do not use them as the default authoring destination.

Keep source in `skills/<id>/SKILL.md`. Retain the existing `skills/also/` layout
for imported adapters because their relative dependency paths use it. Native
Codex entries under `~/.codex/skills/<id>` link to this checkout. Do not copy
skills into runtime or marketplace directories or edit `installed_plugins.json`.

Preserve upstream licenses and pinned Git submodules. Do not edit upstream
tracked files. Local adapter code and instructions belong in this repository.
Use task-local scratch outside canonical skills for generated executable helpers.

Keep unrelated changes and worktrees intact. Use small Conventional Commits and
stage exact files. Verify the affected skill and its real helper behavior before
handoff. Report any checks whose required tools or assets are unavailable.

There is no `bin/library Codex-sync` command in this repository. Inspect the
available adapters before changing loader links. During refresh, fetch and inspect
the current branch and worktrees before a fast-forward pull. Preserve unrelated
third-party links. Restart Codex after source or loader changes.
