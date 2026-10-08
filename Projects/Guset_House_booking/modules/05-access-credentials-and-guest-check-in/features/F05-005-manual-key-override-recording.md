# F05-005 — Manual Key Override Recording

| Field | Value |
|-------|-------|
| Feature ID | F05-005 |
| Feature Name | Manual Key Override Recording |
| Module | 05 — Access Credentials & Guest Check-in |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Allows on-site authorities to record manual physical key overrides when digital access is unavailable or inappropriate.

### Business Objective
Preserve operational continuity and audit trail when physical keys are used.

### Actors
- Site Administrator
- On-site authority

### User Journey
1. On-site authority/admin creates an override event against a booking or room.
2. Enters reason and time; saves override record.
3. May correct notes; cannot delete without elevated policy — prefer reverse entry.
4. Approval does not apply in Phase 1 (direct with audit).
5. No approver inbox.
6. No approver decision.
7. Admin sees override history on booking/occupancy.
8. Auditor reviews override reasons and actors.

### Functional Capabilities
- Record key override
- Require reason
- List overrides
- Link to booking/room

### UI Screens
- Manual key override form
- Override history register
- Override confirmation

### Logical API Operations
- Create key override event
- List overrides
- Get override detail

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Reason mandatory
- Site-scoped access
- Does not auto-change payment state

### Validations
- Booking or room reference required

### Calculations
- None beyond display counters

### Workflow
OverrideRecorded

### Search Requirements
Filter by site/date/actor

### Documents
None

### Reports
Override counts optional in admin MIS

### Notifications
None

### Security
- Role restricted
- Full audit

### Integrations
None

### Dependencies
- F03-005
- F01-004

### Assumptions
- Physical key custody remains offline process

### Risks
- Incomplete recording reduces audit value

### Non Functional Requirements
- Quick entry on site desk

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Manual key override form | Easy | 4 |
| UI | Override history register | Medium | 6 |
| UI | Override confirmation | Simple | 2 |
| API | Create key override event | Medium | 6 |
| API | List overrides | Easy | 4 |
| API | Get override detail | Simple | 2 |
| Database | Persistence for feature entities/constraints | Simple | 1 |
| Testing | Feature test coverage | Easy | 4 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 31 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Physical key custody remains offline process / Incomplete recording reduces audit value.
