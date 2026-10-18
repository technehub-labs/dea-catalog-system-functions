# Taxonomy :  Information System Function Classification

This directory holds the catalogue-level classification architecture for the Information System Function (ISF) catalogue.

The taxonomy is NOT a new metamodel entity hierarchy. It is a catalogue-level classification system that classifies instances of `dea:InformationSystemFunction` across functional domains, categories, subcategories and orthogonal classification facets. Per G-05 (programme-wide governance, source doc section 7), taxonomy nodes are catalogue classifications, not metamodel entities. Per G-06, classification and functional decomposition are separate structures; this directory is classification; CR-IS-CAT-01B (decomposition) is a sibling concern.

## Files

| File | Purpose |
|---|---|
| `functional-domains.yaml` | The 15 initial top-level functional domains (ISF-01..ISF-15) with normative definitions, scope, inclusion criteria and exclusion criteria |
| `orthogonal-facets.yaml` | The 7 orthogonal classification facets (functional nature, interaction pattern, execution characteristics, functional criticality, processing characteristics, information characteristics, automation characteristics) |
| `classification-rules.yaml` | The 11 classification rules that govern how functions are classified |

The `function-categories.yaml` file is owned by CR-IS-CAT-01B (decomposition and documentation standard). It is created in 01B and populated incrementally as the decomposition model is established.

## The 15 functional domains

| Code | Domain | Scope summary |
|---|---|---|
| ISF-01 | Identity and Access | Identity lifecycle, authentication, authorization, access enforcement |
| ISF-02 | Information and Data Management | Structured data lifecycle (typed, queryable, transactional) |
| ISF-03 | Transaction Processing | Transaction initiation, validation, execution, settlement, posting, reconciliation |
| ISF-04 | Workflow and Orchestration | Work coordination, sequencing, routing, scheduling, process execution |
| ISF-05 | Integration and Interoperability | Technical integration: API, protocol, message, event |
| ISF-06 | Communication and Collaboration | Human messaging, notifications, communication sessions, collaborative interaction |
| ISF-07 | Content and Knowledge Management | Unstructured/semi-structured content lifecycle, knowledge extraction, search indexing of content |
| ISF-08 | Analytics and Decision Support | Analytical computation: aggregation, statistics, forecasting, decision support |
| ISF-09 | Security, Privacy and Trust | Security infrastructure: cryptographic processing, threat detection, privacy controls, trust management |
| ISF-10 | Monitoring and Observability | Read-only observation: telemetry, logging, tracing, alerting, diagnostics |
| ISF-11 | Configuration and Administration | Mutating control: configuration management, system administration, provisioning |
| ISF-12 | Resource and Capacity Management | Resource allocation, capacity management, optimization, utilization |
| ISF-13 | AI and Intelligent Processing | AI-native behaviours: model inference, agent task planning, reasoning, agent tool invocation |
| ISF-14 | Experience and Interaction | User interaction, presentation, personalization, interaction management |
| ISF-15 | Search and Discovery | Retrieval and ranking: indexing, search execution, matching, discovery |

## Doctrine on overlapping domains

The 15 domains are NOT strictly MECE. Known overlaps and the boundaries that resolve them (per DOCTRINE-MECE card #463 on board 23):

1. **ISF-01 vs ISF-09**: identity lifecycle vs security infrastructure. The boundary is the actor (identity) vs the protection mechanism (security).
2. **ISF-02 vs ISF-07**: structured data vs unstructured content. The boundary is data shape, not retrieval.
3. **ISF-04 vs ISF-12**: work coordination vs resource allocation. The boundary is work-level vs resource-level.
4. **ISF-05 vs ISF-04 vs ISF-06**: technical integration vs business coordination vs human communication. The boundary is the layer of coordination.
5. **ISF-08 vs ISF-15**: analytical computation vs retrieval/ranking. The boundary is computational vs retrieval.
6. **ISF-10 vs ISF-11**: read-only observation vs mutating control. The boundary is read vs write.
7. **ISF-13 vs all other domains**: AI-native behaviours vs AI-assisted versions of other functions. AI-assisted versions route through the orthogonal facet "automation characteristics" (5.7) with values `AI-assisted` or `agent-orchestrated`.

The 01C population exercise is the validation step. Gaps and overlaps discovered during 01C are recorded in the coverage report and trigger a taxonomy refinement CR.

## Cross-cutting concerns and orthogonal facets

Cross-cutting concerns (technology, AI assistance, interaction pattern, criticality, processing mode, information type, automation mode) are NOT functional domains. They are orthogonal facets. A function MAY have multiple orthogonal facet values; a function MUST have exactly one primary functional-domain assignment.

## Identifier convention

Taxonomy identifiers follow `isf:<type>:<slug>` where `<type>` is `domain`, `category`, `subcategory`, or `facet`, and `<slug>` is the kebab-case name. Example: `isf:domain:identity-and-access`.

## Validation

CI validates the taxonomy at `.github/workflows/validate-taxonomy.yml`. The validation checks:
- YAML syntax
- Unique identifiers
- Valid parent references
- No circular hierarchy
- Valid status and lifecycle values
- Valid function-domain assignments
- No orphaned references
- Stable identifier and migration rules
- Valid inclusion/exclusion metadata

## References

- CR-IS-CAT-01A (this CR): `change-requests/CR-IS-CAT-01A-taxonomy.md`
- Parent CR-IS-CAT-01: `change-requests/CR-IS-CAT-01-information-system-functions-rename.md` (merged 2026-10-18)
- 5-CR programme source doc: `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md`
- Reconciliation plan: `~/.hermes/profiles/coder/kanban/cr-is-cat-01-programme-plan-2026-10-18.md`
- Snapshot: `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-18.md`
