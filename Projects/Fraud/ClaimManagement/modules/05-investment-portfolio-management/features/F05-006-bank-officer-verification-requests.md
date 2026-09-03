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
1. Who creates: Officer
2. How they create: Officer records the bank officer’s email on the investment or return.
3. How they edit: If the bank has not already submitted the data, Officer triggers a verification request to that email.
4. How they send for approval: Officer later records the reply or timeout against the same record. Record email → (optional) send → reply/timeout. Embedded notification, not a standalone notification service.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Capture bank officer email on the investment or return.
- Skip request if data already submitted.
- Send verification request email.
- Record reply or timeout on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My bank-officer verification requests list / queue | Medium |
| Bank-officer email and request screen | Medium |
| Bank-officer verification requests history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Request, reply and timeout operations | Complex |
| Update bank-officer verification requests | Medium |
| Search bank-officer verification requests | Medium |
| Read bank-officer verification requests history | Easy |

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
| My bank-officer verification requests list / queue | UI | Medium | 6 |
| Bank-officer email and request screen | UI | Medium | 6 |
| Bank-officer verification requests history | UI | Medium | 6 |
| Request, reply and timeout operations | API | Complex | 8 |
| Update bank-officer verification requests | API | Medium | 6 |
| Search bank-officer verification requests | API | Medium | 6 |
| Read bank-officer verification requests history | API | Easy | 4 |
| Verification-request persistence | DB | Easy | 2 |
| Bank-officer email send | Integration | Easy | 8 |
| Bank-officer verification requests feature tests | Testing | Medium | 6 |
| Bank-officer verification requests implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **60** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
