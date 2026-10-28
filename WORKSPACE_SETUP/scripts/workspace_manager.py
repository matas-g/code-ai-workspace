#!/usr/bin/env python3
"""Daily workspace tools. Independent of the installer; standard library only."""
import sys
sys.dont_write_bytecode = True

import argparse
from contextlib import contextmanager
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
from urllib.parse import quote, unquote, urlsplit
import uuid

VERSION = "0.1.17"
DESIGN_VERSION = "1.0"
AI_ROOT = Path(__file__).absolute().parent.parent
DEFAULT_ROOT_FOLDER_NAME = "Code-AI"
DEFAULTS = {
    "primary_repositories": "MAIN_PROJECT", "other_repositories": "OTHER_PROJECTS",
    "company_documentation": "COMPANY_DOCS", "ai_work": "AI_WORK",
    "knowledge": "KNOWLEDGE_BASE",
}
FIXED = {"root": ".", "ide_configs": "ide_configs"}
MARKER = ".initialization-incomplete.json"
RESERVED = re.compile(r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])$", re.I)
NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9 _-]{0,63}\Z")
TOKEN = re.compile(r"\{\{([a-z_]+)\}\}")
GROUPS = ("primary_repositories", "other_repositories", "company_documentation")
PREFIXES = dict(zip(GROUPS, ("MAIN", "OTHER", "DOCS")))


class WorkspaceError(Exception):
    def __init__(self, message, code=1):
        super().__init__(message)
        self.code = code


# Runtime-required paths only. No installer sources, manifests, tests or design documents.
LAYOUT = [
    ("root", "README.md", "generated"), ("root", ".gitignore", "generated"),
    ("ai_work", "DAILY_WORK.md", "generated"), ("ai_work", "tools/workspace_manager.py", "framework"),
    ("ai_work", "COPILOT_GUIDE.md", "generated"),
    ("ai_work", ".github/copilot-instructions.md", "user"),
    ("ai_work", "tools/terminal_output_formatter.py", "framework"),
    ("ai_work", "tools/vscode_workspace_updater.py", "framework"),
    ("root", "refresh_vscode_workspace macOS.command", "framework"),
    ("root", "refresh_vscode_workspace Windows.cmd", "framework"),
    ("ai_work", "project/overview.md", "user"), ("ai_work", "project/reference-map.md", "user"),
    ("ai_work", ".github/skills/ca-config-audit/SKILL.md", "user"),
    ("ai_work", ".github/skills/ca-jira-ticket-init/SKILL.md", "user"),
    ("ai_work", ".github/skills/ca-jira-ticket-archive/SKILL.md", "user"),
    ("ai_work", ".github/skills/ca-jira-ticket-restore/SKILL.md", "user"),
    ("ai_work", ".github/skills/ca-jira-ticket-init/scripts/ticket.py", "framework"),
    ("ai_work", ".github/skills/ca-jira-ticket-init/templates/brief.md", "user"),
    ("ai_work", ".github/skills/ca-jira-ticket-init/templates/plan.md", "user"),
    ("ai_work", ".github/skills/ca-jira-ticket-init/templates/review.md", "user"),
    ("ai_work", ".github/skills/ca-jira-ticket-init/templates/notes.md", "user"),
    ("ai_work", ".github/skills/ca-change-review/SKILL.md", "user"),
    ("ai_work", ".github/skills/ca-change-review/resources/review-checklist.md", "user"),
    ("knowledge", "README.md", "user"),
    ("knowledge", "examples/example-guide/guide.md", "user"),
    ("knowledge", "examples/example-guide/assets/example-diagram.svg", "user"),
]


def metadata(config, filename):
    return config["directories"]["ai_work"] + "/.framework/" + filename


def expected_files(config):
    mapping = folder_map(config)
    expected = {mapping_path(mapping, {"directory_id": d, "relative_path": p}): owner for d, p, owner in LAYOUT}
    expected[metadata(config, "installation.json")] = "local"
    expected[vscode_workspace_path(config)] = "generated"
    return expected

def vscode_workspace_path(config):
    return "ide_configs/" + config["vscode_workspace_name"] + ".code-workspace"


def present(path):
    return os.path.lexists(path)


def redirected(info):
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, "st_file_attributes", 0) & 0x400)


def safe(path, boundary=None):
    """Check every existing component without following symlinks/reparse points."""
    path = Path(path)
    if os.name == "nt" and path.drive.startswith("\\"):
        raise WorkspaceError("UNC/network locations are not supported.", 2)
    if not path.is_absolute() or ".." in path.parts:
        raise WorkspaceError("An absolute, non-traversing path is required: " + str(path), 2)
    if boundary is not None and not path.is_relative_to(Path(boundary)):
        raise WorkspaceError("Path escapes the permitted root: " + str(path), 2)
    chain = list(reversed(path.parents)) + [path]
    for part in chain:
        if present(part):
            info = part.lstat()
            if redirected(info):
                raise WorkspaceError("Redirected path refused: " + str(part), 2)
            if part != path and not stat.S_ISDIR(info.st_mode):
                raise WorkspaceError("Path parent is not a directory: " + str(part), 2)
    return path


