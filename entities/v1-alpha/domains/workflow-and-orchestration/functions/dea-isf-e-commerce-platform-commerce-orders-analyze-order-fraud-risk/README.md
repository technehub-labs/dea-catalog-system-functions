# Analyze order fraud risk

## 1. Identity
- Canonical ID: `dea:information-system-function-e-commerce-platform-commerce-orders-analyze-order-fraud-risk`
- Version: 1.0.0
- Lifecycle: planned
- Functional Domain: ISF-04 Workflow and Orchestration (`isf:domain:workflow-and-orchestration`)
- Category: ISF-04 Workflow and Orchestration (categories populated in CR-IS-CAT-01B; v1.0 has no categories yet)
- Decomposition Level: F4
- Parent Function: none (vendor-neutral leaf; grouping is by functional domain per CR-IS-CAT-01C-P4)

## 2. Definition

Executes the 'Analyze order fraud risk' function within the Commerce & Orders sub-system of a E-Commerce Platform. Operating through the Checkout Service and the Catalog Component, it processes information, applies the business logic and rules defined for Commerce & Orders, and contributes to frictionless omnichannel commerce from catalogue to fulfilment. Vendor-neutral record: vendor corroboration (3 distinct vendor systems) is recorded in governance.source_and_evidence; no vendor product is canonical (per G-12).

## 3. Purpose and Responsibility

Responsibility: Executes the 'Analyze order fraud risk' function within the Commerce & Orders sub-system of a E-Commerce Platform. Operating through the Checkout Service and the Catalog Component, it processes information, applies the business logic and rules defined for Commerce & Orders, and contributes to frictionless omnichannel commerce from catalogue to fulfilment. Vendor-neutral record: vendor corroboration (3 distinct vendor systems) is recorded in governance.source_and_evidence; no vendor product is canonical (per G-12).

The function contributes to the Commerce & Retail sector outcome: frictionless omnichannel commerce from catalogue to fulfilment.

## 4. Functional Scope
### In Scope
- Commerce & Orders behaviour of the E-Commerce Platform (generic system class)
- Realized by the Catalog Component via the Checkout Service
### Out of Scope
- Workflow coordination across sub-systems (separate concern; the orchestration lives at the ISC layer)
- Cross-domain data persistence (owned by the information and data management domain where applicable)
- Vendor-specific extensions of the corroborating products (not canonical per G-12)

## 5. Behavioural Specification
### Trigger
Invocation within the Commerce & Orders sub-system (request, event or schedule depending on deployment).
### Preconditions
- The executing component is reachable
- The required business objects are present
### Main Behaviour
Executes the 'Analyze order fraud risk' function within the Commerce & Orders sub-system of a E-Commerce Platform. Operating through the Checkout Service and the Catalog Component, it processes information, applies the business logic and rules defined for Commerce & Orders, and contributes to frictionless omnichannel commerce from catalogue to fulfilment. Vendor-neutral record: vendor corroboration (3 distinct vendor systems) is recorded in governance.source_and_evidence; no vendor product is canonical (per G-12).
### Alternative Behaviour
Not applicable to this function.
### Exception Behaviour
- Failure of the executing component produces a structured error response
- Errors are recorded in the sub-system log
### Postconditions
- The function outcome is produced (or a structured error)

## 6. Inputs
Typed inputs are not declared by this vendor-neutral record; the function consumes the business objects named in its definition. The typed input contract is populated via a follow-on CR.

## 7. Outputs
Typed outputs are not declared by this vendor-neutral record; the function produces the outcome named in its definition. The typed output contract is populated via a follow-on CR.

## 8. Data and Event Interaction
### Consumed Data
- (see the definition; typed inputs follow in a follow-on CR)
### Produced Data
- (see the definition; typed outputs follow in a follow-on CR)
### Consumed Events
None declared.
### Produced Events
None declared.

## 9. Composition and Dependencies
### Parent
None (no synthetic F2 parent; grouped by functional domain per G-06).
### Child Functions
None.
### Dependencies
- The executing component (dea:information-system-component-e-commerce-platform-commerce-orders-catalog-component)
- The Checkout Service
### Orchestration
Not applicable to this function. The function is F4 (leaf); orchestration is at the ISC layer.

## 10. Execution Characteristics
Per-record execution characteristics are not asserted by the vendor-neutral tranche; they vary across the corroborating vendor implementations and are recorded per-deployment.

## 11. Business Alignment
Capability and process alignment is not asserted by this tranche; the realizes/enables allocations remain owned by their catalogues per the metamodel relationship contracts (see CR-IS-CAT-01D). See the P4 coverage report for the sector outcome mapping.

## 12. Executing Components

- `dea:information-system-component-e-commerce-platform-commerce-orders-catalog-component`

## 13. Non-Functional Characteristics

| Characteristic | Value |
|---|---|
| Criticality | business-critical (generic tranche-level value; refined per-deployment) |

## 14. Security and Governance

- Functional owner: IS Semantic Architecture programme
- Steward: IS Semantic Architecture programme
- Approval status: proposed
- Criticality: business-critical (generic tranche-level value)
- Vendor evidence: see governance.source_and_evidence in the function record (at least 3 distinct vendor systems; evidence only per G-12)

## 15. Measurement and Observability
### Relevant Metrics
Metric allocation is owned by the Metric catalogue per G-11 (OpenDEAM v0.7.0 measured_by). No metric is asserted by this record.
### Monitoring Expectations
Monitoring expectations are recorded per-deployment.
### Evidence Sources
- The executing component log
- The sub-system audit trail

## 16. Examples and Use Cases

- Use case 1: a standard invocation of Analyze order fraud risk within the Commerce & Orders sub-system
- Use case 2: a high-volume invocation under load with horizontal scaling of the executing component
- Use case 3: an exceptional case (validation failure, dependency unavailability) with the structured error response

## 17. Limitations and Assumptions

- The function depends on the executing component being available
- The record is vendor-neutral: vendor products corroborate the function as evidence only (per G-12)
- No synthetic F2 parent is admitted by this tranche; grouping is by functional domain and the executing_components crawl (per G-06)
- Typed inputs, outputs and execution characteristics follow in a follow-on CR

## 18. References

- `change-requests/CR-IS-CAT-01C-P4-vendor-neutral-corroborated-population.md` (the CR doc)
- `taxonomy/functional-domains.yaml` (the classification layer)
- `schemas/entities/information-system-function.v2.json` (the v2 schema)
- `technehub-labs/dea-catalog-application-components` (the executing component catalogue; CR-IS-CAT-02C-P4)

## 19. Change History

- 2026-11-10: Initial creation (CR-IS-CAT-01C-P4; vendor-neutral corroborated population).
