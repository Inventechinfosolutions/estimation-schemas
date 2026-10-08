# F01-002 — Administrator User Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-002 |
| Feature Name | Administrator User Management |
| Module | 01 — Administrator Access & Role Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Super Administrator maintains the list of portal users: invite new staff by email, assign one or more roles, edit details, deactivate or reactivate accounts, unlock locked accounts and view each user's sign-in history.

### Business Objective
Give Garrison full control over who can maintain the catalogue, and remove access promptly when staff change roles or leave.

### Actors
- Super Administrator
- Invited administrator

### User Journey
1. **Who creates:** The Super Administrator creates portal users; no other role can add users.
2. **How they create:** From the User register they choose Invite user, enter name, email and role(s), and send; the system emails a time-limited invitation link, and the invitee sets a password to activate the account.
3. **How they edit:** The Super Administrator edits name, roles and status from the user detail; changes to roles apply on the user's next request.
4. **How they send for approval:** User creation does not need approval; the invitation acceptance by the invitee completes activation.
5. **How the approver sees pending items:** There is no approver inbox; pending invitations are visible in the register with status 'Invited' and can be resent or cancelled.
6. **How the approver decides:** No approval decision applies; the Super Administrator decides directly when deactivating, reactivating or unlocking.
7. **How the maker sees history:** An administrator sees their own roles and last sign-in on My Profile; they cannot edit their own roles.
8. **How the approver / auditor sees history:** The Super Administrator and auditors see invitation, activation, role change, deactivation and unlock events with before/after values in the audit log (F01-004).

### Functional Capabilities
- User register with filters (role, status: Invited/Active/Locked/Deactivated) and search by name/email
- Invite user with role assignment and invitation email (72-hour link)
- Resend or cancel pending invitation
- Edit user details and roles; multiple roles per user
- Deactivate / reactivate with reason; deactivation revokes active sessions immediately
- Unlock locked account and force password reset
- User detail with sign-in history tab
- Protection: the last active Super Administrator cannot be deactivated or demoted; users cannot deactivate themselves

### UI Screens
- Administrator user register
- Invite administrator form
- Edit administrator and role assignment
- Deactivate / reactivate confirmation with reason
- Invitation acceptance and first password page
- Administrator detail with sign-in history tab

### Logical API Operations
- List administrators with filters
- Create administrator and send invitation
- Update administrator profile and roles
- Deactivate or reactivate administrator
- Accept invitation and activate account
- Resend or cancel invitation
- Unlock account and force password reset
- Get administrator detail with sign-in history

### Inputs
- Full name, email, role(s)
- Deactivation reason
- Invitation token and new password (invitee)

### Outputs
- Administrator account in Invited/Active/Deactivated state
- Invitation and activation emails
- Audit entries for every change

### Business Rules
- Email is unique across administrators
- At least one active Super Administrator must always exist
- Deactivation immediately revokes sessions
- Invitation links expire after 72 hours and are single-use

### Validations
- Mandatory name, email and at least one role
- Email format and uniqueness
- Password policy on activation (F01-001)

### Calculations
- Invitation expiry = sent time + 72 hours

### Workflow
Invited → Active → Deactivated → Active; Invited → Expired/Cancelled

### Search Requirements
- Name, email, role, status, last sign-in date range

### Documents
- None

### Reports
- User list export (CSV) with role and status

### Notifications
- Invitation email
- Optional account-deactivated email to the user

### Security
- Only Super Administrator can access user management
- Role changes logged with before/after values

### Integrations
- Transactional email service (shared connector)

### Dependencies
- F01-001
- F01-003
- F01-004
- F06-005

### Assumptions
- Expected administrator population is small (under 25 users)
- No self-registration for administrators

### Risks
- Former staff retain access if Garrison does not notify changes promptly

### Non Functional Requirements
- Register loads in under 2 seconds
- All actions audited

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Administrator user register | Medium | 6 |
| UI | Invite administrator form | Medium | 6 |
| UI | Edit administrator and role assignment | Medium | 6 |
| UI | Deactivate / reactivate confirmation with reason | Simple | 2 |
| UI | Invitation acceptance and first password page | Medium | 6 |
| UI | Administrator detail with sign-in history tab | Easy | 4 |
| API | List administrators with filters | Medium | 6 |
| API | Create administrator and send invitation | Complex | 8 |
| API | Update administrator profile and roles | Medium | 6 |
| API | Deactivate or reactivate administrator | Medium | 6 |
| API | Accept invitation and activate account | Complex | 8 |
| API | Resend or cancel invitation | Easy | 4 |
| API | Unlock account and force password reset | Easy | 4 |
| API | Get administrator detail with sign-in history | Easy | 4 |
| Database | Administrator profile and status | Easy | 2 |
| Database | User-role assignment | Easy | 2 |
| Database | Invitation token store | Simple | 1 |
| Integration | Invitation email through shared email connector | Simple | 4 |
| Testing | User lifecycle: invite, activate, deactivate, reactivate | Medium | 6 |
| Testing | Last Super Administrator and self-deactivation protection | Easy | 4 |
| Testing | Role change takes effect and is enforced server-side | Medium | 6 |
| Documentation | User administration guide | Easy | 2 |

**Feature Total: 103 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 46 | 5 | 4 | 16 | 2 | **103** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Invitation-based onboarding adds the acceptance page and token handling
- User list export is a light CSV export inside the list operation
