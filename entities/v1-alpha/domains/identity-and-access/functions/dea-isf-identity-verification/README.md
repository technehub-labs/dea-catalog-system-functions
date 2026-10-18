# Identity Verification

## 1. Identity
- Canonical ID: `dea:information-system-function-identity-verification`
- Version: 1.0.0
- Lifecycle: planned
- Functional Domain: ISF-01 Identity and Access (`isf:domain:identity-and-access`)
- Category: ISF-01 Identity and Access (categories populated in CR-IS-CAT-01B; v1.0 has no categories yet)
- Decomposition Level: F4 (atomic function)
- Parent Function: `dea:information-system-function-identity-and-access-management`

## 2. Definition

The atomic function that verifies a claimed identity against authoritative evidence. Identity verification is the leaf of the identity-and-access domain that produces a verification decision (verified, not-verified, or inconclusive).

## 3. Purpose and Responsibility

Responsibility: produce a verification decision for a claimed identity by consulting authoritative evidence under a verification policy. The function does NOT register identities (that is `dea:information-system-function-identity-registration`); does NOT authenticate the principal after verification (that is `dea:information-system-function-authentication`); does NOT enforce access policy (that is `dea:information-system-function-access-policy-evaluation`).

## 4. Functional Scope

### In Scope
- Accept a claimed identity (a set of identity attributes) and a verification policy.
- Consult the evidence types permitted by the policy.
- Produce a verification decision (verified, not-verified, inconclusive).
- Emit an audit event for every decision.

### Out of Scope
- Identity registration (separate function: `dea:information-system-function-identity-registration`).
- Authentication (separate function: `dea:information-system-function-authentication`).
- Access policy evaluation (separate function: `dea:information-system-function-access-policy-evaluation`).
- Persistence of the verification result (the result is emitted to the caller; the caller decides whether to persist it).
- Federation of identity (separate function in the identity federation sub-tree).

## 5. Behavioural Specification

### Trigger
An API call from a caller presenting a claimed identity and a verification policy.

### Preconditions
- The claimed identity MUST contain all required identity attributes.
- The verification policy MUST be signed and within its validity period.
- The evidence store MUST be reachable.

### Main Behaviour
1. Validate the claimed identity attributes against their format constraints.
2. Load the verification policy and resolve the acceptable evidence types.
3. For each acceptable evidence type, query the evidence store.
4. Combine the evidence per the policy's combination rule.
5. Produce the verification decision: `verified` (all required evidence matches), `not-verified` (at least one required evidence fails), `inconclusive` (at least one evidence type is unreachable).
6. Emit the verification result to the caller.
7. Emit an audit event with the decision, the evidence consulted, and the policy version.

### Alternative Behaviour
If the policy permits multiple evidence combination strategies (e.g., MFA combinations), the function selects the strongest combination available.

### Exception Behaviour
- If the claimed identity fails format validation, the function returns `not-verified` with a structured error.
- If the policy is invalid or expired, the function returns an error (HTTP 503) and emits an audit event.
- If the evidence store is unreachable for one or more types, the function returns `inconclusive` (if at least one required type is reachable) or an error (if no required type is reachable).

### Postconditions
- A verification result is emitted to the caller.
- An audit event is recorded.

## 6. Inputs

| Input ID | Name | Definition | Source | Required | Sensitivity |
|---|---|---|---|---|---|
| `claimed-identity` | Claimed identity | The set of identity attributes the principal asserts. | Caller (via the ISC API; CR-021 specifies relationship). | Yes | Sensitive |
| `verification-policy` | Verification policy | The rules for which evidence types are acceptable. | Policy store (read-only). | Yes | Non-sensitive |

## 7. Outputs

| Output ID | Name | Definition | Destination | Conditions |
|---|---|---|---|---|
| `verification-result` | Verification result | The decision (verified, not-verified, inconclusive) with the evidence consulted and the policy version. | Caller. | Always produced. |

## 8. Data and Event Interaction

### Consumed Data
- `dea:data-entity-identity-claim`
- `dea:data-entity-verification-policy`
- (per evidence type, the corresponding `dea:data-entity-evidence-*` records)

