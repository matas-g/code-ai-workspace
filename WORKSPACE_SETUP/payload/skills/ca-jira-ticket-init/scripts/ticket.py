#!/usr/bin/env python3
"""Self-contained local ticket operations; no Jira/Git/network integration."""
import sys
sys.dont_write_bytecode = True

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat

TRANSFER_MARKER = ".ticket-transfer-incomplete.json"


class TicketError(Exception):
    def __init__(self, message, code=1):
        super().__init__(message)
        self.code = code


def present(path):
    return os.path.lexists(path)


def safe(path, root=None):
    path = Path(path)
    if os.name == "nt" and path.drive.startswith("\\"):
        raise TicketError("UNC/network locations are not supported.", 2)
    if not path.is_absolute() or ".." in path.parts or (root is not None and not path.is_relative_to(root)):
        raise TicketError("Path escapes ticket scope.", 2)
    for part in list(reversed(path.parents)) + [path]:
        if present(part):
            info = part.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
                raise TicketError("Redirected ticket path refused: " + str(part), 2)
            if part != path and not stat.S_ISDIR(info.st_mode):
                raise TicketError("Ticket path parent is not a directory.", 2)
    return path


def ordinary(path, kind):
    mode = path.lstat().st_mode
    return stat.S_ISREG(mode) if kind == "file" else stat.S_ISDIR(mode)


def write_new(path, data, root):
    with safe(path, root).open("xb") as stream:
        stream.write(data)


def snapshot(folder, root):
    safe(folder, root)
    files, directories = {}, []
    def walk(directory):
        for child in sorted(safe(directory, root).iterdir()):
            safe(child, root)
            rel = child.relative_to(folder).as_posix()
            if child.name == TRANSFER_MARKER:
                raise TicketError("Incomplete transfer marker found; reconcile the ticket manually.")
            if ordinary(child, "directory"):
                directories.append(rel)
                walk(child)
            elif ordinary(child, "file"):
                before = child.stat()
                h = hashlib.sha256()
                with child.open("rb") as stream:
                    for data in iter(lambda: stream.read(1024 * 1024), b""):
                        h.update(data)
                after = child.stat()
                signature = lambda s: (s.st_size, s.st_mtime_ns, s.st_ino, s.st_dev)
                if signature(before) != signature(after):
                    raise TicketError("Source changed during inspection; nothing removed.")
                files[rel] = h.hexdigest()
            else:
                raise TicketError("Non-ordinary ticket entry refused: " + rel)
    walk(folder)
    return files, sorted(directories)


def move_ticket(source, dest, root):
    """Reserve destination, copy and verify all bytes, then prune source.

    A partial failure keeps the verified copy and remaining source plus a marker.
    No operation replaces a pre-existing destination. No automatic rollback deletion.
    """
    files, dirs = snapshot(source, root)
    safe(dest, root).mkdir()  # exclusive reservation
    marker = dest / TRANSFER_MARKER
    try:
        write_new(marker, json.dumps({"source": source.relative_to(root).as_posix(), "status": "incomplete"}).encode(), root)
        for rel in sorted(dirs, key=lambda x: (len(Path(x).parts), x)):
            safe(dest / rel, root).mkdir()
        for rel, expected in files.items():
            src = safe(source / rel, root)
            dst = safe(dest / rel, root)
            h = hashlib.sha256()
            with src.open("rb") as inp, dst.open("xb") as out:
                for data in iter(lambda: inp.read(1024 * 1024), b""):
                    out.write(data)
                    h.update(data)
            if h.hexdigest() != expected:
                raise TicketError("Source changed during transfer; inspect both locations.")
        # Destination verification must ignore only our own reserved marker.
        for rel, expected in files.items():
            h = hashlib.sha256()
            with safe(dest / rel, root).open("rb") as stream:
                for data in iter(lambda: stream.read(1024 * 1024), b""):
                    h.update(data)
            if h.hexdigest() != expected:
                raise TicketError("Destination verification failed; source retained.")
        if snapshot(source, root) != (files, dirs):
            raise TicketError("Source changed; reconcile both copies manually.")
        for rel, expected in files.items():
            src = safe(source / rel, root)
            h = hashlib.sha256()
            with src.open("rb") as stream:
                for data in iter(lambda: stream.read(1024 * 1024), b""):
                    h.update(data)
            if h.hexdigest() != expected:
                raise TicketError("Source changed before cleanup; reconcile both locations manually.")
            src.unlink()
        for rel in sorted(dirs, key=lambda x: (len(Path(x).parts), x), reverse=True):
            safe(source / rel, root).rmdir()
        safe(source, root).rmdir()
        safe(marker, root).unlink()
    except (OSError, TicketError) as exc:
        raise TicketError("Transfer incomplete. Inspect source and destination; do not delete either without reconciling the marker. Cause: " + str(exc)) from exc


def render_template(text, filename, ticket_id, description):
    """Resolve template fields before inserting literal user-supplied details."""
    text = text.replace("{{ticket_id}}", ticket_id)
    slot = "{{initial_description}}"
    checked = text.replace(slot, "") if filename == "brief.md" else text
    if "{{" in checked or "}}" in checked:
        raise TicketError("Unresolved ticket template field.")
    if filename != "brief.md":
        return text
    initial = ("Initial details supplied by user (not yet refined):\n\n" + description +
               "\n\nJira link: not yet recorded.") if description else "Not yet recorded. Jira link: not yet recorded."
    if slot in text:
        return text.replace(slot, initial)
    # Older/custom user templates may not have the new field. Preserve their
    # content and append the supplied details rather than silently losing them.
    if description:
        return text.rstrip("\n") + "\n\n## Initial details supplied by user\n\n" + description + "\n"
    return text


