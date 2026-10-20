#!/usr/bin/env python3
"""Shared F2 record + README helper. Used by generate_p2_population.py and
generate_p3_population.py (and any future F2-emitting generator).

The canonical F2 record shape is identical to the P1 hand-edited F2
`dea:information-system-function-identity-and-access-management`. This module
single-sources the shape; generators import and call build_f2_record() to
produce records that match P1.

Usage:
    from scripts._f2_record_helper import build_f2_record, build_f2_readme
    f2_record = build_f2_record(domain, f4_records)
    readme    = build_f2_readme(f2_record, domain_id, domain_name, domain_code)
"""

from __future__ import annotations


F2_INPUT_TEXT = {
 'communication-and-collaboration':    ('collaboration-and-collaboration-event', 'Collaboration event',     'A business event that triggers the collaboration and notification flow.',                  'Caller.',         True,  'non-sensitive'),
 'content-and-knowledge-management':   ('content-lifecycle-event',                'Content lifecycle event', 'A business event that triggers the content storage and retrieval flow.',               'Caller.',         True,  'non-sensitive'),
 'analytics-and-decision-support':     ('analytical-subject-area-event',          'Analytical event',        'A business event that triggers the analytics transformation and insight generation flow.', 'Caller.',        True,  'non-sensitive'),
 'security-privacy-and-trust':         ('security-and-trust-event',               'Security event',          'A business event that triggers the security-monitoring or threat-detection flow.',     'Caller.',         True,  'sensitive'),
 'monitoring-and-observability':       ('runtime-instrumentation-event',          'Runtime event',           'A business event that triggers the metric and log instrumentation flow.',                'Caller.',         True,  'non-sensitive'),
 'configuration-and-administration':   ('configuration-change-event',             'Configuration event',     'A business event that triggers the configuration deployment and validation flow.',       'Caller.',         True,  'non-sensitive'),
 'resource-and-capacity-management':   ('capacity-demand-event',                  'Capacity demand event',   'A business event that triggers the capacity-planning and resource-provisioning flow.',   'Caller.',         True,  'non-sensitive'),
 'ai-and-intelligent-processing':      ('ai-and-intelligence-event',               'AI event',                'A business event that triggers the model-management or inference-execution flow.',         'Caller.',         True,  'non-sensitive'),
 'experience-and-interaction':         ('experience-and-interaction-event',        'Experience event',        'A business event that triggers the interaction or experience-delivery flow.',              'Caller.',         True,  'non-sensitive'),
 'search-and-discovery':               ('search-and-discovery-event',             'Search event',            'A business event that triggers the index-management or query-dispatch flow.',              'Caller.',         True,  'non-sensitive'),
 # P1 keys
 'identity-and-access-management':    ('identity-lifecycle-event',                'Identity lifecycle event','A business event that triggers an identity and access flow (e.g., new hire, role change, termination).', 'HR system (via ISC integration).', True, 'sensitive'),
 'data-management':                    ('data-lifecycle-event',                    'Data lifecycle event',    'A business event that triggers a data management flow (e.g., new record creation, schema change, retention trigger).', 'Source systems (via ISC integration).', True, 'sensitive'),
 'transaction-processing':             ('transaction-event',                       'Transaction event',       'A business event that triggers a transaction processing flow (e.g., order placed, payment captured, refund issued).', 'Caller.', True, 'sensitive'),
 'workflow-orchestration':             ('workflow-event',                          'Workflow event',          'A business event that triggers a workflow execution (e.g., a state-machine transition, a task routing decision).', 'Caller.', True, 'non-sensitive'),
 'integration-and-interoperability':   ('integration-event',                       'Integration event',       'A business event that triggers an integration flow (e.g., API request received, event published, schema validated).', 'Caller.', True, 'non-sensitive'),
}
F2_OUTPUT_TEXT = {
 'communication-and-collaboration':    ('collaboration-and-collaboration-state', 'Collaboration state',     'A collaboration state composed from the F4 children.',                                   'Coordination store, audit log.'),
 'content-and-knowledge-management':   ('content-lifecycle-state',                'Content state',           'A content lifecycle state composed from the F4 children.',                              'Content store, audit log.'),
 'analytics-and-decision-support':     ('analytical-output-state',                'Analytical state',         'An analytical output state composed from the F4 children.',                              'Insight store, audit log.'),
 'security-privacy-and-trust':         ('security-monitoring-state',              'Security state',           'A security state composed from the F4 children.',                                        'Security store, audit log.'),
 'monitoring-and-observability':       ('observability-state',                    'Observability state',      'An observability state composed from the F4 children.',                                   'Observability store, audit log.'),
 'configuration-and-administration':   ('configuration-state',                    'Configuration state',      'A configuration state composed from the F4 children.',                                   'Configuration store, audit log.'),
 'resource-and-capacity-management':   ('capacity-state',                         'Capacity state',          'A capacity state composed from the F4 children (plan, provisioned resource inventory).', 'Capacity store, audit log.'),
 'ai-and-intelligent-processing':      ('inference-state',                        'Inference state',         'An inference state composed from the F4 children (model version, prediction confidence).','Model store, audit log.'),
 'experience-and-interaction':         ('experience-state',                       'Experience state',        'An experience state composed from the F4 children (interaction record, experience signal).','Experience store, audit log.'),
 'search-and-discovery':               ('discovery-state',                        'Discovery state',         'A discovery state composed from the F4 children (index version, query result).',         'Search store, audit log.'),
 # P1 keys
 'identity-and-access-management':    ('identity-and-access-state',                'Identity and access state','The state of the identity record, the credentials, the active sessions, and the access policy decisions.', 'Identity store, audit log, downstream systems.'),
 'data-management':                    ('data-state',                              'Data state',              'The state of the data records (acquisition, transformation, retrieval lineage).', 'Data store, audit log.'),
 'transaction-processing':             ('transaction-state',                       'Transaction state',       'The state of the transactions (initiation, execution, reconciliation).', 'Transaction store, audit log.'),
 'workflow-orchestration':             ('workflow-state',                          'Workflow state',          'The state of the workflows (execution, task routing, completion).', 'Workflow store, audit log.'),
 'integration-and-interoperability':   ('integration-state',                       'Integration state',       'The state of the integration flows (request handling, event publication, interface validation).', 'Integration store, audit log.'),
}
F2_NON_FUNCTIONAL = {
 'availability': '99.95%',
 'performance_latency': 'p99 < 200ms (composed from F4 children)',
 'throughput': 'composed from F4 children',
 'scalability': 'horizontal',
 'resilience': 'active-active',
 'security': 'composed from F4 children',
 'privacy': 'composed from F4 children',
 'auditability': 'full',
 'recoverability': 'rto-15m-rpo-5m',
 'observability': 'prometheus-metrics',
 'compliance_constraints': [],
}


