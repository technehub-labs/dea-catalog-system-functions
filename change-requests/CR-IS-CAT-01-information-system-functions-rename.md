# CR-IS-CAT-01: Information System Functions catalog rename + extension

| Field | Value |
|-------|-------|
| **CR** | CR-IS-CAT-01 |
| **Title** | Information System Functions catalog rename and extension (post-CR-AR-FMWK-04 merge) |
| **Status** | Proposed (this PR) |
| **Layer** | Catalog (T2) |
| **Programme** | Information Systems Semantic Architecture |
| **Architectural parent** | CR-AR-FMWK-04 (OpenDEAM extension; merged 2026-10-16 via PR #17, commit `1063aa3`); CR-018 (ISF introduction; merged 2026-10-16 via PR #171, commit `0f16441`) |
| **Companion to** | CR-022 (metamodel closure; merged 2026-10-16); CR-013 (dea-governance; portfolio adoption; pending) |
| **Depends on** | CR-018 (the canonical entity `dea:InformationSystemFunction`); CR-022 (artifact closure); CR-AR-FMWK-04 (OpenDEAM extension) |
| **Enables** | CR-IS-CAT-02 (catalog rename to `dea-catalog-information-system-components`); CR-IS-CAT-03 (new `dea-catalog-information-system-services`); CR-IS-CAT-04 (new `dea-catalog-information-system-integration-interfaces`) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-16 |

## 1. Executive Summary

This CR is the first catalog-rename slice of Path Y, landing in `technehub-labs/dea-catalog-system-functions`. The GitHub repository rename to `dea-catalog-information-system-functions` is performed by an org admin via GitHub repository transfer; this CR records the rename in the canonical metamodel pointer, the README, the OpenDEAM identifier map, and the artifacts.

The catalog is the rename source for the legacy `dea:entity-system-function` (class alias `SF`) identity. The new canonical entity is `dea:InformationSystemFunction` (class alias `ISF`), introduced in dea-metamodel CR-018 (D-1 disposition). The legacy identity is retained in OpenDEAM and in the catalog for EGV-004 identity continuity; new records use the canonical entity.

The artifacts (JSON Schema, SQLite table, Pydantic module, TypeScript interface) are populated per the metamodel closure in CR-022. The schemas directory, the entities/v1-alpha/ directory, the docs/is-semantic-architecture/ directory, and the change-requests/ directory are all present.

## 2. Scope

### 2.1 In scope

1. The metamodel pointer at `metamodel-pointer.yaml` updated to:
   - Reference the new canonical entity `dea:InformationSystemFunction` (class alias `ISF`).
   - Pin to OpenDEAM model v0.7.0 (post-CR-AR-FMWK-04).
   - Document the migration path (legacy SF -> ISF).
   - List the artifact paths (JSON Schema, SQLite table, Pydantic module, TypeScript interface).
2. The README at `README.md` updated to:
   - Document the new canonical entity.
   - Reference the OpenDEAM model v0.7.0.
   - Document the migration path.
3. The schemas directory at `schemas/entities/information-system-function.json` (new) with the catalog's JSON Schema for the canonical entity.
4. The entities directory at `entities/v1-alpha/README.md` (new) with the directory structure description.
5. The docs directory at `docs/is-semantic-architecture/opendeam-identifier-map.yaml` (new) with the local copy of the OpenDEAM-to-metamodel identifier map.
6. The CI workflow at `.github/workflows/validate-allocation.yml` pinned to v0.7.0.
7. The CR-IS-CAT-01 doc (this file).
8. A `change-requests/README.md` row for CR-IS-CAT-01.

### 2.2 Out of scope

1. The actual GitHub repository rename (`dea-catalog-system-functions` -> `dea-catalog-information-system-functions`). Performed by an org admin via GitHub repository transfer. The CR records the rename as `pending-org-admin-transfer`.
2. The catalog content population. Out of scope; CR-IS-CAT-01 establishes the rename and the artifact structure; content population is a subsequent phase.
3. The cross-catalog migration. The `dea-catalog-processes`, `dea-catalog-business-capabilities`, `dea-catalog-digital-business-service-factory`, `dea-catalog-stakeholders` catalogs are not affected; they continue to be valid.
4. The OpenDEAM identifier map. The canonical version is in `dea-architecture-framework/docs/is-semantic-architecture/opendeam-identifier-map.yaml`; the local copy in this repo is a convenience for catalog operators.

## 3. Migration Path

The legacy `dea:entity-system-function` identity (class alias `SF`) is retained in OpenDEAM and in the catalog for EGV-004 identity continuity. Existing records that reference SF continue to resolve; new records use the canonical ISF.

The catalog supports both identities conditionally:
- `dea:entity-system-function` (legacy; class alias SF; retained for migration)
- `dea:InformationSystemFunction` (canonical; class alias ISF; new)

The conditional merge is documented in the metamodel pointer's `migration.disposition` field. Existing records in `entities/v1-alpha/` are preserved as-is; their `dea:entity-system-function` reference is annotated with the `supersedes` link to `dea:InformationSystemFunction`.

## 4. Artifacts

The artifacts are populated per the metamodel closure in CR-022:

| Artifact | Path | Status |
|---|---|---|
| JSON Schema | `schemas/entities/information-system-function.json` | created (this PR) |
| SQLite table | `information_system_functions` | managed by dea-metamodel; not in this catalog repo |
| Pydantic module | `pydantic/information_system_function.py` | managed by dea-metamodel; not in this catalog repo |
| TypeScript interface | `typescript/src/interfaces.ts` | managed by dea-metamodel; not in this catalog repo |

The catalog repo carries the JSON Schema (the local representation); the SQLite table, Pydantic module, and TypeScript interface are managed by the dea-metamodel repo. The catalog pointer records the paths to all four artifacts for cross-reference.

## 5. CI Workflow

The CI workflow at `.github/workflows/validate-allocation.yml` is pinned to v0.7.0 (was v0.2.1). The workflow uses the reusable workflow at `technehub-labs/dea-architecture-framework/.github/workflows/validate-against-model.yml@v0.7.0`. The pointer file is `metamodel-pointer.yaml`.

If the GitHub repository rename has not yet been performed by the org admin at the time of merge, the CI workflow will continue to operate against the legacy repo URL (`technehub-labs/dea-catalog-system-functions`); the GitHub Actions runner resolves the workflow file from the canonical repo (this one), not from the renamed URL. The reusable workflow resolution may need to be re-pinned after the rename.

## 6. Cross-Repository Impact

| Repository | Required alignment |
|---|---|
| `technehub-labs/dea-architecture-framework` | No action; CR-AR-FMWK-04 has already updated the OpenDEAM model v0.7.0. |
| `technehub-labs/dea-metamodel` | No action; CR-022 has already closed the metamodel side. |
| `technehub-labs/dea-catalog-system-functions` -> `dea-catalog-information-system-functions` | This PR (CR-IS-CAT-01) records the rename in the canonical pointer; the GitHub repository transfer is performed by an org admin. |
| `technehub-labs/dea-catalog-application-components` -> `dea-catalog-information-system-components` | CR-IS-CAT-02 (next slice). |
| `technehub-labs/dea-catalog-platform-services` + new `dea-catalog-information-system-services` | CR-IS-CAT-03. |
| `technehub-labs/dea-catalog-api-contracts` + new `dea-catalog-information-system-integration-interfaces` | CR-IS-CAT-04. |
| `technehub-labs/dea-governance` | `CR-013 (dea-governance)` portfolio adoption (the closure gate for the IS programme). |

## 7. Acceptance Criteria

- [ ] `metamodel-pointer.yaml` references `dea:InformationSystemFunction` (class alias `ISF`); pinned to OpenDEAM v0.7.0.
- [ ] `README.md` documents the new canonical entity and the migration path.
- [ ] `schemas/entities/information-system-function.json` exists and validates.
- [ ] `entities/v1-alpha/README.md` exists.
- [ ] `docs/is-semantic-architecture/opendeam-identifier-map.yaml` exists.
- [ ] `.github/workflows/validate-allocation.yml` pinned to v0.7.0.
- [ ] CR-IS-CAT-01 doc (this file) is present at `change-requests/CR-IS-CAT-01-information-system-functions-rename.md`.
- [ ] `change-requests/README.md` row registered.
- [ ] Cardinal author rule (CR-MM-04 R1) is satisfied: `Author: Emmanuel A. Otchere`.
- [ ] Cardinal author rule (CR-MM-04 R2) is satisfied: this PR is one logical change (rename + extension + artifact structure); no bundle content from CR-IS-CAT-02..04.
- [ ] D-004 / D-005 / Standardization-body embargo clean.

## 8. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| GitHub repository rename not performed by org admin at merge time | The CR records the rename as `pending-org-admin-transfer`; the legacy URL continues to resolve. After the rename, the catalog URL in the metamodel pointer is updated. |
| Reusable workflow resolution after rename | The reusable workflow file resolves from the catalog repo, not the framework repo. The pinning (`@v0.7.0`) targets the model version, not the repo URL. |
| Existing records losing EGV-004 identity | The legacy identity is retained; the migration annotation in the metamodel pointer documents the supersedes link. |
| OpenDEAM identifier map drift | The local copy in this repo is a convenience; the canonical map is in `dea-architecture-framework`. Any drift is caught by the dea-architecture-framework validate-model check. |
| Generated artifact drift | The catalog carries only the JSON Schema; the SQLite table, Pydantic module, and TypeScript interface are managed by the dea-metamodel repo (per CR-022). The artifacts are kept in sync by the dea-metamodel CI. |

## 9. Completion Definition

CR-IS-CAT-01 is complete when:

1. The metamodel pointer references the new canonical entity.
2. The README documents the migration path.
3. The schemas, entities, and docs directories are populated.
4. The CI workflow is pinned to v0.7.0.
5. Local validation passes (the metamodel pointer parses as YAML; the JSON Schema is valid).
6. PR opens against `origin/main`; CI on GitHub Actions shows green before user review.

## 10. Path Y Progress (after this PR)

After CR-IS-CAT-01 lands, the remaining Path Y work is:

1. `CR-IS-CAT-02` (rename `dea-catalog-application-components` to `dea-catalog-information-system-components`; extend)
2. `CR-IS-CAT-03` (establish new `dea-catalog-information-system-services`)
3. `CR-IS-CAT-04` (extend `dea-catalog-api-contracts`; establish new `dea-catalog-information-system-integration-interfaces`)
4. `CR-013 (dea-governance)` portfolio adoption (the closure gate)

## 11. References

### 11.1 Inputs and authorities

- `technehub-labs/dea-metamodel/change-requests/CR-018-information-system-function.md` (ISF introduction; merged 2026-10-16)
- `technehub-labs/dea-metamodel/change-requests/CR-022-metamodel-artifact-and-conformance-closure.md` (artifact closure; merged 2026-10-16)
- `technehub-labs/dea-architecture-framework/change-requests/CR-AR-FMWK-04-information-system-entity-allocation.md` (OpenDEAM extension; merged 2026-10-16)
- `technehub-labs/dea-architecture-framework/docs/is-semantic-architecture/opendeam-identifier-map.yaml` (canonical identifier map)
- `technehub-labs/dea-metamodel/docs/is-semantic-architecture/opendeam-identifier-map.yaml` (consumed stub)

### 11.2 Companion Kanban surface

- Project 23 (DEAMMISE) at `/board/23`: card #393 (CR-IS-CAT-01), In Progress during authoring
- Companion umbrella carrier #384
- DRIFT-4 card #419 (recorded in CR-019)
- Per-channel skill at `~/.hermes/profiles/coder/skills/dea-is-semantic-arch-kanban-discipline/SKILL.md`
- Snapshot doc at `~/.hermes/profiles/coder/kanban/dea-metamodel-is-snapshot-2026-10-16.md`

---

End of CR-IS-CAT-01.
