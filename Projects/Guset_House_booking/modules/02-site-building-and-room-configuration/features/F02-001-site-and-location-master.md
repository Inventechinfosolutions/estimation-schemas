# F02-001 — Site and Location Master

| Field | Value |
|-------|-------|
| Feature ID | F02-001 |
| Feature Name | Site and Location Master |
| Module | 02 — Site, Building & Room Configuration |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Administrator creates and maintains guest-house sites/locations with address and administrative information.

### Business Objective
Provide the top-level property locations against which buildings and bookings are organised.

### Actors
- Platform Administrator
- Site Administrator

### User Journey
1. Platform Administrator creates site records.
2. Administrator enters name, address, location details, and administrative contacts, then saves.
3. Administrator edits site details; deactivates sites no longer bookable.
4. Approval does not apply in Phase 1 — direct save with audit.
5. No approver inbox.
6. No approver decision.
7. Administrator sees site change history on detail view.
8. Auditor reviews site master change history.

### Functional Capabilities
- Create site
- Edit site
- Activate/deactivate site
- List/search sites
- View site detail

### UI Screens
- Site register
- Site create/edit form
- Site detail read-only view
- Deactivate site confirmation

### Logical API Operations
- List/search sites
- Create site
- Update site
- Deactivate site
- Get site detail

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Inactive sites excluded from employee browse
- Site code/name uniqueness

### Validations
- Name and address mandatory
- Valid contact formats

### Calculations
- None beyond display counters

### Workflow
Draft/Active → Inactive

### Search Requirements
Filter by name, city, status

### Documents
Optional site information attachment embedded

### Reports
None

### Notifications
None

### Security
- Admin roles only
- Audit writes

### Integrations
None

### Dependencies
- F01-004

### Assumptions
- Geo-coordinates optional

### Risks
- Duplicate sites confuse booking

### Non Functional Requirements
- Register paginated for multi-site estates

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Site register | Medium | 6 |
| UI | Site create/edit form | Medium | 6 |
| UI | Site detail read-only view | Easy | 4 |
| UI | Deactivate site confirmation | Simple | 2 |
| API | List/search sites | Medium | 6 |
| API | Create site | Medium | 6 |
| API | Update site | Medium | 6 |
| API | Deactivate site | Easy | 4 |
| API | Get site detail | Easy | 4 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 54 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Geo-coordinates optional / Duplicate sites confuse booking.
