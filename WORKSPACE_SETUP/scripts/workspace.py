#!/usr/bin/env python3
"""Offline initializer. Daily tools are deployed separately and need no installer."""
import sys
sys.dont_write_bytecode = True
import argparse
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
from urllib.parse import quote

PACKAGE = Path(__file__).absolute().parent.parent
spec = importlib.util.spec_from_file_location("workspace_runtime", PACKAGE / "scripts/workspace_manager.py")
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)
# Share reviewed primitives; installed runtime never imports this initializer.
for _name in (
    "VERSION", "DESIGN_VERSION", "DEFAULT_ROOT_FOLDER_NAME", "DEFAULTS", "FIXED", "MARKER", "RESERVED", "TOKEN",
    "WorkspaceError", "present", "safe", "relative", "below", "file_bytes", "digest", "json_bytes",
    "load_json", "keys", "validate_config", "folder_map", "mapping_path", "workspace_bytes",
    "exclusive", "atomic_update", "validate_root", "installed", "audit_root", "refresh", "metadata", "expected_files", "vscode_workspace_path",
):
    globals()[_name] = getattr(runtime, _name)


def read_settings(package, config_file=None):
    path = Path(config_file).absolute() if config_file else package / "settings.json"
    return validate_config(load_json(path)), path

def resolve_target(config, override=None, cwd=None):
    """Location is setup-only; relative locations are anchored to the launch working directory."""
    if override is not None:
        return safe(Path(override))
    location = config["parent_directory"]
    if (os.name != "nt" and (re.match(r"^[A-Za-z]:", location) or "\\" in location)) or (os.name == "nt" and location.startswith("/")):
        raise WorkspaceError("parent_directory uses path syntax for another operating system.", 2)
    if location.startswith("~") or "$" in location or "%" in location:
        raise WorkspaceError("Use a literal parent_directory path, without ~ or environment variables.", 2)
    parent = Path(location)
    if os.name == "nt" and (parent.drive or parent.root) and not parent.is_absolute():
        raise WorkspaceError("Use an absolute Windows parent_directory with its drive, or a plain relative path.", 2)
    if not parent.is_absolute():
        parent = Path(cwd or Path.cwd()) / parent
    parent = safe(Path(os.path.abspath(parent)))
    if not parent.is_dir():
        raise WorkspaceError("parent_directory parent must already exist: " + str(parent), 2)
    return safe(parent / config["root_folder_name"])


def load_manifest(package):
    manifest = load_json(package / "package-manifest.json", package)
    keys(manifest, ("schema_version", "package_version", "design_version", "minimum_python", "files", "directories"),
         ("schema_version", "package_version", "design_version", "minimum_python", "files", "directories"))
    if type(manifest["schema_version"]) is not int or manifest["schema_version"] != 1 or manifest["package_version"] != VERSION or manifest["design_version"] != DESIGN_VERSION:
        raise WorkspaceError("Unsupported package manifest/version.", 2)
    if manifest["minimum_python"] != "3.9" or not isinstance(manifest["files"], list) or not isinstance(manifest["directories"], list):
        raise WorkspaceError("Invalid package manifest schema.", 2)
    seen = set()
    for entry in manifest["files"]:
        keys(entry, ("source", "sha256", "destinations", "mutable"), ("source", "sha256", "destinations"))
        source = str(relative(entry["source"]))
        if source.casefold() in seen or source == "package-manifest.json":
            raise WorkspaceError("Duplicate or self-referential manifest source.", 2)
        seen.add(source.casefold())
        if not isinstance(entry["sha256"], str) or not re.fullmatch("[0-9a-f]{64}", entry["sha256"]):
            raise WorkspaceError("Invalid package file hash.", 2)
        data = file_bytes(below(package, source), package)
        if entry.get("mutable", False) and source != "settings.json":
            raise WorkspaceError("Only settings.json may be mutable.", 2)
        if type(entry.get("mutable", False)) is not bool:
            raise WorkspaceError("Invalid mutable flag.", 2)
        if not entry.get("mutable", False) and digest(data) != entry["sha256"]:
            raise WorkspaceError("Package integrity mismatch: " + source)
        if not isinstance(entry["destinations"], list):
            raise WorkspaceError("Invalid manifest destinations.", 2)
        for dest in entry["destinations"]:
            keys(dest, ("directory_id", "relative_path", "render", "owner"), ("directory_id", "relative_path", "render", "owner"))
            if dest["directory_id"] not in set(DEFAULTS) | set(FIXED) or dest["render"] not in ("copy", "markdown") or dest["owner"] not in ("framework", "generated", "user"):
                raise WorkspaceError("Unsupported manifest mapping.", 2)
            relative(dest["relative_path"])
    return manifest


