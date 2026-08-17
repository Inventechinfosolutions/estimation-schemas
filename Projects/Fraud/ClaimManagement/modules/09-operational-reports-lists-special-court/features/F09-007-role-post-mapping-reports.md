# F09-007 — Role / Post mapping reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-007 |
| **Feature Name** | Role / Post mapping reports |
| **Module** | 09 — Operational Reports, Lists & Special Court Outputs |

### Description
An Administrator or auditor generates Role-to-Post and Post-to-Person mapping reports (current and history: who was mapped, effective dates, who changed the mapping). The report is used for access audit, not for granting access.

### Business Objective
Report current and historical Person–Post–Role mappings for access audit without using the report to grant access.

### Actors
Administrator; auditor.

### User Journey
1. Administrator or auditor generates Role-to-Post and Post-to-Person mapping reports.
2. Report includes current and history: who was mapped, effective dates, who changed the mapping.
3. The report is used for access audit, not for granting access (granting remains F01-002).

### Functional Capabilities
- Role-to-Post mapping report.
- Post-to-Person current and history report.
- Show who changed the mapping and effective dates.
- Read-only audit use.

### Inputs
As-of date, Post, Person, Role filters.

### Outputs
Mapping reports (current and history).

### Business Rules
- The report does not grant or change access.
- History comes from F01-002 mapping history.
- This Module 01 mapping is the shared IAM for Legal and Valuation; the report covers that catalogue.

### Validations
- Only Administrator/auditor Posts generate these reports.

### Calculations
None beyond as-of occupancy.

### Workflow
Filter → generate → export. No mapping change from this screen.

### Search Requirements
Person, Post, Role, effective dates, changed-by.

### Documents
None.

### Reports
Role/Post mapping reports.

### Notifications
None.

### Security
Auditor/Administrator only. Generating the report is audited. Does not display passwords.

### Integrations
None (reads Module 01 mapping store).

### Dependencies
F01-002, F01-010.

### Assumptions
- Legal and Valuation do not maintain a second mapping report source.

### Risks
- Using export as an informal access-grant list would bypass F01-002 controls.

### Non Functional Requirements
Mapping history retrievable for access audit.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Mapping report parameters | UI | Medium | 6 |
| Current and history mapping report | UI | Complex | 12 |
| Mapping report operations | API | Medium | 6 |
| Mapping report query support | DB | Medium | 4 |
| Mapping report tests | Testing | Medium | 6 |
| Mapping report note | Documentation | Easy | 2 |
| **Total** | | | **36** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Mapping administration UI is estimated in F01-002; this feature is the audit report.
