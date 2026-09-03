# F01-006 — Access Audit Log

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-006 |
| **Feature Name** | Access Audit Log |
| **Module** | 01 — Person, Post, Role and Access Governance |

### Description
Auditor searches who did what, when, from which Post on CCC modules.

### Business Objective
Tamper-evident access evidence for CCC operations.

### Actors
Auditor searches logs. Access Administrator may export.

### User Journey
1. Who creates: System writes log on privileged actions; Auditor opens search.
2. How they create: Opens Access log search by Person, Post, unit, period, action.
3. How they edit: Logs are not edited.
4. How they send for approval: Not applicable — search/export only.
5. How the approver sees pending items: No approver inbox.
6. How the approver decides: Not applicable.
7. How the user sees history: Administrator sees own export history.
8. How the auditor sees history: Full access log search results.

### Functional Capabilities
- Search access log
- Export retained log

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Access log search | Complex |
| Access log export | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search access log | Complex |
| Export access log | Medium |

### Inputs
Filters: Person, Post, unit, period, action.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Logs are append-only.

### Validations
- Period required for export.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
Optional export file.

### Reports
Access log export.

### Notifications
None.

### Security
Auditor/administrator Posts only.

### Integrations
None.

### Dependencies
Module 01 sessions.

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
| Access log search | UI | Complex | 12 |
| Access log export | UI | Medium | 6 |
| Search access log | API | Complex | 8 |
| Export access log | API | Medium | 6 |
| Immutable access log store | DB | Complex | 6 |
| Access Audit Log feature tests | Testing | Complex | 8 |
| Access Audit Log implementation documentation | Documentation | Medium | 3 |

**Feature total: 49 hours**