### Produced Data
- `dea:data-entity-verification-result`

### Consumed Events
None.

### Produced Events
- `dea:event-identity-verified` (when the decision is `verified`)
- `dea:event-identity-not-verified` (when the decision is `not-verified`)
- `dea:event-identity-verification-inconclusive` (when the decision is `inconclusive`)

## 9. Composition and Dependencies

### Parent
- `dea:information-system-function-identity-and-access-management` (F2 parent).

### Child Functions
None. F4 is a leaf in the decomposition hierarchy.

### Dependencies
- The evidence store (a data entity catalogue dependency; not a function dependency).
- The policy store (same).
- The audit event stream (CR-IS-CAT-01D's concern).

### Orchestration
Not applicable to this function. The function does not orchestrate child functions; it is atomic.

## 10. Execution Characteristics

| Characteristic | Value |
|---|---|
| Execution pattern | Synchronous |
| Trigger mechanism | API call |
| Processing mode | Real-time |
| Idempotency | Idempotent (caller may retry on transient errors) |
| Retry/recovery | Exponential backoff (caller-side) |
| Error handling | Inconclusive on evidence failure; error on policy failure |
| Transactional | No (the function is read-mostly; the result is emitted to the caller) |
| Concurrency | Multi-threaded |

## 11. Business Alignment

### Realized Capabilities
- `dea:business-capability-identity-assurance`

### Enabled Processes
- `dea:business-process-onboarding-authenticated-individual`

## 12. Executing Components

- `dea:information-system-component-identity-broker` (the canonical identity broker component for the enterprise)

## 13. Non-Functional Characteristics

| Characteristic | Value |
|---|---|
| Availability | 99.95% |
| Performance / latency | p99 < 200ms |
| Throughput | 5000 req/s |
| Scalability | Horizontal |
| Resilience | Active-active |
| Security | OAuth2 + mTLS |
| Privacy | GDPR-compliant |
| Auditability | Full |
| Recoverability | RTO 15m, RPO 5m |
| Observability | Prometheus metrics |
| Compliance constraints | SOX, PCI-DSS, eIDAS |

## 14. Security and Governance

- Functional owner: Identity and Access Management team
- Steward: Architecture team
- Approval status: proposed
- Criticality: mission-critical

## 15. Measurement and Observability

### Relevant Metrics
- Verification request rate
- Verification success rate (per evidence type)
- Verification latency (p50, p95, p99)
- Inconclusive rate (per evidence type)
- Error rate (policy failure, evidence store failure)

### Monitoring Expectations
- Dashboard: identity verification health (request rate, success rate, latency, inconclusive rate, error rate)
- Alerts: error rate > 1% for 5m; p99 latency > 500ms for 10m

### Evidence Sources
- Verification request log (structured)
- Verification result log (structured)
- Audit event stream

## 16. Examples and Use Cases

- Use case 1: User signs in to a portal with username and password. The portal calls the identity broker's verification function. The broker verifies the password against the credential store and returns `verified`.
- Use case 2: User attempts a high-value transaction. The transaction service calls the identity broker's verification function with a step-up evidence policy. The broker consults MFA evidence and returns `verified` if the second factor is present.
- Use case 3: A government agency verifies a national ID number against a national identity register. The function returns `verified` or `not-verified` based on the register's response.

## 17. Limitations and Assumptions

- The function does NOT verify the authenticity of the evidence store; that is the responsibility of the platform team.
- The function does NOT handle identity federation (cross-domain identity); that is a separate function in the identity federation sub-tree.
- The function assumes the verification policy is up-to-date; stale policies are the platform team's responsibility.

## 18. References

- `technehub-labs/dea-metamodel/change-requests/CR-018-information-system-function.md`
- `technehub-labs/dea-metamodel/change-requests/CR-021-integration-interface.md`
- NIST SP 800-63A (identity assurance)
- `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md` (the 5-CR programme source)

## 19. Change History

- 2026-10-18: Initial creation (CR-IS-CAT-01B; example F4 record).
