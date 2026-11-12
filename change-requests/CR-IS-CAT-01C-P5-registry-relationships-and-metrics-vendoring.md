# CR-IS-CAT-01C-P5: Relationship Registry Population and Metrics Vendoring

- **CR**: CR-IS-CAT-01C-P5
- **Date**: 2026-11-12
- **Author**: Emmanuel A. Otchere
- **Status**: Proposed (this PR)
- **Catalog**: dea-catalog-information-system-functions (legacy URL: dea-catalog-system-functions until org-admin transfer)
- **Parent CRs**: CR-IS-CAT-01C-P4 (the 594 vendor-neutral function records whose executing_components evidence drives the executes edges), CR-IS-CAT-01R (the hardened reference-integrity validator and target-id snapshots consumed here), CR-IS-CAT-02C-P5 in technehub-labs/dea-catalog-application-components (the F3 atomic component population landed at the new ISC pin)
- **Governance**: G-08 (every relationship uses an authorized semantic contract), G-09 (completeness is evidenced, not assumed), G-10 (all generated artefacts are reproducible and validated), G-11 (metric definitions remain owned by the Metric catalogue; the measured_by row is an OpenDEAM allocation declaration), G-12 (no vendor product becomes canonical)

## 1. Executive Summary

CR-IS-CAT-01C-P5 closes the relationship gap left by the P4 tranche. CR-IS-CAT-01C-P4 admitted 594 vendor-neutral function records, each declaring its executing component in the record's executing_components field, but the cross-catalogue relationship registry carried executes edges only for the legacy P2 population (46 records) and a single forward-declared measured_by row. This CR populates the registry for the full P4 evidence base:

1. **594 dea:executes edges**, one per P4 function record, derived from its executing_components allocation (evidence-driven per G-09; no discretionary selection).
2. **594 dea:measured_by edges**, one per P4 function record, resolved through a curated 34-row system-archetype to anchor-metric bridge (scripts/p5_registry_data.json); every target is a real record of the dea-catalog-metrics catalogue, vendored into the target-id snapshots at pin 50e0e670. Per G-11 these rows are OpenDEAM v0.7.0 allocation declarations, not metamodel relationship claims; the metric definitions remain owned by the Metric catalogue.

The registry grows from 96 to 1284 relationship records. The target-id snapshots are re-pinned: dea-catalog-application-components advances from 8508b867 (276 ids) to 316931db (735 ids, including the 459 CR-IS-CAT-02C-P5 F3 atoms), and dea-catalog-metrics is vendored for the first time (4433 ids). The regenerated reference-integrity report classifies 2116 references: 2110 resolved, 6 forward, 0 unresolved (hard check holds).

## 2. Method: executes edges (derived, not asserted; per G-09)

Every CR-IS-CAT-01C-P4 function record declares exactly one executing component (verified: 594 records, one entry each; 141 distinct components, matching the CR-IS-CAT-02C-P4 F2 population). The generator (scripts/generate_p5_registry.py) emits one registry record per function:

- **id**: rel:{function-slug}-executes-{component-slug}
- **source_id**: the function id; **target_id**: the executing component id
- **relationship_description**: The {Function Name} function is executed by the {component-slug} component (per the CR-IS-CAT-01C-P4 executing_components allocation).
- **provenance / evidence**: the CR-IS-CAT-01C-P4 executing_components evidence (vendor-neutral per G-12).

The generator hard-fails unless every target component id exists in the vendored ISC snapshot. The direction follows the dominant convention of the existing registry (source = function, target = executing component; 44 of the 46 pre-existing executes rows use this form).

## 3. Method: measured_by edges (the system anchor metric bridge; per G-11)

A per-function bespoke metric match against a 4433-record generic metric catalogue is neither evidenced nor reviewable at this scale. The P5 allocation therefore uses a system-anchored bridge, mirroring how CR-IS-CAT-02C-P5 used a curated verb-cluster taxonomy as its decomposition evidence:

1. The 34 vendor-neutral P4 system archetypes (from scripts/p4_function_data.json) are each mapped to one anchor metric record of the dea-catalog-metrics catalogue. The bridge is curated (34 rows, one screen of review), documented in section 4, and machine-readable in scripts/p5_registry_data.json.
2. Selection criteria per row: the anchor is the canonical operational or outcome measure of the archetype, vendor-neutral, and present in the vendored metric snapshot at the pinned SHA.
3. Every function of an archetype is measured by that archetype's anchor metric (the registry cardinality is many; a per-function metric refinement remains owned by the Metric catalogue per G-11).
4. The pre-existing forward-declared measured_by row (rel:identity-verification-measured-by-verification-latency; dea:metric-verification-latency has no record yet) is untouched and stays forward.

The anchor metric definition is never restated in this catalogue; the target id resolves against the vendored snapshot only (G-11).

