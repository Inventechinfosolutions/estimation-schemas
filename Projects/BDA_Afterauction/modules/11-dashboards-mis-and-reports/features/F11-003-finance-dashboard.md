# F11-003 — Finance Dashboard

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-003 |
| Feature Name | Finance Dashboard |
| Module | 11 — Dashboards, MIS & Reports |
| Module Type | Business |
| Release | Go-live |

### Description
Finance dashboard with demands raised, collections by mode and period, outstanding and overdue by ageing bucket, reconciliation status, pending offline verifications, extensions, defaults and disputes.

### Business Objective
Give Finance a daily controlled view of collections and exceptions.

### Actors
- Finance Officer
- Payment Reconciler

### User Journey
1. **Who creates:** Data is aggregated by the system.
2. **How they create:** Finance opens the dashboard.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Finance drills down.
8. **How the approver / auditor sees history:** Auditors see access.

### Functional Capabilities
- Collections
- Outstanding and ageing
- Reconciliation status
- Exceptions panel

### UI Screens
- Finance dashboard
- Collections drill-down

### Logical API Operations
- Finance KPI aggregation
- Ageing buckets
- Drill-down

### Inputs
- Filters

### Outputs
- KPIs

### Business Rules
- Figures match ledger

### Validations
- None

### Calculations
- Totals and ageing

### Workflow
Not applicable

### Search Requirements
- Filters

### Documents
- None

### Reports
- Export

### Notifications
- None

### Security
- Finance roles

### Integrations
- None

### Dependencies
- Module 06

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Loads within 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Finance dashboard | Medium | 6 |
| UI | Collections drill-down | Easy | 4 |
| API | Finance KPI aggregation | Medium | 6 |
| API | Ageing buckets | Easy | 4 |
| API | Drill-down | Easy | 4 |
| Testing | Finance KPI reconciliation tests | Medium | 6 |
| Documentation | Finance dashboard note | Simple | 1 |

**Feature Total: 31 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 14 | 0 | 0 | 6 | 1 | **31** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Moderate
- No external integration channel in this feature; Integration row omitted.
