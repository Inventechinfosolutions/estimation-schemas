# F01-001 — Secure Login & Session Management

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-001 |
| **Feature Name** | Secure Login & Session Management |
| **Module** | 01 — User & Role Management |

### Description
Enable BDA officers, administrators, auditors, and tenant portal users to authenticate securely into CPMS and maintain a controlled application session with timeout and secure logout.

### Business Objective
Protect access to commercial property, lease, and financial data through authenticated sessions aligned with government security expectations (TLS, password policy enforcement at login, session control).

### Actors
- Super Administrator
- All officer roles (Commissioner, Estate Officer, Accounts Officer, etc.)
- Auditor
- Tenant (Portal)
- System (session enforcement)

### User Journey
1. User opens CPMS web application.
2. User enters username/login ID and password on the login screen.
3. System validates credentials and account status (active/inactive).
4. On success, system creates a secured session and redirects to the role-appropriate home/landing view.
5. On idle beyond configured timeout, system expires the session and requires re-login.
6. User can explicitly log out; session is invalidated immediately.

### Functional Capabilities
- Username/password login for officer and tenant users
- Account status check (blocked/inactive users cannot login)
- Secure session creation and server-side invalidation on logout
- Configurable idle session timeout
- Display of generic authentication failure messages (no user enumeration)
- Concurrent session policy (configurable: allow single or multiple sessions)
- Landing redirect based on primary role

### Inputs
- Login ID / username
- Password
- Optional: remember-device flag (if enabled by policy; default off for officers)

### Outputs
- Authenticated session
- Success redirect to application home
- Failure message
- Logout confirmation

### Business Rules
- Only **Active** users may authenticate.
- Failed login attempts are counted; after configurable threshold, temporary lockout applies.
- Session timeout is driven by system security parameter.
- Tenant users can only access tenant portal routes after login.
- Officer users cannot use tenant-only credentials interchangeably if accounts are typed.

### Validations
- Login ID and password are mandatory.
- Password field is masked.
- Lockout state prevents further attempts until unlock time or admin unlock.
- Inactive/deactivated accounts rejected.

### Calculations
- Lockout window remaining time (if displayed).

### Workflow
N/A (direct authentication transaction). Lockout unlock may be admin-assisted under F01-004.

### Search Requirements
N/A for login. Session/admin unlock lists covered under user management / logs.

### Documents
None.

### Reports
None (login success/failure captured in F01-009).

### Notifications
Optional lockout notification to user/admin via Notification Service (if configured).

### Security
- TLS in transit
- Password verified using secure one-way hashing (implementation concern; no plaintext storage)
- Anti-enumeration error messages
- CSRF protection on login form
- Session fixation protection on login
- PII not exposed on login errors

### Integrations
- None mandatory inside this feature (2FA OTP is F01-003; email/SMS reset is F01-002).

### Dependencies
- User master records (F01-004)
- Role assignment available for post-login authorization (F01-005)
- System parameters for timeout/lockout (Module 02 may own parameter UI; defaults acceptable at go-live)

### Assumptions
- Browser-based access only (Chrome/Edge/Firefox).
- No external SSO/IdP in scope.
- Tenant and officer share the same login framework with account-type routing.
- Enterprise-grade auth with logging and unit tests included in estimate.

### Risks
- Lockout policy too strict may block field officers; needs BDA-agreed thresholds.
- Shared workstations increase session hijack risk if timeout is too long.

### Non Functional Requirements
- Login page responsive on desktop and tablet
- Authentication response typically under 3 seconds under agreed load
- Compatible with Chrome, Edge, Firefox (latest 2 major versions)

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: secure credential verification, lockout rules, session lifecycle, enterprise security hardening.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Login page | UI | Easy | 4 |
| Session expiry / re-auth message | UI | Simple | 2 |
| Authenticate user | API | Complex | 8 |
| Logout / session invalidate | API | Easy | 4 |
| User credential & session store | Database | Medium | 4 |
| Auth security test suite | Testing | Complex | 8 |
| Login & session user guide | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- UI screens estimated independently (login + session expiry messaging).
- Authenticate treated as Complex API due to lockout, status, and security rules.
- No external IdP integration hours in this feature.
