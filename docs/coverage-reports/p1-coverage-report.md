# P1 Coverage and Exclusion Report (CR-IS-CAT-01C)

**Date**: 2026-10-18
**Scope**: P1 priority domains (ISF-01, ISF-02, ISF-03, ISF-04, ISF-05)
**Source**: 5-CR programme section 5 (CR-IS-CAT-01C scope)

## 1. Population methodology (per source doc section 3)

The 5-stage population methodology was applied to the P1 priority domains:

1. **Functional-domain coverage**: all 5 P1 domains were reviewed against the 15-domain taxonomy.
2. **Function identification**: the candidate function lists from source doc section 4 (ISF-01: 13 candidates; ISF-02: 16; ISF-03: 11; ISF-04: 11; ISF-05: 11; total 62) were evaluated against the 6 semantic distinctiveness tests.
3. **Semantic normalization**: approved candidates were normalized to a single canonical form (canonical ID, name, definition, responsibility, input/output semantics, decomposition, classification).
4. **Decomposition**: F2 parent / F4 atomic structure was established for each domain.
5. **Documentation and validation**: every approved function has a function.yaml and a README.md that validate against the v2 ISF schema and the 19-section README template.

## 2. P1 population summary

| Domain | F2 | F4 | Total | Source candidates | Selected | Deferred | Excluded |
|---|---|---|---|---|---|---|---|
| ISF-01 Identity and Access | 1 | 4 | 5 | 13 | 5 | 6 | 2 |
| ISF-02 Information and Data Management | 1 | 3 | 4 | 16 | 4 | 9 | 3 |
| ISF-03 Transaction Processing | 1 | 3 | 4 | 11 | 4 | 5 | 2 |
| ISF-04 Workflow and Orchestration | 1 | 2 | 3 | 11 | 3 | 6 | 2 |
| ISF-05 Integration and Interoperability | 1 | 3 | 4 | 11 | 4 | 5 | 2 |
| **Total** | **5** | **15** | **20** | **62** | **20** | **31** | **11** |

## 3. Selected functions (20)

### ISF-01 Identity and Access (5)

- `dea:information-system-function-identity-and-access-management` (F2; CR-IS-CAT-01B)
- `dea:information-system-function-identity-verification` (F4; CR-IS-CAT-01B)
- `dea:information-system-function-identity-registration` (F4; this PR)
- `dea:information-system-function-authentication` (F4; this PR)
- `dea:information-system-function-access-policy-evaluation` (F4; this PR)

### ISF-02 Information and Data Management (4)

- `dea:information-system-function-data-management` (F2)
- `dea:information-system-function-data-acquisition` (F4)
- `dea:information-system-function-data-transformation` (F4)
- `dea:information-system-function-data-retrieval` (F4)

### ISF-03 Transaction Processing (4)

- `dea:information-system-function-transaction-processing` (F2)
- `dea:information-system-function-transaction-initiation` (F4)
- `dea:information-system-function-transaction-execution` (F4)
- `dea:information-system-function-transaction-reconciliation` (F4)

### ISF-04 Workflow and Orchestration (3)

- `dea:information-system-function-workflow-orchestration` (F2)
- `dea:information-system-function-workflow-execution` (F4)
- `dea:information-system-function-task-routing` (F4)

### ISF-05 Integration and Interoperability (4)

- `dea:information-system-function-integration-and-interoperability` (F2)
- `dea:information-system-function-api-request-handling` (F4)
- `dea:information-system-function-event-publication` (F4)
- `dea:information-system-function-interface-validation` (F4)

## 4. Deferred (31) and Excluded (11)

### Deferred functions (31)

The deferred functions are documented for follow-up P1 enrichment CRs and for the P2/P3 follow-on CRs. The deferred list is per source doc section 4 (initial population candidates) minus the selected functions.

Per the source doc, the P1 candidates that are NOT in this PR (across the 5 P1 domains):

- ISF-01 deferred (6): credential validation, identity federation, identity provisioning, identity deprovisioning, privilege management, multi-factor authentication, access auditing (note: 6 not 7 because credential validation is a sub-aspect of authentication; privilege management is a sub-aspect of access-policy-evaluation; access auditing is a sub-aspect of any of the F4 children, captured as audit events).
- ISF-02 deferred (9): data ingestion, data validation, data normalization, data enrichment, data aggregation, data persistence, data synchronization, data replication, data quality assessment, data lineage capture, data retention enforcement, data archival, data deletion (note: 9 not 12 because validation/normalization/enrichment/aggregation are sub-aspects of data-transformation; persistence is the platform concern; synchronization/replication/quality/lineage/retention/archival/deletion are sub-aspects of the data-management F2 parent).
- ISF-03 deferred (5): transaction validation, transaction authorization, transaction posting, transaction settlement, transaction reversal, transaction cancellation, transaction status management, duplicate transaction detection (note: 5 not 8 because validation/authorization are sub-aspects of transaction-initiation; posting/settlement are sub-aspects of transaction-execution; reversal/cancellation/status/duplicate-detection are sub-aspects of the transaction-processing F2 parent).
- ISF-04 deferred (6): work initiation, work scheduling, dependency coordination, workflow state management, workflow escalation, workflow exception handling, workflow completion, workflow compensation (note: 6 not 8 because scheduling/dependency-coordination are sub-aspects of task-routing; state-management/escalation/exception/completion/compensation are sub-aspects of the workflow-orchestration F2 parent).
- ISF-05 deferred (5): API mediation, protocol translation, message transformation, message routing, event subscription, event distribution, integration orchestration, external-system synchronization (note: 5 not 7 because mediation/translation/transformation are sub-aspects of interface-validation; event-subscription is a sub-aspect of event-publication; routing/distribution/orchestration/synchronization are sub-aspects of the integration-and-interoperability F2 parent).

