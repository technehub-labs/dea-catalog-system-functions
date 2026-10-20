#!/usr/bin/env python3
"""F2 record shape parity validator.

Asserts that every F2 record in the catalogue matches the canonical F2 shape
originally hand-authored in CR-IS-CAT-01B (`identity-and-access-management`).
Since CR-IS-CAT-01C-P2H (P2/P3) and CR-IS-CAT-01C-P1H (P1) every F2 record in
the catalogue is generator-emitted via `scripts/_f2_record_helper.py`, so all
15 F2 records are blockers with no out-of-scope set. CI invokes this as step 7
in `.github/workflows/validate-catalogue.yml`.

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
    """Run F2 record shape parity. Every F2 record in the catalogue must match
    the canonical shape (P1 hand-edited F2 parity, per CR-IS-CAT-01C-P2H).
    Returns 1 if any F2 record fails; the catalogue has no out-of-scope set
    (P1 records were brought to shape under CR-IS-CAT-01C-P1H)."""
    repo = Path('.').resolve()
    failures = []
    p2_records = 0
    p1_records = 0
    for f in glob.glob(str(repo / 'entities' / 'v1-alpha' / 'domains' / '*' / 'functions' / '*' / 'function.yaml')):
        d = yaml.safe_load(open(f))
        if d.get('decomposition_level') != 'F2': continue
        domain_id = d.get('functional_domain', '')
        is_p2 = any(s in domain_id for s in [
            'communication-and-collaboration','content-and-knowledge-management',
            'analytics-and-decision-support','security-privacy-and-trust',
            'monitoring-and-observability','configuration-and-administration',
            'resource-and-capacity-management','ai-and-intelligent-processing',
            'experience-and-interaction','search-and-discovery'])
        if is_p2: p2_records += 1
        else:     p1_records += 1
        errors = check_f2_record(d)
        if errors: failures.append((f, errors))
    print()
    if failures:
        print('F2 record shape failures (all F2 records are blockers):')
        for f, errs in failures:
            print(f'  FAIL: {f}')
            for e in errs:
                print(f'      - {e}')
    print()
    print(f'P2/P3 F2 records checked: {p2_records} (failures: {sum(1 for f,_ in failures if any(s in f for s in ["communication","content-and","analytics","security-privacy","monitoring","configuration-and","resource-and","ai-and","experience-and","search-and"]))})')
    print(f'P1 F2 records checked: {p1_records} (failures: {len(failures) - sum(1 for f,_ in failures if any(s in f for s in ["information-and-data","transaction-processing","workflow-and","integration-and","identity-and-access"]))})')
    return 0 if len(failures) == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
