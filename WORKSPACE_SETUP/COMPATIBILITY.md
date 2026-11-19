# Compatibility and known limitations

These limits apply to the version shown by the setup launcher. For changes between versions, see the [release notes](RELEASE_NOTES.md).

## Compatibility

- **Operating systems.** This is a macOS pilot. Native Windows 11 compatibility and some native launcher and terminal behavior still need verification.
- **Python and filesystem.** Setup and daily tools require a manually installed Python 3.9 or later. Ticket creation requires a local filesystem that supports hard links.
- **VS Code and Copilot.** Recorded macOS checks cover Copilot Local context loading, skill use, custom folder names, relocation and daily workflows. Check discovery in your own VS Code and Copilot versions, account and policy settings. Structural validation alone cannot establish that Copilot loaded an instruction or skill.
- **Other editors.** Shared files and Python tools work independently of VS Code. Project import and Copilot integration need separate testing in each editor.

## Known issues and workarounds

- **Copilot ticket context.** Copilot has read an unselected ticket and flattened multiline requirements during ticket creation. Select or attach the intended brief and check its contents before coding. Repeating ticket creation preserves the existing brief. Ask for a separate edit to correct captured requirements.
- **Refresh through chat.** Chat can report default paths for a renamed workspace or omit the recovery reminder. The apply command is not tied to a specific earlier chat preview. Use the generated root refresh launcher to review and apply changes. If a change to the first workspace folder interrupts chat, reopen the launcher to inspect the result and finish the refresh.
- **Interrupted ticket creation.** Version 0.1.22 detects newly interrupted creates. In 0.1.21 and earlier, an interruption could leave an unmarked partial brief that a repeat create accepts as existing. Inspect older partial briefs manually. For a marked ticket, follow **Ticket creation recovery** in the generated AI Work folder's `DAILY_WORK.md`.
- **Ticket transfers.** Archive and restore preserve file contents but can broaden restrictive permissions. Check the required permissions on transferred attachments, including any access control lists. If a transfer fails, inspect both ticket locations before continuing.
- **Reading terminal commands.** Some Markdown editors display the daily guide's optional command section as literal HTML. Use Markdown Preview or read the Markdown source.
- **Package edits and audits.** Edit settings before launching setup and keep package inputs unchanged during preview and creation. Audit can misclassify some Markdown links and skill metadata, including frontmatter with CRLF line endings. If you remove the optional knowledge example, remove its README link too. Review findings before making corrections.
- **Source downloads.** A Git checkout that converts line endings can fail exact-byte integrity checks. Use the prepared installation ZIP when available.

For prerequisites, installation and troubleshooting, see the [setup guide](SETUP_GUIDE.md).
