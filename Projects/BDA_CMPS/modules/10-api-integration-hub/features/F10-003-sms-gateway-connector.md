# F10-003 — SMS Gateway Connector

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F10-003 |
| **Feature Name** | SMS Gateway Connector |
| **Module** | 10 — API / Integration Hub |

### Description
SMS gateway connector with auth, template/sender mapping, send API, delivery report webhook (if available), and retry-friendly error mapping for Module 09.

### Business Objective
Reliable SMS for OTPs, notices, and reminders.

### Actors
- Tech admin, Module 09 dispatch engine

### User Journey
1. Module 09 calls hub SMS send.
2. Hub authenticates to provider, sends, returns provider id.
3. Optional DLR webhook updates status via hub to Module 09 logs.

### Functional Capabilities
- Send SMS
- Sender ID / template id mapping (DLT-style if required in India)
- DLR webhook intake
- Error code mapping; retryable classification
- Health check

### Inputs
- Mobile, message/template vars, priority

### Outputs
- Provider message id; accept/reject

### Business Rules
- Content/policy in Modules 02/09.
- **Reconcile:** F09-001 Easy (8) consumption remains; this feature owns Medium integration (auth+mapping+retry).

### Validations
- E.164/IN mobile normalization; blocked list optional

### Calculations
None.

### Workflow
Send → (DLR) → Status.

### Search Requirements
Ops via Module 09 logs primarily.

### Documents
Provider onboarding checklist (DLT registrations BDA responsibility).

### Reports
Provider error extracts.

### Notifications
Connector down alerts.

### Security
Credential protection; webhook auth.

### Integrations
SMS Gateway — **Medium (16)**.

### Dependencies
F10-001; Module 09

### Assumptions
- India DLT template registration is BDA/ops dependency, not coding hours beyond mapping.
- Medium complexity for auth+mapping+retry.

### Risks
- DLT rejection of templates delays go-live.

### Non Functional Requirements
- OTP priority lane support; batch throughput

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| SMS connector config UI | UI | Easy | 4 |
| SMS send/status facade | API | Medium | 6 |
| SMS message map entities | Database | Easy | 2 |
| SMS Gateway integration | Integration | Medium | 16 |
| SMS connector tests | Testing | Complex | 8 |
| SMS connector guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Not Very High (reserved for GIS/Payment/ERP-class).
