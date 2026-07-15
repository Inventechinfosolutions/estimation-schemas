# F11-004 — OTP Notification Flow

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-004 |
| **Feature Name** | OTP Notification Flow |
| **Module** | 11 — Notification Service |

### Description
Issue and verify one-time passwords for configured LMS identity and transaction-confirmation journeys using the SMS dispatch service.

### Business Objective
Provide a controlled second-factor/verification step where LMS requires it.

### Actors
- Citizen/applicant; officer; System

### User Journey
1. User requests OTP → system sends code → user enters code → system validates expiry and attempt limits → journey continues or fails.

### Functional Capabilities
- OTP request; code issuance; resend cooldown; verification; expiry; attempt limits; verified-state handoff.

### Inputs
- Recipient identifier, purpose, requested action, entered OTP.

### Outputs
- Send acknowledgement and verification result.

### Business Rules
- OTPs are purpose-bound, time-limited, single-use, and rate-limited; business modules decide when OTP is required.

### Validations
- Valid recipient; configured purpose; unexpired code; maximum attempts and resend limits.

### Calculations
- Attempt count and expiry window enforcement.

### Workflow
- Request → send through F11-002 → verify → expire/lock after limits.

### Search Requirements
- Operations lookup by request status/date only; no plaintext OTP search.

### Documents
- None.

### Reports
- OTP request and verification outcome extract.

### Notifications
- Uses SMS dispatch for code delivery.

### Security
- No plaintext OTP in logs; hashed/secured verification state; anti-enumeration controls.

### Integrations
- Internal SMS dispatch service (Simple).

### Dependencies
- Module 01 and citizen/public journeys; F11-002.

### Assumptions
- SMS delivery is estimated in F11-002; this feature owns OTP control flow.

### Risks
- Delayed SMS may cause abandonment; fallback policy requires BDA decision.

### Non Functional Requirements
- Short response time; resilient resend handling; security event logging.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| OTP request/verify interaction | UI | Easy | 4 |
| OTP issue and verification operations | API | Medium | 6 |
| OTP verification state | Database | Easy | 2 |
| SMS dispatch handoff | Integration | Simple | 4 |
| OTP flow tests | Testing | Complex | 8 |
| OTP user guidance | Documentation | Easy | 2 |
| **Total** | | | **26** |

### Estimation Assumptions
- Estimation uses only the Estimation Master values. SMS delivery is estimated in F11-002; this feature owns OTP control flow.
