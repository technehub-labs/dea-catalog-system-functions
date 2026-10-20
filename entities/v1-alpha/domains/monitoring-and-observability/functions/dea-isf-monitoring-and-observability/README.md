# Monitoring and Observability

**Domain**: Monitoring and Observability (ISF-10)
**ID**: `dea:information-system-function-monitoring-and-observability`
**Level**: F2 (parent)
**Status**: planned

## Description

The parent function that composes the monitoring-and-observability sub-tree. It collects signals from the runtime and makes them queryable, alertable, and inspectable.

## Child Functions

- `dea:information-system-function-metric-collection`
- `dea:information-system-function-log-aggregation`

## Decomposition Rationale

The F2 parent composes the named F4 children below. Each F4 captures an atomic responsibility; the F2 composes them without orchestrating them.

## Orchestration Responsibility

Not applicable to this function. The function composes child functions without orchestrating them; orchestration is at the ISC layer.

## Governance

- Functional owner: Monitoring and Observability team
- Steward: Architecture team
- Approval status: proposed

## Change History

- 2026-10-19: CR-IS-CAT-01C-P2 initial P2 population.
