# Code AI Workspace

A portable toolkit for AI-assisted development across multiple independent Git repositories in VS Code, with shared project context and reusable GitHub Copilot workflows.

**Development status:** 0.1.19 pilot; native Windows and full Copilot/GUI verification remain pending. See [validation results](WORKSPACE_SETUP/VALIDATION_REPORT.md) and the [changelog](WORKSPACE_SETUP/CHANGELOG.md).

## What you get

- **One VS Code view** of your main projects, supporting repositories and company documentation.
- **Shared working files** for project context, ticket briefs, attachments and reusable knowledge.
- **Copilot skills** for ticket creation, review, archive/restore, framework checks and repository-list refresh. Daily use follows skills and prepared launchers; terminal commands are optional.

Setup and daily tools run offline using Python's standard library. Copilot itself requires its normal service access. Shared files and Python tools also work with other editors; generated IDE configuration is for VS Code.

## Before you start

Have **Python 3.9+** installed. For the intended workflow, also have Git, VS Code, GitHub Copilot and access to your repositories. Use approved software and accounts where required.

## Quick start

1. **Get the files.** Clone/download this repository, or extract a release ZIP. On Windows, use **Extract All**. Open the folder containing `Start macOS.command`, `Start Windows.cmd` and `WORKSPACE_SETUP/`.
2. **Create your development folder.** Double-click the Start file for your OS. Review [settings](WORKSPACE_SETUP/settings.json): Enter continues to the read-only preview `[Y/n]`; type `y`/`yes` to create `[y/N]` (Enter cancels). Setup creates and validates the new folder; type `q` to finish. To change settings, decline, edit `WORKSPACE_SETUP/settings.json` and relaunch.
3. **Add your repositories.** Inside the generated folder, clone/add repositories under `MAIN_PROJECT/`, `OTHER_PROJECTS/` or `COMPANY_DOCS/`. Ordinary documentation folders work too; unused groups can stay empty.
4. **Refresh before opening VS Code.** In the **generated development folder**, double-click `refresh_vscode_workspace macOS.command` or `refresh_vscode_workspace Windows.cmd`. Approve folder registration, then the VS Code folder-list update. Type `q` to finish. Use this launcher manually for initial setup.
5. **Open the workspace and complete Copilot setup.** Open `Code-AI/ide_configs/Code-AI.code-workspace` in VS Code. In the generated `AI_WORK/COPILOT_GUIDE.md`, prepare project context and verify instruction loading and a sample skill, using its documented fallback where needed. Then follow `AI_WORK/DAILY_WORK.md`. The [complete setup checklist](WORKSPACE_SETUP/SETUP_GUIDE.md#quick-setup) links each remaining step.

Paths above use the defaults. [Settings](WORKSPACE_SETUP/settings.json) can change the development folder's name/location, group names and VS Code filename; setup prints the actual paths. No manual Python commands are needed for these steps.

## Generated layout

```text
Code-AI/
├── MAIN_PROJECT/       # Main project repositories
├── OTHER_PROJECTS/     # Supporting/reference repositories
├── COMPANY_DOCS/       # Documentation repositories or folders
├── AI_WORK/            # Context, tickets, skills and daily guides
├── KNOWLEDGE_BASE/     # Reusable guides and assets
└── ide_configs/        # Saved VS Code workspace
```

Each repository keeps its own Git history. Setup creates no outer Git repository and does not clone repositories for you.

## Setup boundaries and portability

Setup writes only inside a **new** development folder and refuses existing destinations. Software installation, sign-in, global settings and backups remain manual.

By default, `Code-AI/` is created beside the Start files, inside the downloaded setup/repository folder. You can move or rename the entire generated folder afterward. **Move it out before deleting its enclosing setup folder.** Keep its internal names, refresh launchers, tools and hidden state files intact.

## Guides and help

Use the guides inside your generated folder for daily work. Repository links below open the source documentation; daily/Copilot guides are templates whose folder names are filled during setup.

| Guide | What it covers |
|---|---|
| [Setup guide](WORKSPACE_SETUP/SETUP_GUIDE.md) | Complete setup through Copilot verification, settings and troubleshooting |
| [Development folder guide template](WORKSPACE_SETUP/payload/root/README.md) | Folder map, repository registration, backup and removal |
| [Daily workflow template](WORKSPACE_SETUP/payload/root/DAILY_WORK.md) | Copilot skills, ticket workflow and optional Python reference |
| [Copilot guide template](WORKSPACE_SETUP/payload/root/COPILOT_GUIDE.md) | Context preparation, discovery checks and fallback |
| [Validation results](WORKSPACE_SETUP/VALIDATION_REPORT.md) | What was tested and what remains unverified |
| [Changelog](WORKSPACE_SETUP/CHANGELOG.md) | Released and unreleased changes |
| [Design](WORKSPACE_SETUP/DESIGN.md) | Architecture, behavior and constraints |

When reporting a problem, include your OS, Python version, framework version, steps and error output; include VS Code/Copilot versions for IDE issues. Omit credentials and private project data.

For framework contributions, start with the [design](WORKSPACE_SETUP/DESIGN.md) and [maintainer commands](WORKSPACE_SETUP/SETUP_GUIDE.md#maintainer-commands). Implementation and tests live in `WORKSPACE_SETUP/`; generated user workspaces are separate.
