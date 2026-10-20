# CR-IS-CAT-01R: Cross-Catalogue Reference Integrity Remediation (ISF)

## Status

Authoritative governance correction to the cross-catalogue references in the
`dea-catalog-information-system-functions` catalogue (P1 population + 01D
integration).

## 1. Background

An audit of the ISF P1 population and its 01D relationship registry found
that all cross-catalogue references in `business_alignment.realized_capabilities`,
`business_alignment.enabled_processes`, and `executing_components` use identifiers
that do not exist in the target catalogues. The pre-existing reference-integrity
report claimed `unresolved_references: 0` because its validator only tested
prefix shape; it never resolved against the actual target catalogues.

### 1.1 Affected records and refs

- **P1 records**: 20 functions across 5 domains. 21 cross-catalogue references
  used synthetic ids (6 BC + 7 BP + 8 ISC).
- **01D relationship registry**: 16 records. 8 had synthetic target ids; 6 had
  valid forward refs that were not declared as such.
- **F2 identity-and-access-management child_functions** declared 4 children
  that have no F4 record (3 documented in the 01C coverage report as deferred
  or excluded; 1 undocumented).

### 1.2 Why this is a hard gate

The programme-wide control "evidence before assertion" forbids false assurance
in conformance artefacts. The pre-existing `unresolved_references: 0` claim
was structurally unable to detect any reference it should resolve. Authoring
P2 on top of this defect would triple the remediation debt. The defect
must be corrected before any further population work.

## 2. The corrective slice

1. Rebase every synthetic cross-catalogue reference to a real record id in
   the target catalogue (21 rebases; 21/21 verified to exist against the
   pinned target-repo HEAD).
2. Declare the 6 forward references (data-entity, event, ISS, II, metric)
   in the cross-catalogue reference map so the validator distinguishes
   "declared forward (target repo exists, no record yet)" from "unresolved".
3. Remove the 4 dangling intra-catalog children from
   `dea:information-system-function-identity-and-access-management.child_functions`,
   with each disposition documented in the reference map.
4. Hardened `report_reference_integrity` to resolve against vendored
   target-id snapshots (29 BC, 139 BP, 38 ISC at pinned commits).
5. Hardened CI step 8 in `.github/workflows/validate-catalogue.yml` to
   fail when `unresolved_count > 0`. Forward refs are allowed.
6. Added `scripts/build_target_snapshots.py` (deterministic regenerator
   for the vendored snapshots).
7. Updated `scripts/generate_p1_population.py` to emit canonical ids, so
   re-running the generator does not regress the rebasings.

## 3. Rebasing map (21 entries)

| Legacy synthetic id | Canonical target id | Target catalogue |
|---|---|---|
| `dea:business-capability-access-control` | `capabilities:capability-security-management-wmzc7c` | `dea-catalog-business-capabilities` |
| `dea:business-capability-identity-assurance` | `capabilities:capability-security-management-wmzc7c` | `dea-catalog-business-capabilities` |
| `dea:business-capability-data-management` | `capabilities:capability-information-management-6vjgdh` | `dea-catalog-business-capabilities` |
| `dea:business-capability-integration` | `capabilities:capability-technology-enablement-y6nkws` | `dea-catalog-business-capabilities` |
| `dea:business-capability-transaction-processing` | `capabilities:capability-financial-resource-management-cd3c7c` | `dea-catalog-business-capabilities` |
| `dea:business-capability-workflow-coordination` | `capabilities:capability-operations-management-pm3w8k` | `dea-catalog-business-capabilities` |
| `dea:business-process-onboarding-authenticated-individual` | `dea:process-acquire-and-onboard-agents` | `dea-catalog-processes` |
| `dea:business-process-employee-lifecycle` | `dea:process-mobilize-licensed-workforce` | `dea-catalog-processes` |
| `dea:business-process-financial-transaction` | `dea:process-run-accounts-receivable` | `dea-catalog-processes` |
| `dea:business-process-integration-execution` | `dea:process-operate-technology-platforms` | `dea-catalog-processes` |
| `dea:business-process-data-lifecycle` | `dea:process-operate-general-ledger` | `dea-catalog-processes` |
| `dea:business-process-third-party-onboarding` | `dea:process-onboard-regulated-party-relationship` | `dea-catalog-processes` |
| `dea:business-process-workflow-execution` | `dea:process-operate-service-delivery` | `dea-catalog-processes` |
| `dea:information-system-component-identity-broker` | unchanged (canonical) | `dea-catalog-application-components` |
| `dea:information-system-component-api-gateway` | unchanged (canonical) | `dea-catalog-application-components` |
| `dea:information-system-component-policy-decision-point` | `dea:information-system-component-identity-broker` | `dea-catalog-application-components` |
| `dea:information-system-component-session-store` | `dea:information-system-component-identity-broker-session-store` | `dea-catalog-application-components` |
| `dea:information-system-component-data-platform` | `dea:information-system-component-data-warehouse-platform` | `dea-catalog-application-components` |
| `dea:information-system-component-message-broker` | `dea:information-system-component-api-gateway-router` | `dea-catalog-application-components` |
| `dea:information-system-component-transaction-engine` | `dea:information-system-component-order-management-system` | `dea-catalog-application-components` |
| `dea:information-system-component-workflow-engine` | `dea:information-system-component-order-management-orchestrator` | `dea-catalog-application-components` |

