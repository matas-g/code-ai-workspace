# Release notes

For supported environments and workarounds that apply to this package, see [compatibility and known limitations](COMPATIBILITY.md).

## 0.1.22 — 1 November 2026

Ticket creation now verifies prepared files and publishes them without overwriting existing files. If creation is interrupted, a marker identifies the incomplete ticket. Follow **Ticket creation recovery** in the generated AI Work folder's `DAILY_WORK.md` before retrying creation, archiving or restoring it.

The new publication step requires local hard-link support. Existing workspaces keep their installed tools, and older unmarked partial briefs still need manual inspection. To adopt a newer package, follow the [setup guide](SETUP_GUIDE.md#troubleshooting-and-verification-limits).

## 0.1.21 — 1 November 2026

Maintenance release. Setup, daily tools, the Python 3.9+ requirement and the generated folder layout retain their 0.1.20 behavior.
