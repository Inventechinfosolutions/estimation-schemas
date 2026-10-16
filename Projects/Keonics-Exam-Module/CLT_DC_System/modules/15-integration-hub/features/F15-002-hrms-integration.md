# F15-002 — HRMS Integration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F15-002 |
| Feature Name | HRMS Integration |
| Module | 15 — Integration Hub |
| Module Type | Technical |
| Release | Go-live |

### Description
Bidirectional HRMS integration: employee look-up by KGID (name, department, posting, designation, date of birth, contact, status), centre-side validation fetch, and push of results and certificate references with acknowledgement and reconciliation.

### Business Objective
Use HRMS as the source of truth and update it with CLT outcomes.

### Actors
- System

### User Journey
1. **Who creates:** Calls triggered by registration, validation and certificate issue.
2. **How they create:** Connector calls HRMS and maps data.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Operations see failures.
6. **How the approver decides:** Operations replay.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see exchanges.

### Functional Capabilities
- Employee look-up
- Data mapping
- Result push
- Acknowledgement and reconciliation
- Replay

### UI Screens
- HRMS push reconciliation

### Logical API Operations
- HRMS look-up adapter
- HRMS result push adapter
- Reconciliation job

### Inputs
- KGID
- Results

### Outputs
- Employee data
- HRMS updates

### Business Rules
- HRMS data read-only in CLT

### Validations
- Response schema

### Calculations
- None

### Workflow
Requested → Success / Failed

### Search Requirements
- Exchanges

### Documents
- None

### Reports
- Push reconciliation

### Notifications
- Failure alerts

### Security
- Mutual TLS / tokens

### Integrations
- HRMS

### Dependencies
- F15-001

### Assumptions
- HRMS APIs provided by DPAR / CeG

### Risks
- API availability and readiness

### Non Functional Requirements
- Look-up under 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | HRMS push reconciliation | Easy | 4 |
| API | HRMS look-up adapter | Medium | 6 |
| API | HRMS result push adapter | Medium | 6 |
| API | Reconciliation job | Medium | 6 |
| Database | HRMS exchange log | Easy | 2 |
| Integration | HRMS employee look-up API | Complex | 24 |
| Integration | HRMS result update API | Complex | 24 |
| Testing | HRMS integration tests | Complex | 8 |
| Documentation | HRMS interface specification | Easy | 2 |

**Feature Total: 82 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 18 | 2 | 48 | 8 | 2 | **82** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Two HRMS APIs
