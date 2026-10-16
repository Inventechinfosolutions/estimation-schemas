# F01-001 — Staff Authentication & Session Security

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-001 |
| Feature Name | Staff Authentication & Session Security |
| Module | 01 — Access Control & Staff User Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Secure login to the CLT administration console for all staff roles using user ID and password followed by OTP to the registered mobile / e-mail, with password policy, lockout, CAPTCHA, password reset, idle and absolute session timeout and single active session. Candidates and proctors use their own login paths (F04-001, F08-001).

### Business Objective
Ensure only authorised officials can configure tests, handle question banks, monitor sessions or publish results, and protect the console against brute force and session hijacking.

### Actors
- KEONICS Administrator
- Center for E-Governance officer
- District Coordinator
- Question Bank roles
- Examination Monitoring Unit
- Helpdesk Executive
- Super Admin

### User Journey
1. **Who creates:** Accounts are created by the Super Admin in F01-002; this feature covers how an existing official signs in and maintains credentials.
2. **How they create:** The official enters user ID and password, completes CAPTCHA after failures, receives an OTP and lands on the role dashboard; first login forces a password change.
3. **How they edit:** The official changes password from My Profile with current password and OTP; forgotten passwords are reset by OTP plus single-use link.
4. **How they send for approval:** No approval step; access is granted when password, OTP, status and lockout checks pass.
5. **How the approver sees pending items:** No approver inbox; the Super Admin sees locked and dormant accounts in the user register.
6. **How the approver decides:** The Super Admin unlocks or forces reset with a mandatory reason.
7. **How the applicant / maker sees history:** The official sees last login, failed attempts and active sessions and can end other sessions.
8. **How the approver / auditor sees history:** Auditors see every authentication event with IP and device in the audit trail (F16-002).

### Functional Capabilities
- User ID + password + 6-digit OTP (5-minute validity, 3 resends)
- Password policy: 12+ characters, complexity, last-5 history, 90-day expiry
- Lockout after 5 failures in 15 minutes; auto-unlock after 30 minutes
- CAPTCHA after 2 failures; rate limiting per user and IP
- Forgot password with OTP and single-use link
- Idle timeout 15 minutes; absolute 8 hours; expiry warning
- Single active session; revocation on logout, password change, role change
- Dormant account disable after 90 days
- Exam-day restricted login windows for monitoring roles (configurable)

### UI Screens
- Staff login with CAPTCHA
- OTP verification
- First-login password change
- Forgot / reset password
- Session expiry warning
- My Profile: password and active sessions
- Account locked notice

### Logical API Operations
- Validate credentials and issue OTP
- Verify OTP and create session
- Resend OTP with throttling
- Logout and revoke session
- Password reset request and completion
- Change password with history check
- Session refresh and validation
- Lockout evaluation and auto-unlock
- Dormant account sweep job

### Inputs
- User ID, password, OTP
- Policy settings

### Outputs
- Session bound to roles and data scope
- Audit events

### Business Rules
- Deactivated or dormant accounts cannot log in
- OTP single-use; 3 wrong entries invalidate it
- Password change ends all other sessions
- Generic error messages only

### Validations
- Password policy
- OTP format and expiry

### Calculations
- Lockout expiry
- Session expiry = min(idle, absolute)

### Workflow
Active → Locked → Active; Active → Dormant → Reactivated

### Search Requirements
- None

### Documents
- None

### Reports
- Login activity (via F16-002)

### Notifications
- OTP SMS / e-mail
- Lockout and password change alerts

### Security
- Argon2 / bcrypt hashing
- Secure cookies, CSRF tokens
- TLS only

### Integrations
- OTP via F14-002

### Dependencies
- F01-002
- F14-002
- F16-002
- F16-003

### Assumptions
- No single sign-on required

### Risks
- SMS delays; e-mail OTP alternative

### Non Functional Requirements
- Login under 1 second on LAN excluding OTP delivery

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Staff login with CAPTCHA | Medium | 6 |
| UI | OTP verification | Medium | 6 |
| UI | First-login password change | Easy | 4 |
| UI | Forgot / reset password | Medium | 6 |
| UI | Session expiry warning | Simple | 2 |
| UI | My Profile: password and active sessions | Medium | 6 |
| UI | Account locked notice | Simple | 2 |
| API | Validate credentials and issue OTP | Complex | 8 |
| API | Verify OTP and create session | Complex | 8 |
| API | Resend OTP with throttling | Easy | 4 |
| API | Logout and revoke session | Easy | 4 |
| API | Password reset request and completion | Medium | 6 |
| API | Change password with history check | Medium | 6 |
| API | Session refresh and validation | Medium | 6 |
| API | Lockout evaluation and auto-unlock | Medium | 6 |
| API | Dormant account sweep job | Easy | 4 |
| Database | Credential, password history and session store | Medium | 4 |
| Database | OTP challenge and login attempt log | Easy | 2 |
| Testing | Login, OTP, lockout and timeout tests | Medium | 6 |
| Testing | Authentication security tests (brute force, replay, fixation) | Complex | 8 |
| Documentation | Staff login guide | Easy | 2 |
| Documentation | Authentication configuration note | Simple | 1 |

**Feature Total: 107 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 52 | 6 | 0 | 14 | 3 | **107** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- OTP delivery reuses the SMS / e-mail connector
- No external integration channel in this feature; Integration row omitted.
