#!/usr/bin/env python3
"""Maintainer-only allowlisted manifest/release builder; not an initialization step."""
import sys
sys.dont_write_bytecode = True
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import stat
import zipfile

PACKAGE = Path(__file__).absolute().parent.parent
# Only user-package inputs. Repository tests, build tools and maintainer documents
# stay out of the manifest and ZIP even when present beside these sources.
INVENTORY = [
    'LICENSE', 'SETUP_GUIDE.md', 'COMPATIBILITY.md', 'RELEASE_NOTES.md',
    'scripts/workspace.py', 'scripts/workspace_manager.py', 'scripts/terminal_output_formatter.py', 'scripts/vscode_workspace_updater.py', 'settings.json', 'scripts/start.py',
    'launchers/refresh_vscode_workspace macOS.command', 'launchers/refresh_vscode_workspace Windows.cmd',
    'configuration-examples/default.json', 'configuration-examples/renamed.json',
    'payload/root/README.md', 'payload/root/gitignore.txt', 'payload/root/DAILY_WORK.md',
    'payload/root/copilot-instructions.md', 'payload/root/COPILOT_GUIDE.md',
    'payload/project/overview.md', 'payload/project/reference-map.md',
    'payload/knowledge/README.md', 'payload/knowledge/examples/example-guide/guide.md',
    'payload/knowledge/examples/example-guide/assets/example-diagram.svg',
    'payload/examples/copilot-instructions.md',
    'payload/skills/ca-jira-ticket-init/SKILL.md',
    'payload/skills/ca-jira-ticket-archive/SKILL.md', 'payload/skills/ca-jira-ticket-restore/SKILL.md',
    'payload/skills/ca-jira-ticket-init/scripts/ticket.py',
    'payload/skills/ca-jira-ticket-init/templates/brief.md',
    'payload/skills/ca-jira-ticket-init/templates/plan.md',
    'payload/skills/ca-jira-ticket-init/templates/review.md',
    'payload/skills/ca-jira-ticket-init/templates/notes.md',
    'payload/skills/ca-change-review/SKILL.md', 'payload/skills/ca-change-review/resources/review-checklist.md',
    'payload/skills/ca-config-audit/SKILL.md',
    'payload/skills/ca-workspace-refresh/SKILL.md',
]

# Canonical sources for the three enclosing user entrypoints. They are shipped
# once, at the ZIP root, and are not inputs read by the initializer's manifest.
ENTRYPOINTS = {
    'README.md': 'README.md',
    'Start macOS.command': 'launchers/Start macOS.command',
    'Start Windows.cmd': 'launchers/Start Windows.cmd',
}


def mapping(directory_id, path, render='copy', owner='user'):
    return {'directory_id': directory_id, 'relative_path': path, 'render': render, 'owner': owner}


def source_file(package, name):
    p = package / name
    for candidate in [package] + [package / parent for parent in reversed(p.relative_to(package).parents)] + [p]:
        info = candidate.lstat()
        if candidate.is_symlink() or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise ValueError('Redirected release input: ' + name)
    if not stat.S_ISREG(p.lstat().st_mode):
        raise ValueError('Non-ordinary release input: ' + name)
    return p


def release_versions(package=PACKAGE):
    """Read literal constants without importing or executing runtime code."""
    path = source_file(package, 'scripts/workspace_manager.py')
    try:
        tree = ast.parse(path.read_bytes(), filename=str(path))
    except SyntaxError as exc:
        raise ValueError('Invalid runtime source: ' + str(exc)) from exc
    versions = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in ('VERSION', 'DESIGN_VERSION'):
                    if target.id in versions or not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, str):
                        raise ValueError('Release versions must be unique literal string constants.')
                    versions[target.id] = node.value.value
    if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', versions.get('VERSION', '')):
        raise ValueError('VERSION must use MAJOR.MINOR.PATCH.')
    if not re.fullmatch(r'[0-9]+\.[0-9]+', versions.get('DESIGN_VERSION', '')):
        raise ValueError('DESIGN_VERSION must use MAJOR.MINOR independently of VERSION.')
    return versions['VERSION'], versions['DESIGN_VERSION']


def outer_readme(data):
    # Relocate the user README to the ZIP root. The repository's independent
    # README is never read or overwritten by release preparation.
    return re.sub(rb'(\]\()(?![a-zA-Z][a-zA-Z0-9+.-]*:|/|#)([^)]+)(\))',
                  lambda match: match[1] + b'WORKSPACE_SETUP/' + match[2] + match[3], data)


def default_output(directory, package=PACKAGE):
    version, _ = release_versions(package)
    return Path(directory) / ('code-ai-workspace-' + version + '-macos-pilot.zip')


