# Product demo skill and example

Acceptance: canonical product-demo-js/SKILL.md, editable JavaScript example, actual screenshot assets, sourced music with license evidence, playable 1080p MP4, rendered-frame inspection, runnable output check, and independent review.

## Authoring playbook
- [x] Use the create-skill skill. Codex skill-creator read in full.
- [x] Validate the skill: frontmatter has name and description, referenced files exist, cross-skill links resolve. Quick validator and canonical strict validation pass.
- [x] Test cases if structural. The example exercises the actual render path.
- [x] Run Opening a PR. Skip remote PR and publishing for this local artifact request.

## Architect and arena phases
- [x] Ground. Node, FFmpeg, policy and existing skill discovery traced.
- [x] Sketch. Two structurally distinct candidates produced.
- [x] Cross-judge and agree. Read both designs and select a base.
- [x] Implement.
- [x] Scrap. n/a unless runtime evidence invalidates the chosen design.
- [x] Verify synthesized result.

## Throughput checkpoint
- Blocking first steps: read canonical policy and Poteto adapter; inspect existing tooling and two composition designs before implementation.
- Independent workstreams: skill authoring in canonical library; demo code/assets in this workspace; independent read-only review after both finish.
- Shared mutable state: one demo writer; primary owns the skill only. Music lives with demo assets. Do not touch unrelated staged library changes.
- Smallest safe decomposition: one demo implementer and one reviewer; no framework, generator, or cloud pipeline beyond Remotion.

## Phases
- [x] Ground and sketch two alternatives
- [x] Compare designs and choose a composition
- [x] Author the skill
- [x] Implement, capture screens, source music, render example
- [x] Inspect frames, run artifact checks, independently review
- [x] Deliver local artifacts

PR and publishing skipped: this is a local artifact request. Canonical library contains unrelated staged changes, so no commits there. Plant skipped because it mutates unrelated provider runtime homes. No fictional demo will imply an existing real product.

Baseline library doctor: FAIL for pre-existing missing Claude link impeccable. New skill is authored but not planted into provider homes. Strict validation passes with 57 catalog entries.

Final independent demo review passes with no open findings. Browser-option documentation was corrected. No code/media changes followed the successful media checks.
