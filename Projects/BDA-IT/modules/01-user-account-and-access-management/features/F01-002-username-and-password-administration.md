# F01-002 — Username and Password Administration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Username and Password Administration |
| **Module** | 01 — User Account and Access Management |

### Description
Admin is the only party that sets, changes, and resets **username** and **password**. Users have no self-service, forgot-password, or OTP recovery.

### Business Objective
Credentials for every BDA login remain under IT Admin control.

### Actors
Maker: Admin. Applicant: none. Approver: none.

### User Journey
1. Who creates: Admin, when creating or later maintaining an account from F01-001.
2. How they create: On the account, Admin sets a unique username and an initial password, then confirms. The user is told the credentials out of band (not by this application).
3. How they edit: Admin opens credential reset, enters a new password and/or a new unique username, and confirms. Previous password is not shown.
4. How they send for approval: Submit/approval does not apply.
5. How the approver sees pending items: There is no approver inbox.
6. How the approver decides: There is no approval decision on this feature.
7. How the maker sees history: Admin sees credential action history (username changes and password resets, who and when — not the password value).
8. How the approver / auditor sees history: Admin uses the same credential action history.

### Functional Capabilities
- Set username and password at account creation
- Reset password
- Change username with uniqueness check
- Record credential actions without exposing password values
- Hide all credential actions from the User role

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Credential reset form | Easy |
| Credential change confirmation | Simple |
| Credential action history | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Set initial password | Medium |
| Reset password | Medium |
| Change username | Medium |
| Validate username uniqueness | Easy |
| Read credential history | Easy |

### Inputs
Username, new password, confirmation of reset.

### Outputs
Updated credentials (password stored in protected form); credential action history for Admin.

### Business Rules
- User role has no screen or operation to view, change, or recover credentials.
- Username is unique across accounts.
- Password is not recoverable as plain text.
- Admin reset is the only recovery path.

### Validations
- Username unique and mandatory.
- Password and confirm-password match on set/reset.
- User role requests to change credentials are refused.

### Calculations
None.

### Workflow
No approval. Admin confirmation completes the reset.

### Search Requirements
Credential history searchable by account and date (Admin).

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
Admin only. Passwords stored in protected form. History does not show password values.

### Integrations
None. No SSO, AD, or email reset.

### Dependencies
F01-001 (account must exist).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Login using these credentials is F01-003.
- No password-policy product beyond a simple set/reset confirmation.

### Risks
If BDA later requires self-service reset or SSO, this feature’s “Admin only” rule would change and extra hours would apply.

### Non Functional Requirements
Credential actions attributable to the Admin account; passwords never shown in lists or history.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Credential reset form | UI | Easy | 4 |
| Credential change confirmation | UI | Simple | 2 |
| Credential action history | UI | Simple | 2 |
| Set initial password | API | Medium | 6 |
| Reset password | API | Medium | 6 |
| Change username | API | Medium | 6 |
| Validate username uniqueness | API | Easy | 4 |
| Read credential history | API | Easy | 4 |
| Credential records | DB | Easy | 2 |
| Username and password administration tests | Testing | Medium | 6 |
| Username and password administration implementation documentation | Documentation | Easy | 2 |

**Feature total: 44 hours**
