# Changelog

## CR-IS-CAT-01C-P5 (2026-11-12)

- ISF P5 registry population: 1188 new relationship records (594 dea:executes edges from the CR-IS-CAT-01C-P4 executing_components evidence + 594 dea:measured_by edges via the curated 34-row system anchor metric bridge).
- Registry: 96 to 1284 records; measured_by coverage 594 of 594 P4 functions; executes coverage 594 of 594 (per G-09 evidence-driven; per G-11 the measured_by rows are OpenDEAM v0.7.0 allocation declarations, metric definitions owned by the Metric catalogue).
- Target-id snapshots re-pinned: dea-catalog-application-components 8508b867 to 316931db (276 to 735 ids, includes the CR-IS-CAT-02C-P5 F3 atoms); dea-catalog-metrics vendored for the first time (4433 ids at 50e0e670); dea-catalog-business-capabilities 848b1635 to 92a9b6d9 (29 to 40 ids, strictly additive); dea-catalog-processes pin held at 390e73eb (identity-scheme rebasing is a separate CR).
- Reference-integrity: 2116 classified, 2110 resolved, 6 forward, 0 unresolved.
- New scripts/generate_p5_registry.py + scripts/p5_registry_data.json (deterministic and idempotent; per G-10); scripts/build_target_snapshots.py extended with the metrics target repo and a git-less HEAD_SHA pin fallback.

## CR-IS-CAT-01C-P4 (2026-11-10)

- ISF P4 population: 594 vendor-neutral F4 records across 10 of 15 functional domains (34 generic system classes; 63 generic sub-systems; 141 composite components).
- Corroboration rule: every function cites at least 3 distinct vendor systems as external evidence in governance.source_and_evidence (per G-12 no vendor product is canonical).
- Decomposition: F4 leaves grouped by functional_domain; executing_components crawl to the CR-IS-CAT-02C-P4 component records; no synthetic F2 parents (per G-06).
- Reference-integrity: 922 resolved + 6 forward + 0 unresolved; the 594 new executing_components references resolve against the P4 ISC snapshot pin.
- New scripts/generate_p4_population.py + scripts/p4_function_data.json (deterministic and idempotent; per G-10).
- Telecommunications extension: BSS, OSS, mobile core and radio access network classes (embargo-clean generic terminology).

## CR-IS-CAT-01C-P2 (2026-10-19)

- ISF P2 population: 6 new domains (ISF-06..11); 1 F2 + 2 F4 per domain = 18 records.
- Catalog state: 11/15 domains populated, 38 records, 64 cross-cat relationships.
- Reference-integrity report: 200 resolved + 6 forward + 0 unresolved.
- Cross-cat references authored with canonical BC/BP/ISC ids from the start (zero rebases needed in P2).

## CR-IS-CAT-01R (2026-10-19)

- Cross-catalogue reference integrity remediation.
- 21 synthetic BC/BP/ISC ids rebased to canonical target ids (verified 21/21 resolve against pinned target-repo HEAD).
- 6 forward references declared (data-entity / event / ISS / II / metric) with named owning CRs.
- 4 dangling intra-catalog children of F2 identity-and-access-management removed; dispositions documented.
- Reference-integrity report upgraded to real resolution against vendored target-id snapshots; 92 resolved + 6 forward + 0 unresolved.
- CI step 8 hardened: hard-fail on unresolved_count > 0.


## CR-IS-CAT-01C-P2H (2026-10-19)

- P2 authoring hygiene. F2 record shape parity with the P1 hand-edited canonical F2.
- Refactored `scripts/generate_p2_population.py` (single `build_f2_record()` helper composes F2 from F4).
- Added `scripts/validate_f2_record_shape.py` (parity validator).
- Re-emitted 6 P2 F2 records with the canonical shape.
- Reference-integrity: 237 total classified, 231 resolved, 6 forward, 0 unresolved.


## CR-IS-CAT-01C-P3 (2026-10-19)

- ISF P3 population: 4 new domains (ISF-12..15); 1 F2 + 2 F4 per domain = 12 records.
- ISF catalog closed at 15/15 domains, 50 records, 96 cross-cat relationships.
- Reference-integrity: 328 resolved + 6 forward + 0 unresolved.
- ISF-14 `experience-and-interaction` resolves the last ISC-side forward ref `customer-experience-management`.
- New `scripts/_f2_record_helper.py` (shared F2 record + README shape) and `scripts/generate_p3_population.py` (P3 generator; imports the helper).


## CR-IS-CAT-01C-P1H (2026-10-19)

- P1 authoring hygiene. The 4 P1 generator-emitted F2 records now match the canonical F2 shape.
- `scripts/generate_p1_population.py`: separate F4 and F2 emit paths; F2 composed via the shared `_f2_record_helper`.
- `scripts/_f2_record_helper.py`: `f2_slug` parameter (P1 domain slug differs from F2 record slug); 5 P1 input/output text entries.
- Fixed latent defect: the P1 generator unconditionally overwrote `entities/v1-alpha/index.yaml` with P1-only data, truncating the catalogue from 15 domains / 50 functions to 5 / 20. Now merges. Latent since CR-IS-CAT-01C-P2 (P2/P3 each ran after P1, so CI never saw it).
- `scripts/validate_f2_record_shape.py`: single blocker class (the P1-warnings carve-out is removed). 15/15 F2 records pass.
- Population unchanged: 15 domains, 50 functions, 96 relationships, 328 resolved / 6 forward / 0 unresolved.
