#!/usr/bin/env python3
"""Maintainer-only allowlisted manifest/release builder; not an initialization step."""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from pathlib import Path
import stat
import zipfile

PACKAGE = Path(__file__).absolute().parent.parent
# Deliberately explicit. User data or newly added files are never picked up implicitly.
INVENTORY = [
    'README.md', 'DESIGN.md', 'SETUP_GUIDE.md', 'CHANGELOG.md', 'VALIDATION_REPORT.md', '.gitignore',
    'scripts/workspace.py', 'scripts/workspace_manager.py', 'scripts/terminal_output_formatter.py', 'scripts/vscode_workspace_updater.py', 'settings.json', 'scripts/start.py', 'scripts/build_release.py', 'tests/test_workspace.py',
    'launchers/Start macOS.command', 'launchers/Start Windows.cmd',
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
]


def mapping(directory_id, path, render='copy', owner='user'):
    return {'directory_id': directory_id, 'relative_path': path, 'render': render, 'owner': owner}


def manifest(package=PACKAGE):
    if (package / 'installed-state.json').exists():
        raise ValueError('Build releases from reviewed source, never an installed personal copy.')
    files = []
    for name in sorted(INVENTORY):
        if name.startswith("payload/skills/") and not Path(name).parts[2].startswith("ca-"):
            raise ValueError("Framework skill names must use the ca- prefix: " + name)
        p = package / name
        for component in [package] + list(reversed(p.relative_to(package).parents)):
            candidate = component if component == package else package / component
            if candidate.exists() and (candidate.is_symlink() or getattr(candidate.lstat(), 'st_file_attributes', 0) & 0x400):
                raise ValueError('Redirected release input parent: ' + name)
        if p.is_symlink() or getattr(p.lstat(), 'st_file_attributes', 0) & 0x400 or not stat.S_ISREG(p.lstat().st_mode):
            raise ValueError('Non-ordinary release input: ' + name)
        destinations = []
        if name == 'payload/root/README.md':
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
    return {'schema_version': 1, 'package_version': '0.1.16', 'design_version': '1.0',
            'minimum_python': '3.9', 'files': files,
            'directories': []}


def build(output=None, package=PACKAGE):
    release = manifest(package)
    data = (json.dumps(release, indent=2) + '\n').encode()
    if output is not None:
        output = Path(output)
        if not output.is_absolute() or not output.parent.is_dir() or output.exists() or output.is_symlink():
            raise ValueError('Release output must be an absent absolute path with an existing parent.')
        sidecar = Path(str(output) + '.sha256')
        if sidecar.exists() or sidecar.is_symlink():
            raise ValueError('Checksum output already exists.')
    (package / 'package-manifest.json').write_bytes(data)
    if output is not None:
        # One versioned enclosing folder keeps the package together with any extractor.
        prefix = 'Code-AI-Setup-' + release['package_version'] + '/'
        # Exclusive creation. Normalized timestamps make the release content reproducible.
        with output.open('xb') as stream, zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED) as archive:
            members = {'WORKSPACE_SETUP/' + name: name for name in INVENTORY + ['package-manifest.json']}
            members.update({'README.md': 'README.md', 'Start macOS.command': 'launchers/Start macOS.command', 'Start Windows.cmd': 'launchers/Start Windows.cmd'})
            for member, name in sorted(members.items()):
                info = zipfile.ZipInfo(prefix + member, date_time=(2026, 10, 25, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = (0o100755 if member == 'Start macOS.command' else 0o100644) << 16
                content = (package / name).read_bytes()
                if member == 'README.md':
                    content = content.replace(b'(SETUP_GUIDE.md)', b'(WORKSPACE_SETUP/SETUP_GUIDE.md)').replace(b'(settings.json)', b'(WORKSPACE_SETUP/settings.json)').replace(b'(VALIDATION_REPORT.md)', b'(WORKSPACE_SETUP/VALIDATION_REPORT.md)')
                archive.writestr(info, content)
        with sidecar.open('x', encoding='utf-8') as stream:
            stream.write(hashlib.sha256(output.read_bytes()).hexdigest() + '  ' + output.name + '\n')
    return len(INVENTORY)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', help='New absolute zip path; omit to refresh only the source manifest')
    args = parser.parse_args()
    if sys.version_info < (3, 9):
        parser.error('Python 3.9+ required')
    try:
        print('Release manifest built for', build(args.output), 'allowlisted input files.')
        return 0
    except (OSError, ValueError) as exc:
        print('Error: ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
