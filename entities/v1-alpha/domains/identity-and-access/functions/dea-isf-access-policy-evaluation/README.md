# Access Policy Evaluation

## 1. Identity
- Canonical ID: `dea:information-system-function-access-policy-evaluation`
- Version: 1.0.0
- Lifecycle: planned
- Functional Domain: ISF-01 Identity and Access (`isf:domain:identity-and-access`)
- Category: ISF-01 Identity and Access (categories populated in CR-IS-CAT-01B; v1.0 has no categories yet)
- Decomposition Level: F4
- Parent Function: dea:information-system-function-identity-and-access-management

## 2. Definition

The atomic function that evaluates an access policy against a request: collects the attributes (subject, resource, action, environment), resolves the policy, and produces the allow/deny decision.

## 3. Purpose and Responsibility

Responsibility: The atomic function that evaluates an access policy against a request: collects the attributes (subject, resource, action, environment), resolves the policy, and produces the allow/deny decision.

## 4. Functional Scope
### In Scope
- Access request (inputs)
- Access decision (outputs)

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
The atomic function that evaluates an access policy against a request: collects the attributes (subject, resource, action, environment), resolves the policy, and produces the allow/deny decision.

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
| `access-request` | Access request | An access request: subject (who), resource (what), action (read/write/delete), environment (time, location, device). | Caller (the application service). | Yes | sensitive |

## 7. Outputs

| Output ID | Name | Definition | Destination | Conditions |
|---|---|---|---|---|
| `access-decision` | Access decision | The access decision: allow, deny, or not-applicable, with the policy version and the evidence (which rules fired). | Caller, audit log. | Always produced. |

## 8. Data and Event Interaction
### Consumed Data
- (see inputs above)

### Produced Data
- (see outputs above)

### Consumed Events
None.

### Produced Events
- `dea:event-information-system-function-access-policy-evaluation-completed` (on success)
- `dea:event-information-system-function-access-policy-evaluation-failed` (on failure)

## 9. Composition and Dependencies
### Parent
dea:information-system-function-identity-and-access-management

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
| Transactional | False |
| Concurrency | multi-threaded |

## 11. Business Alignment
### Realized Capabilities
- `capabilities:capability-security-management-wmzc7c`

### Enabled Processes
- `dea:process-acquire-and-onboard-agents`

## 12. Executing Components

- `dea:information-system-component-identity-broker`

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
- Dashboard: Access Policy Evaluation health (request rate, success rate, latency, error rate)
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
