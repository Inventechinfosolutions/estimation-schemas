# F01-004 — Staff Login and Session

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-004 |
| **Feature Name** | Staff Login and Session |
| **Module** | 01 — Staff Access and Role Management |

### Description
A staff user with an active account signs in to the staff application, works in a session, and signs out. Password reset is requested by the user and completed with a time-limited link sent through the email channel. This sign-in is not the bidder portal sign-in.

### Business Objective
Only an active staff account can open the staff application, and the session can be ended.

### Actors
Maker: the staff user, for sign-in, sign-out, and password reset. Approver: none.

### User Journey
1. Who creates: the staff user does not create the account here. They create a session by signing in. The administrator has already created the account in F01-001.
2. How they create: Staff sign-in → email and password → session opens on the menu allowed by F01-002.
3. How they edit: they change their password from the session screen, or request a reset from the sign-in screen if they cannot sign in.
4. How they send for approval: they do not. Sign-in is accepted or rejected by the account status and password. There is no approver.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: the user can see their recent sign-in outcomes on the session screen (time and success or failure). They do not see other people’s sessions.
8. How the auditor sees history: the System / Catalogue Administrator can read sign-in history for staff accounts. Failed attempts are part of that history.

### Functional Capabilities
- Sign in an active staff account
- Reject inactive accounts and wrong passwords
- Sign out and expire a session
- Reset a forgotten password by email link
- Show a menu limited to the user’s roles and department

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Email
- Password
- Reset request

### Outputs
- An authenticated staff session, or a rejection
- Password reset email event handed to Module 14

### Business Rules
- Inactive accounts cannot sign in.
- Staff credentials do not open the bidder portal, and bidder credentials do not open the staff application.
- A reset link expires and can be used once.
- Signing out ends that session. It does not deactivate the account.

### Validations
- Email and password are required.
- Reset is offered only for an email that belongs to an active staff account, without revealing whether an unknown email exists in the message shown to the user.

### Calculations
None.

### Workflow
No approval. The email channel delivers the reset link; failure of email does not unlock the account.

### Search Requirements
Administrator searches sign-in history by account and date.

### Documents
None.

### Reports
None.

### Notifications
Password reset uses the email delivery in F14-002. Ordinary sign-in does not send a notification.

### Security
Passwords are not stored in a form that can be read back. Session ends on sign-out or expiry. The public reset message does not disclose whether the email is registered.

### Integrations
Email delivery is provided by F14-002. This feature does not add a second mail channel.

### Dependencies
F01-001 and F01-002. F14-002 for the reset email.

### Assumptions
- The first password is set through the same reset-link mechanism so the administrator never sees the password.
- Session length is an operational setting. The source does not fix a number of minutes.

### Risks
If email is down, a locked-out user cannot self-reset. An administrator can still reactivate process access by issuing a fresh reset once email works.

### Non Functional Requirements
A deactivated account is rejected even if a session was issued before deactivation, on the next action.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Staff sign-in screen | UI | Simple | 2 |
| Password and session screen | UI | Easy | 4 |
| Sign-in history | UI | Easy | 4 |
| Authenticate staff user | API | Medium | 6 |
| End staff session | API | Simple | 2 |
| Issue password reset | API | Medium | 6 |
| Staff credential and session records | DB | Easy | 2 |
| Staff login tests | Testing | Medium | 6 |
| Staff login notes | Documentation | Easy | 2 |

**Feature total: 34 hours**
