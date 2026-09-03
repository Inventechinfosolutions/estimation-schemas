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
1. Who creates: Administrator
2. How they create: Administrator or auditor generates Role-to-Post and Post-to-Person mapping reports.
3. How they edit: Report includes current and history: who was mapped, effective dates, who changed the mapping.
4. How they send for approval: The report is used for access audit, not for granting access (granting remains F01-002). Filter → generate → export. No mapping change from this screen.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Role-to-Post mapping report.
- Post-to-Person current and history report.
- Show who changed the mapping and effective dates.
- Read-only audit use.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Mapping report parameters | Medium |
| Current and history mapping report | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Mapping report operations | Medium |
| Update role / post mapping reports | Medium |
| Search role / post mapping reports | Medium |
| Read role / post mapping reports history | Easy |

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
| Update role / post mapping reports | API | Medium | 6 |
| Search role / post mapping reports | API | Medium | 6 |
| Read role / post mapping reports history | API | Easy | 4 |
| Mapping report query support | DB | Medium | 4 |
| Role / Post mapping reports feature tests | Testing | Medium | 6 |
| Role / Post mapping reports implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
