# F12-001 — Bilingual Notification Template Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-001 |
| Feature Name | Bilingual Notification Template Management |
| Module | 12 — Notification Service |
| Module Type | Shared |
| Release | Go-live |

### Description
Kannada and English templates for e-mail, SMS and WhatsApp for every event, with merge fields, DLT template ID and header for SMS, WhatsApp approved template names, preview and versioning.

### Business Objective
Control message content centrally and comply with TRAI DLT rules.

### Actors
- Auction Admin

### User Journey
1. **Who creates:** The Auction Admin creates templates.
2. **How they create:** The Auction Admin selects an event and channel, enters text in both languages, merge fields and DLT ID.
3. **How they edit:** The Auction Admin edits and previews.
4. **How they send for approval:** Activation does not need approval (configurable).
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The Auction Admin sees versions.
8. **How the approver / auditor sees history:** Auditors see changes.

### Functional Capabilities
- Templates per event × channel × language
- DLT ID and sender ID
- WhatsApp template mapping
- Preview and test send
- Versioning

### UI Screens
- Template list by event
- Template editor
- Test send

### Logical API Operations
- Save template
- Render with data
- Test send
- Resolve template

### Inputs
- Text
- DLT ID

### Outputs
- Templates

### Business Rules
- SMS text must match DLT-registered content

### Validations
- Length limits

### Calculations
- SMS parts count

### Workflow
Draft → Active

### Search Requirements
- By event

### Documents
- None

### Reports
- Template list

### Notifications
- None

### Security
- Auction Admin only

### Integrations
- None

### Dependencies
- F12-002

### Assumptions
- BDA registers DLT templates

### Risks
- DLT mismatch

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Template list by event | Easy | 4 |
| UI | Template editor | Medium | 6 |
| UI | Test send | Easy | 4 |
| API | Save template | Easy | 4 |
| API | Render with data | Medium | 6 |
| API | Test send | Easy | 4 |
| API | Resolve template | Easy | 4 |
| Database | Notification template store | Easy | 2 |
| Testing | Template rendering tests | Medium | 6 |
| Documentation | Notification template guide | Easy | 2 |

**Feature Total: 42 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 18 | 2 | 0 | 6 | 2 | **42** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
