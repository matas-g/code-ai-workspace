# Setup guide

Follow the quick setup from a **new** development folder through a working Copilot check. Settings and troubleshooting follow below; the [README](../README.md) explains the project and default layout.

## Quick setup

1. **Prepare.** Check the [prerequisites](#prerequisites), then extract the ZIP (Windows: **Extract All**) or download/clone the source. Open the folder containing the Start files and `WORKSPACE_SETUP/`.
2. **Create.** Double-click the Start file for your OS. Review settings, press Enter for the read-only preview `[Y/n]`, then type `y` to create `[y/N]`. Setup validates the result; type `q` to finish. To change settings, decline, edit `WORKSPACE_SETUP/settings.json` and relaunch.
3. **Populate.** Manually clone/add repositories or documentation folders under the generated repository groups. Unused groups can stay empty. Use approved URLs/accounts; Git authentication may create state outside this folder.
4. **Refresh.** In the generated development folder, double-click its refresh_vscode_workspace launcher. Approve registration, then the VS Code folder-list update; type `q` to finish.
5. **Open.** Open the saved `.code-workspace` file at the printed path and review any trust prompt. Confirm AI Work, Knowledge and your enabled repositories are visible.
6. **Prepare Copilot and project context.** In your generated AI Work folder, open `COPILOT_GUIDE.md` → **Prepare once**: sign in, select Local, populate `project/overview.md` and `project/reference-map.md` from verified sources, and review the generated orientation. Editing the orientation is optional.
7. **Verify the workflow.** In the same generated guide, follow **Verify your setup** to check context loading and run a small sample ticket/audit. Resolve errors or verify the documented fallback for unavailable features before relying on them.
8. **Start daily work.** Open the generated `DAILY_WORK.md` → **Work on a ticket** for your first task, including requirements, starting Git commits, testing and review.

Steps 6–8 use the guides in your **generated AI Work folder**; its name follows `directories.ai_work`. Open those generated files after creation, where links and folder names match your settings. For use without Copilot, skip 6–7 and use the daily guide's optional Python reference.

The release has one enclosing `Code-AI-Setup-<version>/` folder; an extractor may add another outer folder. By default, setup creates `Code-AI/` beside the Start files, **inside the setup folder**. Move the generated folder out before deleting that enclosing folder, or choose another parent below.

## Prerequisites

For the VS Code/Copilot workflow, have Python 3.9+, Git and VS Code installed, with GitHub Copilot available in VS Code. Use approved software/accounts and ensure access to the repositories and reference sources you need. Installation, sign-in and access requests remain manual; setup installs nothing and changes no global settings. For other editors, see [Using another IDE](#using-another-ide).

## Settings (optional)

Edit [settings.json](settings.json) before creation. It is deliberately editable without rebuilding the manifest; other package inputs remain hash checked. [renamed.json](configuration-examples/renamed.json) shows a complete alternative configuration.

| Setting | Meaning |
|---|---|
| `root_folder_name` | New development folder name; default `Code-AI` |
| `parent_directory` | Existing parent; default `"."` means the launch directory |
| `directories.primary_repositories` | Main repository group |
| `directories.other_repositories` | Supporting/reference repository group |
| `directories.company_documentation` | Documentation repository/folder group |
| `directories.ai_work` | Context, tickets, skills, tools and local setup records |
| `directories.knowledge` | Reusable guides and assets |
| `repositories` | Optional planned inventory; default `[]`. Setup neither clones repositories nor creates their child folders |
| `vscode_workspace_name` | Saved VS Code filename stem; default `Code-AI`, independent of repository groups. Omit `.code-workspace` |
| `schema_version` | Configuration format; leave at `1` |

Use letters, digits, spaces, `_` and `-` for major names, starting with a letter/digit (1–64 characters). Names must be distinct within their scope and cannot be reserved Windows names. Repository child names also allow dots and Unicode, up to 255 characters; separators, controls, surrounding whitespace and trailing dots are refused. Unknown/duplicate JSON keys and invalid types are errors.

Each supplied `repositories` entry needs a unique lowercase `id`, a `group` matching one of the three repository-group keys, a child `directory`, `display_name`, `access` (`develop` or `reference`) and boolean `include_in_workspace`. Display names omit the automatically added `MAIN ·`, `OTHER ·` or `DOCS ·` prefix. Access describes intent only. Most users can leave the inventory empty and let refresh register folders after cloning.

### Locations and names

`parent_directory` must already exist. Use a native local path: absolute paths select another location; relative paths start at the launcher directory (the current working directory for direct Python use), **not** the configuration file's directory. Setup never creates missing parents or expands `~`/environment variables. Symlinked/redirected parents and Windows UNC paths are refused.

Example values, edited into the existing JSON:

```json
"parent_directory": "/Users/yourname/Projects"
```

Windows JSON requires doubled backslashes:

```json
"parent_directory": "C:\\Users\\yourname\\Projects"
```

The result is a new `root_folder_name` child. In command examples, `<ai_work>` means `directories.ai_work`; `<root_folder_name>` and `<vscode_workspace_name>` mean their corresponding settings. Setup prints actual paths, and generated guides use your chosen names. `WORKSPACE_SETUP`, `settings.json`, `ide_configs/`, `tools/` and other internal paths are fixed.

Settings are frozen before confirmation; changes made during the run require a relaunch. Existing destinations are always refused, even empty ones.

### Confirmation and terminal behavior

The capitalized choice is the Enter default: `[Y/n]` continues to preview; `[y/N]` cancels creation or refresh writes. Short/full answers are accepted, invalid input repeats the prompt, and EOF always cancels. Refresh offers `remove-missing` explicitly when missing registrations exist; see the generated root README for those choices.

Declining settings exits before preview. Success, preview cancellation and errors retain launcher output until `q`/`quit` or manual closure; blank/unknown input keeps it visible and cannot execute commands. Quitting does not change the displayed operation result. On macOS, the existing [Terminal profile](https://support.apple.com/guide/terminal/trmlshll/mac) controls whether the finished window closes physically; setup never changes it.

## After setup

After creation, use the **generated guides**, which remain usable after deleting the installer:

- Root `README.md`: folder map, repository registration/refresh, portability, backup and removal.
- `<ai_work>/DAILY_WORK.md`: tickets, review, framework checks and optional Python commands.
- `<ai_work>/COPILOT_GUIDE.md`: context preparation, instruction/skill discovery and fallback.
- `<knowledge>/README.md`: reusable notes, sources and assets.

No daily command depends on `WORKSPACE_SETUP`. Keep a trusted release separately for future fresh initialization. VS Code may create its own session state outside the development folder.

### Optional follow-up

- **Protect your work:** Before keeping irreplaceable notes or unpublished changes, choose permitted storage with recoverable history and test a restore. Follow **Move, back up or remove this folder** in the generated root `README.md`; setup configures no synchronization.
- **Share repository instructions:** Adapt the [example](payload/examples/copilot-instructions.md) through the owning repository's normal review if useful to the team.

### Using another IDE

Open/import repositories normally in IntelliJ, Eclipse or your preferred editor. Shared notes and Python tools work independently of VS Code. Setup generates no native projects for other IDEs; test their Copilot features separately. Keep the unused `.code-workspace` file because framework validation checks it. Refresh, display labels and `include_in_workspace` affect that file only.

## Manual command alternative

Run from the directory containing the Start files and `WORKSPACE_SETUP/`. Use your approved interpreter's full path if needed. On macOS:

```sh
python3 -I -S -B WORKSPACE_SETUP/scripts/start.py
```

On Windows PowerShell, replace the example executable path:

```powershell
& 'C:\Path\To\python.exe' -I -S -B WORKSPACE_SETUP/scripts/start.py
```

`--config FILE` selects another JSON file. `--target ABSOLUTE_NEW_PATH` overrides both the configured location and root name. Relative locations use the terminal's current directory; clickable launchers first change to their own directory.

For noninteractive use, run these separately with the same optional flags; inspect the plan before creation:

```sh
python3 -I -S -B WORKSPACE_SETUP/scripts/workspace.py plan
python3 -I -S -B WORKSPACE_SETUP/scripts/workspace.py init --apply
```

Then, from the **generated development root**, replace `<ai_work>` with your configured folder name and validate:

```sh
python3 -I -S -B "<ai_work>/tools/workspace_manager.py" validate
```

The clickable flow validates automatically. Direct commands exit normally and do not retain the terminal. Daily command examples, JSON output and report options belong in the generated DAILY_WORK.md and subcommand `--help`.

## Troubleshooting and verification limits

| Problem | Next step |
|---|---|
| Existing target or incomplete initialization | Inspect retained files; choose a new absent destination. Never initialize over an existing tree or remove partial work blindly |
| Missing parent or invalid names/configuration | Use an existing native parent; correct JSON, collisions or unsupported names, then relaunch |
| Missing Python or blocked launcher | Use an installed approved Python 3.9+ directly, or follow your software/admin procedure. Nothing is downloaded and no policy is bypassed |
| OS trust, proxy or certificate restriction | Follow the applicable administrator procedure. Setup changes no trust stores, execution policies or other protections |
| Permission or path-length failure | Review the reported path, choose an accessible/shorter location if appropriate and inspect any partial target. Setup does not elevate access or change system limits |
| Missing repositories or unexpected VS Code roots | Check group folders and refresh using the generated root README. Restore missing group directories first |
| Missing/damaged framework files | Use the generated daily guide's audit workflow; inspect findings before restoring from a trusted source/backup. No automatic repair or upgrade is provided |
| Copilot instructions, skills or approved model unavailable | Follow the generated Copilot guide; attach context or use direct commands where permitted. Do not bypass account or organizational restrictions |

Validation checks structure, local links and changes since setup. It does not certify security approval, Copilot loading or IDE behavior. Read [compatibility and known limitations](RELEASE_NOTES.md) for the current user-facing limits, including native Windows/GUI/Copilot checks still pending. Existing generated trees retain their original tools and guides; for a new release or changed internal names, initialize a fresh destination and transfer approved content manually.