def manifest(package=PACKAGE):
    if (package / 'installed-state.json').exists():
        raise ValueError('Build releases from reviewed source, never an installed personal copy.')
    files = []
    for name in sorted(INVENTORY):
        if name.startswith("payload/skills/") and not Path(name).parts[2].startswith("ca-"):
            raise ValueError("Framework skill names must use the ca- prefix: " + name)
        p = source_file(package, name)
        destinations = []
        if name == 'LICENSE':
            destinations.append(mapping('ai_work', 'tools/LICENSE', owner='framework'))
        elif name == 'payload/root/README.md':
            destinations.append(mapping('root', 'README.md', 'markdown', 'generated'))
        elif name == 'payload/root/gitignore.txt':
            destinations.append(mapping('root', '.gitignore', 'markdown', 'generated'))
        elif name == 'scripts/workspace_manager.py':
            destinations.append(mapping('ai_work', 'tools/workspace_manager.py', owner='framework'))
        elif name in ('scripts/terminal_output_formatter.py', 'scripts/vscode_workspace_updater.py'):
            destinations.append(mapping('ai_work', 'tools/' + p.name, owner='framework'))
        elif name.startswith('launchers/refresh_vscode_workspace '):
            destinations.append(mapping('root', p.name, 'markdown', 'framework'))
        elif name == 'payload/root/DAILY_WORK.md':
            destinations.append(mapping('ai_work', 'DAILY_WORK.md', 'markdown', 'generated'))
        elif name == 'payload/root/copilot-instructions.md':
            destinations.append(mapping('ai_work', '.github/copilot-instructions.md', 'markdown', 'user'))
        elif name == 'payload/root/COPILOT_GUIDE.md':
            destinations.append(mapping('ai_work', 'COPILOT_GUIDE.md', 'markdown', 'generated'))
        elif name.startswith('payload/project/'):
            destinations.append(mapping('ai_work', name.removeprefix('payload/')))
        elif name.startswith('payload/knowledge/'):
            destinations.append(mapping('knowledge', name.removeprefix('payload/knowledge/')))
        elif name.startswith('payload/skills/'):
            destinations.append(mapping('ai_work', '.github/' + name.removeprefix('payload/'), owner='framework' if name.endswith('/scripts/ticket.py') else 'user'))
        entry = {'source': name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'destinations': destinations}
        if name == 'settings.json':
            entry['mutable'] = True
        files.append(entry)
    version, design_version = release_versions(package)
    return {'schema_version': 1, 'package_version': version, 'design_version': design_version,
            'minimum_python': '3.9', 'files': files,
            'directories': []}


def build(output=None, package=PACKAGE):
    release = manifest(package)  # Validate every allowlisted input before preparing files.
    for name in ENTRYPOINTS.values():
        source_file(package, name)
    if output is not None:
        output = Path(output)
        if not output.is_absolute() or not output.parent.is_dir() or output.exists() or output.is_symlink():
            raise ValueError('Release output must be an absent absolute path with an existing parent.')
        sidecar = Path(str(output) + '.sha256')
        if sidecar.exists() or sidecar.is_symlink():
            raise ValueError('Checksum output already exists.')
    readme_path = source_file(package, 'README.md')
    original = readme_path.read_bytes()
    readme, count = re.subn(rb'(?m)^(\*\*Package version:\*\* )[0-9]+\.[0-9]+\.[0-9]+(?=\r?$)',
                            lambda match: match[1] + release['package_version'].encode('ascii'), original)
    if count != 1:
        raise ValueError('README.md must contain exactly one Package version label.')
    if readme != original:
        readme_path.write_bytes(readme)
    release = manifest(package)
    data = (json.dumps(release, indent=2) + '\n').encode()
    (package / 'package-manifest.json').write_bytes(data)
    if output is not None:
        # One versioned enclosing folder keeps the package together with any extractor.
        prefix = 'Code-AI-Setup-' + release['package_version'] + '/'
        # Exclusive creation. Normalized timestamps make the release content reproducible.
        with output.open('xb') as stream, zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED) as archive:
            members = {'WORKSPACE_SETUP/' + name: name for name in INVENTORY + ['package-manifest.json']}
            members.update(ENTRYPOINTS)
            for member, name in sorted(members.items()):
                info = zipfile.ZipInfo(prefix + member, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = (0o100755 if member == 'Start macOS.command' else 0o100644) << 16
                content = (package / name).read_bytes()
                if member == 'README.md':
                    content = outer_readme(content)
                archive.writestr(info, content)
        with sidecar.open('x', encoding='utf-8') as stream:
            stream.write(hashlib.sha256(output.read_bytes()).hexdigest() + '  ' + output.name + '\n')
    return len(INVENTORY)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    destination = parser.add_mutually_exclusive_group()
    destination.add_argument('--output', help='New absolute ZIP path with a custom filename')
    destination.add_argument('--output-dir', help='Existing absolute directory; use the versioned default ZIP filename')
    args = parser.parse_args(argv)
    if sys.version_info < (3, 9):
        parser.error('Python 3.9+ required')
    try:
        output = default_output(args.output_dir) if args.output_dir is not None else args.output
        print('Release manifest built for', build(output), 'allowlisted user-package input files.')
        if output is not None:
            print('ZIP:', output)
            print('Checksum:', str(output) + '.sha256')
        return 0
    except (OSError, ValueError) as exc:
        print('Error: ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
