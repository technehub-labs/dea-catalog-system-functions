# P2 Coverage and Exclusion Report (CR-IS-CAT-01C-P2)

**Date**: 2026-10-19
**Scope**: P2 domains (ISF-06..11)
**Source**: 5-CR programme section 5 + 01C-P2 brief

## 1. Population methodology

CR-IS-CAT-01C-P2 added 6 functional domains to the `dea-catalog-information-system-functions` catalogue.
The methodology followed the P1 sequence (functional-domain coverage,
candidate evaluation, semantic normalization, decomposition, documentation):
1. Each of the 6 P2 domains was reviewed against the 15-domain taxonomy and
   the source doc section 5.
2. 1 F2 parent + 2 F4 children admitted per domain = 18 records total.
3. Cross-catalogue references (BC / BP / ISC) for the new records use
   **canonical** ids from the start, per CR-IS-CAT-01R rebasing.

## 2. Population summary

| Domain | F2 | F4 | Total |
|---|---|---|---|
| ISF-06 Communication and Collaboration | 1 | 2 | 3 |
| ISF-07 Content and Knowledge Management | 1 | 2 | 3 |
| ISF-08 Analytics and Decision Support | 1 | 2 | 3 |
| ISF-09 Security, Privacy and Trust | 1 | 2 | 3 |
| ISF-10 Monitoring and Observability | 1 | 2 | 3 |
| ISF-11 Configuration and Administration | 1 | 2 | 3 |
| **Total** | **6** | **12** | **18** |

## 3. Coverage delta

| Metric | Before P2 | After P2 |
|---|---:|---:|
| domains populated | 5/15 | **11/15** |
| functions | 20 | **38** |
| cross-cat relations | 16 | **64** |

## 4. Deferred functions (P2-scope)

Each P2 domain's deferred list is internal to the F2's decomposition rationale.
Future P2 enrichment CRs may split each F2 into more F4 children.

## 5. Per-domain composition

### ISF-06 Communication and Collaboration
- **F2** Communication and Collaboration (composes child functions).
- **F4** Collaboration Coordination: routes work, messages, presence between agents and humans.
- **F4** Notification Dispatch: delivers a notification to a recipient across the appropriate channel.

### ISF-07 Content and Knowledge Management
- **F2** Content and Knowledge Management (composes child functions).
- **F4** Content Management: stores, versions, indexes unstructured content.
- **F4** Knowledge Retrieval: resolves a knowledge query against the indexed corpus.

### ISF-08 Analytics and Decision Support
- **F2** Analytics and Decision Support (composes child functions).
- **F4** Data Analysis: applies analytical transformations over a curated dataset.
- **F4** Insight Generation: produces an insight from analytical outputs.

### ISF-09 Security, Privacy and Trust
- **F2** Security, Privacy and Trust (composes child functions).
- **F4** Security Monitoring: collects security telemetry and evaluates detection rules.
- **F4** Threat Detection: applies detection logic to identify a threat.

### ISF-10 Monitoring and Observability
- **F2** Monitoring and Observability (composes child functions).
- **F4** Metric Collection: samples a runtime metric at the configured cadence.
- **F4** Log Aggregation: ingests a log record, indexes it for retrieval.

### ISF-11 Configuration and Administration
- **F2** Configuration and Administration (composes child functions).
- **F4** Configuration Deployment: applies a configuration change to a target.
- **F4** Configuration Validation: validates a configuration change against policy.

## 6. Reference integrity

| Bucket | Count |
|---|---:|
| total | 206 |
| resolved | 200 |
| forward | 6 |
| unresolved | 0 |

## 7. Next slice

`CR-IS-CAT-01C-P3` (ISF P3, ISF-12..15) closes the ISF catalogue at 15/15.
4 domains left (Resource and Capacity Management, AI and Intelligent
Processing, Experience and Interaction, Search and Discovery) targeting
~12 more records and ~36 more relationships.
