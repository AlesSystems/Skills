# Candidate A. Scene table and captured stills

## Problem

Produce one editable JavaScript source project and a 45-second 1080p MP4 for Frame, a fictional release-planning app. Screenshots carry the product evidence. Frame is explicitly labeled as a sample in the opening and end card. The composition must be readable without narration and must not imply that screenshot camera moves demonstrate real interaction.

## Usage

The example project exposes three commands after an explicit local dependency install.

```sh
npm run capture
npm run preview
npm run render
node scripts/check.mjs out/frame-demo.mp4
```

Typical edits are direct scene-table changes, rather than another configuration layer.

```js
scenes[1].headline = 'See every release at a glance';
scenes[2].focus = {x: 820, y: 280, width: 920, height: 640};
scenes[3].duration = 300;
```

`capture` loads the local HTML fixture at a fixed viewport, selects its named states, waits for fonts and layout, and overwrites three PNGs. `preview` opens the Remotion composition. `render` produces H.264 video and AAC audio. Each frame is a function of the scene table and the frame number. No elapsed-time clock or CSS animation drives the export.

## Grounding and ownership

`docs/SKILLS-HOME.md` makes `~/agent-library/skills/` the authoring location for general skills. A reusable demo-making skill belongs at `skills/product-demo-js/SKILL.md`; it does not belong in native-loader directories. The example and reference instructions can live beneath that skill. Exported projects and rendered media belong in the caller's project or scratch directory, not the canonical library. The user's current Codex discovery instructions govern reconciliation if they differ from older host prose.

`bin/library` scans `skills/*/SKILL.md` and one nested skill level. Its strict validation checks frontmatter name matches folder identity, a nonempty description, supported frontmatter and invocation controls, and agent metadata where present. It does not validate video. The media check therefore belongs to the exported example and remains separately runnable.

The scoped search found no existing Remotion/product-demo skill to reuse. Node v24.15.0, ffmpeg 8.1, and ffprobe are installed. This design pass did not install packages, test Remotion compatibility, capture PNGs, or render media.

## Shape

One scene table is the timing source. Duration and sequence offsets derive from it, so no timeline needs synchronizing.

```js
const video = {width: 1920, height: 1080, fps: 30};
const scenes = [
  {id: 'intro', kind: 'title', duration: 150, headline: 'Release with clarity', subline: 'Frame · fictional sample'},
  {id: 'overview', kind: 'screen', duration: 330, image: 'overview.png', headline: 'One plan for the whole team', focus: null},
  {id: 'detail', kind: 'screen', duration: 330, image: 'release.png', headline: 'Make ownership clear', focus: {x: 820, y: 280, width: 920, height: 640}},
  {id: 'readiness', kind: 'screen', duration: 330, image: 'readiness.png', headline: 'Know what is ready', focus: null},
  {id: 'end', kind: 'title', duration: 210, headline: 'A calmer way to release', subline: 'Frame · fictional sample'},
];
const music = {file: 'music.mp3', gain: 0.18, fadeInFrames: 45, fadeOutFrames: 90};
```

The table contains 1,350 frames. JavaScript uses JSDoc discriminated unions for `title` and `screen`, with mandatory image paths only on screen scenes. A single boundary check rejects invalid kinds, duplicate IDs, noninteger durations, missing PNGs, out-of-bounds focus rectangles, incompatible image dimensions, and durations outside 30–60 seconds. JSDoc supports editing but does not replace runtime checks.

| File | Responsibility and signature |
| --- | --- |
| `SKILL.md` | Workflow, capture-vs-recording rule, rights evidence, readable layout acceptance, export instructions. |
| `example/package.json` | Pinned Remotion/React/browser-capture dependencies and three commands. |
| `example/src/index.jsx` | Scene table, `FrameDemo()`, composition registration, `validateScenes(scenes, assets)`, `sceneRanges(scenes)`, `musicVolume(frame, totalFrames)`. |
| `example/fixture.html` | Self-contained Frame sample with `?screen=overview\|release\|readiness`, local fonts/system fallback, no remote requests. |
| `example/scripts/capture.mjs` | `captureScreens()` writes screenshots only after the deterministic fixture is ready. |
| `example/scripts/check.mjs` | Actual media and source-contract assertions, via Node stdlib and ffprobe. |
| `example/public/` | Three source PNGs, music file, optional narration file, `music-license.md`. |
| `example/out/` | Generated MP4 and review contact sheet. |

