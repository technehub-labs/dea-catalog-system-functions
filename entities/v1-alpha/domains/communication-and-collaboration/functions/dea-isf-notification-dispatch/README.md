# Notification Dispatch

## 1. Identity
- Canonical ID: `dea:information-system-function-notification-dispatch`
- Version: 1.0.0
- Lifecycle: planned
- Functional Domain: ISF-06 Communication and Collaboration (`isf:domain:communication-and-collaboration`)
- Category: ISF-06 Communication and Collaboration (categories populated in CR-IS-CAT-01B; v1.0 has no categories yet)
- Decomposition Level: F4
- Parent Function: dea:information-system-function-communication-and-collaboration

## 2. Definition

The atomic function that delivers a notification (transactional, scheduled, or event-driven) to a recipient across the appropriate channel.

## 3. Purpose and Responsibility

Responsibility: The atomic function that delivers a notification (transactional, scheduled, or event-driven) to a recipient across the appropriate channel.

## 4. Functional Scope
### In Scope
- Notification payload; Recipient policy (inputs)
- Delivered notification (outputs)

### Out of Scope
- Workflow coordination (separate domain: ISF-04)
- Data persistence (separate domain: ISF-02 if cross-domain; otherwise child of this domain)
- Identity and access (separate domain: ISF-01)

## 5. Behavioural Specification
### Trigger
api-call (synchronous)

### Preconditions
- All required inputs are present
- The executing component is reachable
- The audit log is available

### Main Behaviour
The atomic function that delivers a notification (transactional, scheduled, or event-driven) to a recipient across the appropriate channel.

### Alternative Behaviour
Not applicable to this function.

### Exception Behaviour
- Failure of the executing component produces a structured error response
- The audit log records every error

### Postconditions
- The output is produced (or an error response)
- An audit event is recorded

## 6. Inputs

| Input ID | Name | Definition | Source | Required | Sensitivity |
|---|---|---|---|---|---|
| `notification-payload` | Notification payload | The notification payload (subject, body, recipient, channel). | Caller. | Yes | sensitive |
| `recipient-policy` | Recipient policy | The recipient routing and preference policy. | Policy store. | Yes | non-sensitive |

## 7. Outputs

| Output ID | Name | Definition | Destination | Conditions |
|---|---|---|---|---|
| `delivered-notification` | Delivered notification | A delivered-notification record with the channel, timestamp, and delivery evidence. | Notification store, audit log. | Always produced (or an error response). |

## 8. Data and Event Interaction
### Consumed Data
- (see inputs above)

### Produced Data
- (see outputs above)

### Consumed Events
None.

### Produced Events
- `dea:event-information-system-function-notification-dispatch-completed` (on success)
- `dea:event-information-system-function-notification-dispatch-failed` (on failure)

## 9. Composition and Dependencies
### Parent
dea:information-system-function-communication-and-collaboration

### Child Functions
None.

### Dependencies
- The executing component(s)
- The audit log

### Orchestration
Not applicable to this function. The function is F4 (leaf); orchestration is at the ISC layer.

## 10. Execution Characteristics

| Characteristic | Value |
|---|---|
| Execution pattern | synchronous |
| Trigger mechanism | api-call |
| Processing mode | real-time |
| Idempotency | idempotent |
| Transactional | True |
| Concurrency | multi-threaded |

## 11. Business Alignment
### Realized Capabilities
- `capabilities:capability-workforce-management-9e8d8s`

### Enabled Processes
- `dea:process-coordinate-collaboration`

## 12. Executing Components

- `dea:information-system-component-employee-portal-platform`
- `dea:information-system-component-api-gateway`

## 13. Non-Functional Characteristics

| Characteristic | Value |
|---|---|
| Criticality | mission-critical |

## 14. Security and Governance

- Functional owner: Architecture team
- Steward: Architecture team
- Approval status: proposed
- Criticality: mission-critical

## 15. Measurement and Observability
### Relevant Metrics
- Request rate
- Success rate
- Latency (p50, p95, p99)
- Error rate

### Monitoring Expectations
- Dashboard: Notification Dispatch health (request rate, success rate, latency, error rate)
- Alerts: error rate > 1% for 5m; p99 latency exceeded for 10m

### Evidence Sources
- Request log
- Response log
- Audit event stream

## 16. Examples and Use Cases

- Use case 1: a standard invocation by a caller via the API gateway
- Use case 2: a high-volume invocation under load with horizontal scaling
- Use case 3: an exceptional case (timeout, validation failure) with the error response

## 17. Limitations and Assumptions

- The function depends on the executing component being available
- The function does not own identity (separate domain: ISF-01)
- The function does not own the persistence of the output (the caller persists if needed)

## 18. References

- `technehub-labs/dea-metamodel/change-requests/CR-018-information-system-function.md`
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01B-decomposition.md`
- `technehub-labs/dea-catalog-system-functions/change-requests/CR-IS-CAT-01A-taxonomy.md`

## 19. Change History

- 2026-10-18: Initial creation (CR-IS-CAT-01C; P1 population).
