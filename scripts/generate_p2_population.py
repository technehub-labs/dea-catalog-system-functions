#!/usr/bin/env python3
"""CR-IS-CAT-01C-P2: ISF P2 population generator. Produces 6 F2 + 12 F4 = 18 records
across ISF-06..11 (Communication and Collaboration, Content and Knowledge Management,
Analytics and Decision Support, Security Privacy and Trust, Monitoring and Observability,
Configuration and Administration). Imports helper renderers from generate_p1_population
to keep a single source of truth for the YAML / README shape.

Authored with canonical BC/BP/ISC ids from the start (per CR-IS-CAT-01R rebasing).
"""

import importlib.util, os, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("generate_p1_population", BASE / "generate_p1_population.py")
p1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p1)

P2_DOMAINS = [
    {
        'id': 'isf:domain:communication-and-collaboration',
        'domain_name': 'Communication and Collaboration',
        'domain_code': 'ISF-06',
        'f2': {
            'id': 'dea:information-system-function-communication-and-collaboration',
            'name': 'Communication and Collaboration',
            'description': 'The parent function that composes the communication-and-collaboration sub-tree. It coordinates messaging, presence, and shared workspace access across human and AI agents.',
        },
        'f4': [
            ('dea:information-system-function-collaboration-coordination', 'Collaboration Coordination',
             'The atomic function that routes work, messages, and presence between collaborating agents and humans. It applies routing rules and produces a coordination record.',
             ['dea:process-coordinate-collaboration'],
             ['capabilities:capability-workforce-management-9e8d8s'],
             ['dea:information-system-component-employee-portal-platform', 'dea:information-system-component-api-gateway']),
            ('dea:information-system-function-notification-dispatch', 'Notification Dispatch',
             'The atomic function that delivers a notification (transactional, scheduled, or event-driven) to a recipient across the appropriate channel.',
             ['dea:process-coordinate-collaboration'],
             ['capabilities:capability-workforce-management-9e8d8s'],
             ['dea:information-system-component-employee-portal-platform', 'dea:information-system-component-api-gateway']),
        ],
    },
    {
        'id': 'isf:domain:content-and-knowledge-management',
        'domain_name': 'Content and Knowledge Management',
        'domain_code': 'ISF-07',
        'f2': {
            'id': 'dea:information-system-function-content-and-knowledge-management',
            'name': 'Content and Knowledge Management',
            'description': 'The parent function that composes the content-and-knowledge-management sub-tree. It governs the storage, retrieval, and lifecycle of unstructured content and knowledge artefacts.',
        },
        'f4': [
            ('dea:information-system-function-content-management', 'Content Management',
             'The atomic function that stores, versions, and indexes unstructured content (documents, images, knowledge articles) and emits the content-stored event.',
             ['dea:process-operate-service-delivery'],
             ['capabilities:capability-information-management-6vjgdh'],
             ['dea:information-system-component-data-warehouse-platform', 'dea:information-system-component-customer-facing-web-application-platform']),
            ('dea:information-system-function-knowledge-retrieval', 'Knowledge Retrieval',
             'The atomic function that resolves a knowledge query against the indexed corpus and returns ranked results with provenance.',
             ['dea:process-operate-service-delivery'],
             ['capabilities:capability-information-management-6vjgdh'],
             ['dea:information-system-component-data-warehouse-platform', 'dea:information-system-component-data-warehouse-catalog']),
        ],
    },
    {
        'id': 'isf:domain:analytics-and-decision-support',
        'domain_name': 'Analytics and Decision Support',
        'domain_code': 'ISF-08',
        'f2': {
            'id': 'dea:information-system-function-analytics-and-decision-support',
            'name': 'Analytics and Decision Support',
            'description': 'The parent function that composes the analytics-and-decision-support sub-tree. It transforms operational data into analytical outputs and decision signals.',
        },
        'f4': [
            ('dea:information-system-function-data-analysis', 'Data Analysis',
             'The atomic function that applies analytical transformations (aggregations, comparisons, slices) over a curated dataset and produces analytical outputs.',
             ['dea:process-operate-financial-reporting-and-disclosure'],
             ['capabilities:capability-insight-management-ms4n9d'],
             ['dea:information-system-component-data-warehouse-platform', 'dea:information-system-component-data-warehouse-query']),
            ('dea:information-system-function-insight-generation', 'Insight Generation',
             'The atomic function that produces an insight (forecast, anomaly, recommendation) from analytical outputs and emits the insight-ready event.',
             ['dea:process-customer-insight-and-retention'],
             ['capabilities:capability-insight-management-ms4n9d'],
             ['dea:information-system-component-data-warehouse-platform', 'dea:information-system-component-ai-inference-platform']),
        ],
    },
    {
        'id': 'isf:domain:security-privacy-and-trust',
        'domain_name': 'Security, Privacy and Trust',
        'domain_code': 'ISF-09',
        'f2': {
            'id': 'dea:information-system-function-security-privacy-and-trust',
            'name': 'Security, Privacy and Trust',
            'description': 'The parent function that composes the security-privacy-and-trust sub-tree. It protects the enterprise assets, data, and operations against threats and policy violations.',
        },
        'f4': [
            ('dea:information-system-function-security-monitoring', 'Security Monitoring',
             'The atomic function that collects security telemetry from the runtime, evaluates detection rules, and produces a security-monitoring result.',
             ['dea:process-audit-policy-compliance'],
             ['capabilities:capability-security-management-wmzc7c'],
             ['dea:information-system-component-observability-platform', 'dea:information-system-component-distributed-tracer']),
            ('dea:information-system-function-threat-detection', 'Threat Detection',
             'The atomic function that applies detection logic to identify a threat (pattern, anomaly, signature) and emits the threat-detected event.',
             ['dea:process-improve-policy-and-control-framework'],
             ['capabilities:capability-security-management-wmzc7c'],
             ['dea:information-system-component-observability-platform', 'dea:information-system-component-identity-broker']),
        ],
    },
    {
        'id': 'isf:domain:monitoring-and-observability',
        'domain_name': 'Monitoring and Observability',
        'domain_code': 'ISF-10',
        'f2': {
            'id': 'dea:information-system-function-monitoring-and-observability',
            'name': 'Monitoring and Observability',
            'description': 'The parent function that composes the monitoring-and-observability sub-tree. It collects signals from the runtime and makes them queryable, alertable, and inspectable.',
        },
        'f4': [
            ('dea:information-system-function-metric-collection', 'Metric Collection',
             'The atomic function that samples a runtime metric (counter, gauge, histogram) at the configured cadence and produces a metric data-point.',
             ['dea:process-operate-technology-platforms'],
             ['capabilities:capability-continuity-management-v3rn6u'],
             ['dea:information-system-component-observability-platform', 'dea:information-system-component-metrics-collector']),
            ('dea:information-system-function-log-aggregation', 'Log Aggregation',
             'The atomic function that ingests a log record, indexes it for retrieval, and emits the log-indexed event.',
             ['dea:process-operate-technology-platforms'],
             ['capabilities:capability-continuity-management-v3rn6u'],
             ['dea:information-system-component-observability-platform', 'dea:information-system-component-log-aggregator']),
        ],
    },
    {
        'id': 'isf:domain:configuration-and-administration',
        'domain_name': 'Configuration and Administration',
        'domain_code': 'ISF-11',
        'f2': {
            'id': 'dea:information-system-function-configuration-and-administration',
            'name': 'Configuration and Administration',
            'description': 'The parent function that composes the configuration-and-administration sub-tree. It manages the configuration, change, and lifecycle of the technology estate.',
        },
        'f4': [
            ('dea:information-system-function-configuration-deployment', 'Configuration Deployment',
             'The atomic function that applies a configuration change to a target (system, service, environment) under a verified approval and emits the configuration-applied event.',
             ['dea:process-improve-technology-platforms'],
             ['capabilities:capability-change-management-hukdeq'],
             ['dea:information-system-component-development-platform', 'dea:information-system-component-ci-cd-pipeline']),
            ('dea:information-system-function-configuration-validation', 'Configuration Validation',
             'The atomic function that validates a configuration change against the policy and invariant rules before deployment and produces a validation result.',
             ['dea:process-improve-technology-platforms'],
             ['capabilities:capability-change-management-hukdeq'],
             ['dea:information-system-component-development-platform', 'dea:information-system-component-build-service']),
        ],
    },
]

