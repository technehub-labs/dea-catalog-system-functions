#!/usr/bin/env python3
"""F2 record shape parity validator.

Asserts that every F2 record in the catalogue has the same shape. Used to enforce
"P1 F2 parity": the P1 F2 `identity-and-access-management` is the canonical shape,
P2 F2s emitted by `generate_p2_population.py` match it. CI may invoke this via
`.github/workflows/validate-catalogue.yml`.

Usage: python3 scripts/validate_f2_record_shape.py
"""

from __future__ import annotations
import glob, sys
import yaml
from pathlib import Path


EXPECTED_F2_KEYS = {
 'id', 'type', 'name', 'description', 'version', 'lifecycle_status',
 'functional_domain', 'category', 'decomposition_level',
 'child_functions', 'decomposition_rationale', 'responsibility_allocation',
 'orchestration_responsibility', 'inputs', 'outputs', 'execution_characteristics',
 'business_alignment', 'executing_components', 'non_functional_characteristics',
 'governance', 'references', 'metadata',
}
EXPECTED_GOVERNANCE_KEYS = {
 'functional_owner', 'steward', 'approval_status', 'criticality',
 'lifecycle_history', 'review_date', 'source_and_evidence', 'change_history',
}
EXPECTED_BUS_ALIGN_KEYS  = { 'realized_capabilities', 'enabled_processes' }
EXPECTED_EXEC_CHAR_KEYS  = {
 'execution_pattern', 'trigger_mechanism', 'processing_mode',
 'synchronous_asynchronous', 'idempotency', 'retry_recovery',
 'error_handling', 'transactional', 'concurrency',
}
EXPECTED_NFR_KEYS        = {
 'availability', 'performance_latency', 'throughput', 'scalability',
 'resilience', 'security', 'privacy', 'auditability', 'recoverability',
 'observability', 'compliance_constraints',
}


def check_f2_record(d):
    errors = []
    keys = set(d.keys())
    missing = EXPECTED_F2_KEYS - keys
    extra = keys - EXPECTED_F2_KEYS
    if missing: errors.append(f'missing keys: {sorted(missing)}')
    if extra: errors.append(f'extra keys: {sorted(extra)}')
    if not isinstance(d.get('child_functions', None), list):
        errors.append('child_functions should be an array')
    if not isinstance(d.get('responsibility_allocation', None), list):
        errors.append('responsibility_allocation should be an array')
    if d.get('responsibility_allocation'):
        ra = d['responsibility_allocation'][0]
        if not isinstance(ra, dict) or 'child' not in ra or 'responsibility' not in ra:
            errors.append('responsibility_allocation[0] should be {child, responsibility}')
    if not isinstance(d.get('inputs', None), list):
        errors.append('inputs should be an array')
    if not isinstance(d.get('outputs', None), list):
        errors.append('outputs should be an array')
    if not isinstance(d.get('executing_components', None), list):
        errors.append('executing_components should be an array')
    gov = d.get('governance')
    if isinstance(gov, dict):
        gk = set(gov.keys())
        g_missing = EXPECTED_GOVERNANCE_KEYS - gk
        if g_missing: errors.append(f'governance missing keys: {sorted(g_missing)}')
    ba = d.get('business_alignment')
    if isinstance(ba, dict):
        if set(ba.keys()) != EXPECTED_BUS_ALIGN_KEYS:
            errors.append(f'business_alignment keys: {sorted(set(ba.keys()))}')
    ec = d.get('execution_characteristics')
    if isinstance(ec, dict):
        ek = set(ec.keys())
        e_missing = EXPECTED_EXEC_CHAR_KEYS - ek
        if e_missing: errors.append(f'execution_characteristics missing keys: {sorted(e_missing)}')
    nfr = d.get('non_functional_characteristics')
    if isinstance(nfr, dict):
        nk = set(nfr.keys())
        n_missing = EXPECTED_NFR_KEYS - nk
        if n_missing: errors.append(f'non_functional_characteristics missing keys: {sorted(n_missing)}')
    return errors


def main():
    """Run F2 record shape parity. Returns 1 if any P2-domain F2 record fails; P1 findings are warnings only (covered by CR-IS-CAT-01C-P1H)."""
    repo = Path('.').resolve()
    p1_failures = []; p2_failures = []
    p1_records = 0; p2_records = 0
    for f in glob.glob(str(repo / 'entities' / 'v1-alpha' / 'domains' / '*' / 'functions' / '*' / 'function.yaml')):
        d = yaml.safe_load(open(f))
        if d.get('decomposition_level') != 'F2': continue
        domain_id = d.get('functional_domain', '')
        is_p2 = any(s in domain_id for s in [
            'communication-and-collaboration','content-and-knowledge-management',
            'analytics-and-decision-support','security-privacy-and-trust',
            'monitoring-and-observability','configuration-and-administration'])
        if is_p2: p2_records += 1
        else:     p1_records += 1
        errors = check_f2_record(d)
        if not errors: continue
        if is_p2: p2_failures.append((f, errors))
        else:     p1_failures.append((f, errors))
    print()
    if p2_failures:
        print('P2 F2 record failures (must fix in CR-IS-CAT-01C-P2H):')
        for f, errs in p2_failures:
            print(f'  FAIL: {f}')
            for e in errs:
                print(f'      - {e}')
    if p1_failures:
        print('P1 F2 record findings (separate slice CR-IS-CAT-01C-P1H; warning not blocker):')
        for f, errs in p1_failures:
            print(f'  WARN: {f}')
            for e in errs:
                print(f'      - {e}')
    print()
    print(f'P2 F2 records checked: {p2_records} (failures: {len(p2_failures)})')
    print(f'P1 F2 records checked: {p1_records} (warnings: {len(p1_failures)})')
    return 0 if len(p2_failures) == 0 else 1



if __name__ == '__main__':
    sys.exit(main())
