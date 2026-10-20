# CR-IS-CAT-01C-P2: ISF P2 Population (ISF-06..11)

## Status

P2 tranche for the `dea-catalog-information-system-functions` catalogue. Adds
6 new functional domains (ISF-06..11) covering communications, content, analytics,
security, observability and configuration.

Unblocked by `CR-IS-CAT-01R` (cross-catalogue reference integrity remediation).
Authored with **canonical** BC / BP / ISC ids from the start; no rebases needed.

## 1. New domains (6)

| Code | Domain | F2 | F4 | Total |
|---|---|---|---|---|
| ISF-06 | Communication and Collaboration | 1 | 2 | 3 |
| ISF-07 | Content and Knowledge Management | 1 | 2 | 3 |
| ISF-08 | Analytics and Decision Support | 1 | 2 | 3 |
| ISF-09 | Security, Privacy and Trust | 1 | 2 | 3 |
| ISF-10 | Monitoring and Observability | 1 | 2 | 3 |
| ISF-11 | Configuration and Administration | 1 | 2 | 3 |
| **Total** | | 6 | 12 | **18** |

## 2. Population methodology

`scripts/generate_p2_population.py` is a focused generator that imports the
helpers from `scripts/generate_p1_population.py` (per G-10: single source of
truth for the YAML/README shape). The 18 records are deterministic: every
record carries its domain code, inputs/outputs templates, canonical cross-cat
references, and decomposition rationale.

## 3. Reference-integrity (post-P2)

| Bucket | Count |
|---|---:|
| total | 206 |
| resolved | 200 |
| forward | 6 |
| unresolved | 0 |

The validator (CR-IS-CAT-01R hardened) resolves against vendored target-id
snapshots in `docs/is-semantic-architecture/target-id-snapshots.yaml`.
Forward refs are the same 6 declared in 01R (data-entity / event / ISS / II
/ metric); none added in P2 because P2 records all reference canonical ids
that already exist in the target catalogues.

## 4. Files

- **Added**: 6 ISF-06..11 domain directories with 1 F2 + 2 F4 per domain (each F4 has `function.yaml` + `README.md`) = 36 files.
- **Added**: `scripts/generate_p2_population.py` (deterministic generator; imports p1 helpers).
- **Patched**: `entities/v1-alpha/index.yaml` (catalog-level: 11/15 domains, 38 functions).
- **Patched**: `relationships/v1-alpha/relationships.yaml` (48 new P2 relationships: 24 executes + 12 enables + 12 realizes).
- **Regenerated**: `docs/is-semantic-architecture/target-id-snapshots.yaml`, the 5 conformance reports.

## 5. Coverage delta

| Metric | Before P2 | After P2 |
|---|---:|---:|
| domains populated | 5/15 (33%) | 11/15 (73%) |
| functions | 20 | 38 |
| executing-component relationships | 6 | 30 |
| enables-process relationships | 1 | 13 |
| realizes-capability relationships | 6 | 18 |
| unresolved cross-cat refs | 0 (true) | 0 (true) |

## 6. Companion slices (next, not in this CR)

- `CR-IS-CAT-01C-P3`: ISF P3 population (4 domains ISF-12..15) - closes ISF at 15/15. This is the natural completion of the ISF P2 sequence.
- `CR-IS-CAT-03`: ISS 5-CR programme on `dea-catalog-information-system-services`. Resolves 1 of the 6 remaining forward refs.
- `CR-IS-CAT-04`: II 5-CR programme on `dea-catalog-integration-interfaces`. Resolves 4 of the 6.
- `CR-013 (dea-governance)`: portfolio-level reference-resolution policy. Closes Path Y.

## 7. Governance basis

- G-09 (catalogue completeness evidenced, not assumed): the hardened validator
  now resolves against vendored snapshots, not prefix-match.
- G-10 (single source of truth for artifact shape): the P2 generator imports
  p1 helpers; the F4 records' YAML README shape is identical between P1 and P2.
- EGV-006 (references resolve to valid entities within the declared identity
  scope): enforced at CI step 8.
- Programme control: evidence before assertion. P2 added zero synthetic ids.

## 8. Per-domain F2/F4 inventory

### ISF-06 Communication and Collaboration
- F2 `dea:information-system-function-communication-and-collaboration`
  - F4 `collaboration-coordination` (executes on `employee-portal-platform`,
    `api-gateway`; enables `process-coordinate-collaboration`; realizes
    `capability-workforce-management`)
  - F4 `notification-dispatch` (same set as above)

### ISF-07 Content and Knowledge Management
- F2 `dea:information-system-function-content-and-knowledge-management`
  - F4 `content-management` (executes on `data-warehouse-platform`,
    `customer-facing-web-application-platform`)
  - F4 `knowledge-retrieval` (executes on `data-warehouse-platform`,
    `data-warehouse-catalog`)

### ISF-08 Analytics and Decision Support
- F2 `dea:information-system-function-analytics-and-decision-support`
  - F4 `data-analysis` (executes on `data-warehouse-platform`,
    `data-warehouse-query`; enables `process-operate-financial-reporting`)
  - F4 `insight-generation` (executes on `data-warehouse-platform`,
    `ai-inference-platform`; enables `process-customer-insight-and-retention`)

### ISF-09 Security, Privacy and Trust
- F2 `dea:information-system-function-security-privacy-and-trust`
  - F4 `security-monitoring` (executes on `observability-platform`,
    `distributed-tracer`; enables `process-audit-policy-compliance`)
  - F4 `threat-detection` (executes on `observability-platform`,
    `identity-broker`; enables `process-improve-policy-and-control-framework`)

### ISF-10 Monitoring and Observability
- F2 `dea:information-system-function-monitoring-and-observability`
  - F4 `metric-collection` (executes on `observability-platform`,
    `metrics-collector`)
  - F4 `log-aggregation` (executes on `observability-platform`,
    `log-aggregator`)

### ISF-11 Configuration and Administration
- F2 `dea:information-system-function-configuration-and-administration`
  - F4 `configuration-deployment` (executes on `development-platform`,
    `ci-cd-pipeline`; enables `process-improve-technology-platforms`; realizes
    `capability-change-management`)
  - F4 `configuration-validation` (executes on `development-platform`,
    `build-service`; same enables/realizes)
