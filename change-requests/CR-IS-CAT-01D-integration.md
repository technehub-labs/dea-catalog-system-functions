# CR-IS-CAT-01D: Information System Function Cross-Catalogue Integration and Conformance

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-01D |
| **Title** | Information System Function Cross-Catalogue Integration and Conformance |
| **Status** | Proposed (this PR) |
| **Type** | Semantic integration and conformance |
| **Repository** | technehub-labs/dea-catalog-information-system-functions (legacy URL: technehub-labs/dea-catalog-system-functions until org-admin transfer) |
| **Parent** | CR-IS-CAT-01 (merged 2026-10-18) |
| **Depends on** | CR-IS-CAT-01 (merged); CR-IS-CAT-01A (merged); CR-IS-CAT-01B (merged); CR-IS-CAT-01C (merged 2026-10-18) |
| **Enables** | CR-IS-CAT-02..04 (other catalog cascades); `CR-013 (dea-governance)` (closure gate) |
| **Architectural authority** | dea-metamodel, dea-architecture-framework |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR is the fourth and final sibling of the 5-CR ISF catalog programme. It establishes cross-catalogue integration, relationship validation and conformance requirements for the Information System Function catalogue.

The objective is to ensure that Information System Functions are not treated as isolated catalogue entries. They MUST be connected to the wider OpenDEA architecture through canonical semantic relationships.

The catalogue consumes the established metamodel and OpenDEAM relationship definitions rather than independently inventing relationship semantics. Per G-08 (every relationship uses an authorized semantic contract), the hard check for relationship validity is this CR. Per G-11 (metric definitions remain owned by the Metric catalogue), the `measured_by` integration follows the OpenDEAM v0.7.0 allocation; no new `dea:has-metric` or similar relationship is invented.

This CR also closes the integration and conformance layer for the ISF catalog, enabling the closure gate `CR-013 (dea-governance)`.

## 2. Architectural Integration Principles

### 2.1 Metamodel authority

All relationship types, source/target constraints and semantic definitions MUST originate from the normative metamodel (`dea-metamodel`) and the applicable OpenDEAM allocation (`dea-architecture-framework`). The catalogue MUST NOT redefine these contracts.

### 2.2 Canonical identifiers

All external references MUST use canonical identifiers. Display names and natural-language descriptions MUST NOT replace canonical identifiers in machine-readable relationships.

### 2.3 Referential integrity

Every declared relationship MUST resolve to an existing canonical record or a documented external reference. Unresolved references MUST be reported. The validator at `.github/workflows/validate-catalogue.yml` enforces this.

### 2.4 Relationship directionality

Relationships MUST preserve the direction defined by the metamodel. The catalogue MUST NOT infer inverse relationships unless the relationship contract establishes them. For example, `ISF realizes BC` is the canonical direction (the function realizes the capability); the inverse (`BC is-realized-by ISF`) is the inverse relationship per the metamodel and is NOT separately recorded.

### 2.5 Separation of architectural concerns

The function catalogue owns functional descriptions. It does NOT own:
- Business capability definitions (owned by `dea-catalog-business-capabilities`)
- Business process definitions (owned by `dea-catalog-processes`)
- Component definitions (owned by `dea-catalog-information-system-components` after CR-IS-CAT-02)
- Service definitions (owned by `dea-catalog-information-system-services` after CR-IS-CAT-03)
- Data entity definitions (owned by the Data Entity catalogue)
- Event definitions (owned by the Event catalogue)
- Metric definitions (owned by the Metric catalogue)

Those remain in their respective catalogues. The function catalogue references them by canonical identifier.

## 3. Required Integration Domains

Per source doc section 3 (8 integration domains), the function catalogue MUST support the following relationship domains. Each domain corresponds to one or more metamodel relationships from CR-018/019/020/021.

### 3.1 Business Capability Integration (CR-018)

**Relationship**: `InformationSystemFunction` `realizes` `BusinessCapability` (dea:realizes; category G=governance or B=realization).

**Purpose**: establish which business capabilities are supported through information system behaviour.

**Requirements**:
- A function MAY realize one or more capabilities where semantically justified.
- A capability MAY be realized through multiple information system functions.
- Realization MUST NOT be interpreted as ownership.
- Capability references MUST resolve to the canonical Business Capability catalogue.

### 3.2 Business Process Integration (CR-017/018)

**Relationship**: `InformationSystemFunction` `enables` `BusinessProcess` (dea:enables; category B=realization).

**Purpose**: identify how information system functions enable business processes.

**Requirements**:
- A process MAY use multiple functions.
- A function MAY enable multiple processes.
- The function MUST NOT be substituted for the process.
- Process execution responsibility MUST remain explicit.

