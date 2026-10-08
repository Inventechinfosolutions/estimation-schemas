# F07-005 — Scheduled & exportable reports

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-005 |
| Feature Name | Scheduled & exportable reports |
| Module | 07 — Reporting & Analytics |
| Description | PDF/CSV export and scheduled delivery of standard reports |
| Business Objective | Automate recurring management reports and ad-hoc exports in standard formats. |
| Actors | Campaign Manager; Admin; System (scheduler) |

### User Journey

- User configures schedule for a standard report → selects recipients → system generates PDF/CSV on cadence → delivery via email (Module 08) → failures logged.

### Functional Capabilities

- On-demand PDF/CSV export for entitled reports
- Schedule definitions (daily/weekly/monthly as configured)
- Recipient lists within policy
- Job history with last run status

### Inputs

Report type; parameters; schedule; recipients

### Outputs

Generated files; delivery notifications

### Business Rules

Schedules respect role entitlements
Large exports run asynchronously

### Validations

- N/A

### Calculations

- None

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

- None

### Notifications

Success/failure alerts to report owner on failure

### Security

- RBAC and platform security controls apply

### Integrations

Email dispatch via Module 08

### Dependencies

F07-001–F07-003; Module 08 F08-002

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Report catalogue picker for export | Medium | 6 |
| UI | On-demand export dialog (format, filters) | Complex | 12 |
| UI | Schedule configuration wizard steps | Very High | 16 |
| UI | Scheduled job list with next-run display | Medium | 6 |
| API | Render report to PDF/Excel job | Very High | 16 |
| API | Create/update report schedule | Complex | 8 |
| API | Cancel/pause scheduled report job | Easy | 4 |
| API | Fetch report job status and download link | Medium | 6 |
| Integration | Scheduled completion email via Module 08 | Easy | 8 |
| Database | Report job queue persistence | Medium | 4 |
| Database | Schedule recurrence rule storage | Medium | 4 |
| Testing | One-off export format validation | Complex | 8 |
| Testing | Scheduled cron fire mock | Complex | 8 |
| Testing | Failed job retry notification | Medium | 6 |
| Documentation | Report scheduling admin guide | Medium | 3 |
| Documentation | Supported formats matrix | Easy | 2 |

**Feature Total: 117 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
