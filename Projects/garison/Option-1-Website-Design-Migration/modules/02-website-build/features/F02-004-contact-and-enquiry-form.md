# F02-004 — Contact & Enquiry Form

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-004 |
| Feature Name | Contact & Enquiry Form |
| Module | 02 — Website Build |
| Module Type | Business |
| Release | Go-live |

### Description
Contact page with enquiry form (name, email, phone, company, subject, message, optional product reference), validation, spam protection, email delivery to Garrison's mailbox and an acknowledgement email to the visitor, plus confirmation and error states. Delivered with a small serverless or hosted form handler, so no database or admin is needed.

### Business Objective
Turn website visits into enquiries delivered straight to Garrison's existing mailbox.

### Actors
- Visitor
- Garrison staff (enquiry recipients)

### User Journey
1. **Who creates:** Visitors create enquiries.
2. **How they create:** The visitor fills in the form and submits it; the handler validates it and sends the emails.
3. **How they edit:** Visitors can correct errors before submitting; sent enquiries are not edited.
4. **How they send for approval:** No approval applies; enquiries go straight to Garrison's mailbox.
5. **How the approver sees pending items:** Garrison staff see enquiries in their existing Google Workspace mailbox; there is no new inbox.
6. **How the approver decides:** Garrison staff reply from email; no in-system decision.
7. **How the maker sees history:** Visitors receive an acknowledgement email.
8. **How the approver / auditor sees history:** Garrison keeps enquiries in its mailbox.

### Functional Capabilities
- Enquiry form with validation
- Spam protection
- Email to Garrison and acknowledgement to visitor
- Confirmation and error states
- Optional product reference field (used by F03-005)

### UI Screens
- Contact page with enquiry form
- Form confirmation and error states

### Logical API Operations
- Submit enquiry with validation
- Send enquiry email to Garrison and acknowledgement to visitor
- Spam protection check

### Inputs
- Visitor contact details and message

### Outputs
- Enquiry email to Garrison
- Acknowledgement email

### Business Rules
- Enquiries are not stored on the website
- Recipient address configurable by a developer

### Validations
- Required fields, email format, message length limit

### Calculations
- None

### Workflow
Filled → Validated → Sent → Acknowledged

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- Enquiry email to Garrison
- Acknowledgement email to visitor

### Security
- Spam protection, rate limiting and input escaping
- Email sending domain authenticated (SPF/DKIM) alongside Google Workspace records

### Integrations
- Transactional email service
- Spam protection service

### Dependencies
- F02-001
- F05-002

### Assumptions
- Garrison's existing Google Workspace mailbox receives enquiries

### Risks
- Misconfigured email authentication sends enquiries to spam; tested before go-live

### Non Functional Requirements
- Submission response under 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Contact page with enquiry form | Medium | 6 |
| UI | Form confirmation and error states | Easy | 4 |
| API | Submit enquiry with validation | Medium | 6 |
| API | Send enquiry email to Garrison and acknowledgement to visitor | Medium | 6 |
| API | Spam protection check | Easy | 4 |
| Integration | Transactional email service | Easy | 8 |
| Integration | Spam protection service (for example Turnstile or reCAPTCHA) | Simple | 4 |
| Testing | Enquiry delivery and spam tests | Medium | 6 |
| Documentation | Enquiry routing note | Simple | 1 |

**Feature Total: 45 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 16 | 0 | 12 | 6 | 1 | **45** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Serverless handler; no enquiry database
