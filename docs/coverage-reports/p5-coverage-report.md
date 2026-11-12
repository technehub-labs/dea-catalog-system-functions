# P5 Coverage Report (CR-IS-CAT-01C-P5)

**Date**: 2026-11-12
**Scope**: relationship registry population for the CR-IS-CAT-01C-P4 evidence base
(594 executes edges + 594 measured_by edges) and target-id snapshot re-pinning
**Source**: CR-IS-CAT-01C-P4 function records (executing_components evidence);
scripts/p5_registry_data.json (system anchor metric bridge); dea-catalog-metrics
at pin 50e0e670; dea-catalog-application-components at pin 316931db

## 1. Coverage summary

| Measure | Before P5 | After P5 |
|---|---|---|
| Registry relationship records | 96 | 1284 |
| dea:executes edges | 46 | 640 |
| dea:measured_by edges | 1 (forward) | 595 (594 resolved + 1 forward) |
| P4 functions with an executes edge | 0 of 594 | 594 of 594 (100 percent) |
| P4 functions with a measured_by edge | 0 of 594 | 594 of 594 (100 percent) |
| Reference-integrity classification | 928 classified, 922 resolved, 6 forward, 0 unresolved | 2116 classified, 2110 resolved, 6 forward, 0 unresolved |

## 2. executes edge coverage per functional domain

| Functional domain | P4 functions | executes edges |
|---|---|---|
| Transaction Processing | 183 | 183 |
| Workflow and Orchestration | 172 | 172 |
| Information and Data Management | 78 | 78 |
| Integration and Interoperability | 43 | 43 |
| Identity and Access | 25 | 25 |
| Resource and Capacity Management | 37 | 37 |
| Experience and Interaction | 18 | 18 |
| Configuration and Administration | 16 | 16 |
| Monitoring and Observability | 12 | 12 |
| Communication and Collaboration | 10 | 10 |

Total: 594 of 594 functions covered; 141 distinct executing components, all
present in the ISC snapshot at pin 316931db.

## 3. measured_by edge coverage per system archetype

Every function of an archetype is measured by the archetype's anchor metric
(the 34-row bridge in scripts/p5_registry_data.json; rationale per row there).

| System archetype | Functions | Anchor metric |
|---|---|---|
| Card Payment Network | 8 | dea:metric-authorization-approval-rate-deep-dive |
| Claims Management System | 7 | dea:metric-claims-cycle-time-deep-dive |
| Cloud Data Warehouse | 10 | dea:metric-query-p95-latency |
| Cloud Infrastructure Platform | 10 | dea:metric-mean-time-to-provision-resource |
| Communications Platform (CPaaS) | 6 | dea:metric-first-attempt-delivery-success |
| Container Orchestration Platform | 15 | dea:metric-container-image-scan-gate-pass-rate |
| Continuous Integration / Continuous Delivery (CI/CD) Platform | 8 | dea:metric-ci-pipeline-success-rate |
| Core Banking System | 37 | dea:metric-payment-success-rate |
| Customer Relationship Management (CRM) System | 50 | dea:metric-customer-satisfaction-score |
| Customer Service Ticketing Platform | 6 | dea:metric-first-contact-resolution |
| Data Lakehouse Platform | 8 | dea:metric-data-platform-sla-compliance |
| E-Commerce Platform | 23 | dea:metric-checkout-completion-rate |
| Electronic Health Record (EHR) System | 30 | dea:metric-medication-error-rate |
| Email Delivery Platform | 4 | dea:metric-email-deliverability-rate |
| Enterprise Resource Planning (ERP) System | 130 | dea:metric-erp-batch-job-success-rate |
| Event Streaming Platform | 10 | dea:metric-data-pipeline-freshness-sla-attainment |
| Financial Messaging Network | 10 | dea:metric-settlement-window-compliance-rate |
| Human Capital Management (HCM) System | 24 | dea:metric-performance-review-completion-rate |
| Identity and Access Management (IAM) Platform | 25 | dea:metric-access-request-fulfilment-cycle-time |
| Infrastructure as Code (IaC) Platform | 6 | dea:metric-infrastructure-as-code-coverage |
| IoT Device Management Platform | 14 | dea:metric-firmware-currency-rate |
| Issue Tracking Platform | 8 | dea:metric-issue-aging-index |
| IT Service Management (ITSM) Platform | 15 | dea:metric-service-level-attainment |
| Manufacturing Execution System (MES) | 10 | dea:metric-production-plan-attainment |
| Mobile Core Network (EPC/5GC) | 15 | dea:metric-core-network-availability |
| Payment Processing Platform | 23 | dea:metric-payment-processing-uptime |
| Policy Administration System | 8 | dea:metric-digital-policy-issuance-rate |
| Radio Access Network (RAN) | 10 | dea:metric-radio-access-network-utilization |
| Supply Chain Visibility Platform | 5 | dea:metric-inventory-accuracy |
| Telecom Business Support System (BSS) | 18 | dea:metric-billing-accuracy-rate-telecom |
| Telecom Operations Support System (OSS) | 15 | dea:metric-cell-outage-rate |
| Transportation Management System (TMS) | 8 | dea:metric-on-time-delivery-rate |
| Warehouse Management System (WMS) | 12 | dea:metric-order-picking-accuracy |
| Workflow Orchestration Platform | 6 | dea:metric-pipeline-orchestration-success-rate |

All 34 anchors resolve against the vendored dea-catalog-metrics snapshot
(4433 ids at pin 50e0e670). Per G-11 these are OpenDEAM v0.7.0 allocation
declarations; the metric definitions remain owned by the Metric catalogue.

## 4. Exclusions and deferrals

- The 6 pre-existing forward references are unchanged (identity-service,
  identity-api, identity-claim, verification-result, event-identity-verified,
  metric-verification-latency); they resolve when their owning catalogues
  populate the target records.
- The processes target pin is held at 390e73eb (the renamed processes
  repository has moved to a new identity scheme; rebasing is a separate CR).
- Per-function (non-anchored) metric refinement is deferred to the Metric
  catalogue per G-11.
- The 50 legacy non-P4 functions (P1/P2/P3 populations) are out of P5 scope:
  their registry rows predate this CR (46 executes, realizes, enables,
  produces, consumes, provides, exposes edges) and their executing component
  references already resolve against the snapshots.
