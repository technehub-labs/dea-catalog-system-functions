# P4 Coverage and Exclusion Report (CR-IS-CAT-01C-P4)

**Date**: 2026-11-10
**Scope**: P4 vendor-neutral corroborated tranche (594 F4 records across
10 of 15 functional domains)
**Source**: vendor-neutral ISF reference catalog (OpenDEAM metamodel crawl; CR-IS-CAT-02C-P4 carries the
executing components)

## 1. Population methodology

The P4 tranche admits vendor-neutral functions corroborated by at least 3 distinct vendor
systems. Per function: the primary evidence is function-level (the vendor module that documents
the function); the corroborating evidence is module-level (the same generic sub-system realized
by other vendors). Per G-12 no vendor product becomes canonical; evidence is recorded in
governance.source_and_evidence.

## 2. Population summary

| Domain | P4 F4 records |
|---|---|
| Identity and Access | 25 |
| Information and Data Management | 78 |
| Transaction Processing | 183 |
| Workflow and Orchestration | 172 |
| Integration and Interoperability | 43 |
| Communication and Collaboration | 10 |
| Monitoring and Observability | 12 |
| Configuration and Administration | 16 |
| Resource and Capacity Management | 37 |
| Experience and Interaction | 18 |

Total: 594 records. Generic structure: 34 system classes, 63 sub-systems, 141 components
(mirrored in CR-IS-CAT-02C-P4).

## 3. Full (system / sub-system) to domain mapping

