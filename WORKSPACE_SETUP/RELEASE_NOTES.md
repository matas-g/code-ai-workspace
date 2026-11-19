# Release notes

For supported environments and workarounds that apply to this package, see [compatibility and known limitations](COMPATIBILITY.md).

## 0.1.23 — 19 November 2026

- New workspaces include editable branch-name and commit-message examples in the project overview. Use the overview to record conventions for each repository.
- The installation package includes the MIT license. Setup also places a copy beside the installed daily tools.
- The [compatibility guide](COMPATIBILITY.md) collects platform limits, known issues and workarounds.

Existing workspaces keep their installed files. To adopt just the naming guidance, copy the relevant examples into your project overview. For the complete package, follow the [setup guide](SETUP_GUIDE.md#troubleshooting-and-verification-limits).

## 0.1.22 — 1 November 2026

Ticket creation now verifies prepared files and publishes them without overwriting existing files. If creation is interrupted, a marker identifies the incomplete ticket. Follow **Ticket creation recovery** in the generated AI Work folder's `DAILY_WORK.md` before retrying creation, archiving or restoring it.

The new publication step requires local hard-link support. Existing workspaces keep their installed tools, and older unmarked partial briefs still need manual inspection. To adopt a newer package, follow the [setup guide](SETUP_GUIDE.md#troubleshooting-and-verification-limits).

## 0.1.21 — 1 November 2026

Maintenance release. Setup, daily tools, the Python 3.9+ requirement and the generated folder layout retain their 0.1.20 behavior.
