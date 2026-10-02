# Impeccable for Codex

Imported at the user's request on 2026-09-11.

- Upstream: https://github.com/pbakaus/impeccable
- Submodule: `refs/impeccable`
- Imported revision: `cb56ed6c19a07329a9fa0cd4e657bee040156593`
- Skill version: 4.3.1; engine version: 0.1.5.
- License and notices remain in the upstream submodule.

The upstream Codex transformer generates one Codex bundle inside the submodule's
ignored `dist/` directory. `skills/also/impeccable` links to that bundle, and
`~/.codex/skills/impeccable` links to the canonical library entry. No skill files
are copied into runtime or plugin cache folders. Upstream instructions are intact.

After cloning the library, or deliberately updating the pinned submodule, run:

```sh
git submodule update --init refs/impeccable
node adapters/codex/import-impeccable.mjs
git diff --check
```

The adapter uses Node's standard library and upstream's transformer; no npm install
is required. It refuses to replace an unrelated skill entry. Generated artifacts
are rebuilt from the pinned source, not committed or edited directly.

Restart Codex to load the skill. Invoke `$impeccable critique <target>` or
`$impeccable shape <feature>`. Product context initialization belongs in the target
product repository. This import does not enable project hooks or live mode.

The launcher downloads its pinned engine from upstream GitHub releases on first
use and verifies its SHA-256 sidecar before execution. This is an executable
dependency, separate from the Markdown skill.

## Original import evidence

The following checks were recorded in tutoria-hub/agent-library before this
transfer. Its `bin/library` commands are not available in AlesSystems/Skills.
Strict validation passed with 46 entries, the launcher returned
`impeccable-engine 0.1.5`, and triage reported zero errors. The original doctor
retained its pre-existing agents-alias failure.

Current transfer checks are recorded in
[the migration evidence](../work/poteto/skills-migration/acceptance.md).
