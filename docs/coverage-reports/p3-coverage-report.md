# P3 Coverage and Exclusion Report (CR-IS-CAT-01C-P3)

**Date**: 2026-10-19
**Scope**: P3 domains (ISF-12..15) - closes ISF at 15/15
**Source**: 5-CR programme section 5 + 01C-P3 brief

## 1. Population methodology

CR-IS-CAT-01C-P3 admitted the 4 remaining functional domains per the source
doc section 5 (CR-IS-CAT-01A). The methodology followed P1/P2:
1. Each domain was reviewed against the 15-domain taxonomy.
2. 1 F2 parent + 2 F4 children admitted per domain = 12 records total.
3. Cross-catalogue references (BC / BP / ISC) used canonical ids from the
   start, per CR-IS-CAT-01R rebasing discipline and CR-IS-CAT-01C-P2H
   generator-emitted F2 record shape.

## 2. Population summary

| Domain | F2 | F4 | Total |
|---|---|---|---|
| ISF-12 Resource and Capacity Management | 1 | 2 | 3 |
| ISF-13 AI and Intelligent Processing | 1 | 2 | 3 |
| ISF-14 Experience and Interaction | 1 | 2 | 3 |
| ISF-15 Search and Discovery | 1 | 2 | 3 |
| **Total** | **4** | **8** | **12** |

## 3. Coverage closure

| Metric | Before P3 | After P3 |
|---|---:|---:|
| domains populated | 11/15 (73%) | **15/15 (100%)** |
| functions | 38 | **50** |
| cross-cat relationships | 64 | **96** |
| reference-integrity total | 237 | **334** |
| reference-integrity resolved | 231 | **328** |
| reference-integrity unresolved | 0 | 0 |

## 4. Per-domain composition

### ISF-12 Resource and Capacity Management
- **F2** Resource and Capacity Management (composes child functions).
- **F4** Capacity Planning: produces a capacity plan (compute, storage, integration) over a planning horizon.
- **F4** Resource Provisioning: allocates and provisions a resource per the capacity plan.

### ISF-13 AI and Intelligent Processing
- **F2** AI and Intelligent Processing (composes child functions).
- **F4** Model Management: registers, versions, evaluates, retires ML models.
- **F4** Inference Execution: evaluates a model against input features.

### ISF-14 Experience and Interaction
- **F2** Experience and Interaction (composes child functions).
- **F4** Interaction Management: records a single interaction (page view, click, conversation turn).
- **F4** Experience Delivery: resolves the experience signal and renders the experience.

### ISF-15 Search and Discovery
- **F2** Search and Discovery (composes child functions).
- **F4** Index Management: builds and refreshes an index over a content corpus.
- **F4** Query Dispatch: resolves a query against an index.

## 5. Reference integrity

| Bucket | Count |
|---|---:|
| total | 334 |
| resolved | 328 |
| forward | 6 |
| unresolved | 0 |

## 6. ISC-side impact

ISF-14's `experience-and-interaction` function is the canonical ISF
resolution of the ISC-side forward ref
`dea:information-system-function-customer-experience-management` declared
in CR-IS-CAT-02E. When the ISC relationship registry is next updated to
point at the canonical id, that forward ref will resolve.

## 7. Next slice

- CR-IS-CAT-01C-P1H: P1 authoring hygiene. Validator surfaces 4 P1 F2 records
  with shape deficiencies; same shape-parity fix as P2H, applied to P1.
- CR-IS-CAT-03 ISS 5-CR programme.
- CR-IS-CAT-04 II 5-CR programme.
- CR-013 governance portfolio adoption.