def _dedup(seq):
    seen = set(); out = []
    for x in seq:
        if x in seen: continue
        seen.add(x); out.append(x)
    return out


def build_f2_record(domain, f4_records, f2_slug=None):
    """Compose the canonical F2 record (P1 hand-edited shape parity) from the domain
    definition plus its F4 children. f2_slug defaults to the domain_id suffix
    but may be overridden for cases where the domain slug differs from the F2 record slug."""
    domain_id = domain['id']
    domain_slug = f2_slug if f2_slug else domain_id.split(':')[-1]
    f2_id = domain['f2']['id']
    f4_ids = [r['id'] for r in f4_records]
    realized = _dedup(sum([((r.get('business_alignment') or {}).get('realized_capabilities') or []) for r in f4_records], []))
    enabled  = _dedup(sum([((r.get('business_alignment') or {}).get('enabled_processes')  or []) for r in f4_records], []))
    executing = _dedup(sum([r.get('executing_components') or [] for r in f4_records], []))
    in_tid, in_name, in_defn, in_src, in_req, in_sens = F2_INPUT_TEXT[domain_slug]
    composite_input = {
        'input_id': in_tid, 'name': in_name, 'definition': in_defn,
        'data_or_event_reference': 'dea:event-' + domain_slug + '-invocation',
        'source': in_src, 'required': in_req,
        'validation_rules': [
            f'The {in_name.lower()} MUST be the single composite input that fires the F2; '
            'the F2 delegates per-F4 routing to the F4 children based on the event subtype.',
            'All F4 children MUST be registered and reachable.',
            'The audit log MUST be available.',
        ],
        'format_or_schema_reference': 'https://dea.example.org/schemas/' + domain_slug + '-invocation.v1.json',
        'sensitivity_classification': in_sens,
    }
    out_id, out_name, out_defn, out_dest = F2_OUTPUT_TEXT[domain_slug]
    composite_output = {
        'output_id': out_id, 'name': out_name, 'definition': out_defn,
        'data_or_event_reference': 'dea:data-entity-' + domain_slug + '-state',
        'destination': out_dest, 'output_conditions': 'Always produced (or an error response).',
        'quality_expectations': 'Consistent across the F4 children stores.',
    }
    return {
        'id': f2_id,
        'type': 'InformationSystemFunction',
        'name': domain['f2']['name'],
        'description': domain['f2']['description'],
        'version': '1.0.0',
        'lifecycle_status': 'planned',
        'functional_domain': domain_id,
        'category': domain_id,
        'decomposition_level': 'F2',
        'child_functions': f4_ids,
        'decomposition_rationale': (
            f'The F2 parent composes the named F4 children below. Each F4 captures an atomic responsibility; '
            f'the F2 composes them without orchestrating them. The composition follows the CR-IS-CAT-01B section 3.3 '
            f'distinction: the ISC orchestration pattern owns the inter-F4 ordering, retries, and compensation; '
            f'the F2 exposes the composite.'
        ),
        'responsibility_allocation': [
            {'child': f4_id, 'responsibility': f'Realize the {f4_id.split(":")[-1].replace("-", " ")} atomic responsibility.'}
            for f4_id in f4_ids
        ],
        'orchestration_responsibility': (
            'Not applicable to this function. The function composes child functions without orchestrating them; '
            'orchestration is at the ISC layer, per the composition-vs-orchestration distinction in CR-IS-CAT-01B section 3.3.'
        ),
        'inputs': [composite_input],
        'outputs': [composite_output],
        'execution_characteristics': {
            'execution_pattern': 'event-driven',
            'trigger_mechanism': 'event',
            'processing_mode': 'real-time',
            'synchronous_asynchronous': 'asynchronous',
            'idempotency': 'idempotent',
            'retry_recovery': 'Each child function is idempotent; the parent flow is retry-safe.',
            'error_handling': 'Each child function emits a structured error; the parent flow records the error and continues with the next step where possible.',
            'transactional': False,
            'concurrency': 'multi-threaded',
        },
        'business_alignment': {'realized_capabilities': realized, 'enabled_processes': enabled},
        'executing_components': executing,
        'non_functional_characteristics': F2_NON_FUNCTIONAL,
        'governance': {
            'functional_owner': domain['domain_name'] + ' team',
            'steward': 'Architecture team',
            'approval_status': 'proposed',
            'criticality': 'mission-critical',
            'review_date': '2027-10-19',
            'lifecycle_history': [],
            'source_and_evidence': (
                f'Source: ISF taxonomy CR-IS-CAT-01A section 5; P3 population per CR-IS-CAT-01C-P3 (2026-10-19). '
                f'The decomposition follows the F2 -> F4 pattern with explicit responsibility_allocation to the two atomic F4 children. '
                f'Composition-vs-orchestration distinction: CR-IS-CAT-01B section 3.3.'
            ),
            'change_history': [],
        },
        'references': [],
        'metadata': {
            'cr': 'CR-IS-CAT-01C-P3',
            'created_by': 'scripts/generate_p3_population.py',
            'created_date': '2026-10-19',
            'last_modified': '2026-10-19',
            'notes': 'Generator-emitted (P1 F2 record shape parity). Re-run is idempotent.',
        },
    }


