# Code AI Workspace

A portable toolkit for development across independent Git repositories, with shared project context, local ticket files and optional GitHub Copilot workflows.

- Open your main, supporting and documentation repositories together in VS Code.
- Keep ticket briefs, attachments, project context and reusable knowledge alongside them.
- Use local skills and Python commands for ticket creation, review, archive/restore, validation and repository-list refresh.

Setup and daily tools run offline using Python's standard library. Copilot uses its normal service access. Shared files/tools also work with other editors; generated IDE configuration targets VS Code.

**Status:** macOS pilot. See [compatibility and known limitations](WORKSPACE_SETUP/RELEASE_NOTES.md) before relying on the toolkit. Detailed test evidence belongs in the [maintainer validation report](maintenance/VALIDATION_REPORT.md).

## Use the toolkit

For installation, use the prepared **installation ZIP** from the release assets, extract it and follow its README. GitHub's automatic **Source code (zip)** is a repository copy with development files.

You can also run setup from this checkout. Have Python 3.9+, Git and VS Code/Copilot available for the intended workflow, then:

1. Double-click `Start macOS.command` or `Start Windows.cmd`. Review settings, continue to the read-only preview with Enter, and type `y` to create a new development folder.
2. In that generated folder, add repositories under the configured groups and run its refresh_vscode_workspace launcher before opening the saved VS Code workspace.
3. Follow the generated `AI_WORK/COPILOT_GUIDE.md` and `AI_WORK/DAILY_WORK.md`, using your configured AI Work name if changed.

The [setup guide](WORKSPACE_SETUP/SETUP_GUIDE.md#quick-setup) covers the complete workflow, settings, direct commands and troubleshooting. The [installation README source](WORKSPACE_SETUP/README.md) is written for end users; this repository README has its own contributor navigation.

Each repository retains its own Git history. Setup creates a separate new development folder, refuses existing targets and does not install software, authenticate, clone repositories or change global settings. Move the complete generated folder out before deleting its enclosing installer folder.

## Develop the toolkit

| Document | Purpose |
|---|---|
| [Contributor instructions](AGENTS.md) | Change constraints and verification rules |
| [Development and release guide](maintenance/DEVELOPMENT.md) | Source map, tests, package preparation and release commands |
| [Design](maintenance/DESIGN.md) | Canonical architecture and current contracts |
| [Backlog](maintenance/BACKLOG.md) | Single prioritized implementation order and completion gates |
| [Technical review](maintenance/QUALITY_IMPROVEMENT_PLAN.md) | Detailed proposals and known-defect criteria |
| [Manual tests](maintenance/MANUAL_TESTS.md) | Actual environment-specific observations and remaining checks |
| [Validation report](maintenance/VALIDATION_REPORT.md) | Versioned automated/release evidence |
| [Changelog](maintenance/CHANGELOG.md) | Released and unreleased development history |

`WORKSPACE_SETUP/` holds installer/runtime sources and the user payload. Tests and the release builder remain there as repository tools, excluded by the release allowlist. `maintenance/` and project-local `.agents/` skills are repository-only. Temporary development output belongs in `_tmp/`.

When reporting a problem, include the package version, OS, Python version, reproduction and error output; include VS Code/Copilot versions for IDE behavior. Omit credentials and private project data.
