# F08-002 — Email notification dispatch

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F08-002 |
| Feature Name | Email notification dispatch |
| Module | 08 — Notifications & Alerts |
| Description | Email alerts using templates for approvals, assignments, and PoD outcomes |
| Business Objective | Deliver email alerts for key workflow events using configurable templates. |
| Actors | System; Admin |

### User Journey

- Workflow event fires → template selected → merge fields populated → email sent async → delivery status logged.

### Functional Capabilities

- Event-driven email for approvals, assignments, PoD outcomes
- Subject/body template merge from masters
- Async send with bounded retries
- Skip send when user opted out per policy (F08-004)

### Inputs

Event payload; recipient email; template id

### Outputs

Outbound email; delivery log entry

### Business Rules

Configured events only; no email when address missing and no fallback defined

### Validations

Email format; active template

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

- RBAC and platform security controls apply

### Integrations

SMTP or DIPR-provided mail relay

### Dependencies

Module 02 notification templates; F08-004

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Email template preview panel in admin | Medium | 6 |
| UI | Test send dialog with recipient override | Easy | 4 |
| API | Render notification to email body merge | Complex | 8 |
| API | Queue email dispatch attempt | Medium | 6 |
| API | Record delivery status callback handler | Easy | 4 |
| Integration | SMTP/email gateway connector | Easy | 8 |
| Integration | TLS credential vault binding | Medium | 16 |
| Database | Email dispatch attempt log | Easy | 2 |
| Database | Template version reference fields | Simple | 1 |
| Testing | Template merge with sample events | Medium | 6 |
| Testing | Gateway failure retry behaviour | Medium | 6 |
| Testing | Invalid recipient negative | Easy | 4 |
| Documentation | Email dispatch event list | Easy | 2 |
| Documentation | DIPR SMTP setup checklist | Easy | 2 |

**Feature Total: 75 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
