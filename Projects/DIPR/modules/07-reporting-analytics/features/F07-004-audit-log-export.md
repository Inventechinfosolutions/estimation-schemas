# F07-004 — Audit log export

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-004 |
| Feature Name | Audit log export |
| Module | 07 — Reporting & Analytics |
| Description | Exportable audit reports for access and key operational events |
| Business Objective | Support internal audit with exportable trails of access and sensitive operations. |
| Actors | DIPR Admin; Auditor; Security Officer |

### User Journey

- Auditor selects date range and event categories → previews audit log → exports CSV/PDF for review.

### Functional Capabilities

- Filter audit events by user, role, module, action, and date
- Export large result sets with pagination/streaming
- Immutable presentation of logged fields

### Inputs

Filter criteria; export format selection

### Outputs

Audit export files

### Business Rules

Only entitled audit roles may export full logs
Exports watermarked with generator and timestamp

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

- None

### Notifications

- None

### Security

Sensitive fields masked per policy; export action itself audited

### Integrations

- None

### Dependencies

Module 01 access logs; Module 10 retention policies

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Audit log filter panel (actor, entity, date range) | Medium | 6 |
| UI | Export format and column picker dialog | Easy | 4 |
| UI | Export job status toast/list | Simple | 2 |
| API | Audit log search with pagination | Medium | 6 |
| API | Generate audit export file job | Medium | 6 |
| API | Export download entitlement check | Easy | 4 |
| Database | Audit log range query indexes | Easy | 2 |
| Testing | Export completeness vs filter | Medium | 6 |
| Testing | Unauthorized export negative | Easy | 4 |
| Documentation | Audit export usage notes | Easy | 2 |

**Feature Total: 42 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
