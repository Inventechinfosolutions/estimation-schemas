# F01-001 — Staff Authentication & Session Security

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-001 |
| Feature Name | Staff Authentication & Session Security |
| Module | 01 — User, Role & Access Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Secure login to the BDA staff portal for all official roles using user ID and password followed by a one-time password (OTP) to the registered mobile or e-mail, with password policy, lockout, password reset, idle and absolute session timeout and concurrent session control. Bidders do not use this login (see F05-002).

### Business Objective
Ensure only authorised BDA officials can view or act on auction cases, and protect the portal against brute force, credential sharing and session hijacking as required by the RFP security clauses.

### Actors
- All BDA staff roles (Result Verifier, Approving Authority, Payment Reconciler, Deputy Secretary, Case Worker, Finance Officer, Auction Admin, Super Admin, Read-only Viewer)
- Super Admin (unlock and reset)

### User Journey
1. **Who creates:** Staff accounts are created by the Super Admin in F01-002; this feature covers how an existing official signs in and maintains credentials.
2. **How they create:** The official opens the staff portal, enters user ID and password, receives an OTP on the registered mobile / e-mail, enters it and lands on the role dashboard; first login forces a password change.
3. **How they edit:** The official changes their password from My Profile (current password, new password meeting policy, OTP confirmation); a forgotten password is reset through OTP to the registered mobile plus e-mail link.
4. **How they send for approval:** Authentication has no approval step; access is granted automatically when password, OTP, account status and lockout checks pass.
5. **How the approver sees pending items:** There is no approver inbox; the Super Admin sees locked and dormant accounts in the user register (F01-002) with lock reason and time.
6. **How the approver decides:** No approval decision applies; the Super Admin may unlock an account or force a password reset, each with a mandatory reason.
7. **How the applicant / maker sees history:** The official sees last successful login, last failed attempt and active sessions on My Profile and can sign out other sessions.
8. **How the approver / auditor sees history:** The Super Admin and auditors see login success / failure, OTP failures, lockouts, resets and sign-outs with IP and device in the audit trail (F14-001).

### Functional Capabilities
- User ID and password login with generic error messages that never reveal whether the user exists
- Second factor by 6-digit OTP to registered mobile (SMS) and / or e-mail, valid 5 minutes, maximum 3 resends
- Configurable password policy: minimum 12 characters, upper / lower / digit / special, last 5 passwords blocked, 90-day expiry
- Forced password change at first login and after administrator reset
- Account lockout after 5 failed attempts in 15 minutes; automatic unlock after 30 minutes or manual unlock by Super Admin
- Forgot-password flow with OTP verification and single-use reset link valid 30 minutes
- Idle timeout 15 minutes and absolute session lifetime 8 hours with on-screen warning 2 minutes before expiry
- Single active session per user (configurable); new login ends or blocks the older session
- Server-side session revocation on logout, password change, deactivation and role change
- CAPTCHA after 2 failed attempts and rate limiting per user and per IP
- Dormant account auto-disable after 90 days without login (configurable)
- Login banner with acceptable-use notice as per GoK IT policy

### UI Screens
- Staff login page with CAPTCHA
- OTP verification page with resend timer
- First-login forced password change
- Forgot password with OTP and reset link
- Reset password page with strength meter
- Session expiry warning and expired notice
- My Profile: change password and active sessions
- Account locked / dormant notice

### Logical API Operations
- Validate credentials and issue OTP challenge
- Verify OTP and create session
- Resend OTP with throttling
- Logout and revoke session
- Request password reset (OTP plus link)
- Validate reset token and set password
- Change own password with history check
- Refresh and validate session / token
- Evaluate lockout and auto-unlock
- List and revoke own active sessions
- Dormant account sweep job

### Inputs
- User ID and password
- OTP
- Current and new password
- Reset token
- Policy settings: length, complexity, history, expiry, lockout threshold and window, idle and absolute timeouts, dormancy days

### Outputs
- Authenticated session bound to user, roles and DS office
- OTP SMS / e-mail
- Lockout state and unlock time
- Audit entries for each authentication event

