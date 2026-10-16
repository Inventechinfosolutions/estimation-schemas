# F01-003 — Permission Matrix & Data Scope

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-003 |
| Feature Name | Permission Matrix & Data Scope |
| Module | 01 — Access Control & Staff User Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Configurable matrix of roles × screens × actions with record scope (All, District, Centre, Own) and field masking, versioned with two-person activation, enforced centrally on every API, report and export.

### Business Objective
Meet the requirement that only authorised users access data, with configuration instead of code changes.

### Actors
- Super Admin
- All staff roles

### User Journey
1. **Who creates:** The Super Admin edits permission versions; roles are pre-seeded.
2. **How they create:** The Super Admin opens the matrix, selects a role, sets actions and scope, and saves a draft.
3. **How they edit:** The Super Admin edits the draft and compares it with the active version.
4. **How they send for approval:** The draft is submitted for activation by a second Super Admin.
5. **How the approver sees pending items:** The second Super Admin sees pending versions with change summary.
6. **How the approver decides:** The second Super Admin activates or rejects.
7. **How the applicant / maker sees history:** Users see only permitted menus and actions.
8. **How the approver / auditor sees history:** Auditors see versions and access-denied events.

### Functional Capabilities
- Pre-seeded roles: Super Admin, KEONICS Administrator, Approving Authority, Scrutiny Officer, Registration Centre Operator, SME Author, Reviewer, Technical Committee Member, Question Bank Administrator, Proctor, Centre Operator, EMU Monitor, Result Officer, Finance Officer, Helpdesk Executive, Read-only Viewer
- Role × screen × action matrix
- Record scope: All / District / Centre / Own
- Field masking for Aadhaar, mobile and photo
- Versioning with two-person activation
- Effective permission preview

### UI Screens
- Role list and clone
- Permission matrix editor
- Scope and masking settings
- Version comparison and activation
- Effective permission preview

### Logical API Operations
- Save matrix draft
- Activate matrix version
- Central authorisation check
- Data scope filter for queries and exports
- Field masking evaluation
- Effective permissions for user
- Log access-denied

### Inputs
- Permissions
- Scope
- Masking

### Outputs
- Active matrix

### Business Rules
- Authorisation enforced server-side
- Candidate and proctor roles fixed to own data
- Read-only Viewer cannot act

### Validations
- At least one permission per role

### Calculations
- Effective permissions = union of roles narrowed by scope

### Workflow
Draft → Active → Archived

### Search Requirements
- Roles

### Documents
- None

### Reports
- Permission matrix export

### Notifications
- Activation requests

### Security
- Two-person activation

### Integrations
- None

### Dependencies
- F01-002

### Assumptions
- Roles confirmed in FRS

### Risks
- Missed scope on custom reports; central filter mitigates

### Non Functional Requirements
- Check under 20 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Role list and clone | Easy | 4 |
| UI | Permission matrix editor | Complex | 12 |
| UI | Scope and masking settings | Medium | 6 |
| UI | Version comparison and activation | Medium | 6 |
| UI | Effective permission preview | Easy | 4 |
| API | Save matrix draft | Medium | 6 |
| API | Activate matrix version | Medium | 6 |
| API | Central authorisation check | Very High | 16 |
| API | Data scope filter for queries and exports | Complex | 8 |
| API | Field masking evaluation | Medium | 6 |
| API | Effective permissions for user | Medium | 6 |
| API | Log access-denied | Easy | 4 |
| Database | Role, permission and version store | Medium | 4 |
| Testing | Authorisation and scope tests across modules | Complex | 8 |
| Testing | Masking tests | Easy | 4 |
| Documentation | Role-permission reference | Medium | 3 |

**Feature Total: 103 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 52 | 4 | 0 | 12 | 3 | **103** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Central authorisation rated Very High
- No external integration channel in this feature; Integration row omitted.
