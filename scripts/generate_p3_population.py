#!/usr/bin/env python3
"""CR-IS-CAT-01C-P3: ISF P3 population generator.

Adds the 4 remaining functional domains (ISF-12..15):
- ISF-12 Resource and Capacity Management
- ISF-13 AI and Intelligent Processing
- ISF-14 Experience and Interaction  (also resolves the last forward ref
  `customer-experience-management` in the ISC relationship registry)
- ISF-15 Search and Discovery

4 domains x (1 F2 + 2 F4) = 12 records.

Authored with canonical BC/BP/ISC ids from the start (per CR-IS-CAT-01R). F2
records use the canonical shape via the shared `_f2_record_helper` helper (P1
hand-edited F2 parity, per CR-IS-CAT-01C-P2H).
"""

import importlib.util, os, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
helper = importlib.import_module('_f2_record_helper')
build_f2_record = helper.build_f2_record
build_f2_readme = helper.build_f2_readme

spec = importlib.util.spec_from_file_location("generate_p1_population", BASE / "generate_p1_population.py")
p1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p1)


P3_DOMAINS = [
    {
        'id': 'isf:domain:resource-and-capacity-management',
        'domain_name': 'Resource and Capacity Management',
        'domain_code': 'ISF-12',
        'f2': {
            'id': 'dea:information-system-function-resource-and-capacity-management',
            'name': 'Resource and Capacity Management',
            'description': 'The parent function that composes the resource-and-capacity-management sub-tree. It plans capacity and provisions compute, storage, and integration resources to match workload demand.',
        },
        'f4': [
            ('dea:information-system-function-capacity-planning', 'Capacity Planning',
             'The atomic function that consumes historical and forecast demand signals and produces a capacity plan (compute, storage, integration) over a planning horizon.',
             ['dea:process-improve-technology-platforms'],
             ['capabilities:capability-technology-management-maus5n'],
             ['dea:information-system-component-observability-platform','dea:information-system-component-development-platform']),
            ('dea:information-system-function-resource-provisioning', 'Resource Provisioning',
             'The atomic function that allocates and provisions a resource (compute, storage, integration slot) per the capacity plan and emits the resource-provisioned event.',
             ['dea:process-operate-technology-platforms'],
             ['capabilities:capability-technology-enablement-y6nkws'],
             ['dea:information-system-component-development-platform','dea:information-system-component-ci-cd-pipeline']),
        ],
    },
    {
        'id': 'isf:domain:ai-and-intelligent-processing',
        'domain_name': 'AI and Intelligent Processing',
        'domain_code': 'ISF-13',
        'f2': {
            'id': 'dea:information-system-function-ai-and-intelligent-processing',
            'name': 'AI and Intelligent Processing',
            'description': 'The parent function that composes the ai-and-intelligent-processing sub-tree. It manages model lifecycles and executes inferences for predictions and decisions.',
        },
        'f4': [
            ('dea:information-system-function-model-management', 'Model Management',
             'The atomic function that registers, versions, evaluates, and retires machine-learning models, and emits the model-state-changed event.',
             ['dea:process-improve-technology-platforms'],
             ['capabilities:capability-insight-management-ms4n9d'],
             ['dea:information-system-component-ai-inference-platform','dea:information-system-component-model-registry']),
            ('dea:information-system-function-inference-execution', 'Inference Execution',
             'The atomic function that evaluates a model against input features and produces a prediction or a decision with confidence.',
             ['dea:process-customer-insight-and-retention'],
             ['capabilities:capability-insight-management-ms4n9d'],
             ['dea:information-system-component-ai-inference-platform','dea:information-system-component-model-serving-runtime']),
        ],
    },
    {
        'id': 'isf:domain:experience-and-interaction',
        'domain_name': 'Experience and Interaction',
        'domain_code': 'ISF-14',
        'f2': {
            'id': 'dea:information-system-function-experience-and-interaction',
            'name': 'Experience and Interaction',
            'description': 'The parent function that composes the experience-and-interaction sub-tree. It captures interactions across channels and produces a coherent experience signal for downstream personalization and consistency. Note: this F2 is also the resolution of the ISC-side forward ref `dea:information-system-function-customer-experience-management` declared in CR-IS-CAT-02E; the canonical ISF id is `experience-and-interaction`.',
        },
        'f4': [
            ('dea:information-system-function-interaction-management', 'Interaction Management',
             'The atomic function that records a single interaction (page view, click, conversation turn) and emits the interaction-recorded event.',
             ['dea:process-customer-insight-and-retention'],
             ['capabilities:capability-customer-management-f3n8wb'],
             ['dea:information-system-component-customer-facing-web-application-platform','dea:information-system-component-api-gateway']),
            ('dea:information-system-function-experience-delivery', 'Experience Delivery',
             'The atomic function that resolves the experience signal for the current session and renders the experience (channel, content, copy) consistently across surfaces.',
             ['dea:process-customer-insight-and-retention'],
             ['capabilities:capability-customer-management-f3n8wb'],
             ['dea:information-system-component-customer-facing-web-application-platform','dea:information-system-component-employee-portal-platform']),
        ],
    },
    {
        'id': 'isf:domain:search-and-discovery',
        'domain_name': 'Search and Discovery',
        'domain_code': 'ISF-15',
        'f2': {
            'id': 'dea:information-system-function-search-and-discovery',
            'name': 'Search and Discovery',
            'description': 'The parent function that composes the search-and-discovery sub-tree. It indexes content and dispatches queries against the indexed corpus, returning ranked results with provenance.',
        },
        'f4': [
            ('dea:information-system-function-index-management', 'Index Management',
             'The atomic function that builds and refreshes an index over a content corpus and emits the index-rebuilt event.',
             ['dea:process-operate-service-delivery'],
             ['capabilities:capability-information-management-6vjgdh'],
             ['dea:information-system-component-data-warehouse-platform','dea:information-system-component-data-warehouse-catalog']),
            ('dea:information-system-function-query-dispatch', 'Query Dispatch',
             'The atomic function that resolves a query against an index and returns ranked results with provenance.',
             ['dea:process-customer-insight-and-retention'],
             ['capabilities:capability-insight-management-ms4n9d'],
             ['dea:information-system-component-data-warehouse-platform','dea:information-system-component-data-warehouse-query']),
        ],
    },
]


