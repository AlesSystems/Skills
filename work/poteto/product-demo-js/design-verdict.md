# Arena cross-judge verdict

Both complete designs were read. Scores assess proposed designs, not implemented or rendered artifacts.

| Criterion | A | B |
| --- | ---: | ---: |
| Minimal files and indirection | 4 | 4 |
| Editable reusable source | 5 | 3 |
| Readable honest screenshot demonstration | 4 | 5 |
| Deterministic timing and audio | 5 | 3 |
| Rerunnable verification and license evidence | 4 | 4 |
| Total | 22 | 19 |

**Recommend A as the base.** Its scene table derives offsets and composition length from durations. B repeats timing across `Sequence from`, `durationInFrames={1260}`, audio endpoint `1259`, and checker duration `42`. Changing a scene can leave gaps, truncate scenes, or fade audio at the wrong point. A also explicitly delivers the reusable `SKILL.md`; B's file list omits it.

Keep A's table as editable JavaScript, not an exported timeline framework. Laziness Protocol and Model the Domain support one timing owner. A's renderer hides actual scheduling work, so it is not a shallow wrapper. Keep individual visual scenes free to own distinctive framing. Reject fixed role-named asset props becoming a reusable public API that requires consumers to understand this sample's editorial structure.

**Graft B's visual acceptance and checks.** Require a persistent sample label, five-second reading holds, full-size readability review, explicit audio endpoint assertions, and a repeated-frame hash comparison. Keep A's complete MP4 decode and boundary contact sheet. Prove It Works requires inspecting the exported video and listening to its audio; a matching hash proves only the sampled frame.

**Trim A's validation.** Boundary Discipline supports one preflight check for edited durations, required assets, dimensions, and valid focus rectangles. Avoid a schema package or general parser. Validate scene IDs only if rendering actually depends on their uniqueness. Do not duplicate checks inside every scene.

**Resolve two acceptance gaps.** A's checker hardcodes 45 seconds while advertising editable durations. Derive expected duration from the same table and enforce the requested 30–60-second range separately. B proposes bundling `close-up.mp3` while its rights notes prohibit republishing the raw track. Its video-use evidence does not establish editable-project redistribution permission. Select music with explicit source-bundle permission and retain license terms, attribution, retrieval date, and file hash.

Capture, render, and check scripts own external tool boundaries. Neither design needs additional phase modules, renderer adapters, or asset registries.
