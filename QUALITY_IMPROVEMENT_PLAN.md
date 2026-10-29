# Code AI Workspace — implementation review and improvement plan

**Reviewed:** 29 October 2026  
**Baseline:** 0.1.18, commit `20e04c7`  
**Status:** Review and proposed work only. No implementation, configuration, template, version, release, or historical test-record changes were applied.

## 1. Assessment and recommendation

The solution has a sound foundation for a small portable developer tool. Standard-library Python, an offline installer, separate installed runtime, explicit release inventory, relative paths, refusal to overwrite existing installations, and CLI-backed skills are appropriate choices. The current release and its recorded limitations are substantially more careful than a typical prototype.

The strongest improvement is to close specific reliability gaps and make verification reproducible for contributors. A framework rewrite, package manager, service, database, custom VS Code extension, or mandatory AI integration would add more maintenance than value here.

Recommended order:

1. Fix package line-ending stability, incomplete ticket creation, archive permissions, refresh approval binding, and integrity-check snapshot consistency.
2. Establish supported Python versions and native-platform CI, strengthen the test boundary checker, and finish the release verification workflow.
3. Make small architectural improvements around explicit imports, typed contracts, diagnostics, and failure recovery.
4. Improve skills, context templates, and documentation using reproducible synthetic examples and actual IDE evidence.
5. Add the small amount of repository metadata needed for public collaboration and intentional reuse.

The existing pilot label is appropriate. Passing the current suite does not establish native Windows compatibility, complete Copilot discovery, or freedom from the defects reproduced below.

## 2. Scope, method, and actual evidence

### Material reviewed

- All current tracked source, configuration, launchers, instructions, skills, templates, examples, tests, and maintainer/product documents. The tracked inventory contains 53 files, including the current ZIP and checksum.
- Every Python file: six installer/runtime/release modules, the ticket helper, and the behavioral test suite.
- All six `ca-` skills and their resources; both Copilot instruction templates; project, ticket, and knowledge templates; configuration examples and ignore rules.
- The current release ZIP, its member bytes, manifest hashes, checksum, root README mirror, and design mirror.
- Current official documentation for time-sensitive Python support and VS Code customization behavior, plus relevant Git and GitHub guidance, linked beside recommendations below.

Historical archives in `_old zips/`, existing scratch work in `_tmp/`, and the full Git history were not treated as current implementation inputs. This was not a separate complete Git-history secret audit. The two design copies contain identical bytes, so the substantive design was reviewed once.

### Verification performed for this review

All execution used synthetic fixtures in an isolated copy beneath `_tmp/quality-review-20261029-ycyr5e48/`. Existing project files and the published artifact were not rewritten.

| Check | Actual result |
|---|---|
| Existing suite, Python 3.15.0, macOS 26.6.2, Apple Silicon | 98 tests passed; 18.699 seconds |
| Existing suite, Python 3.9.6, same machine | 98 tests passed; 23.657 seconds |
| Current ZIP integrity | Passed; 47 members |
| ZIP payload bytes compared with current manifest source files | No differences |
| Current source hashes and ZIP SHA-256 sidecar | All match |
| Root README and design mirrors | Both match their prepared package sources |
| Focused failure/concurrency/format checks | Confirmed the cases in the next table |
| Native Windows, Finder interaction, VS Code/Copilot sessions | Not exercised; existing manual statuses remain unchanged |

Suite commands, run serially:

```sh
python3 -I -S -B _tmp/quality-review-20261029-ycyr5e48/WORKSPACE_SETUP/tests/test_workspace.py
/usr/bin/python3 -I -S -B _tmp/quality-review-20261029-ycyr5e48/WORKSPACE_SETUP/tests/test_workspace.py
```

Local evidence files are `python315-tests.log`, `python39-tests.log`, `reproductions.json`, `additional-checks.json`, `guard-checks.json`, and `permission-check.json` under that review directory. They are temporary development evidence, excluded from Git and releases; the results above and below are the durable review summary. No manual IDE pass was inferred and `MANUAL_TESTS.md` was not changed.

### Confirmed gaps

| ID | Reproduction | Observed behavior |
|---|---|---|
| R01 | Convert an immutable source file from LF to CRLF without changing its text | Setup refuses it with `Package integrity mismatch: CHANGELOG.md`. No target is created. Git attributes do not currently fix checkout endings. |
| R02 | Inject a write failure after writing part of a new `brief.md`; retry create | The truncated file remains. Retry returns `already-present` and preserves the incomplete brief as though creation had completed. |
| R03 | Archive a ticket with a `0600` attachment inside a `0700` directory, under umask `022` | Destination becomes `0644` and `0755`; the source is removed. Restrictive permissions are broadened. |
| R04 | Preview with one new repository, add another, then invoke `refresh --apply` | Both are registered; apply is not bound to the prior preview. A second injected case restored an enabled missing folder between apply phases and the new workspace plan included it. |
| R05 | Change an asset between its hash check and the installer's second read | The unverified bytes enter the deployment plan. Changing an asset after the builder's final manifest calculation also produces a successful ZIP with a mismatched member hash. |
| R08 | Remove the explicitly optional synthetic knowledge example | Validation reports an error for the remaining example link in `KNOWLEDGE_BASE/README.md`. |
| R09 | Put a link-looking example inside inline Markdown code | Validation treats it as a real missing link and reports a deterministic error. A malformed URL in an audited `AGENTS.md` aborts the audit with `ValueError` instead of producing a complete findings report. |
| R10 | Save an installed user-owned skill with CRLF endings | Its metadata fails with `Missing YAML frontmatter.` despite unchanged frontmatter content. |
| R15 | Feed synthetic traversal and symlink audit events to the suite's guard | It accepts a lexical `scope/../outside` write path and checks a symlink's source instead of its destination. No actual outside write was performed. |

Fault injection makes these failure windows deterministic; it does not establish their real-world frequency. The snapshot issues are consistency defects in a trusted local workflow, not evidence of a remote exploit or an OS sandbox failure.

## 3. Priorities and retained design choices

