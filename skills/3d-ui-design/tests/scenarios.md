# Behavioral checks

Run each request in a fresh agent context, first without the skill for a baseline,
then with `3d-ui-design`. Give the agent the request and environment facts, not
the acceptance criteria. Keep generated artifacts in a temporary workspace.
Use dry runs to check decisions when tools are unavailable; they do not prove
rendered appearance or a working integration.

## Existing renderer, unavailable browser

Request:

> Update our existing React travel dashboard into a polished interactive 3D
> destination experience inspired by this YouTube reference around 10:00:
> https://www.youtube.com/watch?v=pVAxEpP79v0&t=605s. Use complex landmark models,
> make the destinations selectable, and keep the existing sidebar and search.
> Choose the implementation and finish it; don't make me pick a stack. Also
> show me the result.

Environment: `@babylonjs/core` already owns the map canvas. Sidebar and search
are semantic HTML; existing destination selection is authoritative. No landmark
assets, Blender, or model-generation connector. Reference frames and browser
control are unavailable. Free asset research/downloads are possible; paid services
and account signup are not authorized.

Acceptance:

- Keeps Babylon and existing selection ownership; preserves accessible controls.
- Sources suitable free licensed models and inspects them before integration.
- Names actual touch, reduced-motion, asset-failure, and renderer-fallback checks.
- Treats missing video frames, runtime inspection, and screenshots as unverified.
- Does not claim a dry run, build, or resting screenshot proves interactions.

Baseline on 2026-10-02: preserved the renderer and selection state, proposed
licensed sourcing, and disclosed missing proof. It did not specify touch testing
or renderer-fallback testing. These omissions motivate explicit acceptance checks.

## Complex model with no generation setup

Request:

> Add an interactive exploded view of a detailed mechanical watch to our React
> product page. Generate the model as part of the work; let visitors select parts
> and return to the assembled view. Use free solutions and show the final UI.

Environment: existing React app, no renderer, no models, no Blender or generation
service. Normal project dependencies may be added. Free asset research is
available; paid services, new accounts, and uploading private references are not
authorized. Browser control is unavailable during this dry run.

Acceptance:

- Selects compatible React Three Fiber/Three.js rather than a new app template.
- Chooses a concrete free modeling or licensed-source path and preserves separate
  selectable parts, pivots, and assembly transforms.
- Owns model inspection and browser optimization, not only an image or prompt.
- Clearly labels substitutes and missing capabilities; does not call primitive
  placeholders a completed detailed watch or claim a model was generated.
- Includes DOM part selection/reset and honest pending runtime proof.

## Discovery and critique boundaries

Requests to classify separately:

> Build a selectable 3D product scene inside our existing plain JavaScript site.

> Add CSS perspective and hover tilt to these ordinary dashboard cards.

> Build immersive WebXR VR navigation for our browser headset experience.

> Critique this existing interactive 3D product page; do not change its code.

Acceptance: the first and fourth use this skill; the second and third do not.
For the first, reuse a renderer or default to Three.js when none exists. For the
fourth, inspect and report evidence-backed defects without editing; mark missing
visual/runtime evidence unverified. The browser platform alone does not bring
VR/AR into this skill's scope.

Review on 2026-10-02 found that the initial description excluded only native
VR/AR, leaving browser VR/AR in scope. This scenario covers that boundary.

## Acceptance evidence — 2026-10-02

Independent reviewer dry runs A and B satisfied the decision-level criteria:
renderer preservation/defaults, free asset paths, state ownership, explicit
failure checks, and honest missing proof. The corrected discovery classifications
also passed review. No application, model export, or rendered scene was built
as part of these dry runs; live implementation acceptance is not established.

Deterministic checks:

- `bin/library validate --strict`: passed, 59 catalog entries.
- System skill-creator `quick_validate.py`: passed using `/usr/bin/python3`;
  the default `python3` lacks PyYAML, so no dependency was installed.
- `bin/library triage inspect 3d-ui-design`: no metadata findings.
- Local Markdown reference resolution and `git diff --check`: passed.
- `python3 bin/tests/test_library.py`: 67 tests, 61 passed, six failures below.

Repository-wide limitations outside the scene/asset instructions:

- `test_daily_walk_has_one_primitive_per_job` and
  `test_deleted_skills_are_not_on_the_walked_folder`: `grok-build-mini` exists.
- `test_live_folder_is_flat` and `test_skills_home_names_the_flat_folder`:
  `skills/also` exists.
- `test_local_walked_skills_do_not_ship_openai_sidecars`:
  `software-idea-discovery/agents/openai.yaml` exists.
- `test_doctor_reports_origin_main`: the doctor fails on Claude loader links.

The conflicting existing files are present in baseline commit `835d3db`.
Before this work, `bin/library doctor` reported three missing Claude links:
`impeccable`, `product-demo-js`, and `software-idea-discovery`. The new skill is
linked for Codex only, so the doctor also reports its missing Claude link until
that loader is reconciled. A `bin/library plant --dry-run` was performed; no
broad loader reconciliation or unrelated library cleanup was authorized or run.
