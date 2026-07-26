# System Function

> A capability exposed by an application or platform that automates a business process.

**Layer:** L4 · **Entity:** `SF` · **Metamodel:** [v2.0.0-alpha](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=SF)

## Status

This is a **scaffold** repository — created during the Phase 1 metamodel v2 rollout.
Content population is planned for a subsequent phase.

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:entity-sf` |
| Class Alias | `SF` |
| Layer | `L4` |
| Metamodel Version | v2.0.0-alpha |

## Catalog Structure

```
dea-catalog-system-functions/
├── metamodel-pointer.yaml   ← entity mapping (do not edit manually)
├── entities/
│   └── v1-alpha/          ← catalog entries go here
│       └── README.md
├── schemas/                ← JSON Schema for this entity type
│   └── entity.schema.json
└── .github/
    └── workflows/
        └── ci.yml         ← validates entries against schema
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the
[DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.