def plan(package, target, config):
    target = safe(Path(target))
    if present(target):
        raise WorkspaceError("Target already exists; choose a new directory: " + str(target), 2)
    if not target.parent.is_dir():
        raise WorkspaceError("Target parent must already exist.", 2)
    if target == Path.home() or target == Path(target.anchor):
        raise WorkspaceError("Unsafe target directory.", 2)
    name = target.name
    if name.endswith((" ", ".")) or re.search(r'[<>:"|?*\x00-\x1f]', name) or RESERVED.fullmatch(name.split(".")[0]):
        raise WorkspaceError("Target basename is not portable.", 2)
    manifest = load_manifest(package)
    mapping = folder_map(config)
    tokens = dict(config["directories"])
    tokens.update({k + "_link": quote(v, safe="/") for k, v in config["directories"].items()})
    tokens["vscode_workspace_name"] = config["vscode_workspace_name"]
    tokens["vscode_workspace_name_link"] = quote(config["vscode_workspace_name"], safe="")
    output = {}
    names = set()
    def add(path, data, owner):
        below(target, path)
        if path.casefold() in names:
            raise WorkspaceError("Duplicate generated destination: " + path, 2)
        names.add(path.casefold())
        output[path] = (data, owner)
    for entry in manifest["files"]:
        data = file_bytes(below(package, entry["source"]), package)
        for dest in entry["destinations"]:
            rendered = data
            if dest["render"] == "markdown":
                def replace(m):
                    if m[1] not in tokens:
                        raise WorkspaceError("Unknown template field: " + m[1], 2)
                    return tokens[m[1]]
                rendered = TOKEN.sub(replace, data.decode("utf-8")).encode("utf-8")
                if b"{{" in rendered or b"}}" in rendered:
                    raise WorkspaceError("Unresolved template field.", 2)
            add(mapping_path(mapping, dest), rendered, dest["owner"])
    # Never persist the original setup location: installed trees must move independently.
    installed_config = dict(config)
    installed_config.pop("parent_directory", None)
    add(metadata(config, "installation.json"), json_bytes(installed_config), "local")
    workspaces, pending = workspace_bytes(target, config)
    for path, data in workspaces.items():
        add(path, data, "generated")
    directories = set(mapping.values()) - {"."}
    directories |= {mapping["ai_work"] + "/tickets/active", mapping["ai_work"] + "/tickets/archive", metadata(config, "reports")}
    for item in manifest["directories"]:
        keys(item, ("directory_id", "relative_path"), ("directory_id", "relative_path"))
        if item["directory_id"] not in mapping:
            raise WorkspaceError("Unknown directory mapping.", 2)
        directories.add(mapping_path(mapping, item))
    for path in output:
        directories.update(str(p) for p in PurePosixPath(path).parents if str(p) != ".")
    for directory in list(directories):
        directories.update(str(p) for p in PurePosixPath(directory).parents if str(p) != ".")
    folded_directories = [x.casefold() for x in directories]
    if len(set(folded_directories)) != len(folded_directories):
        raise WorkspaceError("Case-insensitive directory destination collision.", 2)
    reserved = {MARKER, metadata(config, "installed-state.json"), metadata(config, ".maintenance.lock")}
    if any(x.casefold() in {r.casefold() for r in reserved} for x in output):
        raise WorkspaceError("Manifest maps a reserved runtime file.", 2)
    for directory in directories:
        below(target, directory)
        if directory.casefold() in names:
            raise WorkspaceError("File/directory destination collision.", 2)
    if {path: owner for path, (_, owner) in output.items()} != expected_files(config):
        raise WorkspaceError("Deployment mappings differ from the reviewed runtime layout.", 2)
    return output, sorted(directories, key=lambda x: (len(PurePosixPath(x).parts), x)), pending