## 4. The System Anchor Metric Bridge (34 rows)

| System archetype | P4 functions | Anchor metric | Metric domain |
|---|---|---|---|
| Card Payment Network | 8 | dea:metric-authorization-approval-rate-deep-dive | payments_cards_deep_dive |
| Claims Management System | 7 | dea:metric-claims-cycle-time-deep-dive | insurance_claims_deep_dive |
| Cloud Data Warehouse | 10 | dea:metric-query-p95-latency | database_data_platform_operations |
| Cloud Infrastructure Platform | 10 | dea:metric-mean-time-to-provision-resource | data_center_cloud_operations |
| Communications Platform (CPaaS) | 6 | dea:metric-first-attempt-delivery-success | postal_courier |
| Container Orchestration Platform | 15 | dea:metric-container-image-scan-gate-pass-rate | devsecops_application_security_engineering |
| Continuous Integration / Continuous Delivery (CI/CD) Platform | 8 | dea:metric-ci-pipeline-success-rate | continuous_integration |
| Core Banking System | 37 | dea:metric-payment-success-rate | banking_financial_services |
| Customer Relationship Management (CRM) System | 50 | dea:metric-customer-satisfaction-score | customer |
| Customer Service Ticketing Platform | 6 | dea:metric-first-contact-resolution | customer |
| Data Lakehouse Platform | 8 | dea:metric-data-platform-sla-compliance | database_data_platform_operations |
| E-Commerce Platform | 23 | dea:metric-checkout-completion-rate | retail_e_commerce |
| Electronic Health Record (EHR) System | 30 | dea:metric-medication-error-rate | healthcare |
| Email Delivery Platform | 4 | dea:metric-email-deliverability-rate | marketing |
| Enterprise Resource Planning (ERP) System | 130 | dea:metric-erp-batch-job-success-rate | erp_enterprise_application_operations |
| Event Streaming Platform | 10 | dea:metric-data-pipeline-freshness-sla-attainment | mlops_model_lifecycle_operations |
| Financial Messaging Network | 10 | dea:metric-settlement-window-compliance-rate | payments_cards_deep_dive |
| Human Capital Management (HCM) System | 24 | dea:metric-performance-review-completion-rate | human_resources |
| Identity and Access Management (IAM) Platform | 25 | dea:metric-access-request-fulfilment-cycle-time | identity_access_management_operations |
| Infrastructure as Code (IaC) Platform | 6 | dea:metric-infrastructure-as-code-coverage | continuous_delivery_deployment |
| IoT Device Management Platform | 14 | dea:metric-firmware-currency-rate | network_change_configuration_management |
| Issue Tracking Platform | 8 | dea:metric-issue-aging-index | project_risk_issue_management |
| IT Service Management (ITSM) Platform | 15 | dea:metric-service-level-attainment | it_service_management |
| Manufacturing Execution System (MES) | 10 | dea:metric-production-plan-attainment | manufacturing |
| Mobile Core Network (EPC/5GC) | 15 | dea:metric-core-network-availability | telecom_network_operations |
| Payment Processing Platform | 23 | dea:metric-payment-processing-uptime | payments_fintech |
| Policy Administration System | 8 | dea:metric-digital-policy-issuance-rate | insurance_distribution_direct_digital |
| Radio Access Network (RAN) | 10 | dea:metric-radio-access-network-utilization | telecom_network_operations |
| Supply Chain Visibility Platform | 5 | dea:metric-inventory-accuracy | supply_chain |
| Telecom Business Support System (BSS) | 18 | dea:metric-billing-accuracy-rate-telecom | telecom_customer_experience_billing |
| Telecom Operations Support System (OSS) | 15 | dea:metric-cell-outage-rate | telecom_network_operations |
| Transportation Management System (TMS) | 8 | dea:metric-on-time-delivery-rate | logistics_transportation |
| Warehouse Management System (WMS) | 12 | dea:metric-order-picking-accuracy | warehousing |
| Workflow Orchestration Platform | 6 | dea:metric-pipeline-orchestration-success-rate | mlops_model_lifecycle_operations |

Per-row selection rationale is recorded in scripts/p5_registry_data.json (rationale field). Function counts sum to 594.

## 5. Target-id snapshot re-pinning

scripts/build_target_snapshots.py is extended (dea-catalog-metrics added to TARGET_REPOS with the dea:metric- id prefix; a HEAD_SHA-file fallback in git-less environments keeps the pinned SHA deterministic per G-10). The regenerated docs/is-semantic-architecture/target-id-snapshots.yaml:

