#!/usr/bin/env python3
"""Review settings, preview, confirm, create and validate without subprocesses."""
import sys
sys.dont_write_bytecode = True
import argparse
import importlib.util
from pathlib import Path

PACKAGE = Path(__file__).absolute().parent.parent
SETTINGS_DECLINED = 4


# Load the same presentation helper deployed beside the daily runtime.
_console_spec = importlib.util.spec_from_file_location("workspace_console", PACKAGE / "scripts/terminal_output_formatter.py")
_console_module = importlib.util.module_from_spec(_console_spec)
_console_spec.loader.exec_module(_console_module)
Console = _console_module.Console


def load_workspace(package):
    path = package / "scripts/workspace.py"
    spec = importlib.util.spec_from_file_location("interactive_workspace", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.safe(path, package)
    return module


def confirm(input_fn=input, output=print, prompt="Create the development folder shown above? [y/N]: ", default=False):
    output("")
    while True:
        try:
            response = input_fn(prompt).strip().casefold()
        except EOFError:
            output("\nNo response received. Canceled; no development folder created.")
            return False
        if not response:
            response = "yes" if default else "no"
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            output("\nCanceled; no development folder created.")
            return False
        output("Please type y or n.")


def show_settings(config, path, target, console):
    c = console
    c.heading("[1/4] Settings review (read-only)")
    c.text("Editable configuration file")
    c.path(path)
    c.blank()
    c.text("To change values, decline below, edit this JSON file, save and launch setup again.")
    c.heading("Development folder destination")
    c.field("root_folder_name", config["root_folder_name"], "Name of the new development folder.")
    c.field("parent_directory", config["parent_directory"], "Existing parent directory for the new folder. A dot (.) means the launch directory; relative paths start there too. --target overrides both settings.")
    c.text("The new development folder will be created here:")
    c.path(target)
    c.field("vscode_workspace_name", config["vscode_workspace_name"], "Optional VS Code configuration filename, without .code-workspace. Default: Code-AI. Other IDE users may leave this unchanged.")
    c.heading("Folder names inside the development folder")
    descriptions = {
        "primary_repositories": "Repositories for the main project. This folder name does not set the VS Code filename.",
        "other_repositories": "Other approved development or reference repositories.",
        "company_documentation": "Approved company documentation repositories.",
        "ai_work": "Daily AI notes, tickets, local skills and small daily tools.",
        "knowledge": "Reusable reference documents with their local assets.",
    }
    for key, description in descriptions.items():
        c.field("directories." + key, config["directories"][key], description)
    c.heading("Repository inventory (optional)")
    c.text("repositories optionally lists planned folders. Setup does not clone anything or create repository child directories. After adding folders, use the generated refresh_vscode_workspace launcher to discover and register them.")
    c.blank()
    if not config["repositories"]:
        c.text("Current value: [] (no repositories configured).", "  ")
    for repo in config["repositories"]:
        c.text(repo["display_name"], "  * ")
        for key in ("id", "group", "directory", "access", "include_in_workspace"):
            c.text(key + " = " + str(repo[key]), "    ")
        c.blank()
    c.blank()
    for description in (
        "id: stable identifier; group: one of the three repository groups.",
        "directory: child folder; display_name: base VS Code label (MAIN/OTHER/DOCS prefix added automatically). Discovery initially uses the exact folder name.",
        "access: develop/reference intent, without enforced permissions.",
        "include_in_workspace: true/false; selected repositories appear after manual cloning and refresh of the VS Code helper file.",
    ):
        c.text(description, "  - ", "    ")
    c.heading("Fixed internal layout")
    c.text("Inside " + target.name + "/ (the new development folder):")
    c.text("ide_configs/ - generated IDE configuration files; currently a VS Code .code-workspace file.", "  - ", "    ")
    c.blank()
    c.text("Inside " + config["directories"]["ai_work"] + "/:")
    for path, description in (
        ("tools/", "daily framework commands"),
        (".framework/", "local setup records and optional reports"),
        (".github/copilot-instructions.md", "short Copilot orientation; verify actual loading"),
        ("COPILOT_GUIDE.md", "Copilot setup, discovery checks and fallback"),
        (".github/skills/", "local Copilot workflows"),
        ("project/", "project overview and reference links"),
        ("tickets/active/", "ongoing ticket work"),
        ("tickets/archive/", "completed ticket folders"),
    ):
        c.text(path + " - " + description + ".", "  - ", "    ")
    c.blank()
    c.text("These internal subfolder names are fixed and cannot be changed in settings.json. Two refresh_vscode_workspace launchers are created at the new development folder root.")
    c.blank()
    c.text("schema_version = 1: configuration format; leave it unchanged.")
    c.blank()
    c.text("Setup writes only inside the new folder. Software, accounts, repository clones, global settings and backup configuration remain manual.")


def run(package=PACKAGE, target=None, config_file=None, input_fn=input, output=print):
    w = load_workspace(package)
    c = Console(output)
    c.heading("Code AI Workspace " + w.VERSION)
    c.text("Python " + sys.version.split()[0])
    c.path(sys.executable)
    try:
        config, config_path = w.read_settings(package, config_file)
        target = w.resolve_target(config, target)
        if w.present(target):
            raise w.WorkspaceError("Target already exists; choose a new directory: " + str(target), 2)
        # Freeze effective settings before either confirmation. No settings reread during creation.
        show_settings(config, config_path, target, c)
        if not confirm(input_fn, output, "Use these settings and continue to the preview? [Y/n]: ", default=True):
            c.blank()
            c.text("Edit " + str(config_path) + " and launch setup again. Exiting setup now.")
            return SETTINGS_DECLINED
        c.heading("[2/4] Preview (read-only)")
        files, directories, pending = w.plan(package, target, config)
        manifest_hash = w.digest(w.file_bytes(package / "package-manifest.json", package))
        c.text("Destination:")
        c.path(target)
        c.heading("Folders (" + str(len(directories)) + ") - all inside " + target.name + "/")
        for path in directories:
            output("  + " + path + "/")
        c.heading("Files (" + str(len(files) + 1) + ") - all inside " + target.name + "/")
        for path in sorted(list(files) + [w.metadata(config, "installed-state.json")]):
            output("  + " + path)
        c.blank()
        c.text("Nothing has been created yet.")
        if not confirm(input_fn, output):
            return 0
        if w.digest(w.file_bytes(package / "package-manifest.json", package)) != manifest_hash:
            raise w.WorkspaceError("Package manifest changed after preview; rerun and review again.")
        c.heading("[3/4] Creating the development folder")
        result = w.initialize(package, target, config)
        c.text("Created " + str(result["files_created"]) + " files.", "  ")
        c.heading("[4/4] Validating the development folder")
        report, code = w.runtime.execute(argparse.Namespace(command="validate", format="text"), target / config["directories"]["ai_work"])
        w.runtime.show_report(report, output=output)
        if code:
            c.heading("Validation reported errors")
            c.text("Review the messages above; do not treat setup as complete.")
            return code
        c.heading("Initialization completed successfully", success=True)
        c.text("The new development folder is structurally valid and can be moved as a whole.")
        c.blank()
        c.text("VS Code users: open this generated file manually:")
        c.path(target / w.vscode_workspace_path(config))
        c.blank()
        c.text("Other IDE users: open/import repositories normally; the notes and Python tools work independently of VS Code. Keep the VS Code helper file because validation expects it.")
        c.blank()
        c.text("The installer is no longer needed. Daily commands are in " + config["directories"]["ai_work"] + "/DAILY_WORK.md.")
        c.text("Clone/add approved folders under the repository groups, then double-click the generated refresh_vscode_workspace launcher to preview registration and workspace updates.")
        c.text("Repository cloning, sign-in, Copilot discovery checks and backups remain manual.")
        c.text("For Copilot orientation and checks, read " + config["directories"]["ai_work"] + "/COPILOT_GUIDE.md. Loading across repository roots still needs manual verification.")
        return 0
    except (w.WorkspaceError, OSError, ValueError, TypeError, KeyError) as exc:
        c.heading("Setup stopped")
        c.text(str(exc), "  ")
        return getattr(exc, "code", 1)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", help="New absolute directory; overrides parent_directory/root_folder_name")
    parser.add_argument("--config", help="JSON settings; default is WORKSPACE_SETUP/settings.json")
    args = parser.parse_args(argv)
    try:
        if sys.version_info < (3, 9):
            print("Python 3.9+ is required. No software has been installed.")
            return 2
        return run(target=args.target, config_file=args.config)
    except KeyboardInterrupt:
        print("\nInterrupted. If creation had begun, inspect the retained target before retrying.")
        return 130
    except Exception as exc:
        print("\nSetup stopped: " + str(exc))
        return getattr(exc, "code", 1)


if __name__ == "__main__":
    raise SystemExit(main())
