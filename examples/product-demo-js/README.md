# Frame sample product demo

An editable 42-second product walkthrough. Frame is a fictional release-planning app. Every video frame carries “Sample product”. Three PNGs are genuine browser captures of the included local HTML fixture. Static screens demonstrate visibility, ownership and readiness, without implying recorded interactions.

## Run

Node 24 and npm were used. Install the locked dependencies with `npm ci`. FFmpeg and ffprobe must be on PATH for the artifact check. Render assets are local; no remote network assets enter the composition.

```sh
npm run preview
npm run still
npm run render
npm run check
```

The preview opens Remotion Studio. The still command renders frame 615 to `out/preview.png`. The render command runs source preflight and writes H.264/yuv420p video with AAC music to `out/frame-demo.mp4`. The check asserts timeline/media agreement, source PNG dimensions, full media decode and audible unclipped audio with faded endpoints. It creates `out/contact-sheet.jpg`, `out/boundary-sheet.jpg` and `out/extracted-preview.png` from the actual MP4.

Remotion can download its own Chromium for stills and video renders. To use an installed browser, append `-- --browser-executable="/path/to/chrome"` to the still or render command. Studio opens the local preview in the default browser. On the authoring machine the still and render commands used `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`.

## Recapture

The capture harness resolves an available Playwright module. It adds no capture dependency. Use an existing installation or set `PLAYWRIGHT_MODULE` to its absolute module directory. Set `CHROME_PATH` to a browser executable if the installation has no bundled browser.

```sh
PLAYWRIGHT_MODULE=/path/to/node_modules/playwright CHROME_PATH=/path/to/chrome npm run capture
```

Capture loads `fixture.html?screen=overview`, `ownership`, and `readiness` at 1920×1080, waits for the explicit ready marker and fonts, and overwrites `public/*.png`. The example fixture makes no remote requests. On this machine Playwright was reused read-only from `/Users/altanesmer/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright`.

## Edit

Edit the five entries in `src/timeline.mjs` for captions, durations and focus outlines. Sequence offsets, final duration and music fade derive from that table. `src/index.jsx` owns visual framing. The composition is 1920×1080 at 30fps. The feature scenes hold for eleven seconds, with brief entrance/exit fades, a restrained 2.5% zoom that settles, and owner/status outlines. No schema, narration pipeline, simulated clicks or generic scene engine is included.

## Asset rights

Music is Close Up by Michael Ramir C. See `public/music-license.md` for official URLs, retrieval date, file hash and distribution limits. `public/close-up.mp3` is a local licensed production asset excluded from git. Obtain this one track through the official Mixkit download before rendering a source-only copy. Do not include raw music in a redistributed archive; source-bundle redistribution permission is not established. No archive was created. The rendered demo is intended for permitted web/social use.

[Remotion’s current license](https://www.remotion.dev/license) permits free use by individuals, organizations with up to three employees, nonprofits and noncommercial evaluation. Other organizations require a Company License. This local example is an evaluation; no license was purchased.

## Inspection

The representative frame and MP4-derived frames were visually inspected for readability, crops and the sample label. Artifact metadata, full decode, audio RMS/peak and endpoint fades are checked by `npm run check`. Subjective music listening and a full real-time playback review have not been verified. No narration is requested or supplied.
