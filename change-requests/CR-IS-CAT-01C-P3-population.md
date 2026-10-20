# CR-IS-CAT-01C-P3: ISF P3 Population (ISF-12..15)

## Status

P3 tranche for `dea-catalog-information-system-functions`. Closes the ISF
catalogue at **15/15 functional domains** with **50 records** (10 F2 + 40 F4).

Unblocked by `CR-IS-CAT-01C-P2H` (P2 authoring hygiene; P2 generator now uses
the canonical F2 record shape; `scripts/_f2_record_helper.py` is the shared
shape source for P2 and P3 generators).

## 1. Coverage closure

| Domain | F2 | F4 | Records |
|---|---|---|---|
| ISF-12 Resource and Capacity Management | 1 | 2 | 3 |
| ISF-13 AI and Intelligent Processing | 1 | 2 | 3 |
| ISF-14 Experience and Interaction | 1 | 2 | 3 |
| ISF-15 Search and Discovery | 1 | 2 | 3 |
| **Total** | **4** | **8** | **12** |

## 2. ISF completion state

| Metric | Before P3 | After P3 |
|---|---:|---:|
| domains populated | 11/15 (73%) | **15/15 (100%)** |
| functions | 38 | **50** |
| cross-cat relationships | 64 | **96** |
| reference-integrity resolved | 231 | **328** |
| reference-integrity forward | 6 | 6 |
| reference-integrity unresolved | 0 | 0 |

## 3. ISF-14 resolves the last ISC forward ref

`ISF-14 Experience and Interaction` admits the function `dea:information-system-function-experience-and-interaction`.
This is the canonical ISF resolution of the ISC-side forward ref
`dea:information-system-function-customer-experience-management` declared in
CR-IS-CAT-02E (ISC-side relationship registry). The canonical ISF id is
`experience-and-interaction`; the ISC-side declaration `customer-experience-management`
remains a forward-ref to be reconciled when the ISC relationship registry is
next updated (target repo: `dea-catalog-system-functions`; CR-IS-CAT-01C-P3).

When CR-IS-CAT-02E is updated to point at the canonical id, **all 6 forward refs
in the ISC side will be resolvable**, leaving the ISC catalogue free of
forward-deferred identifiers except for the targeted ISS / II / data-entity /
metric catalogue admissions (which are forward-declared by named CRs).

## 4. Per-domain F2/F4 inventory

### ISF-12 Resource and Capacity Management
- F2 `dea:information-system-function-resource-and-capacity-management`
  - F4 `capacity-planning` (executes on `observability-platform`, `development-platform`; enables `process-improve-technology-platforms`; realizes `capability-technology-management`)
  - F4 `resource-provisioning` (executes on `development-platform`, `ci-cd-pipeline`; enables `process-operate-technology-platforms`; realizes `capability-technology-enablement`)

### ISF-13 AI and Intelligent Processing
- F2 `dea:information-system-function-ai-and-intelligent-processing`
  - F4 `model-management` (executes on `ai-inference-platform`, `model-registry`)
  - F4 `inference-execution` (executes on `ai-inference-platform`, `model-serving-runtime`)

### ISF-14 Experience and Interaction
- F2 `dea:information-system-function-experience-and-interaction`
  - F4 `interaction-management` (executes on `customer-facing-web-application-platform`, `api-gateway`)
  - F4 `experience-delivery` (executes on `customer-facing-web-application-platform`, `employee-portal-platform`)

### ISF-15 Search and Discovery
- F2 `dea:information-system-function-search-and-discovery`
  - F4 `index-management` (executes on `data-warehouse-platform`, `data-warehouse-catalog`)
  - F4 `query-dispatch` (executes on `data-warehouse-platform`, `data-warehouse-query`)

## 5. Reference integrity (post-P3)

| Bucket | Count |
|---|---:|
| total classified | 334 |
| resolved | 328 |
| forward | 6 |
| unresolved | 0 |

The 97 new resolved references come from the 4 P3 F2 records' composed
business_alignment / executing_components (8 realized_capabilities + 8 enabled_processes
+ 16 executing_components = 32) plus 24 new F4 cross-cat relations (8 executes + 8 enables
+ 8 realizes) plus the 41 new F2/F4 function-record references (P2 helper composes them).

## 6. Files

- **Added**: `scripts/_f2_record_helper.py` (shared F2 record + README helper;
  used by P2 and P3 generators)
- **Added**: `scripts/generate_p3_population.py` (P3 generator; imports the
  shared helper)
- **Added**: 4 new domain directories (ISF-12..15) with 1 F2 + 2 F4 per domain
  (12 records; 28 files including per-domain indexes)
- **Patched**: `entities/v1-alpha/index.yaml` (catalog-level: 15/15 domains, 50 functions)
- **Patched**: `relationships/v1-alpha/relationships.yaml` (32 new P3 relationships)
- **Regenerated**: `docs/is-semantic-architecture/target-id-snapshots.yaml` (50 ISF records)
- **Regenerated**: 5 conformance reports (reference-integrity now 334/328/6/0)

## 7. Governance basis

- G-09 (completeness evidenced, not assumed): ISF P3 closure brings the catalogue
  from 73% to 100% domain coverage with 50 records.
- G-10 (single source of truth): the P3 generator imports the same
  `_f2_record_helper` module as P2.
- EGV-006 (references resolve to valid entities): all P3 cross-cat references
  resolve against vendored target-id snapshots.
- CR-012 (cross-catalogue references resolve to authoritative entities):
  enforced at CI step 8.
- Programme control: evidence before assertion. P3 authored with canonical
  BC / BP / ISC ids from the start (zero rebases needed in P3).
- D-004, D-005, D-006: clean.
- R1, R2: honoured.

## 8. Companion slices (next, not in this CR)

- `CR-IS-CAT-01C-P1H` (P1 authoring hygiene): validator surfaces 4 P1 F2 records
  with shape deficiencies (P1 generator FUNCTIONS dict stubs pre-date the canonical
  shape). Same shape-parity fix as P2H, applied to P1.
- `CR-IS-CAT-03` (ISS 5-CR programme on `dea-catalog-information-system-services`):
  resolves 1 of the 6 remaining forward refs in the ISC registry.
- `CR-IS-CAT-04` (II 5-CR programme on `dea-catalog-integration-interfaces`):
  resolves 4 of the 6 remaining forward refs.
- `CR-013 (dea-governance)`: portfolio-level reference-resolution policy.
