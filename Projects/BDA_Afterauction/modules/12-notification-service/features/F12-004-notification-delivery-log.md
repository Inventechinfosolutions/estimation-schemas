# F12-004 — Notification Delivery Log

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-004 |
| Feature Name | Notification Delivery Log |
| Module | 12 — Notification Service |
| Module Type | Shared |
| Release | Go-live |

### Description
Log of every notification with event, recipient, channel, template version, send time, delivery status and retries, with search, resend, and reports.

### Business Objective
Prove delivery and support troubleshooting.

### Actors
- Auction Admin
- Super Admin

### User Journey
1. **Who creates:** The system writes the log.
2. **How they create:** Each send and status update is logged.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** The Auction Admin searches failed messages.
6. **How the approver decides:** The Auction Admin resends.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors search the log.

### Functional Capabilities
- Searchable log
- Status timeline
- Resend
- Delivery reports

### UI Screens
- Delivery log search
- Message detail

### Logical API Operations
- Write log
- Search log
- Resend

### Inputs
- Send events

### Outputs
- Log

### Business Rules
- Retention per policy

### Validations
- None

### Calculations
- Delivery rates

### Workflow
Not applicable

### Search Requirements
- By recipient, case, status, date

### Documents
- None

### Reports
- Delivery report

### Notifications
- None

### Security
- Masking of mobile / e-mail for non-admin

### Integrations
- None

### Dependencies
- F12-003

### Assumptions
- None

### Risks
- Log volume; partitioning

### Non Functional Requirements
- Search within 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Delivery log search | Medium | 6 |
| UI | Message detail | Easy | 4 |
| API | Write log | Easy | 4 |
| API | Search log | Medium | 6 |
| API | Resend | Easy | 4 |
| Database | Delivery log | Medium | 4 |
| Testing | Log and resend tests | Easy | 4 |
| Documentation | Log user note | Simple | 1 |

**Feature Total: 33 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 14 | 4 | 0 | 4 | 1 | **33** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
