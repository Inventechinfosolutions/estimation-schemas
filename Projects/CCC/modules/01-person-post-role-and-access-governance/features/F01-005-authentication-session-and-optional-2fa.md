# F01-005 — Authentication, Session and Optional 2FA

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-005 |
| **Feature Name** | Authentication, Session and Optional 2FA |
| **Module** | 01 — Person, Post, Role and Access Governance |

### Description
Person signs in, optionally completes OTP/2FA, then selects a current Post. Session is bound to Person + Post.

### Business Objective
Only an activated Person with a current Post mapping may use CCC.

### Actors
User: the Person. Access Administrator may unlock/reset.

### User Journey
1. Who creates: The Person opens login.
2. How they create: Enters user ID and password, completes OTP if configured, selects current Post if more than one mapping is Active.
3. How they edit: Password change after re-authentication. Administrator force-reset.
4. How they send for approval: Not an approval workflow. Success creates a session bound to Person + Post.
5. How the approver sees pending items: No approver inbox. Failed logins appear on the access log.
6. How the approver decides: Not applicable.
7. How the user sees history: Last successful login on home.
8. How the supervisor/auditor sees history: Access log: success, fail, lock, unlock.

### Functional Capabilities
- Login
- Optional OTP/2FA
- Post selection
- Session end

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Login screen | Medium |
| OTP / 2FA screen | Easy |
| Post selection | Easy |
| Session / password change | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Authenticate Person | Complex |
| Verify OTP/2FA | Medium |
| Create/end session | Medium |
| List current Post mappings | Easy |

### Inputs
User ID, password, OTP, selected Post.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Inactive Person refused.
- No current mapping refused.

### Validations
- Credentials mandatory.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Login success/fail counts.

### Notifications
OTP when configured.

### Security
Session bound to Person + Post.

### Integrations
Optional SMS/email OTP.

### Dependencies
F01-001 to F01-004.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- GPS/CCTV/RFID/ANPR field hardware supply and install are out of application-software hours unless stated otherwise.
- Hosting is on KSDC; KSDC consumption INR and AMC/O&M person-months are out of this estimate per confirmed scope.

### Risks
Incomplete vendor API documentation for VLTS, CCTV, SMART-PDS, Vahan or Sarathi would delay integration features.

### Non Functional Requirements
Screens remain usable under concurrent State CCC load; privileged actions are attributable to Person + Post.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Login screen | UI | Medium | 6 |
| OTP / 2FA screen | UI | Easy | 4 |
| Post selection | UI | Easy | 4 |
| Session / password change | UI | Medium | 6 |
| Authenticate Person | API | Complex | 8 |
| Verify OTP/2FA | API | Medium | 6 |
| Create/end session | API | Medium | 6 |
| List current Post mappings | API | Easy | 4 |
| Session and login attempt log | DB | Medium | 4 |
| OTP SMS/email delivery (optional) | Integration | Medium | 16 |
| Authentication, Session and Optional 2FA feature tests | Testing | Very High | 12 |
| Authentication, Session and Optional 2FA implementation documentation | Documentation | Medium | 3 |

**Feature total: 79 hours**
