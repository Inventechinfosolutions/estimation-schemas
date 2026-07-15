# F04-004 — Property Handover & Possession

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F04-004 |
| **Feature Name** | Property Handover & Possession |
| **Module** | 04 — Tenant & Lease Lifecycle |

### Description
Execute property handover with checklist and possession certificate, set possession date, move unit status to Occupied, and enable billing commencement signal to Module 05 (M3-AC2).

### Business Objective
Formally transfer possession and start the operational lease period with audit evidence.

### Actors
- Estate Officer, Property Manager
- Tenant (acknowledgement — optional portal/sign)

### User Journey
1. Officer opens approved/deposit-complete lease → Handover.
2. Completes checklist items; captures possession date; attaches photos if needed.
3. Generates possession certificate.
4. System sets units Occupied; lease becomes Active for billing start.
5. Module 05 can include lease in next bill run.

### Functional Capabilities
- Configurable handover checklist
- Possession date and remarks
- Possession certificate generate/upload
- Unit status transition to Occupied (Module 03)
- Billing commencement flag/date to Module 05
- Reverse/cancel handover only via controlled correction with approval

### Inputs
- Checklist responses, possession date, certificate, photos

### Outputs
- Completed handover record
- Occupied units; billing start signal

### Business Rules
- Handover records possession date and checklist; unit status becomes Occupied (M3-AC2).
- Cannot handover if activation gates incomplete.
- Vacate path is F04-006 (reverse occupancy).

### Validations
- All mandatory checklist items done
- Possession date within policy window vs lease start

### Calculations
None.

### Workflow
Ready for handover → Complete checklist → Confirm → Occupied + billing flag.

### Search Requirements
Handover pending list; by lease/unit/date.

### Documents
Possession certificate, handover photos (Module 08).

### Reports
Handover Register.

### Notifications
Tenant possession confirmation notice (Module 09).

### Security
RBAC; audit; controlled corrections.

### Integrations
Internal status update to Module 03; event to Module 05.

### Dependencies
F04-003, F04-007; Module 03 status; Module 05; Module 08/09

### Assumptions
- Digital tenant countersign optional; baseline officer-attested certificate.

### Risks
- Occupied without billing flag fails revenue start — must be transactional with lease.

### Non Functional Requirements
- Field-friendly checklist on tablet

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Handover checklist & possession UI | UI | Complex | 8 |
| Handover complete / certificate view | UI | Medium | 6 |
| Handover & status transition ops | API | Complex | 8 |
| Handover checklist entities | Database | Medium | 4 |
| Handover tests | Testing | Complex | 8 |
| Handover guide | Documentation | Medium | 3 |
| **Total** | | | **37** |

### Estimation Assumptions
- Billing schedule generation not included (Module 05).