| Target repo | Old pin | New pin | Ids |
|---|---|---|---|
| dea-catalog-business-capabilities | 848b1635 | 92a9b6d9 | 29 to 40 (strictly additive; all 29 prior ids retained) |
| dea-catalog-processes | 390e73eb | 390e73eb (held) | 139 (byte-identical section) |
| dea-catalog-application-components | 8508b867 | 316931db | 276 to 735 (includes the 459 CR-IS-CAT-02C-P5 F3 atoms) |
| dea-catalog-metrics | (absent) | 50e0e670 | 4433 (new target catalogue) |

The processes pin is intentionally held at 390e73eb: the renamed dea-catalog-business-processes repository has moved to a new processes:* identity scheme, and rebasing the ISF dea:process-* references onto it is a separate follow-on CR (the CR-IS-CAT-01R rebased-references mechanism), out of P5 scope. The capabilities pin advance is a consequence of regeneration from the current target main; it is strictly additive (no id used by this catalogue was dropped).

## 6. Repository Deliverables (this PR)

- scripts/generate_p5_registry.py: the deterministic, idempotent registry generator (per G-10; three consecutive runs are byte-identical; strips and re-emits its own marked blocks).
- scripts/p5_registry_data.json: the machine-readable 34-row system anchor metric bridge with per-row rationale and pins.
- scripts/build_target_snapshots.py: metrics target repo + git-less HEAD_SHA fallback.
- relationships/v1-alpha/relationships.yaml: 1188 new records (594 executes + 594 measured_by) in a marked P5 block, plus the P5 change_history entry; the 96 pre-existing records are untouched.
- docs/is-semantic-architecture/target-id-snapshots.yaml: re-pinned and extended (section 5).
- reports/: all 5 conformance reports regenerated (registry 1284 records; reference-integrity 2110 resolved, 6 forward, 0 unresolved).
- docs/coverage-reports/p5-coverage-report.md (this CR's coverage report).
- CHANGELOG.md and change-requests/README.md index row.

Function records, taxonomy, schemas, workflows and metamodel-pointer are untouched.

## 7. CI Requirements

All four existing workflows must pass without modification. Pre-flight verification (local, against the full updated tree):

- validate-entities: no function records changed; 644 records unchanged. PASS.
- validate-catalogue: registry parse (1284 records); relationship-record.schema.json validation of every record (required fields; authorized relationship kinds; id and target patterns); endpoint validation (canonical prefixes); measured_by targets all dea:metric-* (step 9); reference-integrity hard check unresolved_count == 0 with 6 forward; F2 record shape parity. PASS.
- validate-taxonomy: unchanged taxonomy files. PASS.
- validate-allocation: metamodel-pointer.yaml untouched; pinned OpenDEAM v0.7.0 validation unchanged. PASS.

## 8. Acceptance Criteria

1. 594 executes edges exist, one per CR-IS-CAT-01C-P4 function, each matching the record's executing_components evidence.
2. 594 measured_by edges exist, one per function, each targeting a metric id present in the vendored dea-catalog-metrics snapshot at pin 50e0e670.
3. The 96 pre-existing registry records and the forward-declared measured_by row are byte-identical to before this CR.
4. Re-running scripts/generate_p5_registry.py reproduces relationships.yaml byte-identically (G-10).
5. reference-integrity unresolved_count remains 0; all 1188 new references classify as resolved.
6. The D-004 / D-005 glyph and punctuation embargo holds over every emitted record, script, data file, report and doc (no em dash, no en dash, no ellipsis, no triple semicolon).

## 9. Risks and Mitigations

- **Anchor metric fit.** The bridge is system-anchored, not function-bespoke; the CR documents this as an allocation declaration (G-11) whose refinement belongs to the Metric catalogue. A bridge reassessment is a follow-on CR that regenerates the registry deterministically (G-10), not an in-place edit.
- **Snapshot bulk.** The vendored metrics section adds 4433 entries (~1.4MB YAML); CI resolves against it offline and deterministically, unchanged in mechanism.
- **Processes identity drift.** The renamed processes repository has moved to a new identity scheme; the ISF references stay pinned to the harvestable 390e73eb content until a rebasing CR (section 5).

## 10. Definition of Done

All deliverables in section 6 merged to main; all four workflows green on the merge commit; the new main SHA recorded for downstream pinning.

## 11. Remaining ISF Work

- Process-reference rebasing onto the renamed dea-catalog-business-processes identity scheme (CR-IS-CAT-01R mechanism; separate CR).
- The 6 remaining forward references (identity-service, identity-api, 2 data entities, 1 event, verification-latency metric) resolve when their owning catalogues populate the target records.
- Per-function (non-anchored) metric refinement if the Metric catalogue assumes ownership of ISF-level allocation.
- Pre-existing hygiene (untouched by this CR, no CI impact): the NOTICE file and the CR-IS-CAT-01C-P2H doc each contain pre-dated em dash characters that predate the embargo sweep.
