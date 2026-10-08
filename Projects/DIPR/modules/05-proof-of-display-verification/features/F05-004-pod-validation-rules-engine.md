# F05-004 — PoD validation rules engine

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-004 |
| Feature Name | PoD validation rules engine |
| Module | 05 — Proof-of-Display Capture & Verification |
| Description | Apply DIPR-confirmed GPS accuracy, timestamp source, and tamper/validation rules on PoD ingest. |
| Business Objective | Automatically flag or block weak evidence before verifiers spend time on non-compliant captures. |
| Actors | DIPR Administrator (rule config); PoD Verifier (view outcomes); Field Personnel (see flags) |

### User Journey

- Administrator configures rules (max GPS drift from site, allowed timestamp sources, hash/tamper checks) → on PoD submit engine evaluates → outcomes: pass, warn, or fail → verifier sees rule outcome badges on queue item → failed items route to rework without manual accept.

### Functional Capabilities

- Admin rules configuration screen grouped by rule type
- Rule evaluation on ingest and re-evaluation on parameter change (batch optional)
- Outcome badges and detail on PoD record (which rule failed)
- GPS distance compare using site geotag (F04-003) and capture coordinates
- Timestamp source preference (EXIF vs device vs server) with conflict detection
- Basic tamper signals (e.g., reuse hash, edited EXIF) as DIPR confirms

### Inputs

- Rule thresholds from F02-004; PoD metadata and file fingerprint

### Outputs

- Rule evaluation result per PoD; optional auto-reject status

### Business Rules

- Mandatory rules can block verification queue entry until resolved
- Warning rules allow verify with documented override role
- Rule changes audited via F02-005 pattern

### Validations

- Threshold numeric bounds on admin UI

### Calculations

- Haversine or equivalent distance; time delta checks

### Workflow

- Ingest → evaluate → pass/warn/fail → verification eligibility

### Search Requirements

- Register filter by rule failure type

### Documents

- None

### Reports

- Rule failure rates in Module 07

### Notifications

- Alert field user on auto-fail (Module 08)

### Security

- Rule edit administrator-only

### Integrations

- None

### Dependencies

- F02-004 parameters; F04-003 geotags; F05-001 ingest

### Assumptions

- Exact tamper library chosen in technical design phase; effort captured as complex API

### Risks

- Phase 1 ambiguity on rules increases rework after DIPR workshop

### Non Functional Requirements

- Evaluation completes within ingest SLA for single and batch items

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | PoD validation rules admin register | Medium | 6 |
| UI | Rule condition builder editor | Complex | 12 |
| UI | Rule priority ordering drag list | Medium | 6 |
| UI | Rule outcome badges on PoD detail view | Easy | 4 |
| UI | Test rule against sample PoD panel | Medium | 6 |
| UI | Rule publish/activate toggle | Easy | 4 |
| API | CRUD PoD validation rule definitions | Medium | 6 |
| API | Evaluate rules on PoD ingest | Very High | 16 |
| API | Re-evaluate rules on demand for PoD | Medium | 6 |
| API | List evaluation results for PoD | Easy | 4 |
| Database | Rule definition storage | Medium | 4 |
| Database | Per-PoD per-rule evaluation result | Medium | 4 |
| Testing | GPS drift distance fail rule | Complex | 8 |
| Testing | Capture timestamp conflict fail | Medium | 6 |
| Testing | Mandatory metadata fail paths | Medium | 6 |
| Testing | Rule priority ordering outcomes | Medium | 6 |
| Documentation | Validation rules catalog for DIPR sign-off | Easy | 2 |
| Documentation | UAT rule pack regression set notes | Medium | 3 |

**Feature Total: 109 hours**

### Estimation Assumptions

- Machine-learning tamper detection is out of scope unless DIPR adds explicitly.
