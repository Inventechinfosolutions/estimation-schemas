# F06-003 — Progress Reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-003 |
| **Feature Name** | Progress Reports |
| **Module** | 06 — e-Office Upload, Backup and Progress MIS |

### Description
Produce daily, weekly, monthly and overall progress views: files inward, pages scanned by A4/Legal vs A3+, QC pending, defects, metadata complete, uploaded, returned.

### Business Objective
Department and KEONICS can see whether the two-month job is on track without waiting for final certification.

### Actors
Maker: Supervisor (runs reports). Viewer: Department Officer. Approver: none.

### User Journey
1. Who creates: Counts are derived from operational data; Supervisor opens reports.
2. How they create: Daily report for a date; period report for week/month/overall with date range.
3. How they edit: Reports are not edited; underlying data is.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox. The report is the visibility.
6. How the approver decides: No decision.
7. How the maker sees history: Previous days’ daily reports can be reopened.
8. How the auditor sees history: Department Officer same reports.

### Functional Capabilities
- Daily progress
- Weekly/monthly/overall period progress
- Counts from inward, scan, QC, metadata, upload, outward
- Exclude blank pages from scan counts

### UI Screens
| Screen | Complexity |
|---|---|
| Daily progress report | Medium |
| Period progress report | Medium |

### Logical API operations
| Operation | Complexity |
|---|---|
| Compute daily progress | Medium |
| Compute period progress | Medium |
| Generate progress report | Medium |

### Inputs
Date or date range.

### Outputs
Counts and simple lists of bottlenecks (QC pending, defects).

### Business Rules
- Blank pages excluded.
- Indicative IFQ totals are reference only, not auto-completion.

### Validations
- Date range valid.

### Calculations
Sums of files and pages by stage.

### Workflow
No approval.

### Search Requirements
By date.

### Documents
None.

### Reports
This feature is the reports.

### Notifications
None.

### Security
Supervisor and Department Officer.

### Integrations
None.

### Dependencies
Modules 02–06 operational data.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- No scheduled email of reports.

### Risks
Counts disagree with paper log if operators skip digital entry.

### Non Functional Requirements
Report for a day runs on site data volumes (~thousands of files, not lakhs of UI rows).

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Daily progress report | UI | Medium | 6 |
| Period progress report | UI | Medium | 6 |
| Compute daily progress | API | Medium | 6 |
| Compute period progress | API | Medium | 6 |
| Generate progress report | API | Medium | 6 |
| Report snapshot support | DB | Easy | 2 |
| Progress reports tests | Testing | Medium | 6 |
| Progress reports implementation documentation | Documentation | Easy | 2 |

**Feature total: 40 hours**
