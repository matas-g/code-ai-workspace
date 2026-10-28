# Framework maintenance

These rules apply to framework contributors. Keep this file outside the release ZIP and generated workspaces.

- Use the `ca-` prefix for every skill created by Code-AI or for maintaining it. Keep folder names, the `name` field in SKILL.md, command examples, helper/resource links, runtime inventory and release mappings aligned. Leave unrelated third-party and repository-owned skills unchanged.
- Record manual test results in MANUAL_TESTS.md. Automated checks cannot prove IDE skill discovery.
- Put temporary development files in `_tmp/`.
- When building a newer release ZIP, move the previous ZIP and its `.sha256` checksum into `_old zips/`. Never overwrite archived files.
- Change the product version only at `VERSION` in `WORKSPACE_SETUP/scripts/workspace_manager.py`. Prepare release labels, hashes and root document copies with `build_release.py --sync-project-docs`; use `--output-dir` for an automatically versioned ZIP filename. Record changelog and actual test evidence explicitly; never replace historical version numbers automatically.
