---
name: caw-do-release
description: Prepare, verify and package a new Code AI Workspace release, archive the previous artifacts, then commit with Release v followed by the version and push to origin. Use for executing a requested release, not issue implementation or release planning.
---

# Create and push a release

Locate this repository using `AGENTS.md` and `WORKSPACE_SETUP/scripts/workspace_manager.py`. Read [contributor instructions](../../../AGENTS.md) and the [development/release guide](../../../maintenance/DEVELOPMENT.md), including artifact verification and publication. Resolve paths from the repository root. This repository-only skill stays outside release ZIPs and generated workspaces.

A request to execute this workflow authorizes release preparation, archiving, committing and pushing. Continue through those steps without another routine confirmation; execution-environment approvals still apply. A request to create/edit this skill, discuss a release or review a plan does not execute a release.

## Establish the release

Confirm `origin` is `matas-g/code-ai-workspace`, the intended branch/upstream (normally `main`), current working/staged changes, recent history and the latest published ZIP/checksum. Include completed changes in the requested release scope; preserve unrelated work and staging. Do not publish from an uncertain repository or integration point.

Use a version explicitly requested by the user. Otherwise use an already prepared product version newer than the latest release, or increment the latest release's patch number once. Read/edit product `VERSION` only in `WORKSPACE_SETUP/scripts/workspace_manager.py`; leave `DESIGN_VERSION` alone unless a design-version change was requested. Require a newer numeric `major.minor.patch` version; do not silently bump again after a failed attempt.

Review changes since the previous release. Update concise user release notes, the development changelog and version-scoped validation evidence. Keep historical results and unresolved compatibility limits; describe existing-user transition without automatic workspace upgrades. Never present unobserved GUI/Copilot/native-platform results as passed.

## Prepare and verify

Follow the guide's commands with installed compatible Python and `-I -S -B`. Prepare source README labels and manifest hashes with the builder, then run required checks in a disposable package copy under `_tmp/`. Confirm the tested shipped bytes match final source. Record exact interpreters, environments, outcomes and unavailable checks; distinguish required release gates from acknowledged pilot limitations. Failed checks or an unmet required gate stop publication while independent preparation continues.

Build the versioned candidate with:

```sh
python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py --output-dir ABSOLUTE_RELEASE_DIRECTORY
```

Use an existing absolute output directory, normally the repository root. Verify the exact ZIP/checksum, allowlisted inventory, member bytes/hashes, executable metadata and user links. Exercise extracted default/custom-name setup and daily commands after moving the generated folder and removing its installer, as described in the guide. Check reproducibility against the isolated tested inputs. If shipped inputs change afterward, rebuild and repeat affected checks; do not publish stale evidence or artifacts.

After the candidate passes, move the previous ZIP and checksum to `_old zips/` without overwriting archived files or changing their bytes. Keep the new pair at the usual repository-root paths. Existing output destinations are never overwritten: reuse a previous attempt only after verifying its provenance and exact bytes; otherwise report the collision. Record actual final evidence and inspect the complete diff. Keep maintainer files, tests and builder outside delivery; retain launcher mirrors and the release allowlist.

## Commit and push

Stage only the intended release changes, new ZIP/checksum and removal of the previous root pair; archived files remain ignored. Inspect both staged and unstaged diffs. The commit subject must be exactly `Release v<version>`, for example `Release v0.1.22`, using the effective product version. Put included issue references and useful validation details in the body; do not add an issue-number prefix to the release subject.

Commit, then push normally to the confirmed origin branch. Verify the remote branch SHA matches the release commit and report any remaining local changes. Do not force-push or rewrite existing commits. On a rejected push, inspect remote state and report the blocker; on a transient failure, check whether the push already succeeded before retrying. If the release commit already exists, resume verification/push rather than making a duplicate release commit. Preserve completed artifacts and report the exact incomplete step if publication cannot finish.

The usual release consists of the tracked ZIP/checksum and release commit pushed to origin. Create a tag or GitHub Release object only when separately requested. Finish with the version, artifact/checksum, commit link, verified push result, checks and material remaining limitations.
