#!/usr/bin/env python3
"""Deterministic regenerator for target-id snapshots used by the reference-integrity report.

Run locally before opening a PR that touches cross-catalogue references. Re-commits
the snapshot YAML with the resolved commit SHAs of the target repositories.

Usage: python3 scripts/build_target_snapshots.py [--update-shas]
  --update-shas     re-fetch the current HEAD of each target repo (requires git remotes
                    to the local clones or to be in the surrounding /home/hermes/dea-work/).
  (no flag)         default; generate from the local target-repo clones (paths in TARGET_REPOS).

This script is the single source of truth for the vendored target-id snapshots. The CI
validator reads the snapshot YAML and NEVER re-fetches at run time, so CI is deterministic
and offline-safe. Local regeneration (--update-shas or default) ensures the snapshot
reflects the pinned target-repo HEAD.
"""

from __future__ import annotations
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
import yaml

WORKDIR = Path(__file__).resolve().parent.parent
TARGET_REPOS = {
    'dea-catalog-business-capabilities':     '/home/hermes/dea-work/dea-catalog-business-capabilities',
    'dea-catalog-processes':                 '/home/hermes/dea-work/dea-catalog-processes',
    'dea-catalog-application-components':    '/home/hermes/dea-work/dea-catalog-application-components',
}

ID_PREFIX = {
    'dea-catalog-business-capabilities':     'capabilities:',
    'dea-catalog-processes':                 'dea:process-',
    'dea-catalog-application-components':    'dea:information-system-component-',
}


def git_short_sha(repo_path: Path) -> str:
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=str(repo_path)).decode().strip()
    except Exception:
        return 'unknown'


def harvest(repo_path: Path, prefix: str) -> dict:
    """Walk entities/v1-alpha/*.yaml files; collect id, name, definition/outcome."""
    snap = {}
    for f in repo_path.glob('entities/v1-alpha/**/*.yaml'):
        s = str(f)
        if '/candidates/' in s or '/retired/' in s:
            continue
        try:
            d = yaml.safe_load(open(f))
        except Exception:
            continue
        if not isinstance(d, dict) or 'id' not in d:
            continue
        if not isinstance(d['id'], str) or not d['id'].startswith(prefix):
            continue
        snap[d['id']] = {
            'name': d.get('name'),
            'definition_or_outcome': (d.get('definition') or d.get('outcome') or '')[:180],
            'source_file': str(f).replace(str(repo_path) + '/', ''),
        }
    return snap


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--update-shas', action='store_true', help='Re-read current HEAD of each target repo')
    args = ap.parse_args()

    snapshots = {}
    pinned = {}
    for repo_name, repo_path in TARGET_REPOS.items():
        repo = Path(repo_path)
        if not repo.exists():
            print(f"WARN: target repo path does not exist: {repo}", file=sys.stderr)
            continue
        prefix = ID_PREFIX[repo_name]
        snapshots[repo_name] = harvest(repo, prefix)
        pinned[repo_name] = git_short_sha(repo)

    out_path = WORKDIR / 'docs' / 'is-semantic-architecture' / 'target-id-snapshots.yaml'
    doc = {
        'schema': 'dea.is.target-id-snapshots.v1',
        'generated_by': 'scripts/build_target_snapshots.py',
        'generated_for': 'CR-IS-CAT-01R reference integrity resolution (hardened validator)',
        'pinned_commits': pinned,
        'snapshots': {repo: dict(sorted(ids.items())) for repo, ids in snapshots.items()},
        'counts': {repo: len(ids) for repo, ids in snapshots.items()},
    }
    open(out_path, 'w').write(yaml.safe_dump(doc, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200))
    print(f"WROTE {out_path}")
    for repo, count in doc['counts'].items():
        print(f"  {repo:42} {count:>4} ids @ {pinned[repo][:12]}")


if __name__ == '__main__':
    main()
