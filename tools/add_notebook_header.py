#!/usr/bin/env python3
"""
tools/add_notebook_header.py

Inserts a standardized Markdown header cell into Jupyter notebooks that do not already contain one.
This script is intended to help make notebooks reviewer-ready.

Usage:
    python tools/add_notebook_header.py --dry-run
    python tools/add_notebook_header.py --apply
"""

import json
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = list(ROOT.rglob('*.ipynb'))

HEADER = """# {title}

Authors: {author}
Date: {date}
Estimated run time: ~X minutes
Requirements: see repository `requirements.txt`

## Learning objectives
- 

## Data
- Source: 
- Expected files: `data/`
- Schema: 

## Notes
- Random seed: `RANDOM_SEED = 42`
"""


def has_header(nb_json):
    # Look for a top-level markdown cell with 'Learning objectives' or 'Data' headings
    for cell in nb_json.get('cells', [])[:3]:
        if cell.get('cell_type') == 'markdown':
            src = ''.join(cell.get('source', []))
            if 'Learning objectives' in src or '## Learning objectives' in src:
                return True
    return False


def apply_header(path, dry_run=True):
    with path.open('r', encoding='utf-8') as f:
        nb = json.load(f)
    if has_header(nb):
        return False
    # Create a markdown cell
    title = path.stem.replace('_', ' ').title()
    md = HEADER.format(title=title, author='Author Name', date='YYYY-MM-DD')
    cell = {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [md]
    }
    nb['cells'].insert(0, cell)
    if not dry_run:
        with path.open('w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Do not modify files, only report')
    parser.add_argument('--apply', action='store_true', help='Apply changes to notebooks')
    args = parser.parse_args()

    modified = []
    for nb in NOTEBOOKS:
        try:
            changed = apply_header(nb, dry_run=not args.apply)
            if changed:
                modified.append(nb)
        except Exception as e:
            print(f'Error processing {nb}: {e}')

    if not modified:
        print('No notebooks require header insertion or none found.')
    else:
        print('Notebooks that would be/are modified:')
        for m in modified:
            print(f' - {m}')
