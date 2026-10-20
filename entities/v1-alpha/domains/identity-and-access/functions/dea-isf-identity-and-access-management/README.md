# Identity and Access Management

## 1. Identity
- Canonical ID: `dea:information-system-function-identity-and-access-management`
- Version: 1.0.0
- Lifecycle: planned
- Functional Domain: ISF-01 Identity and Access (`isf:domain:identity-and-access`)
- Category: ISF-01 Identity and Access
- Decomposition Level: F2 (parent function)
- Parent Function: None (F2 is the top of the identity-and-access sub-tree)

## 2. Definition

The parent function that composes the identity-and-access sub-tree. The function coordinates the registration, verification, authentication, authorization, and lifecycle management of digital identities. It is the F2 parent of eight F4 atomic functions, each with a distinct responsibility.

## 3. Purpose and Responsibility

Responsibility: provide a coherent identity and access management capability for the enterprise. The function composes the F4 children into a single responsibility that is exposed to upstream business processes. The function does NOT orchestrate the F4 children directly; the orchestration pattern is owned by the Information System Component layer.

## 4. Functional Scope

### In Scope
- Compose the 8 F4 atomic functions (identity registration, verification, authentication, authorization, access policy evaluation, session management, identity provisioning, identity deprovisioning) under a single responsibility.
- Expose the composite to upstream business processes.

### Out of Scope
- Orchestration of the F4 children (owned by the ISC orchestration pattern; per the composition vs orchestration distinction in CR-IS-CAT-01B section 3.3).
- Identity federation (separate sub-tree).
- Identity governance (admin policy; separate sub-tree in ISF-11 Configuration and Administration).

## 5. Behavioural Specification

### Trigger
An identity lifecycle event from the HR system (or another authoritative source).

### Preconditions
- All child functions are registered and reachable.
- The audit log is available.

### Main Behaviour
The F2 function is a composition; it does not have its own main behaviour. The main behaviour is the composition of the child functions, orchestrated at the ISC layer. The F2 function emits the union of the children's events and state changes.

### Alternative Behaviour
Not applicable.

### Exception Behaviour
The F2 function inherits the exception behaviour of the child functions. A child failure is recorded against the child; the F2 parent is not directly responsible for the failure recovery.

### Postconditions
- The identity and access state is consistent across the identity store, the session store, and the policy store.
- An audit event is recorded for every state change.

## 6. Inputs

| Input ID | Name | Definition | Source | Required | Sensitivity |
|---|---|---|---|---|---|
| `identity-lifecycle-event` | Identity lifecycle event | A business event that triggers an identity and access flow. | HR system via ISC-HR-001. | Yes | Sensitive |

## 7. Outputs

| Output ID | Name | Definition | Destination | Conditions |
|---|---|---|---|---|
| `identity-and-access-state` | Identity and access state | The state of the identity record, the credentials, the active sessions, and the access policy decisions. | Identity store, audit log, downstream systems. | Updated on every child function execution. |

## 8. Data and Event Interaction

### Consumed Data
- (inherited from the F4 children)

### Produced Data
- (inherited from the F4 children; the F2 record adds the union of state)

### Consumed Events
- (inherited from the F4 children)

### Produced Events
- (inherited from the F4 children)

## 9. Composition and Dependencies

### Parent
None. F2 is the top of the identity-and-access sub-tree.

### Child Functions
1. `dea:information-system-function-identity-registration` (F4)
2. `dea:information-system-function-identity-verification` (F4) [example F4 in this PR]
3. `dea:information-system-function-authentication` (F4)
4. `dea:information-system-function-authorization` (F4)
5. `dea:information-system-function-access-policy-evaluation` (F4)
6. `dea:information-system-function-session-management` (F4)
7. `dea:information-system-function-identity-provisioning` (F4)
8. `dea:information-system-function-identity-deprovisioning` (F4)

### Dependencies
- HR system (ISC-HR-001)
- Identity broker (ISC identity broker)
- Policy decision point (ISC PDP)
- Session store

### Orchestration
The F2 function does NOT orchestrate the child functions. The orchestration is at the ISC layer. Per the composition vs orchestration distinction (CR-IS-CAT-01B section 3.3), composition is structural; orchestration is the coordination of execution. The F2 function records the composition; the ISC layer records the orchestration.

## 10. Execution Characteristics

| Characteristic | Value |
|---|---|
| Execution pattern | Event-driven |
| Trigger mechanism | Event |
| Processing mode | Real-time |
| Idempotency | Idempotent (each child is idempotent) |
| Retry/recovery | Per child function |
| Error handling | Per child function |
| Transactional | No (read-mostly with state changes emitted) |
| Concurrency | Multi-threaded |

## 11. Business Alignment

### Realized Capabilities
- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-security-management-wmzc7c`

### Enabled Processes
- `dea:process-acquire-and-onboard-agents`
- `dea:process-mobilize-licensed-workforce`
- `dea:process-onboard-regulated-party-relationship`

## 12. Executing Components

- `dea:information-system-component-identity-broker`
- `dea:information-system-component-identity-broker`
- `dea:information-system-component-identity-broker-session-store`

## 13. Non-Functional Characteristics

| Characteristic | Value |
|---|---|
| Availability | 99.95% |
| Performance / latency | p99 < 500ms (parent flow) |
| Throughput | 10000 events/s |
| Scalability | Horizontal |
| Resilience | Active-active |
| Security | OAuth2 + mTLS + SAML |
| Privacy | GDPR-compliant |
| Auditability | Full |
| Recoverability | RTO 15m, RPO 5m |
| Observability | Prometheus metrics |
| Compliance constraints | SOX, PCI-DSS, eIDAS, HIPAA |

## 14. Security and Governance

- Functional owner: Identity and Access Management team
- Steward: Architecture team
- Approval status: proposed
- Criticality: mission-critical

## 15. Measurement and Observability

### Relevant Metrics
- Identity lifecycle event rate
- Identity-and-access state change rate
- Per-child-function SLAs (inherited)

### Monitoring Expectations
- Dashboard: identity and access health (event rate, state change rate, child function SLAs)
- Alerts: child function SLA breaches (inherited)

### Evidence Sources
- Per child function (inherited)

## 16. Examples and Use Cases

- Use case 1: New employee is hired. The HR system emits a `new-hire` event. The F2 function composes the F4 children (registration, verification, authentication, provisioning) to onboard the employee.
- Use case 2: Employee changes role. The HR system emits a `role-change` event. The F2 function composes the F4 children (verification, authorization update, provisioning) to update the employee's access.
- Use case 3: Employee leaves. The HR system emits a `termination` event. The F2 function composes the F4 children (deprovisioning, session termination, audit) to remove the employee's access.

## 17. Limitations and Assumptions

- The F2 function depends on the F4 children being available. The availability SLA is the intersection of the children's SLAs.
- The F2 function does not own identity federation; that is a separate sub-tree.
- The F2 function does not own the orchestration pattern; the orchestration is at the ISC layer.

## 18. References

- `technehub-labs/dea-metamodel/change-requests/CR-018-information-system-function.md`
- `technehub-labs/dea-metamodel/change-requests/CR-019-information-system-component.md`
- NIST SP 800-63

## 19. Change History

- 2026-10-18: Initial creation (CR-IS-CAT-01B; example F2 record).
