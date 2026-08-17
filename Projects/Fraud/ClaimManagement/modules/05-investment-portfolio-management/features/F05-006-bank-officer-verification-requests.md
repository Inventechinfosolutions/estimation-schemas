# F05-006 — Bank-officer verification requests

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-006 |
| **Feature Name** | Bank-officer verification requests |
| **Module** | 05 — Investment Portfolio Management |

### Description
The Officer records the bank officer’s email on the investment or return. Unless the bank has already submitted the data, the Officer triggers a verification request to that email and later records the reply or timeout against the same record.

### Business Objective
Trigger bank-officer email verification when data was not already submitted, and record reply or timeout.

### Actors
Officer; bank officer (external, via email — not an application Person by default).

### User Journey
1. Officer records the bank officer’s email on the investment or return.
2. If the bank has not already submitted the data, Officer triggers a verification request to that email.
3. Officer later records the reply or timeout against the same record.

### Functional Capabilities
- Capture bank officer email on the investment or return.
- Skip request if data already submitted.
- Send verification request email.
- Record reply or timeout on the same record.

### Inputs
Bank officer email, investment/return reference, reply content or timeout.

### Outputs
Request sent; reply or timeout recorded.

### Business Rules
- Do not send if the bank has already submitted the data.
- Bank officer is not an application Person by default.

### Validations
- Email format.
- Request requires an investment or return record.

### Calculations
Timeout against the request timestamp per policy.

### Workflow
Record email → (optional) send → reply/timeout. Embedded notification, not a standalone notification service.

### Search Requirements
Investment/return, request status (sent, replied, timed out).

### Documents
Reply attachments if any.

### Reports
Open bank-verification request list.

### Notifications
Email to bank officer.

### Security
Emails contain only what policy allows. Request events audited.

### Integrations
Bank-officer email send.

### Dependencies
F05-001 / F05-005 records.

### Assumptions
- Official email gateway is available. No generative email drafting.

### Risks
- Sending requests when data already exists would harass banks and duplicate work.

### Non Functional Requirements
Request/reply trail is auditable.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Bank-officer email and request screen | UI | Medium | 6 |
| Request, reply and timeout operations | API | Complex | 8 |
| Verification-request persistence | DB | Easy | 2 |
| Bank-officer email send | Integration | Easy | 8 |
| Bank-officer request tests | Testing | Medium | 6 |
| Bank-officer request note | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Email integration is Easy (REST/SMTP send), not a payment rail.
