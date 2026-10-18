# Information System Function

> A defined unit of functional behaviour performed by an information system or one of its components to process information, execute logic, respond to events, or produce an intended system outcome.

**Layer:** L5 :  **Entity:** `dea:InformationSystemFunction` (class alias `ISF`) :  **Metamodel:** [v1.0.0](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=ISF)

> **CR-IS-CAT-01 status (2026-10-16)**: This catalog is the rename target of the legacy `dea-catalog-system-functions` (per CR-IS-CAT-01). The GitHub repository rename to `dea-catalog-information-system-functions` is performed by an org admin via GitHub repository transfer. Until the rename is complete, the legacy URL continues to resolve. The canonical reference in the OpenDEAM root model (v0.7.0) is `dea-catalog-information-system-functions`.

## Status

This is a **scaffold** repository that is being renamed and extended to cover the canonical Information System Function (ISF) entity introduced in the IS Semantic Architecture programme (dea-metamodel CR-018 D-1). Content population is planned for a subsequent phase; existing SF scaffold records are preserved under the legacy identity.

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:InformationSystemFunction` |
| Class Alias | `ISF` |
| Layer | L5 |
| Building Block | L5-systems |
| Profile | dea:digital |
| Metamodel Version | v1.0.0 |
| Status | planned |
| Supersedes | `dea:entity-system-function` (class alias `SF`; retained for EGV-004 identity continuity) |

## Catalog Structure

```
dea-catalog-information-system-functions/
├── metamodel-pointer.yaml   :  entity mapping (do not edit manually)
├── change-requests/
│   └── CR-IS-CAT-01-information-system-functions-rename.md
├── entities/
│   └── v1-alpha/          :  catalog entries go here
│       └── README.md
├── schemas/                :  JSON Schema for this entity type
│   └── entity.schema.json
├── docs/
│   └── is-semantic-architecture/
│       └── opendeam-identifier-map.yaml
└── .github/
    └── workflows/
        └── ci.yml         :  validates entries against schema
```

## Migration

The legacy `dea:entity-system-function` identity (class alias `SF`) is retained in OpenDEAM and in the catalog for EGV-004 identity continuity. New records should use the canonical `dea:InformationSystemFunction` (class alias `ISF`). Existing records continue to be valid; the catalog supports both identities conditionally.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the
[DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.
