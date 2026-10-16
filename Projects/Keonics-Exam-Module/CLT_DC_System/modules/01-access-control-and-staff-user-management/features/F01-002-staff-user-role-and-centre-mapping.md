# F01-002 — Staff User, Role & Centre Mapping

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-002 |
| Feature Name | Staff User, Role & Centre Mapping |
| Module | 01 — Access Control & Staff User Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Super Admin creates and maintains staff accounts, assigns roles, maps users to district, test centre or question bank function (author, reviewer, committee), manages validity and delegation, deactivates and reactivates users and re-routes open tasks.

### Business Objective
Give KEONICS control over who can act on the CLT and remove access promptly.

### Actors
- Super Admin
- KEONICS Administrator (view)
- Staff user

### User Journey
1. **Who creates:** The Super Admin creates staff users.
2. **How they create:** The Super Admin selects Add User, enters name, designation, organisation, mobile, e-mail, roles, district / centre / function mapping and validity, and saves; an activation link is sent.
3. **How they edit:** The Super Admin edits roles, mapping and validity with a reason.
4. **How they send for approval:** Grants of sensitive roles (Super Admin, Result Approver, Question Bank Administrator) need second Super Admin confirmation.
5. **How the approver sees pending items:** The confirming Super Admin sees pending grants.
6. **How the approver decides:** The confirming Super Admin approves or rejects with remarks.
7. **How the applicant / maker sees history:** Users see their roles and mappings on My Profile.
8. **How the approver / auditor sees history:** Auditors see every user change with before / after values.

### Functional Capabilities
- User register with filters and export
- Create user with duplicate checks
- Multiple roles with validity dates
- District, centre and question bank function mapping
- Delegation for leave periods
- Deactivate / reactivate with task re-routing
- Second-person confirmation of sensitive roles
- Bulk upload from Excel
- Access history

### UI Screens
- User register
- Create / edit user
- Role and mapping panel
- Delegation dialog
- Deactivate with task re-routing
- Pending role confirmations
- Bulk user upload result

### Logical API Operations
- Create / update user
- Grant / revoke role with validity
- Map user to district / centre / function
- Delegation create / end
- Deactivate / reactivate
- Re-route open tasks
- Confirm sensitive role grant
- Bulk upload users
- Search and export users

### Inputs
- User details
- Roles, mapping, validity
- Reason

### Outputs
- Active users
- Mappings

### Business Rules
- Mobile and e-mail unique
- Users cannot change their own roles
- Question bank Author and Reviewer roles cannot be held by the same user for the same subject
- At least one active Super Admin

### Validations
- Mandatory fields
- Formats

### Calculations
- Effective roles = valid roles + delegations

### Workflow
Created → Active → Inactive → Active

### Search Requirements
- Users by name, role, district, centre

### Documents
- Office order reference

### Reports
- User and role list

### Notifications
- Activation link
- Role change notice

### Security
- Super Admin only

### Integrations
- None

### Dependencies
- F01-001
- F01-003

### Assumptions
- KEONICS provides official lists

### Risks
- Late deactivation of transferred staff

### Non Functional Requirements
- Changes effective within 1 minute

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | User register | Medium | 6 |
| UI | Create / edit user | Medium | 6 |
| UI | Role and mapping panel | Medium | 6 |
| UI | Delegation dialog | Easy | 4 |
| UI | Deactivate with task re-routing | Medium | 6 |
| UI | Pending role confirmations | Easy | 4 |
| UI | Bulk user upload result | Medium | 6 |
| API | Create / update user | Medium | 6 |
| API | Grant / revoke role with validity | Medium | 6 |
| API | Map user to district / centre / function | Easy | 4 |
| API | Delegation create / end | Medium | 6 |
| API | Deactivate / reactivate | Easy | 4 |
| API | Re-route open tasks | Complex | 8 |
| API | Confirm sensitive role grant | Easy | 4 |
| API | Bulk upload users | Medium | 6 |
| API | Search and export users | Easy | 4 |
| Database | User master, role assignment and mapping | Medium | 4 |
| Database | Delegation and confirmation store | Easy | 2 |
| Testing | User lifecycle and mapping tests | Medium | 6 |
| Testing | Delegation and re-routing tests | Medium | 6 |
| Documentation | User administration guide | Easy | 2 |

**Feature Total: 106 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 38 | 48 | 6 | 0 | 12 | 2 | **106** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Task re-routing across queues rated Complex
- No external integration channel in this feature; Integration row omitted.
