# F04-004 — Unit Status Lifecycle

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-004 |
| **Feature Name** | Unit Status Lifecycle |
| **Module** | 04 — Flats & Villas Inventory & Status |

### Description
Control and display event-driven unit status from draft through availability, booking, payment, allotment, registration, possession, cancellation, refund, and return to available.

### Business Objective
Make inventory availability accurate and prevent operationally invalid state changes.

### Actors
Engineering Section; Housing officers; Accounts; Registration; Possession; Auditor.

### User Journey
Authorised users view a unit timeline; related business events update status automatically, while permitted manual status actions are validated and audited.

### Functional Capabilities
Status dashboard/register; lifecycle timeline; permitted transitions; current availability; event source display; exception handling.

### Inputs
Unit, current status, triggering business event, remarks, authorised manual action where allowed.

### Outputs
Current unit status, status history, availability result.

### Business Rules
Status reflects latest completed valid business event; booked units are unavailable to others; approved cancellation/auto-cancel returns unit to available; direct overrides are controlled.

### Validations
Valid transition only; source event prerequisites; reason required for authorised override.

### Calculations
None.

### Workflow
Unit created → approval/availability → booking/payment/allotment/registration/possession or cancellation/refund → status update and history.

### Search Requirements
Project, unit, current/historical status, event source, date range.

### Documents
Related documents remain embedded in the owning unit/transaction record.

### Reports
Unit Status Register and Lifecycle History export.

### Notifications
Status-change notifications are initiated by owning business processes.

### Security
RBAC, SoD for sensitive overrides, immutable status audit.

### Integrations
Internal handoffs with booking, payment, allotment and cancellation processes (Medium).

### Dependencies
F04-001; Modules 07–10; F02-004.

### Assumptions
This feature owns inventory state control; transaction processing remains in owning modules.

### Risks
Incorrect event sequencing can show erroneous availability.

### Non Functional Requirements
Safe concurrent updates; chronological history; low-latency availability checks.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Unit status register + filters | UI | Complex | 8 |
| Unit lifecycle timeline and controlled transition view | UI | Very High | 16 |
| Status transition operations | API | Very High | 16 |
| Status history and transition persistence | Database | Complex | 6 |
| Business-process status handoffs | Integration | Medium | 16 |
| Lifecycle tests | Testing | Very High | 12 |
| Status lifecycle guide | Documentation | Complex | 4 |
| **Total** | | | **78** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
