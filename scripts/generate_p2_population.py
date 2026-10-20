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


def main():
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

        from pathlib import Path
        # Hand-write the F2 stub record (p1's index emit only writes a stub; we write a full F2 record here)
        f2_id = domain['f2']['id']
        f2_funcs = [f['id'] for f in f4_entries]
        f2_dir = f'{domain_dir}/functions/dea-isf-{f2_id.split(":")[-1].replace("information-system-function-","")}'
        os.makedirs(f2_dir, exist_ok=True)
        # Compose the F2 record. We mirror the hand-edited identity-and-access structure (canonical refs + version).
        # Use the first F4 entry's processes/capabilities/components as a representative flavor for the F2 realized/enabled/executing.
        # But more correctly: the F2 has child_functions, not full business_alignment. Keep minimal.
        f2_record = {
            'id': f2_id,
            'type': 'InformationSystemFunction',
            'name': domain['f2']['name'],
            'description': domain['f2']['description'],
            'version': '1.0.0',
            'lifecycle_status': 'planned',
            'functional_domain': domain_id,
            'category': domain_id,
            'decomposition_level': 'F2',
            'child_functions': f2_funcs,
            'decomposition_rationale': (
                'The F2 parent composes the named F4 children below. Each F4 captures an atomic responsibility; the F2 composes them without orchestrating them.'
            ),
            'responsibility_allocation': 'Atomic responsibilities live in the F4 records; the F2 composes them.',
            'orchestration_responsibility': 'Not applicable to this function. The function composes child functions without orchestrating them; orchestration is at the ISC layer.',
            'inputs': [],
            'outputs': [],
            'execution_characteristics': EXEC_CHAR,
            'business_alignment': {'realized_capabilities': [], 'enabled_processes': []},
            'executing_components': [],
            'non_functional_characteristics': {},
            'governance': {'functional_owner': f'{domain_name} team', 'steward': 'Architecture team', 'approval_status': 'proposed', 'criticality': 'mission-critical', 'lifecycle_history': [], 'source_and_evidence': f'Source: ISF taxonomy CR-IS-CAT-01A section 5; P2 population per CR-IS-CAT-01C-P2.'},
            'references': [],
            'metadata': {},
        }
        # Set F2 domain code in metadata
        f2_record['metadata'] = {'domain_code': domain_code, 'p2_population_cr': 'CR-IS-CAT-01C-P2'}
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
    f4_ids = f2['child_functions']
    children_section = '\n'.join(f'- `{f}`' for f in f4_ids)
    return (
        f'# {f2["name"]}\n\n'
        f'**Domain**: {domain_name} ({domain_code})\n'
        f'**ID**: `{f2["id"]}`\n'
        f'**Level**: F2 (parent)\n'
        f'**Status**: planned\n\n'
        f'## Description\n\n{f2["description"]}\n\n'
        f'## Child Functions\n\n{children_section}\n\n'
        f'## Decomposition Rationale\n\nThe F2 parent composes the named F4 children below. Each F4 captures an atomic responsibility; the F2 composes them without orchestrating them.\n\n'
        f'## Orchestration Responsibility\n\nNot applicable to this function. The function composes child functions without orchestrating them; orchestration is at the ISC layer.\n\n'
        f'## Governance\n\n- Functional owner: {f2["governance"]["functional_owner"]}\n'
        f'- Steward: {f2["governance"]["steward"]}\n'
        f'- Approval status: {f2["governance"]["approval_status"]}\n\n'
        f'## Change History\n\n- 2026-10-19: CR-IS-CAT-01C-P2 initial P2 population.\n'
    )


if __name__ == '__main__':
    main()
