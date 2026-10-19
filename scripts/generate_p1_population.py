#!/usr/bin/env python3
"""CR-IS-CAT-01C P1 population generator.

Generates the function records (function.yaml + README.md) and the
per-domain index.yaml for the P1 priority domains. The output is
deterministic: re-running this script produces the same files.

Usage:
  python3 scripts/generate_p1_population.py

This script is the source of truth for the P1 population. Do not hand-edit
the generated files; edit this script and re-run.
"""
import os
import textwrap
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)


def generate_function_yaml(f, domain_id, domain_name):
    out = textwrap.dedent(f"""\
id: {f['id']}
type: InformationSystemFunction
name: "{f['name']}"
description: |
  {textwrap.indent(f['description'], '  ').strip()}
version: "1.0.0"
lifecycle_status: planned
functional_domain: {domain_id}
category: {domain_id}
decomposition_level: {f['level']}
""")
    if f.get('parent'):
        out += f"parent_function: {f['parent']}\n"
    if f.get('children'):
        out += "child_functions:\n" + ''.join(f"  - {c}\n" for c in f['children'])
    if f['level'] == 'F4' and f.get('parent'):
        out += textwrap.dedent(f"""\
decomposition_rationale: |
  Not applicable to this function. F4 is a leaf; the rationale lives on the
  F2 parent ({f['parent']}).
""")
    if f.get('children'):
        out += "responsibility_allocation:\n" + ''.join(
            f"  - child: {c}\n    responsibility: \"See child function record.\"\n" for c in f['children'])
    out += "inputs:\n"
    for i in f['inputs']:
        out += textwrap.dedent(f"""\
  - input_id: {i['id']}
    name: "{i['name']}"
    definition: "{i['definition']}"
    source: "{i['source']}"
    required: {str(i['required']).lower()}
    sensitivity_classification: {i['sensitivity']}
""")
    out += "outputs:\n"
    for o in f['outputs']:
        out += textwrap.dedent(f"""\
  - output_id: {o['id']}
    name: "{o['name']}"
    definition: "{o['definition']}"
    destination: "{o['destination']}"
    output_conditions: "{o['conditions']}"
""")
    out += textwrap.dedent(f"""\
execution_characteristics:
  execution_pattern: {f['exec']['pattern']}
  trigger_mechanism: {f['exec']['trigger']}
  processing_mode: {f['exec']['mode']}
  synchronous_asynchronous: {f['exec']['sync_async']}
  idempotency: {f['exec']['idempotency']}
  transactional: {str(f['exec']['transactional']).lower()}
  concurrency: {f['exec']['concurrency']}
business_alignment:
  realized_capabilities:
{chr(10).join(f'    - {c}' for c in f['capabilities'])}
  enabled_processes:
{chr(10).join(f'    - {p}' for p in f['processes'])}
executing_components:
{chr(10).join(f'  - {c}' for c in f['components'])}
non_functional_characteristics:
  criticality: {f['criticality']}
governance:
  functional_owner: "Architecture team"
  steward: "Architecture team"
  approval_status: proposed
  criticality: {f['criticality']}
  review_date: "2027-10-18"
references:
  - technehub-labs/dea-metamodel/change-requests/CR-018-information-system-function.md
metadata:
  created_by: Emmanuel A. Otchere
  created_date: "2026-10-18"
  last_modified: "2026-10-18"
  cr: CR-IS-CAT-01C
  notes: |
    {f['level']} record in the {domain_name} domain. CR-IS-CAT-01C P1 population.
""")
    return out


