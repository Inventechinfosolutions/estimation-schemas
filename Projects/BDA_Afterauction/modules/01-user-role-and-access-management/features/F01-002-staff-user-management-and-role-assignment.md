# F01-002 — Staff User Management & Role Assignment

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-002 |
| Feature Name | Staff User Management & Role Assignment |
| Module | 01 — User, Role & Access Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Super Admin creates and maintains BDA official accounts, assigns one or more roles, maps Deputy Secretaries and Case Workers to a DS office (DS1 / DS2 / DS3), sets delegation during leave, deactivates and reactivates accounts, and reviews each user's access history.

### Business Objective
Give BDA full control over who can act on auction cases and ensure access is removed or changed promptly on transfer, leave or retirement.

### Actors
- Super Admin
- Auction Admin (view only)
- Staff user

### User Journey
1. **Who creates:** The Super Admin creates staff accounts; no other role can add users.
2. **How they create:** From the User Register the Super Admin selects Add User, enters name, designation, employee ID, mobile, e-mail, roles and DS office, and saves; the system sends a one-time activation link and temporary password.
3. **How they edit:** The Super Admin edits designation, roles, DS office, contact details or validity dates from the user detail page; every change asks for a reason.
4. **How they send for approval:** User changes do not need approval; for sensitive roles (Approving Authority, Super Admin) the system can require a second Super Admin to confirm (configurable).
5. **How the approver sees pending items:** Where second confirmation is on, the confirming Super Admin sees pending role grants in a Pending Confirmations tab with requester, user and role.
6. **How the approver decides:** The confirming Super Admin approves or rejects with remarks; on rejection the role is not granted and the requester is informed.
7. **How the applicant / maker sees history:** Each official sees their roles, DS office, delegation and last login on My Profile and cannot edit their own roles.
8. **How the approver / auditor sees history:** The Super Admin and auditors see create, edit, role grant / revoke, delegation, deactivation and reactivation events with before / after values in the audit trail.

### Functional Capabilities
- User Register with filters (role, DS office, status Active / Inactive / Locked / Dormant, designation) and search by name, employee ID, mobile
- Create user with mandatory employee ID, designation, mobile and official e-mail; duplicate checks
- Assign multiple roles per user with optional validity from / to dates
- Map Deputy Secretary and Case Worker users to a DS office; one DS head per DS office
- Delegation: assign an acting officer for a period with the same role and DS scope; auto-expires
- Deactivate / reactivate with reason; deactivation revokes sessions and removes the user from work queues
- Re-route open tasks of a deactivated user to another user of the same role and DS office
- Optional second-person confirmation for grant of Approving Authority and Super Admin roles
- Bulk user upload from Excel template with row-level validation
- Unlock account and force password reset
- User access history view (roles held over time)
- Export of user and role list to Excel / PDF

### UI Screens
- User Register with filters and export
- Create / edit user form
- Role and DS office assignment panel
- Delegation setup dialog
- Deactivate / reactivate with task re-routing dialog
- Pending role confirmations tab
- Bulk user upload and validation result
- User access history view

### Logical API Operations
- Create user with duplicate checks
- Update user profile
- Grant / revoke role with validity
- Map user to DS office
- Create / end delegation
- Deactivate / reactivate user
- Re-route open tasks of a user
- Confirm / reject sensitive role grant
- Bulk upload users
- Search and export users
- Unlock and force password reset
- Get user access history

### Inputs
- Name, employee ID, designation, mobile, e-mail
- Roles and validity dates
- DS office
- Delegate user and period
- Reason for change
- Bulk upload file

### Outputs
- Active account with activation link
- Role and DS mappings
- Delegation records
- Re-routed tasks
- User list export

### Business Rules
- Employee ID, mobile and e-mail must be unique among active users
- A user cannot assign roles to themselves
- Deputy Secretary and Case Worker roles require a DS office
- Delegation cannot exceed 90 days and cannot be granted to a user without the same role eligibility
- Deactivation is blocked until open tasks are re-routed or explicitly left in the shared queue
- At least one active Super Admin must exist at all times

### Validations
- Mandatory fields
- Mobile 10 digits; e-mail format; official domain where configured
- Validity to-date after from-date
- Bulk file template version and column formats

### Calculations
- Effective role set = assigned roles valid today + active delegations

### Workflow
Created → Active → (Deactivate) Inactive → (Reactivate) Active; Sensitive role grant: Requested → Confirmed / Rejected

### Search Requirements
- Users by name, employee ID, mobile, role, DS office, status

### Documents
- Optional office order reference for role grant (uploaded PDF)

### Reports
- User and role list
- Users by DS office
- Delegations active / expired

### Notifications
- Activation link and temporary password to new user
- Role change and deactivation notice to the user
- Pending confirmation alert to Super Admins

### Security
- Only Super Admin can manage users
- All changes audited with before / after values
- Sensitive role grants optionally need two persons

### Integrations
- E-mail / SMS through the Notification Service

### Dependencies
- F01-001
- F01-003
- F12-002
- F14-001

### Assumptions
- BDA provides the list of officials and DS office mapping before go-live

### Risks
- Late deactivation of transferred officials
- Incorrect DS mapping exposing cases of another DS office

### Non Functional Requirements
- Role changes effective within 1 minute
- User register loads within 3 seconds for 1,000 users

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | User Register with filters and export | Medium | 6 |
| UI | Create / edit user form | Medium | 6 |
| UI | Role and DS office assignment panel | Medium | 6 |
| UI | Delegation setup dialog | Easy | 4 |
| UI | Deactivate / reactivate with task re-routing dialog | Medium | 6 |
| UI | Pending role confirmations tab | Easy | 4 |
| UI | Bulk user upload and validation result | Medium | 6 |
| UI | User access history view | Easy | 4 |
| API | Create user with duplicate checks | Medium | 6 |
| API | Update user profile | Easy | 4 |
| API | Grant / revoke role with validity | Medium | 6 |
| API | Map user to DS office | Easy | 4 |
| API | Create / end delegation | Medium | 6 |
| API | Deactivate / reactivate user | Medium | 6 |
| API | Re-route open tasks of a user | Complex | 8 |
| API | Confirm / reject sensitive role grant | Medium | 6 |
| API | Bulk upload users | Complex | 8 |
| API | Search and export users | Medium | 6 |
| API | Unlock and force password reset | Easy | 4 |
| API | Get user access history | Easy | 4 |
| Database | User master with designation and DS office | Medium | 4 |
| Database | User-role assignment with validity | Easy | 2 |
| Database | Delegation register | Easy | 2 |
| Database | Pending role confirmation store | Simple | 1 |
| Testing | User lifecycle and role assignment tests | Medium | 6 |
| Testing | Delegation, expiry and task re-routing tests | Complex | 8 |
| Testing | Bulk upload validation tests | Easy | 4 |
| Documentation | User administration guide | Medium | 3 |
| Documentation | Role and DS office mapping reference | Easy | 2 |

**Feature Total: 142 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 42 | 68 | 9 | 0 | 18 | 5 | **142** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Task re-routing touches every queue in Modules 03–09 and is estimated Complex
- No external integration channel in this feature; Integration row omitted.
