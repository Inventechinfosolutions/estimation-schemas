# F11-001 — Operational and Compliance Reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-001 |
| **Feature Name** | Operational and Compliance Reports |
| **Module** | 11 — Reports, MIS and Analytics |

### Description
Users run vehicle movement, route compliance, RFID/ANPR, CCTV activity, alert/incident, district performance and load monitoring reports with export.

### Business Objective
Governance and decision-support reporting.

### Actors
User: District/State MIS Posts. Auditor: same scoped.

### User Journey
1. Who creates: MIS user runs a report.
2. How they create: Reports → select report, filters (district/period/contractor), Run, Export PDF/Excel.
3. How they edit: Filters re-run. Optional save snapshot.
4. How they send for approval: Snapshot publish to MIS Checker if used; else no approval.
5. How the approver sees pending items: Checker snapshot inbox only if publish used.
6. How the approver decides: Approve snapshot or user just exports.
7. How the user sees history: Recent runs.
8. How the approver sees history: Published snapshots.

### Functional Capabilities
- Standard report catalogue
- Filters
- PDF/Excel export

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Report catalogue | Medium |
| Report runner | Complex |
| Export dialog | Simple |
| Saved snapshot register | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Run operational report | Complex |
| Run compliance report | Complex |
| Export PDF/Excel | Easy |
| Save snapshot | Medium |

### Inputs
Report type, district, period, contractor.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Scope by Post.

### Validations
- Date range required.

### Calculations
Per report KPIs.

### Workflow
Optional snapshot publish.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
Exported file.

### Reports
This feature.

### Notifications
None.

### Security
Role-scoped reports.

### Integrations
None.

### Dependencies
Operational modules.

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
| Report catalogue | UI | Medium | 6 |
| Report runner | UI | Complex | 12 |
| Export dialog | UI | Simple | 2 |
| Saved snapshot register | UI | Medium | 6 |
| Run operational report | API | Complex | 8 |
| Run compliance report | API | Complex | 8 |
| Export PDF/Excel | API | Easy | 4 |
| Save snapshot | API | Medium | 6 |
| Report run metadata | DB | Medium | 4 |
| Operational and Compliance Reports feature tests | Testing | Very High | 12 |
| Operational and Compliance Reports implementation documentation | Documentation | Medium | 3 |

**Feature total: 71 hours**
