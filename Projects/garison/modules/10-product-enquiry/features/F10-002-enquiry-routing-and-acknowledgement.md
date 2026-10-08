# F10-002 — Enquiry Routing & Acknowledgement

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-002 |
| Feature Name | Enquiry Routing & Acknowledgement |
| Module | 10 — Product Enquiry |
| Module Type | Business |
| Release | Go-live |

### Description
Route each enquiry by email to Garrison recipients according to rules (default recipients plus optional per-category recipients), with product code, name and link in the email; send an acknowledgement to the visitor; editable email templates.

### Business Objective
Make sure every enquiry reaches the right Garrison person quickly with enough context to respond.

### Actors
- Super Administrator / Catalogue Administrator (routing settings)
- Garrison enquiry recipients
- Visitor

### User Journey
1. **Who creates:** Routing emails are created automatically when an enquiry is submitted; the administrator configures routing rules and templates.
2. **How they create:** The administrator sets default recipients and optional per-category recipients, and edits the Garrison notification and visitor acknowledgement templates.
3. **How they edit:** They edit rules and templates at any time; changes apply to new enquiries.
4. **How they send for approval:** No approval applies.
5. **How the approver sees pending items:** There is no approver inbox; recipients receive emails in their mailbox.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Visitors receive the acknowledgement; administrators see the email status in the enquiry detail.
8. **How the approver / auditor sees history:** Auditors see routing rule changes in the audit log and email delivery in the delivery log (F06-005).

### Functional Capabilities
- Default recipients and per-category routing rules
- Garrison notification email with enquiry details, product code, name and link
- Visitor acknowledgement email
- Editable templates with placeholders
- Delivery status recorded on enquiry

### UI Screens
- Enquiry routing rules settings
- Enquiry email template editors

### Logical API Operations
- Resolve recipients by routing rules
- Dispatch Garrison enquiry notification
- Dispatch visitor acknowledgement
- Save routing rules

### Inputs
- Enquiry record
- Routing rules
- Templates

### Outputs
- Notification and acknowledgement emails
- Delivery status

### Business Rules
- If no category rule matches, default recipients receive the enquiry
- Reply-to on Garrison email is the visitor's email
- Acknowledgement never includes internal recipient addresses

### Validations
- Recipient emails valid; at least one default recipient

### Calculations
- None

### Workflow
Enquiry submitted → Recipients resolved → Emails queued → Sent/Failed

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- This feature is the enquiry notification capability

### Security
- Routing settings restricted to administrators

### Integrations
- Transactional email service (shared connector)

### Dependencies
- F10-001
- F06-005
- F10-003

### Assumptions
- Garrison provides enquiry recipient addresses before build

### Risks
- Enquiry emails filtered as spam by Garrison mail systems; whitelist sender

### Non Functional Requirements
- Garrison notified within 1 minute

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Enquiry routing rules settings | Medium | 6 |
| UI | Enquiry email template editors | Easy | 4 |
| API | Resolve recipients by routing rules | Medium | 6 |
| API | Dispatch Garrison enquiry notification | Medium | 6 |
| API | Dispatch visitor acknowledgement | Easy | 4 |
| API | Save routing rules | Easy | 4 |
| Database | Enquiry routing rules | Simple | 1 |
| Integration | Enquiry emails through shared email connector | Simple | 4 |
| Testing | Routing rules matrix | Medium | 6 |
| Testing | Email content and delivery failure handling | Easy | 4 |
| Documentation | Enquiry routing configuration guide | Simple | 1 |

**Feature Total: 46 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 20 | 1 | 4 | 10 | 1 | **46** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Reuses email connector from F06-005
