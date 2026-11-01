# Code AI Workspace — backlog index

[GitHub Issues](https://github.com/matas-g/code-ai-workspace/issues) owns imported status, priority and acceptance checklists. Use the few [issues marked next](https://github.com/matas-g/code-ai-workspace/issues?q=is%3Aissue%20is%3Aopen%20label%3Anext); ordinary Open/Closed issues and `bug`, `improvement`, `verification`, `next` labels are sufficient.

Current scope: **macOS pilot**. Manually installed, approved **Python 3.12+** is agreed for the next pilot but remains unimplemented in #11; current source requires 3.9+. This index retains legacy mappings and deferred scope without duplicating a live queue. Original scope and review are preserved in the [pre-migration backlog](https://github.com/matas-g/code-ai-workspace/blob/f79573520f8f6c71c80947b84fb5d26fb2b06a02/maintenance/BACKLOG.md) and [dated review](https://github.com/matas-g/code-ai-workspace/blob/f79573520f8f6c71c80947b84fb5d26fb2b06a02/maintenance/BACKLOG_REVIEW.md).

## Legacy item index

| ID | Issue or disposition |
|---|---|
| B01 | [#1 — Test write guard](https://github.com/matas-g/code-ai-workspace/issues/1); [#2 — Checkout bytes](https://github.com/matas-g/code-ai-workspace/issues/2). |
| B02 | [#3 — Unselected ticket reads](https://github.com/matas-g/code-ai-workspace/issues/3). |
| B03 | [#4 — Interrupted creation](https://github.com/matas-g/code-ai-workspace/issues/4); [#5 — Transfer permissions](https://github.com/matas-g/code-ai-workspace/issues/5). |
| B04 | [#6 — Approved refresh, custom-path summaries and recovery](https://github.com/matas-g/code-ai-workspace/issues/6). |
| B05 | [#7 — Installation snapshot](https://github.com/matas-g/code-ai-workspace/issues/7); builder snapshot belongs to B12/#13. |
| B06 | [#8 — Literal multiline invocation](https://github.com/matas-g/code-ai-workspace/issues/8). |
| B07 | [#9 — Readable optional Python reference](https://github.com/matas-g/code-ai-workspace/issues/9). |
| B08 | Reconciled into [B14/#15](https://github.com/matas-g/code-ai-workspace/issues/15): B21 removed the failing template entry path from current onboarding. Historical BUG-06/DOC-05 stays FAIL for 0.1.19; identify a verified candidate and shipment before claiming the published package is fixed. |
| B09 | [#10 — Optional-example, link and CRLF validation](https://github.com/matas-g/code-ai-workspace/issues/10); broader parsing deferred. |
| B10 | [#11 — Approved Python 3.12+ requirement](https://github.com/matas-g/code-ai-workspace/issues/11). |
| B11 | [#12 — Narrow output and repeatable macOS launcher checks](https://github.com/matas-g/code-ai-workspace/issues/12); Windows/CI expansion deferred. |
| B12 | [#13 — Read-only release checks, builder snapshot and safe ZIP/checksum publication](https://github.com/matas-g/code-ai-workspace/issues/13). |
| B13 | [#14 — Remaining native macOS candidate verification](https://github.com/matas-g/code-ai-workspace/issues/14). |
| B14 | [#15 — Independent first-use macOS journey](https://github.com/matas-g/code-ai-workspace/issues/15), including B08; unavailable sign-in/policy branches remain unverified. |
| B15 | Deferred: public-release licensing, contribution/support and publication/history review. |
| B16 | Deferred: concrete contract/recovery/diagnostic improvements; fix-specific recovery stays with its fix. |
| B17 | Deferred: broad maintenance/refactoring/tooling. |
| B18 | Deferred: optional skill/context/brief/example improvements; defect-specific text stays with its fix. |
| B19 | Reconciled: B21 delivered document ownership, settings-default corrections and validation summary. Old refresh-unreleased wording is historical; no named current mismatch remains. Optional navigation/history restructuring deferred. |
| B20 | Deferred: another IDE only for an actual user need and available installation. |
| B21 | Completed 31 October 2026: user-only packaging/document separation; [recorded evidence](VALIDATION_REPORT.md#unreleased-user-package-separation--31-october-2026). No new GUI/Copilot/Windows pass or active issue. |

## Deferred scope

Promote a concrete outcome to an issue when useful, then replace its deferred note with the link. Detailed proposals remain in [QUALITY_IMPROVEMENT_PLAN.md](QUALITY_IMPROVEMENT_PLAN.md).

- **Windows** (B03/B11/B13/B14; R03/R06/R07/R14/R19/R26): ACL/inheritance, discovery, reparse/paths, input/encoding/redirection, GUI closure, minimum/latest Python and all 24 Windows manual rows remain unqualified. Broader CI can wait; macOS results never establish Windows coverage.
- **Public release** (B15/R25): owner-selected terms for distributed/generated assets, contribution/reporting/support scope and publication-set/history review.
- **Contracts/recovery** (B16; R12/R13/R26): nested-schema errors, original-error preservation, read-only known-marker status, lock metadata and exit/JSON/encoding contracts. Types/durability need a concrete use case; no private-attachment audit scans or automatic ambiguous recovery.
- **Maintenance** (B17; R11/R16/R24): explicit imports/loading, incremental extraction, unittest organization, reusable runner/fixtures and optional pinned tools only when useful. Preserve offline portability and installer independence.
- **Content** (B18; R20–R23): evidence-based review/audit output, verified context guidance, brief-only validation and clearly fictional examples. Keep short orientation, one required brief and optional resources.
- **Parsing** (B09; R09/R10): broader Markdown/YAML/BOM/JSONC cases, pre-read limits and bounded traversal. These inspection proposals do not block #10’s confirmed fixes; preserve unknown workspace bytes and report unsupported syntax honestly.
- **Navigation/history** (B19/R18): restructure only for a named usability problem; preserve historical evidence.
- **Other IDEs** (B20/OTHER-IDE-01): test manual imports/shared files and Copilot features independently if adopted; no automatic metadata, installation or parity claim.

## Evidence

[MANUAL_TESTS.md](MANUAL_TESTS.md) owns actual environment-specific observations; [VALIDATION_REPORT.md](VALIDATION_REPORT.md) owns automated/release evidence. Fix-specific retests stay with fixes; #14/#15 cover residual native/integrated/first-use checks. Preserve historical outcomes, identify exact candidates/artifacts and name unavailable environments. A scoped macOS pilot does not require every deferred platform/publication proposal. Contributor guarantees and verification/release commands remain in [AGENTS.md](../AGENTS.md) and [DEVELOPMENT.md](DEVELOPMENT.md).
