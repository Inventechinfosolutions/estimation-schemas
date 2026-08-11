# F06-003 — Notification Log & Retry Support

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-003 |
| Feature Name | Notification Log & Retry Support |
| Module | 06 — Notifications & Alerts (SMS / Email) |
| Description | Track notification delivery status and support operational retry for failed sends. |
| Business Objective | Enable support/warranty teams to diagnose and resend failed alerts. |
| Actors | Admin; Support (warranty ops) |

### User Journey

- Admin opens notification log → filters failed → reviews error → retries send if permitted.

### Functional Capabilities

- Unified SMS/Email notification log
- Filter by status/channel/complaint
- Manual retry for failed items

### Inputs

- Filters
- Retry action

### Outputs

- Log list
- Retry attempt

### Business Rules

- Retry only failed/eligible statuses
- Retry creates new attempt linked to original

### Validations

- Item eligible for retry

### Calculations

- None

### Workflow

- Dispatch → log → fail → retry → log

### Search Requirements

- By complaint ref, mobile/email, status, date

### Documents

- None

### Reports

- None

### Notifications

- Retry reuses F06-001/002

### Security

- Admin/support role only

### Integrations

- Uses SMS/Email connectors

### Dependencies

- F06-001
- F06-002

### Assumptions

- Warranty ops use this UI; warranty effort itself not in feature hours

### Risks

- High failure volume without gateway SLA

### Non Functional Requirements

- Retain logs per retention policy

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Notification log console with filters and retry | Complex | 8 |
| API | Log query and retry orchestration | Complex | 8 |
| Database | Unified notification log and attempt history | Medium | 4 |
| Testing | Log filter and retry scenarios | Complex | 8 |
| Documentation | Notification log & retry notes | Medium | 3 |

**Feature Total: 31 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