def relative(value):
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise WorkspaceError("Invalid relative path: " + repr(value), 2)
    p = PurePosixPath(value)
    if p.is_absolute() or any(x in ("", ".", "..") for x in value.split("/")):
        raise WorkspaceError("Unsafe relative path: " + value, 2)
    return p


def below(root, value):
    return safe(Path(root).joinpath(*relative(value).parts), root)


def file_bytes(path, boundary=None):
    path = safe(path, boundary)
    if not present(path) or not stat.S_ISREG(path.lstat().st_mode):
        raise WorkspaceError("Expected an ordinary file: " + str(path))
    return path.read_bytes()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def load_json(path, boundary=None):
    def pairs(items):
        obj = {}
        for k, v in items:
            if k in obj:
                raise WorkspaceError("Duplicate JSON key: " + k, 2)
            obj[k] = v
        return obj
    try:
        return json.loads(file_bytes(path, boundary), object_pairs_hook=pairs,
                          parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
    except (ValueError, UnicodeError) as exc:
        raise WorkspaceError("Invalid JSON in " + str(path) + ": " + str(exc), 2) from exc


def keys(obj, allowed, required=()):
    if not isinstance(obj, dict) or set(obj) - set(allowed) or set(required) - set(obj):
        raise WorkspaceError("Invalid object keys; allowed: " + ", ".join(sorted(allowed)), 2)


def component(name):
    if not isinstance(name, str) or not NAME.fullmatch(name) or name != name.strip() or RESERVED.fullmatch(name):
        raise WorkspaceError("Invalid portable directory name: " + repr(name), 2)
    return name


def repository_component(name):
    """Existing repository names may contain dots and Unicode; never rewrite them."""
    if (not isinstance(name, str) or not 1 <= len(name) <= 255 or name in (".", "..")
            or name != name.strip() or name.endswith(".")
            or re.search(r'[<>:"/\\|?*\x00-\x1f\x7f]', name)
            or RESERVED.fullmatch(name.split(".")[0])):
        raise WorkspaceError("Invalid portable repository folder name: " + repr(name), 2)
    return name


def validate_config(raw):
    keys(raw, ("schema_version", "root_folder_name", "parent_directory", "vscode_workspace_name", "directories", "repositories"), ("schema_version",))
    if type(raw["schema_version"]) is not int or raw["schema_version"] != 1:
        raise WorkspaceError("Configuration schema_version must be 1.", 2)
    root_folder_name = component(raw.get("root_folder_name", DEFAULT_ROOT_FOLDER_NAME))
    parent_directory = raw.get("parent_directory", ".")
    if not isinstance(parent_directory, str) or not parent_directory.strip() or any(ord(c) < 32 or ord(c) == 127 for c in parent_directory):
        raise WorkspaceError("parent_directory must be a nonempty directory path without control characters.", 2)
    vscode_workspace_name = component(raw.get("vscode_workspace_name", "Development"))
    supplied = raw.get("directories", {})
    keys(supplied, DEFAULTS)
    directories = dict(DEFAULTS, **supplied)
    names = [component(x).casefold() for x in directories.values()] + ["workspace_setup", "ide_configs"]
    if len(set(names)) != len(names):
        raise WorkspaceError("Case-insensitive top-level name collision.", 2)
    repos = raw.get("repositories", [])
    if not isinstance(repos, list):
        raise WorkspaceError("repositories must be a list.", 2)
    ids, paths = set(), set()
    allowed = {"id", "group", "directory", "display_name", "access", "include_in_workspace"}
    for repo in repos:
        keys(repo, allowed, allowed)
        rid = repo["id"]
        if not isinstance(rid, str) or not re.fullmatch(r"[a-z][a-z0-9-]{0,63}", rid) or rid in ids:
            raise WorkspaceError("Repository IDs must be unique portable lowercase identifiers.", 2)
        ids.add(rid)
        if repo["group"] not in ("primary_repositories", "other_repositories", "company_documentation"):
            raise WorkspaceError("Invalid repository group.", 2)
        repository_component(repo["directory"])
        pair = (repo["group"], repo["directory"].casefold())
        if pair in paths:
            raise WorkspaceError("Repository path collision.", 2)
        paths.add(pair)
        display = repo["display_name"]
        if not isinstance(display, str) or not display.strip() or len(display) > 255 or any(ord(c) < 32 or ord(c) == 127 for c in display):
            raise WorkspaceError("Invalid repository display_name (maximum 255 printable characters).", 2)
        if repo["access"] not in ("develop", "reference") or type(repo["include_in_workspace"]) is not bool:
            raise WorkspaceError("Invalid repository access or include_in_workspace.", 2)
    return {"schema_version": 1, "root_folder_name": root_folder_name, "parent_directory": parent_directory, "vscode_workspace_name": vscode_workspace_name, "directories": directories, "repositories": repos}


def folder_map(config):
    return dict(FIXED, **config["directories"])


def mapping_path(mapping, dest):
    base = mapping[dest["directory_id"]]
    return dest["relative_path"] if base == "." else base + "/" + dest["relative_path"]


def workspace_bytes(root, config):
    paths, pending = [], []
    groups = config["directories"]
    def repo_root(repo):
        p = below(root, groups[repo["group"]] + "/" + repo["directory"])
        if not present(p):
            pending.append(groups[repo["group"]] + "/" + repo["directory"] + ": folder missing; selection retained")
            return None
        if not p.is_dir():
            pending.append(repo["id"] + ": expected directory, excluded")
            return None
        return {"name": PREFIXES[repo["group"]] + " · " + repo["display_name"], "path": "../" + p.relative_to(root).as_posix()}
    refs = {"other_repositories": [], "company_documentation": []}
    for repo in config["repositories"]:
        if repo["include_in_workspace"]:
            item = repo_root(repo)
            if item:
                (paths if repo["group"] == "primary_repositories" else refs[repo["group"]]).append(item)
    paths += [{"name": "AI Work", "path": "../" + groups["ai_work"]},
              {"name": "Knowledge", "path": "../" + groups["knowledge"]}]
    paths += refs["other_repositories"] + refs["company_documentation"]
    return {
        vscode_workspace_path(config): json_bytes({"folders": paths, "settings": {}}),
    }, pending


def exclusive(path, data, root):
    with safe(path, root).open("xb") as stream:
        stream.write(data)


def atomic_update(path, data, root, expected):
    path = safe(path, root)
    if digest(file_bytes(path, root)) != expected:
        raise WorkspaceError("Concurrent edit or drift; refusing overwrite: " + str(path))
    temp = path.parent / ("." + path.name + "." + uuid.uuid4().hex + ".tmp")
    exclusive(temp, data, root)
    try:
        safe(path, root)
        if digest(file_bytes(path, root)) != expected:
            raise WorkspaceError("Concurrent edit; destination retained: " + str(path))
        os.replace(temp, path)
    finally:
        if present(temp):
            safe(temp, root).unlink()


def installed(ai_root):
    ai_root = safe(ai_root)
    root = safe(ai_root.parent)
    state_directory = safe(ai_root / ".framework", root)
    if present(root / MARKER):
        raise WorkspaceError("This initialization is incomplete; inspect it manually.", 3)
    state = load_json(state_directory / "installed-state.json", root)
    keys(state, ("schema_version", "package_version", "design_version", "initialization_status", "directory_names", "vscode_workspace_name", "directories", "managed_files"),
         ("schema_version", "package_version", "design_version", "initialization_status", "directory_names", "vscode_workspace_name", "directories", "managed_files"))
    if type(state["schema_version"]) is not int or state["schema_version"] != 1 or state["package_version"] != VERSION or state["design_version"] != DESIGN_VERSION or state["initialization_status"] != "complete":
        raise WorkspaceError("Unsupported or incomplete installed state.", 2)
    config = validate_config(load_json(state_directory / "installation.json", root))
    if config["directories"]["ai_work"] != ai_root.name:
        raise WorkspaceError("Runtime location does not match the initialized AI directory.", 2)
    if state["directory_names"] != config["directories"]:
        raise WorkspaceError("Directory names changed since initialization; choose a new development folder for different names.", 2)
    if state["vscode_workspace_name"] != config["vscode_workspace_name"]:
        raise WorkspaceError("VS Code workspace name changed since initialization; choose a new development folder for different names.", 2)
    if not isinstance(state["managed_files"], list) or not isinstance(state["directories"], list):
        raise WorkspaceError("Invalid installed-state inventory.", 2)
    seen = set()
    for entry in state["managed_files"]:
        keys(entry, ("path", "owner", "sha256"), ("path", "owner", "sha256"))
        relative(entry["path"])
        if entry["path"].casefold() in seen or entry["owner"] not in ("framework", "generated", "user", "local") or not isinstance(entry["sha256"], str) or not re.fullmatch("[0-9a-f]{64}", entry["sha256"]):
            raise WorkspaceError("Invalid state file entry.", 2)
        seen.add(entry["path"].casefold())
    for directory in state["directories"]:
        relative(directory)
    return root, config, state


def finding(severity, path, evidence, remedy="", classification="deterministic"):
    return {"severity": severity, "path": str(path), "evidence": evidence, "remedy": remedy, "classification": classification}


def markdown_links(path, root, severity="error"):
    result = []
    safe(path, root)
    if path.stat().st_size > 1024 * 1024:
        return [finding("warning", path.relative_to(root), "Document exceeds 1 MiB; link inspection skipped.")]
    data = file_bytes(path, root)
    text = re.sub(r"```.*?```", "", data.decode("utf-8"), flags=re.S)
    for dest in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        dest = dest.strip().strip("<>")
        if urlsplit(dest).scheme or dest.startswith("#"):
            continue
        dest = unquote(dest.split("#", 1)[0])
        if not dest:
            continue
        p = Path(os.path.abspath(path.parent / dest))
        try:
            safe(p, root)
            if not present(p):
                result.append(finding(severity, path.relative_to(root), "Missing linked resource: " + dest, "Restore/reconcile this resource manually."))
        except WorkspaceError as exc:
            result.append(finding(severity, path.relative_to(root), str(exc)))
    return result


def skill_metadata(path, root, strict):
    text = file_bytes(path, root).decode("utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise WorkspaceError("Missing YAML frontmatter.")
    header = text[4:].split("\n---\n", 1)[0]
    info = {}
    for line in header.splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"([a-z-]+): (.+)", line)
        if not match or match[1] in info:
            raise WorkspaceError("Unsupported/duplicate frontmatter syntax; only simple scalar fields are checked.")
        info[match[1]] = match[2].strip().strip("\"'")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", info.get("name", "")) or info["name"] != path.parent.name:
        raise WorkspaceError("Skill name must match its directory and use lowercase letters, digits and hyphens.")
    if not 1 <= len(info.get("description", "")) <= 1024:
        raise WorkspaceError("Missing or oversized skill description.")
    if strict and not info["name"].startswith("ca-"):
        raise WorkspaceError("Framework skill names must use the ca- prefix.")
    if strict and info.get("disable-model-invocation") != "true":
        raise WorkspaceError("Packaged workflow must be explicit-invocation only.")
    return info


def validate_root(root, config, state, initializing=False):
    result = []
    mapping = folder_map(config)
    expected_owners = expected_files(config)
    actual_entries = {x["path"]: x for x in state["managed_files"]}
    for path, owner in expected_owners.items():
        if path not in actual_entries or actual_entries[path]["owner"] != owner:
            result.append(finding("error", path, "State inventory missing or ownership inconsistent with package."))
    required_directories = set(mapping.values()) - {"."}
    required_directories.update({config["directories"]["ai_work"] + "/tickets/active",
                                 config["directories"]["ai_work"] + "/tickets/archive", metadata(config, "reports")})
    if not required_directories.issubset(set(state["directories"])):
        result.append(finding("error", metadata(config, "installed-state.json"), "Required directory inventory was removed."))
    optional_examples = config["directories"]["knowledge"] + "/examples"
    def is_example(path):
        return path == optional_examples or path.startswith(optional_examples + "/")
    for directory in state["directories"]:
        try:
            p = below(root, directory)
            if not p.is_dir():
                result.append(finding("info" if is_example(directory) else "error", directory, "Directory absent (optional example)." if is_example(directory) else "Required directory missing."))
        except (WorkspaceError, OSError) as exc:
            result.append(finding("error", directory, str(exc)))
    for entry in state["managed_files"]:
        path, owner = entry["path"], entry["owner"]
        if expected_owners.get(path) != owner:
            result.append(finding("error", path, "Unexpected managed path/owner; file not inspected."))
            continue
        if is_example(path) and not present(below(root, path)):
            result.append(finding("info", path, "Optional synthetic example removed."))
            continue
        try:
            data = file_bytes(below(root, path), root)
            if path != vscode_workspace_path(config) and digest(data) != entry["sha256"]:
                severity = "error" if owner in ("generated", "framework") else "info"
                result.append(finding(severity, path, "Content differs from recorded baseline (" + owner + ").", "Review intentionally; no automatic repair."))
            if owner == "generated" and path != vscode_workspace_path(config) and (b"{{" in data or b"}}" in data):
                result.append(finding("error", path, "Unresolved generated placeholder."))
            if path.endswith(".md") and owner in ("generated", "user") and "/templates/" not in path:
                result.extend(markdown_links(below(root, path), root))
        except (WorkspaceError, OSError, UnicodeError, ValueError) as exc:
            result.append(finding("error", path, str(exc)))
    ai = config["directories"]["ai_work"]
    for name in ("ca-jira-ticket-init", "ca-jira-ticket-archive", "ca-jira-ticket-restore", "ca-change-review", "ca-config-audit"):
        skill = ai + "/.github/skills/" + name
        try:
            skill_metadata(below(root, skill + "/SKILL.md"), root, True)
        except (WorkspaceError, OSError, UnicodeError) as exc:
            result.append(finding("error", skill, str(exc)))
    try:
        expected, pending = workspace_bytes(root, config)
        for message in pending:
            result.append(finding("pending-manual", "repositories", message))
        for path, content in expected.items():
            _, actual, _, _ = load_helper("vscode_workspace_updater").document(file_bytes(below(root, path), root))
            if actual.get("folders") != json.loads(content)["folders"]:
                result.append(finding("warning", path, "Workspace folders differ from the enabled/present inventory.", "Preview refresh; it replaces only folders and preserves other workspace content."))
    except (WorkspaceError, OSError, ValueError, TypeError) as exc:
        result.append(finding("error", "ide_configs", str(exc)))
    result.append(finding("pending-manual", "Copilot Local", "Automatic orientation loading across workspace roots, skill discovery, Ask/Plan/Agent behavior and native Windows compatibility need manual evidence. Other IDEs require separate discovery checks.", "Follow " + config["directories"]["ai_work"] + "/COPILOT_GUIDE.md for discovery checks and manual fallback. Structural validation does not certify Copilot loading."))
    return result


def audit_root(root, config, state):
    results = validate_root(root, config, state)
    roots = [below(root, config["directories"]["ai_work"])]
    for repo in config["repositories"]:
        p = below(root, config["directories"][repo["group"]] + "/" + repo["directory"])
        if p.is_dir():
            roots.append(p)
    names = {}
    for base in roots:
        for location in (".github/skills", ".agents/skills", ".claude/skills"):
            try:
                folder = below(base, location)
                if not present(folder):
                    continue
                children = sorted(folder.iterdir())
                if len(children) > 250:
                    results.append(finding("warning", folder.relative_to(root), "Scope limited to first 250 skill directories."))
                for child in children[:250]:
                    try:
                        safe(child, root)
                        if not child.is_dir():
                            continue
                        p = safe(child / "SKILL.md", root)
                        meta = skill_metadata(p, root, False)
                        names.setdefault(meta["name"], []).append(str(p.relative_to(root)))
                        results.extend(markdown_links(p, root, "warning"))
                    except (WorkspaceError, OSError, UnicodeError, ValueError) as exc:
                        results.append(finding("warning", child.relative_to(root), str(exc), classification="uncertain"))
            except (WorkspaceError, OSError) as exc:
                results.append(finding("warning", location, str(exc)))
        candidates = [base / x for x in ("AGENTS.md", "CLAUDE.md", ".github/copilot-instructions.md")]
        try:
            instructions = below(base, ".github/instructions")
            if instructions.is_dir():
                stack, count = [instructions], 0
                while stack and count < 250:
                    folder = stack.pop()
                    safe(folder, root)
                    for child in sorted(folder.iterdir()):
                        count += 1
                        if count > 250:
                            break
                        safe(child, root)
                        if child.is_dir():
                            stack.append(child)
                        elif child.suffix == ".md":
                            candidates.append(child)
                if stack or count >= 250:
                    results.append(finding("warning", instructions.relative_to(root), "Instruction traversal limited to 250 entries."))
            for p in candidates:
                if present(p):
                    safe(p, root)
                    if not stat.S_ISREG(p.lstat().st_mode):
                        raise WorkspaceError("Instruction candidate is not an ordinary file.")
                    results.append(finding("info", p.relative_to(root), "Instruction candidate inventoried; loading/semantic compatibility not certified.", classification="uncertain"))
                    results.extend(markdown_links(p, root, "warning"))
        except (WorkspaceError, OSError, UnicodeError) as exc:
            results.append(finding("warning", base.relative_to(root), str(exc)))
    for name, paths in names.items():
        if len(paths) > 1:
            results.append(finding("warning", "; ".join(paths), "Duplicate active-location skill name: " + name, "Reconcile names manually; actual harness loading is unverified."))
    results.append(finding("info", "audit scope", "No global configuration, payload baselines, private attachments, nested repositories or semantic certification included."))
    return results


def load_helper(name):
    path = safe(Path(__file__).absolute().parent / (name + ".py"))
    file_bytes(path, path.parent)
    spec = importlib.util.spec_from_file_location("workspace_" + name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@contextmanager
def maintenance(root, config):
    lock = below(root, metadata(config, ".maintenance.lock"))
    try:
        exclusive(lock, b"refresh\n", root)
    except FileExistsError as exc:
        raise WorkspaceError("Maintenance already running or a stale lock needs manual inspection.") from exc
    try:
        yield
    finally:
        safe(lock, root).unlink()


def repository_path(config, repo):
    return config["directories"][repo["group"]] + "/" + repo["directory"]


def registration_plan(root, config):
    """Read immediate child folders only; existing entries are never rewritten."""
    cp = below(root, metadata(config, "installation.json"))
    before = file_bytes(cp, root)
    raw = load_json(cp, root)
    if validate_config(raw) != config:
        raise WorkspaceError("Configuration changed; rerun and review again.")
    known = {(repo["group"], repo["directory"]): repo for repo in config["repositories"]}
    known_folded = {(repo["group"], repo["directory"].casefold()): repo for repo in config["repositories"]}
    ids = {repo["id"] for repo in config["repositories"]}
    additions, warnings, observed = [], [], []
    for group in GROUPS:
        folder = below(root, config["directories"][group])
        if not folder.is_dir():
            raise WorkspaceError("Grouping directory missing; restore it before refresh: " + str(folder))
        folded = set()
        for child in sorted(folder.iterdir(), key=lambda p: (p.name.casefold(), p.name)):
            info = child.lstat()
            if redirected(info):
                warnings.append(child.relative_to(root).as_posix() + ": redirected path skipped")
                observed.append((group, child.name, "redirected"))
                continue
            if not stat.S_ISDIR(info.st_mode):
                continue
            if child.name.casefold() in folded:
                raise WorkspaceError("Case-insensitive folder collision in " + str(folder) + "; reconcile names manually.")
            folded.add(child.name.casefold())
            observed.append((group, child.name, "directory"))
            if (group, child.name) in known:
                continue
            # On case-insensitive filesystems two spellings can identify the
            # same existing path. Preserve its entry instead of duplicating it.
            candidate = known_folded.get((group, child.name.casefold()))
            if candidate is not None:
                old_path = root / repository_path(config, candidate)
                if present(old_path) and not redirected(old_path.lstat()) and old_path.samefile(child):
                    continue
            try:
                repository_component(child.name)
            except WorkspaceError as exc:
                warnings.append(child.relative_to(root).as_posix() + ": skipped; " + str(exc))
                continue
            # IDs are bookkeeping only. Display names retain the actual folder spelling.
            stem = re.sub('[^a-z0-9]+', '-', child.name.lower()).strip('-')[:32] or 'folder'
            base = 'repo-' + stem + '-' + digest((group + '/' + child.name).encode('utf-8'))[:12]
            rid, suffix = base, 2
            while rid in ids:
                rid = base + '-' + str(suffix)
                suffix += 1
            ids.add(rid)
            additions.append({"id": rid, "group": group, "directory": child.name,
                              "display_name": child.name,
                              "access": "reference" if group == "company_documentation" else "develop",
                              "include_in_workspace": True})
    missing = []
    for repo in config["repositories"]:
        path = root / repository_path(config, repo)
        safe(path.parent, root)
        if not present(path):
            missing.append(repo)
        elif not redirected(path.lstat()) and not path.is_dir():
            warnings.append(repository_path(config, repo) + ": expected a folder; entry retained")
    return {"before": digest(before), "raw": raw, "additions": additions,
            "missing": missing, "warnings": warnings, "observed": observed}


def registration_config(plan, remove_missing=False):
    raw = dict(plan["raw"])
    removed = {repo["id"] for repo in plan["missing"]} if remove_missing else set()
    raw["repositories"] = [repo for repo in raw.get("repositories", []) if repo["id"] not in removed] + plan["additions"]
    validate_config(raw)
    return raw


def apply_registration(root, config, plan, remove_missing=False):
    raw = registration_config(plan, remove_missing)
    with maintenance(root, config):
        installed(below(root, config["directories"]["ai_work"]))
        if registration_plan(root, config) != plan:
            raise WorkspaceError("Folders or configuration changed after preview; rerun and review again.")
        if raw != plan["raw"]:
            atomic_update(below(root, metadata(config, "installation.json")), json_bytes(raw), root, plan["before"])
    return validate_config(raw)


def workspace_plan(root, config, state, proposed=False):
    for directory_id in GROUPS + ("ai_work", "knowledge"):
        directory = below(root, config["directories"][directory_id])
        if not directory.is_dir():
            raise WorkspaceError("Required directory missing; restore it before refresh: " + str(directory))
    if not proposed and validate_config(load_json(below(root, metadata(config, "installation.json")), root)) != config:
        raise WorkspaceError("Configuration changed; rerun and review again.")
    if load_json(below(root, metadata(config, "installed-state.json")), root) != state:
        raise WorkspaceError("Installed state changed; rerun and review again.")
    expected, pending = workspace_bytes(root, config)
    path = vscode_workspace_path(config)
    entries = {entry["path"]: entry for entry in state["managed_files"]}
    if path not in entries or entries[path]["owner"] != "generated":
        raise WorkspaceError("Workspace inventory/ownership is inconsistent: " + path)
    before = file_bytes(below(root, path), root)
    helper = load_helper("vscode_workspace_updater")
    _, actual, _, _ = helper.document(before)
    folders = json.loads(expected[path])["folders"]
    data = helper.replace_folders(before, folders)
    old = actual.get("folders", [])
    changes = []
    old_paths = {item["path"] for item in old}
    new_paths = {item["path"] for item in folders}
    for item in old:
        if item["path"] not in new_paths:
            changes.append({"action": "remove", "folder": item})
    for item in folders:
        previous = [x for x in old if x["path"] == item["path"]]
        if not previous:
            changes.append({"action": "add", "folder": item})
        elif previous != [item]:
            changes.append({"action": "change", "before": previous, "folder": item})
    old_order = [item["path"] for item in old if item["path"] in new_paths]
    new_order = [item["path"] for item in folders if item["path"] in old_paths]
    if old_order != new_order or (data != before and not changes):
        changes.append({"action": "reorder", "folders": folders})
    return {"path": path, "before": digest(before), "data": data,
            "changed": data != before, "changes": changes, "pending_manual": pending,
            "config_before": digest(file_bytes(below(root, metadata(config, "installation.json")), root)),
            "state_before": digest(file_bytes(below(root, metadata(config, "installed-state.json")), root))}


def apply_workspace(root, config, state, plan):
    with maintenance(root, config):
        installed(below(root, config["directories"]["ai_work"]))
        if workspace_plan(root, config, state) != plan:
            raise WorkspaceError("Workspace, configuration or available folders changed after preview; rerun and review again.")
        if plan["changed"]:
            atomic_update(below(root, plan["path"]), plan["data"], root, plan["before"])
            updated = json.loads(json.dumps(state))
            next(item for item in updated["managed_files"] if item["path"] == plan["path"])["sha256"] = digest(plan["data"])
            # A failure here is recoverable: workspace content is user editable and
            # validation does not require its old whole-file hash to match.
            atomic_update(below(root, metadata(config, "installed-state.json")), json_bytes(updated), root, plan["state_before"])


def refresh(root, config, state, apply=False, remove_missing=False):
    """Noninteractive preview/apply of the same discovery and folder-list operations."""
    registration = registration_plan(root, config)
    proposed = registration_config(registration, remove_missing)
    effective = validate_config(proposed)
    workspace = workspace_plan(root, effective, state, proposed=True)
    if apply:
        # Preflight the workspace before committing registration. Each phase is
        # separately durable, matching the interactive two-approval flow.
        effective = apply_registration(root, config, registration, remove_missing)
        _, effective, state = installed(below(root, effective["directories"]["ai_work"]))
        workspace = workspace_plan(root, effective, state)
        if workspace["changed"]:
            apply_workspace(root, effective, state, workspace)
    return {"status": "refreshed" if apply else "preview",
            "registration_additions": registration["additions"],
            "missing_entries": registration["missing"],
            "registration_removals": registration["missing"] if remove_missing else [],
            "warnings": registration["warnings"],
            "workspace_files_to_update": [workspace["path"]] if workspace["changed"] else [],
            "workspace_changes": workspace["changes"], "pending_manual": workspace["pending_manual"]}


def action_prompt(input_fn, output, missing=False):
    while True:
        try:
            response = input_fn("Action [y/N" + ("/remove-missing" if missing else "") + "]: ").strip().casefold()
        except EOFError:
            output("Input closed. Canceled; this step was not applied.")
            return "cancel"
        if response in ("y", "yes"):
            return "keep"
        if missing and response == "remove-missing":
            return "remove"
        if response in ("", "n", "no"):
            return "cancel"
        output("Type y" + (", remove-missing" if missing else "") + ", or n to cancel.")


def printable(value):
    # Paths and labels are data, never terminal escape sequences or shell input.
    return json.dumps(str(value), ensure_ascii=False)[1:-1]


def interactive_refresh(ai_root=None, input_fn=input, output=print):
    c = load_helper("terminal_output_formatter").Console(output)
    c.heading("Refresh VS Code workspace " + VERSION)
    c.text("Python " + sys.version.split()[0])
    c.path(sys.executable)
    registration_saved = False
    try:
        root, config, state = installed(ai_root or AI_ROOT)
        c.text("Development folder:")
        c.path(root)
        c.heading("[1/2] Repository registration")
        registration = registration_plan(root, config)
        rows = [("+ " + printable(repository_path(config, repo)), "— register; enabled")
                for repo in registration["additions"]]
        rows += [("! " + printable(repository_path(config, repo)), "— missing; entry retained unless removed")
                 for repo in registration["missing"]]
        if rows:
            c.text("+ new entry   ! missing entry (removal requires remove-missing)")
            c.blank()
            c.columns(rows)
        else:
            c.heading("No changes")
            c.text("Registration is up to date. No confirmation needed.")
        for warning in registration["warnings"]:
            c.text("! " + printable(warning))
        if registration["additions"] or registration["missing"]:
            c.blank()
            c.text("Registration: " + str(len(registration["additions"])) + " new; " + str(len(registration["missing"])) + " missing. Existing choices are preserved.")
            c.text("y: register additions; retain missing entries.")
            if registration["missing"]:
                c.text("remove-missing: register additions; remove ALL listed missing entries from configuration only. No folders or code are deleted.")
            c.text("n or Enter: cancel and finish.")
            c.blank()
            answer = action_prompt(input_fn, output, bool(registration["missing"]))
            if answer == "cancel":
                c.text("Canceled. No configuration or workspace changes applied.")
                return 0
            config = apply_registration(root, config, registration, answer == "remove")
            registration_saved = bool(registration["additions"] or (answer == "remove" and registration["missing"]))
            c.text("Registration saved." if registration_saved else "Registration unchanged; missing entries retained.")
        root, config, state = installed(root / config["directories"]["ai_work"])
        c.heading("[2/2] VS Code workspace")
        c.path(root / vscode_workspace_path(config))
        workspace = workspace_plan(root, config, state)
        rows = []
        for change in workspace["changes"]:
            if change["action"] != "reorder":
                folder = change["folder"]
                symbol = {"add": "+", "remove": "-", "change": "~"}[change["action"]]
                rows.append((symbol + " " + printable(folder.get("name", folder["path"])),
                             "(" + printable(folder["path"]) + ")"))
        c.columns(rows)
        for change in workspace["changes"]:
            action = change["action"]
            if action == "reorder":
                c.text("~ Root order will become:")
                for index, folder in enumerate(change["folders"], 1):
                    c.text(str(index) + ". " + printable(folder.get("name", folder["path"])), "    ")
                continue
            folder = change["folder"]
            if action == "change":
                c.text("Before: " + json.dumps(change["before"], ensure_ascii=True), "    ")
                c.text("After: " + json.dumps(folder, ensure_ascii=True), "    ")
        if not workspace["changed"]:
            c.heading("No changes")
            c.text("Workspace is up to date. No confirmation needed.")
        for warning in workspace["pending_manual"]:
            c.text("! " + printable(warning))
        if workspace["changed"]:
            c.blank()
            counts = {action: sum(change["action"] == action for change in workspace["changes"]) for action in ("add", "remove", "change", "reorder")}
            c.text("Plan: {add} to add, {remove} to remove, {change} to update, {reorder} order changes.".format(**counts))
            c.text("Only the folders list is updated. Settings and other workspace content are preserved. Manually added roots outside the inventory will be removed.")
            c.text("Apply the workspace changes shown above? Enter cancels.")
            c.blank()
            if action_prompt(input_fn, output) == "cancel":
                c.text("Workspace unchanged." + (" Registration changes remain saved; rerun to finish." if registration_saved else ""))
                return 0
            apply_workspace(root, config, state, workspace)
            c.text("Workspace folder list updated.")
        c.heading("Refresh completed", success=True)
        c.text("Review any warnings above. Missing entries keep their enabled/disabled selection unless explicitly removed.")
        return 0
    except KeyboardInterrupt:
        c.heading("Refresh interrupted")
        c.text("Review saved results before rerunning. Completed registration changes remain saved.")
        return 130
    except (WorkspaceError, OSError, ValueError, TypeError, KeyError, UnicodeError) as exc:
        c.heading("Refresh stopped")
        c.text(printable(exc))
        if registration_saved:
            c.text("Registration changes remain saved. Rerun after resolving the issue to finish the workspace update.")
        return getattr(exc, "code", 1)


def output_report(findings):
    return {"status": "errors" if any(x["severity"] == "error" for x in findings) else "structurally-valid",
            "ai_discovery": "not-certified", "findings": findings}


def show_report(report, command="validate", output=print):
    console = load_helper("terminal_output_formatter").Console(output)
    console.report(report, "Workspace audit" if command == "audit" else "Workspace validation", printable)
    return console


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=VERSION)
    subs = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "audit"):
        sub = subs.add_parser(command)
        sub.add_argument("--format", choices=("text", "json"), default="text")
        if command == "audit":
            sub.add_argument("--save-report", help="New relative path below .framework/reports")
    sub = subs.add_parser("refresh", help="Discover folders and refresh the VS Code folder list")
    mode = sub.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="Apply the preview noninteractively")
    mode.add_argument("--interactive", action="store_true", help="Review and confirm each phase")
    sub.add_argument("--remove-missing", action="store_true", help="Preview/apply removal of all missing entries; never deletes folders")
    ticket = subs.add_parser("ticket")
    ticket.add_argument("action", choices=("create", "archive", "restore"))
    ticket.add_argument("id")
    ticket.add_argument("--with", dest="optional", default="")
    ticket.add_argument("--description", help="Initial user-supplied details for a new brief; create only")
    return parser


