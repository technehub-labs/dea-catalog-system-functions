# Entities (v1-alpha) :  Information System Function

This directory holds the v1-alpha catalogue entries for `dea:InformationSystemFunction`. Entries are JSON files that validate against `schemas/entities/information-system-function.json`.

> **CR-IS-CAT-01 (2026-10-16)**: The catalog is the rename target of `dea-catalog-system-functions`. Existing SF scaffold entries are preserved under the legacy identity. New entries use the canonical `dea:InformationSystemFunction` (class alias `ISF`).

## Structure

Each entry is a single JSON file with a stable id of the form `dea:information-system-function-<slug>`:

```
entities/v1-alpha/
  dea:information-system-function-example.json
```

## Example

```json
{
  "id": "dea:information-system-function-example",
  "type": "InformationSystemFunction",
  "name": "Example Information System Function",
  "description": "A scaffold record demonstrating the v1-alpha schema.",
  "version": "1.0.0",
  "lifecycle_status": "planned",
  "tags": ["scaffold", "v1-alpha"]
}
```

## Population

Content population is planned for a subsequent phase. The schema and the directory structure are in place; entries are added per the governance process documented in [CONTRIBUTING.md](../../CONTRIBUTING.md).
