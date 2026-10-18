# Decomposition and documentation guide :  Information System Function

This guide implements the standard established in `change-requests/CR-IS-CAT-01B-decomposition.md`. It is the catalogue-level reference for how every Information System Function (`dea:InformationSystemFunction`) record is decomposed and documented.

## 1. Decomposition model

The catalogue supports the following logical decomposition levels:

| Level | Designation | Description |
|---|---|---|
| F0 | Functional domain context | Classification context, NOT a function instance. Owned by CR-IS-CAT-01A. |
| F1 | Function family | A coherent grouping of related functional behaviours. F1 records are optional. |
| F2 | Parent function | A significant, composable functional responsibility. |
| F3 | Subfunction | A more specific functional responsibility. |
| F4 | Atomic function | A sufficiently bounded functional behaviour. F4 records MUST NOT be decomposed merely to create artificial granularity. |
| F5 | Execution operation | Optional implementation-level decomposition, only where justified. Tied to the component relationship. |

F0 is a taxonomy level, not an entity. F1 through F5 are catalogue decomposition conventions, NOT new metamodel entity types. The classification hierarchy (CR-IS-CAT-01A) and the decomposition hierarchy (this guide) MUST remain separate structures (G-06).

## 2. Composition vs orchestration

Composition expresses structural relationships between functions. Orchestration expresses coordination and control of execution. A parent function may compose child functions without orchestrating their execution itself. A separate orchestration responsibility MUST be documented where applicable (in the function's `orchestration_responsibility` field).

## 3. Decomposition rules

A parent function MAY be decomposed into multiple child functions. The decomposition MUST:

- Preserve the semantic identity of the parent.
- Explain why decomposition is necessary (in the parent's `decomposition_rationale` field).
- Identify the responsibilities allocated to children (in `responsibility_allocation`).
- Avoid duplicate or contradictory responsibilities.
- Identify dependencies between children.
- Describe the parent's input/output boundary.
- Establish whether child functions are collectively sufficient for the parent outcome.
- Record any deliberate overlap or alternative execution paths.

## 4. Documentation standard

Every function MUST have the 19-section README AND the machine-readable YAML. Both are normative. The sections that do not apply MUST explicitly state `Not applicable to this function.`, rather than being silently omitted.

### 4.1 README template (19 sections)

1. Identity (canonical ID, version, lifecycle, functional domain, category, decomposition level, parent function)
2. Definition
3. Purpose and Responsibility
4. Functional Scope (In Scope, Out of Scope)
5. Behavioural Specification (Trigger, Preconditions, Main Behaviour, Alternative Behaviour, Exception Behaviour, Postconditions)
6. Inputs
7. Outputs
8. Data and Event Interaction (Consumed Data, Produced Data, Consumed Events, Produced Events)
9. Composition and Dependencies (Parent, Child Functions, Dependencies, Orchestration)
10. Execution Characteristics
11. Business Alignment (Realized Capabilities, Enabled Processes)
12. Executing Components
13. Non-Functional Characteristics
14. Security and Governance
15. Measurement and Observability (Relevant Metrics, Monitoring Expectations, Evidence Sources)
16. Examples and Use Cases
17. Limitations and Assumptions
18. References
19. Change History

### 4.2 Machine-readable YAML (required fields)

- id (canonical ID, e.g. `dea:information-system-function-identity-verification`)
- type (always `InformationSystemFunction`)
- name
- description
- version
- lifecycle_status (proposed, planned, active, deprecated, retired)
- functional_domain (cross-reference to `taxonomy/functional-domains.yaml`)
- category
- decomposition_level (F1, F2, F3, F4, F5)

### 4.3 Machine-readable YAML (additional fields)

- parent_function
- child_functions
- inputs
- outputs
- execution_characteristics
- functional_owner
- criticality
- references
- metadata

## 5. Identifier convention

Canonical IDs follow `dea:information-system-function-<semantic-name>`. Example: `dea:information-system-function-identity-verification`. Identifiers MUST NOT encode application names, vendor names, technology products, deployment locations or temporary organisational structures (G-12).

## 6. Directory structure

```
entities/
  v1-alpha/
    index.yaml
    domains/
      <domain-slug>/
        index.yaml
        functions/
          <function-id-without-dea-prefix>/
            function.yaml
            README.md
            examples/
              ...
```

## 7. Validation (CI rules)

The validator at `.github/workflows/validate-entities.yml` enforces 14 rules:

1. Every active function has a `function.yaml`.
2. Every active function has a `README.md`.
3. Canonical IDs are unique.
4. Required fields are present.
5. Schema validation against `schemas/entities/information-system-function.v2.json` succeeds.
6. Parent references resolve.
7. Child references resolve.
8. No composition cycles (unless an explicitly governed recursive pattern is permitted).
9. Decomposition levels are valid (F1-F5).
10. Relationship references resolve to the correct entity types (soft check; hard check is in 01D).
11. Documentation and machine-readable identity agree (the README's identity section matches `function.yaml`).
12. Required sections exist in the README.
13. Examples conform to the schema.
14. No deprecated identity is used for new records.

## 8. Relationship to the 5-CR programme

This guide is the third sibling of the 5-CR ISF catalog programme:

- CR-IS-CAT-01 (foundation; merged 2026-10-18)
- CR-IS-CAT-01A (taxonomy; merged 2026-10-18)
- CR-IS-CAT-01B (decomposition and documentation; this guide, the PR that contains it)
- CR-IS-CAT-01C (population; uses this guide to populate the initial inventory)
- CR-IS-CAT-01D (integration; validates cross-catalogue relationships)

The taxonomy (01A) and the decomposition (01B) are separate structures (G-06). The taxonomy classifies functions into domains, categories and subcategories. The decomposition breaks functions into F1-F5 levels. The two hierarchies MUST NOT be conflated.

## 9. References

- `change-requests/CR-IS-CAT-01B-decomposition.md` (the CR doc that establishes this standard)
- `taxonomy/functional-domains.yaml` (the 15-domain taxonomy from 01A)
- `taxonomy/orthogonal-facets.yaml` (the 7 orthogonal facets from 01A)
- `taxonomy/classification-rules.yaml` (the 11 classification rules from 01A)
- `schemas/entities/information-system-function.v2.json` (the v2 schema)
- `templates/function-template.yaml` (the machine-readable record template)
- `templates/README-template.md` (the 19-section README template)
- `entities/v1-alpha/domains/identity-and-access/functions/` (the example records)
