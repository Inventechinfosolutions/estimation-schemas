# F06-004 — Activity Revenue and Utilization Reports

| Field | Value |
|-------|-------|
| Feature ID | F06-004 |
| Feature Name | Activity Revenue and Utilization Reports |
| Module | 06 — Administration, Monitoring & Reports |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Provides reports for booking activity, revenue, and utilization.

### Business Objective
Support operational and financial oversight with exportable reports.

### Actors
- Platform Administrator
- Site Administrator
- Auditor

### User Journey
1. Administrator creates a report run by selecting type and filters.
2. Runs report and views tabular results; exports CSV/PDF.
3. Re-runs with new filters; no edit of historical frozen exports unless saved snapshots supported lightly.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Admin sees recent report runs if retained.
8. Auditor runs read-only reports.

### Functional Capabilities
- Booking activity report
- Revenue report
- Utilization report
- Export CSV/PDF
- Filter by site/date

### UI Screens
- Report catalogue screen
- Report filter and run screen
- Report results table
- Export confirmation

### Logical API Operations
- Run booking activity report
- Run revenue report
- Run utilization report
- Export report

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Site scope enforced
- Revenue based on successful payments

### Validations
- Date range mandatory

### Calculations
- Utilization = occupied room-nights / available room-nights

### Workflow
FiltersSet → ReportGenerated → Exported

### Search Requirements
Within report results

### Documents
Exported report files

### Reports
This feature

### Notifications
None

### Security
- Role-gated financial figures

### Integrations
None

### Dependencies
- F03-002
- F04-002
- F05-003

### Assumptions
- PDF/CSV sufficient; BI tool out of scope

### Risks
- Heavy date ranges timeout

### Non Functional Requirements
- Async export for large ranges if needed

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Report catalogue screen | Easy | 4 |
| UI | Report filter and run screen | Complex | 12 |
| UI | Report results table | Medium | 6 |
| UI | Export confirmation | Simple | 2 |
| API | Run booking activity report | Complex | 8 |
| API | Run revenue report | Complex | 8 |
| API | Run utilization report | Complex | 8 |
| API | Export report | Medium | 6 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 65 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: PDF/CSV sufficient; BI tool out of scope / Heavy date ranges timeout.
