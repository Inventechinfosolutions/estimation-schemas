# F04-007 — Matter reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-007 |
| **Feature Name** | Matter reports |
| **Module** | 04 — Matter Management |

### Description
An authorised user selects a report type (case, court, team member, CA, FE, key date or stage), sets filters, and generates the report from matter records.

### Business Objective
Produce matter MIS from live matter records: case, court, team member, CA, FE, key date and stage.

### Actors
Authorised Legal Cell; Competent Authority; Administrator (export).

### User Journey
1. Who creates: Authorised Legal Cell
2. How they create: User opens Matter Reports.
3. How they edit: Selects type: case-wise, court-wise, team-member-wise, CA-wise, FE-wise, key-date-wise or stage-wise.
4. How they send for approval: Sets filters and generates the report from matter records. Select type → filter → generate → preview/export.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Authorised Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Authorised Legal Cell opens history on the record. Exports as agreed (Excel/PDF presentation).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Matter Report Type and Filter screen
- Report Preview/Export
- Types: case, court, team member, CA, FE, key date, stage
- Generated from matter records, not a parallel warehouse product
- No Claim settlement or valuation KPIs

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Matter Report Type and Filter screen | Complex |
| Report Preview/Export | Medium |
| Matter reports history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Report generation (case, court, team, CA, FE, key date, stage) | Very High |
| Update matter reports | Medium |
| Search matter reports | Medium |
| Read matter reports history | Easy |

### Inputs
Report type; filters (date, court, CA, FE, Post, stage, key date range).

### Outputs
On-screen report; Excel/PDF export as configured.

### Business Rules
- Listed report types can be produced by an authorised Post.
- Data follows need-to-know: users do not see matters they cannot open.
- FE-wise uses programme FE references.

### Validations
- Type required; date filters coherent; export only if Post allowed.

### Calculations
Counts and grouping by selected dimension; overdue key-date counts where relevant.

### Workflow
Select type → filter → generate → preview/export.

### Search Requirements
N/A (filtered generate).

### Documents
Exported report file.

### Reports
This feature is the reports.

### Notifications
None.

### Security
Row-level by matter visibility; export audited.

### Integrations
Matter data consume (Simple).

### Dependencies
F04-001–F04-006; F01-001.

### Assumptions
- Stage values come from variables/key dates as configured with SPLOCA.

### Risks
Users treat export as complete for matters they cannot see — filters must state scope.

### Non Functional Requirements
Generate within agreed time for typical Legal Cell volumes.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Matter Report Type and Filter screen | UI | Complex | 12 |
| Report Preview/Export | UI | Medium | 6 |
| Matter reports history | UI | Medium | 6 |
| Report generation (case, court, team, CA, FE, key date, stage) | API | Very High | 16 |
| Update matter reports | API | Medium | 6 |
| Search matter reports | API | Medium | 6 |
| Read matter reports history | API | Easy | 4 |
| Matter reports persistence | DB | Medium | 4 |
| Matter data consume | Integration | Simple | 4 |
| Matter reports feature tests | Testing | Complex | 8 |
| Matter reports implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **75** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
