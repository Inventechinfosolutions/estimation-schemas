# F04-003 — Payment Failure Retry and Status

| Field | Value |
|-------|-------|
| Feature ID | F04-003 |
| Feature Name | Payment Failure Retry and Status |
| Module | 04 — Online Payment Processing |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Records payment failures, exposes status, and allows retries within policy without confirming the booking.

### Business Objective
Recover recoverable payment failures without incorrect allocations.

### Actors
- Employee Guest
- Platform Administrator

### User Journey
1. System records failure from gateway or timeout.
2. Employee views failure reason class and retries payment if hold valid.
3. Employee cannot force success; admin may inspect status for support.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Employee sees payment attempt history on booking.
8. Admin/auditor sees failure codes and retry counts.

### Functional Capabilities
- Record failure
- Show status
- Retry payment
- Expire hold on timeout
- Admin payment status view

### UI Screens
- Payment failed screen
- Retry payment confirmation
- Booking payment attempt history
- Admin payment status panel

### Logical API Operations
- Handle payment failure callback
- Retry payment for booking
- List payment attempts
- Admin get payment status

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Failure does not allocate/confirm
- Retry creates new attempt linked to booking
- Max retries/hold expiry enforced

### Validations
- Retry only if booking still pending and hold valid

### Calculations
- Retries remaining

### Workflow
AwaitingGateway → Failed → RetryAllowed → PaymentOrderCreated | HoldExpired

### Search Requirements
Admin filter failed payments

### Documents
None

### Reports
Failure counts feed ops dashboard

### Notifications
Optional failure notify

### Security
- Do not expose raw gateway secrets in UI

### Integrations
F08-001

### Dependencies
- F04-001

### Assumptions
- User-friendly mapped failure reasons

### Risks
- User retries after room hold expired

### Non Functional Requirements
- Clear status within gateway poll window

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Payment failed screen | Easy | 4 |
| UI | Retry payment confirmation | Simple | 2 |
| UI | Booking payment attempt history | Medium | 6 |
| UI | Admin payment status panel | Medium | 6 |
| API | Handle payment failure callback | Complex | 8 |
| API | Retry payment for booking | Complex | 8 |
| API | List payment attempts | Medium | 6 |
| API | Admin get payment status | Easy | 4 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 56 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: User-friendly mapped failure reasons / User retries after room hold expired.