EXEC_CHAR = {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': True, 'concurrency': 'multi-threaded'}
F4_INPUT_TEMPLATES = {
    'collaboration-coordination': [('coordination-request', 'Coordination request', 'A coordination request: target agent or work item and the coordination action (route, ping, hand-off).', 'Caller.', True, 'non-sensitive'),
                                     ('routing-rule', 'Routing rule', 'The rule that determines the recipient channel and policy for this coordination action.', 'Policy store.', True, 'non-sensitive')],
    'notification-dispatch':      [('notification-payload', 'Notification payload', 'The notification payload (subject, body, recipient, channel).', 'Caller.', True, 'sensitive'),
                                     ('recipient-policy', 'Recipient policy', 'The recipient routing and preference policy.', 'Policy store.', True, 'non-sensitive')],
    'content-management':         [('content-body', 'Content body', 'The content body (text, image, structured document) with metadata.', 'Caller or upload service.', True, 'sensitive'),
                                     ('storage-policy', 'Storage policy', 'The retention, encryption, and access policy for the content.', 'Policy store.', True, 'non-sensitive')],
    'knowledge-retrieval':        [('query', 'Query', 'The knowledge query (free text or structured expression).', 'Caller.', True, 'non-sensitive'),
                                     ('corpus-scope', 'Corpus scope', 'The corpus scope (which corpora, which tenants, which roles).', 'Policy store.', True, 'non-sensitive')],
    'data-analysis':              [('analytical-subject', 'Analytical subject', 'The analytical subject: a curated dataset, table, or model reference.', 'Curated data lake.', True, 'sensitive'),
                                     ('analysis-specification', 'Analysis specification', 'The specification of transformations and aggregations to apply.', 'Caller.', True, 'non-sensitive')],
    'insight-generation':         [('analytical-output', 'Analytical output', 'An analytical output produced by the data-analysis function.', 'Data analysis store.', True, 'sensitive'),
                                     ('insight-model', 'Insight model', 'The model or rule that produces an insight from the analytical output.', 'Model store.', True, 'non-sensitive')],
    'security-monitoring':        [('security-telemetry', 'Security telemetry', 'A security telemetry record (audit event, alert, network signal).', 'Runtime instrumentation.', True, 'sensitive'),
                                     ('detection-rule', 'Detection rule', 'The detection rule set (signatures, patterns, thresholds).', 'Threat store.', True, 'non-sensitive')],
    'threat-detection':           [('candidate-signal', 'Candidate signal', 'A candidate security signal under evaluation.', 'Security-monitoring stream.', True, 'sensitive'),
                                     ('threat-model', 'Threat model', 'The threat model that classifies a candidate signal.', 'Threat intelligence store.', True, 'non-sensitive')],
    'metric-collection':          [('metric-source', 'Metric source', 'A runtime source for a metric (counter, gauge, histogram).', 'Runtime instrumentation.', True, 'non-sensitive'),
                                     ('sampling-policy', 'Sampling policy', 'The sampling cadence and aggregation rule.', 'Policy store.', True, 'non-sensitive')],
    'log-aggregation':            [('log-record', 'Log record', 'A log record ingested from a runtime source.', 'Runtime instrumentation.', True, 'sensitive'),
                                     ('index-rule', 'Index rule', 'The retention, indexing, and redaction rule.', 'Policy store.', True, 'non-sensitive')],
    'configuration-deployment':   [('configuration-change', 'Configuration change', 'A configuration change record (diff, target, approval).', 'Change management.', True, 'non-sensitive'),
                                     ('approval-evidence', 'Approval evidence', 'The approval evidence (approver, timestamp, evidence link).', 'Approval store.', True, 'non-sensitive')],
    'configuration-validation':   [('configuration-candidate', 'Configuration candidate', 'A candidate configuration under validation.', 'Configuration store.', True, 'non-sensitive'),
                                     ('validation-rules', 'Validation rules', 'The validation rules (policy, invariants, schemas).', 'Policy store.', True, 'non-sensitive')],
}
F4_OUTPUT_TEMPLATES = {
    'collaboration-coordination': ('coordination-record', 'Coordination record', 'A coordination record (recipient, action, status, evidence).', 'Coordination store, audit log.'),
    'notification-dispatch':      ('delivered-notification', 'Delivered notification', 'A delivered-notification record with the channel, timestamp, and delivery evidence.', 'Notification store, audit log.'),
    'content-management':         ('stored-content', 'Stored content', 'A stored-content record with the content id, version, location, and storage-policy reference.', 'Content store, audit log.'),
    'knowledge-retrieval':        ('query-result', 'Query result', 'A ranked query result list with provenance for each entry.', 'Caller, audit log.'),
    'data-analysis':              ('analytical-output', 'Analytical output', 'An analytical output (aggregation, slice, comparison).', 'Analytical store.'),
    'insight-generation':         ('insight-record', 'Insight record', 'An insight record (insight type, value, confidence, provenance).', 'Insight store.'),
    'security-monitoring':        ('monitoring-result', 'Monitoring result', 'A security-monitoring result (rules fired, evidence, severity).', 'Monitoring store, audit log.'),
    'threat-detection':           ('threat-decision', 'Threat decision', 'A threat decision (threat, severity, response recommendation).', 'Threat response store, audit log.'),
    'metric-collection':          ('metric-data-point', 'Metric data point', 'A metric data-point with timestamp, labels, and value.', 'Metric store.'),
    'log-aggregation':            ('indexed-log', 'Indexed log', 'An indexed-log record ready for retrieval.', 'Log store, audit log.'),
    'configuration-deployment':   ('deployment-record', 'Deployment record', 'A deployment record (target, version, evidence).', 'Deployment store, audit log.'),
    'configuration-validation':   ('validation-decision', 'Validation decision', 'A validation decision (pass, fail, with reasons).', 'Validation store.'),
}



# Per-domain composite input/output text (used to form the F2 composite input/output record).
F2_INPUT_TEXT = {
 'communication-and-collaboration':    ('collaboration-and-collaboration-event', 'Collaboration event',     'A business event that triggers the collaboration and notification flow.',                  'Caller.',         True,  'non-sensitive'),
 'content-and-knowledge-management':   ('content-lifecycle-event',                'Content lifecycle event', 'A business event that triggers the content storage and retrieval flow.',               'Caller.',         True,  'non-sensitive'),
 'analytics-and-decision-support':     ('analytical-subject-area-event',          'Analytical event',        'A business event that triggers the analytics transformation and insight generation flow.', 'Caller.',        True,  'non-sensitive'),
 'security-privacy-and-trust':         ('security-and-trust-event',               'Security event',          'A business event that triggers the security-monitoring or threat-detection flow.',     'Caller.',         True,  'sensitive'),
 'monitoring-and-observability':       ('runtime-instrumentation-event',          'Runtime event',           'A business event that triggers the metric and log instrumentation flow.',                'Caller.',         True,  'non-sensitive'),
 'configuration-and-administration':   ('configuration-change-event',             'Configuration event',     'A business event that triggers the configuration deployment and validation flow.',       'Caller.',         True,  'non-sensitive'),
}
F2_OUTPUT_TEXT = {
 'communication-and-collaboration':    ('collaboration-and-collaboration-state', 'Collaboration state',     'A collaboration state composed from the F4 children.',                                   'Coordination store, audit log.'),
 'content-and-knowledge-management':   ('content-lifecycle-state',                'Content state',           'A content lifecycle state composed from the F4 children.',                              'Content store, audit log.'),
 'analytics-and-decision-support':     ('analytical-output-state',                'Analytical state',         'An analytical output state composed from the F4 children.',                              'Insight store, audit log.'),
 'security-privacy-and-trust':         ('security-monitoring-state',              'Security state',           'A security state composed from the F4 children.',                                        'Security store, audit log.'),
 'monitoring-and-observability':       ('observability-state',                    'Observability state',      'An observability state composed from the F4 children.',                                   'Observability store, audit log.'),
 'configuration-and-administration':   ('configuration-state',                    'Configuration state',      'A configuration state composed from the F4 children.',                                   'Configuration store, audit log.'),
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


def build_f2_record(domain, f4_records):
    """Compose the F2 record from the domain definition + its F4 children.

    The F2 record shape is identical to the P1 hand-edited F2
    `dea:information-system-function-identity-and-access-management` record, so P1 and
    P2 F2 records are interchangeable for tooling (generator-emitted, no post-hoc
    hand-patches).
    """
    domain_id  = domain['id']
    domain_slug = domain_id.split(':')[-1]
    f2_id      = domain['f2']['id']
    f4_ids     = [r['id'] for r in f4_records]
    # Compose from children: realized_capabilities / enabled_processes / executing_components
    realized = _dedup(sum([((r.get('business_alignment') or {}).get('realized_capabilities') or []) for r in f4_records], []))
    enabled  = _dedup(sum([((r.get('business_alignment') or {}).get('enabled_processes')  or []) for r in f4_records], []))
    executing = _dedup(sum([(r.get('executing_components') or []) for r in f4_records], []))
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
                f'Source: ISF taxonomy CR-IS-CAT-01A section 5; P2 population per CR-IS-CAT-01C-P2 (2026-10-19). '
                f'The decomposition follows the F2 -> F4 pattern with explicit responsibility_allocation to the two atomic F4 children. '
                f'Composition-vs-orchestration distinction: CR-IS-CAT-01B section 3.3.'
            ),
            'change_history': [],
        },
        'references': [],
        'metadata': {
            'cr': 'CR-IS-CAT-01C-P2',
            'created_by': 'scripts/generate_p2_population.py',
            'created_date': '2026-10-19',
            'last_modified': '2026-10-19',
            'notes': 'Generator-emitted (P1 F2 record shape parity). Re-run is idempotent.',
        },
    }



