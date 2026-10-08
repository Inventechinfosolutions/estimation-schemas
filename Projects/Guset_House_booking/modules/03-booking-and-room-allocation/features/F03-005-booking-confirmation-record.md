# F03-005 — Booking Confirmation Record

| Field | Value |
|-------|-------|
| Feature ID | F03-005 |
| Feature Name | Booking Confirmation Record |
| Module | 03 — Booking & Room Allocation |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Generates a booking confirmation including booking period, location, and access credential references after allocation.

### Business Objective
Provide the employee with an authoritative confirmation artefact for travel and entry.

### Actors
- Employee Guest
- System

### User Journey
1. System creates confirmation after allocation succeeds.
2. Employee views/downloads confirmation from portal.
3. Regeneration only when credentials reissued or admin correction — not free edit.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Employee sees confirmation version/history if regenerated.
8. Auditor sees confirmation issuance log.

### Functional Capabilities
- Generate confirmation
- View confirmation
- Download/print confirmation
- Include credential reference

### UI Screens
- Booking confirmation view
- Confirmation download action
- Confirmation not-ready empty state

### Logical API Operations
- Generate confirmation
- Get confirmation
- Download confirmation document

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Confirmation only when Allocated
- Must show period, location, credential reference

### Validations
- Booking in confirmed state

### Calculations
- None beyond display counters

### Workflow
Allocated → Confirmed

### Search Requirements
Find confirmation by booking ref

### Documents
Confirmation document/PDF

### Reports
None

### Notifications
Confirmation notification via Module 07

### Security
- Owner-only access

### Integrations
Notification Service

### Dependencies
- F03-004
- F05-001
- F07-002

### Assumptions
- PDF or printable HTML acceptable

### Risks
- Credential reference shown before SMS delivery confuses users

### Non Functional Requirements
- Download available promptly after confirm

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Booking confirmation view | Medium | 6 |
| UI | Confirmation download action | Easy | 4 |
| UI | Confirmation not-ready empty state | Simple | 2 |
| API | Generate confirmation | Complex | 8 |
| API | Get confirmation | Easy | 4 |
| API | Download confirmation document | Medium | 6 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 40 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: PDF or printable HTML acceptable / Credential reference shown before SMS delivery confuses users.