def build_f2_readme(f2, domain_id, domain_name, domain_code):
    """Render the canonical 19-section README for an F2 record (P1 hand-edited parity)."""
    f4_ids = f2['child_functions']
    domain_slug = domain_id.split(':')[-1]
    title = f2['name']
    children_list = chr(10).join(f"- `{c}`" for c in f4_ids)
    components_list = chr(10).join(f"- `{c}`" for c in f2.get('executing_components', []))
    g = f2['governance']
    body = []
    body.append(f"# {title}")
    body.append("")
    body.append("## 1. Identity")
    body.append("")
    body.append(f"- Canonical ID: `{f2['id']}`")
    body.append("- Version: 1.0.0")
    body.append("- Lifecycle: planned")
    body.append(f"- Functional Domain: {domain_code} {domain_name} (`{domain_id}`)")
    body.append(f"- Category: {domain_code} {domain_name}")
    body.append("- Decomposition Level: F2 (parent function)")
    body.append(f"- Parent Function: None (F2 is the top of the {domain_slug} sub-tree)")
    body.append("")
    body.append("## 2. Definition")
    body.append("")
    body.append(f"The parent function that composes the {domain_slug} sub-tree. It exposes a composite view of the F4 children below.")
    body.append("")
    body.append("## 3. Purpose and Responsibility")
    body.append("")
    body.append(f"Responsibility: provide a coherent {domain_name.lower()} capability for the enterprise. The function composes the F4 children into a single responsibility that is exposed to upstream business processes.")
    body.append("")
    body.append("## 4. Functional Scope")
    body.append("")
    body.append("### In Scope")
    body.append(f"- Compose the {len(f4_ids)} F4 atomic functions under a single responsibility.")
    body.append("- Expose the composite to upstream business processes.")
    body.append("")
    body.append("### Out of Scope")
    body.append("- Orchestration of the F4 children (owned by the ISC orchestration pattern; per CR-IS-CAT-01B section 3.3).")
    body.append("")
    body.append("## 5. Behavioural Specification")
    body.append("")
    body.append("### Trigger")
    body.append(f"A business event that triggers the {domain_slug} flow.")
    body.append("")
    body.append("### Preconditions")
    body.append("- All F4 children are registered and reachable.")
    body.append("- The audit log is available.")
    body.append("")
    body.append("### Main Behaviour")
    body.append("The F2 function is a composition; it does not have its own main behaviour. The main behaviour is the composition of the child functions, orchestrated at the ISC layer.")
    body.append("")
    body.append("### Alternative Behaviour")
    body.append("Not applicable.")
    body.append("")
    body.append("### Exception Behaviour")
    body.append("The F2 function inherits the exception behaviour of the child functions. A child failure is recorded against the child.")
    body.append("")
    body.append("### Postconditions")
    body.append(f"- The {domain_slug} state is consistent.")
    body.append("- An audit event is recorded for every state change.")
    body.append("")
    body.append("## 6. Inputs")
    body.append("")
    body.append("The F2 parent composes inputs from its F4 children. Per-domain input specifications are in the F4 records.")
    body.append("")
    body.append("## 7. Outputs")
    body.append("")
    body.append("The F2 parent composes outputs from its F4 children.")
    body.append("")
    body.append("## 8. Data and Event Interaction")
    body.append("")
    body.append("- Consumed Data: composed from F4 children.")
    body.append("- Produced Data: composed from F4 children.")
    body.append("- Consumed Events: composed from F4 children.")
    body.append("- Produced Events: composed from F4 children.")
    body.append("")
    body.append("## 9. Composition and Dependencies")
    body.append("")
    body.append("### Parent")
    body.append(f"None (F2 is the parent of the {domain_slug} sub-tree).")
    body.append("")
    body.append("### Child Functions")
    body.append("")
    body.append(children_list)
    body.append("")
    body.append("## 10. Execution Characteristics")
    body.append("")
    body.append("- Execution Pattern: event-driven")
    body.append("- Trigger Mechanism: event")
    body.append("- Processing Mode: real-time")
    body.append("- Synchronous/Asynchronous: asynchronous")
    body.append("- Idempotency: idempotent (each child function is idempotent)")
    body.append("- Retry/Recovery: Each child function is idempotent; the parent flow is retry-safe.")
    body.append("- Error Handling: Each child function emits a structured error; the parent flow records the error.")
    body.append("- Transactional: false")
    body.append("- Concurrency: multi-threaded")
    body.append("")
    body.append("## 11. Business Alignment")
    body.append("")
    body.append("The realised capabilities and enabled processes of the F2 are the union of the children's. See the F4 records for the per-capability and per-process references.")
    body.append("")
    body.append("## 12. Executing Components")
    body.append("")
    body.append(components_list)
    body.append("")
    body.append("## 13. Non-Functional Characteristics")
    body.append("")
    body.append("- Availability: 99.95%")
    body.append("- Performance Latency: p99 < 200ms (composed from F4 children)")
    body.append("- Throughput: composed from F4 children")
    body.append("- Scalability: horizontal")
    body.append("- Resilience: active-active")
    body.append("- Security: composed from F4 children")
    body.append("- Privacy: composed from F4 children")
    body.append("- Auditability: full")
    body.append("- Recoverability: RTO 15m, RPO 5m")
    body.append("- Observability: prometheus-metrics")
    body.append("- Compliance Constraints: per F4 child")
    body.append("")
    body.append("## 14. Security and Governance")
    body.append("")
    body.append(f"- Functional owner: {g['functional_owner']}")
    body.append(f"- Steward: {g['steward']}")
    body.append(f"- Approval status: {g['approval_status']}")
    body.append(f"- Criticality: {g['criticality']}")
    body.append(f"- Review date: {g['review_date']}")
    body.append("- Change history: see CHANGELOG.md")
    body.append("")
    body.append("## 15. Measurement and Observability")
    body.append("")
    body.append("Composed from F4 children.")
    body.append("")
    body.append("## 16. Examples and Use Cases")
    body.append("")
    body.append("See the F4 records for atomic use cases.")
    body.append("")
    body.append("## 17. Limitations and Assumptions")
    body.append("")
    body.append("The F2 function does not orchestrate the F4 children. The composition is exposed to the ISC layer.")
    body.append("")
    body.append("## 18. References")
    body.append("")
    body.append("- CR-IS-CAT-01A section 5 (taxonomy classification).")
    body.append("- CR-IS-CAT-01B section 3 (composition vs orchestration).")
    body.append("- CR-IS-CAT-01C-P3 P3 population brief.")
    body.append("")
    body.append("## 19. Change History")
    body.append("")
    body.append("- 2026-10-19: CR-IS-CAT-01C-P3 initial P3 population.")
    body.append("- 2026-10-19: CR-IS-CAT-01C-P2H F2 record shape parity (canonical P1 F2 shape).")
    return chr(10).join(body) + chr(10)
