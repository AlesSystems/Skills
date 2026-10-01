# Candidate B: explicit editorial scenes

## Problem
Create a 42-second editable JavaScript product demo and 1920×1080 H.264 MP4 at 30fps. Frame is a fictional release-planning app; every screen and caption carries an unobtrusive “Sample product” label. This is a greenfield example, so grounding into an existing product is skipped. This candidate sketches only; implementation, installation, and rendering belong to the parent workstream.

## Usage (caller’s view)
```sh
npm run capture          # three local fixture states -> PNG assets
npm run studio           # preview FrameDemo; edit src/FrameDemo.jsx
npm run render           # FrameDemo -> out/frame-demo.mp4
npm run check            # one runnable artifact check
```
Three call sites, all in one composition module:
```jsx
<Composition id="FrameDemo" component={FrameDemo} durationInFrames={1260}
  fps={30} width={1920} height={1080} defaultProps={sample} />
<FrameDemo {...sample} />
<FrameDemo {...sample} narration="audio/narration.wav" />
```
Editing a new product means replacing screenshot assets and captions in this module, not configuring a scene engine.

## Shape
Data is fixed role-named assets, rather than a scene table:
```js
const sample = {
  product: 'Frame', sampleLabel: 'Sample product',
  screens: { overview: 'screens/overview.png', plan: 'screens/plan.png', ready: 'screens/ready.png' },
  music: 'audio/close-up.mp3', narration: null,
};
// JSDoc: screens requires all three relative local paths; narration is path|null.
```
Boundary validation rejects missing assets, URLs, unsafe paths, missing sample label, and nonpositive media lengths before rendering. Inside the composition, screenshots are immutable and frames are the only clock. No Date, timers, random values, CSS animations, remote runtime assets, or network content.

```jsx
export function FrameDemo({product, sampleLabel, screens, music, narration}) {
  // Sketch only; actual component body not implemented.
  return <AbsoluteFill>
    <Sequence from={0} durationInFrames={150}><Opening /></Sequence>
    <Sequence from={150} durationInFrames={330}><Overview src={screens.overview} /></Sequence>
    <Sequence from={480} durationInFrames={330}><Plan src={screens.plan} /></Sequence>
    <Sequence from={810} durationInFrames={300}><Ready src={screens.ready} /></Sequence>
    <Sequence from={1110} durationInFrames={150}><Closing /></Sequence>
    {/* Audio lives at composition scope: volume(frame) uses global frames. */}
  </AbsoluteFill>;
}
function Screen({src, caption, focus}) { throw new Error('not implemented'); }
function musicVolume(frame, narration) { throw new Error('not implemented'); }
```
Opening: “Bring the next release into focus.” Overview: readable browser screenshot, restrained 1.00→1.03 camera drift; “One place for the whole release.” Plan: enlarged screenshot crop on the release list, with a single accent outline on a deadline; “Turn priorities into a plan.” Ready: checklist and status view, “See what’s ready. Know what’s next.” Closing: Frame wordmark, “Make room for the next release.” No invented usage metrics.

Cream background, ink text, blue accent, 72px headline, 34px caption, 48px safe edges. Screens occupy roughly 1480×820; fixture uses 24px UI text so it stays readable after scaling. Each feature gets a 5+ second stable reading hold; transitions are brief 12-frame opacity/translation changes computed with interpolate and clamped extrapolation. Avoid continuous perspective tilt or tiny full-dashboard shots. Each scene owns its framing, so zoom never hides the caption.

Music gain is min(clamp(frame/30), clamp((1259-frame)/60)) × 0.18, ending at silence on the final frame. With narration use 0.07 underneath, and give narration its own 12-frame endpoint fades. Missing optional narration is omitted entirely. Audio is trimmed to composition duration; no loop is needed for the proposed 95-second track. Narration remains user supplied, with final script matching the rendered captions.

