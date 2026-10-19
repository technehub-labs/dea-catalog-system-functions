# Data Transformation

## 1. Identity
- Canonical ID: `dea:information-system-function-data-transformation`
- Version: 1.0.0
- Lifecycle: planned
- Functional Domain: ISF-02 Information and Data Management (`isf:domain:information-and-data-management`)
- Category: ISF-02 Information and Data Management (categories populated in CR-IS-CAT-01B; v1.0 has no categories yet)
- Decomposition Level: F4
- Parent Function: dea:information-system-function-data-management

## 2. Definition

The atomic function that transforms data from one schema or shape to another. Transformation includes normalization, enrichment, aggregation and projection.

## 3. Purpose and Responsibility

Responsibility: The atomic function that transforms data from one schema or shape to another. Transformation includes normalization, enrichment, aggregation and projection.

## 4. Functional Scope
### In Scope
- Input record; Transformation specification (inputs)
- Output record (outputs)

### Out of Scope
- Workflow coordination (separate domain: ISF-04)
- Data persistence (separate domain: ISF-02 if cross-domain; otherwise child of this domain)
- Identity and access (separate domain: ISF-01)

## 5. Behavioural Specification
### Trigger
schedule (batch)

### Preconditions
- All required inputs are present
- The executing component is reachable
- The audit log is available

### Main Behaviour
The atomic function that transforms data from one schema or shape to another. Transformation includes normalization, enrichment, aggregation and projection.

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
| `input-record` | Input record | A record in the source schema. | Data acquisition pipeline. | Yes | sensitive |
| `transformation-spec` | Transformation specification | The mapping rules, expressions and filters for the transformation. | Transformation spec registry. | Yes | non-sensitive |

## 7. Outputs

| Output ID | Name | Definition | Destination | Conditions |
|---|---|---|---|---|
| `output-record` | Output record | A record in the target schema. | Downstream pipeline or data store. | Always produced (or an error response). |

## 8. Data and Event Interaction
### Consumed Data
- (see inputs above)

### Produced Data
- (see outputs above)

### Consumed Events
None.

### Produced Events
- `dea:event-information-system-function-data-transformation-completed` (on success)
- `dea:event-information-system-function-data-transformation-failed` (on failure)

## 9. Composition and Dependencies
### Parent
dea:information-system-function-data-management

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
| Execution pattern | batch |
| Trigger mechanism | schedule |
| Processing mode | near-real-time |
| Idempotency | idempotent |
| Transactional | True |
| Concurrency | multi-threaded |

## 11. Business Alignment
### Realized Capabilities
- `capabilities:capability-information-management-6vjgdh`

### Enabled Processes
- `dea:process-operate-general-ledger`

## 12. Executing Components

- `dea:information-system-component-data-warehouse-platform`

## 13. Non-Functional Characteristics

| Characteristic | Value |
|---|---|
| Criticality | business-critical |

## 14. Security and Governance

- Functional owner: Architecture team
- Steward: Architecture team
- Approval status: proposed
- Criticality: business-critical

## 15. Measurement and Observability
### Relevant Metrics
- Request rate
- Success rate
- Latency (p50, p95, p99)
- Error rate

### Monitoring Expectations
- Dashboard: Data Transformation health (request rate, success rate, latency, error rate)
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
