# F11-004 — Standard MIS Reports

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-004 |
| Feature Name | Standard MIS Reports |
| Module | 11 — Dashboards, MIS & Reports |
| Module Type | Business |
| Release | Go-live |

### Description
Library of standard reports — auction-wise results, layout-wise awards, DS-wise pendency, period-wise collections, outstanding dues, extensions, defaults and cancellations, disputes, completion, notifications and audit summaries — with filters and export to Excel and PDF.

### Business Objective
Meet BDA's routine reporting needs with consistent, exportable reports.

### Actors
- All staff roles (per permission)

### User Journey
1. **Who creates:** Reports are predefined.
2. **How they create:** Users select a report, apply filters and run it.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Users export results.
8. **How the approver / auditor sees history:** Auditors see report runs and exports.

### Functional Capabilities
- 15+ standard reports
- Filters by auction, layout, DS, period
- Excel / PDF export
- Scheduled e-mail of reports

### UI Screens
- Report catalogue
- Report viewer with filters
- Report schedule

### Logical API Operations
- Run report
- Export Excel / PDF
- Schedule report
- Report definitions (15+)

### Inputs
- Filters

### Outputs
- Reports

### Business Rules
- DS isolation in all reports

### Validations
- Date ranges

### Calculations
- Report totals

### Workflow
Not applicable

### Search Requirements
- Reports by name

### Documents
- Exports

### Reports
- All standard reports

### Notifications
- Scheduled report e-mails

### Security
- Permission per report; export logging

### Integrations
- None

### Dependencies
- All business modules

### Assumptions
- Report list confirmed in SRS

### Risks
- Report scope creep

### Non Functional Requirements
- Reports up to 50,000 rows within 30 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Report catalogue | Easy | 4 |
| UI | Report viewer with filters | Medium | 6 |
| UI | Report schedule | Easy | 4 |
| API | Run report | Medium | 6 |
| API | Export Excel / PDF | Medium | 6 |
| API | Schedule report | Easy | 4 |
| API | Report definitions (15+) | Complex | 8 |
| Database | Reporting views | Medium | 4 |
| Testing | Report accuracy tests | Complex | 8 |
| Documentation | Report catalogue with definitions | Medium | 3 |

**Feature Total: 53 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 24 | 4 | 0 | 8 | 3 | **53** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Report definitions rated Complex as a group
- No external integration channel in this feature; Integration row omitted.
