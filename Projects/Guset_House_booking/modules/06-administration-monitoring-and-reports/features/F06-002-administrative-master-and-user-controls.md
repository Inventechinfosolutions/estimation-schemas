# F06-002 — Administrative Master and User Controls

| Field | Value |
|-------|-------|
| Feature ID | F06-002 |
| Feature Name | Administrative Master and User Controls |
| Module | 06 — Administration, Monitoring & Reports |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Administrative controls to manage sites, buildings, rooms, and users within policy (oversight entry points).

### Business Objective
Centralise admin navigation for property and user management responsibilities.

### Actors
- Platform Administrator
- Site Administrator

### User Journey
1. Administrator uses admin console hubs to reach masters/users.
2. Navigates to Module 02/01 maintenance screens; may perform allowed edits per role.
3. Edits occur in owning modules; this feature provides console shell and shortcuts.
4. Approval does not apply beyond owning module rules.
5. No separate approver inbox here.
6. No separate approver decision here.
7. Admin sees recent admin actions feed.
8. Auditor sees admin action feed.

### Functional Capabilities
- Admin home/console
- Shortcuts to sites/buildings/rooms/users
- Recent admin actions
- Respect role scope

### UI Screens
- Admin console home
- Admin shortcuts navigation
- Recent admin actions panel

### Logical API Operations
- Get admin console summary
- List recent admin actions

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Does not duplicate deep master logic — routes to Modules 01/02
- Enforce role scope

### Validations
- None

### Calculations
- None beyond display counters

### Workflow
View/Navigate

### Search Requirements
Console search users/sites shortcut

### Documents
None

### Reports
None

### Notifications
None

### Security
- Admin roles only

### Integrations
None

### Dependencies
- F01-004
- F02-001
- F02-003

### Assumptions
- Deep forms remain in Modules 01/02

### Risks
- Duplicate CRUD if not carefully bounded

### Non Functional Requirements
- Console snappy

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Admin console home | Medium | 6 |
| UI | Admin shortcuts navigation | Easy | 4 |
| UI | Recent admin actions panel | Easy | 4 |
| API | Get admin console summary | Medium | 6 |
| API | List recent admin actions | Easy | 4 |
| Database | Persistence for feature entities/constraints | Simple | 1 |
| Testing | Feature test coverage | Easy | 4 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 31 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Deep forms remain in Modules 01/02 / Duplicate CRUD if not carefully bounded.
