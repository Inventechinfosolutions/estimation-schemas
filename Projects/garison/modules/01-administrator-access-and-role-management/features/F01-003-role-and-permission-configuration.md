# F01-003 — Role & Permission Configuration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-003 |
| Feature Name | Role & Permission Configuration |
| Module | 01 — Administrator Access & Role Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Configure roles and their permissions as a matrix of portal areas (products, combinations, taxonomy, attributes, media, sources, workflow, publishing, import, enquiries, SEO, users, audit) against actions (view, create, edit, delete, submit, approve, publish, export). Seeded with the four default roles from the proposal.

### Business Objective
Let Garrison adjust who can do what as its catalogue team grows, without code changes, while enforcing permissions on every server operation.

### Actors
- Super Administrator
- Auditor (read-only view of matrix)

### User Journey
1. **Who creates:** The Super Administrator creates and maintains roles; the four default roles are seeded at go-live and marked as system roles.
2. **How they create:** They create a role by name and description, or clone an existing role, then tick permissions in the matrix grouped by portal area.
3. **How they edit:** They edit the matrix at any time; system roles can have permissions adjusted but cannot be deleted.
4. **How they send for approval:** Role configuration does not require approval; changes are effective on save.
5. **How the approver sees pending items:** There is no approver inbox for role changes.
6. **How the approver decides:** No approval decision applies; the Super Administrator decides directly.
7. **How the maker sees history:** Users see the effect as menu items and actions appearing or disappearing; they can view their effective permissions on My Profile.
8. **How the approver / auditor sees history:** Auditors see every role and permission change with before/after matrix values in the audit log (F01-004).

### Functional Capabilities
- Role register showing user count per role
- Create, edit, clone and delete (non-system, unused) roles
- Permission matrix editor by portal area and action, with select-all per area
- Field-scope permission for Content Administrator (content fields only on products)
- Effective permissions viewer for any user (union of roles)
- Server-side authorisation check on every admin operation; UI hides unauthorised actions
- Seed default roles: Super Administrator, Catalogue Administrator, Catalogue Reviewer, Content Administrator

### UI Screens
- Role register
- Role create / edit form
- Permission matrix editor by area and action
- Clone role dialog
- Effective permissions viewer for a user

### Logical API Operations
- List roles with user counts
- Create or update role
- Get permission catalogue
- Save role permission matrix
- Clone role
- Delete unused role
- Resolve effective permissions for user
- Enforce authorisation on admin operations

### Inputs
- Role name, description
- Permission selections per area/action
- Field-scope selection for content-only editing

### Outputs
- Role definitions and permission matrix
- Effective permission set per user
- Audit entries

### Business Rules
- System roles cannot be deleted or renamed
- A role assigned to users cannot be deleted
- Super Administrator always retains user and role management permissions
- Effective permissions are the union of all assigned roles

### Validations
- Role name unique and mandatory
- At least one permission per role

### Calculations
- Effective permissions = union of permissions across assigned roles

### Workflow
Not applicable (configuration saved directly)

### Search Requirements
- Role name

### Documents
- None

### Reports
- Role-permission matrix export (CSV) for Garrison review

### Notifications
- None

### Security
- Authorisation enforced server-side; UI hiding is convenience only
- Permission checks cached per session and invalidated on role change

### Integrations
- None

### Dependencies
- F01-002
- F01-004

### Assumptions
- Access model is User → Role → Permissions; no department or post hierarchy

### Risks
- Over-granting permissions to many users weakens maker-checker controls

### Non Functional Requirements
- Authorisation check adds negligible latency (< 10 ms)

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Role register | Easy | 4 |
| UI | Role create / edit form | Easy | 4 |
| UI | Permission matrix editor by area and action | Complex | 12 |
| UI | Clone role dialog | Simple | 2 |
| UI | Effective permissions viewer for a user | Medium | 6 |
| API | List roles with user counts | Simple | 2 |
| API | Create or update role | Medium | 6 |
| API | Get permission catalogue | Simple | 2 |
| API | Save role permission matrix | Complex | 8 |
| API | Clone role | Easy | 4 |
| API | Delete unused role | Easy | 4 |
| API | Resolve effective permissions for user | Medium | 6 |
| API | Enforce authorisation on admin operations | Complex | 8 |
| Database | Role master | Simple | 1 |
| Database | Permission catalogue | Easy | 2 |
| Database | Role-permission matrix | Easy | 2 |
| Database | Default role and permission seed | Easy | 2 |
| Testing | Permission matrix behaviour for each default role | Complex | 8 |
| Testing | Server-side enforcement across all admin operations | Complex | 8 |
| Testing | System role and in-use role protection | Easy | 4 |
| Documentation | Role and permission reference matrix | Medium | 3 |

**Feature Total: 98 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 40 | 7 | 0 | 20 | 3 | **98** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Field-scope editing for Content Administrator increases enforcement complexity
- Enforcement across all operations is estimated once here and reused by every feature
- No external integration channel in this feature; Integration row omitted.
