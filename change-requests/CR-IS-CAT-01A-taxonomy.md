# CR-IS-CAT-01A: Information System Function Taxonomy and Classification Architecture

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-01A |
| **Title** | Information System Function Taxonomy and Classification Architecture |
| **Status** | Proposed (this PR) |
| **Type** | Catalogue taxonomy and classification |
| **Repository** | technehub-labs/dea-catalog-information-system-functions (legacy URL: technehub-labs/dea-catalog-system-functions until org-admin transfer) |
| **Parent** | CR-IS-CAT-01 (merged 2026-10-18 via PR #2, commit `4358a32`) |
| **Depends on** | CR-IS-CAT-01 |
| **Enables** | CR-IS-CAT-01B (documentation); CR-IS-CAT-01C (population); CR-IS-CAT-01D (integration) |
| **Canonical entity** | `dea:InformationSystemFunction` (class alias `ISF`; OpenDEAM-local `dea:entity-information-system-function`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR establishes the functional taxonomy and classification architecture for the Information System Function catalogue. The taxonomy is the catalogue-level content that classifies `dea:InformationSystemFunction` instances across functional domains, categories, subcategories and orthogonal classification facets.

The taxonomy is NOT a new metamodel entity hierarchy. It is a catalogue-level classification system. Per G-05, taxonomy nodes are catalogue classifications, not metamodel entities. Per G-06, classification and functional decomposition are separate structures. Per G-09, catalogue completeness must be evidenced, not assumed; the 01C population exercise is the validation step.

The 15 functional domains are a starting baseline. The DOCTRINE-MECE review (card #463 on board 23) establishes the boundaries between overlapping domains; cross-cutting concerns route through orthogonal facets.

## 2. Classification Principles

### 2.1 Function vs capability

A function describes behaviour performed by an information system. A capability describes an ability to achieve an outcome. The taxonomy classifies the former, not the latter. Functions and capabilities are related through the `dea:InformationSystemFunction realizes dea:BusinessCapability` relationship, not through the taxonomy.

### 2.2 Function vs application

An application is not a functional domain. An application may execute multiple functions, and a function may be executed by multiple components. Functional classification is independent of application ownership.

### 2.3 Functional classification vs technology classification

A function MUST NOT be classified primarily by its implementation technology. For example, identity verification remains an identity function whether implemented through a conventional application, an API, an AI model or a distributed architecture. Implementation technology is captured through the orthogonal facet "execution characteristics" (5.3).

### 2.4 Multi-dimensional classification

A function MUST have exactly one primary functional-domain assignment. It MAY have multiple additional classifications where justified. The primary classification supports catalogue navigation; orthogonal facets support analysis and discovery. G-06 governs the separation between classification and decomposition.

### 2.5 Taxonomy stability

The functional-domain structure SHOULD remain relatively stable. New technology patterns, implementation methods and emerging practices SHOULD normally be expressed through orthogonal classification facets rather than constant restructuring of the functional taxonomy.

## 3. Functional Domain Taxonomy

The initial top-level functional domains are:

| Code | Functional domain | Scope |
|---|---|---|
| ISF-01 | Identity and Access | Identification, authentication, authorization, identity lifecycle and access enforcement |
| ISF-02 | Information and Data Management | Data acquisition, validation, transformation, storage, retrieval, retention and disposal |
| ISF-03 | Transaction Processing | Transaction initiation, validation, execution, settlement, posting and reconciliation |
| ISF-04 | Workflow and Orchestration | Work coordination, sequencing, routing, scheduling and process execution |
| ISF-05 | Integration and Interoperability | API interaction, protocol mediation, message exchange, event distribution and transformation |
| ISF-06 | Communication and Collaboration | Messaging, notifications, communication sessions and collaborative interaction |
| ISF-07 | Content and Knowledge Management | Content lifecycle, document management, search, knowledge retrieval and management |
| ISF-08 | Analytics and Decision Support | Reporting, analytical processing, forecasting, decision support and insight generation |
| ISF-09 | Security, Privacy and Trust | Security enforcement, cryptographic operations, privacy controls, threat detection and trust management |
| ISF-10 | Monitoring and Observability | Monitoring, telemetry collection, logging, tracing, diagnostics and alerting |
| ISF-11 | Configuration and Administration | Configuration management, system administration, provisioning and operational control |
| ISF-12 | Resource and Capacity Management | Resource allocation, capacity management, optimization and utilization |
| ISF-13 | AI and Intelligent Processing | Model inference, intelligent classification, recommendation, reasoning and agentic execution |
| ISF-14 | Experience and Interaction | User interaction, presentation, personalization and interaction management |
| ISF-15 | Search and Discovery | Search execution, indexing, discovery, matching and retrieval |

### 3.1 Doctrine on overlapping domains (per DOCTRINE-MECE card #463)

The 15 domains are NOT strictly MECE. Known overlaps and the boundaries that resolve them:

1. **ISF-01 (Identity and Access) vs ISF-09 (Security, Privacy and Trust)**: ISF-01 = identity lifecycle; ISF-09 = security infrastructure. Boundary: actor vs protection mechanism.
2. **ISF-02 (Information and Data Management) vs ISF-07 (Content and Knowledge Management)**: ISF-02 = structured data lifecycle; ISF-07 = unstructured/semi-structured content. Boundary: structured vs content.
3. **ISF-04 (Workflow and Orchestration) vs ISF-12 (Resource and Capacity Management)**: ISF-04 = work coordination; ISF-12 = resource allocation. Boundary: work-level vs resource-level.
4. **ISF-05 (Integration and Interoperability) vs ISF-04 (Workflow and Orchestration) vs ISF-06 (Communication and Collaboration)**: ISF-05 = technical integration; ISF-04 = business coordination; ISF-06 = human communication. Boundary: technical vs business vs human.
5. **ISF-08 (Analytics and Decision Support) vs ISF-15 (Search and Discovery)**: ISF-08 = analytical computation; ISF-15 = retrieval and ranking. Boundary: computational vs retrieval.
6. **ISF-10 (Monitoring and Observability) vs ISF-11 (Configuration and Administration)**: ISF-10 = read-only observation; ISF-11 = mutating control. Boundary: read vs write.
7. **ISF-13 (AI and Intelligent Processing) vs all other domains**: ISF-13 = AI-native behaviours; AI-assisted versions of other functions route through the orthogonal facet "automation characteristics" (5.7). Boundary: primary behaviour is AI-native vs AI-assisted.

The 01C population exercise validates these boundaries. Gaps and overlaps discovered during 01C are recorded in the coverage report and trigger a taxonomy refinement CR.

## 4. Classification Hierarchy

Each functional domain MAY contain:
- Functional categories
- Functional subcategories
- More specific functional classifications

The hierarchy is:

```
Functional Domain
  -> Functional Category
  -> Functional Subcategory
  -> Information System Function (instance)
```

A taxonomy node is a classification value, NOT an `dea:InformationSystemFunction` entity. The hierarchy MUST NOT be mistaken for function decomposition. Classification groups concepts; decomposition (F0-F5 in CR-IS-CAT-01B) establishes behavioural composition.

## 5. Orthogonal Classification Facets

Every catalogue record SHOULD support the following facets where applicable.

### 5.1 Functional nature

Examples: processing, transformation, validation, coordination, orchestration, retrieval, communication, analysis, monitoring, enforcement, generation.

### 5.2 Interaction pattern

Examples: synchronous request/response, asynchronous messaging, event-driven, batch, streaming, scheduled, human-initiated, agent-initiated.

### 5.3 Execution characteristics

Examples: deterministic, rule-based, statistical, model-based, AI-assisted, agentic, human-in-the-loop.

### 5.4 Functional criticality

Examples: mission-critical, business-critical, operationally significant, supporting, convenience.

Criticality is contextual and MUST NOT be treated as an intrinsic universal characteristic of the function. Per-record criticality is captured in the function record, not in the taxonomy.

### 5.5 Processing characteristics

Examples: real-time, near-real-time, eventual, periodic, on-demand, continuous.

### 5.6 Information characteristics

Examples: structured information, semi-structured information, unstructured information, transactional information, analytical information, sensitive information.

### 5.7 Automation characteristics

Examples: manual initiation, human-assisted, rule-automated, fully automated, AI-assisted, agent-orchestrated.

This facet is the answer to the ISF-13 vs all-domains overlap: an AI-assisted function (e.g., an AI-assisted identity verification) is classified under ISF-01 with the "automation characteristics" facet set to "AI-assisted"; it is NOT classified under ISF-13 unless the function's primary behaviour is AI-native (model inference, agent task planning).

## 6. Taxonomy Data Model

### 6.1 Files created

- `taxonomy/README.md` (this directory's purpose)
- `taxonomy/functional-domains.yaml` (the 15 functional domains)
- `taxonomy/function-categories.yaml` (categories and subcategories; populated incrementally as 01C proceeds)
- `taxonomy/classification-rules.yaml` (the 11 rules from section 7)
- `taxonomy/orthogonal-facets.yaml` (the 7 facets from section 5)
- `schemas/taxonomy.schema.json` (JSON Schema for taxonomy records)

### 6.2 Required fields per taxonomy record

Each taxonomy record MUST include:
- Stable identifier (e.g., `isf:domain:identity-and-access` for ISF-01)
- Name
- Definition
- Parent identifier (where applicable)
- Status (proposed, active, deprecated)
- Version
- Effective date
- Synonyms (where applicable)
- Inclusion criteria
- Exclusion criteria
- Related taxonomy references
- Change history

Taxonomy identifiers MUST remain stable across definition refinements. Renaming or restructuring MUST use a documented migration rather than identifier reuse.

## 7. Classification Rules

1. Every active function MUST have exactly one primary functional-domain assignment.
2. Additional domain associations MUST be explicitly justified.
3. Classification MUST be based on the behaviour performed.
4. Implementation technology MUST NOT determine functional identity.
5. Application ownership MUST NOT determine functional classification.
6. A function MUST NOT be classified as a business capability (per the semantic boundary in CR-IS-CAT-01B §2).
7. Classification nodes MUST NOT be registered as metamodel entities (G-05).
8. Deprecated taxonomy values MUST remain traceable.
9. No taxonomy node may have itself as an ancestor.
10. Circular taxonomy hierarchies MUST be rejected.
11. Classification assignments MUST reference registered taxonomy identifiers.

## 8. Repository Deliverables (this PR)

- `taxonomy/README.md` (new)
- `taxonomy/functional-domains.yaml` (new; 15 functional domains)
- `taxonomy/orthogonal-facets.yaml` (new; 7 facets)
- `taxonomy/classification-rules.yaml` (new; 11 rules)
- `schemas/taxonomy.schema.json` (new; JSON Schema for taxonomy records)
- `change-requests/CR-IS-CAT-01A-taxonomy.md` (this file)
- `change-requests/README.md` (updated with CR-IS-CAT-01A row)

The following are owned by 01B and are out of scope of 01A:
- `function-categories.yaml` (populated by 01B as part of the decomposition model)

## 9. CI Requirements

CI MUST validate:
- Taxonomy YAML syntax
- Unique taxonomy identifiers
- Valid parent references
- No circular hierarchy
- Valid status and lifecycle values
- Valid function-domain assignments
- No orphaned taxonomy references
- Stable identifier and migration rules
- Valid inclusion/exclusion metadata

The validation is implemented via a new workflow at `.github/workflows/validate-taxonomy.yml`. The workflow uses the existing reusable `validate-against-model.yml@v0.7.0` for the allocation check; the new taxonomy validation is a local step in the same workflow.

## 10. Acceptance Criteria

1. All 15 initial functional domains are represented in `functional-domains.yaml`.
2. Each domain has a normative definition, scope, inclusion criteria, and exclusion criteria.
3. All 7 orthogonal facets are defined in `orthogonal-facets.yaml`.
4. The 11 classification rules are documented in `classification-rules.yaml`.
5. The taxonomy JSON Schema validates.
6. Duplicate and circular identifiers are rejected by the CI validator.
7. Taxonomy is independent of the metamodel entity hierarchy (no taxonomy node is a metamodel entity).
8. DOCTRINE-MECE boundaries are documented in the taxonomy README.
9. The 01B (documentation) and 01C (population) CRs can use the taxonomy.
10. CI passes.

## 11. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Overly broad domains | Inclusion and exclusion criteria for each domain; per-record criticality; per-record technology neutralization |
| Overly granular taxonomy | Fine-grained classification at subcategory level; subcategories are populated in 01B, not in 01A |
| Technology-driven classification | Classification is based on functional behaviour; technology is captured through the orthogonal facet "execution characteristics" (5.3) |
| Artificial MECE claims | The 15-domain baseline is explicitly NOT MECE; cross-cutting concerns route through orthogonal facets; 01C population exercise validates boundaries |
| Taxonomy proliferation | Governance of additions and changes is recorded in section 7; per-rule change requires a documented migration |
| Confusion with decomposition | Per G-06, classification and decomposition are separate structures; 01A establishes classification, 01B establishes decomposition |

## 12. Definition of Done

The taxonomy is complete when functional domains and classification facets are documented, machine-readable, validated and usable for consistent classification of the initial Information System Function catalogue. Per G-09, completeness is evidenced by the 01C population exercise; a populated domain is NOT automatically considered complete.

## 13. References

- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01-information-system-functions-rename.md` (parent CR; merged 2026-10-18 via PR #2, commit `4358a32`)
- `technehub-labs/dea-metamodel/change-requests/CR-018-information-system-function.md` (the canonical entity; merged 2026-10-16 via PR #171, commit `0f16441`)
- `technehub-labs/dea-architecture-framework/change-requests/CR-AR-FMWK-04-information-system-entity-allocation.md` (OpenDEAM extension; merged 2026-10-16 via PR #17, commit `1063aa3`)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme; saved 2026-10-18)
- `~/.hermes/profiles/coder/kanban/cr-is-cat-01-programme-plan-2026-10-18.md` (the reconciliation plan)
- `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-18.md` (snapshot)
- Kanban card #459 (CR-IS-CAT-01A), #460 (01B), #461 (01C), #462 (01D), #463 (DOCTRINE-MECE)

## 14. Standing Rules Acknowledged

The following programme-wide governance rules from CR-IS-CAT-01 §7 apply to 01A and are acknowledged in this PR:

- G-01: `dea:InformationSystemFunction` is the only canonical entity for new catalogue records.
- G-03: Metamodel definitions remain authoritative in `dea-metamodel`.
- G-05: Taxonomy nodes are catalogue classifications, not metamodel entities.
- G-06: Classification and functional decomposition are separate structures.
- G-08: Every relationship uses an authorized semantic contract.
- G-09: Catalogue completeness must be evidenced, not assumed.
- G-12: No implementation-specific function becomes canonical merely because it exists in an application.

---

End of CR-IS-CAT-01A.
