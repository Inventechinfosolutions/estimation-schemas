# F07-004 — First-Come Booking Confirmation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-004 |
| **Feature Name** | First-Come Booking Confirmation |
| **Module** | 07 — Application First Come Booking |

### Description
Create the confirmed first-come booking after an approved application has a successful booking-amount payment, reserve the unit, and establish the booking due date and status.

### Business Objective
Convert one qualified paid application into one authoritative unit booking.

### Actors
Citizen; Housing/Estate Officer; Accounts Officer; Auditor.

### User Journey
After approval and a successful booking payment signal, the system evaluates the active unit state, creates the booking, marks the unit Booked, calculates the balance due date, publishes confirmation, and prevents a second current booking.

### Functional Capabilities
- Payment-qualified booking queue and booking detail/register.
- Booking number, booking date, amount, balance due date, status, and linked application/unit context.
- Controlled exception view for payment received but booking not confirmed.

### Inputs
Approved application, successful booking-payment status, unit availability, configured balance due period, and confirmation context.

### Outputs
Booking reference, reserved unit status, due date, booking history, and confirmation event.

### Business Rules
Booking is confirmed only after successful online booking payment; one active booking per unit; failed/pending payment never confirms booking; balance due period defaults to 90 days but is configurable.

### Validations
Approved application, matching successful payment, current available unit, valid configured due period, and no existing current booking.

### Calculations
Balance outstanding and balance-payment due date from booking date plus configured period.

### Workflow
Approved application + successful payment → booking confirmed → unit Booked → balance payment pending → later lifecycle event.

### Search Requirements
Booking number, application, citizen, project, unit, booking date, due date, payment status, and booking status.

### Documents
Booking confirmation and linked payment receipt.

### Reports
Booking register, payment-qualified exceptions, and balance-due register.

### Notifications
Booking confirmation, balance due date, and exception alerts through Module 12.

### Security
Authorised officer exception access, citizen-only own confirmation, immutable payment-to-booking linkage, and full status audit.

### Integrations
Payment status consumption from Module 08/13 (Medium); inventory status reflection (Medium); notification handoff (Easy).

### Dependencies
F07-003, F07-005, F07-006, Modules 04, 08, 12, and 13.

### Assumptions
Payment gateway callback/connector implementation is in Module 13; this feature consumes a settled business payment status.

### Risks
Late or duplicate payment notifications can create booking exceptions requiring controlled resolution.

### Non Functional Requirements
Atomic booking confirmation, immediate status visibility, and recoverable exception handling.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Booking confirmation and exception worklists | UI | Complex | 8 |
| Booking detail and balance-due screens | UI | Complex | 8 |
| Payment-gated booking transaction processing | API | Very High | 16 |
| Booking, due-date, and status persistence | Database | Complex | 6 |
| Payment hub and inventory status handoffs | Integration | Medium | 16 |
| Booking integrity tests | Testing | Very High | 12 |
| Booking operations guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
The external payment connector is excluded; hours cover payment-status consumption and the booking domain transition.
