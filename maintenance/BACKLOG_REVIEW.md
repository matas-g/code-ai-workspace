# Backlog review for a small, single-maintainer project

**Reviewed:** 1 November 2026; simplified after owner feedback.<br>
**Baseline:** Source commit `338334b`, product 0.1.19, including unreleased B21 packaging changes.<br>
**Decisions:** Improve the macOS pilot first; require manually installed, approved Python 3.12+ for the next pilot release.<br>
**Ownership:** [BACKLOG.md](BACKLOG.md) remains the current queue until issues are actually moved to GitHub. The changes below are review recommendations.

## Recommendation

Use ordinary GitHub Issues with short descriptions and completion checklists. A solo maintainer working with an AI agent needs a clear next task, enough context to implement it safely, and a way to tell when it is finished. A board, issue hierarchy, estimates and several metadata fields would add upkeep without enough benefit at this scale.

Keep the useful parts of the backlog: stable B IDs, concrete findings, sensible ordering, and links to technical detail and actual test evidence. Improve vague titles, remove overlap and stale work, and split an item only when its parts need separate priority or can be completed independently. Related small fixes can remain in one issue with a checklist and several small PRs if useful. GitHub supports issue splitting and dependencies; use those features when they solve an actual tracking problem. [GitHub guidance](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects).

## Just enough issue tracking

- **Labels:** Start with `bug`, `improvement`, `verification` and `next`. Use the first three to distinguish kinds of work; add `next` to the small set worth doing soon. A missing test result is verification work, not automatically a bug. No separate area, platform, size or priority label families are needed.
- **Status:** Use Open and Closed. A short comment can explain that work has started, is blocked, or is waiting for a manual check. No custom status workflow is required.
- **Priority:** Work from the few issues marked `next`. Choose them by consequence and current pilot needs. Keep optional polish and future-platform work out of that immediate set. There is no need to reproduce every Markdown rank or P level as GitHub metadata.
- **Scope:** Keep related work together. Split when doing so makes it easier to choose, implement or close the work; file boundaries and individual checklist lines do not each need an issue. No parent issues or sub-issues are required.
- **Dependencies:** Write “Needs #123 because …” only for a real blocker. Shared files or a preferred sequence can be mentioned without creating a dependency graph.
- **Process:** No Project board, sprint, estimate, assignee rotation, automation or milestone is needed to start. A release milestone can be added when it helps assemble a real release. A plain reusable Markdown issue template is sufficient; a YAML form can wait for actual reporting problems.

A larger label scheme would make filtering more precise, but would require more classification on every issue. The four-label approach is the recommended starting point. GitHub labels are sufficient for this simple categorization. [GitHub labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels).

## A short issue format

Use a concrete title, such as **“Preserve multiline ticket details”** or **“Reject refresh changes that were not approved.”** An area prefix is optional. Put the B ID and detailed technical references in the body.

```markdown
## Problem or outcome
What is wrong or needed, and why it matters.
For a bug, include a short reproduction and relevant version/environment.

## Done when
- [ ] Observable result
- [ ] Relevant regression or manual check completed

## References
B ID; relevant R/BUG reference; evidence or related issue links.
```

Aim for a description that fits on one screen, with links for deeper detail. Complex failure cases may need more explanation; do not remove important no-loss/no-overwrite criteria just to meet a length target. There is no need for a user story, severity score, estimate, formal readiness checklist or duplicated status field.

For example:

**Title:** Detect interrupted ticket creation<br>
**Labels:** `bug`, `next`

**Problem:** A failed write can leave a partial brief. Retrying then treats it as an existing completed brief. The original review reproduced this on 0.1.18; the same direct-write/existence mechanism remains in source `338334b`.

**Done when:**

- [ ] Injected brief and optional-file write failures leave an identifiable incomplete state; retry does not report normal completed creation.
- [ ] Completed, user-edited files remain byte-identical on repeat creation; no automatic overwrite or deletion occurs.
- [ ] The focused regression and recovery guidance are updated, with actual results recorded.

**References:** B03; R02; relevant R13/R22. Permission preservation is a separate outcome if implemented separately.

## Review of all current items