def generate_readme(f, domain_id, domain_name, domain_code):
    crit = f['criticality']
    func_event = f['id'].split(':')[-1]
    children = f.get('children', [])
    parent = f.get('parent') or f'None (top of the {domain_name} sub-tree)'
    children_section = (
        '\n'.join(f"{i+1}. `{c}`" for i, c in enumerate(children)) or "None."
    )
    out = textwrap.dedent(f"""\
# {f['name']}

## 1. Identity
- Canonical ID: `{f['id']}`
- Version: 1.0.0
- Lifecycle: planned
- Functional Domain: {domain_code} {domain_name} (`{domain_id}`)
- Category: {domain_code} {domain_name} (categories populated in CR-IS-CAT-01B; v1.0 has no categories yet)
- Decomposition Level: {f['level']}
- Parent Function: {parent}

## 2. Definition

{f['description']}

## 3. Purpose and Responsibility

Responsibility: {f['description']}

## 4. Functional Scope
### In Scope
- {"; ".join(i['name'] for i in f['inputs'])} (inputs)
- {"; ".join(o['name'] for o in f['outputs'])} (outputs)

### Out of Scope
- Workflow coordination (separate domain: ISF-04)
- Data persistence (separate domain: ISF-02 if cross-domain; otherwise child of this domain)
- Identity and access (separate domain: ISF-01)

## 5. Behavioural Specification
### Trigger
{f['exec']['trigger']} ({f['exec']['pattern']})

### Preconditions
- All required inputs are present
- The executing component is reachable
- The audit log is available

### Main Behaviour
{f['description']}

### Alternative Behaviour
Not applicable to this function.

### Exception Behaviour
- Failure of the executing component produces a structured error response
- The audit log records every error

### Postconditions
- The output is produced (or an error response)
- An audit event is recorded

## 6. Inputs

| Input ID | Name | Definition | Source | Required | Sensitivity |
|---|---|---|---|---|---|
""")
    for i in f['inputs']:
        out += f"| `{i['id']}` | {i['name']} | {i['definition']} | {i['source']} | {'Yes' if i['required'] else 'No'} | {i['sensitivity']} |\n"
    out += textwrap.dedent("""
## 7. Outputs

| Output ID | Name | Definition | Destination | Conditions |
|---|---|---|---|---|
""")
    for o in f['outputs']:
        out += f"| `{o['id']}` | {o['name']} | {o['definition']} | {o['destination']} | {o['conditions']} |\n"
    out += textwrap.dedent(f"""
## 8. Data and Event Interaction
### Consumed Data
- (see inputs above)

### Produced Data
- (see outputs above)

### Consumed Events
None.

### Produced Events
- `dea:event-{func_event}-completed` (on success)
- `dea:event-{func_event}-failed` (on failure)

## 9. Composition and Dependencies
### Parent
{parent}

### Child Functions
{children_section}

### Dependencies
- The executing component(s)
- The audit log

### Orchestration
Not applicable to this function. {'The function is F4 (leaf); orchestration is at the ISC layer.' if f['level'] == 'F4' else 'The function composes child functions without orchestrating them; orchestration is at the ISC layer.'}

## 10. Execution Characteristics

| Characteristic | Value |
|---|---|
| Execution pattern | {f['exec']['pattern']} |
| Trigger mechanism | {f['exec']['trigger']} |
| Processing mode | {f['exec']['mode']} |
| Idempotency | {f['exec']['idempotency']} |
| Transactional | {f['exec']['transactional']} |
| Concurrency | {f['exec']['concurrency']} |

## 11. Business Alignment
### Realized Capabilities
""")
    for c in f['capabilities']:
        out += f"- `{c}`\n"
    out += "\n### Enabled Processes\n"
    for p in f['processes']:
        out += f"- `{p}`\n"
    out += "\n## 12. Executing Components\n\n"
    for c in f['components']:
        out += f"- `{c}`\n"
    out += textwrap.dedent(f"""
## 13. Non-Functional Characteristics

| Characteristic | Value |
|---|---|
| Criticality | {crit} |

## 14. Security and Governance

- Functional owner: Architecture team
- Steward: Architecture team
- Approval status: proposed
- Criticality: {crit}

## 15. Measurement and Observability
### Relevant Metrics
- Request rate
- Success rate
- Latency (p50, p95, p99)
- Error rate

### Monitoring Expectations
- Dashboard: {f['name']} health (request rate, success rate, latency, error rate)
- Alerts: error rate > 1% for 5m; p99 latency exceeded for 10m

### Evidence Sources
- Request log
- Response log
- Audit event stream

## 16. Examples and Use Cases

- Use case 1: a standard invocation by a caller via the API gateway
- Use case 2: a high-volume invocation under load with horizontal scaling
- Use case 3: an exceptional case (timeout, validation failure) with the error response

## 17. Limitations and Assumptions

- The function depends on the executing component being available
- The function does not own identity (separate domain: ISF-01)
- The function does not own the persistence of the output (the caller persists if needed)

## 18. References

- `technehub-labs/dea-metamodel/change-requests/CR-018-information-system-function.md`
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01B-decomposition.md`
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01A-taxonomy.md`

## 19. Change History

- 2026-10-18: Initial creation (CR-IS-CAT-01C; P1 population).
""")
    return out


