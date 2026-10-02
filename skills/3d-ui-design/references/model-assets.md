# Model sourcing and generation

Read when a task needs 3D assets. Deliver actual, inspected models that fit the
scene and its interaction; own the acquisition path rather than leaving it as a
suggestion to the user.

## Choose a free path that meets the brief

Inspect existing project assets first. For each required object, establish its
silhouette, detail visible at the intended camera distance, dimensions, origin,
materials, and required selectable parts or animations. This decides whether a
licensed model, procedural modeling, or AI generation is suitable.

| Path | Use and completion condition |
|---|---|
| Existing or freely licensed model | Find the original source, confirm permitted use and redistribution, acquire the actual file, then inspect it in the project's renderer. |
| Procedural modeling | Use available renderer geometry or local modeling tools. For complex assets, author/export a scene with the required silhouette, topology, parts, materials, and animation; retain the generating source. |
| AI model generation | Discover a configured tool and its current capabilities/terms. Give it a model brief, obtain the exported mesh and textures, then inspect and repair the output. |

Suitable free sources and tools are the fallback when a preferred path is
unavailable. Research alternatives and carry the asset through integration.
If a free solution cannot meet the required result, identify the specific missing
capability while continuing independent UI work. Label temporary geometry and
keep the required asset unfinished; changing its required fidelity or behavior
is a material design decision.

Local [Blender automation](https://docs.blender.org/manual/en/latest/advanced/command_line/index.html)
can generate and repair complex scenes when Blender is available. Use an authored
script or editable scene so the result is reproducible. Renderer geometry can
generate browser-native meshes without Blender when it meets the brief. Detect
tools and project permissions before installing anything.

External services are optional paths, not mandatory dependencies. Check current
official documentation for export, account requirements, credits, licensing, and
whether a genuinely free path exists:

- [Sketchfab downloads](https://sketchfab.com/developers/download-api/downloading-models)
  and [license/attribution guidelines](https://sketchfab.com/developers/download-api/guidelines).
- [Meshy text-to-3D](https://docs.meshy.ai/en/api/text-to-3d).
- [Tripo generation](https://platform.tripo3d.ai/docs/generation).

Use only task-authorized accounts, uploads, and spending. Free access does not
authorize new account signup or uploading private project references. Paid model
purchases or generation require an explicit request and an authorized budget.
Raster image generation may help concept art or textures; it does not produce a
usable 3D model by itself.

## Preserve rights and provenance

Verify each asset's actual license and any plan-dependent generated-output terms
from the original source. Record creator/provider, source URL or generation task,
license and required attribution, modifications, and rights to input references
beside the assets using project conventions. Keep editable sources separately
from optimized delivery files. Free download is not proof of reuse rights.

Prefer checked-in or project-hosted production assets over unowned hotlinks.
Acquire data files from verifiable sources; executable project imports and build
scripts from an asset archive need separate inspection.

## Inspect, optimize, and load

Prefer GLB/glTF 2.0 when the renderer supports it; retain another existing format
when conversion would lose required behavior. Review the tool's current
[glTF export guidance](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html).
Preserve referenced buffers and textures when delivering separate glTF files.

Load the real export in the target engine and inspect:

- Scale, orientation, bounding box, origin/pivots, clipping, and camera target.
- Silhouette, normals, material channels/color handling, texture paths, lighting,
  and visible artifacts at the actual viewing distance.
- Named/selectable parts, their picking targets, assembly transforms, animation
  clips, and reset behavior. A single fused mesh may not satisfy part selection.
- Renderer/decoder support for extensions and compression, plus slow or missing
  asset behavior.

Measure download size, loading time, geometry, draw calls, texture memory, and
runtime cost. Optimize the observed bottleneck with existing tools: remove unseen
geometry, reuse materials/instances, reduce excess texture resolution, or apply
supported compression/LOD. Preserve interaction, pivots, materials, and animation;
reload and compare after optimization. Use project targets rather than a universal
polygon or megabyte limit.
