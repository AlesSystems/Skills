# Owned skills only — 2026-10-02

Decision: AlesSystems/Skills contains only Altan's owned skills. Keep
`3d-ui-design`, `landing-page-art-direction`, `product-demo-js`, and
`software-idea-discovery`. External skill collections belong in separate sources.
This decision implements the owner's request to remove the imported collections.

Removed Poteto, Impeccable, and diagram-design, their adapters, two external
skill submodules, gallery, tests, setup documentation, and obsolete migration
verification. Historical imports, license notices, and migration evidence remain
in Git history at baseline `39dc7a32f68fe5b3a86c9a86c6f9462c860517fc`.
Retained licenses and owned skill content are unchanged. The Frame demo example
and its earlier acceptance records remain available; the `work/poteto/product-demo-js`
folder records development of our owned demo skill, rather than an installed skill.

Verification before publication:

- All four owned skills pass the system skill-creator `quick_validate.py` with
  `/usr/bin/python3`; the catalog lists exactly these four existing skill paths.
- `git diff --exit-code 39dc7a32f68fe5b3a86c9a86c6f9462c860517fc --
  skills/3d-ui-design skills/landing-page-art-direction skills/product-demo-js
  skills/software-idea-discovery examples/product-demo-js LICENSE
  work/poteto/product-demo-js docs/validation/landing-page-art-direction.md`
  passes: retained skill source, example, license, and acceptance files match baseline.
- The Git index contains no submodule entries, and `.gitmodules`, imported skill
  entry points, adapters, and obsolete import tests are absent.
- `git diff --check` passes. Local README and agent-instruction links resolve.
- Five direct loader symlinks targeting the removed canonical imports were
  removed: three Codex entries and the Poteto/Impeccable Claude entries.
  All 127 remaining provider symlinks were verified unchanged; all four owned
  Codex skill links resolve to this primary checkout. Unrelated library/plugin
  sources and provider settings remain intact.
- Global Codex instructions now refresh owned skills without external adapter
  or submodule setup. Existing worktrees were preserved.

This is a source-library cleanup. It makes no application UI, schema, security,
privacy, or deployment changes. No new browser/model demo or video render was
run; owned implementation resources are unchanged. External skills from separate
libraries/plugins are outside this cleanup. Restart Codex to reload the changed
skill inventory.
