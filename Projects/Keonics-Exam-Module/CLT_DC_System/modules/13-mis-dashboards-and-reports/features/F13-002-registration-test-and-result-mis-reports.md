# F13-002 — Registration, Test & Result MIS Reports

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F13-002 |
| Feature Name | Registration, Test & Result MIS Reports |
| Module | 13 — MIS, Dashboards & Reports |
| Module Type | Business |
| Release | Go-live |

### Description
Catalogue of standard MIS reports (about 20): registrations by category / department / district, scrutiny status, bookings and utilisation, rescheduling, forced moves, attendance, results by session / district / department, topic-wise performance, fee collections and refunds, malpractice, certificates issued, HRMS push status; filters, scheduling and export.

### Business Objective
Meet periodic reporting needs of KEONICS and DPAR.

### Actors
- KEONICS
- Center for E-Governance
- DPAR
- Finance Officer

### User Journey
1. **Who creates:** Users run reports.
2. **How they create:** Users select report and filters.
3. **How they edit:** Users save filter presets.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Users see scheduled report history.
8. **How the approver / auditor sees history:** Auditors see report runs.

### Functional Capabilities
- Report catalogue of about 20 reports
- Filters and presets
- Excel / PDF export
- Scheduling by e-mail
- Data scope enforcement

### UI Screens
- Report catalogue
- Report viewer with filters
- Report scheduling

### Logical API Operations
- Report query engine
- Export Excel / PDF
- Schedule reports
- Report definitions (about 20)

### Inputs
- Filters

### Outputs
- Reports

### Business Rules
- Data scope applies

### Validations
- Date ranges

### Calculations
- Report totals

### Workflow
Not applicable

### Search Requirements
- Reports

### Documents
- Exports

### Reports
- As listed

### Notifications
- Scheduled e-mails

### Security
- Scope

### Integrations
- None

### Dependencies
- All business modules

### Assumptions
- Report list confirmed in FRS

### Risks
- Additional report requests

### Non Functional Requirements
- Under 10 seconds for one year

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Report catalogue | Easy | 4 |
| UI | Report viewer with filters | Complex | 12 |
| UI | Report scheduling | Easy | 4 |
| API | Report query engine | Complex | 8 |
| API | Export Excel / PDF | Medium | 6 |
| API | Schedule reports | Easy | 4 |
| API | Report definitions (about 20) | Very High | 16 |
| Database | Report definitions and schedules | Easy | 2 |
| Testing | Report reconciliation tests | Complex | 8 |
| Documentation | Report catalogue | Easy | 2 |

**Feature Total: 66 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 34 | 2 | 0 | 8 | 2 | **66** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Report definitions rated Very High as a group
- No external integration channel in this feature; Integration row omitted.
