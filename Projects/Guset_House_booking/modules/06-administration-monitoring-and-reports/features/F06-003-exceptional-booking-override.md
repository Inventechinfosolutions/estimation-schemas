# F06-003 — Exceptional Booking Override

| Field | Value |
|-------|-------|
| Feature ID | F06-003 |
| Feature Name | Exceptional Booking Override |
| Module | 06 — Administration, Monitoring & Reports |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Allows administrators to override bookings in exceptional scenarios with mandatory reason and audit.

### Business Objective
Handle edge cases (compassionate stay, corrections) without breaking auditability.

### Actors
- Platform Administrator
- Site Administrator
- Auditor

### User Journey
1. Administrator creates an override action on a booking (cancel confirmed, move room, extend dates — as policy allows).
2. Selects override type, enters reason, confirms impact.
3. May reverse some overrides with a new compensating override.
4. Approval does not apply in Phase 1 — dual-control optional later; reason + audit required.
5. No approver inbox in Phase 1.
6. No approver decision in Phase 1.
7. Admin and employee (if affected) see override notes on booking history.
8. Auditor reviews override register.

### Functional Capabilities
- Override cancel
- Override room change
- Override date adjustment (policy)
- Mandatory reason
- Override register

### UI Screens
- Booking override dialog
- Override impact confirmation
- Override register

### Logical API Operations
- Apply booking override
- List booking overrides
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
- Conflict checks still apply on move/extend
- Payment refunds out of scope unless separately specified

### Validations
- Override type allowed for role
- Target room available if move

### Calculations
- None beyond display counters

### Workflow
OverrideRequested → Applied → Compensated

### Search Requirements
Filter overrides by site/type/date

### Documents
None

### Reports
Override tally in admin MIS optional

### Notifications
Notify employee on material override

### Security
- Restricted roles
- Immutable audit

### Integrations
May revoke credentials via Module 05

### Dependencies
- F03-002
- F03-004
- F05-001

### Assumptions
- Refund automation not included unless added

### Risks
- Abuse of override without governance

### Non Functional Requirements
- Override transactional with booking

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Booking override dialog | Complex | 12 |
| UI | Override impact confirmation | Easy | 4 |
| UI | Override register | Medium | 6 |
| API | Apply booking override | Very High | 16 |
| API | List booking overrides | Medium | 6 |
| API | Get override detail | Easy | 4 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Very High | 12 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 67 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Refund automation not included unless added / Abuse of override without governance.
