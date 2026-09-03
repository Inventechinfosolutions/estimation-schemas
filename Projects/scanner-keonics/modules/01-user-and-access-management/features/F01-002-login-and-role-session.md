# F01-002 — Login and Role Session

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Login and Role Session |
| **Module** | 01 — User and Access Management |

### Description
Staff sign in and receive only Operator, Supervisor or Department Officer functions. Disabled accounts cannot sign in.

### Business Objective
Stop unauthorised use of the custody and production tool on the DMG premises.

### Actors
Maker: any enabled account holder. Approver: none.

### User Journey
1. Who creates: The account holder starts a session.
2. How they create: Login → username and password → land on role home.
3. How they edit: Session is not edited; sign out or timeout.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox.
6. How the approver decides: No decision.
7. How the maker sees history: Current signed-in identity on screen.
8. How the auditor sees history: Last sign-in visible to Supervisor/Department Officer.

### Functional Capabilities
- Authenticate
- Role-scoped session
- Sign out
- Access denied for wrong role

### UI Screens
| Screen | Complexity |
|---|---|
| Login screen | Easy |
| Role landing after login | Medium |
| Access denied message | Simple |

### Logical API operations
| Operation | Complexity |
|---|---|
| Authenticate credentials | Complex |
| Establish session | Medium |
| End session | Easy |
| Resolve role functions | Medium |

### Inputs
Username, password.

### Outputs
Role session.

### Business Rules
- One role per session.
- Disabled accounts refused.

### Validations
- Credentials required and must match.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
None.

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
Site-only; no public login.

### Integrations
None.

### Dependencies
F01-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- No OTP/SSO.

### Risks
Password sharing on a busy scan floor.

### Non Functional Requirements
Works on Department office PCs during 10:00–17:30 operations.

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
