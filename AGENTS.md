# Ales Skills

`https://github.com/AlesSystems/Skills` is the default source of truth for our own
skills. The primary local checkout is `~/Desktop/Ales/Skills`. New owned skills,
their resources, and their maintenance changes belong here.

Check `git remote get-url origin` before a push or PR. Owned skill changes target
`AlesSystems/Skills`. Other libraries and plugin caches are separate sources.
Read them when needed, but do not use them as the default authoring destination.

Keep owned source in `skills/<id>/SKILL.md`. External skill collections and
their adapters belong in separate sources. Native Codex entries under
`~/.codex/skills/<id>` link to this checkout. Do not copy skills into runtime
or marketplace directories or edit `installed_plugins.json`.

Preserve licenses for retained material. This library has no external skill
submodules or adapter bundles. Use task-local scratch outside canonical skills
for generated executable helpers.

Keep unrelated changes and worktrees intact. Use small Conventional Commits and
stage exact files. Verify the affected skill and its real helper behavior before
handoff. Report any checks whose required tools or assets are unavailable.

There is no `bin/library Codex-sync` command in this repository. Inspect the
actual skill paths before changing loader links. During refresh, fetch and inspect
the current branch and worktrees before a fast-forward pull. Preserve unrelated
third-party links. Restart Codex after source or loader changes.
