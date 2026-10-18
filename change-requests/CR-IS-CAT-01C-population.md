# CR-IS-CAT-01C: Initial Information System Function Catalogue Population (P1 priority)

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-01C |
| **Title** | Initial Information System Function Catalogue Population (P1 priority) |
| **Status** | Proposed (this PR) |
| **Type** | Catalogue content establishment (P1 slice) |
| **Repository** | technehub-labs/dea-catalog-information-system-functions (legacy URL: technehub-labs/dea-catalog-system-functions until org-admin transfer) |
| **Parent** | CR-IS-CAT-01 (merged 2026-10-18) |
| **Depends on** | CR-IS-CAT-01 (merged); CR-IS-CAT-01A (merged); CR-IS-CAT-01B (merged 2026-10-18) |
| **Enables** | CR-IS-CAT-01D (integration); CR-IS-CAT-01C-P2 (P2 follow-on); CR-IS-CAT-01C-P3 (P3 follow-on) |
| **Canonical entity** | `dea:InformationSystemFunction` (class alias `ISF`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-18 |

## 1. Executive Summary

This CR establishes the P1 priority slice of the initial Information System Function catalogue population, per the 5-CR ISF catalog programme section 5. The P1 slice covers the 5 foundational domains: ISF-01 Identity and Access, ISF-02 Information and Data Management, ISF-03 Transaction Processing, ISF-04 Workflow and Orchestration, ISF-05 Integration and Interoperability.

The population follows the 5-stage methodology from source doc section 3: functional-domain coverage, function identification (with the 6 semantic distinctiveness tests), semantic normalization, decomposition, and documentation/validation.

The 5-stage methodology and 10-step quality assurance are applied to each candidate function. The result: 20 functions across the 5 P1 domains (5 F2 parents + 15 F4 atomic functions), with 31 functions deferred to follow-on P1 enrichment CRs and 11 functions excluded with documented rationale.

The 15-domain taxonomy from CR-IS-CAT-01A is validated through the P1 population exercise. Per G-09, completeness is evidenced, not assumed; the coverage report (`docs/coverage-reports/p1-coverage-report.md`) documents the deferred and excluded functions.

The PR is a deliberately manageable slice. The P2 (6 domains) and P3 (4 domains) populations are follow-on CRs (CR-IS-CAT-01C-P2 and CR-IS-CAT-01C-P3). The 5-CR programme is the standing template; the user can request more in this PR or defer to follow-on CRs.

## 2. Scope

### 2.1 In scope (this PR)

1. Initial population of 5 P1 priority domains: ISF-01, ISF-02, ISF-03, ISF-04, ISF-05.
2. 20 function records: 5 F2 parents + 15 F4 atomic functions.
3. Per-domain `index.yaml` files.
4. Catalog-level `index.yaml` at `entities/v1-alpha/index.yaml`.
5. The deterministic generator at `scripts/generate_p1_population.py` (source of truth for re-generation).
6. The P1 coverage and exclusion report at `docs/coverage-reports/p1-coverage-report.md`.
7. Updated `change-requests/README.md` with the CR-IS-CAT-01C row.

### 2.2 Out of scope (this PR; follow-on CRs)

1. P2 priority domains (ISF-06 Communication, ISF-07 Content, ISF-08 Analytics, ISF-09 Security, ISF-10 Monitoring, ISF-11 Configuration): CR-IS-CAT-01C-P2.
2. P3 priority domains (ISF-12 Resource, ISF-13 AI, ISF-14 Experience, ISF-15 Search): CR-IS-CAT-01C-P3.
3. P1 enrichment (more F4 records per F2 parent per the deferred list): CR-IS-CAT-01C-enrichment (per-domain or per-domain-group).
4. Cross-catalogue relationships and integration: CR-IS-CAT-01D.
5. The orthogonal-facet classification layer: separate CR (a CR-IS-CAT-01C-orthogonal-facets extension).

## 3. Population Methodology

The 5-stage population methodology from source doc section 3 was applied to the P1 priority domains:

### 3.1 Functional-domain coverage

All 5 P1 domains were reviewed against the 15-domain taxonomy from CR-IS-CAT-01A. The boundaries are established by the 7 DOCTRINE-MECE doctrines (per card #463 on board 23). The P1 domains are the foundational enterprise functions (security, data, transactions, workflow, integration); they correspond to the architectural patterns that every enterprise information system must implement.

### 3.2 Function identification

The candidate function lists from source doc section 4 (62 candidates across the 5 P1 domains) were evaluated against the 6 semantic distinctiveness tests from source doc section 3.2:

1. Does it describe behaviour performed by an information system? PASS for 53 candidates.
2. Does it have a distinct functional responsibility? PASS for 31 candidates.
3. Can its purpose be defined independently of a particular application? PASS for 27 candidates.
4. Can its expected outcome be described? PASS for 24 candidates.
5. Can it be distinguished from a capability, process, service or component? PASS for 22 candidates.
6. Is it sufficiently reusable to warrant canonical catalogue representation? PASS for 20 candidates.

The 20 selected candidates are the canonical functions in this PR. The 31 deferred candidates are documented in section 4 of the coverage report. The 11 excluded candidates are documented with rationale (sub-aspects of F2 parents or platform concerns, not separate canonical functions).

### 3.3 Semantic normalization

The 20 selected candidates were normalized to a single canonical form: canonical ID (`dea:information-system-function-<semantic-name>`), name (sentence case), definition (one-paragraph), responsibility, input/output semantics, decomposition, and classification (functional_domain cross-reference).

Duplicate detection: PASS. The 5 F2 parents and 15 F4 atomics are unique. No semantic duplicates were found.

### 3.4 Decomposition

Each P1 domain has 1 F2 parent and 2-4 F4 atomic functions. The F2 parents record the composite responsibility and the `child_functions` list. The F4 atomics record the atomic responsibility, the `parent_function`, and the `decomposition_rationale` (or a pointer to the F2 parent's rationale).

Not every function requires all 5 decomposition levels. F1 (function family) and F3 (subfunction) are not used in this PR; F1 is optional and the F2 parent serves as the family root; F3 is optional and the F2 -> F4 decomposition is the natural shape. F5 is tied to the ISC relationship and is not used in this PR.

### 3.5 Documentation and validation

Every populated function has:
- A machine-readable record at `entities/v1-alpha/domains/<domain>/functions/<function>/function.yaml` that validates against the v2 ISF schema (`schemas/entities/information-system-function.v2.json`).
- A README at `entities/v1-alpha/domains/<domain>/functions/<function>/README.md` that follows the 19-section template from CR-IS-CAT-01B.
- A `decomposition_rationale` field (or pointer) that explains the decomposition choice.
- Cross-references to taxonomy, business capabilities, business processes, and executing components (cross-catalog relationships are validated by 01D).

## 4. Initial Population (20 functions)

### ISF-01 Identity and Access (5)

- F2 `dea-isf-identity-and-access-management` (from CR-IS-CAT-01B)
- F4 `dea-isf-identity-verification` (from CR-IS-CAT-01B)
- F4 `dea-isf-identity-registration` (this PR)
- F4 `dea-isf-authentication` (this PR)
- F4 `dea-isf-access-policy-evaluation` (this PR)

### ISF-02 Information and Data Management (4)

- F2 `dea-isf-data-management`
- F4 `dea-isf-data-acquisition`
- F4 `dea-isf-data-transformation`
- F4 `dea-isf-data-retrieval`

### ISF-03 Transaction Processing (4)

- F2 `dea-isf-transaction-processing`
- F4 `dea-isf-transaction-initiation`
- F4 `dea-isf-transaction-execution`
- F4 `dea-isf-transaction-reconciliation`

### ISF-04 Workflow and Orchestration (3)

- F2 `dea-isf-workflow-orchestration`
- F4 `dea-isf-workflow-execution`
- F4 `dea-isf-task-routing`

### ISF-05 Integration and Interoperability (4)

- F2 `dea-isf-integration-and-interoperability`
- F4 `dea-isf-api-request-handling`
- F4 `dea-isf-event-publication`
- F4 `dea-isf-interface-validation`

## 5. Coverage and Completeness

Per G-09, the P1 population includes a coverage assessment. The coverage report is at `docs/coverage-reports/p1-coverage-report.md`. Summary:

- 62 candidates evaluated; 20 selected; 31 deferred; 11 excluded.
- Deferred functions are documented for follow-on P1 enrichment CRs.
- Excluded functions are documented with rationale (sub-aspects of F2 parents or platform concerns, not separate canonical functions).
- No claim of exhaustive completeness is made. The P1 population is a baseline; the catalogue may continue to evolve.

The 15-domain taxonomy from CR-IS-CAT-01A is validated through the P1 population exercise. The 7 boundary doctrines (per DOCTRINE-MECE card #463) are applied. The 5 P1 domains are confirmed as foundational; the 10 P2/P3 domains are scheduled for follow-on CRs.

## 6. CI Validation

The CI workflow at `.github/workflows/validate-entities.yml` (from CR-IS-CAT-01B) validates the 20 function records. The local validation (per `python3 -c '...'`) confirms all 20 records pass:
- v2 ISF schema validation
- canonical ID uniqueness
- parent/child references resolve
- bidirectional consistency (if A.parent = B, then B.child_functions includes A)
- no composition cycles
- decomposition level validity (F1-F5)
- README has all 19 sections
- README and function.yaml identity agreement

## 7. Cross-Repository Impact

| Repository | Required alignment |
|---|---|
| `technehub-labs/dea-architecture-framework` | No action; CR-AR-FMWK-04 (v0.7.0) already allocates the entities. |
| `technehub-labs/dea-metamodel` | No action; CR-018 + CR-022 establish the canonical entity and the artifact closure. |
| `technehub-labs/dea-catalog-business-capabilities` | The 20 functions reference `dea:business-capability-*` identifiers; 01D's cross-catalogue check will validate. |
| `technehub-labs/dea-catalog-processes` | The 20 functions reference `dea:business-process-*` identifiers; 01D's cross-catalogue check will validate. |
| `dea-catalog-information-system-components` (CR-IS-CAT-02) | The 20 functions reference `dea:information-system-component-*` identifiers; the cross-catalogue check is owned by 01D. |
| `technehub-labs/dea-governance` | `CR-013 (dea-governance)` registers the 20 functions in the portfolio; the closure gate for the IS programme. |

## 8. Acceptance Criteria

1. All 5 P1 domains have undergone population assessment.
2. Initial functional categories are documented (in the per-domain `index.yaml`).
3. 20 approved function records exist in machine-readable form.
4. Every active record has a 19-section README.
5. Every record conforms to the CR-IS-CAT-01A taxonomy.
6. Every record conforms to the CR-IS-CAT-01B documentation standard.
7. Duplicate identities are eliminated.
8. Decomposition and relationships are validated.
9. Coverage and exclusion reports are published (`docs/coverage-reports/p1-coverage-report.md`).
10. CI passes.
11. No unsupported claim of exhaustive completeness is made.

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Overpopulation with trivial functions | The 6 semantic distinctiveness tests reject candidates that fail the sufficiency test |
| Missing enterprise functions | Coverage analysis per the source doc section 4 candidates (62 in P1) |
| Duplicate concepts | Canonical ID uniqueness check (CI rule 3) and semantic distinctiveness tests |
| Vendor-specific bias | Technology-independent definitions; identifiers MUST NOT encode application names (per CR-IS-CAT-01B section 7) |
| AI terminology becoming transient | Classify behaviour, not product terminology (per source doc section 5, supported by the orthogonal facet 5.7 `automation-characteristics`) |
| False completeness | The coverage report documents deferred and excluded functions; no exhaustive-completeness claim |

## 10. Definition of Done

CR-IS-CAT-01C is complete when:
- 20 function records are published (function.yaml + README.md per function).
- Per-domain and catalog-level indexes are published.
- The deterministic generator is committed.
- The coverage and exclusion report is published.
- CI passes.
- The PR is reviewed and merged.

The P2 and P3 populations are follow-on CRs. The catalogue may continue to evolve after this PR closes.

## 11. References

- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01-information-system-functions-rename.md` (parent; merged)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01A-taxonomy.md` (sibling; merged)
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01B-decomposition.md` (sibling; merged)
- `technehub-labs/dea-catalog-system-functions/taxonomy/functional-domains.yaml` (15 functional domains)
- `technehub-labs/dea-catalog-system-functions/schemas/entities/information-system-function.v2.json` (v2 ISF schema)
- `technehub-labs/dea-catalog-system-functions/scripts/generate_p1_population.py` (deterministic generator)
- `technehub-labs/dea-catalog-system-functions/docs/coverage-reports/p1-coverage-report.md` (P1 coverage and exclusion report)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (5-CR programme source; section 5)
- `~/.hermes/profiles/coder/kanban/cr-is-cat-01-programme-plan-2026-10-18.md` (reconciliation plan)
- `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-18.md` (snapshot)
- DOCTRINE-MECE card #463 on board 23 (7 boundary doctrines for 15-domain taxonomy)

## 12. Standing Rules Acknowledged

The following programme-wide governance rules from CR-IS-CAT-01 §7 apply to 01C and are acknowledged in this PR:

- G-01: `dea:InformationSystemFunction` is the only canonical entity for new catalogue records. (All 20 records have `type: InformationSystemFunction`.)
- G-03: Metamodel definitions remain authoritative in `dea-metamodel`. (The 20 records reference metamodel entities by ID, not by redefinition.)
- G-05: Taxonomy nodes are catalogue classifications, not metamodel entities. (The 20 records reference `isf:domain:*` for classification.)
- G-06: Classification and functional decomposition are separate structures. (The taxonomy is from 01A; the decomposition is from 01B; the population is from 01C.)
- G-07: Every active function has machine-readable content and individual documentation. (All 20 records have function.yaml + README.md.)
- G-08: Every relationship uses an authorized semantic contract. (Soft check in 01B; hard check in 01D.)
- G-09: Catalogue completeness must be evidenced, not assumed. (The coverage report documents deferred and excluded functions.)
- G-11: Metric definitions remain owned by the Metric catalogue. (No metric definitions are introduced in this PR; the `measured_by: [MTR]` allocation is owned by OpenDEAM v0.7.0 and the Metric catalogue.)
- G-12: No implementation-specific function becomes canonical merely because it exists in an application. (Identifiers are semantic, not vendor- or application-specific.)

---

End of CR-IS-CAT-01C.
