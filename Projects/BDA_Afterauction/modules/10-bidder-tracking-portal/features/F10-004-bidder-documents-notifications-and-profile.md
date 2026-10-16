# F10-004 — Bidder Documents, Notifications & Profile

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-004 |
| Feature Name | Bidder Documents, Notifications & Profile |
| Module | 10 — Bidder Tracking Portal |
| Module Type | Business |
| Release | Go-live |

### Description
Bidder document area with intimation letter, demand notices, receipts, orders, draft sale deed and uploaded documents; notification inbox with read status; document requests to respond to; and profile settings.

### Business Objective
One place for the bidder to find every document and message.

### Actors
- Successful Bidder

### User Journey
1. **Who creates:** Documents and messages are created by other features.
2. **How they create:** The bidder opens Documents or Inbox.
3. **How they edit:** The bidder uploads documents only against requests.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The bidder sees all documents and messages.
8. **How the approver / auditor sees history:** Auditors see downloads and uploads.

### Functional Capabilities
- Document list by type
- Pending requests with upload
- Notification inbox
- Profile link

### UI Screens
- Documents area
- Pending requests
- Notification inbox

### Logical API Operations
- List bidder documents
- List pending requests
- Inbox and mark read

### Inputs
- Uploads

### Outputs
- Lists

### Business Rules
- Own documents only

### Validations
- Ownership

### Calculations
- Unread count

### Workflow
Unread → Read

### Search Requirements
- By type and date

### Documents
- All bidder documents

### Reports
- None

### Notifications
- In-portal inbox

### Security
- Bidder isolation; malware scan on upload

### Integrations
- None

### Dependencies
- F07-004
- F12-004

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Documents area | Medium | 6 |
| UI | Pending requests | Easy | 4 |
| UI | Notification inbox | Easy | 4 |
| API | List bidder documents | Easy | 4 |
| API | List pending requests | Easy | 4 |
| API | Inbox and mark read | Easy | 4 |
| Database | Bidder inbox | Simple | 1 |
| Testing | Documents and inbox tests | Easy | 4 |
| Documentation | Bidder help: documents | Simple | 1 |

**Feature Total: 32 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 12 | 1 | 0 | 4 | 1 | **32** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small
- No external integration channel in this feature; Integration row omitted.
