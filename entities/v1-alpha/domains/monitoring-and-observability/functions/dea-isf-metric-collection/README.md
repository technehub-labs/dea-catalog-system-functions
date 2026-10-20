# Metric Collection

## 1. Identity
- Canonical ID: `dea:information-system-function-metric-collection`
- Version: 1.0.0
- Lifecycle: planned
- Functional Domain: ISF-10 Monitoring and Observability (`isf:domain:monitoring-and-observability`)
- Category: ISF-10 Monitoring and Observability (categories populated in CR-IS-CAT-01B; v1.0 has no categories yet)
- Decomposition Level: F4
- Parent Function: dea:information-system-function-monitoring-and-observability

## 2. Definition

The atomic function that samples a runtime metric (counter, gauge, histogram) at the configured cadence and produces a metric data-point.

## 3. Purpose and Responsibility

Responsibility: The atomic function that samples a runtime metric (counter, gauge, histogram) at the configured cadence and produces a metric data-point.

## 4. Functional Scope
### In Scope
- Metric source; Sampling policy (inputs)
- Metric data point (outputs)

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
The atomic function that samples a runtime metric (counter, gauge, histogram) at the configured cadence and produces a metric data-point.

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
| `metric-source` | Metric source | A runtime source for a metric (counter, gauge, histogram). | Runtime instrumentation. | Yes | non-sensitive |
| `sampling-policy` | Sampling policy | The sampling cadence and aggregation rule. | Policy store. | Yes | non-sensitive |

## 7. Outputs

| Output ID | Name | Definition | Destination | Conditions |
|---|---|---|---|---|
| `metric-data-point` | Metric data point | A metric data-point with timestamp, labels, and value. | Metric store. | Always produced (or an error response). |

## 8. Data and Event Interaction
### Consumed Data
- (see inputs above)

### Produced Data
- (see outputs above)

### Consumed Events
None.

### Produced Events
- `dea:event-information-system-function-metric-collection-completed` (on success)
- `dea:event-information-system-function-metric-collection-failed` (on failure)

## 9. Composition and Dependencies
### Parent
dea:information-system-function-monitoring-and-observability

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
- `capabilities:capability-continuity-management-v3rn6u`

### Enabled Processes
- `dea:process-operate-technology-platforms`

## 12. Executing Components

- `dea:information-system-component-observability-platform`
- `dea:information-system-component-metrics-collector`

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
- Dashboard: Metric Collection health (request rate, success rate, latency, error rate)
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
