# F01-005 — Authentication, Session, OTP and 2FA

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-005 |
| **Feature Name** | Authentication, Session, OTP and 2FA |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Person signs in with credentials, completes 2FA using official mobile/email OTP, then selects a current Post. RFP requires 2FA using mobile and email.

### Business Objective
Only an activated Person with a current Post mapping may use the application.

### Actors
User: The Person. Access Administrator may unlock/reset. Auditor: read-only history.

### User Journey
1. Who creates: The Person. Access Administrator may unlock/reset.
2. How they create: Opens login, enters user ID and password, completes OTP/2FA, selects current Post if more than one mapping is Active.
3. How they edit: Password change after re-authentication. Administrator force-reset.
4. How they send for approval: Not an approval workflow. Success creates a session bound to Person + Post. MAC and IP are stored as required by the RFP.
5. How the approver sees pending items: No approver inbox. Failed logins appear on the access log.
6. How the approver decides: Not applicable.
7. How the user sees history: Last successful login on home. Full log is administrator/auditor.
8. How the supervisor / auditor sees history: Access log: success, fail, lock, unlock.

### Functional Capabilities
- Authorised user creates, edits and searches login session records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Login session register | Medium |
| Login session form (create and edit) | Complex |
| Login session history | Medium |
| Login screen | Medium |
| OTP / 2FA screen | Easy |
| Post selection | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create login session | Medium |
| Update login session | Medium |
| Search login session | Medium |
| Read login session history | Easy |
| Authenticate Person | Complex |
| Verify OTP/2FA | Medium |
| Create/end session | Medium |

### Inputs
User ID, password, OTP, selected Post.

### Outputs
Persisted login session; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Inactive Person refused.
- No current mapping refused.

### Calculations
None.

### Workflow
Not an approval workflow. Success creates a session bound to Person + Post. MAC and IP are stored as required by the RFP.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Login success/fail counts.

### Notifications
On-screen confirmation. Optional notice to the user on save failure.

### Security
Need-to-know by Post. Actions attributed to Person acting in a Post.

### Integrations
Module 01 identity. Document store if attachments are used.

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

### Assumptions
- Hours use Estimation Master values only, at capability grain (not one billed row per screen).

### Risks
Unscoped access would expose records outside the user's office.

### Non Functional Requirements
Register and history remain searchable during office hours.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Login session register | UI | Medium | 6 |
| Login session form (create and edit) | UI | Complex | 12 |
| Login session history | UI | Medium | 6 |
| Login screen | UI | Medium | 6 |
| OTP / 2FA screen | UI | Easy | 4 |
| Post selection | UI | Easy | 4 |
| Create login session | API | Medium | 6 |
| Update login session | API | Medium | 6 |
| Search login session | API | Medium | 6 |
| Read login session history | API | Easy | 4 |
| Authenticate Person | API | Complex | 8 |
| Verify OTP/2FA | API | Medium | 6 |
| Create/end session | API | Medium | 6 |
| Login session record and history | DB | Medium | 4 |
| Internal identity/document hooks for login session | Integration | Medium | 16 |
| Authentication, Session, OTP and 2FA feature tests | Testing | Very High | 12 |
| Authentication, Session, OTP and 2FA implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **115** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
