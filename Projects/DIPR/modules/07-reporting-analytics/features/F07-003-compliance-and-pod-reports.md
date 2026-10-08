# F07-003 — Compliance & PoD reports

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-003 |
| Feature Name | Compliance & PoD reports |
| Module | 07 — Reporting & Analytics |
| Description | Reports of verification outcomes, exceptions, and compliance posture |
| Business Objective | Demonstrate campaign compliance based on PoD verification results and exceptions. |
| Actors | Campaign Manager; Verifier; DIPR Admin; Auditor (read-only) |

### User Journey

- User runs compliance report → filters by campaign/channel/status → reviews exception list → exports for audit pack.

### Functional Capabilities

- Compliance summary by campaign and site
- Exception listing (rejected, pending rework, overdue verification)
- PoD outcome breakdown (accepted/rejected/third-party)
- Parameterized report run with saved filters where allowed

### Inputs

Campaign; date range; verification status; channel

### Outputs

Compliance report dataset and on-screen views

### Business Rules

Compliance posture derived from latest verification state per PoD
Exceptions include SLA breaches when configured

### Validations

- N/A

### Calculations

- None

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

Compliance & PoD outcome standard reports

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

- None

### Dependencies

Module 05 PoD verification; F07-005 for export scheduling

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Compliance report parameter form | Complex | 12 |
| UI | PoD outcome results grid with status badges | Complex | 12 |
| UI | Report run progress indicator | Easy | 4 |
| API | Build compliance report dataset | Complex | 8 |
| API | PoD verification outcome query | Medium | 6 |
| API | Report export file generation trigger | Medium | 6 |
| Database | Compliance report query views support | Medium | 4 |
| Database | Verification outcome indexed lookups | Easy | 2 |
| Testing | Compliance figures vs PoD source UAT | Complex | 8 |
| Testing | Parameter validation negative cases | Medium | 6 |
| Testing | Large result set pagination | Medium | 6 |
| Documentation | Compliance report field dictionary | Medium | 3 |
| Documentation | Auditor usage notes | Easy | 2 |

**Feature Total: 79 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
