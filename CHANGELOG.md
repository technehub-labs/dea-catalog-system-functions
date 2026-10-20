# Changelog

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
