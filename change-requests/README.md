# Change Requests

This directory tracks formal change requests (CRs) for `technehub-labs/dea-catalog-information-system-functions` (legacy URL: `technehub-labs/dea-catalog-system-functions` until org-admin transfer).

## 5-CR programme (2026-10-18)

The IS Semantic Architecture programme is delivered through the 5-CR programme for the ISF catalog. CR-IS-CAT-01 is the foundation (repo migration + identity + governance + CI). CR-IS-CAT-01A..01D are the four siblings (taxonomy, documentation, population, integration). G-01..G-12 governance rules from the 5-CR source doc section 7 apply to all CRs in this directory.

Source programme doc: `~/.hermes/profiles/coder/cache/cr-is-cat-01-programme/CR-IS-CAT-01-Programme.md`
Reconciliation plan: `~/.hermes/profiles/coder/kanban/cr-is-cat-01-programme-plan-2026-10-18.md`
Snapshot: `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-18.md`

| CR | Title | Status | Notes |
|---|---|---|---|
| [CR-IS-CAT-01](CR-IS-CAT-01-information-system-functions-rename.md) | Information System Functions catalog rename and extension (post-CR-AR-FMWK-04 merge) | Merged (PR #2, commit `4358a32`, 2026-10-18) | First catalog-rename slice of Path Y. Records the GitHub repository rename in the canonical metamodel pointer, the README, the OpenDEAM identifier map, and the artifacts. Pinned to OpenDEAM v0.7.0. The GitHub repository transfer itself is performed by an org admin; this CR records the rename as `pending-org-admin-transfer`. Existing SF scaffold records are preserved under the legacy identity (EGV-004). Consumed: dea-metamodel CR-018 (ISF introduction); CR-022 (artifact closure). dea-architecture-framework CR-AR-FMWK-04 (OpenDEAM extension). Cardinal rule compliance: Author: Emmanuel A. Otchere. D-004 / D-005 / embargo clean. |
| [CR-IS-CAT-01A](CR-IS-CAT-01A-taxonomy.md) | Information System Function Taxonomy and Classification Architecture | Proposed (this PR) | Sibling 1 of 4. Establishes the 15 functional domains (ISF-01..ISF-15) with normative definitions, scope, inclusion criteria and exclusion criteria; the 7 orthogonal classification facets (5.1-5.7) including the doctrine on ISF-13 vs all-other-domains (AI-assisted vs AI-native via the automation characteristics facet); the 11 classification rules; the JSON Schema for taxonomy records; the CI validator workflow. Per DOCTRINE-MECE card #463, the 15 domains are NOT strictly MECE; the boundaries are established by actor / data shape / coordination layer / read-write / computational distinction. G-05 (taxonomy is classification not metamodel), G-06 (classification separate from decomposition), G-09 (completeness evidenced not assumed), G-12 (no implementation-leakage). The 01C population exercise is the validation step. |