def main():
    import yaml as _yaml
    WS2 = Path("entities/v1-alpha/domains")  # base for F2 compose-from-F4 reads
    total_files = 0
    for domain in P2_DOMAINS:
        domain_id = domain['id']
        domain_name = domain['domain_name']
        domain_code = domain['domain_code']
        domain_slug = domain_id.split(':')[-1]
        domain_dir = f'entities/v1-alpha/domains/{domain_slug}'
        os.makedirs(domain_dir, exist_ok=True)

        # Build F4 entries
        f4_entries = []
        # The F4 stub used by p1's index.yaml renderer needs (id, level, name, description, parent, children, inputs, outputs, exec, components, capabilities, processes, criticality)
        for (f4_id, f4_name, f4_desc, processes, capabilities, components) in domain['f4']:
            slug = f4_id.split(':')[-1].replace('information-system-function-', '')
            # Render inputs/outputs/children -- build a dict compatible with the p1 render
            inputs_list = []
            for tid, name, defn, src, required, sensitivity in F4_INPUT_TEMPLATES[slug]:
                inputs_list.append({'id': tid, 'name': name, 'definition': defn, 'source': src, 'required': required, 'sensitivity': sensitivity})
            otid, oname, odefn, odest = F4_OUTPUT_TEMPLATES[slug]
            outputs_list = [{'id': otid, 'name': oname, 'definition': odefn, 'destination': odest, 'conditions': 'Always produced (or an error response).'}]
            f4_entries.append({
                'id': f4_id, 'level': 'F4', 'name': f4_name,
                'description': f4_desc, 'parent': domain['f2']['id'], 'children': [],
                'inputs': inputs_list, 'outputs': outputs_list, 'exec': EXEC_CHAR,
                'components': components, 'capabilities': capabilities, 'processes': processes,
                'criticality': 'mission-critical',
            })

        # Write F4 function.yaml + README
        for f in f4_entries:
            func_slug = f['id'].split(':')[-1].replace('information-system-function-', '')
            func_dir = f'{domain_dir}/functions/dea-isf-{func_slug}'
            os.makedirs(func_dir, exist_ok=True)
            with open(f'{func_dir}/function.yaml', 'w') as fp:
                fp.write(p1.generate_function_yaml(f, domain_id, domain_name))
            with open(f'{func_dir}/README.md', 'w') as fp:
                fp.write(p1.generate_readme(f, domain_id, domain_name, domain_code))
            total_files += 2

        # Build per-domain index.yaml with F2 + F4 entries
        # Reuse p1's main() pattern but emit only this domain
        functions_index = []
        for f in f4_entries:
            functions_index.append({'id': f['id'], 'decomposition_level': 'F4', 'lifecycle_status': 'planned', 'parent': f['parent'], 'children': []})
        functions_index.insert(0, {'id': domain['f2']['id'], 'decomposition_level': 'F2', 'lifecycle_status': 'planned', 'parent': None, 'children': [f['id'] for f in f4_entries]})

        # Hand-write the F2 stub record (p1's index emit only writes a stub; we write a full F2 record here)
        f2_id = domain['f2']['id']
        f2_funcs = [f['id'] for f in f4_entries]
        f2_dir = f'{domain_dir}/functions/dea-isf-{f2_id.split(":")[-1].replace("information-system-function-","")}'
        os.makedirs(f2_dir, exist_ok=True)
        # Build F2 record by compositing from F4 children (canonical P1 F2 record shape parity).
        # First emit F4 records to disk, then load them back so the F2 composition reads from the
        # canonical F4 source (G-10: single source of truth).
        f4_records_for_compose = []
        for fid in f2_funcs:
            f4_slug = fid.split(':')[-1].replace('information-system-function-', '')
            f4_path = WS2 / domain_slug / 'functions' / ('dea-isf-' + f4_slug) / 'function.yaml'
            f4_records_for_compose.append(_yaml.safe_load(open(f4_path)))
        f2_record = build_f2_record(domain, f4_records_for_compose)
        with open(f'{f2_dir}/function.yaml', 'w') as fp:
            from yaml import safe_dump
            fp.write(safe_dump(f2_record, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200))
        # README for F2
        with open(f'{f2_dir}/README.md', 'w') as fp:
            fp.write(build_f2_readme(f2_record, domain_id, domain_name, domain_code))

        # Per-domain index
        idx = {
            'domain': domain_id, 'code': domain_code, 'cr': 'CR-IS-CAT-01C-P2', 'version': '1.0',
            'functions': functions_index, 'change_history': [
                {'version': '1.0', 'date': '2026-10-19', 'cr': 'CR-IS-CAT-01C-P2', 'note': f'P2 population. {len(functions_index)} functions in {domain_name} domain.'},
            ],
        }
        with open(f'{domain_dir}/index.yaml', 'w') as fp:
            from yaml import safe_dump
            fp.write(safe_dump(idx, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200))
        total_files += 2

    print(f'Generated {total_files} P2 files (yaml + md + 2 per domain).')


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
    body.append("- CR-IS-CAT-01C-P2 P2 population brief.")
    body.append("")
    body.append("## 19. Change History")
    body.append("")
    body.append("- 2026-10-19: CR-IS-CAT-01C-P2 initial P2 population.")
    body.append("- 2026-10-19: CR-IS-CAT-01C-P2H F2 record shape parity (canonical P1 F2 shape).")
    return chr(10).join(body) + chr(10)


if __name__ == '__main__':
    main()
