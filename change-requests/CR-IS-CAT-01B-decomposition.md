# CR-IS-CAT-01B: Information System Function Decomposition and Documentation Standard

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-01B |
| **Title** | Information System Function Decomposition and Documentation Standard |
| **Status** | Proposed (this PR) |
| **Type** | Semantic decomposition and documentation standard |
| **Repository** | technehub-labs/dea-catalog-information-system-functions (legacy URL: technehub-labs/dea-catalog-system-functions until org-admin transfer) |
| **Parent** | CR-IS-CAT-01 (merged 2026-10-18 via PR #2, commit `4358a32`) |
| **Depends on** | CR-IS-CAT-01 (merged); CR-IS-CAT-01A (merged 2026-10-18 via PR #3, commit `a70cf3d`) |
| **Enables** | CR-IS-CAT-01C (population); CR-IS-CAT-01D (integration) |
| **Canonical entity** | `dea:InformationSystemFunction` (class alias `ISF`; OpenDEAM-local `dea:entity-information-system-function`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR establishes the decomposition model, entity specification and documentation requirements for `dea:InformationSystemFunction` records in the Information System Function catalogue. The standard is the third sibling of the 5-CR ISF catalog programme (after CR-IS-CAT-01 foundation and CR-IS-CAT-01A taxonomy).

Per G-06 (programme-wide governance), classification and functional decomposition are separate structures. This CR is decomposition; the taxonomy is in CR-IS-CAT-01A. Per the source doc section 9.2, the F0-F5 decomposition levels are catalogue conventions, NOT new metamodel entity types. The metamodel entity `dea:InformationSystemFunction` remains the only kind of entity a function record is an instance of.

The standard ensures that every function in the catalogue is described consistently, regardless of its domain, complexity, implementation or decomposition level. The standard is intended to make every catalogue entry independently understandable and machine-verifiable.

## 2. Semantic Boundary

An Information System Function represents a defined unit of functional behaviour. It MUST NOT represent:

- An application
- An application component
- An information system service
- A business capability
- A business process
- A user role
- A technology product
- A deployment instance

These may be associated with the function through the appropriate relationships (defined in CR-IS-CAT-01D). They are NOT the function itself.

## 3. Decomposition Model

### 3.1 Hierarchical structure

The catalogue supports the following logical decomposition levels:

| Level | Designation | Description |
|---|---|---|
| F0 | Functional domain context | Classification context, NOT a function instance. Owned by CR-IS-CAT-01A. |
| F1 | Function family | A coherent grouping of related functional behaviours. F1 records are optional; many F2 records will be the top of a hierarchy without an explicit F1 wrapper. |
| F2 | Parent function | A significant, composable functional responsibility. |
| F3 | Subfunction | A more specific functional responsibility. |
| F4 | Atomic function | A sufficiently bounded functional behaviour. F4 records MUST NOT be decomposed merely to create artificial granularity. |
| F5 | Execution operation | Optional implementation-level decomposition, only where justified. F5 is owned by the catalog's relationship to ISC (Information System Component), not by the function hierarchy itself. |

F0 is a taxonomy level, not an entity. F1 through F5 are catalogue decomposition conventions. The classification hierarchy from CR-IS-CAT-01A (functional domains, categories, subcategories) is separate from the decomposition hierarchy. Per G-06, the two hierarchies MUST NOT be conflated.

### 3.2 Decomposition rules

A parent function MAY be decomposed into multiple child functions. The decomposition MUST:

- Preserve the semantic identity of the parent.
- Explain why decomposition is necessary (in the parent's `decomposition_rationale` field).
- Identify the responsibilities allocated to children.
- Avoid duplicate or contradictory responsibilities.
- Identify dependencies between children.
- Describe the parent's input/output boundary.
- Establish whether child functions are collectively sufficient for the parent outcome.
- Record any deliberate overlap or alternative execution paths.

Not every function requires all five decomposition levels. F2 records MAY be the top of a hierarchy without an F1 wrapper. F3 records MAY be skipped if F2 -> F4 is the natural decomposition. F5 is optional and tied to the component relationship, not the function hierarchy.

### 3.3 Composition and orchestration

Composition and orchestration are distinct. Composition expresses structural relationships between functions. Orchestration expresses coordination and control of execution.

A parent function may compose child functions without orchestrating their execution itself. A separate orchestration responsibility MUST be documented where applicable (in the function's `orchestration_responsibility` field).

All relationships MUST use the registered metamodel relationship definitions. The function catalogue MUST NOT invent new relationship semantics. Per G-08, every relationship uses an authorized semantic contract.

## 4. Function Documentation Standard

Every function MUST have the following documentation. The README template (section 5) and the machine-readable schema (section 6) enforce this standard.

### 4.1 Identity

- Canonical ID (`dea:information-system-function-<semantic-name>`)
- Name
- Short name (where applicable)
- Definition
- Description
- Version
- Lifecycle status (proposed, planned, active, deprecated, retired)
- Decomposition level (F1, F2, F3, F4, F5)
- Parent function ID (where applicable)
- Functional domain (cross-reference to `taxonomy/functional-domains.yaml`)
- Category (cross-reference to taxonomy)
- Synonyms and aliases
- Provenance and references

### 4.2 Functional responsibility

- Purpose
- Responsibility statement
- Trigger or activation condition
- Preconditions
- Postconditions
- Expected outcome
- Behavioural boundaries
- In-scope responsibilities
- Explicit exclusions

### 4.3 Inputs

For each input: input identifier, name, definition, data or event reference, source, required/optional status, validation rules, format or schema reference, sensitivity classification (where applicable).

### 4.4 Outputs

For each output: output identifier, name, definition, data or event reference, destination or consumer, output conditions, format or schema reference, quality expectations.

### 4.5 Execution characteristics

- Execution pattern
- Trigger mechanism
- Processing mode
- Synchronous/asynchronous characteristics
- Idempotency expectations
- Retry and recovery behaviour
- Error and exception handling
- Transactional characteristics
- Concurrency characteristics

### 4.6 Relationships

Where applicable:
- Parent and child functions
- Function dependencies
- Orchestrated functions
- Executing components
- Realized business capabilities
- Enabled business processes
- Consumed data
- Produced data
- Consumed events
- Produced events
- Provided or exposed services through associated components
- Integration interfaces

These relationships are CR-IS-CAT-01D's concern; the function record captures the relationship endpoints as IDs, and the integration CR validates them against the metamodel.

### 4.7 Non-functional characteristics

Where applicable:
- Availability expectations
- Performance and latency
- Throughput
- Scalability
- Resilience
- Security
- Privacy
- Auditability
- Recoverability
- Observability
- Compliance constraints

These are expectations or references, not invented performance measurements. Per G-09, completeness must be evidenced, not assumed; missing measurements are recorded as `unmeasured` with a rationale.

### 4.8 Governance

- Functional owner
- Steward
- Approval status
- Criticality
- Lifecycle history
- Source and evidence
- Review date
- Change history

## 5. README Documentation Template

Every catalogue function MUST have its own README.md following the 19-section structure defined in the source doc section 5. The template is implemented at `entities/v1-alpha/domains/<domain>/functions/<function>/README.md` per function.

Sections that do not apply MUST explicitly state `Not applicable to this function.`, rather than being silently omitted from normative documentation.

## 6. Machine-Readable Record

Each function MUST also have a machine-readable representation in `entities/v1-alpha/domains/<domain>/functions/<function>/function.yaml`. The schema is `schemas/entities/information-system-function.v2.json` (the v2 schema; v1 is the simpler schema from CR-IS-CAT-01).

The v2 schema extends the v1 schema with the decomposition, documentation and governance fields defined in sections 3 and 4. The schema does NOT redefine `dea:InformationSystemFunction`; it specializes the v1 schema for catalog use.

Required fields (per source doc section 6):

- id
- type
- name
- description
- version
- lifecycle_status
- functional_domain
- category
- decomposition_level

Additional fields SHOULD capture:

- parent_function
- child_functions
- inputs
- outputs
- execution_characteristics
- functional_owner
- criticality
- references
- metadata

Relationship fields MUST resolve to canonical entity identifiers.

## 7. Directory and Identifier Convention

Recommended structure (per source doc section 7):

```
entities/
  v1-alpha/
    index.yaml
    domains/
      identity-and-access/
        functions/
          dea-isf-identity-verification/
            function.yaml
            README.md
            examples/
              ...
      information-and-data-management/
        functions/
          ...
```

Canonical identifiers SHOULD follow `dea:information-system-function-<semantic-name>`. Example: `dea:information-system-function-identity-verification`.

Identifiers MUST be stable and MUST NOT encode:

- Application names
- Vendor names
- Technology products
- Deployment locations
- Temporary organisational structures

Per G-12, no implementation-specific function becomes canonical merely because it exists in an application.

## 8. Documentation by Decomposition Level

| Level | Minimum documentation emphasis |
|---|---|
| F1 | Family scope, boundaries and constituent functions |
| F2 | Parent responsibility, outcome, inputs/outputs and composition |
| F3 | Specific responsibility, dependencies and behaviour |
| F4 | Detailed behavioural contract, inputs, outputs and exceptions |
| F5 | Execution semantics and implementation-level constraints |

All levels require identity, definition, classification, lifecycle and references.

## 9. Validation

CI MUST verify (per source doc section 9):

1. Every active function has a machine-readable record (`function.yaml`).
2. Every active function has a README.
3. Canonical IDs are unique.
4. Required fields are present.
5. Schema validation succeeds.
6. Parent references resolve.
7. Child references resolve.
8. No composition cycles exist unless an explicitly governed recursive pattern is permitted.
9. Decomposition levels are valid (F1-F5).
10. Relationship references resolve to the correct entity types (this is a soft check in 01B; the hard check is in 01D).
11. Documentation and machine-readable identity agree (the README's identity section matches `function.yaml`).
12. Required sections exist in the README.
13. Examples conform to the schema.
14. No deprecated identity is used for new records.

## 10. Repository Deliverables (this PR)

- `entities/v1-alpha/domains/identity-and-access/functions/dea-isf-identity-verification/` (an F4 atomic function example)
- `entities/v1-alpha/domains/identity-and-access/functions/dea-isf-identity-and-access-management/` (an F2 parent function example with the F4 child)
- `entities/v1-alpha/domains/identity-and-access/functions/dea-isf-identity-verification/function.yaml` (machine-readable record)
- `entities/v1-alpha/domains/identity-and-access/functions/dea-isf-identity-verification/README.md` (README using the 19-section template)
- `entities/v1-alpha/domains/identity-and-access/functions/dea-isf-identity-and-access-management/function.yaml` (machine-readable record)
- `entities/v1-alpha/domains/identity-and-access/functions/dea-isf-identity-and-access-management/README.md` (README using the 19-section template)
- `entities/v1-alpha/domains/identity-and-access/index.yaml` (per-domain function index)
- `entities/v1-alpha/index.yaml` (catalog-level function index)
- `schemas/entities/information-system-function.v2.json` (the v2 schema extending v1)
- `docs/decomposition-guide.md` (the decomposition and documentation standard, mirroring the CR-IS-CAT-01B doc body)
- `templates/function-template.yaml` (the machine-readable record template)
- `templates/README-template.md` (the 19-section README template)
- `.github/workflows/validate-entities.yml` (the entity validation workflow)
- `change-requests/CR-IS-CAT-01B-decomposition.md` (this file)
- `change-requests/README.md` (updated with 01B row)

## 11. CI Requirements

CI MUST validate (per section 9):

- YAML and JSON syntax
- Schema validation against the v2 schema
- Canonical identifier format and uniqueness
- Required fields are present
- Parent and child references resolve
- No composition cycles
- Decomposition levels are valid
- README has the 19 required sections
- README and function.yaml identity agree

The validation is implemented at `.github/workflows/validate-entities.yml`.

## 12. Acceptance Criteria

1. Decomposition levels and their meaning are documented.
2. Composition and orchestration are distinguished.
3. Function README template is published at `templates/README-template.md`.
4. Machine-readable template is published at `templates/function-template.yaml`.
5. Schema is compatible with CR-018 and CR-IS-CAT-01A.
6. Documentation requirements are enforceable.
7. Documentation and entity identity consistency tests pass.
8. Example records exist at multiple decomposition levels (F2 and F4 in this PR).
9. The standard is usable by CR-IS-CAT-01C.

## 13. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Excessive decomposition | Require a meaningful responsibility boundary in `decomposition_rationale` |
| Artificial atomicity | Permit functions to remain undecomposed; F2 may be the top of a hierarchy |
| Parent/child duplication | Require `responsibility_allocation` field; CI validates no overlap |
| README and YAML divergence | Automated consistency check (rule 11 in section 9) |
| Confusion with processes | Maintain distinct semantics per the semantic boundary (section 2) |
| Implementation leakage | Keep technology and deployment details secondary; identifier convention per section 7 |

## 14. Definition of Done

CR-IS-CAT-01B is complete when the decomposition standard, machine-readable templates, README template, examples and validation rules are implemented and enforceable. The standard is published at `docs/decomposition-guide.md`. The 2 example functions (F2 + F4) are committed. The validation workflow is green. CR-IS-CAT-01C can use the standard to populate the initial inventory.

## 15. References

- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01-information-system-functions-rename.md` (parent; merged 2026-10-18 via PR #2, commit `4358a32`)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01A-taxonomy.md` (sibling; merged 2026-10-18 via PR #3, commit `a70cf3d`)
- `technehub-labs/dea-catalog-system-functions/taxonomy/functional-domains.yaml` (the 15-domain taxonomy from 01A)
- `technehub-labs/dea-catalog-system-functions/taxonomy/classification-rules.yaml` (the 11 classification rules from 01A)
- `technehub-labs/dea-catalog-system-functions/schemas/entities/information-system-function.json` (the v1 ISF schema from CR-IS-CAT-01)
- `technehub-labs/dea-metamodel/change-requests/CR-018-information-system-function.md` (the canonical entity)
- `technehub-labs/dea-metamodel/change-requests/CR-MM-PROC-01.md` (kernel+specialization template precedent)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme; source doc section 4)
- `~/.hermes/profiles/coder/kanban/cr-is-cat-01-programme-plan-2026-10-18.md` (reconciliation plan)
- `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-18.md` (snapshot)
- DOCTRINE-MECE card #463 on board 23 (the 7 boundary doctrines from 01A)

## 16. Standing Rules Acknowledged

The following programme-wide governance rules from CR-IS-CAT-01 §7 apply to 01B and are acknowledged in this PR:

- G-01: `dea:InformationSystemFunction` is the only canonical entity for new catalogue records.
- G-03: Metamodel definitions remain authoritative in `dea-metamodel`.
- G-05: Taxonomy nodes are catalogue classifications, not metamodel entities.
- G-06: Classification and functional decomposition are separate structures. (This CR is decomposition; the classification is in 01A.)
- G-07: Every active function has machine-readable content and individual documentation. (This CR enforces it.)
- G-08: Every relationship uses an authorized semantic contract.
- G-09: Catalogue completeness must be evidenced, not assumed.
- G-12: No implementation-specific function becomes canonical merely because it exists in an application.

---

End of CR-IS-CAT-01B.
