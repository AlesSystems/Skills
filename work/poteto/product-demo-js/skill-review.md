# Independent skill review

Reviewed `/Users/altanesmer/agent-library/skills/product-demo-js/SKILL.md` against the approved brief. Re-read the primary agent's corrections to lines 34 and 52. Both findings are resolved. No actionable findings remain within the assigned scope. This reviewer changed only this report and spawned no child agents.

## Resolved findings

1. **Resolved P2. Retaining original captures could undo redaction.** The original line 34 required keeping original captures after line 30 permitted redaction. The revised line 34 now requires safe captures, retaining and delivering only sanitized copies when redaction is needed, and keeping raw sensitive inputs outside the output project. This closes the delivered-source privacy gap.

2. **Resolved P2. Reporting a required Remotion license did not establish permission to render.** The original line 52 required only reporting a paid-license requirement. The revised line 52 requires confirming that an applicable paid license is in place before rendering for the intended use, reporting a missing license without buying one, and continuing evaluation only where permitted. This agrees with the [official Remotion license](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md), which requires a Company License for entities outside its free-license categories.

## Validation

- `/usr/bin/python3 /Users/altanesmer/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/altanesmer/agent-library/skills/product-demo-js` passed with `Skill is valid!`, both before and after the corrections. The default `python3` failed because it lacks PyYAML. No installation was needed.
- The name matches the folder and naming rules. The description selects code-generated product demos and excludes unrelated video edits and standalone motion. The skill has no local supporting references to resolve.
- All eight external references resolved. The animation, sequence, audio, Studio, and render references point to official Remotion documentation. The render documentation supports yuv420p, and the sequence documentation supports local frame timing.
- [Mixkit's music license](https://mixkit.co/license/modal/musicFree/) permits commercial web and social videos, including online advertisements. It restricts other distribution channels. The skill correctly requires checking intended distribution rather than treating "free" as universal permission. The [site terms](https://mixkit.co/terms/) prohibit mass downloads. The skill's single-track normal download instruction agrees with that restriction.
- Prove It Works guided checking the actual canonical file, validator result, and official references. The no-comments delegation step was skipped because this assignment explicitly forbids child agents and contains no source-code comments to review.

## Scenario checks

These are mental forward-tests of instructions. They do not establish that a generated MP4 renders or plays correctly.

| Scenario | Expected behavior and acceptance check | Result |
| --- | --- | --- |
| Supplied screenshots for a 40-second commercial web demo | Reuse screenshots, preserve proportions, animate supported behavior, produce editable JavaScript and a 1920 × 1080 30 fps H.264 MP4 with audible licensed music. Inspect asset notes and verify license eligibility before rendering. | Covered. Revised line 52 requires confirming any required paid license before the intended render. |
| Live product containing customer records | Capture a test account or redact before output. Inspect every retained capture and source asset, not just MP4 frames, for the sensitive data. | Covered. Revised line 34 excludes raw sensitive inputs from the output project and delivers sanitized copies. |
| External music download unavailable | Continue visuals, report missing music, and label any silent export incomplete while music remains required. Preserve exact render commands and identify the missing asset. | Covered by lines 42 and 80. No requirement to bypass access controls or claim a silent export finished. |

The scenario checks and validator were repeated after the corrections. A later behavioral smoke test should render an actual short fixture, run the retained invariant check, inspect representative frames, and verify audible audio. That render was outside this review's assigned scope and remains a validation limitation, not an observed defect.
