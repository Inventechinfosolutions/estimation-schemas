# F01-005 — Authentication, Session and MFA Controls

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-005 |
| **Feature Name** | Authentication, Session and MFA Controls |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
The Person signs in with official credentials, completes MFA, and works under a selected current Post.

### Business Objective
Only an activated Person mapped to an Active Post may use the staff application.

### Actors
User: The Person (staff). Access Administrator may unlock or reset per policy. Auditor: read-only history.

### User Journey
1. Who creates: The Person (staff). Access Administrator may unlock or reset per policy.
2. How they create: Person opens login, enters official user ID and password. System challenges MFA (OTP to official email/mobile). On success, Person selects current Post if more than one mapping is Active.
3. How they edit: Person changes password from profile after re-authentication. Administrator may force reset. Person cannot edit MFA target away from official contacts on the Person master.
4. How they send for approval: Not an approval workflow. Login success creates a session bound to Person + selected Post.
5. How the approver sees pending items: Not applicable — no approver inbox. Failed logins appear on the security log (F01-008).
6. How the approver decides: Not applicable.
7. How the user sees history: Person sees own last successful login time on the home page. Full login history is not a self-service dump.
8. How the supervisor / auditor sees history: Access Administrator / auditor opens login and MFA history for a Person (success, fail, lock, unlock).

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
| MFA OTP screen | Easy |
| Post selection after login | Easy |
| Change password | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create login session | Medium |
| Update login session | Medium |
| Search login session | Medium |
| Read login session history | Easy |
| Authenticate Person | Complex |
| Verify MFA OTP | Medium |
| Create/end session | Medium |
| Unlock / force password reset | Easy |

### Inputs
User ID, password, MFA OTP, selected Post.

### Outputs
Persisted login session; searchable register; history.

### Business Rules
- Login is refused if Person is Inactive or has no current Post mapping.
- Session carries Person and Post; APIs authorise against Roles on that Post.

### Validations
- Password policy. OTP expiry. Lock after configured failed attempts.

### Calculations
None.

### Workflow
Not an approval workflow. Login success creates a session bound to Person + selected Post.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Login success/fail counts for administrators.

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
| MFA OTP screen | UI | Easy | 4 |
| Post selection after login | UI | Easy | 4 |
| Change password | UI | Easy | 4 |
| Create login session | API | Medium | 6 |
| Update login session | API | Medium | 6 |
| Search login session | API | Medium | 6 |
| Read login session history | API | Easy | 4 |
| Authenticate Person | API | Complex | 8 |
| Verify MFA OTP | API | Medium | 6 |
| Create/end session | API | Medium | 6 |
| Unlock / force password reset | API | Easy | 4 |
| Login session record and history | DB | Medium | 4 |
| Internal identity/document hooks for login session | Integration | Medium | 16 |
| Authentication, Session and MFA Controls feature tests | Testing | Very High | 12 |
| Authentication, Session and MFA Controls implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **123** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
