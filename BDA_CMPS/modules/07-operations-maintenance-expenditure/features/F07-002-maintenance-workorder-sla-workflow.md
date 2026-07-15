# F07-002 — Maintenance Work Order & SLA Workflow

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F07-002 |
| **Feature Name** | Maintenance Work Order & SLA Workflow |
| **Module** | 07 — Operations, Maintenance & Expenditure |

### Description
Execute complaint workflow: assign engineer/agency → inspection → work order → completion → verification → closure, with SLA timers/escalation and attachments; enforce verification before close when configured (M6-AC2).

### Business Objective
Ensure maintenance work is completed, verified, and measured against SLAs with full audit trail.

### Actors
- Maintenance Officer, Assigned engineer/agency user, Chief Engineer (escalations), Verifier

### User Journey
1. Officer assigns complaint to engineer/vendor.
2. Site inspection notes captured.
3. Work order created with estimate; execution updates.
4. Completion recorded; verification performed.
5. Closure allowed only after verification when configured (M6-AC2).
6. Optional link to expenditure/vendor payment (F07-005/006).

### Functional Capabilities
- Stages: Assign → Inspect → Work Order → Complete → Verify → Close
- SLA timers and escalation (configurable)
- Photo/document at each stage
- Link vendor and cost estimate
- Work queue by assignee/status/SLA breach
- Cannot close without verification when configured

### Inputs
- Assignee, inspection notes, WO details, estimates, completion evidence, verification outcome

### Outputs
- Work order record; stage history; SLA status

### Business Rules
- Work order cannot close without verification when configured (M6-AC2).
- Escalation notifies supervisors via Module 09 when SLA breached.
- Reopen path for failed verification.

### Validations
- Stage-gate mandatory fields; assignee active
- Verification role ≠ completer when SoD configured

### Calculations
- SLA due timestamps; breach flags; optional time-to-close metrics

### Workflow
Complaint → Assign Engineer → Inspection → Work Order → Completion → Verification → Closure.

### Search Requirements
WO by number, complaint, vendor, SLA status, property.

### Documents
Stage attachments (Module 08); completion certificate refs (F07-004).

### Reports
Work Order Report; SLA breach report.

### Notifications
Assignment, escalation, verification requests (Module 09).

### Security
RBAC; stage permissions; audit all transitions.

### Integrations
Notification Service (Simple).

### Dependencies
F07-001; F07-004 vendors; F02-009 optional approvals; Modules 08–09

### Assumptions
- Workflow UI = Very High; engine API = Very High.
- Not a separate BPM product—embedded workflow per schema.

### Risks
- Over-complex real-world handoffs — keep stages configurable but finite.

### Non Functional Requirements
- Field-friendly responsive screens; SLA job reliable

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Assignment & work queue UI | UI | Complex | 8 |
| Work order create/update/close UI | UI | Very High | 16 |
| Verification/closure screens | UI | Medium | 6 |
| Maintenance workflow + SLA ops | API | Very High | 16 |
| Work order & SLA entities | Database | Complex | 6 |
| Notification/escalation handoff | Integration | Simple | 4 |
| Maintenance workflow tests | Testing | Very High | 12 |
| Maintenance workflow guide | Documentation | Complex | 4 |
| **Total** | | | **72** |

### Estimation Assumptions
- Native apps excluded; responsive web included.
