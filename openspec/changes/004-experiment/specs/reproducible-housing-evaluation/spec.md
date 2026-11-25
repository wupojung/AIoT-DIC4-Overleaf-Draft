# reproducible-housing-evaluation

## Purpose

Establish reviewable acceptance criteria for the experiment deliverable of an evidence-grounded IEEE-format housing comparison paper.

## ADDED Requirements

### Requirement: Dataset audit reproducibility

The Experiment section SHALL report the verified snapshot with release ID, hash, filters, field definitions and limitations. Unknown date semantics SHALL remain explicit.

#### Scenario: Dataset audit reproducibility review

- **WHEN** The source CSV is reprocessed
- **THEN** The procedure reproduces 10638 records, 32 fields and 9152 residential candidates with scoped interpretations

### Requirement: Controlled comparison

The protocol SHALL specify dataset, runtime, model and prompts, fixed and adaptive baselines, shared tools and budgets, case-level scoring, metric denominators, uncertainty and threats to validity.

#### Scenario: Controlled comparison review

- **WHEN** Paired runs produce no reproducible logs or scored data
- **THEN** The section identifies the comparison as planned and excludes outcome metrics or improvement claims

### Requirement: Conditional valuation

Any price-prediction evaluation SHALL require an approved target, leakage-safe split and data support before fitting or reporting models.

#### Scenario: Conditional valuation review

- **WHEN** The target or temporal semantics remain unresolved
- **THEN** The core evaluation stays with descriptive analytics and Agent reliability