def execute(args, ai_root=None):
    root, config, state = installed(ai_root or AI_ROOT)
    if args.command == "refresh":
        return refresh(root, config, state, args.apply, getattr(args, "remove_missing", False)), 0
    if args.command == "ticket":
        path = below(root, config["directories"]["ai_work"] + "/.github/skills/ca-jira-ticket-init/scripts/ticket.py")
        file_bytes(path, root)
        spec = importlib.util.spec_from_file_location("workspace_ticket", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        try:
            return module.perform(args.action, args.id, args.optional, script=path,
                                  description=getattr(args, "description", None)), 0
        except module.TicketError as exc:
            raise WorkspaceError(str(exc), exc.code) from exc
    findings = audit_root(root, config, state) if args.command == "audit" else validate_root(root, config, state)
    report = output_report(findings)
    if args.command == "audit" and args.save_report:
        dest = below(below(root, metadata(config, "reports")), args.save_report)
        if not dest.parent.is_dir():
            raise WorkspaceError("Saved report parent must already exist.", 2)
        exclusive(dest, json_bytes(report), root)
    return report, 1 if report["status"] == "errors" else 0


def main(argv=None):
    if sys.version_info < (3, 9):
        print("Python 3.9+ is required. Select an approved newer interpreter; no software has been installed.", file=sys.stderr)
        return 2
    args = build_parser().parse_args(argv)
    try:
        if args.command == "refresh" and args.interactive:
            if args.remove_missing:
                print("Use the remove-missing choice in the interactive registration preview.", file=sys.stderr)
                return 2
            return interactive_refresh()
        result, code = execute(args)
        if getattr(args, "format", "json") == "text" and "findings" in result:
            console = show_report(result, args.command)
            if args.command == "audit" and args.save_report:
                console.text("JSON report saved under .framework/reports/:")
                console.path(printable(args.save_report))
                console.blank()
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        return code
    except (WorkspaceError, OSError, ValueError, TypeError, KeyError) as exc:
        print("Error: " + str(exc), file=sys.stderr)
        return getattr(exc, "code", 1)


if __name__ == "__main__":
    raise SystemExit(main())
