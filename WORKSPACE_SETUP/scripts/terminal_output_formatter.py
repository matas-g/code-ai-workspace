"""Shared terminal formatting for setup, refresh and diagnostic reports."""
import os
import shutil
import sys
import textwrap
import unicodedata


class Console:
    """Readable plain text everywhere, with optional emphasis in a real terminal."""
    def __init__(self, output=print):
        self.output = output
        self.width = min(96, max(60, shutil.get_terminal_size((88, 24)).columns))
        self.color = os.name != "nt" and output is print and sys.stdout.isatty() and os.environ.get("TERM", "") not in ("", "dumb") and "NO_COLOR" not in os.environ

    def blank(self):
        self.output("")

    def heading(self, title, success=False):
        self.blank()
        line = title
        if self.color:
            line = ("\033[1;32m" if success else "\033[1;36m") + title + "\033[0m"
        self.output(line)
        self.output("-" * min(self.width, len(title)))
        self.blank()

    def text(self, value, indent="", subsequent=None):
        for line in textwrap.wrap(str(value), width=self.width, initial_indent=indent,
                                  subsequent_indent=indent if subsequent is None else subsequent,
                                  break_long_words=False, break_on_hyphens=False) or [""]:
            self.output(line)

    def path(self, value):
        # Preserve a complete copyable path; terminal soft-wrapping is harmless.
        self.output("  " + str(value))

    def columns(self, rows):
        """Align preview details without wrapping away their padding or names."""
        rows = list(rows)
        if not rows:
            return
        def width(value):
            return sum(0 if unicodedata.category(c) in ("Mn", "Me", "Cf") else
                       2 if unicodedata.east_asian_width(c) in ("W", "F") else 1
                       for c in value)
        left_width = max(width(left) for left, _ in rows)
        right_width = max(width(right) for _, right in rows)
        if left_width + 2 + right_width <= self.width:
            for left, right in rows:
                self.output(left + " " * (left_width - width(left) + 2) + right)
        else:
            # Preserve full names in narrow terminals; details share an indent.
            for index, (left, right) in enumerate(rows):
                if index:
                    self.blank()
                self.output(left)
                self.text(right, "    ")

    def field(self, label, value, description=""):
        self.text(label + " = " + str(value), "  * ", "    ")
        if description:
            self.text(description, "    ")
        self.blank()

    def report(self, report, title, clean=str):
        """Present diagnostics by urgency without changing their underlying data."""
        findings = report["findings"]
        groups = [("error", "Errors"), ("warning", "Warnings"),
                  ("pending-manual", "Manual checks"), ("info", "Notes")]
        counts = {severity: sum(item["severity"] == severity for item in findings)
                  for severity, _ in groups}
        self.heading(title)
        self.text("Result: " + ("Errors found" if report["status"] == "errors" else "Structurally valid"))
        self.blank()
        self.columns([("  " + label, str(counts[severity])) for severity, label in groups])
        self.blank()
        if counts["error"]:
            self.text("Resolve the errors below before treating setup as complete.")
        elif counts["warning"]:
            self.text("No structural errors. Review the warnings below.")
        else:
            self.text("No structural errors or warnings.")
        self.text("Copilot discovery: not certified; verify actual loading in VS Code.")

        editable_changes = {
            "Content differs from recorded baseline (local).": "Local configuration changed",
            "Content differs from recorded baseline (user).": "User file changed",
        }
        for severity, label in groups:
            items = [item for item in findings if item["severity"] == severity]
            if not items:
                continue
            self.heading(label + " (" + str(len(items)) + ")")
            changes = [item for item in items if severity == "info" and item["evidence"] in editable_changes]
            if changes:
                self.text("Changed since setup:")
                self.blank()
                self.columns([("  " + clean(item["path"]), editable_changes[item["evidence"]]) for item in changes])
                self.blank()
                self.text("Intentional edits to these files are normal, including repository registration and project context updates. No repair is needed for changes you made; review unexpected changes.")
            for item in items:
                if item in changes:
                    continue
                self.path(clean(item["path"]))
                self.text(clean(item["evidence"]), "    ")
                if item["remedy"]:
                    self.text("Next: " + clean(item["remedy"]), "    ")
                self.blank()
        self.blank()

