# Validation report — design 1.0

**Last updated:** 1 November 2026<br>
**Current scope:** Release 0.1.22 macOS pilot, including integrated ticket-creation recovery for issue #4 and the repository-only release skill. Design remains 1.0. Historical evidence below retains its original scope; current native/manual observations remain in [MANUAL_TESTS.md](MANUAL_TESTS.md).

## Release verification — 0.1.22

Prepared on 1 November 2026 from clean `main` at `ba1d36c`, confirmed equal to live origin/main before preparation. Environment: macOS 26.6.2 (25G83), arm64; Python 3.15.0 (`/opt/homebrew/bin/python3`) and Python 3.9.6 (`/usr/bin/python3`). This release packages integrated [#4](https://github.com/matas-g/code-ai-workspace/issues/4) ticket-creation recovery. Product version is 0.1.22; design 1.0, schemas and Python 3.9+ minimum remain unchanged. Existing generated trees retain their installed tools; adopt this release through fresh setup and manual transfer of permitted content.

| Check | Actual result |
|---|---|
| Python 3.15.0 isolated suite | 120 tests passed in 15.217 seconds; no skips |
| Python 3.9.6 isolated suite | 120 tests passed in 20.080 seconds; no skips |
| Exact candidate archive | 35 allowlisted inputs, manifest and three enclosing entrypoints; all 39 members passed CRC, exact source bytes, manifest hashes, safe inventory, normalized timestamps, executable macOS entrypoint metadata and checksum checks |
| Reproducibility | Byte-identical rebuild from isolated tested inputs; all shipped inputs/entrypoints and manifest match final source |
| Extracted default/custom layouts | Each initialized with 30 daily files and six skills; each passed 63 local links/anchors |
| Relocation and installer removal | Both complete generated trees moved, extracted installer removed, then seven installed daily CLI calls per layout passed from another directory: version, validate, audit, refresh apply, ticket create/archive/restore. Literal multiline details and synthetic repository bytes preserved |
| Documentation/preservation | 13 extracted user links and 62 source/contributor links passed before this entry; 61 current source/contributor links passed after updating the scope header. Repository README, canonical design, manual tracker and root launchers retain baseline bytes; root launchers match canonical sources |
| Previous artifact | 0.1.21 ZIP/checksum moved into ignored `_old zips/` without overwriting or changing bytes |

Commands used `-I -S -B` throughout. Prepared source inputs with `python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py`, copied them into `_tmp/release-0.1.22/verification/WORKSPACE_SETUP/`, prepared that disposable copy, then ran its `tests/test_workspace.py` serially with both absolute interpreters above. Built the final candidate with `python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py --output-dir '/Users/matt/Codex Projects/code-ai-workspace'`. Artifact/lifecycle verification used `python3 -I -S -B _tmp/release-0.1.22/verify_release.py`; final document/preservation checks used its `--static-only` mode. Logs and machine-readable results remain under `_tmp/release-0.1.22/`. `git diff --check` passed.

Artifact: `code-ai-workspace-0.1.22-macos-pilot.zip`; SHA-256 `3abfa395b6a0e29d4bb3216cace964163bb1e4edd1bb30730f96dfd03f2ee800`.

Synthetic fixtures only; no software installation, authentication or global-setting changes. The prior source-based macOS ticket recovery/Copilot observations below apply to unchanged helper/skill/guide bytes; this release run adds automated artifact evidence and does not claim another native GUI/Copilot session. Windows, remaining native launcher/first-use checks and unrelated known issues retain their documented scope. Hard-link support is required for ticket publication; old unmarked partial briefs cannot be detected, and there is no automatic repair, upgrade or power-loss durability guarantee.

## Source-based manual ticket retest — 1 November 2026

The [manual tracker](MANUAL_TESTS.md#observed-macos-session--1-november-2026-source-765ba04) records observed TICKET-RECOVERY-01 results against source `765ba04`, including integrated #4, on macOS 26.6.2 arm64 / Python 3.15.0 / VS Code 1.144.0 / Copilot Chat 0.72.0, Local Agent. Default creation/repeat preservation and archive/restore passed. In a relocated custom layout without the installer, Copilot stopped init/archive/restore on a deliberately incomplete ticket, identified recorded completion and pending resources, and preserved all bytes. The installed skill's recovery link opened the rendered guide; explicit operator reconciliation and retry added only missing resources, after which archive/restore preserved the completed ticket and attachment.

These are scoped source/manual observations, not a new release or a full skill/platform qualification. Incomplete-state UI refusals occurred before helper execution; the prior automated CLI/fault/termination results remain separate. Operator file/hash checks confirmed default/custom lifecycle preservation, unchanged incomplete-state bytes through refusals, preserved brief/plan after reconciliation, and no leftover creation metadata after successful retry. Scratch evidence is under `_tmp/manual-issue4-20261101/`; the durable result is in the manual tracker. Source/package/manifest/version/launchers and published ZIP/checksum retain baseline bytes, as do VS Code user settings. Final checks passed 45 related local links/anchors, preservation of all 59 other tracked files and `git diff --check`. No product-suite rerun was needed for evidence-only edits. No release, version change, staging, commit or push was performed. Existing unrelated failures and Windows/manual gaps remain at their recorded scope; #1 introduced no product manual retest.

## Unreleased release-workflow skill — 1 November 2026

Added [caw-do-release](../.agents/skills/caw-do-release/SKILL.md) against clean baseline `225131b`. It follows the existing release process through preparation, isolated verification, ZIP/checksum checks, previous-artifact archival, an exact `Release v<version>` commit subject and a verified push. With no version supplied, it uses a prepared newer product version or the next patch version. It preserves unrelated changes, records real evidence and limitations, and distinguishes executing a release from creating/editing the skill. Contributor/development discovery tables, release authorization and release-commit conventions are aligned; issue references go in the release commit body. No release was executed while creating this skill.

Checks on macOS 26.6.2 arm64 with Python 3.15.0:

- The bundled skill-creator `quick_validate.py` could not run because PyYAML is unavailable under `-I -S -B`; no dependency was installed. A standard-library fallback checked the simple plain-scalar frontmatter subset used by all five maintainer skills, directory/name agreement, naming/length rules, required description fields and absence of unfinished placeholders. This is not general YAML validation or proof of native skill discovery.
- Local skill/contributor links and anchors passed. Reviewed the workflow against the builder's actual command options, version ownership, output-collision behavior and the development guide. No release commands or remote mutations were executed as a test of the skill.
- Static release inventory/entrypoint inspection confirms that maintainer skills and documents remain excluded. All tracked files outside the five maintenance-document changes retain baseline bytes, including package inputs/manifest, behavioral tests, launchers, product/design versions and published ZIP/checksum. `git diff --check` passed. This instruction/documentation change did not require another product-suite run; the preceding 120-test results retain their original scope.

Scratch validation is under `_tmp/caw-do-release/`. The new skill has only `SKILL.md`; no runtime helper, dependency, UI metadata or shipped skill was added. Skill creation changes are local and uncommitted; no release, version change, staging, commit or push was performed. Native invocation and a future end-to-end execution remain unobserved; existing manual qualifications are unchanged.

## Unreleased ticket creation recovery — issue #4 — 1 November 2026

Implemented [#4](https://github.com/matas-g/code-ai-workspace/issues/4) locally against clean baseline `311b3e3`. A synthetic nine-byte final-brief write followed by an error reproduced the original defect: retry returned `already-present` with brief bytes `# ABC-123`. The isolated baseline package, reproduction and JSON output are under `_tmp/issue-4/baseline/`, `baseline.py` and `baseline.json`; no real ticket data was used.

The authoritative ticket helper now reserves a creation-record directory before resource writes, records only resource names/empty completion receipts, verifies staged bytes, and publishes files through same-directory hard links without replacement. Partial writes, publication collisions, unsupported hard links and interrupted completion/cleanup leave identifiable incomplete state. Repeats and transfers stop for manual reconciliation, reporting completed and pending/unconfirmed resources. User-edited completed files remain byte-identical. The generated daily guide, ticket-init skill and canonical design document recovery and limitations; user release notes distinguish these local changes from the published pilot.

**Environment:** macOS 26.6.2 arm64; Python 3.15.0 (`/opt/homebrew/bin/python3`) and Python 3.9.6 (`/usr/bin/python3`). Python 3.9+ remains the package minimum; #11 is separate work. Product/design versions and configuration/manifest/state schemas are unchanged.

| Check | Actual result |
|---|---|
| Focused creation regressions, Python 3.15.0 | Eight passed in 2.269 seconds |
| Full isolated suite, Python 3.15.0 | 120 passed in 22.423 seconds; no skips |
| Full isolated suite, Python 3.9.6 | 120 passed in 29.454 seconds; no skips |
| Partial writes/verification | Partial writes of brief/plan/review/notes staging files never publish a truncated final file; silent short writes fail verification. Partial creation-record writes and optional-directory failures remain incomplete |
| Interruption boundaries | Injected `KeyboardInterrupt` before and after every traced creation mutation, including record reservation, metadata/staging writes, publication, receipts, optional-directory creation and cleanup. Retry refuses marked results; before reservation no resources were written, and after final record removal all requested resources are complete |
| Hard process exit/CLI | A child terminated with code 91 during a partial staging write, preserving the record/stage and operation lock. After explicit manual lock removal, both installed CLI entrypoints returned code 1 with incomplete-creation guidance. Exercised custom directory names after relocation and installer removal |
| Preservation/recovery | Existing edited brief bytes survive optional-resource failure and explicit manual reconciliation. Publication collision preserves the concurrent user file and prepared bytes; unsupported hard links preserve staged data. Retry create/archive/restore changes no incomplete ticket bytes |
| Metadata/scope | Empty, malformed, nested, out-of-scope and oversized metadata fail conservatively; redirected record/plan/receipt/staging paths are refused. External sentinel bytes/mtime remain unchanged. Metadata does not contain the synthetic private description |
| Source and generated documents | 43 source/contributor local links/anchors passed; default and renamed generated layouts each contain the same 30 daily files and pass 63 local links/anchors. No new deployed file path or inventory entry is needed |
| Package preservation | Source hashes refreshed with the builder; final isolated inputs, tests and manifest match source bytes. All 51 tracked files outside the nine-path change scope retain baseline bytes, including version-owning runtime, AGENTS.md, manual tracker, launchers and published ZIP/checksum. Root launchers match canonical sources |

Hash preparation and suites used the disposable `_tmp/issue-4/final/WORKSPACE_SETUP/` copy. Final commands:

```sh
python3 -I -S -B _tmp/issue-4/final/WORKSPACE_SETUP/scripts/build_release.py
python3 -I -S -B _tmp/issue-4/run_checks.py
python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py
python3 -I -S -B _tmp/issue-4/verify_change.py
```

`run_checks.py` invokes the eight tracked focused methods, the full suite with Python 3.15.0, then the full suite with `/usr/bin/python3`, all using `-I -S -B`. Full logs are `focused-python315.log`, `suite-python315.log` and `suite-python39.log` under `_tmp/issue-4/`. `verification.json` records source/generated link and byte-preservation results; static checks and `git diff --check` were repeated after this evidence entry. Scratch scripts/logs supplement the tracked regressions rather than replacing them.

At the local verification checkpoint, no release ZIP, version change, commit or push had been performed; concurrent staging of implementation files was preserved, and issue #4 was open pending integration. The owner subsequently authorized integration; the live issue records the resulting commit and closure status. The published 0.1.21 ZIP remains SHA-256 `8f080e3c8b7a476090908a90cebb2d57a964ceb06d47604a3c8c5288cd098850`; its original evidence follows below. Existing generated workspaces are not automatically upgraded, and older unmarked partial briefs cannot be identified by the new protocol. Hard-link support is required; there is no direct-write fallback, automatic recovery or power-loss durability guarantee. Native Windows filesystem/GUI, VS Code/Copilot invocation and other manual qualifications remain unobserved here; no new manual result is claimed.

## Release verification — 0.1.21

Prepared on 1 November 2026 on macOS 26.6.2 arm64, after integrating and pushing [test-guard fix e7c37a0](https://github.com/matas-g/code-ai-workspace/commit/e7c37a0026da6a1aa359879ecfc2d4f1b073b1e3) to main. [Issue #1](https://github.com/matas-g/code-ai-workspace/issues/1) is closed as completed, with the acceptance checklist and published evidence verified. The earlier unreleased entries below preserve the state and evidence at the time of those checks.

This is a maintenance pilot with updated product version, user README, manifest and concise release notes. The test guard and maintainer skills stay outside the installation ZIP. Daily behavior, generated layout, design 1.0 and configuration/manifest/state schema 1 are unchanged; existing workspaces are not automatically upgraded. Python 3.9+ remains the current minimum; the approved Python-policy implementation is separate work in #11.

| Check | Actual result |
|---|---|
| Python 3.15.0 isolated suite | 112 tests passed in 20.293 seconds; no skips |
| Python 3.9.6 isolated suite | 112 tests passed in 26.517 seconds; no skips |
| Exact installation ZIP | 35 allowlisted inputs, manifest and three enclosing entrypoints: 39 members; CRC, member bytes, manifest hashes, safe paths, normalized timestamps, executable macOS entrypoint metadata and SHA-256 sidecar passed |
| Repeat build | Byte-identical ZIP from the isolated tested package; shipped inputs match final source |
| Extracted default/custom-name lifecycle | Each initialized with 30 daily files and six skills, passed 62 local links/anchors, then passed seven daily CLI calls from another directory after relocation and installer removal |
| Daily CLI calls | Installed version, validation, audit, refresh apply and ticket create/archive/restore passed; literal multiline details and synthetic repository bytes preserved |
| Documentation | 13 extracted user-document links and 59 source/contributor links passed before recording this section; final static link checks repeated after recording evidence |
| Preservation/archive | Repository README, canonical design, manual tracker and root launchers retain baseline bytes; root launchers match canonical sources. Previous 0.1.20 ZIP/checksum moved into `_old zips/` without overwriting archived files or changing bytes |

The versioned suites ran serially after preparing hashes only in the disposable package copy:

```sh
python3 -I -S -B _tmp/release-0.1.21/verification/WORKSPACE_SETUP/scripts/build_release.py
python3 -I -S -B _tmp/release-0.1.21/verification/WORKSPACE_SETUP/tests/test_workspace.py
/usr/bin/python3 -I -S -B _tmp/release-0.1.21/verification/WORKSPACE_SETUP/tests/test_workspace.py
```

Source preparation and the final artifact used `python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py --output-dir '/Users/matt/Codex Projects/code-ai-workspace'`. The archive is `code-ai-workspace-0.1.21-macos-pilot.zip`, SHA-256 `8f080e3c8b7a476090908a90cebb2d57a964ceb06d47604a3c8c5288cd098850`. Artifact checks used `python3 -I -S -B _tmp/release-0.1.21/verify_release.py`; full suite logs and machine-readable results are in the same scratch directory. `git diff --check` passed.

Synthetic fixtures only. No software installation, authentication or global-setting change was performed. Native GUI/VS Code/Copilot/Windows and first-use checks remain at their previously recorded scope; no new manual result is claimed. Other open runtime/AI/parser issues remain unresolved. Historical versioned evidence below is unchanged.

## Unreleased test write guard — issue #1 — 1 November 2026

Implemented [#1](https://github.com/matas-g/code-ai-workspace/issues/1) locally against clean baseline `85dc48f`. Before editing, both original synthetic audit events were accepted: `scope/../outside` as a write path and an outside symlink destination with an in-scope target. These reproductions emitted events only; they did not attempt real outside writes. Baseline evidence: `_tmp/issue-1/baseline.json`.

The guard now resolves ancestors before collapsing traversal, checks event-specific endpoints and rejects ambiguous descriptor mutations. Symlink creation checks its destination; directory-entry operations preserve link semantics. Relative `dir_fd` writes fail closed, including `os.open` calls whose audit event omits the descriptor; absolute paths remain supported. Only the main thread can change the process-wide scope, workers share it, and nested scopes restore state and `os.open` after exceptions. [Development guidance](DEVELOPMENT.md#test-write-guard) records supported behavior and limits.

**Environment:** macOS 26.6.2 arm64; Python 3.15.0 (`/opt/homebrew/bin/python3`) and Python 3.9.6 (`/usr/bin/python3`). Synthetic fixtures only. Product remains 0.1.20, design 1.0; the older interpreter run qualifies this test change against the currently shipped minimum, not the pending policy change in #11.

| Check | Actual result |
|---|---|
| Focused `AuditGuardTests`, Python 3.15.0 | 12 passed in 0.042 seconds |
| Full isolated suite, Python 3.15.0 | 112 passed in 20.341 seconds; no skips |
| Full isolated suite, Python 3.9.6 | 112 passed in 25.934 seconds; no skips |
| Guard regressions | Both synthetic reproductions rejected; real traversal, sibling/relative paths, symlink ancestors/leaf/dangling links, rename/replace/link endpoints, metadata and descriptor mutations rejected. External sentinel bytes, modes, mtimes and directory inventory preserved |
| Descriptor coverage | Both interpreters support all nine exercised `dir_fd` APIs: open, mkdir, unlink, rmdir, chmod, utime, symlink, rename and link. Relative descriptor writes refused; absolute-path operations permitted |
| Allowed behavior and scope | In-scope writes, metadata, hard links, renames and link-entry cleanup work; readonly reads work; nested exception restoration and worker scope checks pass |

Hash preparation and all tests used the disposable `_tmp/issue-1/verification/WORKSPACE_SETUP/` copy. Commands, run serially:

```sh
python3 -I -S -B _tmp/issue-1/verification/WORKSPACE_SETUP/scripts/build_release.py
python3 -I -S -B _tmp/issue-1/verification/WORKSPACE_SETUP/tests/test_workspace.py AuditGuardTests
python3 -I -S -B _tmp/issue-1/verification/WORKSPACE_SETUP/tests/test_workspace.py
/usr/bin/python3 -I -S -B _tmp/issue-1/verification/WORKSPACE_SETUP/tests/test_workspace.py
```

Full logs are `_tmp/issue-1/suite-python315.log` and `_tmp/issue-1/suite-python39.log`. The regressions are tracked in `WORKSPACE_SETUP/tests/test_workspace.py`; scratch logs are supplementary. Relevant document links and `git diff --check` passed. Only the test file, development guide, changelog and this report changed; source package metadata, shipped runtime/payload, root launchers and published ZIP/checksum retain baseline bytes. No source preparation, release build, version change, staging, commit or push was performed. Issue #1 remains open pending integration of these local changes.

The process-wide hook is instrumentation rather than an OS sandbox: native calls, captured API aliases, unaudited existing-handle writes, existing hard-link aliases and filesystem replacement races remain outside its guarantees. Independent production checks/sentinels remain necessary. No native GUI/VS Code/Copilot/Windows result is claimed or needed for this test-only fix; other issues and historical evidence retain their original scope.

## Unreleased maintainer skills — 1 November 2026

Renamed ca-code-ai-onboarding to caw-chat-onboarding, preserving its full-read behavior and exclusions. Added caw-whats-next (read-only issue shortlist), caw-issue-triage (requested queue/label maintenance), and caw-implement-issue (one issue through implementation, verification and evidence). All four live in repository `.agents/skills/`; shipped payload skills keep `ca-`. Updated contributor/development/design namespace rules and current technical-plan wording. Historical namespace/manual/release evidence retains its original scope.

Checks on macOS 26.6.2 arm64, Python 3.15.0, against clean baseline `09dac26`:

- All four frontmatter blocks passed standard-library validation of the plain-scalar name/description subset used, matching directory names, naming/length rules and absence of unfinished placeholders. The bundled skill-creator quick_validate.py could not run because PyYAML is absent; no dependency was installed. This fallback is not a claim of general YAML conformance or native skill discovery.
- Thirteen new/changed local links resolved, including skill-to-root navigation and the contributor section anchor. The renamed onboarding body is byte-identical apart from its frontmatter name; current callers use the new name and no old SKILL.md alias remains.
- The release builder's 35 allowlisted inputs plus three entrypoint mappings and the package manifest exclude maintainer skill paths. All 46 protected product/package/launcher/artifact files retained baseline hashes. No builder preparation or release rebuild was needed or run.
- A read-only GitHub workflow walkthrough confirmed the origin repository, retrieved 15 open issues and inspected the three `next` issue bodies; all three had no comments. The current test-guard source still matches the #1 finding, supporting it as a ready recommendation. No issues, labels or state were changed. Read-only/triage/implementation authorization and completion boundaries were reviewed by inspection; live mutation workflows were not executed.
- `git diff --check` passed and the Git index was preserved. Evidence is `_tmp/maintainer-skills-20261101/verification.json`; native skill-picker discovery/invocation in a fresh chat remains unverified. No product suite, manual IDE/product run, version change, commit or push was performed.

## Release verification — 0.1.20

Prepared on 1 November 2026 on macOS 26.6.2, Apple Silicon (arm64), from clean baseline `1247b00`. The owner chose a current-source release retaining Python 3.9+; the approved Python 3.12+ transition remains pending in issue #11. This release ships the user-only installation inventory and documentation separation. Daily runtime behavior and the generated layout are unchanged apart from the package version. Design version remains 1.0; configuration/manifest/state schemas remain 1. Existing generated workspaces are not automatically upgraded.

| Check | Actual result |
|---|---|
| Python 3.15.0 behavioral suite | 100 tests passed; 20.144 seconds reported by unittest |
| Python 3.9.6 behavioral suite | 100 tests passed; 26.193 seconds reported by unittest |
| Exact installation ZIP | 35 allowlisted inner inputs, manifest and three enclosing entrypoints: 39 members; CRC, member bytes, manifest hashes, paths, normalized timestamps, executable macOS entrypoint metadata and SHA-256 sidecar passed |
| Repeat build | Byte-identical ZIP built from the isolated tested package copy; its shipped inputs match the final source |
| Extracted default/custom-name lifecycle | Both initialized with 30 daily files and six skills; each passed 62 local Markdown links/anchors, relocation and seven daily CLI calls from another working directory after installer removal |
| Daily CLI calls | Installed version, validation, audit, refresh apply and ticket create/archive/restore all passed; literal multiline details and synthetic repository contents were preserved |
| Documentation | 13 extracted user-document links and 53 source/contributor links passed; final report links checked again after recording evidence |
| Preservation | Repository README, canonical design, manual-test tracker and root launchers retain baseline bytes; root launchers match canonical sources. Previous 0.1.19 ZIP/checksum moved to `_old zips/` without overwriting archived files or changing their bytes |

Both suites ran serially against the isolated `_tmp/release-0.1.20/verification/WORKSPACE_SETUP/` copy after preparing its hashes:

```sh
python3 -I -S -B _tmp/release-0.1.20/verification/WORKSPACE_SETUP/tests/test_workspace.py
/usr/bin/python3 -I -S -B _tmp/release-0.1.20/verification/WORKSPACE_SETUP/tests/test_workspace.py
```

Source preparation/build used `python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py --output-dir '/Users/matt/Codex Projects/code-ai-workspace'`. The final archive is `code-ai-workspace-0.1.20-macos-pilot.zip`, SHA-256 `d429fdc5d8509c882e3fd7c5ce9a646b2bd845a7df7bc47b0edd9f6a76efc148`. Artifact checks used `python3 -I -S -B _tmp/release-0.1.20/verify_release.py`; logs, suite timings and machine-readable artifact results are retained alongside it in the ignored scratch folder.

Synthetic fixtures only. No software installation, authentication, global-setting change, real development-workspace change, Git commit/push or GitHub publication was performed. No issue implementation or manual result is claimed. Native GUI/VS Code/Copilot/Windows and first-use checks remain outstanding, as do the recorded runtime/AI/parser reliability issues. Historical evidence below retains its original dates, versions and scope.

## Local backlog cleanup — 1 November 2026

Removed the local BACKLOG_REVIEW.md after applying its recommendations; the dated review remains available through pinned GitHub history links. Shortened [BACKLOG.md](BACKLOG.md) to the B01–B21 issue/disposition index, deferred scope and evidence pointers. GitHub remains authoritative for imported status/priority. Historical test results and migration evidence below retain their original scope.

Documentation-only verification checked all 21 B IDs, all 15 imported issue targets, retained deferred categories, local paths/anchors and the historical review target. `git diff --check` passed. The pre-existing Git index/staged contents and all files outside these three cleanup paths were preserved. No product tests/build, GitHub issue changes, staging, commit or push were performed. Local evidence: `_tmp/backlog-cleanup-20261101/verification.json`.

## GitHub backlog migration — 1 November 2026

Migrated the actionable macOS pilot backlog from local source `f795735` to [matas-g/code-ai-workspace Issues](https://github.com/matas-g/code-ai-workspace/issues). The working tree/index were clean at inspection; current local files were used. GitHub now owns imported status/priority; [BACKLOG.md](BACKLOG.md) is a B01–B21 issue index with explicit deferred/reconciled/completed scope. The review remains dated, and contributor/design/technical-plan/manual-tracker/onboarding ownership statements now agree.

- **Repository/access:** Confirmed the expected private repository, enabled Issues and write/triage access. Inspected all open/closed issues before mutation: none existed. Created 15 issues, [#1](https://github.com/matas-g/code-ai-workspace/issues/1) through [#15](https://github.com/matas-g/code-ai-workspace/issues/15); no duplicate or historical reconstruction issues. Read back every body, state and label; all match the migration drafts and remain Open.
- **Labels/priority:** Inspected 10 existing labels in the signed-in GitHub UI, reused `bug`, and created exactly `improvement`, `verification` and `next`; all original labels remain. The plugin handled issues; native Chrome handled labels because the plugin exposes no label-management tools, its generic fetch rejects the label endpoint, and no CLI credential was available. Exactly [#1](https://github.com/matas-g/code-ai-workspace/issues/1), [#4](https://github.com/matas-g/code-ai-workspace/issues/4) and [#11](https://github.com/matas-g/code-ai-workspace/issues/11) are marked `next`: trustworthy guard evidence, incomplete-creation detection and the approved Python policy implementation.
- **Reconciliation:** B01/B03 split only for independent outcomes; installation snapshot is #7 and builder snapshot is #13. B08’s remaining current-flow verification is in #15, preserving historical DOC-05 failure and the published-package limitation. B21 stays completed without an active issue. No named current B19 mismatch remains to import; optional restructuring is deferred. B15–B18/B20 and future Windows/IDE/publication work are retained explicitly, with fix-specific retests kept on fixes and residual macOS checks in #14/#15.
- **Links/publication:** Issue evidence links use files/line anchors pinned to the inspected GitHub baseline `f79573520f8f6c71c80947b84fb5d26fb2b06a02`, whose paths were confirmed through the repository tree. Issue bodies contain reproduction/acceptance context rather than relying on ignored logs. Documentation changes from this migration are local and unpublished; remote `main` remains at the inspected baseline. No commit or push was made.
- **Documentation verification:** All 21 B IDs are accounted for exactly once in the index; imported issue links, issue bodies/labels, added documentation links/anchors, index preservation and unchanged product/package/artifact bytes were checked. 85 added-document/issue links passed path/anchor checks, and `git diff --check` passed. On macOS 26.6.2 arm64 with Python 3.15.0, all 48 tracked files outside the ten edited maintainer/navigation documents retained their baseline bytes. Detailed evidence is `_tmp/github-migration-20261101/verification.json`; this is scratch evidence, not a new process document.

This migration changes issue tracking and maintainer documentation only. No product fix, version, manifest, release artifact, repository visibility, Project, milestone, hierarchy, automation or manual-test result was changed. No product suite, release build or native product GUI/Copilot/Windows qualification was run. Python 3.12+ remains approved but unimplemented. Earlier evidence below retains its original version/environment and historical planning context.

## Maintainer backlog review — 1 November 2026

Reviewed B01–B21 against the technical proposals, recorded manual evidence and relevant current source at commit `338334b`. The [lightweight GitHub review](https://github.com/matas-g/code-ai-workspace/blob/f79573520f8f6c71c80947b84fb5d26fb2b06a02/maintenance/BACKLOG_REVIEW.md) recommends short issues, completion checklists, four labels and one source of truth for imported work. The owner selected macOS pilot improvements first and Python 3.12+ for the next pilot release; B10 records that decision while implementation remains open. Proposed scope changes have not replaced the current queue.

Initial-draft documentation checks on macOS with standard-library Python passed: all 21 B items were assessed once, 22 local paths/anchors across BACKLOG.md and BACKLOG_REVIEW.md resolved, and `git diff --check` reported no whitespace errors. The added report-to-review link also resolved. Results are retained under `_tmp/backlog-review-20261101/document-check.json`. Current official GitHub workflow and Python support references were checked during the review.

Later the same day, the owner clarified that tracking must suit one maintainer working with an AI agent. The review was shortened and revised to avoid mandatory hierarchies, estimates, custom status fields, boards, milestones or automation; related fixes can use checklists. BACKLOG.md records this constraint. The simplified documents passed 16 local link/anchor checks, coverage of all 21 items and `git diff --check`. Evidence: `_tmp/backlog-review-20261101/simplified-document-check.json`.

This is a maintainer-document change only. No product suite, release build or native IDE/Terminal/Windows run was performed; no product source, manifest, artifact or manual-test outcome was changed. The earlier evidence below retains its original scope.

## Unreleased user-package separation — 31 October 2026

Moved the single canonical design, full validation history and changelog into maintenance/. Removed the root design mirror and release-to-repository README synchronization. The independent repository README links to contributor material; the canonical user README is emitted once at the ZIP root. User setup/release notes contain no maintenance links. Tests and the builder remain repository tools under WORKSPACE_SETUP/ but are excluded from the installation inventory. Daily runtime/payload files and the generated 30-file layout are unchanged. The obsolete --sync-project-docs option is removed.

**Environment:** Native macOS 26.6.2, Apple Silicon (arm64). Synthetic fixtures only; no software installation, authentication, global-setting change or publication.

| Check | Actual result |
|---|---|
| Python 3.15.0 behavioral suite | 100 tests passed; 12.895 seconds reported by unittest |
| Python 3.9.6 behavioral suite | 100 tests passed; 16.340 seconds reported by unittest |
| New/updated archive regression coverage | Excludes maintainer/leftover files, tests/build tool, development ignore rules and duplicate entrypoint sources; checks missing-entrypoint refusal, independent repository-document preservation and extracted default/custom lifecycle |
| Exact candidate archive | 35 allowlisted inner inputs plus manifest and three enclosing entrypoints: 39 members; paths, hashes, checksum and executable macOS entrypoint metadata passed |
| Source and user documentation | Local paths/anchors passed; 13 user-document links in the extracted ZIP; no maintenance references in its README/setup/release notes |
| Generated documentation | 124 local links/anchors passed across default/custom layouts; each fresh tree has 30 daily files |
| Final extracted artifact lifecycle | Both layouts initialized, moved/renamed and operated after the extracted installer was deleted; 12 validation/audit/refresh/ticket subprocess commands succeeded from another working directory |
| Document/source preservation | Build preparation preserved independent repository README/design/tracker; root Start launchers match canonical sources; published ZIP/checksum remain unchanged |

Suite commands ran serially from an isolated source copy:

```sh
python3 -I -S -B _tmp/distribution-structure-20261031-_yy7lgm7/verification-final/WORKSPACE_SETUP/tests/test_workspace.py
/usr/bin/python3 -I -S -B _tmp/distribution-structure-20261031-_yy7lgm7/verification-final/WORKSPACE_SETUP/tests/test_workspace.py
```

Before the suite, the same copy's builder prepared its hashes. Initial focused verification found one obsolete assertion expecting an unanchored setup link; it was corrected to the actual quick-setup section target. Both full suites above passed after that correction. Logs are _tmp/distribution-structure-20261031-_yy7lgm7/final-python315-tests.log and _tmp/distribution-structure-20261031-_yy7lgm7/final-python39-tests.log; machine-readable summaries are final-suite-results.json and final-artifact-verification.json in the same directory. The final candidate ZIP/checksum stay under its candidate-final/ folder. Source manifest hashes were prepared deliberately with the updated builder.

No new GUI, VS Code/Copilot or native Windows session was run. The macOS shell launcher tests in the suite do not establish Finder/Terminal UI behavior. Changed onboarding/rendering paths still need relevant novice/IDE checks. Known runtime/AI/parser defects remain open; this packaging change does not close them. Backlog B21 records this completed structural scope; B12/B19 retain their remaining work.

## Historical reports

The dated material below preserves its original artifact, command, path and verification scope. References to old mirrors, source locations, counts or options describe those earlier versions/stages; use DEVELOPMENT.md for current commands. Earlier manual-status summaries do not replace the current tracker.

**Date:** 30 October 2026<br>
**Status:** macOS pilot. Copilot orientation inclusion across roots/modes, native Windows and physical GUI behavior remain manual checks.

## Unreleased maintainer-document organization — 31 October 2026

Moved the backlog, technical improvement plan and manual-test tracker into the repository-root `maintenance/` directory. Updated relative links, contributor navigation, the design's tracker-location contract and the project-local onboarding skill references. Historical test results and their dates/version scope are preserved.

Static checks passed 30 local file/section links across the contributor instructions and moved documents. Default and renamed read-only initialization plans each contain 30 daily files and exclude maintainer material. Source manifest hashes, README/design mirrors, release exclusions and onboarding skill metadata were checked; the existing Git index was left unchanged. Evidence is retained under `_tmp/maintenance-reorganization/`. The applied onboarding skill was byte-compared with the validated path-only update.

No behavioral suite or manual IDE test was run for this documentation reorganization. Product/design versions are unchanged. No delivery ZIP was built; the released archive retains its original contents.

## Release verification — 0.1.19

Prepared on 30 October 2026 on macOS 26.6.2, Apple Silicon. This release packages the current implementation with `Code-AI.code-workspace` as the default VS Code filename. Explicit `Development` and custom names remain supported. Existing installations are not renamed or upgraded. Design version remains 1.0; configuration/manifest/state schemas remain 1.

- Python 3.15.0: **98 behavioral tests passed** in 20.066 seconds. Command: `python3 -I -S -B _tmp/release-0.1.19/verification/WORKSPACE_SETUP/tests/test_workspace.py`.
- Python 3.9.6: **98 behavioral tests passed** in 25.392 seconds. Command: `/usr/bin/python3 -I -S -B _tmp/release-0.1.19/verification/WORKSPACE_SETUP/tests/test_workspace.py`.
- Both used an isolated source copy and separate synthetic fixture sessions beneath `_tmp/release-0.1.19/verification/`. Logs are `python315-tests.log` and `python39-tests.log` in `_tmp/release-0.1.19/`.
- Fresh shipped-default, renamed (`Data Platform View`), omitted-setting and explicit `Development` installations each passed **62 local file/section links**, all **six daily Python examples**, sample ticket creation, a scripted folder move to archive followed by command restore, validation/audit and report saving. Each fresh tree contains **30 daily files**, six prefixed skills and installed version 0.1.19. Static project/package documentation passed **40 local file/section links**. Source workflow command: `python3 -I -S -B _tmp/release-0.1.19/check_release.py`; results: `_tmp/release-0.1.19/verification-source.json`.

- The archive has **43 allowlisted source inputs**, their manifest and three enclosing README/launcher copies: **47 files** under `Code-AI-Setup-0.1.19/`. Member bytes, ZIP integrity, executable macOS entrypoint metadata, source hashes, project-root document mirrors and the SHA-256 sidecar match. A second build is byte-identical. AGENTS.md, MANUAL_TESTS.md, the maintainer improvement plan, development fixtures and machine metadata remain excluded.
- The extracted archive passed the same four-layout workflow checks above; final static project/package documentation passed **41 local file/section links** after the manual-tracker evidence link was added. Commands: `python3 -I -S -B _tmp/release-0.1.19/verify_archive.py` and `python3 -I -S -B _tmp/release-0.1.19/check_release.py _tmp/release-0.1.19/extracted-final/Code-AI-Setup-0.1.19/WORKSPACE_SETUP -packaged`. Final results are `_tmp/release-0.1.19/archive-verification-final.json` and `_tmp/release-0.1.19/verification-packaged.json`.

The superseded 0.1.18 ZIP/checksum are archived without overwriting existing files. No manual result was marked passed. Earlier pre-release entries retain their original dates, version scope and statements about the artifacts available at that time.

Known reliability limitations from the existing implementation review remain unresolved: checkout line-ending sensitivity, interrupted ticket-creation detection, restrictive permission preservation during ticket transfers, binding apply to a prior preview, consistent snapshots of verified source bytes, Markdown/frontmatter parsing limits and test-guard coverage. These were not fixed or re-reproduced for this packaging release; passing the existing suite does not establish their absence. The maintainer improvement plan retains the original evidence and proposed work.

## Unreleased verification — default VS Code workspace name

On 30 October 2026, the default `vscode_workspace_name` changed from `Development` to `Code-AI` in shipped settings, the default configuration example and the omitted-setting fallback. Setup text, current guides/design and existing behavioral checks use `Code-AI.code-workspace`. Explicit custom names, including `Development`, remain supported; existing installations are not renamed.

- Python 3.15.0 and Python 3.9.6: **98 behavioral tests passed on each interpreter**, run serially on macOS against an isolated source copy. Commands: `python3 -I -S -B WORKSPACE_SETUP/tests/test_workspace.py` and `/usr/bin/python3 -I -S -B WORKSPACE_SETUP/tests/test_workspace.py` from that copy.
- Fresh omitted-setting, shipped-default, explicitly named `Development` and custom `Data Platform View` installations each passed validation, audit and generated README workspace-link checks.
- Source hashes and prepared root README/design mirrors were checked after documentation preparation. Logs and smoke results are retained under `_tmp/default-vscode-name-20261030/` in the maintainer project.

No native Windows or actual IDE/Copilot test was performed. Product/design versions and the existing 0.1.18 release ZIP/checksum remain unchanged; this is an unreleased source change. Earlier evidence below retains its original scope.

## Release verification — 0.1.18

Prepared on 29 October 2026 on macOS 26.6.2, Apple Silicon. This release includes the six-skill inventory with ca-workspace-refresh, centralized release-version preparation, revised guides and complete Copilot onboarding. Configuration/manifest/state schemas remain 1 and design version remains 1.0. Existing generated workspaces are not automatically upgraded.

- Python 3.9.6: **98 behavioral tests passed**. Command: `/usr/bin/python3 -I -S -B _tmp/release-0.1.18/verification/WORKSPACE_SETUP/tests/test_workspace.py`.
- Python 3.15.0: **98 behavioral tests passed**. Command: `python3 -I -S -B _tmp/release-0.1.18/verification/WORKSPACE_SETUP/tests/test_workspace.py`.
- Runs were serial against an isolated source copy with synthetic fixtures. Logs are `_tmp/release-0.1.18/python39-tests.log` and `_tmp/release-0.1.18/python315-tests.log`.
- Default/custom-name installations from the extracted final archive each passed **62 local file/section links**, all **six daily Python examples**, the sample ticket command, manual archive/command restore, validation/audit and report saving. Fresh trees contain **30 daily files**, six correctly named skills and installed version 0.1.18. Static project/package documentation passed **40 local file/section links**. The same workflow checks passed against the prepared source.
- The archive has **43 allowlisted source inputs**, their manifest and three enclosing README/launcher copies: **47 files** under `Code-AI-Setup-0.1.18/`. Member bytes, ZIP integrity, executable macOS entrypoint metadata, all source hashes, root document mirrors and the SHA-256 sidecar match. A second build is byte-identical. AGENTS.md, MANUAL_TESTS.md, development fixtures and machine metadata remain outside the archive.

Packaged workflow command: `python3 -I -S -B _tmp/release-0.1.18/check_release.py _tmp/release-0.1.18/extracted/Code-AI-Setup-0.1.18/WORKSPACE_SETUP -packaged`. Results are `_tmp/release-0.1.18/verification.json` and `_tmp/release-0.1.18/archive-verification.json`. The superseded 0.1.17 ZIP/checksum are archived without overwriting existing files.

Native Windows, physical GUI behavior, first-use readability and actual Copilot instruction/skill execution remain manual checks. Pending tracker entries now identify 0.1.18; no manual result was marked passed. The pre-release entries below retain their original dates, version scope and statements about artifacts available at that time; “unreleased” there describes their development-stage status.

## Unreleased documentation verification — complete Copilot onboarding

On 29 October 2026, the quick setup was extended through prerequisites, creation, repository population, refresh, opening VS Code, verified overview/reference-map context, orientation review, a basic context/ticket/audit check and the first daily task. Links identify packaged templates and direct users to their generated copies. Orientation editing is optional; unavailable features have explicit fallback checks. Extended maintainer checks remain separate. The mixed manual-completion table was replaced with focused prerequisites, optional follow-up and conditional troubleshooting. The landing/generated READMEs and design section 14.1 now use the same handoff; runtime behavior and schemas are unchanged.

Fresh default/custom-name installations each passed **62 local file/section links**, the **six daily Python examples**, the new `TEST-1` sample through the direct-command fallback, manual archive/command restore, validation/audit and report saving. Synthetic overview/reference-map edits remained informational. Static project/package documents passed **40 local file/section links**; all **43 source hashes** and both root document mirrors matched. Command: `python3 -I -S -B _tmp/copilot-onboarding/check_guides.py -final`. Results are `_tmp/copilot-onboarding/verification.json`. The setup guide is 1719 words versus 1658 before this change (about 4% longer).

The linked official [instruction](https://code.visualstudio.com/docs/agent-customization/custom-instructions) and [skill](https://code.visualstudio.com/docs/agent-customization/agent-skills) references were rechecked on 29 October 2026. No IDE/Copilot session was exercised; these checks do not certify onboarding usability, automatic loading or skill execution by Copilot. DOC-05 remains pending on both platforms. The behavioral suite was not rerun for this documentation-only change; prior results below retain their original scope. No new delivery ZIP or product/design version change was made.

## Unreleased documentation verification — guide organization

Reviewed the current implementation and project documents, excluding release ZIPs, machine metadata and the `_tmp`/`_old zips` development folders. The landing README retains the project overview and quick start; SETUP_GUIDE.md owns installation/settings/troubleshooting; the generated root README owns folder management, refresh choices and recovery; DAILY_WORK.md owns ticket/review/audit workflows and the optional Python reference; COPILOT_GUIDE.md owns context preparation, discovery and fallback. Knowledge guides retain their separate note-authoring purpose. The comprehensive design and historical evidence are preserved.

Repeated refresh, ticket and Copilot procedures in the setup guide were replaced with guide pointers; short entry-point quick starts remain usable independently. The setup guide is **1658 words**, down from **2672** (about 38% shorter). The five distinct landing/setup/generated guides are about **19% shorter overall**, using whitespace-delimited counts that include headings, tables and commands. Wording also clarifies manual ticket moves, external ticket links, audit scope and outer-folder renaming. Runtime behavior is unchanged.

The organization follows [GitHub's README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) and [Google's linking guidance](https://developers.google.com/style/cross-references): keep a useful landing page, provide enough context for the immediate action and link selectively to related detail. VS Code's [instruction](https://code.visualstudio.com/docs/agent-customization/custom-instructions), [skill](https://code.visualstudio.com/docs/agent-customization/agent-skills) and [workspace event](https://code.visualstudio.com/api/references/vscode-api#workspace.onDidChangeWorkspaceFolders) references were rechecked on 28 October 2026; their documented behavior does not establish this layout's actual Copilot compatibility.

On 28 October 2026, **98 behavioral tests passed** on Python 3.9.6 and Python 3.15.0 on macOS, run serially against an isolated source copy. Commands: `/usr/bin/python3 -I -S -B _tmp/guide-coherence/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/guide-coherence/verification/WORKSPACE_SETUP/tests/test_workspace.py`. Logs are `_tmp/guide-coherence/python39-tests.log` and `_tmp/guide-coherence/python315-tests.log`.

Default and custom-name installations each passed **56 local file/section links**, all **six daily Python examples**, manual archive followed by command restore with unchanged brief contents, JSON validation/audit and explicit report saving. Static project/package documentation passed **32 local file/section links**. The 43 source hashes and root README/design mirrors match; results are `_tmp/guide-coherence/verification.json`. These automated checks do not certify rendered usability or IDE discovery. DOC-04 remains pending on both platforms; prior manual results are unchanged. No new delivery ZIP or version change was made; the released archive below retains its original contents.

## Unreleased verification — repository landing README

The shared repository/release README now explains capabilities, prerequisites, a five-step quick start, generated layout, scope/portability, help and contribution entry points. Repository population and manual refresh precede opening VS Code. The setup guide follows the same sequence. The structure follows [GitHub's README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), checked on 28 October 2026. The builder relocates package-relative Markdown links for the root copy, including fragments, while preserving external URLs and same-document anchors.

On 28 October 2026, **98 behavioral tests passed** on Python 3.9.6 and Python 3.15.0 on macOS 26.6.2, Apple Silicon. Commands: `/usr/bin/python3 -I -S -B _tmp/readme-landing/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/readme-landing/verification/WORKSPACE_SETUP/tests/test_workspace.py`, run serially. Logs are `_tmp/readme-landing/python39-tests.log` and `_tmp/readme-landing/python315-tests.log`. The release test additionally verifies that relocated guide links reach the same bytes and preserve external/section targets.

Additional checks passed all 12 local file/section links in each of the repository, package, extracted-root and extracted-package README copies. A 47-file test archive initialized default/custom-name trees; synthetic repository folders in all three groups, followed by approved interactive refresh, produced the expected five VS Code roots and successful validation. Results are `_tmp/readme-landing/navigation-checks.json`. These checks do not open VS Code or certify usability; DOC-03 remains pending on both platforms. No new delivery ZIP was created, and the existing release archive/version remain unchanged.

## Unreleased documentation verification — daily workflow

DAILY_WORK.md now leads with Copilot skills and refresh launchers, with all manual Python examples in a collapsed optional reference at the bottom. The guide is 633 words, down from 825 (about 23% shorter). Baseline capture, initial manual refresh, preservation and recovery guidance remain included.

Read-only default/custom-name plans each verified 44 local links/anchors across the guides, orientation and refresh skill, and parsed all six Python examples against the current CLI. Checks also confirmed terminal examples appear only in the final disclosure, source hashes match and design copies are synchronized. Results are recorded in `_tmp/daily-work-focus/verification.json`. Runtime behavior is unchanged; the behavioral suite was not rerun for this documentation edit. Actual rendering and first-use readability remain pending under DOC-02 in MANUAL_TESTS.md. No new release ZIP was created.

## Unreleased development verification — refresh skill

The new explicit ca-workspace-refresh skill delegates to the existing noninteractive refresh tool. It previews changes, requests approval, repeats the preview before applying, retains missing registrations unless cleanup is explicitly requested, and applies as its final tool action. Guides recommend the manual launcher before first opening the VS Code workspace and explain possible Copilot interruption during later updates. No refresh algorithm, configuration schema or automatic upgrade behavior changes.

On 28 October 2026, **98 behavioral tests passed** on Python 3.9.6 and Python 3.15.0, run serially against `_tmp/workspace-refresh-skill/verification/WORKSPACE_SETUP` on macOS 26.6.2, Apple Silicon. Commands: `/usr/bin/python3 -I -S -B _tmp/workspace-refresh-skill/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/workspace-refresh-skill/verification/WORKSPACE_SETUP/tests/test_workspace.py`. Logs are `_tmp/workspace-refresh-skill/python39-tests.log` and `_tmp/workspace-refresh-skill/python315-tests.log`.

The extended namespace test requires all six skill folders. A new behavioral test covers default/custom-name installation, metadata and deployed links, user ownership, relocation, read-only preview, application with settings/repository-content preservation, and validation errors when the new skill is removed. Existing archive/manifest, launcher, ticket and concurrent-edit tests also pass. The unreleased source inventory has 43 inputs and generates 30 daily files; these counts do not describe the existing released archive below.

Final read-only default/custom-name plans each passed 44 local file/section link checks across the three guides, orientation and new skill. All 43 current source hashes match the manifest and both design copies are synchronized.

The generic Codex skill validator could not run because its local PyYAML dependency is unavailable. The actual Copilot frontmatter was checked with the framework's strict metadata validator; no dependency was installed. Automated checks do not execute Copilot or prove its approval behavior. SKILL-05 in MANUAL_TESTS.md remains pending on both platforms for discovery, approval/reapproval, first-root changes, interruption and launcher recovery. No new delivery ZIP was created; version and released archive remain unchanged.

## Unreleased development verification — centralized release versioning

On 28 October 2026, **97 behavioral tests passed** on Python 3.9.6 and Python 3.15.0, run serially against an isolated source copy. Commands: `/usr/bin/python3 -I -S -B _tmp/release-versioning/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/release-versioning/verification/WORKSPACE_SETUP/tests/test_workspace.py`. Logs are `_tmp/release-versioning/python39-tests.log` and `_tmp/release-versioning/python315-tests.log`.

Four new tests cover a synthetic version change propagated through the default ZIP filename, enclosing folder, README labels, source hashes, fresh installed state and daily CLI; static version reading without runtime execution; invalid version/output refusal before preparation writes; explicit root-document synchronization; preservation of historical test/changelog content; and byte-identical repeated ZIP builds. Existing custom-name, relocation, launcher and daily workflow coverage also passes.

The product version remains unchanged until a new release is prepared. No new delivery ZIP was created for this development change; the released archive and evidence below remain associated with their original versions. No manual GUI/Copilot result is inferred from these automated checks.

## Verification — released 0.1.17

- macOS 26.6.2, Apple Silicon.
- Python 3.9.6: **93 behavioral tests passed**.
- Python 3.15.0: **93 behavioral tests passed**.
- Commands: `/usr/bin/python3 -I -S -B _tmp/guide-review-0.1.17/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/guide-review-0.1.17/verification/WORKSPACE_SETUP/tests/test_workspace.py`, run serially against an isolated source copy; each test uses synthetic directories. Logs remain in the ignored `_tmp` development folder.
- Existing default/custom-name, local-link, relocation, audit, ownership and package-inventory checks use the renamed daily tools. The distribution-boundary test also verifies exclusion of a synthetic maintainer MANUAL_TESTS.md input.
- Synthetic fixtures only; no real development workspace, corporate repository, sign-in, global setting or Copilot session was changed.

## New-user guide review (0.1.17)

The generated README clarifies repository labels, the two refresh approvals, disabled/missing entries and backup coverage. DAILY_WORK.md explains local ticket folders, recording a starting Git commit before edits, the Python working directory and incomplete-transfer recovery. COPILOT_GUIDE.md defines orientation and skills, explains where to find customization controls and preserves separate discovery/loading checks. Contributor-only AGENTS.md is organized as short maintenance rules.

The three guide templates total **1467 words**, down from **1553** (about 6% shorter), counting headings, tables and commands. The design's operating boundaries, configuration schema and command behavior are unchanged. VS Code instruction/skill documentation was rechecked on 28 October 2026; references are linked in COPILOT_GUIDE.md.

Default and custom-name generation each passed 41 local file/section link checks, all six documented Python commands, validation, audit and explicit report saving, alongside the existing behavioral suite. These checks establish structural correctness, not first-use usability or actual Copilot loading. DOC-01 and the existing platform/Copilot checks remain pending; no manual result is inferred from automated checks. Existing workspaces retain their original generated guides.

## IDE configuration wording

Version 0.1.16 changes the generated root README table to describe ide_configs as holding saved workspaces and other IDE-specific configuration files. No setup, refresh or IDE discovery behavior changes. The packaged README, source hashes, archive checksum and fresh default/custom-name generation are checked for this release; manual test results remain unchanged.

## Daily guide filename

Version 0.1.15 deploys the AI working guide as DAILY_WORK.md from payload/root/DAILY_WORK.md. Its contents are byte-for-byte identical to the previous AI_README.md template. The development-root README.md, knowledge README.md and COPILOT_GUIDE.md retain their names; no redundant AI-root README alias is installed.

Root navigation, Copilot guide section links, the orientation's daily-guide link, setup completion text, runtime required-file inventory, release mappings and current design/setup references use the new name. Existing default/custom-layout tests now assert DAILY_WORK.md exists and the old AI-root README.md does not. All 93 behavioral tests pass on both interpreters listed above, including relocation and release checks.

Additional synthetic default and custom-name checks verified 41 local file/section links across the three guides and orientation, successful validate/audit, and refusal when DAILY_WORK.md is missing even if the old README name exists. Package/source hashes, archive checksum and synchronized design copies are checked for the new release. These checks do not certify IDE discovery or first-use readability; manual results remain unchanged.

Existing generated workspaces are not automatically renamed or upgraded. Their older tools and file inventories remain paired with the original filenames; the new name applies to fresh 0.1.15 installations.

## Shorter generated guides (0.1.14)

Version 0.1.14 changes documentation and release metadata only. The root README starts with setup and repository management; the AI working README covers the ticket lifecycle and daily commands; COPILOT_GUIDE.md covers context preparation, loading verification and fallback. Repeated explanations, optional extension suggestions and low-value implementation details were removed. Less common CLI options remain available through subcommand help and the design retains the full technical contracts.

| Generated guide | Previous words | Revised words |
|---|---|---|
| Root README | 1320 | 574 |
| AI working README | 791 | 527 |
| COPILOT_GUIDE.md | 840 | 450 |

Whitespace-delimited counts include headings, tables and commands: 2951 to 1551 words overall (about 47% shorter).

The edit follows [GitHub README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) and [Google technical-writing guidance](https://developers.google.com/style/paragraph-structure): put the common task first, use short paragraphs/action headings, and link to related details. Current VS Code instruction and skill documentation was checked on 25 October 2026; this is documentation verification, not IDE discovery evidence.

Synthetic default and custom-name installations passed validation. The three rendered templates in each layout had 31 valid local file/section links, with no unresolved configuration tokens. The existing 93 behavioral tests passed on each interpreter listed above; no prose-matching tests were added. Final archive/source hash checks and generated-guide checks cover the packaged files. The full framework skill resources, runtime mappings and Copilot orientation remain unchanged apart from the runtime package version.

First-use readability, actual IDE rendering and the existing Copilot/platform checks remain manual. DOC-01 was added to MANUAL_TESTS.md with pending status; no prior manual result was closed or reset. Existing generated workspaces are not automatically rewritten, because these guides have generated-file baselines.

## Public distribution review

Version 0.1.13 generalizes project origins, platform adoption and security requirements without changing the initialization boundary, configuration schema or daily operations. Historical manual observations retain their recorded results and limits; identifying paths, debug identifiers and private artifact names have been removed. Technical platform/interpreter versions remain as compatibility evidence.

Git ignore checks exclude local development fixtures, archived releases, machine metadata, caches and common credential files. A source scan found no remaining identifying origin details, non-placeholder home paths, email addresses or common credential signatures. The new archive contains only the explicit release inventory. These checks cover the current source and release; private development folders are outside the publication set. No Git history was available in the reviewed source folder.

## Consistent confirmation defaults

Start displays `[Y/n]` only for continuing from reviewed settings to the read-only preview; empty/whitespace input proceeds without creating files. The creation confirmation and both refresh write phases display `[y/N]`, with empty/whitespace input canceling. Missing-entry registration displays `[y/N/remove-missing]`; only the explicit keyword requests configuration cleanup. Short/full answers remain case-insensitive, invalid input repeats the prompt, and EOF cancels even at the yes-default question.

Behavioral coverage verifies read-only preview through Enter, creation cancellation through blank/no/EOF and successful explicit creation afterward. Refresh checks verify matching labels, blank cancellation of each write phase, preservation of already-approved registrations, and explicit missing-entry cleanup. No-change phases still skip prompts; the existing native launcher test covers final Enter retention and q/quit. Native Windows and physical GUI confirmation behavior remain manual checks in SETUP-01 and REFRESH-01.

## Framework skill namespace

All five packaged skills now use `ca-` in their directory names, frontmatter names and slash commands. Shared ticket-helper links, runtime loading/required-file inventory, release mappings, tests and current guides use the prefixed paths. No duplicate old-name aliases are installed. Future framework and framework-maintenance skills follow the same convention, documented in the design and the maintainer-only AGENTS.md. The release builder rejects unprefixed skill paths, and strict packaged-skill validation enforces the prefix; ordinary audit still accepts unrelated skill names.

A namespace regression test checks the exact five generated skill folders, matching metadata and local resources, rejection of an unprefixed framework skill without configuration writes, and successful read-only audit of an unrelated unprefixed skill. Existing relocated ticket lifecycle and release tests cover the renamed helper. Copilot discovery of the renamed commands remains a new manual check (SKILL-04); earlier results under the original names are preserved separately.

## Ticket prompt capture and lifecycle skills

The init skill extracts the supplied ID and task details, passes properly quoted literal text through `--description` and creates only the selected resources. A new brief records those details without inventing acceptance criteria or baselines. The new template field is resolved before inserting user content; braces, quotes, multiline and Unicode text are preserved. Older/custom templates without the field receive an appended details section. Existing briefs remain byte-for-byte intact, with an explicit result when supplied details were not applied. Blank details retain the original template behavior; invalid controls and archive/restore description arguments are refused before changes.

The new ca-jira-ticket-archive and ca-jira-ticket-restore skills invoke the existing sibling ticket helper. All five workflows are packaged, inventoried, link-checked and validated as explicit-invocation skills. No new Git/Jira/network integration or movement implementation is added. Five additional behavioral tests cover capture, repeat preservation, custom/unresolved templates, invalid options and both CLI entry points after custom-name relocation/installer removal, including unchanged archive/restore round trips.

## Readable diagnostic reports

Default validate/audit output and setup validation share the terminal formatter: a result and severity counts followed by nonempty Errors, Warnings, Manual checks and Notes sections. Editable user/local file changes are grouped with an explanation that intentional registration/context edits are normal. Paths remain complete; prose wraps to terminal width, with plain redirected/NO_COLOR/Windows output. Errors and warnings precede informational changes. Copilot loading remains explicitly uncertified.

Diagnostic-output behavioral tests exercise read-only text diagnostics, informational changes, error/warning ordering and exit status, JSON equivalence, saved audit report content/confirmation and narrow output with long Unicode paths. JSON report data and exit codes are unchanged; saved reports remain JSON. Noninteractive refresh/ticket and initializer output remain JSON.

## Daily tool filenames

Generated workspaces contain `tools/workspace_manager.py`, `tools/terminal_output_formatter.py` and `tools/vscode_workspace_updater.py`, deployed from matching source filenames. The initializer remains `scripts/workspace.py`. Both refresh launchers, dynamic helper loading, required-file inventory, package mappings, the ca-config-audit skill and documented daily commands use the new names. The diagnostic text layout is retained; ticket creation additionally supports initial prompt details. Existing installations retain their original filenames and are not automatically upgraded.

The relocation tests run validation, audit, refresh and ticket create/archive/restore without the installer, with default and customized directory names. The native macOS refresh-launcher test exercises the renamed command and formatting helper after relocation, including final quit handling. Windows launcher references are checked structurally; native Windows execution remains pending.

## Copilot orientation and onboarding

The package deploys a short, user-owned `.github/copilot-instructions.md` inside the configured AI Work root. It links to overview/reference-map documents, the active/archive ticket containers, configured repository groups, knowledge and daily commands. Relative links and encoded names support custom directory names and relocation. The orientation asks for relevant context and verified facts; it does not attach the whole framework or grant execution authorization.

The generated AI Work/COPILOT_GUIDE.md explains context preparation, Local discovery inspection, fresh-chat References/debug evidence, cross-root/mode checks, coexistence with repository instructions and explicit-attachment/direct-command fallback. The generated root README, DAILY_WORK.md and setup messages link users to it. Instruction support is environment/settings dependent, does not govern inline suggestions and is not certified by file presence.

Validation/audit require both files, check their local links and inventory ownership, and report orientation edits as informational user drift. Refresh preserves orientation edits. The pending-manual finding points to the generated guide and explicitly avoids certifying actual Copilot loading. No instruction setting, user/global instruction file or corporate clone is modified.

## Manual-test tracking

The development project has a separate tracker at `maintenance/MANUAL_TESTS.md`, relative to the project root and outside WORKSPACE_SETUP. It records stable IDs, priorities, separate macOS/Windows status, evidence requirements and a run template. Historical inspection of a debug export confirms orientation inclusion while a MAIN file is active; the full cross-root/mode discovery matrix remains incomplete. Earlier macOS testing reported successful original three-skill and small task/refresh/direct archive/restore checks. Exact IDE/Python versions and the wider matrix were not supplied, so these reports are scoped separately from the 0.1.10 init-capture/lifecycle checks and 0.1.11 prefixed-command discovery checks, which remain pending. This tracker is excluded from the release archive and generated development folders; it remains a maintainer aid across versions.

## Packaging and compatibility — released 0.1.17

The archive has **42 allowlisted source inputs**, their manifest and three enclosing README/setup-launcher copies: **46 files** under `Code-AI-Setup-0.1.17/`. Development folders generated from that release contain **29 daily files**. Source hashes and the separate SHA-256 sidecar are integrity checks; trusted delivery provides authenticity. Both design copies are synchronized. Configuration/manifest/state schemas remain 1; design version remains 1.0.

Existing generated workspaces are not automatically upgraded. New installations use a fresh absent destination. Previous release ZIPs/checksums are moved into the project's _old zips folder as release housekeeping, not by the installer/runtime.

## Remaining checks

Full automatic orientation coverage for fresh Local chats across MAIN/OTHER/DOCS and available Ask/Plan/Agent modes remains unverified, including custom names and relocation. First MAIN-request inclusion has direct debug evidence, and the original three-skill flow has reported success. Prompt capture and discovery/resource loading for the current six skills, including the unreleased refresh skill, need fresh manual checks. Use the generated COPILOT_GUIDE.md and explicit attachments where automatic loading is unavailable; do not bypass policy or change global settings automatically.

Native Windows interpreter discovery, paths/reparse handling, rendering/input and console closure remain untested. Finder associations/trust prompts and physical macOS window closure require user testing; q/quit exits the process and the existing Terminal profile controls its window. Actual IntelliJ/Eclipse integration remains manual. No organizational approval, OS sandbox or automatic instruction compliance is claimed.
