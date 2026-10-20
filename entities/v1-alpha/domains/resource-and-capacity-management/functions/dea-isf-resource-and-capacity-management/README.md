# Resource and Capacity Management

## 1. Identity

- Canonical ID: `dea:information-system-function-resource-and-capacity-management`
- Version: 1.0.0
- Lifecycle: planned
- Functional Domain: ISF-12 Resource and Capacity Management (`isf:domain:resource-and-capacity-management`)
- Category: ISF-12 Resource and Capacity Management
- Decomposition Level: F2 (parent function)
- Parent Function: None (F2 is the top of the resource-and-capacity-management sub-tree)

## 2. Definition

The parent function that composes the resource-and-capacity-management sub-tree. It exposes a composite view of the F4 children below.

## 3. Purpose and Responsibility

Responsibility: provide a coherent resource and capacity management capability for the enterprise. The function composes the F4 children into a single responsibility that is exposed to upstream business processes.

## 4. Functional Scope

### In Scope
- Compose the 2 F4 atomic functions under a single responsibility.
- Expose the composite to upstream business processes.

### Out of Scope
- Orchestration of the F4 children (owned by the ISC orchestration pattern; per CR-IS-CAT-01B section 3.3).

## 5. Behavioural Specification

### Trigger
A business event that triggers the resource-and-capacity-management flow.

### Preconditions
- All F4 children are registered and reachable.
- The audit log is available.

### Main Behaviour
The F2 function is a composition; it does not have its own main behaviour. The main behaviour is the composition of the child functions, orchestrated at the ISC layer.

### Alternative Behaviour
Not applicable.

### Exception Behaviour
The F2 function inherits the exception behaviour of the child functions. A child failure is recorded against the child.

### Postconditions
- The resource-and-capacity-management state is consistent.
- An audit event is recorded for every state change.

## 6. Inputs

The F2 parent composes inputs from its F4 children. Per-domain input specifications are in the F4 records.

## 7. Outputs

The F2 parent composes outputs from its F4 children.

## 8. Data and Event Interaction

- Consumed Data: composed from F4 children.
- Produced Data: composed from F4 children.
- Consumed Events: composed from F4 children.
- Produced Events: composed from F4 children.

## 9. Composition and Dependencies

### Parent
None (F2 is the parent of the resource-and-capacity-management sub-tree).

### Child Functions

- `dea:information-system-function-capacity-planning`
- `dea:information-system-function-resource-provisioning`

## 10. Execution Characteristics

- Execution Pattern: event-driven
- Trigger Mechanism: event
- Processing Mode: real-time
- Synchronous/Asynchronous: asynchronous
- Idempotency: idempotent (each child function is idempotent)
- Retry/Recovery: Each child function is idempotent; the parent flow is retry-safe.
- Error Handling: Each child function emits a structured error; the parent flow records the error.
- Transactional: false
- Concurrency: multi-threaded

## 11. Business Alignment

The realised capabilities and enabled processes of the F2 are the union of the children's. See the F4 records for the per-capability and per-process references.

## 12. Executing Components

- `dea:information-system-component-observability-platform`
- `dea:information-system-component-development-platform`
- `dea:information-system-component-ci-cd-pipeline`

## 13. Non-Functional Characteristics

- Availability: 99.95%
- Performance Latency: p99 < 200ms (composed from F4 children)
- Throughput: composed from F4 children
- Scalability: horizontal
- Resilience: active-active
- Security: composed from F4 children
- Privacy: composed from F4 children
- Auditability: full
- Recoverability: RTO 15m, RPO 5m
- Observability: prometheus-metrics
- Compliance Constraints: per F4 child

## 14. Security and Governance

- Functional owner: Resource and Capacity Management team
- Steward: Architecture team
- Approval status: proposed
- Criticality: mission-critical
- Review date: 2027-10-19
- Change history: see CHANGELOG.md

## 15. Measurement and Observability

Composed from F4 children.

## 16. Examples and Use Cases

See the F4 records for atomic use cases.

## 17. Limitations and Assumptions

The F2 function does not orchestrate the F4 children. The composition is exposed to the ISC layer.

## 18. References

- CR-IS-CAT-01A section 5 (taxonomy classification).
- CR-IS-CAT-01B section 3 (composition vs orchestration).
- CR-IS-CAT-01C-P3 P3 population brief.

## 19. Change History

- 2026-10-19: CR-IS-CAT-01C-P3 initial P3 population.
- 2026-10-19: CR-IS-CAT-01C-P2H F2 record shape parity (canonical P1 F2 shape).
