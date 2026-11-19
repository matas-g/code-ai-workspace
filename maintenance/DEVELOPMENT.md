# Development and release guide

Run the commands below from the repository root using an installed approved Python compatible with the current package minimum. Setup and runtime code use only the standard library; do not install dependencies to run these checks.

## Source and document ownership

| Location | Purpose |
|---|---|
| `WORKSPACE_SETUP/scripts/workspace.py`, `start.py` | Initializer and interactive setup |
| `WORKSPACE_SETUP/scripts/workspace_manager.py` | Installed daily runtime and sole product `VERSION` owner |
| Formatter/JSONC helpers, launchers and `payload/` | User tools, generated guides, local skills and templates |
| `WORKSPACE_SETUP/scripts/build_release.py`, `tests/` | Repository build tool and behavioral tests; excluded from installation ZIPs |
| Repository `README.md` | Independent product/contributor entry point; never overwritten by the builder |
| `LICENSE`, `WORKSPACE_SETUP/LICENSE` | Keep the MIT notices byte-identical. The package copy ships in the ZIP and installs at `<ai_work>/tools/LICENSE`. |
| `WORKSPACE_SETUP/README.md` | Canonical user installation README; emitted once at the ZIP root with relocated links |
| [Setup guide](../WORKSPACE_SETUP/SETUP_GUIDE.md), [release notes](../WORKSPACE_SETUP/RELEASE_NOTES.md), [compatibility](../WORKSPACE_SETUP/COMPATIBILITY.md) | Installation procedures, dated user-visible changes, and current platform limits and workarounds |
| [DESIGN.md](DESIGN.md) | Single canonical architecture/current-contract document; no generated root copy |
| [Issue-specific design drafts](designs/issue-16-git-worktree-support.md) under `designs/issue-<number>-<topic>.md` | Proposed behavior and open decisions linked to an owning GitHub issue; not current product contracts or a separate status queue; excluded from user delivery |
| [BACKLOG.md](BACKLOG.md), [technical review](QUALITY_IMPROVEMENT_PLAN.md) | Legacy issue index/deferred ideas and detailed proposals; GitHub Issues owns imported status/priority |
| [MANUAL_TESTS.md](MANUAL_TESTS.md), [VALIDATION_REPORT.md](VALIDATION_REPORT.md) | Actual manual observations and automated/release evidence |
| [CHANGELOG.md](CHANGELOG.md) | Complete released/unreleased development history |
| [Test data ZIP](test_data.zip) | Complete sample repositories, Git histories and project context for manual testing; excluded from product releases |

`WORKSPACE_SETUP/` is the source location, not an instruction to ship every file beneath it. The builder's explicit `INVENTORY` includes only required user-package inputs. `ENTRYPOINTS` adds the enclosing README and two Start launchers; their canonical source copies are omitted from the packaged inner folder. The package manifest covers initializer inputs, while the ZIP checksum covers the entire archive. Maintainer files remain in this repository.

Keep the two repository-root Start launchers byte-identical to their canonical sources under `WORKSPACE_SETUP/launchers/`. Update payload resources, runtime `LAYOUT`, release mappings and affected checks together. Shipped framework skills use `ca-`; repository-only maintainer skills use `caw-`. Unrelated skills keep their own names.

## Maintainer skills

The five project-local skills in `.agents/skills/` support this repository's development process. They are excluded from installation ZIPs and generated workspaces by the release allowlist; a prefix alone is not an exclusion mechanism. See [AGENTS.md](../AGENTS.md#maintainer-skills-and-issue-workflows) for shared rules and skill links.

To explore the source, open a session at the repository root and enter `$caw-chat-onboarding` in Codex or `/caw-chat-onboarding` in GitHub Copilot CLI. Both invoke the same read-only skill.

| Codex invocation | Outcome |
|---|---|
| `$caw-chat-onboarding` | Read and understand the complete current project; no changes |
| `$caw-whats-next` | Summarize live open `next` issues briefly and recommend one |
| `$caw-issue-triage` | Review priorities/scope; apply issue and label changes when requested |
| `$caw-implement-issue` with an issue number/link | Implement one issue, verify it and update actual evidence |
| `$caw-do-release` with an optional version | Prepare, verify and package a release, archive the previous ZIP/checksum, commit and push |

For example, ask “Use caw-issue-triage to recommend the next few issues” for a read-only review, or explicitly request the label changes to apply. Use caw-implement-issue for the selected issue rather than automatically consuming the entire `next` queue. Required manual checks keep an issue open until observed; local changes awaiting integration are reported as such. Existing end-user `ca-` skills continue to operate on generated workspaces and local ticket files.

Run `$caw-do-release` for the usual release workflow below, including its commit and push to origin. With no version supplied, use the next patch version unless a newer unreleased product version is already prepared. Use the exact commit subject `Release v<version>`; issue references belong in the body. This workflow uses the tracked ZIP/checksum convention; tags and GitHub Release objects are created only when requested. Creating or editing the skill does not execute a release.