# Domain and function data (compact representation)
FUNCTIONS = {
    'isf:domain:identity-and-access': {
        'domain_name': 'Identity and Access',
        'domain_code': 'ISF-01',
        'functions': [
            {
                'id': 'dea:information-system-function-identity-registration',
                'name': 'Identity Registration',
                'level': 'F4',
                'description': 'The atomic function that registers a new identity: creates the identity record, provisions the initial credentials, and emits the identity-registered event.',
                'parent': 'dea:information-system-function-identity-and-access-management',
                'children': [],
                'inputs': [
                    {'id': 'identity-attributes', 'name': 'Identity attributes', 'definition': 'The set of attributes that constitute the new identity (name, email, employee ID, etc.).', 'source': 'Caller (HR system, registration portal, or self-service).', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'identity-record', 'name': 'Identity record', 'definition': 'A new identity record with a unique identifier, the initial credentials reference, and the registration metadata.', 'destination': 'Identity store, audit log, credential vault.', 'conditions': 'Always produced (or an error response).'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': True, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-identity-broker'],
                'capabilities': ['capabilities:capability-security-management-wmzc7c'],
                'processes': ['dea:process-acquire-and-onboard-agents'],
                'criticality': 'mission-critical',
            },
            {
                'id': 'dea:information-system-function-authentication',
                'name': 'Authentication',
                'level': 'F4',
                'description': 'The atomic function that authenticates a principal: verifies the presented credentials against the stored credential, applies the authentication policy (MFA, step-up), and produces an authentication result.',
                'parent': 'dea:information-system-function-identity-and-access-management',
                'children': [],
                'inputs': [
                    {'id': 'principal-identifier', 'name': 'Principal identifier', 'definition': 'The identifier the principal presents (username, email, biometric template).', 'source': 'Caller (via the authentication flow).', 'required': True, 'sensitivity': 'sensitive'},
                    {'id': 'credential', 'name': 'Credential', 'definition': 'The credential the principal presents (password hash, OTP, biometric signature).', 'source': 'Caller.', 'required': True, 'sensitivity': 'sensitive'},
                    {'id': 'authentication-policy', 'name': 'Authentication policy', 'definition': 'The rules that determine the required authentication factors (single-factor, MFA, step-up).', 'source': 'Policy store.', 'required': True, 'sensitivity': 'non-sensitive'},
                ],
                'outputs': [
                    {'id': 'authentication-result', 'name': 'Authentication result', 'definition': 'The authentication decision (authenticated, not-authenticated, requires-step-up) with the evidence.', 'destination': 'Caller, audit log.', 'conditions': 'Always produced.'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-identity-broker'],
                'capabilities': ['capabilities:capability-security-management-wmzc7c', 'capabilities:capability-security-management-wmzc7c'],
                'processes': ['dea:process-acquire-and-onboard-agents'],
                'criticality': 'mission-critical',
            },
            {
                'id': 'dea:information-system-function-access-policy-evaluation',
                'name': 'Access Policy Evaluation',
                'level': 'F4',
                'description': 'The atomic function that evaluates an access policy against a request: collects the attributes (subject, resource, action, environment), resolves the policy, and produces the allow/deny decision.',
                'parent': 'dea:information-system-function-identity-and-access-management',
                'children': [],
                'inputs': [
                    {'id': 'access-request', 'name': 'Access request', 'definition': 'An access request: subject (who), resource (what), action (read/write/delete), environment (time, location, device).', 'source': 'Caller (the application service).', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'access-decision', 'name': 'Access decision', 'definition': 'The access decision: allow, deny, or not-applicable, with the policy version and the evidence (which rules fired).', 'destination': 'Caller, audit log.', 'conditions': 'Always produced.'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-identity-broker'],
                'capabilities': ['capabilities:capability-security-management-wmzc7c'],
                'processes': ['dea:process-acquire-and-onboard-agents'],
                'criticality': 'mission-critical',
            },
        ],
    },
    'isf:domain:information-and-data-management': {
        'domain_name': 'Information and Data Management',
        'domain_code': 'ISF-02',
        'functions': [
            {
                'id': 'dea:information-system-function-data-management',
                'name': 'Data Management',
                'level': 'F2',
                'description': 'The parent function that composes the data-management sub-tree. It coordinates the acquisition, validation, transformation, persistence, retrieval, retention and disposal of structured data.',
                'children': [
                    'dea:information-system-function-data-acquisition',
                    'dea:information-system-function-data-transformation',
                    'dea:information-system-function-data-retrieval',
                ],
                'parent': None,
                'inputs': [
                    {'id': 'data-lifecycle-event', 'name': 'Data lifecycle event', 'definition': 'A business event that triggers a data management flow (e.g., new record creation, schema change, retention trigger).', 'source': 'Source systems (via ISC integration).', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'data-state', 'name': 'Data state', 'definition': 'The state of the data store: the records, the schema, the indices, the retention markers.', 'destination': 'Data store, audit log, downstream systems.', 'conditions': 'Updated on every child function execution.'},
                ],
                'exec': {'pattern': 'event-driven', 'trigger': 'event', 'mode': 'real-time', 'sync_async': 'asynchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-data-warehouse-platform'],
                'capabilities': ['capabilities:capability-information-management-6vjgdh'],
                'processes': ['dea:process-operate-general-ledger'],
                'criticality': 'business-critical',
            },
            {
                'id': 'dea:information-system-function-data-acquisition',
                'name': 'Data Acquisition',
                'level': 'F4',
                'description': 'The atomic function that acquires data from a source system and prepares it for downstream processing. Acquisition is the entry point of the data lifecycle.',
                'parent': 'dea:information-system-function-data-management',
                'children': [],
                'inputs': [
                    {'id': 'source-record', 'name': 'Source record', 'definition': 'A record ingested from a source system (database change capture, file drop, API webhook, event).', 'source': 'Source system via the integration layer.', 'required': True, 'sensitivity': 'sensitive'},
                    {'id': 'acquisition-policy', 'name': 'Acquisition policy', 'definition': 'The schema, validation rules and routing rules for the acquired record.', 'source': 'Policy store.', 'required': True, 'sensitivity': 'non-sensitive'},
                ],
                'outputs': [
                    {'id': 'acquired-record', 'name': 'Acquired record', 'definition': 'A record that has been acquired, validated against the schema and routed for downstream processing.', 'destination': 'Downstream data processing pipeline.', 'conditions': 'Always produced (or an error response).'},
                ],
                'exec': {'pattern': 'streaming', 'trigger': 'event', 'mode': 'real-time', 'sync_async': 'asynchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-data-warehouse-platform'],
                'capabilities': ['capabilities:capability-information-management-6vjgdh'],
                'processes': ['dea:process-operate-general-ledger'],
                'criticality': 'business-critical',
            },
            {
                'id': 'dea:information-system-function-data-transformation',
                'name': 'Data Transformation',
                'level': 'F4',
                'description': 'The atomic function that transforms data from one schema or shape to another. Transformation includes normalization, enrichment, aggregation and projection.',
                'parent': 'dea:information-system-function-data-management',
                'children': [],
                'inputs': [
                    {'id': 'input-record', 'name': 'Input record', 'definition': 'A record in the source schema.', 'source': 'Data acquisition pipeline.', 'required': True, 'sensitivity': 'sensitive'},
                    {'id': 'transformation-spec', 'name': 'Transformation specification', 'definition': 'The mapping rules, expressions and filters for the transformation.', 'source': 'Transformation spec registry.', 'required': True, 'sensitivity': 'non-sensitive'},
                ],
                'outputs': [
                    {'id': 'output-record', 'name': 'Output record', 'definition': 'A record in the target schema.', 'destination': 'Downstream pipeline or data store.', 'conditions': 'Always produced (or an error response).'},
                ],
                'exec': {'pattern': 'batch', 'trigger': 'schedule', 'mode': 'near-real-time', 'sync_async': 'asynchronous', 'idempotency': 'idempotent', 'transactional': True, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-data-warehouse-platform'],
                'capabilities': ['capabilities:capability-information-management-6vjgdh'],
                'processes': ['dea:process-operate-general-ledger'],
                'criticality': 'business-critical',
            },
            {
                'id': 'dea:information-system-function-data-retrieval',
                'name': 'Data Retrieval',
                'level': 'F4',
                'description': 'The atomic function that retrieves data by query or by key. Retrieval is read-only and is the dominant data access pattern for application services.',
                'parent': 'dea:information-system-function-data-management',
                'children': [],
                'inputs': [
                    {'id': 'query-spec', 'name': 'Query specification', 'definition': 'A query (SQL, NoSQL, search, vector) with parameters.', 'source': 'Caller (via API).', 'required': True, 'sensitivity': 'non-sensitive'},
                ],
                'outputs': [
                    {'id': 'result-set', 'name': 'Result set', 'definition': 'A set of records matching the query.', 'destination': 'Caller.', 'conditions': 'Always produced (possibly empty).'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-data-warehouse-platform'],
                'capabilities': ['capabilities:capability-information-management-6vjgdh'],
                'processes': ['dea:process-operate-general-ledger'],
                'criticality': 'mission-critical',
            },
        ],
    },
    'isf:domain:transaction-processing': {
        'domain_name': 'Transaction Processing',
        'domain_code': 'ISF-03',
        'functions': [
            {
                'id': 'dea:information-system-function-transaction-processing',
                'name': 'Transaction Processing',
                'level': 'F2',
                'description': 'The parent function that composes the transaction-processing sub-tree. It coordinates the initiation, validation, execution, settlement, posting, reconciliation, reversal and cancellation of transactions.',
                'children': [
                    'dea:information-system-function-transaction-initiation',
                    'dea:information-system-function-transaction-execution',
                    'dea:information-system-function-transaction-reconciliation',
                ],
                'parent': None,
                'inputs': [
                    {'id': 'transaction-request', 'name': 'Transaction request', 'definition': 'A request to initiate a transaction (a financial transaction, a state change, a business event).', 'source': 'Caller (via API).', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'transaction-state', 'name': 'Transaction state', 'definition': 'The state of the transaction: initiated, validated, executed, settled, posted, reconciled, reversed, cancelled.', 'destination': 'Transaction store, audit log, downstream systems.', 'conditions': 'Updated on every child function execution.'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': True, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-order-management-system'],
                'capabilities': ['capabilities:capability-financial-resource-management-cd3c7c'],
                'processes': ['dea:process-run-accounts-receivable'],
                'criticality': 'mission-critical',
            },
            {
                'id': 'dea:information-system-function-transaction-initiation',
                'name': 'Transaction Initiation',
                'level': 'F4',
                'description': 'The atomic function that initiates a transaction. It validates the request, performs the authorization check, and produces a transaction record in the initiated state.',
                'parent': 'dea:information-system-function-transaction-processing',
                'children': [],
                'inputs': [
                    {'id': 'initiation-request', 'name': 'Initiation request', 'definition': 'A request to initiate a transaction.', 'source': 'Caller (via API).', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'initiated-transaction', 'name': 'Initiated transaction', 'definition': 'A transaction record in the initiated state, with an authorization decision.', 'destination': 'Transaction store, audit log.', 'conditions': 'Always produced (or an error response).'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': True, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-order-management-system'],
                'capabilities': ['capabilities:capability-financial-resource-management-cd3c7c'],
                'processes': ['dea:process-run-accounts-receivable'],
                'criticality': 'mission-critical',
            },
            {
                'id': 'dea:information-system-function-transaction-execution',
                'name': 'Transaction Execution',
                'level': 'F4',
                'description': 'The atomic function that executes a transaction. It applies the transaction logic, produces the post-state, and emits the execution result.',
                'parent': 'dea:information-system-function-transaction-processing',
                'children': [],
                'inputs': [
                    {'id': 'authorized-transaction', 'name': 'Authorized transaction', 'definition': 'A transaction record in the validated state.', 'source': 'Transaction store.', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'executed-transaction', 'name': 'Executed transaction', 'definition': 'A transaction record in the executed state, with the post-state and the execution result.', 'destination': 'Transaction store, audit log.', 'conditions': 'Always produced (or an error response).'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': True, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-order-management-system'],
                'capabilities': ['capabilities:capability-financial-resource-management-cd3c7c'],
                'processes': ['dea:process-run-accounts-receivable'],
                'criticality': 'mission-critical',
            },
            {
                'id': 'dea:information-system-function-transaction-reconciliation',
                'name': 'Transaction Reconciliation',
                'level': 'F4',
                'description': 'The atomic function that reconciles two transaction records (e.g., a local record and an external record) and produces a reconciliation result (matched, mismatched, pending).',
                'parent': 'dea:information-system-function-transaction-processing',
                'children': [],
                'inputs': [
                    {'id': 'local-record', 'name': 'Local record', 'definition': 'The local transaction record.', 'source': 'Transaction store.', 'required': True, 'sensitivity': 'sensitive'},
                    {'id': 'external-record', 'name': 'External record', 'definition': 'The external transaction record (e.g., from a counterparty, a clearing house, a payment processor).', 'source': 'External system via integration.', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'reconciliation-result', 'name': 'Reconciliation result', 'definition': 'The reconciliation decision (matched, mismatched, pending) with the evidence.', 'destination': 'Reconciliation store, audit log.', 'conditions': 'Always produced.'},
                ],
                'exec': {'pattern': 'batch', 'trigger': 'schedule', 'mode': 'eventual', 'sync_async': 'asynchronous', 'idempotency': 'idempotent', 'transactional': True, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-order-management-system'],
                'capabilities': ['capabilities:capability-financial-resource-management-cd3c7c'],
                'processes': ['dea:process-run-accounts-receivable'],
                'criticality': 'mission-critical',
            },
        ],
    },
    'isf:domain:workflow-and-orchestration': {
        'domain_name': 'Workflow and Orchestration',
        'domain_code': 'ISF-04',
        'functions': [
            {
                'id': 'dea:information-system-function-workflow-orchestration',
                'name': 'Workflow Orchestration',
                'level': 'F2',
                'description': 'The parent function that composes the workflow-orchestration sub-tree. It coordinates the sequencing, routing, scheduling, escalation and completion of business tasks.',
                'children': [
                    'dea:information-system-function-workflow-execution',
                    'dea:information-system-function-task-routing',
                ],
                'parent': None,
                'inputs': [
                    {'id': 'workflow-event', 'name': 'Workflow event', 'definition': 'A business event that triggers a workflow (e.g., new order, claim, application).', 'source': 'Source systems (via ISC integration).', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'workflow-state', 'name': 'Workflow state', 'definition': 'The state of the workflow: initiated, in-progress, suspended, completed, escalated, exception.', 'destination': 'Workflow store, audit log, downstream systems.', 'conditions': 'Updated on every child function execution.'},
                ],
                'exec': {'pattern': 'event-driven', 'trigger': 'event', 'mode': 'real-time', 'sync_async': 'asynchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-order-management-orchestrator'],
                'capabilities': ['capabilities:capability-operations-management-pm3w8k'],
                'processes': ['dea:process-operate-service-delivery'],
                'criticality': 'business-critical',
            },
            {
                'id': 'dea:information-system-function-workflow-execution',
                'name': 'Workflow Execution',
                'level': 'F4',
                'description': 'The atomic function that executes a workflow step. It applies the step logic, transitions the workflow state, and emits the step result.',
                'parent': 'dea:information-system-function-workflow-orchestration',
                'children': [],
                'inputs': [
                    {'id': 'workflow-step', 'name': 'Workflow step', 'definition': 'A step in a workflow instance: the activity, the input, the current state.', 'source': 'Workflow store.', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'step-result', 'name': 'Step result', 'definition': 'The result of the step: success, failure, suspended, with the post-state and the next step.', 'destination': 'Workflow store, audit log.', 'conditions': 'Always produced.'},
                ],
                'exec': {'pattern': 'event-driven', 'trigger': 'event', 'mode': 'real-time', 'sync_async': 'asynchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-order-management-orchestrator'],
                'capabilities': ['capabilities:capability-operations-management-pm3w8k'],
                'processes': ['dea:process-operate-service-delivery'],
                'criticality': 'business-critical',
            },
            {
                'id': 'dea:information-system-function-task-routing',
                'name': 'Task Routing',
                'level': 'F4',
                'description': 'The atomic function that routes a task to a queue, a role, an agent, or a human. The routing decision is based on the task type, the routing rules, and the current state of the work pool.',
                'parent': 'dea:information-system-function-workflow-orchestration',
                'children': [],
                'inputs': [
                    {'id': 'task', 'name': 'Task', 'definition': 'A task to be routed: the task type, the input, the priority.', 'source': 'Workflow engine or external system.', 'required': True, 'sensitivity': 'sensitive'},
                    {'id': 'routing-rules', 'name': 'Routing rules', 'definition': 'The rules that determine the routing target.', 'source': 'Routing rule registry.', 'required': True, 'sensitivity': 'non-sensitive'},
                ],
                'outputs': [
                    {'id': 'routed-task', 'name': 'Routed task', 'definition': 'A task with a routing target assigned.', 'destination': 'Work pool, queue, agent inbox.', 'conditions': 'Always produced.'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-order-management-orchestrator'],
                'capabilities': ['capabilities:capability-operations-management-pm3w8k'],
                'processes': ['dea:process-operate-service-delivery'],
                'criticality': 'business-critical',
            },
        ],
    },
    'isf:domain:integration-and-interoperability': {
        'domain_name': 'Integration and Interoperability',
        'domain_code': 'ISF-05',
        'functions': [
            {
                'id': 'dea:information-system-function-integration-and-interoperability',
                'name': 'Integration and Interoperability',
                'level': 'F2',
                'description': 'The parent function that composes the integration sub-tree. It coordinates the API interaction, protocol mediation, message transformation, event distribution and external-system synchronization.',
                'children': [
                    'dea:information-system-function-api-request-handling',
                    'dea:information-system-function-event-publication',
                    'dea:information-system-function-interface-validation',
                ],
                'parent': None,
                'inputs': [
                    {'id': 'integration-event', 'name': 'Integration event', 'definition': 'A business event that triggers integration (an API call, a message, an event).', 'source': 'Caller systems (via API gateway or message broker).', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'integration-state', 'name': 'Integration state', 'definition': 'The state of the integration: received, validated, transformed, dispatched, acknowledged.', 'destination': 'Integration store, audit log, downstream systems.', 'conditions': 'Updated on every child function execution.'},
                ],
                'exec': {'pattern': 'event-driven', 'trigger': 'event', 'mode': 'real-time', 'sync_async': 'asynchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-api-gateway', 'dea:information-system-component-api-gateway-router'],
                'capabilities': ['capabilities:capability-technology-enablement-y6nkws'],
                'processes': ['dea:process-operate-technology-platforms'],
                'criticality': 'mission-critical',
            },
            {
                'id': 'dea:information-system-function-api-request-handling',
                'name': 'API Request Handling',
                'level': 'F4',
                'description': 'The atomic function that handles an API request: authentication, authorization, rate limiting, routing, response shaping, and audit.',
                'parent': 'dea:information-system-function-integration-and-interoperability',
                'children': [],
                'inputs': [
                    {'id': 'api-request', 'name': 'API request', 'definition': 'An HTTP/gRPC/GraphQL request with headers, body, and authentication context.', 'source': 'Caller (via the API gateway).', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'api-response', 'name': 'API response', 'definition': 'A response to the API request: status code, headers, body.', 'destination': 'Caller.', 'conditions': 'Always produced (or an error response).'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-api-gateway'],
                'capabilities': ['capabilities:capability-technology-enablement-y6nkws'],
                'processes': ['dea:process-operate-technology-platforms'],
                'criticality': 'mission-critical',
            },
            {
                'id': 'dea:information-system-function-event-publication',
                'name': 'Event Publication',
                'level': 'F4',
                'description': 'The atomic function that publishes a domain event to the event bus. The publication is at-least-once with ordering guarantees per partition key.',
                'parent': 'dea:information-system-function-integration-and-interoperability',
                'children': [],
                'inputs': [
                    {'id': 'domain-event', 'name': 'Domain event', 'definition': 'A domain event: the event type, the event payload, the partition key, the metadata.', 'source': 'Source system.', 'required': True, 'sensitivity': 'sensitive'},
                ],
                'outputs': [
                    {'id': 'publication-result', 'name': 'Publication result', 'definition': 'The publication result: the event ID, the offset, the partition, the publication timestamp.', 'destination': 'Event store, audit log.', 'conditions': 'Always produced (or an error response).'},
                ],
                'exec': {'pattern': 'streaming', 'trigger': 'event', 'mode': 'real-time', 'sync_async': 'asynchronous', 'idempotency': 'idempotent', 'transactional': True, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-api-gateway-router'],
                'capabilities': ['capabilities:capability-technology-enablement-y6nkws'],
                'processes': ['dea:process-operate-technology-platforms'],
                'criticality': 'mission-critical',
            },
            {
                'id': 'dea:information-system-function-interface-validation',
                'name': 'Interface Validation',
                'level': 'F4',
                'description': 'The atomic function that validates an interface contract: schema conformance, semantic conformance, and contract version. Returns accepted, rejected, or warning.',
                'parent': 'dea:information-system-function-integration-and-interoperability',
                'children': [],
                'inputs': [
                    {'id': 'interface-payload', 'name': 'Interface payload', 'definition': 'A payload to be validated against an interface contract.', 'source': 'Caller.', 'required': True, 'sensitivity': 'sensitive'},
                    {'id': 'interface-contract', 'name': 'Interface contract', 'definition': 'The contract: schema, semantic rules, version.', 'source': 'Contract registry.', 'required': True, 'sensitivity': 'non-sensitive'},
                ],
                'outputs': [
                    {'id': 'validation-result', 'name': 'Validation result', 'definition': 'The validation result: accepted, rejected (with reason), or warning (with reason).', 'destination': 'Caller, audit log.', 'conditions': 'Always produced.'},
                ],
                'exec': {'pattern': 'synchronous', 'trigger': 'api-call', 'mode': 'real-time', 'sync_async': 'synchronous', 'idempotency': 'idempotent', 'transactional': False, 'concurrency': 'multi-threaded'},
                'components': ['dea:information-system-component-api-gateway'],
                'capabilities': ['capabilities:capability-technology-enablement-y6nkws'],
                'processes': ['dea:process-operate-technology-platforms'],
                'criticality': 'mission-critical',
            },
        ],
    },
}


def main():
    total_files = 0
    for domain_id, domain_data in FUNCTIONS.items():
        domain_slug = domain_id.split(':')[-1]
        domain_dir = f'entities/v1-alpha/domains/{domain_slug}'
        os.makedirs(domain_dir, exist_ok=True)

        for f in domain_data['functions']:
            func_slug = f['id'].split(':')[-1].replace('information-system-function-', '')
            func_dir = f'{domain_dir}/functions/dea-isf-{func_slug}'
            os.makedirs(func_dir, exist_ok=True)

            with open(f'{func_dir}/function.yaml', 'w') as fp:
                fp.write(generate_function_yaml(f, domain_id, domain_data['domain_name']))
            with open(f'{func_dir}/README.md', 'w') as fp:
                fp.write(generate_readme(f, domain_id, domain_data['domain_name'], domain_data['domain_code']))
            total_files += 2

        # Per-domain index.yaml
        functions_index = []
        for f in domain_data['functions']:
            functions_index.append({
                'id': f['id'],
                'decomposition_level': f['level'],
                'lifecycle_status': 'planned',
                'parent': f.get('parent'),
                'children': f.get('children', []),
            })

        # For the identity-and-access domain, include the 2 records from 01B
        if domain_id == 'isf:domain:identity-and-access':
            # CR-IS-CAT-01R: 4 children removed -- documented deferred/excluded per CR-IS-CAT-01C
            # coverage report (authorization deferred to ISF-09 Security Privacy and Trust;
            # session-management, identity-provisioning, identity-deprovisioning excluded:
            # "will be separate F4 records in a follow-up CR").
            functions_index.append({
                'id': 'dea:information-system-function-identity-and-access-management',
                'decomposition_level': 'F2',
                'lifecycle_status': 'planned',
                'parent': None,
                'children': [
                    'dea:information-system-function-identity-registration',
                    'dea:information-system-function-identity-verification',
                    'dea:information-system-function-authentication',
                    'dea:information-system-function-access-policy-evaluation',
                ],
            })
            functions_index.append({
                'id': 'dea:information-system-function-identity-verification',
                'decomposition_level': 'F4',
                'lifecycle_status': 'planned',
                'parent': 'dea:information-system-function-identity-and-access-management',
                'children': [],
            })

        index_data = {
            'domain': domain_id,
            'code': domain_data['domain_code'],
            'cr': 'CR-IS-CAT-01C',
            'version': '1.0',
            'functions': functions_index,
            'change_history': [
                {'version': '1.0', 'date': '2026-10-18', 'cr': 'CR-IS-CAT-01C', 'note': f"Initial P1 population. {len(functions_index)} functions in the {domain_data['domain_name']} domain."},
            ],
        }
        with open(f'{domain_dir}/index.yaml', 'w') as fp:
            yaml.dump(index_data, fp, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200)

    # Catalog-level index
    catalog_index = {
        'catalog': 'dea-catalog-information-system-functions',
        'version': '1.0',
        'cr': 'CR-IS-CAT-01C',
        'date': '2026-10-18',
        'domains': [
            {'code': d['domain_code'], 'id': did, 'name': d['domain_name'], 'index': f"domains/{did.split(':')[-1]}/index.yaml", 'function_count': sum(1 for f in d['functions']) + (2 if did == 'isf:domain:identity-and-access' else 0)}
            for did, d in FUNCTIONS.items()
        ],
        'change_history': [
            {'version': '1.0', 'date': '2026-10-18', 'cr': 'CR-IS-CAT-01C', 'note': f"Initial P1 population. {sum(1 + len(d['functions']) + (2 if did == 'isf:domain:identity-and-access' else 0) for did, d in FUNCTIONS.items())} functions across {len(FUNCTIONS)} P1 domains."},
        ],
    }
    with open('entities/v1-alpha/index.yaml', 'w') as fp:
        yaml.dump(catalog_index, fp, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200)

    print(f"Generated {total_files} function records (yaml + md) + {len(FUNCTIONS)} domain indexes + 1 catalog index")


if __name__ == '__main__':
    main()