## Files and signatures
- `src/FrameDemo.jsx`: composition registration, explicit Sequence tree, scene components, Screen and pure audio-envelope function. One file intentionally keeps the edit path visible.
- `fixture/frame.html`: local static UI with deterministic `?view=overview|plan|ready`; no app backend, external fonts, or live data.
- `scripts/capture.mjs`: `captureScreens({fixturePath, outputDir}) -> Promise<void>`; fixed 1600×900 viewport, wait for fonts, save three PNGs. Overwrite the same names, so reruns converge.
- `scripts/check.mjs`: one artifact checker, described below.
- `public/screens/*.png`, `public/audio/close-up.mp3`, optional `public/audio/narration.wav`, `public/audio/LICENSE.md`.
- `package.json`, pinned lockfile; runtime uses React and Remotion, capture uses the already selected browser tool or installed Playwright. No second video framework.

If the app interaction itself becomes the claim (dragging release order, typing, etc.), capture the actual interaction as a local MP4 and use Remotion Video inside the relevant Sequence. Do not simulate a product interaction with an animated pointer over static PNGs. Static screenshots suffice for this example’s visibility and planning claims.

## Runnable artifact check
`npm run check` invokes a single Node assert script after rendering: read PNG headers to require 1600×900; require each asset exists and the license file names source/download/license URLs; run ffprobe JSON on the MP4 and assert H.264, 1920×1080, 30fps, duration 42±0.1s, and audio stream. Render frame 615 twice and compare SHA-256 to expose nondeterministic visuals. Assert audio-envelope outputs at frames 0, 30, 1200, 1259, including narration attenuation. Also extract a contact sheet at seconds 3, 10, 21, 31, 39 for visual review of text readability, crops, scene continuity, and the Sample product label. Metadata alone cannot prove polish; the reviewer must inspect it.

## Music evidence
One selected item: **Close Up — Michael Ramir C.**, 1:35, described on Mixkit as positive/futuristic rhythmic underscore with bass and drums. Audition before final render to confirm editorial fit; instrumentation suggests a suitable restrained technology demo bed, but this research did not listen to the track.
- Official listing: https://mixkit.co/free-stock-music/corporate-music/
- Official item download dialog: https://mixkit.co/free-stock-music/download/1167/?context=item+grid
- Asset URL exposed by that dialog: https://assets.mixkit.co/music/1167/1167.mp3
- License: https://mixkit.co/license/modal/musicFree/
- Terms: https://mixkit.co/terms/ (last revised October 2, 2025).
Verified 2026-10-01: the Music Free License allows commercial and noncommercial projects, web/social platforms, advertisements, and online video. It forbids music-only remix/ownership claims and rights-management registration; CDs/DVDs, games, TV/radio are excluded. The MP4 is a web demo, within the stated permitted media. Preserve the source/license record with the demo; do not republish the raw track as a library item. Terms clause 9.10 prohibits mass downloading; only this single track was inspected. Clicking its official Download control automatically initiated the single download, though no media was displayed or auditioned.

## Synthesis decision
Pending parent comparison; this is candidate B, not a claim of synthesis.

## Tradeoffs accepted
- Accept editing JSX timing by hand in exchange for direct creative control and no scene schema/parser.
- Accept three static fixture states in exchange for reproducible screens and no fabricated interaction.
- Accept a fixed 42-second sample in exchange for one auditable timeline; adapt durations in JSX for another brief.

## Alternatives considered
A declarative scene table plus generic scene renderer hides scheduling but exposes crop/effect/caption configuration to every caller and needs a schema. It loses for a short editable sample with three distinct editorial moments. A single prerecorded walkthrough hides every UI transition but exposes capture timing and rerecording work to the author; use it when interaction is the evidence.

## Open questions and risks
Will auditioning Close Up support the desired calm tone? Is the highlighted release list readable at final size? Resolve both with audition/contact-sheet inspection during implementation; no user checkpoint is needed.

## Next implementation step
Build the local HTML fixture and capture the three PNGs, then register the explicit 1260-frame composition.