EXEC_CHAR = {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': True, 'concurrency': 'multi-threaded'}

F4_INPUT_TEMPLATES = {
    'capacity-planning':         [('capacity-demand-signal', 'Capacity demand signal', 'A demand signal (historical workload or forecast) for a capacity dimension (compute, storage, integration).', 'Observability, planning store.', True, 'non-sensitive'),
                                    ('capacity-policy', 'Capacity policy', 'The capacity-planning policy (thresholds, growth factor, headroom).', 'Policy store.', True, 'non-sensitive')],
    'resource-provisioning':     [('resource-allocation-request', 'Resource allocation request', 'A request to allocate and provision a resource (compute, storage, integration slot) per the capacity plan.', 'Capacity-planning flow.', True, 'non-sensitive'),
                                    ('provisioning-policy', 'Provisioning policy', 'The provisioning policy (region, image, identity, network policy).', 'Policy store.', True, 'non-sensitive')],
    'model-management':          [('model-candidate', 'Model candidate', 'A candidate model under evaluation (training pipeline output, registry pull, or external submission).', 'Model registry, training pipeline.', True, 'non-sensitive'),
                                    ('evaluation-policy', 'Evaluation policy', 'The model evaluation policy (metrics, fairness, drift thresholds).', 'Policy store.', True, 'non-sensitive')],
    'inference-execution':       [('inference-input', 'Inference input', 'The input feature bundle for an inference (real-time or batch).', 'Caller.', True, 'sensitive'),
                                    ('model-reference', 'Model reference', 'The model reference (id + version) to evaluate.', 'Model registry.', True, 'non-sensitive')],
    'interaction-management':    [('interaction-record', 'Interaction record', 'A single interaction (page view, click, conversation turn) with timestamp, channel, identity.', 'Channel instrumentation.', True, 'sensitive'),
                                    ('identity-reference', 'Identity reference', 'The identity reference (subject id, session id) for the interaction.', 'Identity store.', True, 'sensitive')],
    'experience-delivery':       [('experience-signal', 'Experience signal', 'The experience signal for the current session (segment, journey state, recommendation).', 'Signal store.', True, 'sensitive'),
                                    ('rendering-policy', 'Rendering policy', 'The rendering policy (channels, layout, copy variant).', 'Policy store.', True, 'non-sensitive')],
    'index-management':          [('corpus-snapshot', 'Corpus snapshot', 'A snapshot of the corpus to index (delta or full).', 'Content store.', True, 'sensitive'),
                                    ('index-policy', 'Index policy', 'The index policy (tokenization, fields, scoring, retention).', 'Policy store.', True, 'non-sensitive')],
    'query-dispatch':            [('query', 'Query', 'The query (free text or structured expression).', 'Caller.', True, 'non-sensitive'),
                                    ('scope-policy', 'Scope policy', 'The query scope (corpus, tenant, role).', 'Policy store.', True, 'non-sensitive')],
}
F4_OUTPUT_TEMPLATES = {
    'capacity-planning':         ('capacity-plan', 'Capacity plan', 'A capacity plan over the planning horizon (compute, storage, integration).', 'Capacity store, audit log.'),
    'resource-provisioning':     ('provisioned-resource', 'Provisioned resource', 'A provisioned-resource record (target, version, identity, evidence).', 'Resource store, audit log.'),
    'model-management':          ('model-record', 'Model record', 'A model-state-changed record (id, version, evaluation summary, status).', 'Model registry, audit log.'),
    'inference-execution':       ('prediction', 'Prediction', 'A prediction (value, confidence, model reference, input provenance).', 'Caller, audit log.'),
    'interaction-management':    ('interaction-event', 'Interaction event', 'An interaction-recorded event with channel, identity, and content metadata.', 'Event store, audit log.'),
    'experience-delivery':       ('experience-rendered', 'Experience rendered', 'A rendered-experience record (channel, layout, copy variant, signal).', 'Caller, audit log.'),
    'index-management':          ('index-record', 'Index record', 'An index-rebuilt record (corpus version, index version, retention).', 'Index store, audit log.'),
    'query-dispatch':            ('query-result', 'Query result', 'A ranked query result list with provenance for each entry.', 'Caller, audit log.'),
}


def main():
    import yaml as _yaml
    WS2 = Path('entities/v1-alpha/domains')
    total_files = 0
    for domain in P3_DOMAINS:
        domain_id = domain['id']
        domain_name = domain['domain_name']
        domain_code = domain['domain_code']
        domain_slug = domain_id.split(':')[-1]
        domain_dir = f'entities/v1-alpha/domains/{domain_slug}'
        os.makedirs(domain_dir, exist_ok=True)

        # Build F4 entries
        f4_entries = []
        for (f4_id, f4_name, f4_desc, processes, capabilities, components) in domain['f4']:
            slug = f4_id.split(':')[-1].replace('information-system-function-', '')
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

        # Build per-domain index.yaml
        functions_index = []
        for f in f4_entries:
            functions_index.append({'id': f['id'], 'decomposition_level': 'F4', 'lifecycle_status': 'planned', 'parent': f['parent'], 'children': []})
        functions_index.insert(0, {'id': domain['f2']['id'], 'decomposition_level': 'F2', 'lifecycle_status': 'planned', 'parent': None, 'children': [f['id'] for f in f4_entries]})

        # F2 record via the shared helper (composes from F4 children)
        f2_id = domain['f2']['id']
        f2_funcs = [f['id'] for f in f4_entries]
        f2_dir = f'{domain_dir}/functions/dea-isf-{f2_id.split(":")[-1].replace("information-system-function-","")}'
        os.makedirs(f2_dir, exist_ok=True)
        f4_records_for_compose = []
        for fid in f2_funcs:
            f4_slug = fid.split(':')[-1].replace('information-system-function-', '')
            f4_path = WS2 / domain_slug / 'functions' / ('dea-isf-' + f4_slug) / 'function.yaml'
            f4_records_for_compose.append(_yaml.safe_load(open(f4_path)))
        f2_record = build_f2_record(domain, f4_records_for_compose)
        with open(f'{f2_dir}/function.yaml', 'w') as fp:
            fp.write(_yaml.safe_dump(f2_record, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200))
        with open(f'{f2_dir}/README.md', 'w') as fp:
            fp.write(build_f2_readme(f2_record, domain_id, domain_name, domain_code))
        total_files += 2

        idx = {
            'domain': domain_id, 'code': domain_code, 'cr': 'CR-IS-CAT-01C-P3', 'version': '1.0',
            'functions': functions_index, 'change_history': [
                {'version': '1.0', 'date': '2026-10-19', 'cr': 'CR-IS-CAT-01C-P3', 'note': f'P3 population. {len(functions_index)} functions in {domain_name} domain.'},
            ],
        }
        with open(f'{domain_dir}/index.yaml', 'w') as fp:
            fp.write(_yaml.safe_dump(idx, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200))
        total_files += 1

    print(f'Generated {total_files} P3 files (yaml + md).')


if __name__ == '__main__':
    main()
