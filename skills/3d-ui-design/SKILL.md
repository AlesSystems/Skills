---
name: 3d-ui-design
description: Use when designing, implementing, updating, or critiquing web UI containing interactive 3D objects or scenes, including model sourcing and generation. Covers existing Three.js, React Three Fiber, and other web renderers. Ordinary CSS depth/tilt effects and VR/AR interfaces are outside this scope.
metadata:
  owner: altanesmer
  status: active
  last_reviewed: "2026-10-02"
  review_after_days: 90
  risk: medium
  tools: [browser, shell, web]
---

# 3D UI Design

Own the scene, its assets, and its integration into a usable web interface.
Design and implement within the existing project; critique is a supporting mode.

## Understand and state the direction

Inspect repository instructions, imports, renderer, UI conventions, selection
state, asset pipeline, browser support, and performance targets. Trace how scene
events reach application state before editing. Discover tool capabilities rather
than assuming Blender, a generation connector, or browser control exists.

Inspect supplied visual references at the requested timestamp or state. Extract
composition, materials, lighting, camera behavior, interaction, and UI integration;
adapt these to the project. If frames are inaccessible, disclose that limitation
and work from verified references and project cues. A title or transcript does
not establish visual details.

State a short direction, then implement within the task's authorization. Ask only
when a missing decision materially changes the result. Establish:

- **Composition:** one clear focal object, readable silhouette, useful depth,
  and space for stable HTML controls and text at wide and narrow sizes.
- **Look:** materials, environment light, contact shadows, and contrast consistent
  with the surrounding interface; effects serve the scene's purpose.
- **Camera:** intentional initial framing, orbit/zoom limits, target, and reset.
  Enable camera movement when it helps the task.
- **Interaction:** what selecting or manipulating an object means, its immediate
  feedback, and how it shares authoritative state with conventional controls.

For critique, inspect without editing unless fixes are requested. Report concrete
defects, their effect on the task, evidence, and the smallest useful correction.

## Acquire and implement

For sourced or generated models, read [model-assets.md](references/model-assets.md).
Own complex model acquisition, generation, inspection, and optimization through
delivery; a prompt or concept image is not a mesh. Use free solutions first.
Paid services require an explicit request and an authorized budget.

Keep an existing renderer, including one outside the defaults. With no renderer,
use [React Three Fiber](https://r3f.docs.pmnd.rs/getting-started/introduction) for
React and [Three.js](https://threejs.org/docs/) otherwise. Add helpers only for an
actual need; verify installed versions and peer compatibility in current official
docs. Preserve framework client/SSR boundaries and existing component conventions.

Integrate a visible, selectable asset before expanding the scene. Use application
state for meaningful actions and renderer-local updates for frame animation.
Keep essential navigation, selection, and reset available through accessible HTML.
Provide equivalent keyboard and touch actions; hover is an enhancement. Canvas
gestures must preserve surrounding page scrolling and control focus.

Keep layout stable while assets load. Provide loading, error/retry, and usable
renderer fallback states. Handle initialization failure and context loss, not
only model download failure. Match quality to measured project/device budgets:
bound pixel ratio, draw calls, geometry, and texture memory; pause unnecessary
offscreen work. Clean up only resources this integration owns.

Reduced motion preserves task feedback and direct manipulation while reducing
automatic rotation, parallax, and camera travel. Apply preference changes live.

## Prove and show

Run relevant project checks, then inspect the actual UI in a browser. Verify:

1. Desktop and narrow layouts, camera framing, legibility, and final asset loads.
2. Object interactions and their HTML equivalents, keyboard focus, reset, repeated
   input, and touch gestures without scroll conflicts. Label emulation as such.
3. Reduced-motion behavior, including changes while the page is open.
4. Slow/failed asset loading, error recovery, and renderer unavailability/context
   loss; surrounding controls and task content remain usable.
5. Representative responsiveness and resource use against project targets.

Show a final screenshot and report what changed, asset provenance, checks with
observed results, and remaining limitations. A screenshot proves appearance;
interaction and performance claims need runtime evidence. Mark unavailable
checks unverified and the affected work incomplete. A successful build alone
does not satisfy visual acceptance.
