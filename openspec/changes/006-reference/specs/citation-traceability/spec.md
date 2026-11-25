# citation-traceability

## Purpose

Establish reviewable acceptance criteria for the reference deliverable of an evidence-grounded IEEE-format housing comparison paper.

## ADDED Requirements

### Requirement: Metadata and claim traceability

Each cited source SHALL have an ID, canonical metadata, a resolvable DOI when assigned or an authoritative URL, and an exact location supporting the associated claim.

#### Scenario: Metadata and claim traceability review

- **WHEN** A lead has only secondary metadata or no accessible supporting text
- **THEN** Its metadata and content-review states remain separate and the unsupported claim is withheld

### Requirement: IEEE citation integrity

The assembled manuscript SHALL use numeric citations in first-appearance order and resolve each citation to one unique bibliography entry.

#### Scenario: IEEE citation integrity review

- **WHEN** The final LaTeX draft is compiled
- **THEN** Duplicate DOI or title variants, undefined citation keys and unintended uncited entries are corrected
