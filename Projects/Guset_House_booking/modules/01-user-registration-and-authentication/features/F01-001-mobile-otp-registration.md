# F01-001 — Mobile OTP Registration

| Field | Value |
|-------|-------|
| Feature ID | F01-001 |
| Feature Name | Mobile OTP Registration |
| Module | 01 — User Registration & Authentication |
| Type | Shared |
| Notes | Go-live |

## Feature Specification

### Description
Allows a government employee to start registration using a mobile number and complete OTP-based verification before profile continuation.

### Business Objective
Establish a verified mobile identity for each employee user as the first gate to platform access.

### Actors
- Employee Guest
- Platform Administrator

### User Journey
1. Employee Guest creates the registration by entering mobile number on the registration screen.
2. Employee requests OTP; system sends OTP via notification channel and employee enters the code to verify.
3. Employee may re-request OTP within rate limits; verified mobile cannot be freely edited without re-verification.
4. Submit/approval does not apply — OTP verification is the gate, not an approver inbox.
5. There is no approver inbox for OTP registration.
6. There is no approver decision on this feature.
7. Employee sees registration progress and OTP status on the registration flow; failed attempts show safe messages.
8. Auditor/Administrator may view registration attempt history (mobile masked) from user audit views in Module 06/01 admin tools.

### Functional Capabilities
- Request OTP for mobile
- Verify OTP
- Resend OTP with cooldown
- Block disposable/invalid numbers per policy
- Persist verified mobile on user draft

### UI Screens
- Employee mobile registration screen
- OTP verification screen
- OTP resend confirmation popup

### Logical API Operations
- Request registration OTP
- Verify registration OTP
- Resend registration OTP

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- OTP required before continuing registration
- OTP expiry and attempt limits enforced
- One active registration OTP challenge per mobile

### Validations
- Mobile number mandatory and valid format
- OTP length/format validation
- Cooldown between resends

### Calculations
- OTP expiry remaining seconds

### Workflow
MobileEntered → OTPSent → OTPVerified | OTPFailed/Expired → Retry

### Search Requirements
Admin search of registration attempts by masked mobile/date (operational)

### Documents
None beyond on-screen instructions

### Reports
None in this feature

### Notifications
OTP SMS/email via Notification Service

### Security
- Rate limit OTP requests
- Do not reveal whether mobile already registered beyond safe messaging
- Mask mobile in logs

### Integrations
Notification Service / Integration Hub SMS

### Dependencies
- F07-002
- F08-002

### Assumptions
- SMS provider provisioned
- India mobile format assumed unless configured

### Risks
- SMS delivery delay blocks registration

### Non Functional Requirements
- OTP verify response under 2s excluding SMS latency

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Employee mobile registration screen | Medium | 6 |
| UI | OTP verification screen | Easy | 4 |
| UI | OTP resend confirmation popup | Simple | 2 |
| API | Request registration OTP | Medium | 6 |
| API | Verify registration OTP | Complex | 8 |
| API | Resend registration OTP | Easy | 4 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 40 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: SMS provider provisioned, India mobile format assumed unless configured / SMS delivery delay blocks registration.