def initialize(package, target, config):
    output, directories, pending = plan(package, target, config)
    root = Path(target)
    try:
        root.mkdir()
    except FileExistsError as exc:
        raise WorkspaceError("Target appeared concurrently; refusing it.", 2) from exc
    try:
        exclusive(root / MARKER, json_bytes({"status": "incomplete", "package_version": VERSION}), root)
        for directory in directories:
            below(root, directory).mkdir()
        for path, (data, _) in output.items():
            exclusive(below(root, path), data, root)
            if path == "refresh_vscode_workspace macOS.command":
                launcher = below(root, path)
                launcher.chmod(launcher.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        state = {"schema_version": 1, "package_version": VERSION, "design_version": DESIGN_VERSION,
                 "initialization_status": "incomplete", "directory_names": config["directories"],
                 "vscode_workspace_name": config["vscode_workspace_name"],
                 "directories": directories,
                 "managed_files": [{"path": path, "owner": owner, "sha256": digest(data)} for path, (data, owner) in sorted(output.items())]}
        sp = below(root, metadata(config, "installed-state.json"))
        exclusive(sp, json_bytes(state), root)
        findings = validate_root(root, config, state, initializing=True)
        errors = [x for x in findings if x["severity"] == "error"]
        if errors:
            raise WorkspaceError("Internal validation failed: " + errors[0]["evidence"])
        before = digest(file_bytes(sp, root))
        state["initialization_status"] = "complete"
        atomic_update(sp, json_bytes(state), root, before)
        safe(root / MARKER, root).unlink()
        return {"status": "initialized", "target": str(root), "files_created": len(output) + 1,
                "pending_manual": pending + manual_steps(config)}
    except (OSError, WorkspaceError, ValueError) as exc:
        raise WorkspaceError("Initialization incomplete; retained target for manual inspection. Choose another target or remove it manually after inspection. Cause: " + str(exc), 3) from exc


def manual_steps(config):
    return ["Manually populate project overview/reference map as needed.",
            "Manually clone/add approved folders under the repository groups, then open the generated refresh_vscode_workspace launcher to discover and review them.",
            "VS Code users: manually open " + vscode_workspace_path(config) + ". Other IDE users: open/import repositories normally and keep this helper file for validation.",
            "Read " + config["directories"]["ai_work"] + "/COPILOT_GUIDE.md and verify orientation/skill discovery in the actual IDE; use explicit attachments/direct commands if unavailable.",
            "Choose and configure an allowed backup location manually."]


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=VERSION)
    subs = parser.add_subparsers(dest="command", required=True)
    for command in ("plan", "init"):
        sub = subs.add_parser(command)
        sub.add_argument("--target", help="New absolute directory; overrides parent_directory/root_folder_name settings")
        sub.add_argument("--config", help="JSON settings; default is WORKSPACE_SETUP/settings.json")
        if command == "init":
            sub.add_argument("--apply", action="store_true", required=True)
    return parser


def execute(args, package=None):
    package = safe(package or PACKAGE)
    config, _ = read_settings(package, args.config)
    target = resolve_target(config, args.target)
    if args.command == "init":
        return initialize(package, target, config), 0
    files, dirs, pending = plan(package, target, config)
    return {"status": "preview-only", "target": str(target), "directories": dirs,
            "files": [{"path": path, "owner": owner} for path, (_, owner) in sorted(files.items())] +
                     [{"path": metadata(config, "installed-state.json"), "owner": "local"}],
            "transient_files": [MARKER, metadata(config, ".installed-state.<unique>.tmp")],
            "pending_manual": pending + manual_steps(config)}, 0


def main(argv=None):
    if sys.version_info < (3, 9):
        print("Python 3.9+ is required. Select an approved newer interpreter; no software has been installed.", file=sys.stderr)
        return 2
    args = build_parser().parse_args(argv)
    try:
        result, code = execute(args)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return code
    except (WorkspaceError, OSError, ValueError, TypeError, KeyError) as exc:
        print("Error: " + str(exc), file=sys.stderr)
        return getattr(exc, "code", 1)


if __name__ == "__main__":
    raise SystemExit(main())
