# F04-001 — Payment Checkout Initiation

| Field | Value |
|-------|-------|
| Feature ID | F04-001 |
| Feature Name | Payment Checkout Initiation |
| Module | 04 — Online Payment Processing |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Starts online payment for a pending booking via payment gateway supporting UPI, net banking, and cards.

### Business Objective
Collect payment through approved digital methods before confirmation.

### Actors
- Employee Guest

### User Journey
1. Employee initiates payment from booking summary.
2. System creates payment order and redirects/invokes gateway checkout.
3. Employee cannot edit amount; may cancel and return if gateway allows.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Employee sees payment attempts on booking payment panel.
8. Admin/auditor sees payment initiation log.

### Functional Capabilities
- Create payment order
- Launch gateway checkout
- Show supported methods messaging
- Record initiation

### UI Screens
- Payment checkout launch screen
- Redirect/waiting for gateway screen
- Payment methods info panel

### Logical API Operations
- Create payment order
- Get payment order status

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Amount equals booking summary
- Only Pending Payment bookings
- Idempotent order creation

### Validations
- Booking hold still valid

### Calculations
- None beyond display counters

### Workflow
SummaryAccepted → PaymentOrderCreated → AwaitingGateway

### Search Requirements
Admin search payments by booking ref

### Documents
None

### Reports
None

### Notifications
None at initiation

### Security
- Server-side amount authority
- No client-trusted price

### Integrations
Uses F08-001 adapter

### Dependencies
- F03-003
- F08-001

### Assumptions
- Gateway merchant account ready

### Risks
- User drop-off on gateway

### Non Functional Requirements
- Order creation fast

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Payment checkout launch screen | Medium | 6 |
| UI | Redirect/waiting for gateway screen | Easy | 4 |
| UI | Payment methods info panel | Simple | 2 |
| API | Create payment order | Complex | 8 |
| API | Get payment order status | Medium | 6 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 41 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Gateway merchant account ready / User drop-off on gateway.
