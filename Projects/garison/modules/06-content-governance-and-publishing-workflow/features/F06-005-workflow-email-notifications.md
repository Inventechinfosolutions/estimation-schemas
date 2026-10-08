# F06-005 — Workflow Email Notifications

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-005 |
| Feature Name | Workflow Email Notifications |
| Module | 06 — Content Governance & Publishing Workflow |
| Module Type | Business |
| Release | Go-live |

### Description
Email notifications for workflow events (submitted for review, changes requested, approved, published, re-verification due), with editable templates, recipient settings per event, queued dispatch with retry, and a delivery log. Provides the shared email connector used by all platform emails.

### Business Objective
Keep makers and reviewers informed without them polling the portal, and provide reliable email delivery for the whole platform.

### Actors
- Super Administrator
- All administrators (recipients)

### User Journey
1. **Who creates:** Notifications are created automatically by the system on workflow events; templates and recipient settings are maintained by the Super Administrator.
2. **How they create:** The Super Administrator edits a template (subject, body with placeholders such as product code, link, comment) and sets recipients per event (for example all Catalogue Reviewers).
3. **How they edit:** Templates and settings are edited at any time; changes apply to future emails.
4. **How they send for approval:** Notification configuration does not require approval.
5. **How the approver sees pending items:** There is no approver inbox; emails link directly to the review queue or item.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Administrators see emails in their mailbox; delivery history is visible to the Super Administrator.
8. **How the approver / auditor sees history:** The Super Administrator sees the delivery log (sent, failed, retried) and template changes in the audit log.

### Functional Capabilities
- Shared transactional email connector (SMTP or provider API) with queue, retry and bounce handling
- Event catalogue: submitted, changes requested, approved, published, unpublished, re-verification due, import completed
- Template editor with placeholders and preview
- Recipient settings per event (roles, specific users, item maker)
- Delivery log with retry of failed emails
- Per-user opt-out for non-critical notifications

### UI Screens
- Notification template list
- Notification template editor with placeholders and preview
- Notification recipient settings by event
- Email delivery log

### Logical API Operations
- Dispatch workflow notification through queue
- Render template with placeholders
- Save template and recipient settings
- Get delivery log
- Retry failed email

### Inputs
- Workflow events
- Template content
- Recipient settings

### Outputs
- Emails
- Delivery log

### Business Rules
- Emails are queued and never block workflow actions
- Failed emails retried up to 3 times with back-off
- Links in emails require sign-in

### Validations
- Template placeholders must be from the allowed list
- Sender domain configured (SPF/DKIM by Garrison)

### Calculations
- Retry back-off schedule

### Workflow
Queued → Sent | Failed → Retried → Sent | Failed

### Search Requirements
- Delivery log by event, recipient, status, date

### Documents
- None

### Reports
- Delivery log export

### Notifications
- This feature is the notification capability

### Security
- Templates and settings: Super Administrator

### Integrations
- Transactional email service / SMTP (Garrison-provided)

### Dependencies
- F06-002
- F06-003
- F06-004
- F07-003
- F10-002

### Assumptions
- Garrison provides an email account or provider with SPF/DKIM configured for the sending domain

### Risks
- Emails landing in spam if domain authentication is not configured

### Non Functional Requirements
- Emails dispatched within 1 minute of the event

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Notification template list | Easy | 4 |
| UI | Notification template editor with placeholders and preview | Medium | 6 |
| UI | Notification recipient settings by event | Medium | 6 |
| UI | Email delivery log | Medium | 6 |
| API | Dispatch workflow notification through queue | Complex | 8 |
| API | Render template with placeholders | Medium | 6 |
| API | Save template and recipient settings | Easy | 4 |
| API | Get delivery log | Medium | 6 |
| API | Retry failed email | Easy | 4 |
| Database | Notification templates and settings | Easy | 2 |
| Database | Email delivery log | Easy | 2 |
| Integration | Transactional email service connector with retry and bounce handling | Medium | 16 |
| Testing | Event-to-email mapping and placeholders | Medium | 6 |
| Testing | Retry and failure handling | Easy | 4 |
| Documentation | Notification configuration guide | Simple | 1 |

**Feature Total: 81 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 28 | 4 | 16 | 10 | 1 | **81** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Email connector with retry estimated once here and reused (Simple rows) by other features