## Verify a change

Use synthetic fixtures and keep all transient output under `_tmp/`. For behavioral or packaging changes, prepare hashes and run the suite in an isolated copy:

```sh
mkdir -p _tmp
verification_dir="$(mktemp -d "$PWD/_tmp/check.XXXXXX")"
cp -R WORKSPACE_SETUP "$verification_dir/WORKSPACE_SETUP"
python3 -I -S -B "$verification_dir/WORKSPACE_SETUP/scripts/build_release.py"
python3 -I -S -B "$verification_dir/WORKSPACE_SETUP/tests/test_workspace.py"
```

The suite writes `.test-sandbox/` only inside that copy. Use the approved interpreter's absolute path when comparing supported versions. There is currently no configured lint command or CI workflow. Documentation-only changes need relevant link/path/command checks; broaden testing when behavior or packaging changes.

Record actual results in the validation report, including command, version/environment, outcome and remaining limits. Record native GUI/Copilot observations only in the manual tracker; automated tests do not close those checks. Preserve historical results and update the owning backlog item.

### Test write guard

`tests/test_workspace.py` installs a process-wide CPython audit hook. Only the main thread may enter or change `guard(...)`; nested scopes restore the previous scope, including after exceptions. Worker threads share the active scope. Run guarded cases serially and finish worker operations before leaving the scope. The separate initialization-race test runs without this guard.

The guard resolves ancestors before interpreting `..`, checks containment by path components, and checks write endpoints using the [CPython audit argument contracts](https://docs.python.org/3/library/audit_events.html). Symlink creation checks the new link's location; rename/unlink check directory entries rather than following their final symlink. Metadata operations conservatively follow the final link because their events omit `follow_symlinks`.

Relative `dir_fd` mutations and descriptor-only mutations are refused when their destinations cannot be established portably. Absolute paths with `dir_fd` remain supported. Since the `open` event omits `dir_fd`, each scope also wraps `os.open` to reject relative descriptor-based writes before the call.

This is test instrumentation, not an OS sandbox. It covers the enumerated audit events and current `os.open` attribute, not native calls, previously captured `os.open` aliases, unaudited writes through existing handles, existing hard-link aliases, or concurrent filesystem replacement races. Subprocess tests run separately outside the guard. Keep production path checks and independent external sentinels; passing this guard does not prove absence of all OS-level effects. `AuditGuardTests` retains synthetic reproductions and real negative operations with sentinels outside the permitted scope.

## Prepare package inputs

Edit the product version only at `VERSION` in `WORKSPACE_SETUP/scripts/workspace_manager.py`. Change `DESIGN_VERSION` only for a design-version change. Record changelog entries and actual verification explicitly; never relabel historical evidence.

```sh
python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py
```

This prepares the user README's package-version label and the source manifest hashes inside `WORKSPACE_SETUP/`. It mutates those files and is not a read-only integrity check. Review the prepared diff. Preparation never rewrites the repository README, design or other maintenance documents. The old `--sync-project-docs` option has been removed with document mirroring; historical commands remain evidence for their original versions.

The builder and tests remain available in the checkout; end users do not need them in the installation ZIP. Refreshing hashes is deliberate release preparation, not a workaround for unexplained drift.

## Build and check an installation ZIP

```sh
python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py --output-dir ABSOLUTE_RELEASE_DIRECTORY
```

Use an existing absolute directory. The default name is `code-ai-workspace-<version>-macos-pilot.zip`; `--output ABSOLUTE_NEW_ZIP` accepts a custom filename. Existing ZIP/checksum destinations are refused. For development verification, use a directory under `_tmp/` and do not replace the published artifact.

The archive contains one enclosing `Code-AI-Setup-<version>/` folder: a user README, two Start launchers and the allowlisted `WORKSPACE_SETUP/` inputs. It excludes maintenance documents, project-local skills, the test suite, release builder, the installer source's development `.gitignore` and redundant entrypoint source copies. The separate generated-workspace ignore template remains in the daily payload. No contributor document is needed to initialize it.

Before release, verify member paths, hashes, executable metadata, checksum and user-document links. Extract the exact candidate and exercise default/custom-name setup, validation, refresh and ticket operations. Move the complete generated tree, remove the extracted installer and repeat daily commands from another working directory. Check that generated file inventory remains the intended daily-only set.

Add a dated entry to the release notes for shipped user-visible changes, newest first. Review the compatibility page against recorded platform checks and update affected workarounds. Verify that the extracted README links to both pages and that they link to each other. Keep installation procedures in the setup guide and detailed test evidence in the validation report.

## Publish a requested release

After verifying a newer release, move the previous ZIP and `.sha256` sidecar into `_old zips/` without overwriting archived files. The builder does not archive or publish for you. Preserve the explicit allowlist; do not recursively package the source tree.

Users should download the prepared installation asset. GitHub's automatic source archives contain the repository, including development documentation. A release checksum detects changed bytes; authenticity depends on a trusted distribution source. State unverified platforms and manual scopes explicitly.
