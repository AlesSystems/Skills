---
name: product-demo-js
description: Create or revise product demo videos with Remotion and editable JavaScript, using real screenshots, selective recordings, and background music. Use for code-generated product walkthroughs and feature demos. Skip AI-generated footage, unrelated video edits, and standalone UI animations.
metadata:
  owner: altanesmer
  status: active
  last_reviewed: 2026-10-01
  review_after_days: 90
  risk: medium
  tools: [shell, browser]
  dependencies: [node, remotion, react]
---

# Create a product demo with JavaScript

Deliver an editable JavaScript project and a finished MP4. Make the product readable and its demonstrated behavior accurate.

## Establish the brief

Read the supplied product context and assets first. Identify the audience, the useful action to demonstrate, and the final call to action. Ask only for missing facts that block an honest demo.

Default to 1920 × 1080, 16:9, 30 fps, and 30–60 seconds. Use concise on-screen text and background music. Add narration only when requested. Follow the product's brand and any supplied reference style.

For an example without a specified product, use an explicitly labeled fictional fixture. Do not present invented screens or claims as evidence of a real product.

## Collect product evidence

Use supplied screenshots first. Otherwise capture clean screens from the product with an available browser or device tool. Reuse the project's capture harness if one exists. Wait for fonts, images, and the demonstrated state to settle before capture.

Use a consistent viewport and safe sample data. Exclude private messages, credentials, customer records, and unrelated desktop content. Use a test account or redact sensitive content before it becomes an output asset.

Animate screenshots by default. Use a short recording when the interaction itself explains the feature, such as a drag, an editor change, or a result that updates. Show an interaction only if the recording or observed product behavior supports it. Avoid rebuilding a supplied interface in React or fabricating its responses.

Keep safe captures with the project. If redaction is needed, retain and deliver only the sanitized copies. Keep raw sensitive inputs outside the output project. Record each capture's source and the state it demonstrates.

## Find background music

Accept a supplied track as an override. Otherwise find a suitable instrumental track online. Start with [Mixkit stock music](https://mixkit.co/free-stock-music/), and inspect the selected track and current [music license](https://mixkit.co/license/modal/musicFree/) and [site terms](https://mixkit.co/terms/).

Check that the license permits the intended distribution and commercial use when applicable. Read a different provider's license before substituting it. Do not infer permission from a title such as "no copyright."

Use the provider's normal download flow for one selected track. Do not mass scrape or bypass access controls. If the download is unavailable, continue the visual work and report the missing music. Ask for a supplied track or download assistance before calling a music-required video finished.

Save the track title, artist when listed, source URL, license URL, retrieval date, and applicable credit text in the project's asset notes. Preserve a license receipt or permitted snapshot when available. Treat the downloaded track as a licensed production asset. Do not publish or package raw music for redistribution unless its license permits that use.

Choose music to support the pace. Trim at a useful phrase, fade the beginning and end, and keep the level below narration when present. Avoid an audible loop seam.

## Compose with Remotion

Inspect the target project before adding files. Reuse an existing Remotion setup. Otherwise create a small local project with React, Remotion, and its CLI. Keep packages in the video project, outside skill folders. Pin compatible Remotion packages to the same exact version and keep the lockfile.

Consult the current [Remotion license](https://www.remotion.dev/license) for the user's intended use. If that use requires a paid license, confirm the applicable license is in place before rendering for that use. Report a missing license without purchasing one. Continue evaluation work only where the license permits it. Use official docs for the installed version rather than guessing API names.

Model the edit as scenes with a capture, text, duration in frames, and any focus region. A short scene table and one screenshot component usually suffice. Use a separate component when a scene has distinct behavior. Keep the source in JavaScript or JSX unless the target project already uses TypeScript.

Use `Composition` and `Sequence` or `Series` for timing. Drive all animation from `useCurrentFrame()` and `useVideoConfig()`, using `interpolate()` or `spring()`. Do not rely on CSS animation, wall-clock timers, or unseeded randomness. Sequence children receive local frames.

Keep rendering independent of live network assets. Place captures and music in the project's `public/` directory and load them with `staticFile()`. Use Remotion image and media components so rendering waits for assets.

Use restrained pans, zooms, and highlights to explain one action at a time. Preserve screenshot proportions. Hold important text long enough to read. Show a detail crop instead of shrinking the entire interface until its text is unreadable. Avoid decorative motion that competes with the product.

Useful official references:

- [Frame-driven animation](https://www.remotion.dev/docs/animating-properties)
- [Sequences and local timing](https://www.remotion.dev/docs/sequence)
- [Audio](https://www.remotion.dev/docs/media/audio)
- [Studio preview](https://www.remotion.dev/docs/studio)
- [Render CLI](https://www.remotion.dev/docs/cli/render)

## Preview and verify

Open a Studio preview when supported. Render representative stills before the full render, including a detail view and each scene boundary. Inspect them for legibility, crop errors, missing images, and text overlap. Fix observed problems before export.

Render a local H.264 MP4 with a compatible pixel format such as yuv420p and AAC audio. Supply the actual entry point, composition ID, and output path to the CLI.

Check the finished MP4, not just the source. Verify its dimensions, frame rate, duration, video codec, and audio stream. Inspect extracted frames and check the audio for silence, clipping, abrupt cuts, and narration balance when applicable. Use available playback for the whole edit when possible, and state any inspection limit.

Leave one runnable check for the project's meaningful invariants, such as matching the rendered duration to the scene timeline and confirming audible audio. Reuse existing checks rather than adding a test framework.

Deliver the MP4, editable source, captures, asset notes, and exact preview and render commands. Identify any missing requirement or unverified claim. Do not publish the video unless the user asks.

Example invocation:

> Use product-demo-js to make a 40-second demo of this product's release workflow. Use these screenshots, focus on assigning an owner and reviewing launch readiness, find free background music, and deliver the JavaScript project and MP4.