The table is a review of scope and need, not a second ordered queue. Keep existing B IDs as references; do not introduce decimal child IDs or create a hierarchy just for migration. Current runtime correctness matters more than optional tooling and editorial expansion.

| Item | Practical recommendation |
|---|---|
| **B01** | **Keep the verification fixes; separate only if useful.** The write-guard repair and checkout-byte policy solve different problems, so two ordinary issues are reasonable when scheduled. Reusable fixtures can be added with the fix that needs them. The entire B01 package must not block unrelated wording or helper work. |
| **B02** | **Keep:** “Avoid reading tickets when no ticket is selected.” This is a confirmed context-scope failure, not an access-control guarantee. Verify actual reads in fresh no-selection and selected-ticket controls; instruction-text checks alone are insufficient. |
| **B03** | **Keep both defects.** Interrupted creation and restrictive transfer permissions justify separate issues if worked independently. Each should preserve existing user bytes and cover failure recovery. Verify the promised macOS/POSIX behavior now; retain Windows ACL limits explicitly for later qualification. |
| **B04** | **Use one refresh issue with a checklist initially.** Include runtime approval binding, correct custom-path summaries and the pre-apply launcher reminder. A small prose fix can land before plan binding without closing the whole issue. Split the runtime change from messaging only if it helps schedule or finish them independently. Actual chat checks remain necessary. |
| **B05** | **Clarify ownership:** installation snapshot consistency belongs here; builder snapshot consistency belongs with B12. Both are confirmed verified-byte consistency gaps. Use deterministic between-read edits to check the frozen/refused outcome. Avoid two tickets owning the same builder change. |
| **B06** | **Keep:** “Preserve multiline ticket details through Copilot invocation.” Supplied task detail is being lost. Reproduce the actual skill-to-tool path; existing helper argument tests do not cover the failure. Keep repeat preservation, special characters and custom/relocated paths in the acceptance checklist. Add a new input method only if needed. |
| **B07** | **Keep as a small guide fix.** Make the optional Python reference readable in the default Markdown Editor and Preview. A normal Markdown section is sufficient. Preserve commands and recovery content, and retest incoming links and custom names. |
| **B08** | **Reconcile before creating new implementation work.** B21 removed the failing template entry path from current onboarding. Reuse its automated evidence and put the remaining native current-flow check in B14. The published 0.1.19 package is still affected; historical DOC-05 stays FAIL until a new result is recorded. Link candidate verification and shipment before claiming consumer resolution. |
| **B09** | **Use a validation bug checklist.** Optional-example removal, malformed-URL audit failure, inline-code false positives and CRLF frontmatter are concrete defects. They can share an issue while being fixed together; split a larger parser change if it would hold up the others. Broader syntax support and resource limits should be bounded follow-ups, not prerequisites for the small fixes. |
| **B10** | **Ready as a policy-backed implementation task:** “Require Python 3.12+ for the next pilot.” The owner decision is settled. Align guards, launchers, manifest/builder, skills, guides and tests; fail before writes on older versions. Keep installation manual and historical 3.9 results intact. |
| **B11** | **Reduce current scope to macOS checks.** Automate the documented isolated checks when useful; a test-suite reorganization is unnecessary first. Windows discovery/reparse/redirected-output work waits for Windows qualification. Handle the observed narrow-width problem as a small CLI fix when scheduled. Automated launcher checks do not establish native GUI behavior. |
| **B12** | **Keep one release-reliability issue with a checklist.** Include read-only verification, the builder snapshot from B05, identifiable ZIP/checksum failures, absent-output enforcement and extracted-artifact checks. B21 packaging separation is already done. Split a part only if it becomes a substantial independent change; do not create a release-workstream hierarchy. |
| **B13** | **Use one remaining macOS verification checklist.** Fix issues own their targeted retests; this covers residual native Terminal/launcher/recovery and integrated candidate checks. Reuse MANUAL_TESTS.md rather than creating an issue per matrix cell. Keep Windows evidence for a later scope. Name the missing environment when genuinely blocked. |
| **B14** | **Keep one practical first-use check.** A new tester should complete the corrected macOS setup and daily journey with default/custom names and generated-only navigation. Record assistance and failures. Fresh sign-in or managed-policy checks can remain explicit unverified branches until an appropriate environment is available; they need separate issues only when someone will test them. |
| **B15** | **Defer public-only decisions.** Licensing, public contribution/support policy and publication/history review are needed when public release is targeted. They do not block internal issue tracking or current macOS fixes. Basic labels and a short issue template can be set up directly during migration without a separate process project. |
| **B16** | **Retain concrete error/recovery improvements; avoid a general redesign.** Fix actionable schema errors, lost original errors or confusing CLI results when a reproduction/use case exists. Introduce types or lock diagnostics where they help that change. Do not make broad contract work a prerequisite for existing bugs. |
| **B17** | **Defer broad maintenance work.** Prefer small refactors encountered during real fixes. Keep unittest and the existing documented commands. A consolidated runner or optional pinned tooling is useful only when it saves repeated effort; neither requires an architectural or test-framework project. |
| **B18** | **Keep only useful content improvements.** Improve review output, context guidance or briefs against a concrete example or usability problem. Do not turn every R20–R23 suggestion into an issue. Keep a single required brief, short orientation and optional supporting resources. Fix-specific text belongs with its owning bug. |
| **B19** | **Re-triage; avoid an open-ended cleanup issue.** B21 already delivered document ownership, settings-default corrections and a prominent current validation summary. The old refresh-unreleased wording now sits in historical material. Create remaining work only for a named current mismatch or useful navigation improvement; preserve historical evidence. |
| **B20** | **Keep deferred.** Evaluate another IDE only when there is an actual user need, named editor and available installation. No active GitHub issue is necessary now. |
| **B21** | **Keep complete.** Link its evidence from related items. Do not reopen it or create an active issue merely to reconstruct history. Its automated packaging evidence does not establish native onboarding, Windows or runtime fixes. |