def perform(action, ticket_id, optional="", script=None, description=None):
    script = Path(script or __file__).absolute()
    safe(script)
    if script.parent.name != "scripts" or script.parents[1].name != "ca-jira-ticket-init" or script.parents[2].name != "skills" or script.parents[3].name != ".github":
        raise TicketError("Run the installed ticket script, not the package payload copy.", 2)
    root = script.parents[4]
    initialized_root = root.parent
    safe(initialized_root)
    if present(initialized_root / ".initialization-incomplete.json"):
        raise TicketError("Initialization incomplete; inspect it manually.", 3)
    state_path = safe(root / ".framework/installed-state.json", initialized_root)
    if not present(state_path) or not ordinary(state_path, "file"):
        raise TicketError("No completed framework state found.", 2)
    try:
        state = json.loads(state_path.read_bytes())
        if state.get("initialization_status") != "complete" or state.get("directory_names", {}).get("ai_work") != root.name:
            raise TicketError("Incomplete or mismatched framework state.", 2)
    except (ValueError, AttributeError) as exc:
        raise TicketError("Invalid framework state.", 2) from exc
    skill = script.parents[1]
    if not isinstance(ticket_id, str) or not re.fullmatch(r"[A-Z][A-Z0-9]{0,19}-[1-9][0-9]{0,9}", ticket_id):
        raise TicketError("Invalid ticket ID; expected e.g. ABC-1234.", 2)
    chosen = optional.split(",") if optional else []
    if len(set(chosen)) != len(chosen) or set(chosen) - {"plan", "review", "notes", "files"}:
        raise TicketError("--with accepts unique comma-separated plan,review,notes,files.", 2)
    if action not in ("create", "archive", "restore") or (action != "create" and chosen):
        raise TicketError("Optional resources apply only to create.", 2)
    if description is not None:
        if action != "create":
            raise TicketError("--description applies only to create.", 2)
        if not isinstance(description, str) or any(ord(c) < 32 and c not in "\n\r\t" or ord(c) == 127 for c in description):
            raise TicketError("Description must be text without control characters other than tabs/newlines.", 2)
        if not description.strip():
            description = None
    tickets = safe(root / "tickets", root)
    for state in ("active", "archive"):
        folder = safe(tickets / state, root)
        if not folder.is_dir():
            raise TicketError("Required ticket directory missing; validate the installation first.")
    active, archive = safe(tickets / "active" / ticket_id, root), safe(tickets / "archive" / ticket_id, root)
    lock = tickets / ".ticket-operation.lock"
    try:
        write_new(lock, (action + " " + ticket_id + "\n").encode(), root)
    except FileExistsError as exc:
        raise TicketError("Another ticket operation is running, or a stale lock requires manual inspection.") from exc
    try:
        for path in (active, archive):
            safe(path, root)
            if present(path):
                if not ordinary(path, "directory"):
                    raise TicketError("Ticket location is not an ordinary directory.")
                if present(path / TRANSFER_MARKER):
                    raise TicketError("Incomplete transfer; reconcile both locations manually.")
        if present(active) and present(archive):
            raise TicketError("Ticket exists in both active and archive; no merge performed.")
        if action == "create":
            if present(archive):
                raise TicketError("Ticket is archived; use explicit restore.")
            desired = ["brief.md"] + [x + ".md" for x in chosen if x != "files"]
            data = {}
            for filename in desired:
                path = safe(active / filename, root)
                if present(path):
                    if not ordinary(path, "file"):
                        raise TicketError("Expected file at " + filename)
                else:
                    template = safe(skill / "templates" / filename, skill)
                    if not present(template) or not ordinary(template, "file"):
                        raise TicketError("Missing ordinary template: " + filename)
                    text = render_template(template.read_text(encoding="utf-8"), filename, ticket_id, description)
                    data[filename] = text.encode("utf-8")
            if "files" in chosen:
                files = safe(active / "files", root)
                if present(files) and not ordinary(files, "directory"):
                    raise TicketError("Expected files/ directory.")
            created, existing = [], []
            if not present(active):
                active.mkdir()
                created.append(ticket_id + "/")
            for filename in desired:
                if filename in data:
                    write_new(active / filename, data[filename], root)
                    created.append(filename)
                else:
                    existing.append(filename)
            if "files" in chosen:
                if present(active / "files"):
                    existing.append("files/")
                else:
                    safe(active / "files", root).mkdir()
                    created.append("files/")
            result = {"status": "created" if created else "already-present", "ticket": ticket_id, "created": created, "already_present": existing}
            if description:
                result["description_status"] = "captured" if "brief.md" in data else "preserved-existing-brief"
            return result
        source, dest = (active, archive) if action == "archive" else (archive, active)
        if not present(source):
            if present(dest):
                return {"status": "already-archived" if action == "archive" else "already-active", "ticket": ticket_id}
            raise TicketError("Ticket not found.")
        move_ticket(source, dest, root)
        return {"status": "archived" if action == "archive" else "restored", "ticket": ticket_id}
    finally:
        safe(lock, root).unlink()


def main(argv=None):
    if sys.version_info < (3, 9):
        print("Python 3.9+ is required; no software was installed.", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("create", "archive", "restore"))
    parser.add_argument("id")
    parser.add_argument("--with", dest="optional", default="")
    parser.add_argument("--description", help="Initial user-supplied details for a new brief; create only")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(perform(args.action, args.id, args.optional, description=args.description), indent=2))
        return 0
    except (TicketError, OSError, UnicodeError) as exc:
        print("Error: " + str(exc), file=sys.stderr)
        return getattr(exc, "code", 1)


if __name__ == "__main__":
    raise SystemExit(main())