## 4. Forward references (6)

| Legacy target id | Target catalogue | Owning CR |
|---|---|---|
| `dea:data-entity-identity-claim` | `dea-catalog-business-objects` | data-entity CR (deferred) |
| `dea:data-entity-verification-result` | `dea-catalog-business-objects` | data-entity CR (deferred) |
| `dea:event-identity-verified` | `dea-catalog-business-objects` | event catalogue CR (deferred) |
| `dea:information-system-service-identity-service` | `dea-catalog-information-system-services` | CR-IS-CAT-03 (ISS 5-CR programme) |
| `dea:integration-interface-identity-api` | `dea-catalog-integration-interfaces` | CR-IS-CAT-04 (II 5-CR programme) |
| `dea:metric-verification-latency` | `dea-catalog-metrics` | metric catalogue CR (deferred) |

## 5. Intra-catalog dangling children (F2 identity-and-access-management)

The F2 `dea:information-system-function-identity-and-access-management`
declared 8 children in its `child_functions`; the matching F4 records do not
exist for 4 of them. Their disposition follows the 01C coverage report
(deferred/excluded disposition) and is recorded in the cross-catalogue
reference map.

| Removed child | Disposition rationale |
|---|---|
| `authorization` | Not in 01C deferred/excluded lists. Deferred to ISF-09 Security Privacy and Trust (P3 candidate). |
| `session-management` | 01C coverage report: "will be a separate F4 in a follow-up CR". |
| `identity-provisioning` | 01C coverage report: "will be separate F4 records in a follow-up CR". |
| `identity-deprovisioning` | 01C coverage report: "will be separate F4 records in a follow-up CR". |

## 6. Hardened validator behaviour

The reference-integrity report now distinguishes three buckets:

- **resolved** -- target id exists in a vendored target-id snapshot pinned
  to a specific commit.
- **forward** -- target repo is named and the target repo exists; the target
  record is admitted by a named future CR. These are NOT failures.
- **unresolved** -- everything else. Hard-fail in CI.

The vendored snapshots come from `docs/is-semantic-architecture/target-id-snapshots.yaml`,
generated by `scripts/build_target_snapshots.py`. CI does not fetch;
it consumes the vendored snapshot so reference-integrity is deterministic
and offline-safe.

## 7. Files

- Added: `docs/is-semantic-architecture/cross-catalogue-reference-map.yaml` (authoritative rebasing + forward + dangling dispositions)
- Added: `docs/is-semantic-architecture/target-id-snapshots.yaml` (vendored target ids at pinned commits; deterministic CI input)
- Added: `scripts/build_target_snapshots.py` (regenerator for the snapshots)
- Patched: `entities/v1-alpha/domains/identity-and-access/functions/dea-isf-identity-and-access-management/function.yaml` (canonical refs + 4 dangling children removed + rationale noted)
- Patched: `entities/v1-alpha/domains/identity-and-access/functions/dea-isf-identity-verification/function.yaml` (canonical refs)
- Patched: `scripts/generate_p1_population.py` (synthetic literals replaced + F2 dangling children list fixed)
- Patched: `relationships/v1-alpha/relationships.yaml` (forward refs marked)
- Patched: `scripts/generate_conformance_reports.py` (real resolution, 3-bucket report)
- Patched: `.github/workflows/validate-catalogue.yml` (Step 8: hard-fail on unresolved)
- Regenerated: `entities/v1-alpha/**/function.yaml` (15 F4 records) + per-domain `index.yaml` (5) + catalog `index.yaml`
- Regenerated: `reports/{catalogue-conformance,relationship-coverage,reference-integrity,taxonomy-coverage,documentation-coverage}.yaml`

## 8. Reference-integrity report (post-PR)

| Bucket | Count |
|---|---|
| total classified | 98 |
| resolved | 92 |
| forward | 6 |
| unresolved | 0 |

## 9. Companion slices (next, not in this CR)

- `CR-IS-CAT-02E` in `dea-catalog-application-components`: equivalent remediation
  for the ISC catalogue's 5 dangling ISF references. The ISC-side ISF targets
  resolve as ISF P2/P3 lands.
- `CR-IS-CAT-01C-P2`: ISF P2 population (6 domains). Unblocked by this CR.
- `CR-013 (dea-governance)`: portfolio-level reference-resolution policy
  formalised in this same shape (3 buckets + vendored snapshot + hard CI).

## 10. Governance basis

- EGV-006 (references resolve to valid entities within the declared identity scope).
- CR-012 (cross-catalogue references resolve to authoritative entities).
- CR-IS-CAT-01B documentation rule 12.
- Programme-wide control: evidence before assertion.
