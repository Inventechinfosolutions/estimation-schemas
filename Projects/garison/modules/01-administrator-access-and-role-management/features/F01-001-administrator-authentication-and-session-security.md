# F01-001 — Administrator Authentication & Session Security

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-001 |
| Feature Name | Administrator Authentication & Session Security |
| Module | 01 — Administrator Access & Role Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Secure sign-in to the catalogue administration portal for Garrison staff with a strong password policy, account lockout, self-service password reset, change password and idle/absolute session timeout. Public catalogue visitors never authenticate.

### Business Objective
Ensure only authorised Garrison staff can change catalogue content, and protect the portal against credential stuffing, brute force and session hijacking.

### Actors
- Super Administrator
- Catalogue Administrator
- Catalogue Reviewer
- Content Administrator

### User Journey
1. **Who creates:** Administrator accounts are created by the Super Administrator in F01-002; this feature covers how an existing administrator signs in and maintains their credentials.
2. **How they create:** The administrator opens the portal URL, enters email and password, and is signed in to the role-specific dashboard; after the configured number of failed attempts the account is locked for the lockout period.
3. **How they edit:** The administrator changes their own password from My Profile (current password plus new password meeting policy); a forgotten password is reset through a time-limited emailed link.
4. **How they send for approval:** Authentication has no approval step; sign-in is granted automatically when credentials, account status and lockout rules pass.
5. **How the approver sees pending items:** There is no approver inbox; the Super Administrator sees locked accounts in the user register (F01-002) and can unlock them.
6. **How the approver decides:** No approval decision applies; the Super Administrator's only intervention is manual unlock or forced password reset.
7. **How the maker sees history:** The administrator sees their last successful sign-in time and active session on My Profile.
8. **How the approver / auditor sees history:** The Super Administrator and auditors see sign-in success/failure, lockouts, resets and sign-outs in the audit log (F01-004).

### Functional Capabilities
- Email + password sign-in with generic error messages (no user enumeration)
- Configurable password policy: minimum length 12, character classes, password history (last 5), expiry optional
- Account lockout after N failed attempts within a window, with automatic unlock after a cool-down period
- Forgot-password flow with single-use, time-limited (30 min) reset token sent by email
- Change own password with current-password confirmation
- Idle timeout (default 30 min) and absolute session lifetime (default 12 h) with warning before expiry
- Sign out and server-side session revocation; revoke all sessions on password change
- Last sign-in information and active session indicator on My Profile

### UI Screens
- Administrator sign-in page
- Forgot password request page
- Reset password page with policy strength meter
- Account locked / session expired notice
- Change password screen
- My profile and active session panel

### Logical API Operations
- Authenticate administrator
- Sign out and revoke session
- Request password reset link
- Validate reset token and set new password
- Change own password
- Refresh and validate session
- Evaluate lockout counter and auto-unlock

### Inputs
- Email address and password
- Current and new password (change)
- Reset token from emailed link
- Policy settings: minimum length, history depth, lockout threshold, lockout window, idle and absolute timeouts

### Outputs
- Authenticated session bound to the administrator and role
- Lockout state and unlock time
- Password reset email
- Audit entries for every authentication event

### Business Rules
- Inactive or deactivated accounts cannot sign in even with correct credentials
- Reset tokens are single-use and expire after 30 minutes
- Password change revokes all other active sessions
- New password cannot equal any of the last five passwords
- Error messages never reveal whether an email exists

### Validations
- Email format
- Password meets policy (length, classes, not in history, not equal to email)
- Reset token exists, unused and unexpired
- Current password correct on change

### Calculations
- Lockout expiry = time of last failed attempt + lockout period
- Session expiry = min(last activity + idle timeout, sign-in time + absolute lifetime)

### Workflow
Active → (N failures) Locked → (cool-down or Super Administrator unlock) Active; Reset requested → Token issued → Password set → Active

### Search Requirements
- None on this feature (sign-in history searched in F01-004)

### Documents
- None

### Reports
- None (authentication events are reported through F01-004)

### Notifications
- Password reset link email
- Optional email to the user when their account is locked

### Security
- Passwords stored with a modern adaptive hash (bcrypt/Argon2)
- Secure, HTTP-only, SameSite cookies or equivalent token handling
- Rate limiting on sign-in and reset endpoints (F13-002)
- HTTPS only

### Integrations
- Transactional email service (shared connector delivered in F06-005)

### Dependencies
- F01-002 (accounts)
- F01-004 (audit)
- F06-005 (email connector)
- F13-002 (rate limiting)

### Assumptions
- Single sign-on with Garrison's directory is not required in this phase
- Multi-factor authentication is not required in this phase; the design leaves room to add it

### Risks
- Shared administrator credentials among Garrison staff weaken audit accountability
- Email deliverability issues may block password resets

### Non Functional Requirements
- Sign-in response under 1 second at normal load
- Lockout and session rules enforced server-side
- No sensitive data in URLs or logs

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Administrator sign-in page | Medium | 6 |
| UI | Forgot password request page | Easy | 4 |
| UI | Reset password page with policy strength meter | Medium | 6 |
| UI | Account locked / session expired notice | Simple | 2 |
| UI | Change password screen | Easy | 4 |
| UI | My profile and active session panel | Easy | 4 |
| API | Authenticate administrator | Complex | 8 |
| API | Sign out and revoke session | Easy | 4 |
| API | Request password reset link | Medium | 6 |
| API | Validate reset token and set new password | Complex | 8 |
| API | Change own password | Medium | 6 |
| API | Refresh and validate session | Medium | 6 |
| API | Evaluate lockout counter and auto-unlock | Medium | 6 |
| Database | Administrator credential and password history store | Easy | 2 |
| Database | Session and refresh token store | Easy | 2 |
| Database | Sign-in attempt and lockout log | Easy | 2 |
| Database | Password reset token store | Simple | 1 |
| Integration | Password reset email through shared email connector | Simple | 4 |
| Testing | Sign-in, lockout and session timeout scenarios | Medium | 6 |
| Testing | Password policy, history and reset token expiry | Medium | 6 |
| Testing | Authentication security tests (brute force, session fixation, enumeration) | Complex | 8 |
| Documentation | Administrator sign-in and password policy guide | Easy | 2 |
| Documentation | Authentication security configuration notes | Simple | 1 |

**Feature Total: 104 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 44 | 7 | 4 | 20 | 3 | **104** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Standard credential authentication with lockout and reset; no SSO or MFA
- Email delivery reuses the shared connector, so only a Simple internal integration row is included
