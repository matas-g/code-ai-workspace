---
name: caw-implement-issue
description: Implement one specified GitHub issue in this project through scoped changes, required verification and evidence updates. Use for implementation requests, not choosing or reprioritizing issues.
---

# Complete one issue with evidence

Locate this repository using `AGENTS.md` and `WORKSPACE_SETUP/scripts/workspace_manager.py`. Read [contributor instructions](../../../AGENTS.md), their maintainer issue-workflow rules and the relevant [development/verification guidance](../../../maintenance/DEVELOPMENT.md). Work on the issue selected by the user; do not silently start the whole `next` queue. If no issue is identifiable, establish the selection before editing.

Fetch the live issue, acceptance checklist and relevant progress/blocker comments from the confirmed repository. Inspect current working/staged changes and relevant source/evidence before editing. Reproduce the bug when practical, or establish the remaining gap for an improvement/verification task. A stale report or an already-satisfied checklist does not justify manufacturing a code change: report the evidence and update the issue appropriately. An unexpectedly closed issue needs a current reason before reopening or implementing more work.

Choose a narrow approach consistent with the acceptance criteria and project guarantees. Explain consequential design choices briefly; ask only for material decisions that cannot reasonably be inferred. A routine fix needs no separate plan document or mandatory plan-approval round. Keep unrelated cleanup and newly discovered independent work outside this change; report useful follow-ups without silently expanding scope.

Implement the scoped work, focused regression coverage for behavioral changes, and affected contracts/guides. Follow AGENTS.md's isolated-copy checks for behavior/packaging; use link/path checks for documentation-only work. Run the appropriate checks, fix failures introduced by this change, and inspect the resulting diff against the issue criteria. Preserve pre-existing work and report unrelated baseline failures separately. Keep actual GUI/Copilot/native-platform verification distinct from structural or automated checks.

Continue through the authorized implementation and available verification. If a required manual check or environment is unavailable, finish independent work, record exactly what remains and leave the issue open. Do not use a wording change or passing suite as proof of an unobserved manual result.

Record actual automated/release evidence in VALIDATION_REPORT.md and actual manual observations in MANUAL_TESTS.md as applicable; preserve historical entries. Invoking this implementation workflow includes updating the selected issue with completed checklist items, concise results and remaining checks unless the user restricts remote writes. Re-read before updating so concurrent context is preserved, then verify the update. Use resolving links; summarize unpublished local evidence rather than linking to missing GitHub files.

Close only when every applicable acceptance criterion is supported, required manual checks are complete, and changes have reached the user's intended integration point. If the user wants local review first or changes remain unintegrated, leave it open with that status. Respect explicit instructions about issue closure, labels, commits and pushes; this workflow does not authorize a release, version bump or publication. If GitHub is unavailable, proceed only with a sufficiently complete user-provided issue snapshot and identify the pending remote update.

Finish with the issue link, changed behavior, actual verification and remaining limitations. Do not move automatically to another issue.
