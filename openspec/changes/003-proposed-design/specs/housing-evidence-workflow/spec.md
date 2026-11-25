# housing-evidence-workflow

## Purpose

Establish reviewable acceptance criteria for the proposed design deliverable of an evidence-grounded IEEE-format housing comparison paper.

## ADDED Requirements

### Requirement: Architecture and contracts

The design SHALL specify typed queries, read-only tools, versioned retrieval, deterministic analytics, observation validation, and cited or partial responses. It SHALL distinguish approved decisions from provisional settings.

#### Scenario: Architecture and contracts review

- **WHEN** A diagram or pseudocode is proposed
- **THEN** Its actors, budget and validation paths agree with the text and are traceable to the proposal

### Requirement: Evidence failure and trade-offs

The design SHALL define authorization, units, dates, applicability and provenance checks, bounded clarification and retry, and abstention when core price evidence is unavailable.

#### Scenario: Evidence failure and trade-offs review

- **WHEN** Optional evidence fails or all core evidence fails
- **THEN** The workflow retains independently supported claims in the first case and withholds price claims in the second
