# F08-004 — Notification preference & delivery log

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F08-004 |
| Feature Name | Notification preference & delivery log |
| Module | 08 — Notifications & Alerts |
| Description | User/role preferences within policy and delivery/failure logs |
| Business Objective | Let users control allowed channels within policy and give support visibility into delivery failures. |
| Actors | User; Admin; Support |

### User Journey

- User opens notification preferences → toggles allowed channels per event category within policy → saves → admin/support searches delivery log for failures.

### Functional Capabilities

- User preference matrix bounded by role policy defaults
- Admin override for mandatory security alerts
- Delivery log with channel, status, error reason, correlation id
- Filter log by user, event, date, channel

### Inputs

Preference selections; search filters

### Outputs

Updated preferences; log views

### Business Rules

Mandatory events cannot be fully opted out if policy requires
Preferences apply to email/SMS/in-app where configured

### Validations

- N/A

### Calculations

- None

### Workflow

- N/A

### Search Requirements

Delivery log search by recipient, event type, status, date range

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

- None

### Dependencies

F08-001; F08-002; F08-003; Module 01

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | User notification preference settings screen | Complex | 12 |
| UI | Channel opt-in/opt-out per event category | Medium | 6 |
| UI | Delivery log viewer with filters | Medium | 6 |
| API | Fetch user notification preferences | Easy | 4 |
| API | Save preference updates with policy bounds | Medium | 6 |
| API | Query delivery log paginated | Medium | 6 |
| Database | User preference persistence | Medium | 4 |
| Database | Delivery log append-only store | Medium | 4 |
| Testing | Policy bounds on mandatory alerts | Medium | 6 |
| Testing | Delivery log accuracy vs dispatch | Medium | 6 |
| Testing | Preference change audit | Easy | 4 |
| Documentation | Notification preference policy guide | Medium | 3 |

**Feature Total: 67 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
