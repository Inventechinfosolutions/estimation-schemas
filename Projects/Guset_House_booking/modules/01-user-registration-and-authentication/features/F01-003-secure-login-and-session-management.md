# F01-003 — Secure Login and Session Management

| Field | Value |
|-------|-------|
| Feature ID | F01-003 |
| Feature Name | Secure Login and Session Management |
| Module | 01 — User Registration & Authentication |
| Type | Shared |
| Notes | Go-live |

## Feature Specification

### Description
Authenticates registered users and maintains secure sessions for employee and administrative portals.

### Business Objective
Provide controlled access to the platform with session timeout and secure credential handling.

### Actors
- Employee Guest
- Site Administrator
- Platform Administrator

### User Journey
1. Registered user creates a login session by entering credentials (mobile/username + secret or OTP-assisted login per policy).
2. User submits login form; system validates identity and account status.
3. User may update password/secret via profile security settings when enabled.
4. Approval does not apply to login.
5. No approver inbox.
6. No approver decision.
7. User sees own active session/device list if exposed; logout ends session.
8. Auditor reviews login success/failure history for investigations.

### Functional Capabilities
- Login
- Logout
- Session timeout/renewal
- Lockout after failed attempts
- View own profile security basics

### UI Screens
- Login screen
- Session timeout warning popup
- Logout confirmation popup
- Profile security settings screen

### Logical API Operations
- Authenticate user
- Refresh/validate session
- Logout
- Change password/secret

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Inactive or identity-rejected users cannot book even if login allowed for status view
- Session expires per policy
- Failed attempt lockout

### Validations
- Credentials required
- Account must exist and not be disabled

### Calculations
- Session remaining time

### Workflow
CredentialsSubmitted → Authenticated → ActiveSession → Expired/LoggedOut | Locked

### Search Requirements
Admin/auditor login audit search

### Documents
None

### Reports
None

### Notifications
Optional login alert on new device

### Security
- Hashed secrets
- HTTPS-only cookies/tokens
- Rate limit login

### Integrations
Optional OTP via Notification Service if OTP login enabled

### Dependencies
- F01-001
- F01-002

### Assumptions
- Password or OTP-login policy chosen at implementation kickoff

### Risks
- Credential stuffing without rate limits

### Non Functional Requirements
- Login API p95 under 1s excluding external OTP

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Login screen | Medium | 6 |
| UI | Session timeout warning popup | Simple | 2 |
| UI | Logout confirmation popup | Simple | 2 |
| UI | Profile security settings screen | Easy | 4 |
| API | Authenticate user | Complex | 8 |
| API | Refresh/validate session | Medium | 6 |
| API | Logout | Simple | 2 |
| API | Change password/secret | Medium | 6 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 46 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Password or OTP-login policy chosen at implementation kickoff / Credential stuffing without rate limits.
