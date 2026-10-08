# F05-003 — Self Check-in and Occupancy Tracking

| Field | Value |
|-------|-------|
| Feature ID | F05-003 |
| Feature Name | Self Check-in and Occupancy Tracking |
| Module | 05 — Access Credentials & Guest Check-in |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Allows users to check in using credentials/QR and tracks occupancy including active stays and no-shows.

### Business Objective
Record arrival and stay state for operational control and utilization.

### Actors
- Employee Guest
- Site Administrator

### User Journey
1. Employee creates check-in event by scanning QR or entering booking identifier on/after allowed check-in window.
2. System validates credential and booking dates, marks Active Stay.
3. Site Administrator may correct status (e.g., mark no-show) with reason.
4. Approval does not apply for self check-in; admin corrections are direct with audit.
5. No approver inbox.
6. No approver decision workflow.
7. Employee sees check-in status on booking; admin sees occupancy board.
8. Auditor sees check-in and no-show history.

### Functional Capabilities
- Self check-in via QR/code
- Validate credential window
- Mark active stay
- Mark no-show
- Occupancy board

### UI Screens
- Self check-in screen
- QR scan check-in screen
- Occupancy board
- Mark no-show dialog

### Logical API Operations
- Check in with credential
- Admin mark no-show
- List occupancy for site/date
- Get booking occupancy status

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Check-in only for confirmed bookings in window
- No-show after configured cutoff
- Active stay blocks duplicate check-in

### Validations
- Credential must be active
- Site match if site-scoped check-in

### Calculations
- No-show cutoff time

### Workflow
Confirmed → CheckedIn(ActiveStay) | NoShow → CheckedOut (future light)

### Search Requirements
Occupancy filter by building/floor/status

### Documents
None

### Reports
Feeds utilization

### Notifications
Optional check-in confirmation

### Security
- Credential validation server-side
- Admin corrections audited

### Integrations
None required

### Dependencies
- F05-001
- F03-005

### Assumptions
- Checkout process can be light status update if not deeply specified

### Risks
- Early/late arrivals outside window need admin help

### Non Functional Requirements
- Occupancy board near-real-time

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Self check-in screen | Medium | 6 |
| UI | QR scan check-in screen | Complex | 12 |
| UI | Occupancy board | Very High | 16 |
| UI | Mark no-show dialog | Easy | 4 |
| API | Check in with credential | Complex | 8 |
| API | Admin mark no-show | Medium | 6 |
| API | List occupancy for site/date | Complex | 8 |
| API | Get booking occupancy status | Easy | 4 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 79 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Checkout process can be light status update if not deeply specified / Early/late arrivals outside window need admin help.
