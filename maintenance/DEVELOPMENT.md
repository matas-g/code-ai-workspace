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
| `WORKSPACE_SETUP/README.md` | Canonical user installation README; emitted once at the ZIP root with relocated links |
| `WORKSPACE_SETUP/SETUP_GUIDE.md`, `RELEASE_NOTES.md` | User setup/reference and concise compatibility/known-issue information |
| [DESIGN.md](DESIGN.md) | Single canonical architecture/current-contract document; no generated root copy |
| [BACKLOG.md](BACKLOG.md), [technical review](QUALITY_IMPROVEMENT_PLAN.md) | Current work order and detailed proposed changes |
| [MANUAL_TESTS.md](MANUAL_TESTS.md), [VALIDATION_REPORT.md](VALIDATION_REPORT.md) | Actual manual observations and automated/release evidence |
| [CHANGELOG.md](CHANGELOG.md) | Complete released/unreleased development history |

`WORKSPACE_SETUP/` is the source location, not an instruction to ship every file beneath it. The builder's explicit `INVENTORY` includes only required user-package inputs. `ENTRYPOINTS` adds the enclosing README and two Start launchers; their canonical source copies are omitted from the packaged inner folder. The package manifest covers initializer inputs, while the ZIP checksum covers the entire archive. Maintainer files remain in this repository.

Keep the two repository-root Start launchers byte-identical to their canonical sources under `WORKSPACE_SETUP/launchers/`. Update payload resources, runtime `LAYOUT`, release mappings and affected checks together. Framework skills use `ca-`; unrelated skills keep their own names.

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

Update concise user release notes without exposing development history as setup instructions. Keep unresolved user-relevant limitations visible. Full test evidence and changelog history stay here.

## Publish a requested release

After verifying a newer release, move the previous ZIP and `.sha256` sidecar into `_old zips/` without overwriting archived files. The builder does not archive or publish for you. Preserve the explicit allowlist; do not recursively package the source tree.

Users should download the prepared installation asset. GitHub's automatic source archives contain the repository, including development documentation. A release checksum detects changed bytes; authenticity depends on a trusted distribution source. State unverified platforms and manual scopes explicitly.