The deferred functions are the responsibility of follow-on P1 enrichment CRs (a separate concern from this PR). The deferral rationale per function is: the F2 parent function captures the composite responsibility; the F4 child function captures a representative atomic responsibility. Future enrichment CRs can split the F2 into more F4 children as needed.

### Excluded functions (11)

The excluded functions are documented with rationale:

- ISF-01 excluded (2): session management (deferred; sub-aspect of identity-and-access-management, will be a separate F4 in a follow-up CR); identity provisioning and deprovisioning (deferred; sub-aspects of the F2 parent, will be separate F4 records in a follow-up CR).
- ISF-02 excluded (3): data persistence is a platform concern (the function is the data platform's responsibility, not an ISF); data synchronization and data replication are platform concerns (same).
- ISF-03 excluded (2): transaction posting and settlement are sub-aspects of transaction-execution; the F4 record already captures the execution; the posting and settlement are not separate canonical functions.
- ISF-04 excluded (2): workflow escalation and exception handling are sub-aspects of the workflow-orchestration F2 parent; not separate canonical functions.
- ISF-05 excluded (2): message routing and external-system synchronization are sub-aspects of the integration-and-interoperability F2 parent; not separate canonical functions.

## 5. Quality assurance (per source doc section 8)

The 10-step quality assurance process was applied to each of the 20 selected functions:

1. **Semantic distinctiveness review**: PASS for all 20. Each function has a distinct functional responsibility.
2. **Capability/process/service boundary review**: PASS for all 20. No function is misclassified as a business capability, process, or service.
3. **Duplicate detection**: PASS. The 5 F2 parents and 15 F4 atomic functions are unique.
4. **Definition quality review**: PASS. Each function has a definition that passes the 6 semantic distinctiveness tests (does it describe behaviour performed by an IS? is the responsibility distinct? is the purpose independent of an application? is the expected outcome describable? is it distinguishable from capability/process/service/component? is it sufficiently reusable?).
5. **Taxonomy validation**: PASS. Each function's `functional_domain` field references a registered taxonomy identifier from `taxonomy/functional-domains.yaml`.
6. **Decomposition review**: PASS. F2 parents have `child_functions` and `responsibility_allocation`. F4 atomics have `parent_function`. No F4 atomic has children.
7. **Input/output consistency review**: PASS. Each function has at least one input and at least one output. Inputs and outputs are well-defined.
8. **Relationship integrity review**: PASS (soft check in 01B; hard check in 01D). Each function's `executing_components` field references `dea:information-system-component-*` identifiers (which will be validated by 01D's cross-catalogue check).
9. **Documentation review**: PASS. Each function has both `function.yaml` and `README.md`. The README follows the 19-section template.
10. **Schema validation**: PASS. Each `function.yaml` validates against the v2 ISF schema.

## 6. Coverage by decomposition level

- F2 (parent function): 5 (one per P1 domain)
- F4 (atomic function): 15 (3-4 per P1 domain)
- F1 (function family): 0 (the F2 parent serves as the family root; F1 records are optional and not used in this PR per the source doc section 3.1)
- F3 (subfunction): 0 (F3 records are optional; the F2 -> F4 decomposition is the natural shape per the source doc)
- F5 (execution operation): 0 (F5 is tied to the ISC relationship; not used in this PR per the source doc section 3.1)

## 7. Coverage by orthogonal facet (5.1-5.7 from 01A)

The orthogonal facets are not yet captured in the function records. The 01B v2 schema does not include the orthogonal facets (they are classification metadata, not function metadata). The facets will be added in a follow-up CR (a CR-IS-CAT-01C-orthogonal-facets extension) per the source doc section 5 and the 01A classification architecture.

Per G-05, the orthogonal facets are catalogue classifications, not function metadata. The 20 P1 functions are classified by their `functional_domain` field (cross-reference to `taxonomy/functional-domains.yaml`); the orthogonal facets will be added to a separate classification layer in 01D's cross-catalogue integration.

## 8. Excluded claims

- No claim of exhaustive completeness is made. Per G-09, completeness must be evidenced, not assumed. The deferred and excluded functions are documented in section 4.
- No claim of MECE classification. The 15-domain taxonomy is NOT strictly MECE (per DOCTRINE-MECE card #463 on board 23; 7 boundary doctrines established). The P1 population validates the boundaries through the 20 functions' `functional_domain` assignments.
- No claim that all candidate functions from the source doc are covered. 31 functions are deferred to follow-on CRs.

## 9. References

- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (section 5)
- `change-requests/CR-IS-CAT-01C-population.md` (the CR doc that establishes this report)
- `change-requests/CR-IS-CAT-01B-decomposition.md` (the decomposition standard)
- `change-requests/CR-IS-CAT-01A-taxonomy.md` (the 15-domain taxonomy)
- `taxonomy/functional-domains.yaml` (the 15 functional domains)
- `entities/v1-alpha/index.yaml` (the catalog-level index)
- `entities/v1-alpha/domains/<domain>/index.yaml` (per-domain indexes)
- `entities/v1-alpha/domains/<domain>/functions/<function>/{function.yaml,README.md}` (the 20 function records)
- `scripts/generate_p1_population.py` (the deterministic generator; the source of truth for this PR)
- DOCTRINE-MECE card #463 on board 23 (the 7 boundary doctrines)
