# F05-004 — Result Intimation Dispatch & Delivery Status

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-004 |
| Feature Name | Result Intimation Dispatch & Delivery Status |
| Module | 05 — Successful Bidder Notification & Account |
| Module Type | Business |
| Release | Go-live |

### Description
Dispatch of the signed intimation letter and portal login instructions to the bidder by e-mail (PDF attached) and SMS (link), optionally WhatsApp, with delivery status tracking, resend, and manual recording of physical dispatch by registered post / speed post where required.

### Business Objective
Ensure and prove that each bidder was intimated, since the payment timeline runs from intimation.

### Actors
- System
- Auction Admin
- Successful Bidder

### User Journey
1. **Who creates:** The system dispatches automatically on signing.
2. **How they create:** Signed letters trigger e-mail and SMS; the Auction Admin can also record postal dispatch with consignment number.
3. **How they edit:** The Auction Admin can resend to the same or corrected contact.
4. **How they send for approval:** No approval.
5. **How the approver sees pending items:** The Auction Admin sees undelivered intimations in an exception list.
6. **How the approver decides:** The Auction Admin decides to resend or dispatch by post.
7. **How the applicant / maker sees history:** The bidder sees the letter and dispatch date in the portal.
8. **How the approver / auditor sees history:** Auditors see each dispatch attempt and delivery status.

### Functional Capabilities
- Automatic e-mail and SMS dispatch
- Optional WhatsApp dispatch
- Delivery status capture from gateways
- Undelivered exception list and resend
- Postal dispatch recording with proof
- Intimation acknowledgement on first bidder login

### UI Screens
- Dispatch status by auction
- Undelivered exceptions and resend
- Postal dispatch entry

### Logical API Operations
- Dispatch intimation on signing
- Update delivery status
- Resend intimation
- Record postal dispatch
- Record first-login acknowledgement
- List dispatch status

### Inputs
- Signed letter
- Contact details
- Postal details

### Outputs
- Dispatch records
- Delivery status

### Business Rules
- Dispatch only after signature
- Every resend is logged

### Validations
- Contact present

### Calculations
- None

### Workflow
Queued → Sent → Delivered | Failed → Resent / Posted

### Search Requirements
- By auction, bidder, status

### Documents
- Postal receipt scan

### Reports
- Intimation dispatch report

### Notifications
- The intimation itself

### Security
- Letter link requires login

### Integrations
- E-mail, SMS, WhatsApp through F12-003

### Dependencies
- F05-003
- F12-002
- F12-003

### Assumptions
- DLT templates approved

### Risks
- Undelivered messages; postal fallback

### Non Functional Requirements
- Dispatch within 15 minutes of signing

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Dispatch status by auction | Medium | 6 |
| UI | Undelivered exceptions and resend | Easy | 4 |
| UI | Postal dispatch entry | Easy | 4 |
| API | Dispatch intimation on signing | Medium | 6 |
| API | Update delivery status | Easy | 4 |
| API | Resend intimation | Easy | 4 |
| API | Record postal dispatch | Easy | 4 |
| API | Record first-login acknowledgement | Simple | 2 |
| API | List dispatch status | Easy | 4 |
| Database | Dispatch and delivery log per letter | Easy | 2 |
| Testing | Dispatch, failure and resend tests | Medium | 6 |
| Documentation | Dispatch procedure | Simple | 1 |

**Feature Total: 47 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 24 | 2 | 0 | 6 | 1 | **47** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Gateways via Notification Service; no Integration row
- No external integration channel in this feature; Integration row omitted.
