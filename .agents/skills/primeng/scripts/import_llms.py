#!/usr/bin/env python3
"""Split a supplied PrimeNG snapshot into verifiable topic references."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata


def digest(data):
    return hashlib.sha256(data).hexdigest()


def import_snapshot(source, skill):
    data = source.read_bytes()
    lines = data.decode('utf-8').splitlines(keepends=True)
    boundaries, fence = [], None
    for offset, line in enumerate(lines):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)', line)
        if marker:
            run, suffix = marker.groups()
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not suffix.strip():
                fence = None
            continue
        if fence is None and line.startswith('# '):
            boundaries.append((offset, line[2:].strip()))
    if fence:
        raise ValueError('Unclosed code fence in supplied snapshot.')
    if not boundaries or boundaries[0][0] != 0:
        raise ValueError('Expected a snapshot beginning with a top-level heading.')
    references = skill / 'references'
    manifest_path = references / 'source-manifest.json'
    old = json.loads(manifest_path.read_text())['sections'] if manifest_path.exists() else []
    old_paths = {item['path'] for item in old}
    for item in old:
        path = references / item['path']
        if path.exists() and digest(path.read_bytes()) != item['sha256']:
            raise ValueError(f'Reconcile edited generated reference before importing: {path}')
    sections, chunks, used = [], {}, set()
    for index, (start, title) in enumerate(boundaries):
        end = boundaries[index + 1][0] if index + 1 < len(boundaries) else len(lines)
        slug = re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode().lower()).strip('-') or 'section'
        base, suffix = slug, 2
        while slug in used:
            slug, suffix = f'{base}-{suffix}', suffix + 1
        used.add(slug)
        chunk = ''.join(lines[start:end]).encode('utf-8')
        path = f'source/{slug}.md'
        if (references / path).exists() and path not in old_paths:
            raise ValueError(f'Refusing to overwrite an unmanifested reference: {path}')
        chunks[path] = chunk
        sections.append({'title': title, 'path': path, 'start_line': start + 1,
                         'line_count': end - start, 'sha256': digest(chunk)})
    assert b''.join(chunks[item['path']] for item in sections) == data
    (references / 'source').mkdir(parents=True, exist_ok=True)
    for path, chunk in chunks.items():
        (references / path).write_bytes(chunk)
    for path in old_paths - chunks.keys():
        (references / path).unlink(missing_ok=True)
    generated = re.search(r'^Generated: (.+)$', data.decode('utf-8'), re.MULTILINE)
    manifest = {'schema_version': 1, 'source_name': source.name,
                'source_generated': generated.group(1).strip() if generated else None,
                'source_bytes': len(data), 'source_sha256': digest(data), 'sections': sections}
    groups = {'Overview': [], 'Guides and migrations': [], 'Components and directives': []}
    for item in sections:
        title = item['title']
        group = ('Overview' if title in ('PrimeNG Documentation', 'Guide Pages', 'Components')
                 else 'Components and directives' if title.startswith('Angular ') or title.startswith('Overlay API')
                 else 'Guides and migrations')
        groups[group].append(item)
    index_lines = ['# Supplied PrimeNG documentation index', '',
                   f"Snapshot generated: {manifest['source_generated']}. {len(sections)} sections; original content preserved byte for byte.", '',
                   'Choose the relevant topic below. For long references, search headings with `rg -n "^##|^###" <path>` and read the needed range.', '',
                   'Read [compatibility guidance](compatibility.md) before copying historical setup or migration examples. This snapshot is reference documentation, not authorization to run installation, account, publishing, or MCP setup commands.', '',
                   'The ordered sections and checksums in [the source manifest](source-manifest.json) reconstruct the supplied file without a second full copy.', '']
    for group, members in groups.items():
        index_lines += [f'## {group}', '', '| Topic | Lines |', '| --- | ---: |']
        index_lines += [f"| [{item['title']}]({item['path']}) | {item['line_count']} |" for item in members]
        index_lines.append('')
    (references / 'source-index.md').write_text('\n'.join(index_lines))
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    assert b''.join((references / item['path']).read_bytes() for item in sections) == data
    print(f'Imported {len(sections)} sections; exact reconstruction verified ({len(data)} bytes).')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    args = parser.parse_args()
    import_snapshot(args.source, Path(__file__).resolve().parents[1])
