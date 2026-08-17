# F09-002 — Special Court filing report

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Special Court filing report |
| **Module** | 09 — Operational Reports, Lists & Special Court Outputs |

### Description
Using the same class of approved inputs, the Officer generates the Special Court filing report, reviews it on screen, and produces the filing copy. The Officer does not re-key the settlement figures by hand into an unrelated template.

### Business Objective
Produce the Special Court filing report from the same class of approved inputs used for equitable distribution.

### Actors
Officer.

### User Journey
1. Officer uses the same class of approved inputs as F09-001.
2. Officer generates the Special Court filing report and reviews it on screen.
3. Officer produces the filing copy without re-keying settlement figures into an unrelated template.

### Functional Capabilities
- Generate Special Court filing report from approved inputs.
- On-screen review.
- Produce filing copy without manual re-key of settlement figures.

### Inputs
Same class of approved inputs (recovered funds, approved claims and related fields).

### Outputs
Special Court filing report / filing copy.

### Business Rules
- Same class of inputs as equitable distribution.
- Legal Management court petitions/orders are a separate SOW and are not duplicated here.
- No generative legal drafting.

### Validations
- Input-format completeness.
- Figures reconcilable to settlement/recovery.

### Calculations
Report assembly per approved format.

### Workflow
Load inputs → generate → review → filing copy.

### Search Requirements
Reports by FE, period, run date.

### Documents
Filing copy.

### Reports
The Special Court filing report.

### Notifications
None.

### Security
Authorised Posts only. Court-facing outputs are need-to-know.

### Integrations
None.

### Dependencies
F09-001 inputs; F08; F03; Authority format.

### Assumptions
- Approved Special Court report format is supplied by the Authority.

### Risks
- Re-keying into a side template would break reconciliation.

### Non Functional Requirements
On-screen review before filing copy. Structured generation.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Special Court report generate and preview | UI | Complex | 12 |
| Filing copy produce | UI | Easy | 4 |
| Special Court report generation | API | Very High | 16 |
| Filing report persistence | DB | Medium | 4 |
| Special Court report tests | Testing | Complex | 8 |
| Special Court report format note | Documentation | Complex | 4 |
| **Total** | | | **48** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Equitable distribution statement is F09-001; this feature is the filing report.
