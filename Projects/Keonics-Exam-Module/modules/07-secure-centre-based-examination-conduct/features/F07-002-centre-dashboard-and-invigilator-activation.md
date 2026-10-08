# F07-002 — Centre Dashboard and Invigilator Activation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | Centre Dashboard and Invigilator Activation |
| **Module** | 07 — Secure Centre-Based Examination Conduct |

### Description
Provide a centre-scoped operational dashboard for today’s and upcoming examinations with live candidate counts (present/absent, started/completed, active/submitted), plus invigilator workflows to verify attendance, validate identity against hall ticket/registration, and activate eligible candidate sessions so CBT can begin only after human activation.

### Business Objective
Give centre staff real-time control of exam-day seating and ensure no candidate starts without invigilator verification and session activation.

### Actors
- Invigilator / Centre user (primary maker of attendance and activation)
- Centre supervisor (if mapped; same centre scope)
- Examination Administrator (read-only cross-centre monitoring; does not activate remote centres)
- Auditor (activation and attendance history)

### User Journey
1. Who creates: Invigilators create attendance marks and session activation records for candidates allotted to their centre; the dashboard aggregates live status from those actions and from examination conduct events.
2. How they create: Open centre dashboard → select today’s examination/session → open candidate roster → verify identity → mark present/absent → activate eligible present candidates (individually or approved batch) → monitor started/completed tiles.
3. How they edit: Correct attendance before activation where policy allows; revoke activation only before first successful exam login if Department rules permit; after start, status is driven by conduct features (F07-003–F07-005).
4. How they send for approval: Session activation is an invigilator operational action, not a multi-level approval package. No maker–checker inbox unless Department later mandates dual control (out of current SOW).
5. How the approver sees pending items: There is no Department approver inbox for activation. Administrators may view centre dashboards in read-only mode for oversight.
6. How the approver decides: No approval decision on this feature; invigilator decides present/absent and activate/not activate within centre scope.
7. How the applicant / maker sees history: Invigilators see activation and attendance history for their centre’s sessions, including who activated whom and when.
8. How the approver / auditor sees history: Administrators and auditors search activation/attendance history by centre, examination, session and invigilator with full attribution.

### Functional Capabilities
- Centre-scoped dashboard: today’s and upcoming exams; candidate counts; present/absent; started/completed; active/submitted; status tiles
- Invigilator schedule and candidate list for the mapped centre only
- Identity verification against hall ticket / registration details before activation
- Attendance marking (present/absent) with timestamp and actor
- Activate eligible sessions only for present, allotted, not-completed candidates within schedule window
- Live monitoring of activation vs started vs submitted counts
- Centre day operational snapshot / centre report view (centre-scoped)
- Prevent activation for wrong centre, inactive session, or candidates failing eligibility
- Batch activation of eligible present candidates where finally approved
- Drill from dashboard tiles into filtered candidate lists

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Centre operational dashboard | Very High |
| Today’s session board | Complex |
| Candidate roster and identity verification | Complex |
| Attendance marking screen | Medium |
| Session activation console | Complex |
| Live centre status monitor | Very High |
| Centre day operational report view | Medium |
| Activation history for centre | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Load centre dashboard aggregates | Very High |
| List today’s and upcoming centre sessions | Medium |
| Search and filter centre candidates | Medium |
| Verify candidate identity for seating | Complex |
| Mark attendance present or absent | Complex |
| Activate eligible candidate session | Complex |
| Revoke pre-start activation | Medium |
| Monitor live status counts | Complex |
| Load centre day snapshot | Medium |
| Search activation history | Medium |

### Inputs
Centre identity (from staff mapping), examination/session selection, candidate registration/hall-ticket identifiers, attendance mark, activation confirmation, filters (status, session, time).

### Outputs
Dashboard aggregates, attendance records, activation records, live status counts, centre day snapshot, activation history.

### Business Rules
- Centre users see only their centre’s candidates and sessions.
- Examination cannot start without invigilator activation for that candidate/session (consumed by F07-001/F07-003).
- Only present, allotted, eligible, not-completed candidates within the schedule window may be activated.
- Absent candidates cannot be activated.
- Administrators do not perform remote activation for a centre unless explicitly granted the same centre mapping.
- Counts on the dashboard must reconcile to underlying attendance, activation and conduct records for the selected day/session.

### Validations
- Invigilator centre scope enforced on every list and action
- Activation blocked if gate prerequisites fail
- Attendance required before activation when policy mandates present mark
- Dual activation of the same candidate/session rejected

### Calculations
Aggregate counts: registered/allotted, present, absent, activated, started, active, submitted, completed for selected centre/session/day.

### Workflow
Roster → verify → mark attendance → activate → monitor. No Department approval step.

### Search Requirements
Candidates by name/registration/hall-ticket number within centre; sessions by date; activation history by invigilator and time range.

### Documents
Hall ticket details shown for verification; no new document generation.

### Reports
Centre day operational report view; feeds Module 09 examination reports with centre-scoped facts.

### Notifications
Optional staff alerts on session start windows owned by F09-003.

### Security
Strict centre scope; activation actions attributable to invigilator user; read-only admin oversight without cross-centre write.

### Integrations
None.

### Dependencies
Modules 01, 03, 05; F07-001 (gate consumes activation); F07-003–F07-005 (status tiles); F07-006 (audit of activation).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Dashboard is Very High effort due to live multi-tile operational UI and concurrent exam-day updates.
- Physical biometric devices are out of software scope unless Department later adds them.

### Risks
Invigilators activating without proper identity checks creates integrity exposure.
Network lag can make live counts briefly diverge from true session state.

### Non Functional Requirements
Dashboard remains usable under peak concurrent centre load; status refresh supports exam-day operations without full page reload dependency.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Centre operational dashboard | UI | Very High | 16 |
| Today’s session board | UI | Complex | 12 |
| Candidate roster and identity verification | UI | Complex | 12 |
| Attendance marking screen | UI | Medium | 6 |
| Session activation console | UI | Complex | 12 |
| Live centre status monitor | UI | Very High | 16 |
| Centre day operational report view | UI | Medium | 6 |
| Activation history for centre | UI | Easy | 4 |
| Load centre dashboard aggregates | API | Very High | 16 |
| List today’s and upcoming centre sessions | API | Medium | 6 |
| Search and filter centre candidates | API | Medium | 6 |
| Verify candidate identity for seating | API | Complex | 8 |
| Mark attendance present or absent | API | Complex | 8 |
| Activate eligible candidate session | API | Complex | 8 |
| Revoke pre-start activation | API | Medium | 6 |
| Monitor live status counts | API | Complex | 8 |
| Load centre day snapshot | API | Medium | 6 |
| Search activation history | API | Medium | 6 |
| Attendance and activation entities | DB | Complex | 6 |
| Centre dashboard and invigilator activation tests | Testing | Very High | 12 |
| Centre dashboard and invigilator activation implementation documentation | Documentation | Complex | 4 |

**Feature total: 184 hours**
