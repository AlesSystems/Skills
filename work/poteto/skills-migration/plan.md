# Move owned skills to AlesSystems/Skills

- [x] Read the Principles section of poteto-mode.
- [x] Phase A: Frame.
- [x] Phase B: Design the workflow.
- [x] Phase C: Run the loop.
- [x] Capture a migration manifest before moving files.
- [x] Transfer six skill directories and two pinned dependency submodules.
- [x] Verify file equivalence, existing destination files, and skill checks.
- [x] Prepare history-preserving reverts of source PRs 24 and 23; verify the baseline tree.
- [x] Review both diffs independently, then publish and land the transfer and revert.
- [x] Update the primary checkout, owned Codex links, and default library guidance.
- [x] Phase D: Keep the audit trail.
- [x] Phase E: Verify and hand back.

Done means the source main tree matches its pre-contribution baseline, all owned
skills and required dependencies are available from the destination main branch,
existing destination content is preserved, the six owned Codex links resolve to
that checkout, the two removed imported Claude entries resolve there, and the
default guidance names AlesSystems/Skills.

The scope is source PRs 23 and 24, 115 changed paths plus the unchanged support
files required by the updated diagram skill. Preserve directory nesting and
dependency pins. Skip architecture alternatives because the path move is
mechanical. Skip new general library tooling because the destination has none
and the existing adapters already derive their root. GitHub is the selected
forge. No external origin CLI is needed for these GitHub repositories.

Sequence work into verifiable units puts the verified transfer before the source
rollback. Prove It Works requires hashes, dependency fingerprints, real helper
tests, and remote main checks. Laziness Protocol preserves the existing paths
instead of adding a second adapter layout.
