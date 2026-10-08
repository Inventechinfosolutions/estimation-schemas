# F03-004 — Automatic Room Allocation

| Field | Value |
|-------|-------|
| Feature ID | F03-004 |
| Feature Name | Automatic Room Allocation |
| Module | 03 — Booking & Room Allocation |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Upon successful payment, the system automatically allocates the room(s) to the booking.

### Business Objective
Remove manual allocation for standard bookings after payment success.

### Actors
- System
- Employee Guest
- Site Administrator

### User Journey
1. System creates allocation when payment success event is received.
2. Allocation binds room to booking dates; employee sees allocated room on confirmation.
3. Re-allocation only via admin override (Module 06), not self-service edit.
4. Approval does not apply — automatic on payment success.
5. No approver inbox for standard allocation.
6. No approver decision for standard allocation.
7. Employee sees allocation on booking detail; admin sees allocation log.
8. Auditor sees allocation timestamps and room ids.

### Functional Capabilities
- Allocate room on payment success
- Fail safe if room lost to race (compensate)
- Expose allocation on booking
- Record allocation audit

### UI Screens
- Allocation status on booking detail
- Allocation failure support message

### Logical API Operations
- Allocate room for paid booking
- Get allocation for booking

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Allocation only after payment success
- Allocated room must remain conflict-free
- Compensation path if allocation fails post-payment

### Validations
- Booking must be Paid/Eligible

### Calculations
- None beyond display counters

### Workflow
Paid → Allocated | AllocationFailed (ops handling)

### Search Requirements
Admin filter allocation failures

### Documents
None

### Reports
None

### Notifications
Notify ops on allocation failure

### Security
- System-triggered; admin read

### Integrations
Triggered by Module 04 success

### Dependencies
- F04-002
- F03-002

### Assumptions
- Usually allocates the reserved room; auto-alternate room only if policy enabled

### Risks
- Payment success with allocation failure needs finance ops playbook

### Non Functional Requirements
- Allocation completes quickly after payment callback

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Allocation status on booking detail | Easy | 4 |
| UI | Allocation failure support message | Simple | 2 |
| API | Allocate room for paid booking | Very High | 16 |
| API | Get allocation for booking | Easy | 4 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Very High | 12 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 45 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Usually allocates the reserved room; auto-alternate room only if policy enabled / Payment success with allocation failure needs finance ops playbook.
