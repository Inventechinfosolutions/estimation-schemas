# F09-002 — Operational and Statutory Reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Operational and Statutory Reports |
| **Module** | 09 — Dashboards, Reports, Notifications and Audit |

### Description
Deliver the candidate, fee, examination and certificate report families required for operations and statutory needs, with parameterised builders and approved Excel/PDF exports, plus an export download history for administrators.

### Business Objective
Produce repeatable, exportable reports that administrators can submit for operational control and Departmental statutory use without manual data stitching.

### Actors
- Examination Administrator (runs and exports reports)
- Auditor (may run read-only report set if mapped)
- Candidates and centre users do not receive this full report catalogue

### User Journey
1. Who creates: Administrators create report runs by selecting a report family and parameters; the system creates result sets and export files. Underlying transactions are created in Modules 03–08.
2. How they create: Open report catalogue → choose candidate/fee/examination/certificate report → set filters (examination, centre, period, status) → run → preview → export Excel and/or PDF as approved → retrieve from download history if needed.
3. How they edit: Report outputs are not edited in-tool; re-run with new parameters. Saved parameter presets may be updated if provided.
4. How they send for approval: Does not apply — report generation is not an approval package (Department may approve exports offline).
5. How the approver sees pending items: No approver inbox.
6. How the approver decides: No decision.
7. How the applicant / maker sees history: Administrators see export download history of prior runs they are permitted to access.
8. How the approver / auditor sees history: Auditors review the same exports with attribution of who ran which report when.

### Functional Capabilities
- Report catalogue of approved operational/statutory reports
- Candidate report family (registrations, status, centre preferences/allocation as approved)
- Fee report family (payable, paid, exempt, reconciliation-oriented lists as approved)
- Examination report family (schedules, attendance/conduct summaries, pass/fail as approved)
- Certificate report family (issued, cancelled, pending eligibility as approved)
- Parameterised builders per family
- Export to Excel and PDF in finally approved layouts
- Export download history
- Centre/examination/period filters consistent with admin scope

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Report catalogue | Medium |
| Candidate report builder | Complex |
| Fee report builder | Complex |
| Examination report builder | Complex |
| Certificate report builder | Complex |
| Export download history | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| List available reports | Easy |
| Run candidate report | Complex |
| Run fee report | Complex |
| Run examination report | Complex |
| Run certificate report | Complex |
| Export report to Excel | Very High |
| Export report to PDF | Very High |
| Search export download history | Medium |

### Inputs
Report type, examination, centre, date range, status filters, export format choice.

### Outputs
On-screen result sets, Excel exports, PDF exports, export history records.

### Business Rules
- Named reports export in approved formats only.
- Exports include only fields approved for that report.
- Centre-scoped staff (if ever granted limited reports) see only their centre; default catalogue is administrator-wide.
- Large extracts are asynchronous if required by volume, with status in download history.

### Validations
- Mandatory parameters per report type
- Date range validity
- Role allowed to run/export each report family

### Calculations
Aggregates and groupings defined per report (counts, sums of fees, pass rates) without altering source transactions.

### Workflow
Select → parameterise → run → preview → export. No approval.

### Search Requirements
Export history by report type, user, date; in-report search/filter on preview grids where applicable.

### Documents
Excel and PDF export artefacts.

### Reports
This feature is the reports capability.

### Notifications
Optional “export ready” portal/email notice via F09-003 for large async exports if configured.

### Security
Administrator (or designated) role; export actions audited; sensitive fee/PII columns per approval.

### Integrations
None (file generation is internal). External email of exports would use F09-003.

### Dependencies
Modules 03–08 data; F09-004 audits export actions.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Excel and PDF export APIs are each Very High effort.
- Exact column lists finalised with Department from SOW report families; no separate BI product.

### Risks
Column churn after UAT inflating rework — freeze layouts at confirmation.
Very large date ranges timing out — mitigate with async export.

### Non Functional Requirements
Exports complete within approved SLA for typical annual volumes; failed exports visible in history with reason.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Report catalogue | UI | Medium | 6 |
| Candidate report builder | UI | Complex | 12 |
| Fee report builder | UI | Complex | 12 |
| Examination report builder | UI | Complex | 12 |
| Certificate report builder | UI | Complex | 12 |
| Export download history | UI | Easy | 4 |
| List available reports | API | Easy | 4 |
| Run candidate report | API | Complex | 8 |
| Run fee report | API | Complex | 8 |
| Run examination report | API | Complex | 8 |
| Run certificate report | API | Complex | 8 |
| Export report to Excel | API | Very High | 16 |
| Export report to PDF | API | Very High | 16 |
| Search export download history | API | Medium | 6 |
| Report run and export metadata | DB | Complex | 6 |
| Operational and statutory reports tests | Testing | Very High | 12 |
| Operational and statutory reports implementation documentation | Documentation | Complex | 4 |

**Feature total: 154 hours**