The public interface is a scene table and familiar npm commands. Remotion hides frame sampling and export machinery. No renderer adapter, asset registry, theme system, timeline editor, or upload service is needed.

`FrameDemo()` maps the derived ranges to Remotion sequences. Each screen has a fixed headline region and a large screenshot below it. Camera movement uses `interpolate()` on local frames and clamps its endpoints. A focus rectangle centers and enlarges useful content without cropping surrounding context unexpectedly. Scene transitions use frame-driven opacity/translation; each scene owns its short entrance and exit inside its allocated duration, so no negative offsets or hidden overlaps alter total duration.

Music volume multiplies gain by clamped linear fade-in and fade-out envelopes. Narration is optional and absent in this example. If later added, one local audio file starts at frame zero with captions authored against the same frame table; music gain is adjusted deliberately after listening. No generated narration or automatic ducking service is necessary.

## Readability and audio constraints

- Capture at 1920×1080 with a settled layout and fixed device scale. Use a comfortable fixture font size and sparse release data so text survives presentation inside the composition.
- Keep scene headlines around 56–72 px and product text visibly readable at exported 1080p. Review sampled frames at full size, including the maximum zoom and each transition midpoint.
- Design a warm paper canvas, dark ink, a restrained blue accent, and one editorial hierarchy. Render believable dates, owners, and release statuses without borrowing real customer data.
- Do not make screenshots mimic clicks or status transitions. Use a recording only when the product claim depends on showing the interaction, and revise the scene union to support an actual video asset at that point.
- Find a downloadable track on a public free-music source during implementation. Before use, record exact track/source URL, author, license URL and terms, retrieval date, attribution requirement, and file hash. Check the specific license permits this MP4 and redistribution of the editable project. A free download alone is not sufficient evidence. Include required attribution in the example README or end card as the license requires.

## One runnable artifact check

`node scripts/check.mjs out/frame-demo.mp4` runs source validation and ffprobe, then asserts H.264 video, 1920×1080, 30 fps, 45 seconds within one frame, and an AAC audio stream. It checks each source PNG header/dimensions and music-license evidence file. It also decodes the MP4 with ffmpeg to surface corrupt frames and extracts a contact sheet from the output, including scene boundaries. Human review checks readability, framing, pacing, and audible fades; metadata cannot prove those qualities. Output inspection must use the rendered MP4, not only the source screenshots.

## Synthesis decision

Pending parent-agent comparison. This candidate deliberately concentrates edits and timing in a single scene table.

## Tradeoffs accepted

- Accept static fixture states in exchange for predictable readable captures. Recordings enter only when the claim needs interaction evidence.
- Accept one composition and one example in exchange for short call chains. Avoid a reusable engine before a second distinct demo needs one.
- Accept a browser dependency for capturing HTML in exchange for keeping screenshots reproducible from editable source.

## Alternatives considered

A hand-authored React section per scene hides fewer timing and asset rules and requires callers to edit component code for ordinary duration/text changes. A JSON timeline plus renderer framework gives a smaller non-code editing surface but adds schema parsing and another synchronization boundary while the user explicitly wants editable JavaScript. The scene table keeps the useful capability while exposing the smallest practical interface.

## Open questions and risks

Can the selected music license redistribute its audio inside the editable example? Resolve from the actual license before choosing a track. Does the local Chromium capture and pinned Remotion toolchain work on Node 24? Resolve with capture and a short render smoke test in the implementation workspace before producing the full video.

## Next implementation step

Build the fixture and scene table, capture three PNGs, and verify one readable preview frame before committing to the complete render.

## Design-pass acceptance

Ground and sketch complete. Candidate comparison belongs to the parent. Implementation, render, install, commits, and PRs are excluded from this assignment.
