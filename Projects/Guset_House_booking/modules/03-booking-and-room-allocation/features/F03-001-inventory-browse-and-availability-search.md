# F03-001 — Inventory Browse and Availability Search

| Field | Value |
|-------|-------|
| Feature ID | F03-001 |
| Feature Name | Inventory Browse and Availability Search |
| Module | 03 — Booking & Room Allocation |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Employees browse sites, buildings, and rooms and search availability for selected dates.

### Business Objective
Help employees find bookable rooms that match stay dates across locations.

### Actors
- Employee Guest

### User Journey
1. Employee creates a search by choosing dates and optional site filters.
2. Employee runs search and browses results; opens room detail.
3. Employee refines filters; no persistent 'edit' of a search entity beyond refining criteria.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Employee may see recent searches only if stored locally/session — no approval history.
8. Auditor may review anonymised search metrics only if later reported — not required here.

### Functional Capabilities
- Search by date range and site
- List available rooms
- View room detail
- Empty states when no availability

### UI Screens
- Availability search screen
- Search results list
- Room detail view
- No availability empty state

### Logical API Operations
- Search available rooms
- Get room detail for booking
- List ready sites for browse

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Only Ready sites and Available rooms
- Respect existing bookings when computing availability

### Validations
- End date after start date
- Stay within configured max length

### Calculations
- Nights/days count
- Indicative price preview

### Workflow
CriteriaEntered → ResultsShown

### Search Requirements
Primary capability of this feature

### Documents
None

### Reports
None

### Notifications
None

### Security
- Only authenticated eligible employees
- No leaking unavailable room internals

### Integrations
None

### Dependencies
- F02-003
- F02-004
- F01-002

### Assumptions
- Availability computed against confirmed/held bookings per payment-hold policy

### Risks
- Slow search if indexes missing

### Non Functional Requirements
- Search p95 suitable for concurrent users

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Availability search screen | Complex | 12 |
| UI | Search results list | Medium | 6 |
| UI | Room detail view | Medium | 6 |
| UI | No availability empty state | Simple | 2 |
| API | Search available rooms | Very High | 16 |
| API | Get room detail for booking | Easy | 4 |
| API | List ready sites for browse | Simple | 2 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 62 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Availability computed against confirmed/held bookings per payment-hold policy / Slow search if indexes missing.
