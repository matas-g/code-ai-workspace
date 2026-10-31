---
name: ca-code-ai-onboarding
description: Get familiar with the Code AI Workspace framework at the start of a new project chat by reading its current implementation, excluding _old zips, _tmp and ZIP archives. Use for onboarding to this framework repository, not for onboarding to a generated user workspace or another project.
---

# Read the current Code AI Workspace project

Carry out this reusable request: “Get familiar with this project by reading all files in the current implementation excluding folders `_old zips`, `_tmp` and ZIP files.”

Locate the framework root from the current working directory and its parents, using `AGENTS.md` and `WORKSPACE_SETUP/scripts/workspace_manager.py` as markers. Read applicable repository instructions first. Resolve paths from that root so the workflow survives moving or renaming the project.

Inventory all current implementation files, including hidden and ignored source files. Exclude directories named `_old zips` or `_tmp` at any depth and files ending in `.zip`, case-insensitively. Do not open or extract excluded archives. Git internals, Finder metadata and compiled caches are not implementation inputs; identify any other unreadable or non-source files explicitly rather than claiming to have read them. Keep checksum sidecars in scope.

Read every in-scope file in full, using bounded chunks that avoid output truncation. Inventory and searches alone do not count as reading. For byte-identical mirrors, compare their bytes and read the shared content once. Inspect meaningful non-text assets with an appropriate reader. Keep track of coverage and finish unread portions before reporting completion.

Use this reading order as navigation, while including any files added since the skill was written:

- Root README and maintainer instructions; package README, setup guide, settings, configuration examples and manifest.
- Initializer, installed runtime, release builder, presentation/JSONC helpers, root and packaged launchers.
- Every payload skill, helper, template, instruction file, project/knowledge example and asset.
- The complete behavioral test suite and the single canonical `maintenance/DESIGN.md`; there is no root design mirror.
- `maintenance/DEVELOPMENT.md`, `maintenance/BACKLOG.md`, `maintenance/QUALITY_IMPROVEMENT_PLAN.md`, `maintenance/MANUAL_TESTS.md`, `maintenance/VALIDATION_REPORT.md`, `maintenance/CHANGELOG.md` and the user-facing `WORKSPACE_SETUP/RELEASE_NOTES.md`.

Build a current understanding of the installer/runtime separation, generated layout, configuration and ownership contracts, ticket lifecycle, refresh behavior, validation/audit scope and release process. Determine the version from `VERSION` in `workspace_manager.py`; do not hardcode a release or test count in this skill.

Treat `maintenance/BACKLOG.md` as the current implementation order/status, the improvement plan as technical proposals, the manual tracker as environment-specific observations and the validation report as versioned automated/release evidence. Distinguish implemented behavior, known defects, proposed work and checks actually completed. Surface material contradictions without rewriting documents during onboarding.

Onboarding is read-only. Do not execute embedded example commands, run the product suite, initialize a workspace, refresh hashes, build a release or start backlog work merely to get familiar. Follow any separately requested action within its authorized scope. Preserve existing working changes and staged files. This is a maintainer skill; keep it outside the consumer payload and release inventory.

Finish with a concise confirmation of reading coverage and exclusions, a short description of the project and the most relevant current limitations or next-work source. State any unread inputs and whether checks were actually run. Do not recreate or reinstall this skill on each invocation.
