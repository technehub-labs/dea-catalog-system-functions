# CR-IS-CAT-01C-P4: Information System Function P4 Vendor-Neutral Corroborated Population

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-01C-P4 |
| **Title** | Information System Function P4 Population (vendor-neutral, corroborated) |
| **Status** | Proposed (this PR) |
| **Type** | Catalogue population (P4 follow-on; vendor-neutral corroborated tranche) |
| **Repository** | technehub-labs/dea-catalog-information-system-functions (legacy URL: technehub-labs/dea-catalog-system-functions until org-admin transfer) |
| **Parent** | CR-IS-CAT-01 (merged); CR-IS-CAT-01A..01D (merged) |
| **Depends on** | CR-IS-CAT-01 (merged); CR-IS-CAT-01A..01D (merged); CR-IS-CAT-02C-P4 (this programme pair; the ISC PR carries the executing components) |
| **Canonical entity** | `dea:InformationSystemFunction` (class alias `ISF`; OpenDEAM-local `dea:entity-information-system-function`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-10 |

## 1. Executive Summary

This CR is the P4 follow-on population of the ISF catalogue: a vendor-neutral, corroborated
tranche of 594 F4 records across 10 of 15 functional domains, grounded in a
reference catalog of 34 generic system classes, 63 generic sub-systems and 141 composite
components. After this PR merges the ISF catalogue holds 644 function records.

The tranche applies two standing rules beyond the P1-P3 methodology:

1. **Vendor neutrality (G-12)**: every record uses generic industry terminology; vendor products
   appear only as evidence in governance.source_and_evidence, never in identifiers, names,
   descriptions or domains.
2. **Corroboration rule**: every function cites at least 3 distinct vendor systems as evidence
   (the primary function-level evidence plus at least two module-level corroborations of the
   same generic sub-system realized by other vendors).

## 2. Selection Methodology

The P4 source inventory is the vendor-neutral reference catalog built on the OpenDEAM metamodel
crawl (ISF executed by ISC; ISC composed of ISC recursively: system class to sub-system to
component). Selection criteria per function:

1. **Generic**: the function is stated in vendor-free industry terms.
2. **Corroborated**: at least 3 distinct vendor systems evidence the generic sub-system that
   executes the function.
3. **Crawlable**: the function executes on a component admitted by the CR-IS-CAT-02C-P4 population.

## 3. P4 Function Inventory

| Domain | F4 records | Generic (system / sub-system) pairs |
|---|---|---|
| Identity and Access | 25 | Identity and Access Management (IAM) Platform / Identity & Access Services |
| Information and Data Management | 78 | Cloud Data Warehouse / Cloud Data Warehouse; Data Lakehouse Platform / Lakehouse Platform; Enterprise Resource Planning (ERP) System / Human Capital Management; Human Capital Management (HCM) System / Human Capital Management; IoT Device Management Platform / Device Connectivity; Mobile Core Network (EPC/5GC) / Subscriber Data Management; Telecom Business Support System (BSS) / Product & Offer Catalog Management; Telecom Operations Support System (OSS) / Network Inventory & Topology |
| Transaction Processing | 183 | Card Payment Network / Authorization, Clearing & Settlement; Core Banking System / Customer & Deposit Accounts; Core Banking System / Deposits & Payments; Core Banking System / Lending; Core Banking System / Payments & Financial Messaging; Core Banking System / Trade Finance & Treasury; Electronic Health Record (EHR) System / Revenue Cycle; Enterprise Resource Planning (ERP) System / Financial Accounting; Enterprise Resource Planning (ERP) System / Materials Management; Enterprise Resource Planning (ERP) System / Sales Order Management; Mobile Core Network (EPC/5GC) / Charging Function; Payment Processing Platform / Checkout & Wallet; Payment Processing Platform / Payments; Payment Processing Platform / Subscription Billing & Payouts; Policy Administration System / Policy Origination & Administration; Telecom Business Support System (BSS) / Rating & Billing |
| Workflow and Orchestration | 172 | Claims Management System / Claims Intake & Adjudication; Continuous Integration / Continuous Delivery (CI/CD) Platform / CI/CD Workflows; Customer Relationship Management (CRM) System / Customer Service Management; Customer Relationship Management (CRM) System / Sales Force Automation; Customer Service Ticketing Platform / Customer Service Management; E-Commerce Platform / Commerce & Orders; Electronic Health Record (EHR) System / Clinical Management; Enterprise Resource Planning (ERP) System / Production Planning; Enterprise Resource Planning (ERP) System / Project Management; Enterprise Resource Planning (ERP) System / Supply Chain Management; IT Service Management (ITSM) Platform / IT Service Management; Issue Tracking Platform / Issue Tracking & Planning; Manufacturing Execution System (MES) / Manufacturing Execution; Telecom Business Support System (BSS) / Order Management & Orchestration; Transportation Management System (TMS) / Transportation & Freight; Warehouse Management System (WMS) / Warehouse Operations; Workflow Orchestration Platform / Workflow Orchestration |
| Integration and Interoperability | 43 | Customer Relationship Management (CRM) System / Platform Automation Services; E-Commerce Platform / Composable Commerce API; Event Streaming Platform / Event Streaming Platform; Financial Messaging Network / Messaging & Connectivity; Telecom Business Support System (BSS) / Mediation & Charging |
| Communication and Collaboration | 10 | Communications Platform (CPaaS) / Programmable Communications; Email Delivery Platform / Email Delivery |
| Monitoring and Observability | 12 | Supply Chain Visibility Platform / Visibility Network; Telecom Operations Support System (OSS) / Fault Management & Service Assurance; Telecom Operations Support System (OSS) / Performance Management |
| Configuration and Administration | 16 | Infrastructure as Code (IaC) Platform / Infrastructure as Code; Mobile Core Network (EPC/5GC) / Policy Control; Radio Access Network (RAN) / Self-Organizing Network; Telecom Operations Support System (OSS) / Service Provisioning & Activation |
| Resource and Capacity Management | 37 | Cloud Infrastructure Platform / Compute, Storage & Networking Services; Container Orchestration Platform / Cluster Control Plane & Workloads; Mobile Core Network (EPC/5GC) / Mobility & Session Management; Radio Access Network (RAN) / Cell & Radio Resource Management; Radio Access Network (RAN) / Handover & Mobility Optimization |
| Experience and Interaction | 18 | Customer Relationship Management (CRM) System / Customer Service & Marketing; Electronic Health Record (EHR) System / Patient Engagement & Population Health |

## 4. Decomposition Decision (G-06)

The P4 records are F4 leaves with no synthetic F2 parents: grouping is by functional_domain and
the executing_components crawl. Per G-06 classification and decomposition are separate
structures; admitting fabricated F2 parents for the vendor-neutral tranche would assert
decomposition that the corroborating evidence does not support. The bidirectional and cycle
validators pass trivially (no parent_function fields are set).

## 5. Exclusions (G-09)

| Domain | Exclusion rationale |
|---|---|
| Content and Knowledge Management | No corroborated candidate in the P4 source inventory maps primarily to this domain; admitted in a follow-on CR once a 3-vendor corroborated candidate exists (per G-09) |
| Analytics and Decision Support | No corroborated candidate in the P4 source inventory maps primarily to this domain; admitted in a follow-on CR once a 3-vendor corroborated candidate exists (per G-09) |
| AI and Intelligent Processing | No corroborated candidate in the P4 source inventory maps primarily to this domain; admitted in a follow-on CR once a 3-vendor corroborated candidate exists (per G-09) |
| Search and Discovery | No corroborated candidate in the P4 source inventory maps primarily to this domain; admitted in a follow-on CR once a 3-vendor corroborated candidate exists (per G-09) |

## 6. Executing Components and the Snapshot Pin

Every record lists its executing component (admitted by CR-IS-CAT-02C-P4 in
technehub-labs/dea-catalog-application-components) in `executing_components`. The vendored
target-id snapshot `docs/is-semantic-architecture/target-id-snapshots.yaml` is extended with the
238 P4 component ids and the application-components pin is advanced to
the head commit of the CR-IS-CAT-02C-P4 PR. All 594 new references classify as resolved; the CI hard
check (unresolved_count = 0) holds. If the CR-IS-CAT-02C-P4 PR is merged with a rewritten commit (squash
or rebase), the pin MUST be re-advanced by a hygiene CR (the snapshot regeneration scripts own
that step).

## 7. Repository Deliverables (this PR)

- `change-requests/CR-IS-CAT-01C-P4-vendor-neutral-corroborated-population.md` (this file)
- `change-requests/README.md` (updated with the P4 row)
- `docs/coverage-reports/p4-coverage-report.md` (new; the coverage report with the full 63-pair
  domain mapping)
- `scripts/generate_p4_population.py` (new; deterministic idempotent generator)
- `scripts/p4_function_data.json` (new; the P4 inventory)
- `entities/v1-alpha/index.yaml` (updated; catalog counts and change history)
- 10 domain index.yaml files (updated)
- 594 function.yaml records + 594 19-section READMEs under `entities/v1-alpha/domains/`
- `docs/is-semantic-architecture/target-id-snapshots.yaml` (updated; P4 component ids + pin)
- `reports/catalogue-conformance.yaml`, `reports/taxonomy-coverage.yaml`,
  `reports/documentation-coverage.yaml`, `reports/reference-integrity.yaml` (refreshed committed
  copies; CI regenerates)

## 8. CI Requirements

CI MUST validate: v2 ISF schema validation for all 644 records; canonical id uniqueness;
parent/child consistency and cycle checks (trivial: no parents); decomposition level F4;
19-section README conformance; README/function.yaml identity agreement; lifecycle status; F2
record shape parity (unchanged F2 population); cross-catalogue reference integrity with
unresolved_count = 0 (all executing_components resolve against the vendored snapshot);
conformance report determinism.

## 9. Acceptance Criteria

1. 594 F4 vendor-neutral records are admitted across 10 domains.
2. Every record cites at least 3 distinct vendor systems in governance.source_and_evidence.
3. No vendor product name appears in any canonical field (per G-12).
4. All executing_components references resolve against the vendored snapshot (0 unresolved).
5. All READMEs carry the 19 sections and identity agreement with the function record.
6. The domain indexes and catalog index reflect the new counts.
7. The deterministic generator reproduces the P4 artifacts byte-identically (G-10).
8. CI passes.

## 10. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Vendor leakage into canonical fields | Vendor-token assertion in the P4 pipeline; evidence is quarantined to governance.source_and_evidence |
| Inflated corroboration | The corroboration rule requires 3 distinct vendor systems; module-level corroborations must cite the same generic sub-system |
| Snapshot pin drift on merge strategy | Documented in section 6; the pin is re-advanced by a hygiene CR if the CR-IS-CAT-02C-P4 PR head is rewritten |
| Missing F2 parents | Intentional per G-06 (section 4); synthetic parents are not asserted by the evidence |
| Documentation volume (594 READMEs) | Deterministic generation; the generator is idempotent and byte-reproducible |

## 11. Remaining ISF Work

- Typed input/output and execution-characteristic population CR (per-record contracts).
- ISF-07/08/13/15 candidate admission once 3-vendor corroborated candidates exist (G-09).
- Capability/process alignment allocations once the BC/BP catalogues extend their taxonomies.
- ISS and IF catalogue populations (CR-IS-CAT-03/04) to complete the provides/exposes crawl.
