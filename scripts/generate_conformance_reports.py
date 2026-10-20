#!/usr/bin/env python3
"""CR-IS-CAT-01D conformance report generator.

Generates the 5 conformance reports at reports/*.yaml from the current
state of the catalogue. The generator is deterministic; re-running
produces the same reports. Per G-10, all generated artefacts must be
reproducible and validated.

Usage:
  python3 scripts/generate_conformance_reports.py
"""
import os
import glob
import yaml
from pathlib import Path
from collections import Counter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)


def load_functions():
    out = []
    for f in glob.glob('entities/v1-alpha/domains/*/functions/*/function.yaml'):
        with open(f) as fp:
            d = yaml.safe_load(fp)
        d['_path'] = f
        out.append(d)
    return out


def load_taxonomy():
    with open('taxonomy/functional-domains.yaml') as fp:
        return yaml.safe_load(fp)


def load_relationships():
    with open('relationships/v1-alpha/relationships.yaml') as fp:
        return yaml.safe_load(fp)['relationships']


def report_catalogue_conformance(functions, taxonomy, relationships):
    """Overall conformance summary."""
    return {
        'version': '1.0',
        'date': '2026-10-18',
        'cr': 'CR-IS-CAT-01D',
        'total_functions': len(functions),
        'total_domains': len(taxonomy['domains']),
        'total_relationships': len(relationships),
        'domains': [
            {
                'id': d['id'],
                'code': d['code'],
                'name': d['name'],
                'status': d['status'],
                'function_count': sum(1 for f in functions if f.get('functional_domain') == d['id']),
            }
            for d in taxonomy['domains']
        ],
        'conformance_level': 'P1-populated (5/15 domains populated)',
        'governance': 'G-01..G-12 acknowledged; see change-requests/CR-IS-CAT-01D-integration.md',
    }


def report_relationship_coverage(relationships, functions):
    """Per-relationship coverage."""
    rel_type_counts = Counter(r['relationship_type'] for r in relationships)
    return {
        'version': '1.0',
        'date': '2026-10-18',
        'cr': 'CR-IS-CAT-01D',
        'total_relationships': len(relationships),
        'by_type': dict(rel_type_counts),
        'by_source_domain': dict(Counter(
            next((f.get('functional_domain') for f in functions if f['id'] == r['source_id']), 'external')
            for r in relationships
        )),
        'by_target_kind': dict(Counter(
            'internal' if r['target_id'] in {f['id'] for f in functions} else 'external'
            for r in relationships
        )),
    }


