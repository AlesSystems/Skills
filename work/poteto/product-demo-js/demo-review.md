# Independent demo review

Reviewed 2026-10-01. Scope was the local `examples/product-demo-js` project, its actual rendered MP4, its decoded visual artifacts, and the canonical `product-demo-js/SKILL.md`. Application files were read-only. This report is the only reviewer-written file.

Source and rendered-media acceptance passed. No open findings remain after the primary agent corrected the one documentation issue below. No actionable correctness, security, regression, or music-rights finding was established.

## Resolved finding

### P3. Preview browser override, resolved

The initially reviewed `examples/product-demo-js/README.md:18` instructed readers to append `-- --browser-executable="/path/to/chrome"` to the preview command. `package.json:8` runs Remotion Studio. Installed Remotion 4.0.532 selects the Studio browser using `browserOption` in `node_modules/@remotion/cli/dist/studio.js:207`, and does not read `browserExecutableOption` in this entry point. Thus that override did not select the intended browser for preview. The still/render override was correct.

The primary agent narrowed the `--browser-executable` instruction to still/render and described Studio's default browser. Independently re-read README line 18 and confirmed this correction. The [official Studio documentation](https://www.remotion.dev/docs/cli/studio#--browser) confirms the `--browser` flag. Media checks were not repeated after this documentation-only change.

## Actual verification

- `node scripts/check.mjs --source` exited 0 with `Source and asset preflight passed.` This checked the timeline, fade endpoints, focus bounds, PNG dimensions, music provenance, and local music SHA-256.
- Independent `ffprobe -v error -show_streams -show_format -of json out/frame-demo.mp4` found H.264 High, yuv420p, BT.709, 1920×1080, 30/1 fps, 1260 frames, and 42.000 seconds of video. Container duration is 42.005 seconds. Audio is AAC LC, stereo, 48 kHz, and 42.005 seconds.
- `ffmpeg -v error -i out/frame-demo.mp4 -f null -` exited 0. The entire MP4 decoded successfully.
- Independent stereo PCM decoding measured peak amplitude 0.221996, body RMS 0.032921, first 100 ms RMS 0.000992, and last 100 ms RMS 0.000431. The actual artifact has a non-silent signal, headroom, and faded endpoints. These measurements do not establish subjective music quality.
- Visually inspected `out/extracted-preview.png`, `out/contact-sheet.jpg`, and `out/boundary-sheet.jpg`. Also decoded the actual MP4 at 30 seconds directly into an in-memory PNG and inspected it at 1920×1080. Ownership and readiness text is readable. Focus outlines align with owner/status columns. The final pending status is visible. The boundary sheet shows the intentional fade through the cream background. The sample label persists through those boundaries. The black sixth contact-sheet tile is unused grid padding, not a video frame.
- `npm ls --depth=0` exited 0. Installed and lockfile root dependencies agree with `package.json`. Both Remotion packages are pinned to 4.0.532. React and React DOM are pinned to 19.2.4. Node is v24.15.0.
- Resolved the documented external Playwright module at `/Users/altanesmer/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js`. The capture harness waits for its fixture ready marker and fonts and saves 1920×1080 screenshots. This review did not overwrite the captures or reinstall dependencies.
- Read `src/index.jsx`, `src/timeline.mjs`, `fixture.html`, both scripts, `package.json`, `package-lock.json` root metadata, `.gitignore`, README, music notes, and the canonical skill. The composition uses local assets and frame-driven motion. Its five scenes total 42 seconds. It labels the product as a sample and its closing caption explicitly calls it fictional. It does not simulate a recorded interaction.

## Asset-rights evidence

The [official Mixkit source page](https://mixkit.co/free-stock-music/corporate-music/) lists Close Up by Michael Ramir C. The [Music Free License](https://mixkit.co/license/modal/musicFree/) permits commercial and noncommercial web/social use and excludes the offline/broadcast/game uses named in the project notes. The [current terms](https://mixkit.co/terms/) show the recorded revision date of October 2, 2025. Project notes preserve source/license/terms URLs, retrieval date, and the verified file hash.

`git check-ignore public/close-up.mp3` confirms the raw track is ignored. README and music notes expressly exclude it from redistribution archives and direct recipients to obtain it from Mixkit. No archive is offered by this project. The live [Remotion license](https://www.remotion.dev/license) supports the documented evaluation eligibility and size threshold. The Mixkit download-dialog URL was not accessible through this review's web tool; no new download or bypass was attempted.

## Independent Comment Sicko audit

Applied the scoped `no-comments` leaf and Comment Sicko role directly. Child delegation was prohibited for this assignment. Scanned `src/`, `scripts/`, and `fixture.html`, including lint and TypeScript suppressions. No comments, commented-out code, or suppressions were present. The URL string in `scripts/check.mjs:16` is not a comment.

Touched application files none. Deletion count 0. Restorations 0. Reruns 0. MUST KILL flags none. Architect sketch, fixes, encoding offers, encodings, and unenforced constraints none. Skipped application edits and child delegation under the assignment's read-only fence.

## Inspection limits

Subjective audio audition and full real-time playback were not performed. The project's README already discloses those limits. Fresh dependency installation, recapture, preview startup, and another full render were not rerun because this independent assignment prohibited those writes and left final artifact generation with the implementer. The full checker was not run concurrently because it writes the contact sheets.

The Prove It Works principle changed verification to inspect and decode the actual MP4 rather than rely on source or the implementer's summary.