### 3.3 Information System Component Integration (CR-018/019)

**Relationship**: `InformationSystemComponent` `executes` `InformationSystemFunction` (dea:executes; category B=realization).

**Purpose**: identify the components responsible for executing functional behaviour.

**Requirements**:
- A function MAY be executed by multiple components.
- A component MAY execute multiple functions.
- Execution allocation MUST distinguish primary and supporting components where applicable.
- Deployment instances MUST NOT be confused with canonical components.

### 3.4 Information System Service Integration (CR-020)

**Relationship**: `InformationSystemComponent` `provides` `InformationSystemService` (dea:provides; category B=realization).

**Purpose**: identify the services provided by components that expose or make available one or more functions.

**Requirements**:
- The catalogue MUST support traceability through the established architecture.
- The catalogue MUST NOT assume that every function is itself a service.
- A function is exposed through a service via a component.

### 3.5 Integration Interface Integration (CR-021)

**Relationship**: `InformationSystemService` `exposes` `IntegrationInterface` (dea:exposes; category B=realization).

**Purpose**: identify the interaction boundaries through which functions are exposed.

**Requirements**:
- Functions may depend on information exchange through integration interfaces.
- The catalogue MUST support traceability to relevant integration interfaces, API contracts, events, and data exchanges.
- The relationship between API and Integration Interface MUST follow the CR-021 `specifies` decision (the new `dea:specifies` relationship, category M=contract).
- A function MUST NOT be directly equated with an API operation.

### 3.6 Data Architecture Integration (CR-017/018)

**Relationships**: `InformationSystemFunction` `consumes` `DataEntity` and `InformationSystemFunction` `produces` `DataEntity` (dea:consumes / dea:produces; category F=information).

**Purpose**: identify the data entities consumed and produced by functional behaviour.

**Requirements**:
- Inputs MUST identify consumed information.
- Outputs MUST identify produced information.
- Data references MUST resolve to canonical Data Entity records.
- Data classification and sensitivity MUST be inherited from the authoritative data definitions where applicable.

### 3.7 Event Integration (CR-017/018)

**Relationships**: `InformationSystemFunction` `consumes` `Event` and `InformationSystemFunction` `produces` `Event` (dea:consumes / dea:produces; category F=information).

**Purpose**: identify the events consumed and produced by functional behaviour.

**Requirements**:
- Event references MUST resolve to canonical Event records.
- Triggering and produced-event semantics MUST be distinguishable.
- Event-driven execution MUST be documented.

### 3.8 Measurement Integration (OpenDEAM v0.7.0)

**Allocation**: OpenDEAM v0.7.0 already allocates `measured_by: [MTR]` to `dea:entity-information-system-function`.

**Purpose**: connect functions to the Metric catalogue through the established measurement model.

**Requirements**:
- The Metric catalogue remains the authoritative source of metric definitions.
- The function catalogue supports references to metrics measuring relevant characteristics (execution frequency, processing latency, throughput, success rate, error rate, availability, resource utilization, functional completion, quality of outputs).
- The following distinctions MUST be preserved: a metric defines what is measured; a measurement is an observation or result obtained through measurement; a function is the subject or object of architectural measurement; a target or threshold is a governed expectation, not a measurement itself.
- A metric reference MUST NOT be converted into an invented direct relationship if the existing OpenDEAM measurement allocation or metamodel does not support it.
- Where a relationship is not yet expressible through the current metamodel, the catalogue MUST record the integration gap and raise a separate metamodel/framework CR.

## 4. Cross-Catalogue Relationship Matrix

Per source doc section 4, the function catalogue's relationships to other catalogues are:

| Source | Relationship | Target | Authority |
|---|---|---|---|
| InformationSystemFunction | realizes | BusinessCapability | CR-018 |
| InformationSystemFunction | enables | BusinessProcess | CR-017/018 |
| InformationSystemComponent | executes | InformationSystemFunction | CR-018/019 |
| InformationSystemComponent | provides | InformationSystemService | CR-020 |
| InformationSystemService | exposes | IntegrationInterface | CR-021 |
| InformationSystemFunction | consumes | DataEntity | CR-017/018 |
| InformationSystemFunction | produces | DataEntity | CR-017/018 |
| InformationSystemFunction | consumes | Event | CR-017/018 |
| InformationSystemFunction | produces | Event | CR-017/018 |
| InformationSystemFunction | measured_by | Metric | OpenDEAM v0.7.0 |

The final row is an OpenDEAM allocation declaration, NOT a claim that `measured_by` is necessarily a metamodel relationship of the same name. The implementation MUST preserve this distinction. Per G-11, metric definitions remain owned by the Metric catalogue; the function catalogue references them through the established allocation.