def report_reference_integrity(relationships, functions):
    """Cross-catalogue reference integrity: real resolution against target-id snapshots.
       Three buckets: resolved (target id exists in target repo), forward (declared forward,
       target repo named, target repo may be empty), unresolved (everything else -- hard fail).
       CR-IS-CAT-01R hardened this from prefix-match-only to snapshot-based resolution.
    """
    import yaml
    # Load the cross-catalogue reference map and target-id snapshots
    map_path = Path(__file__).resolve().parent.parent / 'docs' / 'is-semantic-architecture' / 'cross-catalogue-reference-map.yaml'
    snap_path = Path(__file__).resolve().parent.parent / 'docs' / 'is-semantic-architecture' / 'target-id-snapshots.yaml'
    ref_map = yaml.safe_load(open(map_path)) if map_path.exists() else {}
    snapshots = yaml.safe_load(open(snap_path)) if snap_path.exists() else {}
    snap_pinned = (snapshots or {}).get('pinned_commits', {}) or {}
    snap_data = (snapshots or {}).get('snapshots', {}) or {}

    # Build the set of valid ids per target catalogue
    valid_ids = {}
    for repo_name, ids in snap_data.items():
        if isinstance(ids, dict):
            valid_ids[repo_name] = set(ids.keys())

    # Build forward-ref declarations indexed by legacy id and by canonical target_repo
    forward_refs = {}
    for fr in (ref_map.get('forward_references') or []):
        forward_refs[fr['legacy']] = fr

    # Walk every external reference on every relationship AND every function record
    function_ids = {f['id'] for f in functions}
    buckets = {'resolved': [], 'forward': [], 'unresolved': []}
    seen_target_ids = {}

    def classify(target_id, source_record_id=None):
        if target_id in function_ids:
            buckets['resolved'].append({'target_id': target_id,'record_id': source_record_id,'kind': 'internal'})
            return
        # Forward ref declared?
        if target_id in forward_refs:
            rec = forward_refs[target_id]
            buckets['forward'].append({'target_id': target_id, 'record_id': source_record_id, 'target_repo': rec.get('target_repo'), 'owning_cr': rec.get('rationale')})
            return
        # Try to resolve against each target-repo snapshot
        for repo_name, ids in valid_ids.items():
            if target_id in ids:
                buckets['resolved'].append({'target_id': target_id, 'record_id': source_record_id, 'kind': 'external', 'target_repo': repo_name})
                return
        buckets['unresolved'].append({'target_id': target_id, 'record_id': source_record_id})
        return

    for r in relationships:
        classify(r['target_id'], r.get('id'))

    # Also check refs in function records
    for f in functions:
        for c in (f.get('business_alignment') or {}).get('realized_capabilities') or []:
            classify(c, f.get('id') + '.realized_capabilities')
        for p in (f.get('business_alignment') or {}).get('enabled_processes') or []:
            classify(p, f.get('id') + '.enabled_processes')
        for c in f.get('executing_components') or []:
            classify(c, f.get('id') + '.executing_components')
        for c in f.get('child_functions') or []:
            classify(c, f.get('id') + '.child_functions')

    return {
        'version': '2.0',
        'date': '2026-10-19',
        'cr': 'CR-IS-CAT-01R',
        'check': 'real resolution against vendored target-id snapshots; rebased via cross-catalogue reference map',
        'target_repo_pinning': snap_pinned,
        'total_references_classified': sum(len(v) for v in buckets.values()),
        'resolved_count':   len(buckets['resolved']),
        'forward_count':    len(buckets['forward']),
        'unresolved_count': len(buckets['unresolved']),
        'unresolved':       buckets['unresolved'],
        'forward':          buckets['forward'],
        'resolved':         buckets['resolved'],
        'passes_resolved_check_when': 'unresolved_count == 0',
    }



def report_taxonomy_coverage(taxonomy, functions):
    """Per-taxonomy coverage."""
    return {
        'version': '1.0',
        'date': '2026-10-18',
        'cr': 'CR-IS-CAT-01D',
        'total_domains': len(taxonomy['domains']),
        'populated_domains': sum(1 for d in taxonomy['domains'] if any(f.get('functional_domain') == d['id'] for f in functions)),
        'unpopulated_domains': [d['id'] for d in taxonomy['domains'] if not any(f.get('functional_domain') == d['id'] for f in functions)],
        'by_domain': {
            d['id']: {
                'function_count': sum(1 for f in functions if f.get('functional_domain') == d['id']),
                'functions': sorted([f['id'] for f in functions if f.get('functional_domain') == d['id']]),
            }
            for d in taxonomy['domains']
        },
    }


def report_documentation_coverage(functions):
    """Per-function documentation coverage."""
    missing_readme = [f['id'] for f in functions if not os.path.exists(f['_path'].replace('function.yaml', 'README.md'))]
    return {
        'version': '1.0',
        'date': '2026-10-18',
        'cr': 'CR-IS-CAT-01D',
        'total_functions': len(functions),
        'with_readme': len(functions) - len(missing_readme),
        'missing_readme': missing_readme,
        'coverage_pct': round(100 * (len(functions) - len(missing_readme)) / len(functions) if functions else 0, 2),
    }


def main():
    functions = load_functions()
    taxonomy = load_taxonomy()
    relationships = load_relationships()

    os.makedirs('reports', exist_ok=True)

    reports = {
        'catalogue-conformance': report_catalogue_conformance(functions, taxonomy, relationships),
        'relationship-coverage': report_relationship_coverage(relationships, functions),
        'reference-integrity': report_reference_integrity(relationships, functions),
        'taxonomy-coverage': report_taxonomy_coverage(taxonomy, functions),
        'documentation-coverage': report_documentation_coverage(functions),
    }

    for name, data in reports.items():
        path = f'reports/{name}.yaml'
        with open(path, 'w') as fp:
            yaml.dump(data, fp, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200)
        print(f'OK: {path}')

    print(f'Total functions: {len(functions)}')
    print(f'Total relationships: {len(relationships)}')
    print(f'Total domains: {len(taxonomy["domains"])}')


if __name__ == '__main__':
    main()
