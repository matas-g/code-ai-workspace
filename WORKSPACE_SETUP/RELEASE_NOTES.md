# Compatibility and known limitations

Find the package version in the enclosing [README](../README.md) or the setup output. Follow the [setup guide](SETUP_GUIDE.md) for installation and troubleshooting.

## Changes in 0.1.22

- Ticket creation now marks incomplete operations and verifies prepared files before publishing them without overwriting existing files. A marked ticket requires manual reconciliation before create/archive/restore can continue; the generated daily guide explains recovery.
- File publication requires local hard-link support. Existing workspaces retain their installed tools; older unmarked partial briefs still require manual inspection. This change does not add automatic repair or upgrades.

## Changes in 0.1.21

- Maintenance release. Setup and daily runtime behavior, Python 3.9+ compatibility and the generated folder layout are unchanged from 0.1.20.
- Existing generated folders are not automatically upgraded. The known limitations below remain applicable.

## Compatibility

- This is a **macOS pilot**. Native Windows 11 compatibility and some native launcher/terminal behavior remain unverified. Python 3.9+ is the current package minimum; installation is manual.
- Recorded macOS checks include VS Code/Copilot Local context loading, skill use, custom names, relocation and daily workflows. Features still depend on the actual VS Code/Copilot version, account and applicable policy; a structural audit does not certify them.
- Other editors can use shared files and Python tools. Their project import and Copilot features need separate testing.

## Known issues and workarounds

- **Copilot context and ticket details:** Copilot has read an unselected ticket during a project question and flattened a multiline description during ticket creation. Select or attach the intended brief explicitly and inspect captured requirements before coding. Repeating initialization preserves an existing brief and does not add new details; request a separate requirements edit when needed.
- **Refresh through chat:** A chat summary can use default names despite custom paths, and omit the launcher-recovery reminder. Apply is not yet bound to a particular prior chat preview. Prefer the generated root refresh launcher for reviewed updates. Changing the first workspace root may restart extensions and interrupt chat; the launcher can inspect current state and finish remaining work.
- **Ticket failures and permissions:** In the published 0.1.21 package and older installations, interrupted creation can leave a partial brief that a repeat treats as existing. Version 0.1.22 detects newly interrupted creation; it cannot identify older unmarked partial files. Transfers preserve contents but can broaden restrictive permission bits; ACL/metadata guarantees are limited. Inspect incomplete work and both locations after a failed transfer, and verify required access restrictions before relying on transferred attachments. Commands do not repair ambiguous partial results automatically.
- **Optional terminal commands:** Some Markdown editor views display the daily guide's HTML disclosure literally. Use Markdown Preview or the document's source view to read the optional Python reference; the direct commands remain available.
- **Package edits and audits:** Keep setup inputs unchanged during preview/creation, apart from settings edited before launching. Some Markdown/frontmatter forms, including CRLF skill metadata, can be misclassified by audit. Deleting the optional knowledge example also requires removing its README link. Review findings before making manual changes; no automatic repair is performed.
- **Source downloads:** A Git checkout with converted line endings can fail exact-byte package integrity checks. Use the prepared installation ZIP when available; source copies also include development files.

## Installation and daily use

Setup creates a new development folder and refuses existing targets. Daily tools and generated guides work after that complete folder is moved and the installer is removed. Existing generated folders are not automatically upgraded; use a fresh destination and transfer permitted content manually when adopting a newer package.
