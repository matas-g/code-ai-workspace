# Code AI Workspace

A portable toolkit for working across independent Git repositories in VS Code, with shared project context, local tickets and optional GitHub Copilot workflows.

**Package version:** 0.1.20

**Status:** macOS pilot. Read the [compatibility and known limitations](RELEASE_NOTES.md) before relying on the workflow.

## Before you start

Have **Python 3.9+** installed. For the VS Code/Copilot workflow, also have Git, VS Code, GitHub Copilot and access to your repositories. Use approved software and accounts where required. Setup installs nothing and changes no global settings.

## Quick start

1. **Extract the installation ZIP.** On Windows, use **Extract All**. Open the folder containing this README, `Start macOS.command`, `Start Windows.cmd` and `WORKSPACE_SETUP/`.
2. **Create your development folder.** Double-click the Start file for your OS. Review [settings](settings.json), press Enter for the read-only preview `[Y/n]`, then type `y` to create `[y/N]` (Enter cancels). Setup validates the result; type `q` to finish. To change settings, decline, edit `WORKSPACE_SETUP/settings.json` and relaunch.
3. **Add repositories.** In the generated development folder, clone/add your repositories under `MAIN_PROJECT/`, `OTHER_PROJECTS/` or `COMPANY_DOCS/`. Ordinary documentation folders work too; unused groups can stay empty.
4. **Refresh before opening VS Code.** Double-click the generated folder's `refresh_vscode_workspace macOS.command` or `refresh_vscode_workspace Windows.cmd`. Approve registration, then the folder-list update; type `q` to finish.
5. **Open and prepare your workspace.** Open the generated `ide_configs/Code-AI.code-workspace`. Follow the generated `AI_WORK/COPILOT_GUIDE.md` for context and Copilot checks, then `AI_WORK/DAILY_WORK.md` for your first task. Direct Python commands remain available without Copilot.

Paths above use default names. Settings can change the development folder's location/name, repository groups, AI Work name and VS Code filename. Setup prints the actual paths. Follow the [complete setup guide](SETUP_GUIDE.md#quick-setup) for settings, verification and troubleshooting.

## Your generated development folder

```text
Code-AI/
├── MAIN_PROJECT/       # Main repositories
├── OTHER_PROJECTS/     # Supporting repositories
├── COMPANY_DOCS/       # Documentation repositories/folders
├── AI_WORK/            # Context, tickets, skills, tools and guides
├── KNOWLEDGE_BASE/     # Reusable guides and assets
└── ide_configs/        # Saved VS Code workspace
```

Each repository keeps its own Git history. Setup creates no outer Git repository and does not clone repositories for you.

## After setup

Use these guides inside your generated folder:

| Guide | What it covers |
|---|---|
| Root `README.md` | Folder management, repository refresh, portability, backup and recovery |
| `AI_WORK/DAILY_WORK.md` | Tickets, review, audit and optional Python commands |
| `AI_WORK/COPILOT_GUIDE.md` | Context preparation, instruction/skill discovery and fallback |
| `KNOWLEDGE_BASE/README.md` | Reusable notes and assets |

These names follow your settings. The guides and tools work independently of the installer.

By default, the development folder is created inside the extracted setup folder. **Move the complete generated folder out before deleting that enclosing folder.** Keep its internal names, refresh launchers, tools and hidden state intact. Software installation, sign-in and backup configuration remain manual.

For setup problems, see [troubleshooting](SETUP_GUIDE.md#troubleshooting-and-verification-limits). Include your package version, OS, Python version, steps and error output when reporting a problem; include VS Code/Copilot versions for IDE issues. Omit credentials and private project data.
