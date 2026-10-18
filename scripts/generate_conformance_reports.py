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
        'by_source_domain': Counter(
            next((f.get('functional_domain') for f in functions if f['id'] == r['source_id']), 'external')
            for r in relationships
        ),
        'by_target_kind': Counter(
            'internal' if r['target_id'] in {f['id'] for f in functions} else 'external'
            for r in relationships
        ),
    }


def report_reference_integrity(relationships, functions):
    """Per-entity reference integrity."""
    function_ids = {f['id'] for f in functions}
    unresolved = [r for r in relationships if r['target_id'] not in function_ids and not r['target_id'].startswith(('dea:business-capability-', 'dea:business-process-', 'dea:information-system-component-', 'dea:information-system-service-', 'dea:integration-interface-', 'dea:data-entity-', 'dea:event-', 'dea:metric-'))]
    return {
        'version': '1.0',
        'date': '2026-10-18',
        'cr': 'CR-IS-CAT-01D',
        'total_relationships': len(relationships),
        'internal_references': sum(1 for r in relationships if r['target_id'] in function_ids),
        'external_references': sum(1 for r in relationships if r['target_id'] not in function_ids),
        'unresolved_references': len(unresolved),
        'unresolved': [r['id'] for r in unresolved],
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
