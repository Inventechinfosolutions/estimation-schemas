# F03-003 — Bidder Login and Session

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Bidder Login and Session |
| **Module** | 03 — Bidder Registration and Profile |

### Description
An activated bidder signs in to the bidder portal, uses the participation and bidding functions, and signs out. Password reset uses a time-limited email link. Inactive, pending, and rejected bidders are refused.

### Business Objective
Only a verified bidder can open the portal that leads to participation and live bidding.

### Actors
Maker: the activated bidder. Approver: none.

### User Journey
1. Who creates: the bidder creates a session by signing in. They do not create the account here.
2. How they create: Bidder sign-in → email and password → portal home.
3. How they edit: they change the password from the session screen or request a reset from the sign-in screen.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: the bidder sees their own recent sign-in results.
8. How the auditor sees history: the System / Catalogue Administrator can read bidder sign-in history. Auction staff do not get that history unless they hold the administrator role.

### Functional Capabilities
- Sign in an active bidder
- Refuse pending, rejected, and deactivated bidders
- Sign out and expire the session
- Reset a forgotten password by email

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Email
- Password

### Outputs
- Bidder session
- Reset email event

### Business Rules
- Staff passwords do not authenticate here.
- A bidder with no active status cannot sign in.
- Reset links expire and work once.
- Sign-out does not withdraw a participation already submitted.

### Validations
- Email and password are required.
- The reset response does not reveal whether an unknown email exists.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
Administrator searches sign-in history by bidder and date.

### Documents
None.

### Reports
None.

### Notifications
Password reset email through F14-002.

### Security
Passwords cannot be read back. Session ends on sign-out or expiry. Deactivation blocks the next action.

### Integrations
Email delivery stays in F14-002.

### Dependencies
F03-002 activation. F14-002 for reset email.

### Assumptions
- The first password is set by the same reset link after activation, so staff never see the bidder’s password.

### Risks
Email outage blocks self-service reset. Participation already in progress is not deleted.

### Non Functional Requirements
A bidder deactivated during a live auction cannot place a further bid on the next submit.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Bidder sign-in screen | UI | Simple | 2 |
| Bidder password reset screen | UI | Easy | 4 |
| Authenticate bidder | API | Medium | 6 |
| Issue bidder password reset | API | Easy | 4 |
| Bidder credential records | DB | Easy | 2 |
| Bidder login tests | Testing | Medium | 6 |
| Bidder login notes | Documentation | Easy | 2 |

**Feature total: 26 hours**
