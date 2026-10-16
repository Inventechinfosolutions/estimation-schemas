# F11-002 — Deputy Secretary Dashboard

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-002 |
| Feature Name | Deputy Secretary Dashboard |
| Module | 11 — Dashboards, MIS & Reports |
| Module Type | Business |
| Release | Go-live |

### Description
DS-wise dashboard showing cases received, under processing, awaiting bidder, draft deed stage, awaiting final payment, registration and completion, timer status, officer workload and ageing, restricted to the DS office.

### Business Objective
Help Deputy Secretaries manage pendency and workload.

### Actors
- Deputy Secretary
- Case Worker

### User Journey
1. **Who creates:** Data is aggregated by the system.
2. **How they create:** The DS opens the dashboard.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The DS drills down to cases.
8. **How the approver / auditor sees history:** Auditors see access.

### Functional Capabilities
- Stage counts
- Timer status
- Officer workload
- Ageing
- Drill-down

### UI Screens
- DS dashboard
- Officer workload view

### Logical API Operations
- DS KPI aggregation
- Workload computation
- Drill-down

### Inputs
- Filters

### Outputs
- KPIs

### Business Rules
- DS isolation

### Validations
- None

### Calculations
- Counts and ageing

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
- DS isolation

### Integrations
- None

### Dependencies
- F07-005
- F01-003

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Loads within 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | DS dashboard | Medium | 6 |
| UI | Officer workload view | Easy | 4 |
| API | DS KPI aggregation | Medium | 6 |
| API | Workload computation | Easy | 4 |
| API | Drill-down | Easy | 4 |
| Testing | DS isolation and KPI tests | Medium | 6 |
| Documentation | DS dashboard note | Simple | 1 |

**Feature Total: 31 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 14 | 0 | 0 | 6 | 1 | **31** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Moderate
- No external integration channel in this feature; Integration row omitted.
