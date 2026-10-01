# Product demo acceptance evidence

## Delivered artifacts

- Canonical skill: /Users/altanesmer/agent-library/skills/product-demo-js/SKILL.md
- Editable example: /Users/altanesmer/Desktop/Ales/Skills/examples/product-demo-js/README.md
- Movie: /Users/altanesmer/Desktop/Ales/Skills/examples/product-demo-js/out/frame-demo.mp4
- Composition: examples/product-demo-js/src/index.jsx
- Scene table: examples/product-demo-js/src/timeline.mjs
- Music evidence: examples/product-demo-js/public/music-license.md

The example depicts Frame, a fictional release-planning product. Three actual browser screenshots of its included local fixture support the edit. Persistent Sample product text identifies the example in every frame.

## Checks run

- Poteto pinned dependency verification passed, commit 7366ac128bdf95f45e6734f412b49a4031800169.
- /usr/bin/python3 quick_validate.py on the canonical skill passed. Default Python lacks PyYAML; the system Python supplies it, so no new dependencies were installed for validation.
- bin/library validate --strict passed, 57 entries.
- bin/library triage inspect product-demo-js reported no findings.
- bin/library plant --dry-run only. No provider homes were changed.
- npm run render with the installed Chrome browser completed.
- npm run check passed. Full MP4 decode, timeline duration agreement, dimensions, video/audio codecs, source captures, licensed asset provenance, and audio signal/fades were checked.
- Repeated representative frame 615 hashes match c6330b19571c93d82cf92178734cafdbeb096212ea7433dbdf1e0c512d472f1c.
- Primary independently inspected final ffprobe data and the MP4-derived contact sheet, boundary sheet, and full-size ownership frame.

Measured output: 1920×1080 at 30 fps; H.264 yuv420p with limited-range BT.709; AAC; 42.005 seconds; 3,997,522 bytes. Stereo audio body RMS 0.0329, peak 0.2220, endpoint RMS 0.0010 and 0.0004. The checker preserves original audio channels when measuring clipping; it does not establish subjective music quality.

Movie SHA-256: 8645e86c0fdda4e568d3ba79f471f25a398ee4846ee1af2301b86d24a1c26bb4.

## Review

Two design candidates were compared by an independent reviewer on one model family. A small scene table won over repeated explicit offsets. The synthesized example keeps the table and applies focal outlines from the other design.

Independent skill review found two privacy/licensing defects. Both were corrected and re-reviewed with no remaining actionable issues. Final example review passed with no open findings, recorded in demo-review.md. The reviewer independently passed source preflight, ffprobe, and full FFmpeg decode, and inspected representative and boundary frames. A preview browser-option documentation error was corrected without changing the source or media.

## Limits

Subjective music listening and full real-time playback were not available and remain unverified. Rendered-frame and technical audio checks passed.

The skill is authored and catalogued in the canonical library. It can be explicitly used by its SKILL.md path. No runtime loader sync/install was performed. Baseline library doctor already failed for a missing Claude link to impeccable. Provider wiring was not repaired or changed.

The initial local delivery created no commits or PR. Publication was subsequently authorized on 2026-10-01. The music file remains a local production asset excluded from git, and source-bundle redistribution permission is not asserted.

Publication review found that mono downmixing could hide clipping in one stereo channel. The checker now decodes original channels. A 42-second AAC regression video with a left-channel square wave and a quieter opposite-phase right channel passed the old checker (mono peak 0.9600); the corrected checker rejects it at the unclipped-audio assertion. The actual demo passes the corrected check with the stereo metrics above. Rendered media is unchanged.

Reproduce the clipping check from `examples/product-demo-js` after rendering:

```sh
ffmpeg -y -v error -i out/frame-demo.mp4 -f lavfi -i 'aevalsrc=0.9*sgn(sin(2*PI*220*t))*min(1\,min(t/1.5\,(42-t)/3))|-0.45*sgn(sin(2*PI*220*t))*min(1\,min(t/1.5\,(42-t)/3)):s=48000:d=42' -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest out/clipping-regression.mp4
node scripts/check.mjs out/clipping-regression.mp4
```

The second command must exit nonzero with `unclipped audio`; restoring mono downmixing makes it pass. The fixture is ignored with the rest of `out/`.

## Detailed records

- [Plan and throughput checkpoint](plan.md)
- [Design synthesis and applied principles](synthesis.md)
- [Skill review](skill-review.md)
- [Demo review](demo-review.md)
