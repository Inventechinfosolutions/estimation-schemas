# F01-003 — Login and Role Session

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | Login and Role Session |
| **Module** | 01 — User Account and Access Management |

### Description
A person signs in with Admin-issued username and password. The session exposes only the functions of that account’s role (User or Admin). Disabled accounts cannot sign in.

### Business Objective
Controlled entry to the internal web application with a single role per session and no person/post selection.

### Actors
Maker: User or Admin signing in. Approver: none.

### User Journey
1. Who creates: The account holder starts a session by signing in (Admin previously created the account).
2. How they create: Login screen → enter username and password → sign in. On success they land on the functions for their role (User: raise/track; Admin: administration plus user functions).
3. How they edit: Session is not edited. The user signs out, or the session ends on timeout. Credentials cannot be changed here (F01-002).
4. How they send for approval: Submit/approval does not apply to login.
5. How the approver sees pending items: There is no approver inbox.
6. How the approver decides: There is no approval decision on this feature.
7. How the applicant / maker sees history: The signed-in user sees their own current session (signed in as themselves). Login history for Admin audit is a simple last-login / session record, not a maker–checker trail.
8. How the approver / auditor sees history: Admin may see that an account last signed in; there is no separate auditor role or OTP log.

### Functional Capabilities
- Authenticate username and password
- Refuse disabled or unknown accounts
- Establish a role-scoped session
- Sign out / end session
- Show access denied when a User attempts Admin functions

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Login screen | Easy |
| Role landing after login | Medium |
| Access denied message | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Authenticate credentials | Complex |
| Establish session | Medium |
| End session | Easy |
| Resolve role functions | Medium |

### Inputs
Username, password.

### Outputs
Authenticated session with role User or Admin; access denied when role does not permit the function.

### Business Rules
- One role per account; no post picker.
- Disabled accounts cannot authenticate (status from F01-004).
- User role never receives Admin menus (users, dropdown values, all-records dashboard).

### Validations
- Username and password required.
- Credentials must match a stored account.
- Account must be enabled.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
None on the login screen.

### Documents
None.

### Reports
None.

### Notifications
None. No OTP.

### Security
Username/password only. Session bound to the account and role. User cannot reach Admin functions.

### Integrations
None.

### Dependencies
F01-001, F01-002; F01-004 for disabled-account refusal.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Admin dashboard landing widgets are estimated under Module 05, not as a second dashboard here. Role landing is the role-specific home (User vs Admin shell).
- No 2FA, captcha product, or SSO.

### Risks
Password sharing among staff cannot be prevented by this feature alone.

### Non Functional Requirements
Login usable on common office browsers; failed attempts do not reveal whether username or password was wrong beyond a generic failure message.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Login screen | UI | Easy | 4 |
| Role landing after login | UI | Medium | 6 |
| Access denied message | UI | Simple | 2 |
| Authenticate credentials | API | Complex | 8 |
| Establish session | API | Medium | 6 |
| End session | API | Easy | 4 |
| Resolve role functions | API | Medium | 6 |
| Session records | DB | Easy | 2 |
| Login and role session tests | Testing | Complex | 8 |
| Login and role session implementation documentation | Documentation | Easy | 2 |

**Feature total: 48 hours**
