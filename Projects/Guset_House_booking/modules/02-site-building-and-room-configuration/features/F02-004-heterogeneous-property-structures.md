# F02-004 — Heterogeneous Property Structures

| Field | Value |
|-------|-------|
| Feature ID | F02-004 |
| Feature Name | Heterogeneous Property Structures |
| Module | 02 — Site, Building & Room Configuration |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Ensures configuration and booking navigation work when buildings differ in floors, room types, and layout without forcing a uniform template.

### Business Objective
Avoid blocking multi-site rollout when guest houses have different physical structures.

### Actors
- Platform Administrator
- Site Administrator
- Employee Guest

### User Journey
1. Administrator configures atypical structures using flexible floor/room setup (no single mandatory template).
2. Administrator uses structure validation checklist when publishing a site for booking.
3. Administrator adjusts structure; system warns on orphaned rooms.
4. Approval does not apply beyond optional 'ready for booking' flag set by admin.
5. No approver inbox.
6. No approver decision.
7. Administrator sees readiness checklist history per site.
8. Auditor sees readiness flag changes.

### Functional Capabilities
- Flexible hierarchy without uniform floor counts
- Site booking-readiness checklist
- Warn on incomplete structure
- Employee browse respects actual structure

### UI Screens
- Site structure overview screen
- Booking readiness checklist screen
- Structure warning dialog

### Logical API Operations
- Get site structure overview
- Validate site booking readiness
- Set site ready-for-booking flag

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Sites not marked ready are hidden from employee booking browse
- Buildings may have different floor counts and room type mixes

### Validations
- Readiness requires at least one Available room

### Calculations
- Counts of buildings/floors/available rooms

### Workflow
Configuring → ReadyForBooking → Suspended

### Search Requirements
Filter sites by readiness

### Documents
None

### Reports
None

### Notifications
None

### Security
- Admin flag changes audited

### Integrations
None

### Dependencies
- F02-001
- F02-002
- F02-003

### Assumptions
- No CAD/floor-plan designer in scope

### Risks
- Admins mark ready with incorrect inventory

### Non Functional Requirements
- Validation completes quickly for large sites

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Site structure overview screen | Complex | 12 |
| UI | Booking readiness checklist screen | Medium | 6 |
| UI | Structure warning dialog | Simple | 2 |
| API | Get site structure overview | Medium | 6 |
| API | Validate site booking readiness | Complex | 8 |
| API | Set site ready-for-booking flag | Medium | 6 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 51 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: No CAD/floor-plan designer in scope / Admins mark ready with incorrect inventory.
