#!/usr/bin/env python3
"""
tools/check_readmes.py

Scans top-level directories and reports folders missing README.md. Optionally creates a README stub.

Usage:
    python tools/check_readmes.py --list
    python tools/check_readmes.py --create-stubs
"""

import os
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
FOLDERS_TO_CHECK = [p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith('.')]

README_STUB = """# {folder}

This folder contains notebooks and resources for the {folder} module. Please refer to the repository README for running instructions.
"""


def list_missing():
    missing = []
    for d in FOLDERS_TO_CHECK:
        if not (d / 'README.md').exists():
            missing.append(d)
    return missing


def create_stubs():
    for d in list_missing():
        p = d / 'README.md'
        with p.open('w', encoding='utf-8') as fh:
            fh.write(README_STUB.format(folder=d.name))
        print(f'Created stub: {p}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true', help='List folders missing README.md')
    parser.add_argument('--create-stubs', action='store_true', help='Create README.md stubs in missing folders')
    args = parser.parse_args()

    if args.list:
        missing = list_missing()
        if not missing:
            print('All folders have README.md')
        else:
            print('Folders missing README.md:')
            for m in missing:
                print(f' - {m}')
    if args.create_stubs:
        create_stubs()