## 5. Integration Record Structure

The integration record file is at `relationships/v1-alpha/relationships.yaml`. Each relationship record includes:

- Stable relationship record ID (e.g., `rel:isf-realizes-identity-assurance`)
- Source entity ID
- Relationship type (cross-referenced to the metamodel's relationship vocabulary)
- Target entity ID
- Relationship description
- Provenance
- Validity status
- Effective version
- Evidence or reference
- Relationship-specific metadata (where permitted)

The catalogue MUST use registered relationship semantics. It MUST NOT create a competing relationship vocabulary.

## 6. Cross-Repository Integration

The following catalogues are the expected integration partners:

| Repository | Integration responsibility |
|---|---|
| `dea-catalog-business-capabilities` | Business outcomes and capabilities (realized by functions) |
| `dea-catalog-processes` | Business process enablement (enabled by functions) |
| `dea-catalog-information-system-components` (CR-IS-CAT-02) | Function execution (executes functions) |
| `dea-catalog-information-system-services` (CR-IS-CAT-03) | Service exposure and consumption (exposes integration interfaces) |
| `dea-catalog-information-system-integration-interfaces` (CR-IS-CAT-04) | Interaction boundaries (exposed by services) |
| Data Entity catalogue | Data consumption and production (consumed/produced by functions) |
| Event catalogue | Event consumption and production (consumed/produced by functions) |
| Metric catalogue | Measurement definitions and observations (measured_by) |

Repository names and entity identities MUST be verified against their authoritative allocations before implementing individual connectors or reference validators. The validator in this PR uses the OpenDEAM v0.7.0 identifier map (`docs/is-semantic-architecture/opendeam-identifier-map.yaml`) as the canonical cross-reference.

## 7. Conformance Architecture

The repository implements conformance checks at 4 levels.

### 7.1 Structural conformance

- YAML and JSON syntax.
- Required properties.
- Schema validation.
- Canonical identifier format.
- Version format.
- Directory and index consistency.

### 7.2 Semantic conformance

- Correct entity type.
- Valid taxonomy references.
- Valid decomposition.
- Correct relationship direction.
- Correct source/target types.
- No invalid semantic substitutions.

### 7.3 Cross-catalogue conformance

- External references resolve.
- Deprecated identities are handled correctly.
- Relationship endpoints exist.
- Metric references use the canonical metric identity (per the OpenDEAM v0.7.0 `measured_by: [MTR]` allocation).
- Missing external catalogues are distinguished from invalid records.

### 7.4 Governance conformance

- Ownership and stewardship metadata.
- Lifecycle transitions.
- Version history.
- Provenance.
- Deprecation and supersession records.
- Change approval and review.

## 8. CI/CD Requirements

The CI workflow is at `.github/workflows/validate-catalogue.yml`. The workflow executes:

1. YAML and JSON parsing.
2. Schema validation (against the v2 ISF schema and the relationship record schema).
3. Catalogue index generation and verification.
4. Taxonomy validation (per CR-IS-CAT-01A's validator).
5. Function identity validation (per CR-IS-CAT-01B's validator).
6. Decomposition integrity validation (per CR-IS-CAT-01B's validator).
7. Relationship endpoint validation (the hard check; complements the soft check in 01B).
8. Cross-catalogue reference validation (against the OpenDEAM v0.7.0 identifier map).
9. Measurement reference validation (the `measured_by: [MTR]` allocation is checked; no competing relationship).
10. Documentation completeness checks (per CR-IS-CAT-01B's validator).
11. Duplicate detection.
12. Legacy identifier validation.
13. Lifecycle validation.
14. Generated artefact consistency checks.

Where a dependency repository is unavailable, CI MUST distinguish unavailable external validation from invalid local records. External repositories MUST NOT be silently treated as valid simply because they cannot be accessed.

## 9. Integration and Conformance Reporting

The following reports are generated at `reports/`:

- `catalogue-conformance.yaml` (overall conformance summary)
- `relationship-coverage.yaml` (per-relationship coverage)
- `reference-integrity.yaml` (per-entity reference integrity)
- `taxonomy-coverage.yaml` (per-taxonomy coverage)
- `documentation-coverage.yaml` (per-function documentation coverage)

Reports identify:
- Total active functions.
- Functions by domain.
- Functions by decomposition level.
- Missing documentation.
- Unresolved relationships.
- Deprecated references.
- Missing measurement references where required by applicable policy.
- Cross-catalogue integration coverage.
- Excluded and deferred records.

Generated reports MUST be reproducible. The report generator is at `scripts/generate_conformance_reports.py`.

## 10. Repository Deliverables (this PR)

- `relationships/v1-alpha/relationships.yaml` (new; the relationship registry)
- `schemas/relationships/relationship-record.schema.json` (new; JSON Schema for relationship records)
- `.github/workflows/validate-catalogue.yml` (new; the 14-step CI validator)
- `scripts/generate_conformance_reports.py` (new; the report generator)
- `reports/catalogue-conformance.yaml` (new; generated)
- `reports/relationship-coverage.yaml` (new; generated)
- `reports/reference-integrity.yaml` (new; generated)
- `reports/taxonomy-coverage.yaml` (new; generated)
- `reports/documentation-coverage.yaml` (new; generated)
- `change-requests/CR-IS-CAT-01D-integration.md` (this file)
- `change-requests/README.md` (updated with 01D row)

## 11. Acceptance Criteria

1. The catalogue uses canonical metamodel entity identity.
2. Relationship semantics match the normative metamodel.
3. Business capability integration is validated (realizes).
4. Business process integration is validated (enables).
5. Component execution references are validated (ISC executes ISF).
6. Service and interface references are supported (ISC provides ISS; ISS exposes IF).
7. Data and event references are supported (ISF consumes/produces DataEntity/Event).
8. Metric integration follows the existing OpenDEAM measurement allocation (measured_by:[MTR]).
9. Invalid endpoint types fail validation.
10. Unresolved external references are reported (not silently treated as valid).
11. Conformance reports are generated.
12. CI is operational.
13. Legacy identities remain traceable.
14. No new metamodel relationship is introduced without a separate authorized change.

## 12. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Relationship semantics drift | Consume normative metamodel contracts (per source doc section 2.1) |
| Circular or contradictory relationships | Validate graph integrity (per source doc section 3.1) |
| External repositories unavailable | Distinguish unavailable from invalid (per source doc section 8) |
| Metric and measurement confusion | Preserve separate semantic definitions (per source doc section 3.8) |
| API/function conflation | Maintain explicit entity boundaries (per source doc section 3.5) |
| Cross-catalogue identifier drift | Canonical identifier validation (per source doc section 2.2) |
| Excessive CI dependencies | Local mandatory checks and controlled external checks (per source doc section 8) |

## 13. Definition of Done

CR-IS-CAT-01D is complete when:
- The Information System Function catalogue is integrated with its relevant architectural catalogues.
- Relationship and measurement references are validated.
- Conformance reporting is available at `reports/`.
- CI reliably enforces the agreed contracts.
- The 5-CR ISF programme is complete.

The 5-CR programme is the template; the remaining Path Y work is the cascade of the same template to CR-IS-CAT-02 (APC rename), CR-IS-CAT-03 (ISS new), CR-IS-CAT-04 (II new), and the `CR-013 (dea-governance)` closure gate.

## 14. References

- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01-information-system-functions-rename.md` (parent)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01A-taxonomy.md` (sibling)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01B-decomposition.md` (sibling)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01C-population.md` (sibling)
- `technehub-labs/dea-metamodel/change-requests/CR-018-information-system-function.md` (the canonical entity; the `realizes` relationship)
- `technehub-labs/dea-metamodel/change-requests/CR-019-information-system-component.md` (the `executes` relationship)
- `technehub-labs/dea-metamodel/change-requests/CR-020-information-system-service.md` (the `provides` relationship)
- `technehub-labs/dea-metamodel/change-requests/CR-021-integration-interface.md` (the `exposes` and `specifies` relationships)
- `technehub-labs/dea-architecture-framework/model/opendeam-model.yaml` (v0.7.0; the `measured_by: [MTR]` allocation)
- `technehub-labs/dea-architecture-framework/docs/is-semantic-architecture/opendeam-identifier-map.yaml` (the canonical cross-reference)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme; source doc section 6)

## 15. Standing Rules Acknowledged

The following programme-wide governance rules from CR-IS-CAT-01 §7 apply to 01D and are acknowledged in this PR:

- G-01: `dea:InformationSystemFunction` is the only canonical entity.
- G-03: Metamodel definitions remain authoritative.
- G-05: Taxonomy nodes are catalogue classifications, not metamodel entities.
- G-06: Classification and functional decomposition are separate structures.
- G-07: Every active function has machine-readable content and individual documentation.
- G-08: Every relationship uses an authorized semantic contract. (HARD check in this CR.)
- G-09: Catalogue completeness must be evidenced, not assumed.
- G-10: All generated artefacts must be reproducible and validated. (The conformance reports are reproducible; the generator is deterministic.)
- G-11: Metric definitions remain owned by the Metric catalogue. (The `measured_by` integration follows the OpenDEAM v0.7.0 allocation.)
- G-12: No implementation-specific function becomes canonical.

---

End of CR-IS-CAT-01D.
