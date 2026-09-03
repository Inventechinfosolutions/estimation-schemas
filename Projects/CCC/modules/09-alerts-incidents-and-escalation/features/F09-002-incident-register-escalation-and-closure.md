# F09-002 — Incident Register, Escalation and Closure

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Incident Register, Escalation and Closure |
| **Module** | 09 — Alerts, Incidents and Escalation |

### Description
Operators raise or auto-create incidents from alerts; track escalation, assignment, remarks and closure with audit trail.

### Business Objective
Timely response to operational incidents across the State.

### Actors
Applicant: CCC/District Operator. Approver: Supervisor / Vigilance Post. Other: assignee.

### User Journey
1. Who creates: Operator or system from alert.
2. How they create: Incident → New: type, vehicle/godown, description, link alert/CCTV, Save draft.
3. How they edit: Draft/Returned editable; after submit, status updates with remarks.
4. How they send for approval: Submit / escalate to Supervisor.
5. How the approver sees pending items: Incident inbox by severity and district.
6. How the approver decides: Assign, escalate, close or return.
7. How the applicant sees history: My incidents timeline.
8. How the approver sees history: Team/state incident history.

### Functional Capabilities
- Incident create
- Escalation
- Assignment
- Closure
- Audit trail

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Incident register | Complex |
| Incident form | Complex |
| Incident inbox | Complex |
| Incident decision / escalation panel | Complex |
| Incident timeline history | Medium |
| Team incident history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create incident | Complex |
| Submit/escalate incident | Complex |
| Assign incident | Medium |
| Close incident | Complex |
| Query inbox | Medium |
| Read timeline | Medium |

### Inputs
Type, severity, location/vehicle, status, remarks.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Closed incidents not silently edited.

### Validations
- Type and severity mandatory.

### Calculations
Ageing for SLA display.

### Workflow
Open → In Progress → Escalated → Closed.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
Optional evidence attachment (embedded).

### Reports
Incident reports (Module 11).

### Notifications
On assign/escalate/close.

### Security
Unit-scoped with Vigilance override.

### Integrations
Links to GPS/CCTV/RFID/ANPR events.

### Dependencies
F09-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- GPS/CCTV/RFID/ANPR field hardware supply and install are out of application-software hours unless stated otherwise.
- Hosting is on KSDC; KSDC consumption INR and AMC/O&M person-months are out of this estimate per confirmed scope.

### Risks
Incomplete vendor API documentation for VLTS, CCTV, SMART-PDS, Vahan or Sarathi would delay integration features.

### Non Functional Requirements
Screens remain usable under concurrent State CCC load; privileged actions are attributable to Person + Post.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Incident register | UI | Complex | 12 |
| Incident form | UI | Complex | 12 |
| Incident inbox | UI | Complex | 12 |
| Incident decision / escalation panel | UI | Complex | 12 |
| Incident timeline history | UI | Medium | 6 |
| Team incident history | UI | Medium | 6 |
| Create incident | API | Complex | 8 |
| Submit/escalate incident | API | Complex | 8 |
| Assign incident | API | Medium | 6 |
| Close incident | API | Complex | 8 |
| Query inbox | API | Medium | 6 |
| Read timeline | API | Medium | 6 |
| Incident and status history | DB | Complex | 6 |
| Incident Register, Escalation and Closure feature tests | Testing | Very High | 12 |
| Incident Register, Escalation and Closure implementation documentation | Documentation | Medium | 3 |

**Feature total: 123 hours**