### Business Rules
- Inactive, deactivated or dormant accounts cannot log in
- OTP is single-use and expires in 5 minutes; 3 wrong OTP entries invalidate the challenge
- Password change revokes all other sessions
- New password cannot match the last 5 or contain the user ID
- Role or DS office change takes effect on the next request
- Error messages are identical for wrong user and wrong password

### Validations
- User ID format
- Password meets policy
- OTP numeric, 6 digits, unexpired, unused
- Reset token valid and unexpired
- Current password correct on change

### Calculations
- Lockout expiry = last failed attempt + lockout period
- Session expiry = min(last activity + idle timeout, login time + absolute lifetime)
- Password expiry date = last change + 90 days

### Workflow
Active → (5 failures) Locked → (30 min or Super Admin unlock) Active; Active → (90 days idle) Dormant → (Super Admin reactivation) Active; Reset requested → OTP verified → Token issued → Password set → Active

### Search Requirements
- None (login history searched in F14-002)

### Documents
- None

### Reports
- Login activity and failed-login report (through F14-002)
- Dormant and locked accounts list (through F01-002)

### Notifications
- Login OTP by SMS / e-mail
- Password reset OTP and link
- Alert to user on lockout and on password change

### Security
- Passwords hashed with Argon2 / bcrypt
- Secure, HTTP-only, SameSite cookies; anti-CSRF tokens
- Rate limiting and CAPTCHA (F14-003)
- TLS 1.2 or above only
- No credentials or OTP in logs or URLs

### Integrations
- SMS and e-mail delivery through the Notification Service (F12-003)

### Dependencies
- F01-002 (accounts)
- F12-003 (OTP delivery)
- F14-001 (audit)
- F14-003 (rate limiting, CAPTCHA)

### Assumptions
- Single sign-on with other BDA systems is not required
- Every official has a registered mobile number and official e-mail

### Risks
- SMS delays block login; e-mail OTP is offered as an alternative
- Shared credentials among staff weaken accountability

### Non Functional Requirements
- Login response within 2 seconds excluding OTP delivery
- Session controls enforced server-side
- Supports 500 concurrent users

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Staff login page with CAPTCHA | Medium | 6 |
| UI | OTP verification page with resend timer | Medium | 6 |
| UI | First-login forced password change | Easy | 4 |
| UI | Forgot password with OTP and reset link | Medium | 6 |
| UI | Reset password page with strength meter | Easy | 4 |
| UI | Session expiry warning and expired notice | Simple | 2 |
| UI | My Profile: change password and active sessions | Medium | 6 |
| UI | Account locked / dormant notice | Simple | 2 |
| API | Validate credentials and issue OTP challenge | Complex | 8 |
| API | Verify OTP and create session | Complex | 8 |
| API | Resend OTP with throttling | Easy | 4 |
| API | Logout and revoke session | Easy | 4 |
| API | Request password reset (OTP plus link) | Medium | 6 |
| API | Validate reset token and set password | Medium | 6 |
| API | Change own password with history check | Medium | 6 |
| API | Refresh and validate session / token | Medium | 6 |
| API | Evaluate lockout and auto-unlock | Medium | 6 |
| API | List and revoke own active sessions | Easy | 4 |
| API | Dormant account sweep job | Easy | 4 |
| Database | Credential and password history store | Easy | 2 |
| Database | Session and refresh token store | Medium | 4 |
| Database | OTP challenge store with expiry | Easy | 2 |
| Database | Login attempt and lockout log | Easy | 2 |
| Database | Password reset token store | Simple | 1 |
| Testing | Login, OTP, lockout and timeout scenarios | Medium | 6 |
| Testing | Password policy, history, expiry and reset flows | Medium | 6 |
| Testing | Authentication security tests (brute force, session fixation, enumeration, OTP replay) | Complex | 8 |
| Testing | Concurrent session and revocation tests | Easy | 4 |
| Documentation | Staff login and password guide | Easy | 2 |
| Documentation | Authentication configuration notes for administrators | Simple | 1 |

**Feature Total: 136 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 36 | 62 | 11 | 0 | 24 | 3 | **136** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- OTP delivery reuses the Notification Service connector; no Integration row in this feature
- CAPTCHA and rate limiting are configured from F14-003
- No external integration channel in this feature; Integration row omitted.
