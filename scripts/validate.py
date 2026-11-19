"""Validate local LiveLabs content without network or cloud operations."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / 'workshops/tenancy/manifest.json'
manifest = json.loads(manifest_path.read_text())
errors = []
assert manifest.get('workshoptitle'), 'Missing workshop title'
assert len(manifest['tutorials']) >= 3, 'Expected introduction and at least two labs'
images = set()
acknowledgements = []
for item in manifest['tutorials']:
    path = (manifest_path.parent / item['filename']).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        errors.append(f'Invalid tutorial path: {path}')
        continue
    content = path.read_text()
    if len(re.findall(r'^# ', content, re.M)) != 1:
        errors.append(f'{path.name}: expected one H1')
    for heading in ['## Introduction', '### Objectives', '### Prerequisites', '## Task 1:']:
        if heading not in content:
            errors.append(f'{path.name}: missing {heading}')
    if re.search(r'^## Acknowledgements$', content, re.M):
        acknowledgements.append(path)
    h2 = re.findall(r'^## (.+)', content, re.M)
    if len(h2) < 2 or not h2[1].startswith('Task 1:'):
        errors.append(f'{path.name}: second H2 must start with Task 1:')
    if path.name != path.parent.name + '.md':
        errors.append(f'Lab directory and Markdown name differ: {path}')
    for alt, target in re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content):
        target = target.split(' "')[0]
        image = (path.parent / target).resolve()
        if not alt.strip() or not image.is_file() or image.parent.name != 'images':
            errors.append(f'{path.name}: invalid image {target}')
        images.add(image)
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', content):
        if not target.startswith(('https://', 'http://', '#', 'mailto:')):
            if not (path.parent / target.split('#')[0]).is_file():
                errors.append(f'{path.name}: broken local link {target}')
    if re.search(r'ABcd_|nacemc01|radunistor', content):
        errors.append(f'{path.name}: source credential or account-specific sign-in value')
if acknowledgements != [ROOT / 'introduction/introduction.md']:
    errors.append('Expected one workshop acknowledgement in the introduction')
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix in ('.md', '.png', '.html', '.json') and path.name not in ('README.md', 'AUTHOR_NOTES.md'):
        if path.name != path.name.lower():
            errors.append(f'Filename is not lowercase: {path}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(manifest["tutorials"])} modules, {len(images)} referenced images, manifest paths and required sections valid.')
