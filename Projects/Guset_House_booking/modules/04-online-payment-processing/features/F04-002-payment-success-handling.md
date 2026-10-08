# F04-002 — Payment Success Handling

| Field | Value |
|-------|-------|
| Feature ID | F04-002 |
| Feature Name | Payment Success Handling |
| Module | 04 — Online Payment Processing |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Processes successful payment callbacks/status and advances booking to paid state triggering allocation.

### Business Objective
Confirm funds success before room allocation and confirmation.

### Actors
- System
- Employee Guest

### User Journey
1. Gateway/system records success against payment order.
2. System marks booking Paid and triggers allocation.
3. No employee edit of success records.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Employee sees Paid status and proceeds to confirmation.
8. Auditor sees payment success trail and correlation ids.

### Functional Capabilities
- Accept success callback
- Verify signature/status with gateway
- Mark booking paid
- Trigger allocation handoff
- Show success receipt

### UI Screens
- Payment success receipt screen

### Logical API Operations
- Handle payment success callback
- Verify payment with gateway
- Mark booking paid

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Trust verified gateway status only
- Idempotent success handling
- Paid booking cannot be unpaid by employee

### Validations
- Callback correlation matches order
- Amount match

### Calculations
- None beyond display counters

### Workflow
AwaitingGateway → Paid → AllocationTriggered

### Search Requirements
Reconcile by gateway reference

### Documents
Payment receipt

### Reports
Feeds revenue reports

### Notifications
Optional payment success notify

### Security
- Verify callbacks
- No sensitive card data stored

### Integrations
F08-001

### Dependencies
- F04-001
- F03-004

### Assumptions
- Gateway provides reliable webhook + status API

### Risks
- Duplicate callbacks

### Non Functional Requirements
- Idempotent processing

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Payment success receipt screen | Easy | 4 |
| API | Handle payment success callback | Very High | 16 |
| API | Verify payment with gateway | Complex | 8 |
| API | Mark booking paid | Complex | 8 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Very High | 12 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 55 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Gateway provides reliable webhook + status API / Duplicate callbacks.
