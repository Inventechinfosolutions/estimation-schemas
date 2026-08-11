# F01-004 — Access Audit

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-004 |
| Feature Name | Access Audit |
| Module | 01 — User Access & Role Management |
| Description | Record privileged user and role changes for audit and compliance review. |
| Business Objective | Provide accountability for access administration actions. |
| Actors | Admin |

### User Journey

- Admin performs privileged change → system writes audit entry → Admin reviews access audit log with filters.

### Functional Capabilities

- Immutable-style audit entries for user/role/permission changes
- Audit log list with date and actor filters

### Inputs

- Filter: date range, actor, action type

### Outputs

- Audit trail records
- Filtered audit list

### Business Rules

- Privileged access changes always audited
- Audit records not editable by Admin UI

### Validations

- Valid date range for search

### Calculations

- None

### Workflow

- Change occurs → audit write → optional review

### Search Requirements

- By actor, action, date, target user/role

### Documents

- None

### Reports

- Optional export of audit list if FRS requires

### Notifications

- None

### Security

- Admin-only audit view
- Tamper-resistant storage practices

### Integrations

- None

### Dependencies

- F01-001
- F01-002

### Assumptions

- Retention period set in system parameters / FRS

### Risks

- High volume of changes may need archival policy

### Non Functional Requirements

- Reliable write of audit on each privileged action

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Access audit log list with filters | Medium | 6 |
| API | Audit query and privileged-change write hooks | Medium | 6 |
| Database | Access audit store with indexes | Medium | 4 |
| Testing | Audit capture and filter verification | Easy | 4 |
| Documentation | Access audit feature notes | Easy | 2 |

**Feature Total: 22 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