- **P1:** Address before the next wider external pilot or stronger reliability claim.
- **P2:** Valuable quality work after the immediate fixes; complete before calling the implementation broadly mature.
- **P3:** Optional polish, driven by actual user feedback.
- **Confirmed:** Reproduced during this review.
- **Inspection:** Supported directly by source structure or missing repository configuration.
- **Verification gap:** Needs the specified environment or experiment; not a claim that the feature fails.

Keep these existing choices:

- Offline, standard-library-only installation and daily commands; no automatic prerequisites, authentication, clones, or global settings.
- New-directory-only initialization and independently portable daily tools.
- Explicit allowlists, relative generated paths, user-owned context, preserved edits, and refusal to merge ticket collisions.
- Minimal explicit skills with `ca-` names, normal tool approvals, relevant context loading, and direct-command fallbacks.
- Honest separation of structural checks from IDE discovery and organizational approval.
- Fresh-install/manual-transfer upgrade policy until real demand justifies an updater.

The runtime's independent expected-layout check is useful defense against accidental deployment mapping changes. Do not replace it with blind trust in a generated manifest while reducing duplication elsewhere.

## 4. Reliability and platform work

### R01 — Make checkout and release line endings deterministic

**Priority/evidence:** P1; confirmed failure plus inspection.  
**Locations:** missing root `.gitattributes`; `workspace.py:52–83`; package hashes; all launchers and Markdown/Python inputs.

