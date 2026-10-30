# Code AI Workspace — contributor instructions

## Project orientation

This repository builds a portable toolkit for multi-repository development with shared context, local ticket files and Copilot workflows. Setup and daily tools use Python's standard library and run offline. Generated IDE configuration targets VS Code; other editors use the shared files and tools manually.

The disposable `WORKSPACE_SETUP/` package creates a separate development folder. Installed daily tools must work after the installer is removed and the complete generated folder is moved or renamed. There is no automatic upgrade of existing workspaces.

## Where to look

Read the files relevant to the requested task; a small edit does not require full onboarding.

| Location | Purpose |
|---|---|
| [README.md](README.md), [setup guide](WORKSPACE_SETUP/SETUP_GUIDE.md) | Product overview, setup, settings and maintainer commands |
| `WORKSPACE_SETUP/scripts/` | `workspace.py`: initializer; `start.py`: interactive setup; `workspace_manager.py`: installed runtime; formatter/JSONC helpers; `build_release.py`: release preparation |
| `WORKSPACE_SETUP/payload/` | Generated guides, context/knowledge examples, Copilot instructions, skills and ticket helper/templates |
| `WORKSPACE_SETUP/settings.json`, `configuration-examples/`, `launchers/` | Setup inputs, example configurations and canonical launcher sources, all under `WORKSPACE_SETUP/` |
| `WORKSPACE_SETUP/tests/test_workspace.py` | Synthetic behavioral suite |
| [DESIGN.md](WORKSPACE_SETUP/DESIGN.md) | Architecture and intended contracts; `WORKSPACE_DESIGN.md` is its generated root mirror |
| [maintenance/BACKLOG.md](maintenance/BACKLOG.md) | Single current implementation order, dependencies, status and completion gates |
| [maintenance/QUALITY_IMPROVEMENT_PLAN.md](maintenance/QUALITY_IMPROVEMENT_PLAN.md) | Detailed technical proposals and known-defect criteria; proposals are not implemented behavior |
| [maintenance/MANUAL_TESTS.md](maintenance/MANUAL_TESTS.md), [validation report](WORKSPACE_SETUP/VALIDATION_REPORT.md) | Actual manual observations and versioned automated/release evidence respectively |

For a requested full project read, use `$ca-code-ai-onboarding` at [.agents/skills/ca-code-ai-onboarding/SKILL.md](.agents/skills/ca-code-ai-onboarding/SKILL.md). It excludes `_old zips/`, `_tmp/` and ZIP archives. Those locations are historical artifacts or scratch work, not current implementation sources.

## Change constraints

- Preserve new-directory-only initialization: refuse existing targets, write only within the new target and retain incomplete results for inspection. Setup must not install software, authenticate, clone repositories or change global settings. Keep Python setup/runtime tools free of network and subprocess requirements.
- Derive generated names and relative paths from effective configuration. Keep installed tools independent of source-package files and the terminal's working directory.
- When changing deployed files or skill paths, align payload resources, runtime `LAYOUT`, release `INVENTORY`/mappings, guides and affected tests. Root Start launchers must match their canonical `WORKSPACE_SETUP/launchers/` copies.
- Use `ca-` for every framework or framework-maintenance skill. Keep folder names, `SKILL.md` names, invocation examples and resource links aligned. Leave unrelated third-party and repository-owned skills unchanged.
- Put temporary development files and synthetic test output in `_tmp/`. Preserve existing working/staged changes. Keep this file, project-local maintainer skills, planning documents and manual-test tracker outside release ZIPs and generated workspaces.

## Verification

Use an installed Python compatible with the package's current minimum, with `-I -S -B`. No dependency installation is needed. For setup usage and read-only preview commands, follow the [setup guide](WORKSPACE_SETUP/SETUP_GUIDE.md#manual-command-alternative).

For behavioral changes, add or update focused regression coverage and run the suite from an isolated package copy. From the repository root, the following keeps fixture writes and hash preparation under `_tmp/`:

```sh
mkdir -p _tmp
check_dir="$(mktemp -d "$PWD/_tmp/check.XXXXXX")"
cp -R WORKSPACE_SETUP "$check_dir/WORKSPACE_SETUP"
python3 -I -S -B "$check_dir/WORKSPACE_SETUP/scripts/build_release.py"
python3 -I -S -B "$check_dir/WORKSPACE_SETUP/tests/test_workspace.py"
```

The builder prepares hashes in the disposable copy; the suite creates `.test-sandbox/` there. For documentation-only changes, check affected links, paths and commands; run broader tests when behavior or packaging is affected. There is currently no configured lint command or CI workflow.

Record actual manual results in `maintenance/MANUAL_TESTS.md` and automated/release evidence in `WORKSPACE_SETUP/VALIDATION_REPORT.md`, scoped to the tested version and environment. Automated checks cannot prove IDE skill discovery, Copilot behavior or native GUI compatibility. Preserve historical results and report remaining checks explicitly. Update the owning backlog item when implementing planned work; a passing suite alone does not close its manual gates.

## Release maintenance

- Change the product version only at `VERSION` in `WORKSPACE_SETUP/scripts/workspace_manager.py`; change `DESIGN_VERSION` only for a design-version change.
- Prepare release labels, hashes and root README/design copies with `python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py --sync-project-docs`. Edit canonical package documents rather than their root mirrors. Preparation mutates files; it is not a read-only integrity check.
- Build a requested release with that command plus `--output-dir ABSOLUTE_RELEASE_DIRECTORY` for an automatically versioned ZIP filename. Use an existing directory; the builder refuses existing ZIP/checksum destinations.
- When replacing a release, move the previous ZIP and its `.sha256` checksum into `_old zips/` without overwriting archived files. Keep the release inventory allowlisted.
- Record the changelog and actual verification evidence explicitly. Never replace historical version numbers automatically or present a proposed fix as completed.
