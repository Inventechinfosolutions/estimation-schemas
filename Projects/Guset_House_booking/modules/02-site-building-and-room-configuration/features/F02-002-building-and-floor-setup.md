# F02-002 — Building and Floor Setup

| Field | Value |
|-------|-------|
| Feature ID | F02-002 |
| Feature Name | Building and Floor Setup |
| Module | 02 — Site, Building & Room Configuration |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Administrator configures buildings under each site and floor-wise structure within each building.

### Business Objective
Model physical building/floor hierarchy needed for room placement and navigation.

### Actors
- Platform Administrator
- Site Administrator

### User Journey
1. Administrator creates buildings under a selected site.
2. Administrator defines building attributes and adds floors in order.
3. Administrator edits building/floor labels and sequence; retires unused floors.
4. Approval does not apply — direct admin save.
5. No approver inbox.
6. No approver decision.
7. Administrator sees hierarchy on site structure view and change history.
8. Auditor sees structural change history.

### Functional Capabilities
- Add building to site
- Configure floors
- Reorder/rename floors
- Deactivate building/floor
- View structure tree

### UI Screens
- Building register for site
- Building create/edit form
- Floor configuration screen
- Deactivate building confirmation

### Logical API Operations
- List buildings by site
- Save building
- Save floors for building
- Deactivate building/floor

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Building belongs to one site
- Floor numbers unique within building
- Cannot deactivate building with active future bookings without override policy

### Validations
- Building name mandatory
- At least one floor when rooms will be added

### Calculations
- Floor count

### Workflow
BuildingActive with FloorsConfigured

### Search Requirements
Search buildings by name within site

### Documents
None

### Reports
None

### Notifications
None

### Security
- Site-scoped admin where configured

### Integrations
None

### Dependencies
- F02-001

### Assumptions
- Floors may be non-contiguous labels (e.g., G, 1, 2)

### Risks
- Floor renumbering after rooms exist causes confusion

### Non Functional Requirements
- Structure tree loads for typical building sizes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Building register for site | Medium | 6 |
| UI | Building create/edit form | Medium | 6 |
| UI | Floor configuration screen | Complex | 12 |
| UI | Deactivate building confirmation | Simple | 2 |
| API | List buildings by site | Easy | 4 |
| API | Save building | Medium | 6 |
| API | Save floors for building | Complex | 8 |
| API | Deactivate building/floor | Easy | 4 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 60 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Floors may be non-contiguous labels (e.g., G, 1, 2) / Floor renumbering after rooms exist causes confusion.
