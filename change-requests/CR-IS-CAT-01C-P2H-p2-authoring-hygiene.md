# CR-IS-CAT-01C-P2H: P2 Authoring Hygiene (F2 Record Shape Parity)

## Status

Quality-of-life slice on top of `CR-IS-CAT-01C-P2`. Brings the 6 P2 F2 records
to the same shape as the P1 F2 (`dea:information-system-function-identity-and-access-management`,
the hand-edited example in `CR-IS-CAT-01B` and the canonical F2 record in
this catalogue).

## 1. The gap

`scripts/generate_p2_population.py` produced F2 records with three classes
of post-hoc defects:
1. `responsibility_allocation` was emitted as a string ("Atomic responsibilities live in the F4 records...")
   not an array of `{child, responsibility}` objects. Schema validation rejected this.
2. `inputs`, `outputs`, `business_alignment.realized_capabilities`,
   `business_alignment.enabled_processes`, `executing_components`,
   `non_functional_characteristics`, `governance.review_date`, `governance.source_and_evidence`,
   `governance.change_history`, `metadata` were all empty or stub values.
3. `execution_characteristics` was emitted in the F4 form (not the F2 form
   `execution_pattern / trigger_mechanism / processing_mode / synchronous_asynchronous / ...`).

These were caught by CI step "entities" (F2 schemas rejected; 6 functions
failed validation). Each was patched by hand in commit `7c2dad3` and the
README 19-section template was hand-rendered in commit `1ee979f`. **The hand-patches
are the wrong way to land a shape-parity correction; the generator itself
must emit the canonical shape so re-running the generator does not regress.**

## 2. The corrective slice

1. **`scripts/generate_p2_population.py` refactored**: a single helper
   `build_f2_record(domain, f4_records)` composes the canonical F2 record
   shape from the domain definition plus the freshly-emitted F4 records.
   - `inputs` / `outputs` -- a single composite input/output that fires the F2
     and delegates to F4 children, with the same schema as a P1 F2.
   - `business_alignment.realized_capabilities` -- the union of the F4
     children's realized_capabilities.
   - `business_alignment.enabled_processes` -- the union of the F4 children's
     enabled_processes.
   - `executing_components` -- the union of the F4 children's executing_components.
   - `non_functional_characteristics` -- the full 11-key set with sensible
     defaults (99.95% availability, p99 < 200ms, etc.).
   - `governance` -- functional_owner, steward, approval_status, criticality,
     review_date (2027-10-19), source_and_evidence (textual chain to
     CR-IS-CAT-01A section 5 + CR-IS-CAT-01C-P2), change_history.
   - `metadata` -- cr, created_by (the generator), created_date, last_modified, notes.
   - `responsibility_allocation` -- array of `{child, responsibility}` objects.
   - `orchestration_responsibility` -- the standard CR-IS-CAT-01B section 3.3
     statement.

2. **`scripts/validate_f2_record_shape.py` added**: scans every F2 record in
   the catalogue and asserts shape parity. This validator is runnable
   locally and is intended for CI integration.

3. **Re-emitted 6 P2 F2 records**: the generator was re-run on this branch;
   the new records have identical canonical shape to the P1 F2. The F4
   records are unchanged.

## 3. Validator outcome (post-regeneration)

- 11 F2 records total checked (1 P1 hand-edited + 6 P2 emitted + 4 P1 generator-emitted).
- 6 P2 F2 records: PASS.
- 4 P1 F2 records (`data-management`, `transaction-processing`,
  `workflow-orchestration`, `integration-and-interoperability`): FAIL — same
  shape deficiencies as the original P2 F2 records had.
- 1 P1 F2 record (`identity-and-access-management`): PASS — the canonical
  reference shape.

The 4 P1 F2 generator-emitted records require their own hygiene slice
(`CR-IS-CAT-01C-P1H`); out of scope for this CR.

## 4. Reusability for P3

The P2 generator's `build_f2_record()` is the template for P3:
`scripts/generate_p3_population.py` will reuse the helper, plus a
`F3_DOMAINS` data block. The F2 record shape is now established, and
P3 emits records consistent with P1 hand-edits.

## 5. Reference-integrity (post-hygiene)

The composite F2 records contribute new resolved refs to the
reference-integrity report:

| Bucket | Before P2H | After P2H |
|---|---:|---:|
| total classified | 206 | **237** |
| resolved | 200 | **231** |
| forward | 6 | 6 |
| unresolved | 0 | 0 |

The 31 additional resolved references come from the F2 records' composed
`business_alignment` (5 records * 2 realized_capabilities unique ~2 each =
~6 new), `business_alignment.enabled_processes` (~12 new) and
`executing_components` (~12 new). All resolve against the existing
target-id snapshots.

## 6. Files

- **Modified**: `scripts/generate_p2_population.py` (refactored F2 emit;
  ~80 fewer lines; canonical helper added)
- **Added**: `scripts/validate_f2_record_shape.py` (parity validator)
- **Regenerated**: 6 P2 F2 record files; each carries the canonical F2 shape
- **Regenerated**: 5 conformance reports (reference-integrity now reports
  the 31 new resolved references)

## 7. Governance basis

- G-10 (single source of truth for artifact shape): the generator is now the
  source. Re-running the generator is idempotent.
- EGV-006 (references resolve to valid entities): the additional F2 composed
  references all resolve against vendored target-id snapshots.
- Programme control: evidence before assertion. The validator ensures
  future F2 emissions cannot regress from the canonical shape.
- G-09 (completeness evidenced, not assumed): the validator surfaces
  P1 F2 records that need their own hygiene slice (CR-IS-CAT-01C-P1H).

## 8. Companion slices (next, not in this CR)

- `CR-IS-CAT-01C-P1H` -- P1 authoring hygiene. Same shape parity fix for
  the 4 P1 F2 records that come from the P1 generator. Out of scope here.
- `CR-IS-CAT-01C-P3` -- ISF P3 (ISF-12..15). Reuses the `build_f2_record`
  helper from this CR.