| Generic system class | Generic sub-system | Functional domain | F4 records |
|---|---|---|---|
| Card Payment Network | Authorization, Clearing & Settlement | Transaction Processing | 8 |
| Claims Management System | Claims Intake & Adjudication | Workflow and Orchestration | 7 |
| Cloud Data Warehouse | Cloud Data Warehouse | Information and Data Management | 10 |
| Cloud Infrastructure Platform | Compute, Storage & Networking Services | Resource and Capacity Management | 10 |
| Communications Platform (CPaaS) | Programmable Communications | Communication and Collaboration | 6 |
| Container Orchestration Platform | Cluster Control Plane & Workloads | Resource and Capacity Management | 15 |
| Continuous Integration / Continuous Delivery (CI/CD) Platform | CI/CD Workflows | Workflow and Orchestration | 8 |
| Core Banking System | Customer & Deposit Accounts | Transaction Processing | 12 |
| Core Banking System | Deposits & Payments | Transaction Processing | 5 |
| Core Banking System | Lending | Transaction Processing | 7 |
| Core Banking System | Payments & Financial Messaging | Transaction Processing | 6 |
| Core Banking System | Trade Finance & Treasury | Transaction Processing | 7 |
| Customer Relationship Management (CRM) System | Customer Service & Marketing | Experience and Interaction | 15 |
| Customer Relationship Management (CRM) System | Customer Service Management | Workflow and Orchestration | 12 |
| Customer Relationship Management (CRM) System | Platform Automation Services | Integration and Interoperability | 11 |
| Customer Relationship Management (CRM) System | Sales Force Automation | Workflow and Orchestration | 12 |
| Customer Service Ticketing Platform | Customer Service Management | Workflow and Orchestration | 6 |
| Data Lakehouse Platform | Lakehouse Platform | Information and Data Management | 8 |
| E-Commerce Platform | Commerce & Orders | Workflow and Orchestration | 15 |
| E-Commerce Platform | Composable Commerce API | Integration and Interoperability | 8 |
| Electronic Health Record (EHR) System | Clinical Management | Workflow and Orchestration | 20 |
| Electronic Health Record (EHR) System | Patient Engagement & Population Health | Experience and Interaction | 3 |
| Electronic Health Record (EHR) System | Revenue Cycle | Transaction Processing | 7 |
| Email Delivery Platform | Email Delivery | Communication and Collaboration | 4 |
| Enterprise Resource Planning (ERP) System | Financial Accounting | Transaction Processing | 62 |
| Enterprise Resource Planning (ERP) System | Human Capital Management | Information and Data Management | 10 |
| Enterprise Resource Planning (ERP) System | Materials Management | Transaction Processing | 15 |
| Enterprise Resource Planning (ERP) System | Production Planning | Workflow and Orchestration | 12 |
| Enterprise Resource Planning (ERP) System | Project Management | Workflow and Orchestration | 8 |
| Enterprise Resource Planning (ERP) System | Sales Order Management | Transaction Processing | 15 |
| Enterprise Resource Planning (ERP) System | Supply Chain Management | Workflow and Orchestration | 8 |
| Event Streaming Platform | Event Streaming Platform | Integration and Interoperability | 10 |
| Financial Messaging Network | Messaging & Connectivity | Integration and Interoperability | 10 |
| Human Capital Management (HCM) System | Human Capital Management | Information and Data Management | 24 |
| IT Service Management (ITSM) Platform | IT Service Management | Workflow and Orchestration | 15 |
| Identity and Access Management (IAM) Platform | Identity & Access Services | Identity and Access | 25 |
| Infrastructure as Code (IaC) Platform | Infrastructure as Code | Configuration and Administration | 6 |
| IoT Device Management Platform | Device Connectivity | Information and Data Management | 14 |
| Issue Tracking Platform | Issue Tracking & Planning | Workflow and Orchestration | 8 |
| Manufacturing Execution System (MES) | Manufacturing Execution | Workflow and Orchestration | 10 |
| Mobile Core Network (EPC/5GC) | Charging Function | Transaction Processing | 3 |
| Mobile Core Network (EPC/5GC) | Mobility & Session Management | Resource and Capacity Management | 5 |
| Mobile Core Network (EPC/5GC) | Policy Control | Configuration and Administration | 3 |
| Mobile Core Network (EPC/5GC) | Subscriber Data Management | Information and Data Management | 4 |
| Payment Processing Platform | Checkout & Wallet | Transaction Processing | 8 |
| Payment Processing Platform | Payments | Transaction Processing | 9 |
| Payment Processing Platform | Subscription Billing & Payouts | Transaction Processing | 6 |
| Policy Administration System | Policy Origination & Administration | Transaction Processing | 8 |
| Radio Access Network (RAN) | Cell & Radio Resource Management | Resource and Capacity Management | 4 |
| Radio Access Network (RAN) | Handover & Mobility Optimization | Resource and Capacity Management | 3 |
| Radio Access Network (RAN) | Self-Organizing Network | Configuration and Administration | 3 |
| Supply Chain Visibility Platform | Visibility Network | Monitoring and Observability | 5 |
| Telecom Business Support System (BSS) | Mediation & Charging | Integration and Interoperability | 4 |
| Telecom Business Support System (BSS) | Order Management & Orchestration | Workflow and Orchestration | 5 |
| Telecom Business Support System (BSS) | Product & Offer Catalog Management | Information and Data Management | 4 |
| Telecom Business Support System (BSS) | Rating & Billing | Transaction Processing | 5 |
| Telecom Operations Support System (OSS) | Fault Management & Service Assurance | Monitoring and Observability | 4 |
| Telecom Operations Support System (OSS) | Network Inventory & Topology | Information and Data Management | 4 |
| Telecom Operations Support System (OSS) | Performance Management | Monitoring and Observability | 3 |
| Telecom Operations Support System (OSS) | Service Provisioning & Activation | Configuration and Administration | 4 |
| Transportation Management System (TMS) | Transportation & Freight | Workflow and Orchestration | 8 |
| Warehouse Management System (WMS) | Warehouse Operations | Workflow and Orchestration | 12 |
| Workflow Orchestration Platform | Workflow Orchestration | Workflow and Orchestration | 6 |

## 4. Coverage closure

| Metric | Before P4 | After P4 |
|---|---:|---:|
| Function records | 50 | 644 |
| Populated domains | 15 of 15 | 15 of 15 |
| Vendor-neutral corroborated records | 0 | 594 |
| executing_components references | 328 classified refs total | 922 resolved + 6 forward + 0 unresolved |

## 5. Exclusions (G-09)

The following domains receive no P4 records: content-and-knowledge-management,
analytics-and-decision-support, ai-and-intelligent-processing, search-and-discovery. The P4
source inventory contains no corroborated candidate whose primary behaviour maps to these
domains (the covered classes express content, analytics, AI and search behaviour only as
secondary aspects of data-management or integration functions). Admission is deferred to a
follow-on CR once 3-vendor corroborated candidates exist; completeness is evidenced, not
assumed (per G-09).

## 6. Corroboration rule

Every record cites at least 3 distinct vendor systems (primary function-level evidence plus at
least two module-level corroborations). The rule is asserted by the P4 pipeline before emission
and by the local validation suite; no record is admitted below the threshold.