The README supports both source clones/downloads and release extraction. Exact-byte hashes currently depend on a contributor's Git checkout behavior. A source checkout with line-ending conversion can fail before setup starts creating files. Git's `text` and `eol` attributes provide repository-level control over checkout endings. [Git attributes documentation](https://git-scm.com/docs/gitattributes).

**Proposed work:**

- Add explicit attributes: LF for Python, JSON, Markdown, SVG, shell launchers, ignore files and checksums; exact-byte handling for ZIPs and the existing CRLF `.cmd` files.
- For `.cmd`, prefer preserving the current CRLF blob bytes with `-text` and checking their endings during release verification. Merely setting `text eol=crlf` normalizes stored blobs to LF, so source archives and working-tree files can still differ. Alternatively, adopt canonical LF only after proving native launcher compatibility. The acquisition methods must agree on the hashed bytes.
- Normalize affected tracked content once, rebuild manifest hashes through the approved builder, and review that diff separately from functional changes.
- Define the release builder's input-byte policy and verify it before hashing. Do not make integrity checking silently normalize tampered bytes.
- Test fresh checkouts with `core.autocrlf=true`, `false`, and `input`, plus a GitHub source archive and the release ZIP. Use native Windows for the corresponding execution checks.

**Acceptance:** All supported acquisition paths initialize without asking users to rebuild hashes. The same reviewed source produces the same member bytes. Actual immutable content changes still fail integrity checks.

### R02 — Detect interrupted ticket creation

**Priority/evidence:** P1; confirmed.  
**Locations:** `ticket.py:48–50`, `152–246`.

Exclusive creation prevents overwriting another file, but does not make the file's contents complete. A failed write can leave a normal-looking partial brief that subsequent invocations deliberately preserve.

**Proposed work:**

- Introduce an explicit creation-in-progress record before publishing newly requested ticket files; identify the intended resources without storing duplicate private descriptions.
- Ensure a failed write or interrupted operation leaves a detectable incomplete state. Retry must report that state instead of returning normal `already-present` success.
- Prefer preparing and verifying complete bytes before publication. Any staging/publish method must preserve the current no-overwrite contract on both platforms; do not substitute unconditional `os.replace` over a potentially existing user file.
- Keep the distinction between a completed existing user brief and an incomplete framework creation. Never infer that an intentionally edited brief is corrupt merely because its content differs from a template.
- Report which resources completed and how to inspect/reconcile the remainder. Do not automatically delete partially created user work.

**Acceptance:** Inject failures during brief and optional-resource writes, and interrupts at each completion boundary. No truncated file is later reported as successful completed initialization; existing user bytes remain intact; cleanup never escapes the ticket scope.

### R03 — Preserve restrictive permissions during ticket transfers

**Priority/evidence:** P1; confirmed on macOS.  
**Locations:** `ticket.py:82–129`.

The byte-preserving transfer recreates files and directories using default permissions. This can broaden access when archiving or restoring manually restricted material. Content preservation and filesystem metadata preservation need separate contracts.

**Proposed work:**

- Reserve new destination directories and files with restrictive initial permissions where supported, so a partial copy is not temporarily more accessible.
- Preserve ordinary source permission bits where appropriate; do not copy privileged mode bits or claim ownership/ACL/xattr equivalence without implementing and testing it.
- Define and document the native Windows ACL/inheritance behavior. Fail or report limitations when the promised access properties cannot be maintained.
- Decide whether preserving modification times is useful for attachments; keep that separate from the required restriction-preservation fix.
- Retain exclusive destination reservation, streamed hashing, collision refusal, and marked partial recovery.

**Acceptance:** Archive/restore restricted files and directories under permissive and restrictive umasks. Verify content, access restrictions, and failure recovery. Native Windows evidence must address ACL behavior independently.

### R04 — Bind noninteractive apply to the approved refresh plan

**Priority/evidence:** P1; confirmed.  
**Locations:** `workspace_manager.py:588–675`; `ca-workspace-refresh/SKILL.md`, procedure steps 1–3.

The interactive path rechecks its in-memory phase plans. The chat skill, however, previews in separate processes and then applies a freshly computed plan. Repeating preview reduces the race window but does not enforce the skill's promise that changed proposals require renewed approval. Apply also discards its original workspace preflight and computes another plan after saving registration.

**Proposed work:**

- Return a deterministic plan identifier covering the target, relevant configuration/state/workspace bytes, observed folders, effective options, and proposed changes.
- Add an apply precondition such as `--expected-plan DIGEST`. Require it for the chat skill. Keep a plainly documented direct `--apply` workflow if users intentionally want to apply current state without a previous preview.
- Recheck the approved plan under the maintenance lock immediately before mutation. Detect changes between phases instead of silently broadening the workspace update.
- Preserve separately durable registration/workspace semantics where intentional. If registration already completed before a later failure, report that fact and require a fresh preview for the remaining phase.
- Update skill text, JSON output, help, design, and manual recovery guidance together.

**Acceptance:** Change a folder, selection, label, option, workspace byte, or state between preview and apply; apply refuses unapproved changes. Also test a returning enabled folder between phases, no-op plans, relocation, and interrupted chat recovery.

### R05 — Hash and use one immutable source snapshot

**Priority/evidence:** P1; confirmed by deterministic injected edits.  
**Locations:** `workspace.py:52–123`; `start.py:129–147`; `build_release.py:90–176`.

The installer hashes source bytes, then rereads those files for rendering. The builder hashes sources into a manifest, then rereads them for the archive. Both can use bytes different from the bytes they verified. The current release is consistent; this finding concerns subsequent operations while files change.

**Proposed work:**

- Read each small allowlisted source asset once into an immutable package snapshot; validate and render from that snapshot.
- Derive manifest entries and archive members from the same prepared byte map. For these small payloads, this is simpler than complex streaming synchronization.
- Freeze setup's reviewed plan/snapshot through confirmation, or explicitly compare a newly built snapshot with the reviewed one before creating the target.
- Keep editable settings behavior intentional: validate/freeze selected settings without treating them as immutable official package content during ordinary setup.
- Detect changes to source preparation inputs and report them without silently mixing revisions.

**Acceptance:** The reproduced between-read changes either cause explicit refusal or have no effect on the frozen operation. Every successful archive validates all of its own member hashes, and installed bytes match the verified plan.

### R06 — Define a maintained Python support policy

**Priority/evidence:** P1; current support-policy gap.  
**Locations:** runtime version guards, launchers, manifest `minimum_python`, documentation, release tests.

Python 3.9 reached end of life on 31 October 2025; Python 3.10 reached it on 1 October 2026. Both dates precede this review. Python 3.12 remains supported through October 2028. [Python version status](https://devguide.python.org/versions/).

**Trade-off and recommendation:** Retaining 3.9 makes use of some already installed macOS interpreters convenient, but turns an unsupported interpreter into the advertised baseline. Recommend **Python 3.12+ for the next public release**, with an explicit transition note. If legacy compatibility is retained, label it separately from the recommended supported configuration and time-limit it.

**Proposed work:**

- Centralize the minimum interpreter requirement and generate/check dependent guards, manifest metadata, launcher probes, and guide wording.
- Test the selected minimum and newest stable supported interpreter on both native target platforms; add intermediate versions where practical.
- Continue to require manual interpreter installation. Never upgrade/download Python automatically.
- Keep legacy 3.9 test history intact. Today's 3.9 pass is compatibility evidence, not a support endorsement.

**Acceptance:** Requirement messages, probes, package metadata, CLI behavior, and tested-version table agree. An unsupported interpreter fails clearly before mutation.

### R07 — Add contributor-reproducible native-platform CI

**Priority/evidence:** P1; missing `.github/workflows/` and native Windows evidence.  
**Locations:** repository configuration, `tests/test_workspace.py`, validation and manual tracking.

The 98 tests cover useful behavior, including real macOS shell launchers. They currently depend on local execution and do not establish native Windows paths, reparse handling, PowerShell discovery, console encoding, or `.cmd` behavior.

**Proposed work:**

- Add pull-request/push CI on macOS and Windows, using the agreed minimum and latest stable Python versions.
- Run tests against an isolated copy under `_tmp/`, matching the project's temporary-file rule. Include package consistency checks and extracted-release smoke tests.
- Add native Windows launcher tests for interpreter discovery, missing interpreter, approved installed distributions, paths with spaces/Unicode/shell punctuation, literal quit input, and failure/cancellation outcomes.
- Detect symlink/junction test capability. Report an unavailable capability explicitly; do not count skipped protection checks as successful Windows coverage.
- Test redirected stdout/stderr, JSON output, and non-ASCII paths on supported Python/Windows combinations.
- Give subprocesses and jobs explicit timeouts; preserve concise failure transcripts as CI artifacts.
- Use read-only default workflow permissions and pin third-party actions to reviewed full commit SHAs. [GitHub Actions secure-use guidance](https://docs.github.com/en/actions/reference/security/secure-use).

**Acceptance:** A clean contributor checkout has one documented verification command and reproducible CI results. Native automated checks remain separate from GUI/IDE manual checks; update `MANUAL_TESTS.md` only with actual manual evidence.

### R08 — Make removal of optional examples work cleanly

**Priority/evidence:** P2; confirmed.  
**Locations:** `payload/knowledge/README.md`; `workspace_manager.py:373–399`.

Missing example files are informational, but the required knowledge README's link makes removal an error. The advertised optional lifecycle is inconsistent.

**Proposed work:** Treat the shipped example reference as optional in a narrowly defined way, or give users a clear removal procedure that also removes its README link. Prefer a minimal design that makes the documented removal action pass validation; do not downgrade all broken knowledge links.

**Acceptance:** Removing the example according to the guide produces no structural error. A broken non-optional resource still reports the appropriate finding. Test both default and renamed layouts.

### R09 — Make link inspection accurate within its declared scope

**Priority/evidence:** P2; two confirmed failures.  
**Locations:** `workspace_manager.py:312–333`, `423–480`; `build_release.py:78–82`.

The regex does not implement Markdown. It handles the controlled payload's simple links but can misclassify ordinary user content. A malformed URL in an audited instruction file can also abort the whole audit because parsing is outside the relevant error boundary.

**Proposed work:**

- Isolate parse failures per file/link and continue returning other findings. Unsupported user syntax should be classified as uncertain rather than a proven missing resource.
- Exclude inline code and supported fenced-code forms; handle angle-bracket destinations, encoded paths, titles, and balanced parentheses within a clearly documented subset.
- Add maintainer checks for section anchors, which runtime link inspection currently drops. Avoid network access during validation.
- Preserve strict errors for simple required generated links whose absence is unambiguous.
- Prefer a small bounded scanner for runtime needs. A complete Markdown parser can remain a development-only choice if broader authoring checks justify it.
- Test README link relocation against the same supported forms; do not blindly extend the existing regex until it becomes an undocumented parser.

**Acceptance:** Inline-code examples do not become broken-link errors; malformed URLs do not terminate audit; controlled missing links still fail; source/root/generated documentation links and anchors are checked reproducibly.

### R10 — Normalize metadata text and bound parser inputs

**Priority/evidence:** P2; CRLF failure confirmed; resource-limit gaps from inspection.  
**Locations:** `skill_metadata`, `load_json`, `markdown_links`, `vscode_workspace_updater.document`, audit traversal.

**Proposed work:**

- Normalize LF/CRLF for metadata parsing after reading original bytes, so drift hashes still describe the actual file. Define BOM handling explicitly.
- Keep the controlled simple frontmatter subset, but distinguish unsupported YAML from invalid metadata in third-party skills. Add missing name-shape checks such as leading/trailing or consecutive hyphens when claiming conformance. [Agent Skills format specification](https://agentskills.io/specification).
- Limit document size before loading/parsing skill text and workspace JSONC. The existing 1 MiB link check happens after some callers have already read the file.
- Bound collection work without first materializing arbitrarily large directory listings. Keep limits visible in findings.
- Exercise JSONC nesting limits, duplicate keys, comments, BOM, CRLF, escaped strings, malformed tokens, and missing `folders` insertion.
- Preserve unknown workspace properties byte-for-byte. The existing handwritten JSONC editor is justified by that requirement; replacing it with plain `json.loads`/`dumps` would regress behavior.

**Acceptance:** Equivalent LF/CRLF skills validate consistently; oversized/malformed files produce bounded, useful diagnostics; no parser error causes unintended writes or a misleading complete audit.

## 5. Architecture, contracts, and maintainability

### R11 — Replace hidden module coupling with explicit dependencies

**Priority/evidence:** P2; inspection.  
**Locations:** `workspace.py:14–25`; loaders in `start.py`, `workspace_manager.py`, and tests.

The 879-line runtime is still manageable, but it combines configuration, paths, state, validation, audit, discovery, write operations, CLI routing, and interactive presentation. The initializer copies many runtime attributes into `globals()`. Some functions then execute with runtime globals while adjacent functions use copied initializer globals, making dependencies and test patches difficult to follow.

**Proposed work:**

- First replace the `globals()` export loop with explicit module-qualified calls or explicit imports through a reviewed loader.
- Establish a small number of modules around actual responsibilities: filesystem/configuration primitives, installed state and validation, repository/workspace operations, and CLI/presentation. Extract incrementally, not all at once.
- Keep `workspace_manager.py` as the stable entrypoint and the sole product `VERSION` owner, as required by `AGENTS.md`.
- Use one small, allowlisted local-loading mechanism compatible with `-I -S -B`; do not depend on the current working directory or site-packages.
- Check intended local paths before module execution. Current `start.load_workspace` performs its explicit path safety check after execution.
- Keep the standalone ticket helper self-contained unless a shared dependency clearly improves the product. Its small duplicated path checks may be preferable to breaking that contract; document and contract-test them.

**Acceptance:** Source initialization and installed runtime work from unrelated working directories and after relocation/installer removal. Dependencies are visible to readers and static tools. A pure refactor preserves generated content and observable behavior unless a separate change explicitly alters them.

### R12 — Introduce explicit data contracts and actionable schema errors

**Priority/evidence:** P2; inspection.  
**Locations:** `validate_config`, `installed`, `registration_plan`, `workspace_plan`, findings and result dictionaries.

**Proposed work:**

- Add type annotations at public boundaries. Use `TypedDict` for serialized JSON contracts or small dataclasses for internal plans where they improve clarity; avoid a large object hierarchy.
- Give plan fields names/types that distinguish source hashes, target hashes, options, proposed bytes, and findings. Avoid positional booleans such as `refresh(..., True)` in internal calls and tests.
- Validate nested types before operations that assume hashable values or mappings. Include field paths such as `repositories[1].include_in_workspace` and expected/actual types in errors.
- Separate setup-only, installed editable, and recorded-state invariants explicitly. Document which fields may change after installation.
- Reject duplicate directory inventory entries and malformed ownership records consistently; define which schema additions require a version change.
- Remove unused parameters/exports, including the unused `initializing` argument, after checking intended future behavior.

**Acceptance:** Malformed JSON shapes yield predictable domain errors rather than incidental `TypeError`/`KeyError` messages. Typed plans make equality/revalidation semantics understandable. Existing supported configuration files still behave as documented.

### R13 — Clarify failure states, locks, and durability guarantees

**Priority/evidence:** P2; inspection, supported by existing fault-injection coverage.  
**Locations:** `atomic_update`, `maintenance`, initialization markers, ticket locks and transfer markers.

**Proposed work:**

- Document operation states and recovery for initialization, ticket creation, transfer, registration, and workspace update. Include the possible partial success between independently committed phases.
- Give locks non-secret diagnostic metadata: operation, process identifier, start time, and an ownership token. Never automatically delete a lock merely because it appears old.
- Preserve the original operation error when lock/temp cleanup also fails; report cleanup problems separately. Ensure interrupt cleanup handles framework-owned temporary files without deleting user data.
- Decide what crash durability is promised. Atomic replacement alone does not establish persistence after power loss. If a stronger guarantee is intended, flush/fsync copied data before deleting the source and test supported platform behavior; otherwise document the narrower guarantee. [Python filesystem APIs](https://docs.python.org/3/library/os.html).
- Add a read-only recovery/status check for known lock/operation-marker locations. Do not turn ordinary audit into a recursive ticket-attachment scan.
- State that editors and other processes should not edit a ticket during transfer. Do not claim protection from hostile concurrent filesystem replacement; the design already excludes that threat model.

**Acceptance:** Failures during copy, verification, source pruning, state recording, and cleanup leave an understandable state and preserve recoverable bytes. Recovery never silently merges, deletes, or resumes ambiguous work.

### R14 — Make launchers maintainable and their contracts consistent

**Priority/evidence:** P2; inspection; native Windows behavior remains a verification gap.  
**Locations:** root Start copies and all `launchers/` files.

The Windows discovery logic is repeated as a long embedded PowerShell command, while setup root launchers are tracked copies of package templates. Current copies match, but there is no comprehensive mirror check. macOS forwards CLI arguments while Windows launchers do not; wrapper session exit codes also intentionally differ from operation codes.

**Proposed work:**

- Add checks that root launchers match their canonical sources. Keep copies as ordinary files for portability.
- Make interpreter discovery logic readable and testable, using a reviewed shared source or generation step if useful. Preserve the existing no-profile/no-download behavior; do not replace `-Command` with a script-file flow that unexpectedly changes execution-policy requirements.
- Define which installed Python distributions are supported. The adjacent-DLL filter may exclude legitimate layouts; test intended distributions before changing it.
- Decide whether clickable launchers deliberately omit CLI flag forwarding. Either provide safe, tested parity or document direct Python as the flag-bearing interface.
- Preserve the operation result in displayed output. Specify the wrapper's clean-session exit separately; do not promise a nonzero automation status while deliberately returning zero after `q`.

**Acceptance:** Supported interpreter discovery, literal input, cancellation, no-interpreter behavior, and exit contracts are tested natively. Updating a canonical launcher cannot silently leave source-download users with an older root copy.

## 6. Tests and release engineering

### R15 — Correct the test boundary instrumentation

**Priority/evidence:** P1 for verification integrity; confirmed guard gaps.  
**Locations:** `tests/test_workspace.py:26–70`.

The guard is useful defense in depth, but its lexical `Path.absolute().is_relative_to(...)` test does not remove `..`, and the `os.symlink` event checks argument zero rather than the new link path. Its global state also makes future threaded use easy to misunderstand. These are weaknesses in test evidence, not proof that production path checks allow the same operations.

**Proposed work:**

- Add direct guard tests for parent traversal, sibling prefixes, symlink destinations, rename/link endpoints, relative paths, and relevant `dir_fd` behavior.
- Interpret each audit event according to its documented argument contract. Reject unsupported cases in guarded tests instead of silently assuming containment.
- Normalize/check paths appropriately and retain independent production path tests and external sentinels.
- Isolate boundary-sensitive cases in subprocesses or make guard state explicitly scoped; Python audit hooks are process-wide and cannot simply be removed after a fixture.
- Document the instrumentation's limits. It must not be described as proof of all possible OS-level effects.

**Acceptance:** The two reproduced synthetic events are rejected; allowed in-scope operations still work; negative tests would fail if a guarded implementation attempted an actual out-of-scope operation.

### R16 — Organize tests around behavior and preserve reusable verification

**Priority/evidence:** P2; inspection.  
**Locations:** 1,870-line `tests/test_workspace.py`; `_tmp`-only scripts cited throughout `VALIDATION_REPORT.md`; `MANUAL_TESTS.md` fixture pointers.

**Proposed work:**

- Split tests by configuration/initialization, filesystem boundaries, tickets, refresh/JSONC, diagnostics, launchers, and release packaging; keep one documented runner/discovery command.
- Keep `unittest`: a framework migration is unnecessary. Test suites and independent fixtures are already supported. [Python unittest documentation](https://docs.python.org/3/library/unittest.html).
- Replace broad `assertRaises(Exception)` with expected domain errors and meaningful postconditions. Audit names such as `test_reserved_destination_and_case_collision_rejected_before_write`, whose current body primarily rejects an invalid mapping rather than independently exercising each named condition.
- Add the regression cases in this plan before fixing their corresponding behavior. Prefer externally observable invariants over assertions that mirror a particular implementation.
- Add explicit subprocess timeouts and diagnostics. Exercise real two-process locking/concurrency for key cases alongside deterministic fault injection.
- Move reusable release/link/example verification logic out of ignored scratch directories into reviewed maintainer scripts/tests. Keep generated output and transient fixtures under `_tmp/`.
- Provide small tracked, sanitized fixture sources or a reproducible fixture recipe for manual Copilot checks. The current `_tmp/test_data/` instructions are unavailable to a new contributor.
- Measure branch coverage of critical failure paths using an optional development-only tool if helpful. Do not substitute an arbitrary global percentage for the no-loss/no-overwrite invariants.

**Acceptance:** A contributor can reproduce every current release gate without private scratch scripts. Tests run independently and under the documented runner, with explicit skipped capabilities and useful failure output.

### R17 — Separate release preparation, verification, and publication

**Priority/evidence:** P1 for release confidence; inspection and R05 reproduction.  
**Locations:** `build_release.py`; source manifest; release README/checksum; maintainer commands.

The allowlisted, timestamp-normalized archive is a good fit. The main gaps are a missing read-only check mode, repeated source reads, and interruption handling while writing the archive/checksum pair.

**Proposed work:**

- Add a read-only `--check` or separate verifier for source hashes, README/design/launcher mirrors, version metadata, template coverage, and inventory invariants. It must report drift rather than refresh hashes and hide it.
- Continue using `build_release.py --sync-project-docs` for deliberate preparation, preserving `VERSION` as the sole product-version edit point.
- Stage and validate release output using the immutable snapshot from R05. Publish to absent final names without overwriting existing ZIPs or checksums. Detect and explain partial ZIP/sidecar states after failures.
- For official releases, check that shipped settings are reviewed distribution defaults; a schema-valid personal `settings.json` should not silently become an official default. Keep intentional private/custom bundles possible through an explicit path.
- Verify the final extracted archive: member paths/metadata, content hashes, defaults/custom names, installed commands after relocation, and installer independence.
- Record the build interpreter/platform and the scope of reproducibility. Current byte-identical rebuild evidence does not establish cross-platform/compression-library byte identity; test that before promising it.
- Keep archival housekeeping explicit: after verifying a newer release, move the previous ZIP/checksum to `_old zips/` without overwriting archived files.
- Prefer GitHub Releases for future distribution binaries. Keep the current tracked ZIP/history unchanged until a deliberate repository policy change; there is no need to rewrite Git history.

**Acceptance:** Verification from a clean checkout writes nothing. Successful final archives verify themselves. Injected archive/sidecar failures leave identifiable recoverable output. Release notes retain actual versioned evidence rather than relabelling historical results.

### R18 — Give current specifications and historical evidence clear ownership

**Priority/evidence:** P2; specific contradictory/stale wording found.  
**Locations:** `DESIGN.md` sections 1.4, 7.3, 8.4, 18–21; root design mirror; `VALIDATION_REPORT.md`; maintainer guides.

Design sections 1.4 and 8.4 still say blank settings input exits, while section 7.3, code, tests, and current guides correctly use Enter to continue to the read-only preview. The validation report's final remaining-checks section calls the refresh skill unreleased although the current release includes it. Build/test narratives are also mixed into a large current implementation specification.

**Proposed work:**

- Correct current normative statements and clearly mark intentionally historical ones. Do not edit old test outcomes to imply newer-version coverage.
- Keep one canonical design source and generated root mirror with a check, as already intended. Never hand-maintain divergent copies.
- Put current CLI/schema/failure contracts and architectural decisions in focused sections; move historical implementation prompts/build narratives to an appendix or history document if that improves navigation.
- Make the current validation summary short and prominent, with versioned historical evidence beneath or linked from it. Historical local log paths are context, not a reproducible test procedure.
- Keep installer, generated root, daily, and Copilot guides focused on their existing jobs; avoid undoing the recent simplification by copying this whole plan into user-facing documentation.

**Acceptance:** Code, tests, help, current design, and current guides agree on defaults, ownership, supported platforms, and recovery. Every historical result retains its original release and scope.

## 7. Copilot instructions, skills, and templates

### R19 — Establish an actual compatibility baseline for AI workflows

**Priority/evidence:** P1 before stronger AI compatibility claims; verification gap.  
**Locations:** `COPILOT_GUIDE.md`, `MANUAL_TESTS.md`, six skills, multi-root generated workspace.

The existing guide correctly distinguishes discovery, instruction inclusion, resource reads, and correct task behavior. Preserve that distinction. Current VS Code documentation still makes instruction behavior harness-dependent and documents separate Local discovery settings; references alone cannot establish this non-Git multi-root layout's behavior. [VS Code instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions).

**Proposed work:**

- Record a tested VS Code/Copilot version pair and intended Local environment, rather than relying only on an indefinitely moving “latest stable” target.
- Run the existing basic onboarding check and all six skill smoke tests on native supported platforms. Extend cross-root/mode/custom-name/relocation checks according to actual claims and relevant changes.
- Use synthetic facts and predictable failure cases, including conflicting repository guidance, missing context, repeated ticket creation, and returning/missing repositories during refresh.
- Preserve explicit attachment/direct-command fallbacks. Do not introduce global instruction copies or repository modifications solely to force discovery.
- Keep sanitized fixture inputs and a scoring/checklist rubric under version control. Keep private IDE debug exports outside the repository.

**Acceptance:** `MANUAL_TESTS.md` contains actual environment-specific evidence or explicit pending/blocked scope. Each verified skill demonstrates loading its intended helper/resource, correct operation, and appropriate handling of refusal.

### R20 — Refine the six skills and orientation without expanding ceremony

**Priority/evidence:** P2; editorial/behavioral improvement from inspection.  
**Locations:** `payload/root/copilot-instructions.md`; `payload/skills/`.

The skills are already concise, explicit, and mostly well scoped. Keep their small size and progressive resource loading. Current VS Code documentation supports manual-only invocation through `disable-model-invocation: true`; it also offers `argument-hint` for slash-command usability. [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).

| Asset | Proposed improvement | Verification |
|---|---|---|
| Orientation | Make overview/reference-map reading conditional on task relevance, unknown ownership, or cross-repository scope. Preserve reuse of current chat context. Clarify that quoted ticket/reference content supplies facts, not authority to broaden actions. | Small local edit avoids unnecessary context reads; cross-repository task reads the needed map; incomplete fields are surfaced without fabrication. |
| `ca-jira-ticket-init` | Add a concise argument hint and clear ID-only/details/options examples. Standardize approved interpreter wording across platforms. Exercise literal multiline descriptions through actual shell/tool invocation, not only subprocess argument arrays. Consider an explicit file/stdin description input only if it materially improves safe transport. | Quotes, leading dashes, braces, Unicode, shell substitutions, and multiline text survive literally; no extra documents are created; incomplete creation is reported under R02. |
| `ca-jira-ticket-archive` | Explain content versus metadata guarantees after R03 and the new recovery-state behavior. Keep explicit ticket selection and no inference of completion. | Complete folder preserved; restricted access preserved as promised; collisions and partial transfers do not trigger an improvised move. |
| `ca-jira-ticket-restore` | Match archive's guarantees and result vocabulary; keep missing-ticket creation separate. | Repeat restore is an accurate no-op; missing/colliding/incomplete tickets remain untouched. |
| `ca-change-review` | Define a compact findings format: severity, file/location, observed behavior, consequence, evidence, suggested next step. State unresolved baseline/scope limits even when no confirmed defect is found. | A seeded regression is found with evidence; a clean change is not padded with speculative findings; partial scope is explicit. |
| Review checklist | Put general behavior, interfaces, errors, configuration, tests, and deployment/recovery first. Keep SQL/infrastructure examples conditional. Add optional read-only Git comparison recipes that disable external diff/textconv and explicitly cover untracked/pre-existing work. | Reviews cover cumulative relevant changes without executing repository-defined diff helpers or modifying Git state. |
| `ca-config-audit` | Define summary ordering and the distinction between deterministic errors, unsupported syntax, and possible semantic conflict. Show an exact command shape consistent with other skills. | Findings remain useful after malformed/unfamiliar documents; no repairs or unrelated reads occur. |
| `ca-workspace-refresh` | Use R04's approved-plan precondition; explain no-op and partial-result handling using the actual returned status. | Changed plans require fresh approval; settings survive; interruption fallback works in the IDE. |

Do not add model names, forked agents, experimental tool grants, mandatory plan files, or automatic skill selection to improve apparent sophistication. Keep every framework/maintenance skill under the required `ca-` namespace.

### R21 — Make overview and reference-map templates more useful to fill

**Priority/evidence:** P2; inspection.  
**Locations:** `payload/project/overview.md`, `reference-map.md`.

The blank templates are honest and compact. Their weakness is that they tell a new user what headings exist but provide little help producing verifiable, maintainable content.

**Proposed work:**

- Add brief field guidance, clearly separate from actual project facts. Tell users to replace the unpopulated title/status when appropriate and retain explicit unknowns.
- In overview, identify repositories by stable ID plus relative local path/link; describe responsibilities, key interfaces/dependencies, behavior to preserve, and ownership when known.
- Link to repository-owned build/test/development instructions instead of duplicating command lists that become stale.
- Associate important architecture/behavior claims with sources and verification context, not just one undifferentiated date at the bottom.
- In reference map, distinguish the canonical authoritative source from an optional local mirror. Capture a revision/commit/version when available, a checked date, and owner/limitations without creating an excessively wide table.
- Explain that a date records an actual check, not a guarantee of freshness, and that local paths should remain relative for portability.
- Add one small fully populated synthetic example in the source examples, clearly labelled as fictional. Do not populate users' actual context with invented architecture.

**Acceptance:** A new tester can fill the templates using a small two-repository fixture, find the right source, recognize an unknown/stale claim, and keep links valid after relocation/custom naming. The default orientation still remains short.

### R22 — Improve ticket templates for the brief-only workflow

**Priority/evidence:** P2; inspection.  
**Locations:** `ca-jira-ticket-init/templates/{brief,plan,review,notes}.md`.

**Proposed work:**

- Keep only `brief.md` required. Add a small place for validation intent and actual outcomes, so users need not create a plan/review file just to record meaningful checks.
- Distinguish supplied requirements, agreed acceptance criteria, and open questions. Keep acceptance criteria unfilled until known.
- Clarify repository ID/path and baseline capture context. Keep the current reminder that a SHA alone does not preserve uncommitted/untracked work.
- Add an example acceptance criterion and baseline row in a separate fictional example, not as apparent live evidence in the default template.
- Give review findings severity/location/evidence fields and separate executed checks from recommended checks.
- Make optional plan approvals conditional and explicitly sourced. Avoid a heading that implies every task needs a separate approval ceremony.
- Preserve internal relative attachment links and document that external links into an active/archive path can change.

**Acceptance:** A small task can be specified, implemented, checked, reviewed, and archived using only its brief. Optional resources add value for larger work. Repeat creation and all transfers preserve user content exactly as promised.

### R23 — Strengthen repository-instruction and knowledge examples

**Priority/evidence:** P2; inspection.  
**Locations:** `payload/examples/copilot-instructions.md`; knowledge README, synthetic guide and SVG.

**Proposed work:**

- Show a compact repository-instruction structure with purpose, relevant conventions, source-of-truth documentation, and verified commands including their working directory. Clearly mark replacement fields and do not execute placeholders.
- Keep adoption through the owning repository's normal review. Do not commit a developer's sibling paths or personal setup into other repositories.
- Make the knowledge example demonstrate an actually usable synthetic procedure: expected result, verification, common failure, sources, and last-checked meaning, while retaining its small static asset.
- Explain when to update/retire a note and when to link to upstream documentation rather than copy it.
- Address optional example removal consistently with R08. Preserve the static, script-free, locally linked SVG.

**Acceptance:** A tester can distinguish template instructions, fictional example data, verified project facts, and authoritative external policy. Examples remain useful without implying executed work or current company guidance.

## 8. Contributor experience and public sharing

### R24 — Add lightweight development tooling and code conventions

**Priority/evidence:** P2; inspection.  
**Locations:** missing developer tool configuration; Python modules and tests.

**Proposed work:**

- Add a small `pyproject.toml` for development tooling and agreed Python targets. Recommend one formatter/linter such as Ruff, rather than several overlapping tools; it supports both roles and project configuration. [Ruff documentation](https://docs.astral.sh/ruff/).
- Keep tooling optional for consumers and separate from the offline runtime. Pin contributor/CI tool versions and keep caches/output under `_tmp/` or explicitly ignored paths.
- Standardize import organization, wrapping, naming, and a consistent quote/format style. Make formatting a separate reviewable change.
- Add docstrings for exported functions and non-obvious contracts: allowed path forms, ownership, side effects, failure retention, expected hashes, and encoding. Comments should explain invariants and reasons, not restate individual assignments.
- Apply type checking incrementally to the contracts in R12. Do not require immediate strict typing of the entire test suite.
- Document how to run checks, deliberately refresh package hashes after edits, reproduce a failure, and prepare a release. Avoid hidden hooks that modify files on every command.

**Acceptance:** Contributors can discover and run a small consistent set of checks. Consumers still run from a downloaded folder with a supported Python interpreter and no dependency installation.

### R25 — Add intentional reuse and contribution metadata

**Priority/evidence:** P1 for an intended open-source release decision; P2 for surrounding polish. Missing files observed.

**Proposed work:**

- The project owner should choose and add explicit licensing terms before presenting the project as open source. Include the selected license in distributed source and release artifacts, and decide how it applies to generated helpers/templates. The review does not select legal terms on the owner's behalf. [GitHub repository licensing guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
- Add concise contribution instructions: architecture map, temporary-file rules, `ca-` naming, manual evidence requirements, tests, version source, release preparation, and expected PR information.
- Provide an issue template asking for release, acquisition method, OS/Python, reproduction, and sanitized errors; add IDE/harness versions for AI issues.
- State support scope and a suitable private vulnerability-reporting route when one exists. Do not invent contact details or a response-time promise.
- Before initial public publication, review the intended tracked tree and history for private data using an appropriate local/history scan. Keep scratch fixtures, private IDE exports, and archived local packages excluded.
- Keep maintainer `AGENTS.md`, `MANUAL_TESTS.md`, and this plan outside consumer ZIPs and generated workspaces. Add relevant exclusion tests as inventory evolves.

**Acceptance:** Prospective users know the intended reuse terms, supported configurations, reporting route, and contribution workflow. Published artifacts contain the required license and reviewed files, without maintainer/private material.

### R26 — Make CLI diagnostics and terminal behavior predictable

**Priority/evidence:** P2; inspection and native Windows verification gap.  
**Locations:** CLI `main` functions; `Console`; `printable`; JSON reports.

**Proposed work:**

- Document stable exit-code meanings, cancellation/no-op/partial-completion statuses, and stdout/stderr behavior across entrypoints.
- Define machine-readable failure output for JSON consumers, including early state/schema failures, without dumping private content or tracebacks by default.
- Sanitize displayed user-controlled labels and exception text consistently. Current refresh output uses `printable`, while some setup paths/errors use raw values.
- Specify UTF-8 JSON/file output and useful behavior when a terminal/pipe cannot encode a character. Test supported Windows redirection explicitly.
- Avoid imposing a minimum prose width of 60 columns when the actual terminal is narrower; preserve full copyable paths and test visual readability separately from byte preservation.
- Include operation/version/root context in saved report metadata where useful, using relative identifiers and explicit timestamps. Version that report schema if external consumers depend on it.

**Acceptance:** Scripts can reliably distinguish success, no-op, cancellation, invalid input, incomplete work, and operational failure. Human output remains readable in narrow/plain/redirected terminals without hiding the actual result.

## 9. Recommended implementation sequence

Use small reviewed changes. Relative sizes below are planning estimates, not calendar commitments: **S** = localized; **M** = several coordinated files/tests; **L** = platform or lifecycle work with substantial verification.

| Work package | Scope and dependencies | Size | Completion gate | Progress and decisions |
|---|---|---|---|---|
| 1. Reproducible baseline | R01, R15; add failing regressions for confirmed cases; retain current behavior otherwise | M | Deterministic checkout bytes and trustworthy guard tests; existing suite remains green | Not started |
| 2. Ticket integrity | R02, R03, relevant R13/R22 recovery contracts | L | Interrupted creation and restricted transfers behave safely on native platforms | Not started |
| 3. Approved plans and package snapshots | R04, R05 | L | Stale refresh plans cannot broaden writes; verified bytes are the bytes installed/archived | Not started |
| 4. Small validation fixes | R08, R09, R10; selected R12 diagnostics | M | Optional removal, CRLF metadata, malformed links and parser limits have regression coverage | Not started |
| 5. Platform/release automation | R06, R07, R14, R17; reusable checks from R16 | L | Clean-checkout CI plus extracted-artifact workflows on macOS/Windows; supported Python policy agreed | Not started |
| 6. Maintainability | R11, remaining R12/R13, R24, R26; do after behavior is protected | M–L | Explicit dependencies/contracts; stable CLI and relocation behavior; separate formatting diff | Not started |
| 7. AI content and onboarding | R18–R23; plan-binding and recovery updates depend on packages 2–3 | M plus manual testing | Useful synthetic templates and actual skill/context evidence; historical results preserved | Not started |
| 8. Public release preparation | R25; final checks from R17 | M | Owner's licensing choice, contribution/reporting docs, exact-artifact verification, honest compatibility statement | Not started |

Update **Progress and decisions** as work proceeds: status (`Not started`, `In progress`, `Blocked`, `Complete`, or `Deferred`), update date, key decisions and reasons, remaining work, and links to evidence or PRs. Keep entries brief; link longer notes. Mark a package complete only when its completion gate is met. Record actual manual test results in `MANUAL_TESTS.md` and link them here.

Within each package: add/confirm the relevant behavioral regression, implement the narrow change, update affected contracts/guides, run focused checks, then the required suite. Broaden testing when a changed boundary or failure warrants it; do not repeatedly rerun everything for unrelated prose polish.

Do not start with the architecture refactor. The current structure is sufficient to fix the confirmed defects, and those tests will make later restructuring safer.

## 10. Final acceptance matrix for the improved release

| Area | Required evidence |
|---|---|
| Acquisition | Source clone with supported line-ending configurations, source archive, and release extraction all produce usable reviewed inputs |
| Setup boundary | Preview is read-only; explicit creation is new-root-only; existing targets/redirections/collisions fail; source/package bytes are unchanged |
| Ticket creation | ID-only/details/options, repeats, interrupted writes and recovery; no fabricated requirements or silent acceptance of partial creation |
| Transfer | Bytes, empty directories, promised permissions, collisions, copy/prune failures, stale markers and repeated archive/restore outcomes |
| Refresh | Approved-plan binding, literal options, changed files/folders/state, missing-entry cleanup, settings preservation, partial completion and no-op behavior |
| Validation/audit | Accurate controlled links, uncertain unsupported syntax, LF/CRLF metadata, bounded malformed inputs, continued findings after per-file errors |
| Runtime independence | Default/custom names, unrelated working directory, moved/renamed complete tree, installer removed, all daily commands usable |
| Release | Read-only consistency check; immutable source snapshot; normalized member metadata; self-consistent manifest/checksum; extracted final artifact tested |
| Platforms | Supported minimum/latest Python on native macOS and Windows; unsupported capabilities explicitly recorded; native launchers and redirected output tested |
| Copilot | Actual Local discovery/inclusion/resource-use evidence for claimed workflows; synthetic tasks, refusal cases and fallback; manual tracker updated honestly |
| Documentation | Current code/help/spec/guides agree; first-use tester can complete the common workflow; no historical test result is relabelled |
| Publication | Chosen license, reporting/contribution guidance, reviewed publication set, no scratch/private artifacts, version/archive rules followed |

Product version changes remain restricted to `VERSION` in `WORKSPACE_SETUP/scripts/workspace_manager.py`. Preparation and root document synchronization use `build_release.py --sync-project-docs`; versioned archives use `--output-dir`. Update changelog and actual validation evidence explicitly. Move the superseded ZIP and checksum to `_old zips/` without overwriting prior archives.

No release should be described as fully verified on a platform or in an IDE mode for which the corresponding evidence remains pending. A clearly scoped pilot can still be shared for review while those limits are explicit.
