# F04-005 — Registration Confirmation and Status

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-005 |
| **Feature Name** | Registration Confirmation and Status |
| **Module** | 04 — Candidate Registration and Fee Payment |

### Description
After identity, preferences and mandatory payment (where applicable) succeed, the system issues a unique registration/application number, stores the application pack (examination, preferences, documents, payment), shows a confirmation to the candidate, and allows ongoing status viewing from the candidate login.

### Business Objective
Give every successful candidate an immutable registration reference and a clear status view of what was submitted, paid and verified, for use through scheduling, hall ticket and examination.

### Actors
Maker: Candidate (receives confirmation). Approver: none for number issuance (system issues on gate success). Auditor: Examination Administrator.

### User Journey
1. Who creates: The system issues the unique registration number when the candidate’s draft satisfies completion gates (identity + preferences + payment where mandatory + document where Type 2).
2. How they create: Candidate reaches confirmation step after payment gate → system persists application pack → issues unique registration/application number → shows confirmation screen with key particulars.
3. How they edit: Candidate cannot edit the issued registration number; demographic/preference edits after issue follow Department lock rules (normally locked; corrections via admin process if configured). Status view is read-oriented for the candidate.
4. How they send for approval: Does not apply for number issuance; if admin verification is configured, the completed registration becomes visible in F04-006 inbox without a separate “send” action beyond completion.
5. How the approver sees pending items: No confirmation approver inbox here; F04-006 owns verification inbox.
6. How the approver decides: No decision in this feature.
7. How the applicant / maker sees history: Candidate opens registration status from login to see number, examination, preferences, payment/receipt, document presence, verification status and timeline.
8. How the approver / auditor sees history: Administrator views the stored application pack and status timeline on the registration record.

### Functional Capabilities
- Enforce completion gates before issuing registration number.
- Generate unique registration/application number.
- Persist application pack: identity, examination, two preferences, documents (if any), payment/receipt linkage.
- Display confirmation with registration number and key summary.
- Provide candidate status view from login after OTP authentication.
- Show status timeline (drafted, paid, confirmed, verification pending/approved/returned as applicable).
- Prevent duplicate number issuance for the same completed draft.
- Allow candidate to locate own registrations when multiple examinations exist.
- Keep confirmation immutable for number and critical paid facts.
- Audit number issuance and pack persistence events.
- Feed downstream scheduling/allocation eligibility with confirmed registrations.

### UI Screens
| Screen | Purpose |
|---|---|
| Registration confirmation screen | Show unique number and success summary |
| Stored application pack view screen | Read-only pack of exam, preferences, payment, documents |
| Candidate registration status dashboard | List/status of candidate’s registrations |
| Registration status timeline screen | Chronological status events |
| Candidate own-registration search screen | Find own registration by number/exam |

### Logical API operations
| Operation | Purpose |
|---|---|
| Issue unique registration number | Generate and assign number when gates pass |
| Persist completed application pack | Store pack linked to number |
| Get registration confirmation details | Return confirmation payload for display |
| Get candidate registration status | Return status and pack summary |
| Get registration status timeline | Return chronological events |
| Search candidate own registrations | Locate registrations for logged-in candidate |

### Inputs
Completed draft satisfying gates; payment-gate flag; document-present flag for Type 2; candidate session.

### Outputs
Unique registration/application number; stored application pack; confirmation view; status and timeline for candidate and admin.

### Business Rules
- Number issued only after mandatory payment success where fee applies, and Type 2 document association where required.
- Registration number is unique and visible in candidate login.
- Confirmation does not itself allocate a centre or publish a hall ticket.
- Admin verification state (if configured) is displayed but decided in F04-006.

### Validations
- All completion gates true before issue.
- Idempotent issue if confirmation is retried after success.
- Candidate may view only own registrations.

### Calculations
None beyond status derivation from underlying events.

### Workflow
Payment gate open (or zero-fee acknowledged) → issue number → persist pack → show confirmation → candidate may reopen status anytime. No approval decision here.

### Search Requirements
Candidate search of own registrations; admin search covered primarily in F04-006.

### Documents
Application pack references prior uploads/receipts; no new upload here.

### Reports
Confirmed registration counts feed Module 09.

### Notifications
Registration confirmation notification via Module 09 channels as configured.

### Security
Number issuance server-controlled; candidate scoped reads; audited issue events.

### Integrations
None directly (uses payment outcome from F04-004).

### Dependencies
F04-001–F04-004; Module 02 login for status; consumed by Modules 05–08.

### Assumptions
- Numbering format approved by Department.
- Verification workflow hours sit on F04-006.
- Six logical APIs estimated independently including confirmation get.

### Risks
Race on double-submit could attempt duplicate issue without idempotency; status confusion if verification pending is not labelled clearly.

### Non Functional Requirements
Idempotent issuance; durable pack storage; clear confirmation UX on mobile and desktop portal.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Registration confirmation screen | UI | Complex | 12 |
| Stored application pack view screen | UI | Complex | 12 |
| Candidate registration status dashboard | UI | Medium | 6 |
| Registration status timeline screen | UI | Easy | 4 |
| Candidate own-registration search screen | UI | Easy | 4 |
| Issue unique registration number | API | Complex | 8 |
| Persist completed application pack | API | Complex | 8 |
| Get registration confirmation details | API | Medium | 6 |
| Get candidate registration status | API | Medium | 6 |
| Get registration status timeline | API | Easy | 4 |
| Search candidate own registrations | API | Medium | 6 |
| Registration number and application pack persistence | Database | Medium | 4 |
| Registration confirmation and status tests | Testing | Medium | 6 |
| Registration confirmation and status documentation | Documentation | Easy | 2 |

**Feature total: 88 hours**

### Estimation Assumptions
- Payment initiation/callback remain on F04-004.
- Admin verification UI/API remain on F04-006.
