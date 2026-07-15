# F07-005 — Concurrent Booking Exclusivity Controls

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-005 |
| **Feature Name** | Concurrent Booking Exclusivity Controls |
| **Module** | 07 — Application First Come Booking |

### Description
Enforce the single-active-booking rule when multiple citizens or officers attempt to progress applications for the same unit at nearly the same time.

### Business Objective
Prevent double allocation and preserve a defensible first-come booking outcome.

### Actors
System; Citizen; Housing/Estate Officer; Auditor.

### User Journey
When a booking-eligible application receives a successful payment signal, the booking action checks the live unit state, permits one winning confirmation, returns a clear unavailable outcome to later attempts, and records the contention event.

### Functional Capabilities
- Live unit-availability recheck at booking confirmation.
- Contention outcome handling, duplicate payment/bookings exception identification, and operational resolution queue.
- Audit evidence showing attempted time, outcome, and resulting active booking.

### Inputs
Booking-eligible application, payment success reference, unit state, event time, and existing booking context.

### Outputs
Single successful booking or controlled unavailable/exception outcome, contention audit, and resolution item where needed.

### Business Rules
At most one active booking exists per unit; availability shown during browsing is indicative and does not reserve the unit; only the confirmed booking transition determines the winner; cancellation/release restores eligibility through owning lifecycle features.

### Validations
Active unit state, matched payment/application, no current booking, idempotent payment event, and valid retry context.

### Calculations
Booking-attempt sequence, contention count, and exception ageing.

### Workflow
Concurrent attempts → authoritative availability check → one confirmed booking; remaining attempts unavailable/exception → officer resolution if payment needs follow-up.

### Search Requirements
Unit, application, booking/payment reference, event time, result, and unresolved exception status.

### Documents
No primary citizen document; contention/export evidence retained for audit.

### Reports
Booking contention, duplicate-payment exception, and exclusivity-control audit report.

### Notifications
Citizen unavailable/refund-follow-up message where applicable and officer exception alert through Module 12.

### Security
No citizen can inspect competing applicant information; privileged exception resolution is role-controlled and fully audited.

### Integrations
Inventory availability/status handoff (Medium) and payment status consumption (Medium).

### Dependencies
F07-004; Modules 04, 08, 12, and 13.

### Assumptions
Baseline is first-come-first-served without lottery, quota, or temporary reservation policy beyond approved booking processing.

### Risks
Peak release traffic and delayed payment events increase contention and reconciliation cases.

### Non Functional Requirements
Safe concurrent handling, deterministic outcomes, idempotent event treatment, and clear user feedback under peak load.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Booking contention and exception resolution UI | UI | Complex | 8 |
| Exclusive booking and idempotency processing | API | Very High | 16 |
| Contention and exception persistence | Database | Complex | 6 |
| Inventory and payment event consumption | Integration | Medium | 16 |
| Concurrent booking tests | Testing | Very High | 12 |
| Exclusivity operations guide | Documentation | Complex | 4 |
| **Total** | | | **62** |

### Estimation Assumptions
This estimate includes enterprise-grade concurrent business processing; gateway connector and infrastructure scaling are outside this feature.