The strongest immediate outcomes remain incomplete-creation detection, restrictive permissions, approved refresh binding, verified-byte consistency, literal task capture and selected-ticket scope, supported by reliable regressions. Correctness fixes should not wait for a refactor, Windows access or elaborate tracking setup. The smaller guide and message fixes can be completed along the way.

## Completion and moving to GitHub

Keep a fix open until its checklist and relevant checks are satisfied. For AI/editor behavior, record the actual manual result; a passing structural test is not enough. If a manual check is unavailable, a comment stating what remains is sufficient. A macOS result must remain scoped to macOS. Use the existing manual tracker and validation report for evidence, with a link from the issue rather than another copy of the test report.

When moving the work:

1. Create the four labels and the few issues worth doing next. Leave optional or speculative ideas in the existing deferred list until needed. No bulk import of every proposed subtask is necessary.
2. Include the B ID, short problem, completion checklist and relevant reference links in each issue. Use repository URLs for links in GitHub; ignored scratch logs must not be the sole reproduction.
3. Make GitHub the source of truth for imported issues' status and priority. Replace their BACKLOG.md rows with links and leave deferred ideas in a clearly separate section. Do not maintain two live queues for the same work. Update the contributor/technical-plan ownership wording once as part of that move.

The next delivery scope remains the macOS pilot. Python 3.12+ is an approved next-release change, not an implemented requirement yet. The policy favors maintained support over older preinstalled-interpreter compatibility; current support dates were checked in the original review. [Python version status](https://devguide.python.org/versions/).

## Review evidence

The original review read the complete backlog, technical proposals and manual tracker, then checked the current validation summary, guides and relevant source mechanisms. Its conclusions remain: B08/B19 need reconciliation against B21; the other recorded runtime/AI defects have not been closed by that packaging change. Current [setup steps](../WORKSPACE_SETUP/SETUP_GUIDE.md#quick-setup) direct users to generated guides, and [B21 validation](VALIDATION_REPORT.md#unreleased-user-package-separation--31-october-2026) distinguishes automated package checks from native onboarding.

Original reproductions and manual results retain their recorded versions/environments. Source `338334b` and the published artifact share version 0.1.19 but differ in packaging, so identify the source commit or exact artifact when that distinction matters. This review and its simplification add no product-suite, release-build or native IDE/Terminal/Windows evidence.
