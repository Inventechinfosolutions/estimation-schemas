# F14-002 — Email Delivery of Auction Notifications

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F14-002 |
| **Feature Name** | Email Delivery of Auction Notifications |
| **Module** | 14 — Notifications |

### Description
The same lifecycle events that create an in-portal alert are also emailed to the recipient’s recorded address. Delivery success or failure is stored so an administrator can see that a message failed. A failed email does not undo publication, approval, closure, or award. SMS is not sent.

### Business Objective
People who are not currently on the portal still receive the lifecycle message, and staff can see when email did not go out.

### Actors
The system sends. The System / Catalogue Administrator reads the delivery log. Recipients are staff and bidders. Approver: none.

### User Journey
1. Who creates: the lifecycle event creates the email. The administrator does not type each one.
2. How they create: after F14-001 stores the alert, this feature sends the email to the address on the staff account or the bidder profile.
3. How they edit: the administrator does not edit a sent message. They can see the failure and rely on the in-portal alert. A manual resend of a failed message is available from the log.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no approval inbox. The delivery log is an operational list.
6. How the approver decides: there is no auction decision. Resend is an operational retry.
7. How the maker sees history: the administrator sees queued, sent, or failed, with the time and the event type, not the full text of another bidder’s letter in a shared export.
8. How the auditor sees history: the same log is the audit of delivery. The business history of the auction remains Module 15.

### Functional Capabilities
- Email each lifecycle event to the recipient address
- Record sent or failed
- Allow a failed message to be resent
- Leave the business action standing when email fails
- Do not send SMS

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Lifecycle event
- Recipient email address

### Outputs
- An email and a delivery log row

### Business Rules
- The address is the official email on the staff account or the bidder profile.
- Bidder-specific events go only to that bidder’s address.
- Failure does not revert the auction status.
- Password-reset messages from staff and bidder sign-in use this same delivery path.
- SMS is out of scope and has no sender.

### Validations
- An address is present. If it is missing, the log records failed and the in-portal alert still exists.
- Resend is available only to the administrator.
- The event is one of the named lifecycle events or a password reset.

### Calculations
None.

### Workflow
Alert created → email attempted → sent or failed. Resend retries a failure. No approval.

### Search Requirements
Delivery log by auction, event type, recipient, and sent or failed.

### Documents
None.

### Reports
The delivery log is the operational list.

### Notifications
This feature is the email channel for Module 14.

### Security
The log does not become a way to read another bidder’s letter body from a general screen. The log shows event, auction, recipient, and outcome. The letter itself stays in Module 13.

### Integrations
The organisation’s email service. This is the only external delivery channel in the system.

### Dependencies
F14-001. Organisation-provided email service. Addresses from F01-001 and F03-004.

### Assumptions
- The email service is supplied and reachable by the organisation. Credentials for that service are an operational dependency.
- Retry of a failed send is a single administrator resend plus the initial attempt. There is no unbounded automatic retry loop specified by the source.

### Risks
If the organisation’s email service is down, users still have the in-portal alert. They will not see email until it is resent.

### Non Functional Requirements
Email failure is recorded and does not roll back the business transaction that raised the event.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Email delivery log | UI | Medium | 6 |
| Send lifecycle email | API | Medium | 6 |
| Resend failed email | API | Easy | 4 |
| Email delivery service | Integration | Medium | 16 |
| Email delivery log records | DB | Easy | 2 |
| Email delivery tests | Testing | Complex | 8 |
| Email delivery notes | Documentation | Medium | 3 |

**Feature total: 45 hours**
