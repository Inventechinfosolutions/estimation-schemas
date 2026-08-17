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
1. User opens Matter Reports.
2. Selects type: case-wise, court-wise, team-member-wise, CA-wise, FE-wise, key-date-wise or stage-wise.
3. Sets filters and generates the report from matter records.
4. Exports as agreed (Excel/PDF presentation).

### Functional Capabilities
- Matter Report Type and Filter screen
- Report Preview/Export
- Types: case, court, team member, CA, FE, key date, stage
- Generated from matter records, not a parallel warehouse product
- No Claim settlement or valuation KPIs

### Inputs
Report type; filters (date, court, CA, FE, Post, stage, key date range).

### Outputs
On-screen report; Excel/PDF export as configured.

### Business Rules
- Listed report types can be produced by an authorised Post.
- Data follows need-to-know: users do not see matters they cannot open.
- FE-wise uses programme FE references.

### Validations
Type required; date filters coherent; export only if Post allowed.

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
Stage values come from variables/key dates as configured with SPLOCA.

### Risks
Users treat export as complete for matters they cannot see — filters must state scope.

### Non Functional Requirements
Generate within agreed time for typical Legal Cell volumes.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Matter Report Type and Filter screen | UI | Complex | 12 |
| Report Preview/Export | UI | Medium | 6 |
| Report generation (case, court, team, CA, FE, key date, stage) | API | Very High | 16 |
| Report query support | Database | Complex | 6 |
| Matter data consume | Integration | Simple | 4 |
| Matter report tests | Testing | Complex | 8 |
| Matter reports guide | Documentation | Medium | 3 |
| **Total** | | | **55** |

### Estimation Assumptions
- Does not include a separate BI platform.
