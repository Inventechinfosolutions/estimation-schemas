# F09-006 — OTP Messaging Support

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F09-006 |
| **Feature Name** | OTP Messaging Support |
| **Module** | 09 — Notification Service |

### Description
Specialized high-priority OTP message dispatch path for authentication and optional 2FA, with tight TTL handling and privacy-preserving logs, used by Module 01.

### Business Objective
Deliver OTPs quickly and securely for login/2FA/reset flows.

### Actors
- System (Module 01 auth), End users (recipients)

### User Journey
1. Module 01 requests OTP send to mobile/email.
2. Notification service dispatches via high-priority queue.
3. Module 01 verifies OTP (verification logic remains Module 01); this feature ensures delivery.

### Functional Capabilities
- High-priority OTP send API
- Template for OTP messages
- Suppress full OTP in durable logs (mask)
- Coalesce/resend cooldown support signals to Module 01
- Prefer SMS with email fallback if configured

### Inputs
- Destination, OTP payload/ref, TTL hint, purpose code

### Outputs
- Dispatch result; provider id

### Business Rules
- OTP verification and generation owned by Module 01 (F01-002/003).
- This feature is channel delivery specialization on F09-001.
- No WhatsApp OTP baseline.

### Validations
- Purpose allow-list; destination present

### Calculations
None.

### Workflow
N/A.

### Search Requirements
Ops may see “OTP sent” events without code (F09-004 masking).

### Documents
None.

### Reports
OTP send success/failure rates (ops).

### Notifications
N/A.

### Security
Mask OTP; prioritize TLS; anti-abuse via Module 01 rate limits.

### Integrations
Uses F09-001 channels.

### Dependencies
F09-001/002/004; Module 01 auth features

### Assumptions
- Does not duplicate Module 01 OTP validate hours.
- Complex API for priority path + privacy controls.

### Risks
- SMS latency for 2FA mandatory roles — operational SOP for outages.

### Non Functional Requirements
- p95 dispatch enqueue < 1s under normal load; provider SLA separate

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| OTP send status (minimal UX) | UI | Simple | 2 |
| OTP issue/verify support ops | API | Complex | 8 |
| OTP challenge persistence | Database | Easy | 2 |
| OTP notification tests | Testing | Complex | 8 |
| OTP messaging notes | Documentation | Simple | 1 |
| **Total** | | | **21** |

### Estimation Assumptions
- Minimal UI; Module 01 owns challenge screens.
