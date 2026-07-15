# F11-002 — SMS Dispatch Service

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-002 |
| **Feature Name** | SMS Dispatch Service |
| **Module** | 11 — Notification Service |

### Description
Send LMS OTPs, workflow alerts, and auction/allotment notices through the mandated SMS gateway with delivery-state handling.

### Business Objective
Provide reliable SMS delivery for mandatory LMS communications.

### Actors
- System; Super Administrator; notification operations users

### User Journey
1. A business event selects a template and recipient → service sends SMS → provider status is recorded → failures are visible.

### Functional Capabilities
- Template-variable rendering; sender/template mapping; priority sends; delivery status capture; retry classification; health visibility.

### Inputs
- Mobile number, approved template, variables, priority, source reference.

### Outputs
- Provider message reference, delivery/failure state.

### Business Rules
- Content templates are configured in Module 02; only approved templates may be dispatched.

### Validations
- Mobile format, required template values, configured sender/template mapping.

### Calculations
- Delivery success/failure counts.

### Workflow
- Queue → send → provider acknowledgement → delivery update/retry.

### Search Requirements
- By date, recipient, provider reference, source, and delivery state.

### Documents
- Provider onboarding and template-registration records.

### Reports
- SMS delivery/failure extracts.

### Notifications
- Sends the notification requested by LMS producers.

### Security
- Restricted gateway credentials; authenticated delivery callbacks; masked mobile numbers in operations views.

### Integrations
- SMS Gateway — Medium (16), including auth, mapping, and retry.

### Dependencies
- Module 02 templates; Module 01 identities; F11-006 logging.

### Assumptions
- BDA supplies active gateway credentials and DLT approvals.

### Risks
- Provider throttling or template rejection can delay delivery.

### Non Functional Requirements
- OTP-priority lane; provider-limit-aware throughput; observable failure rates.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| SMS dispatch configuration | UI | Easy | 4 |
| SMS send and delivery-state operations | API | Medium | 6 |
| SMS provider mapping and delivery state | Database | Easy | 2 |
| SMS Gateway integration | Integration | Medium | 16 |
| SMS dispatch tests | Testing | Complex | 8 |
| SMS dispatch guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Estimation uses only the Estimation Master values. BDA supplies active gateway credentials and DLT approvals.
