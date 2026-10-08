# F03-003 — Booking Summary and Pricing Preview

| Field | Value |
|-------|-------|
| Feature ID | F03-003 |
| Feature Name | Booking Summary and Pricing Preview |
| Module | 03 — Booking & Room Allocation |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Presents a booking summary including pricing before the employee proceeds to payment.

### Business Objective
Give transparent cost and stay details prior to payment commitment.

### Actors
- Employee Guest

### User Journey
1. System creates summary view when employee proceeds from booking request.
2. Employee reviews period, room, site, price breakdown, then continues to payment.
3. Employee cannot edit price; may go back to change booking before payment.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Summary snapshot retained on booking record for later confirmation comparison.
8. Auditor can see priced summary on booking detail.

### Functional Capabilities
- Show stay summary
- Show price breakdown
- Proceed to payment CTA
- Back to edit pending booking

### UI Screens
- Booking summary and pricing screen
- Price breakdown panel

### Logical API Operations
- Get booking pricing summary
- Confirm summary and start payment

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Displayed price must match charge sent to payment
- Summary required before payment initiation

### Validations
- Pending booking must still be valid/hold active

### Calculations
- Nights × rate (+ taxes if configured as simple line)

### Workflow
PendingPayment → SummaryAccepted → PaymentInitiated

### Search Requirements
None

### Documents
None

### Reports
None

### Notifications
None

### Security
- Summary only for booking owner

### Integrations
Hands off to Module 04

### Dependencies
- F03-002
- F02-003

### Assumptions
- Simple tax line optional; complex GST engine out of scope

### Risks
- Price change after summary if admin edits room mid-hold

### Non Functional Requirements
- Summary load fast

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Booking summary and pricing screen | Medium | 6 |
| UI | Price breakdown panel | Easy | 4 |
| API | Get booking pricing summary | Complex | 8 |
| API | Confirm summary and start payment | Medium | 6 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 34 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Simple tax line optional; complex GST engine out of scope / Price change after summary if admin edits room mid-hold.
