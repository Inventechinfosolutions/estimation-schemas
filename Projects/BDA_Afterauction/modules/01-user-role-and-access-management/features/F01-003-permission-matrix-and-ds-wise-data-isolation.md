# F01-003 — Permission Matrix & DS-wise Data Isolation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-003 |
| Feature Name | Permission Matrix & DS-wise Data Isolation |
| Module | 01 — User, Role & Access Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Configurable permission matrix mapping each role to menus, screens, actions and record scopes, together with enforced DS-wise data isolation so that Deputy Secretaries and their case workers see only cases allocated to their DS office in every queue, case file, dashboard, report, search and export.

### Business Objective
Meet the RFP requirement that permissions are configurable without code changes and that DS-wise isolation is enforced everywhere.

### Actors
- Super Admin
- All staff roles (subject to permissions)

### User Journey
1. **Who creates:** The Super Admin creates or edits permission sets; roles are pre-seeded with the RFP role list.
2. **How they create:** The Super Admin opens the Permission Matrix, selects a role, ticks menus, actions (view, create, edit, approve, sign, export) and record scope (All, Own DS office, Own cases), and saves as a new draft version.
3. **How they edit:** The Super Admin edits the draft matrix; a side-by-side comparison shows changes against the active version.
4. **How they send for approval:** The Super Admin submits the draft for activation; activation can require a second Super Admin confirmation (configurable).
5. **How the approver sees pending items:** The confirming Super Admin sees pending matrix versions with a change summary.
6. **How the approver decides:** The confirming Super Admin activates or rejects with remarks; activation applies on users' next request.
7. **How the applicant / maker sees history:** Staff see only permitted menus and actions; a disallowed action returns an access-denied message without data.
8. **How the approver / auditor sees history:** The Super Admin and auditors view all matrix versions, who changed and activated them, and access-denied events in the audit trail.

### Functional Capabilities
- Pre-seeded roles: Successful Bidder, Result Verifier, Approving Authority, Payment Reconciler, Deputy Secretary, Case Worker, Finance Officer, Auction Admin, Super Admin, Read-only Viewer
- Create custom roles by cloning an existing role
- Permission matrix by role × menu / screen × action (view, create, edit, delete, submit, approve, sign, export, configure)
- Record scope per role: All cases, Own DS office, Own assigned cases
- DS-wise isolation filter applied centrally to queries, search, dashboards, reports, report builder and exports
- Field-level masking for bidder PAN, Aadhaar reference, bank account for roles without permission
- Versioned matrix with draft, active and archived states and comparison view
- Optional two-person activation of matrix changes
- Effective permission preview for a selected user
- Access-denied logging

### UI Screens
- Role list and clone role
- Permission matrix editor (role × screen × action)
- Record scope and field masking settings
- Matrix version comparison
- Pending activation view
- Effective permissions preview for a user

### Logical API Operations
- Create / clone role
- Save permission matrix draft
- Compare matrix versions
- Submit and activate matrix version
- Resolve effective permissions for a user
- Central authorisation check (action and record scope)
- DS-wise data filter for queries and exports
- Field masking policy evaluation
- Log access-denied events

### Inputs
- Role name
- Menu / action selections
- Record scope
- Masked fields
- Activation remarks

### Outputs
- Active permission matrix version
- Effective permission preview
- Access-denied log

### Business Rules
- Super Admin role cannot be removed from the last Super Admin
- Read-only Viewer cannot be given create, approve or sign actions
- Successful Bidder role is fixed to own sites only and cannot be widened
- DS-scoped roles never see cases of another DS office even through search or export
- Matrix changes apply to new requests only

### Validations
- Role name unique
- At least one permission per role
- Scope compatible with role type

### Calculations
- Effective permissions = union of permissions of all valid roles and active delegations, narrowed by record scope

### Workflow
Draft → Submitted → Active → Archived (on next activation); Rejected returns to Draft

### Search Requirements
- Roles by name
- Matrix versions by date and author

### Documents
- None

### Reports
- Role-permission matrix export
- Access-denied events report

### Notifications
- Pending activation alert to Super Admins

### Security
- Authorisation enforced on the server for every API, never only in the UI
- Isolation filter applied at the data access layer

### Integrations
- None

### Dependencies
- F01-002
- F14-001

### Assumptions
- Three DS offices (DS1, DS2, DS3) at go-live; more can be added through F02-002

### Risks
- Missed isolation in a custom report path; mitigated by central data filter and dedicated tests

### Non Functional Requirements
- Authorisation check adds under 20 ms per request

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Role list and clone role | Easy | 4 |
| UI | Permission matrix editor (role × screen × action) | Complex | 12 |
| UI | Record scope and field masking settings | Medium | 6 |
| UI | Matrix version comparison | Medium | 6 |
| UI | Pending activation view | Easy | 4 |
| UI | Effective permissions preview for a user | Medium | 6 |
| API | Create / clone role | Easy | 4 |
| API | Save permission matrix draft | Medium | 6 |
| API | Compare matrix versions | Medium | 6 |
| API | Submit and activate matrix version | Medium | 6 |
| API | Resolve effective permissions for a user | Complex | 8 |
| API | Central authorisation check (action and record scope) | Very High | 16 |
| API | DS-wise data filter for queries and exports | Very High | 16 |
| API | Field masking policy evaluation | Complex | 8 |
| API | Log access-denied events | Easy | 4 |
| Database | Role, permission and matrix version store | Medium | 4 |
| Database | Record scope and masking policy store | Easy | 2 |
| Testing | Permission matrix configuration tests | Medium | 6 |
| Testing | DS-wise isolation tests across queues, reports and exports | Very High | 12 |
| Testing | Field masking and access-denied tests | Medium | 6 |
| Documentation | Role and permission reference matrix | Medium | 3 |
| Documentation | Administrator guide to permission changes | Easy | 2 |

**Feature Total: 147 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 38 | 74 | 6 | 0 | 24 | 5 | **147** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Central authorisation and DS filter are rated Very High because every module depends on them
- No external integration channel in this feature; Integration row omitted.
