# F16-002 — Migration Validation & Reconciliation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F16-002 |
| Feature Name | Migration Validation & Reconciliation |
| Module | 16 — Legacy Case Migration |
| Module Type | Technical |
| Release | Go-live |

### Description
Business validation of staged data (site exists, payments sum, schedule consistency, stage consistency), reconciliation reports of counts and amounts against BDA records, correction cycles and BDA sign-off.

### Business Objective
Ensure migrated data is accurate before activation.

### Actors
- Migration team
- Finance Officer
- Auction Admin

### User Journey
1. **Who creates:** The migration team runs validation.
2. **How they create:** Validation produces error and reconciliation reports.
3. **How they edit:** BDA corrects data and reloads.
4. **How they send for approval:** Final data is submitted for sign-off.
5. **How the approver sees pending items:** Finance and Auction Admin review reconciliation.
6. **How the approver decides:** They sign off or return.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Sign-off retained.

### Functional Capabilities
- Business validation rules
- Reconciliation reports
- Correction cycles
- Sign-off

### UI Screens
- Validation results
- Reconciliation report
- Sign-off

### Logical API Operations
- Run business validation
- Reconciliation computation
- Sign-off

### Inputs
- Staged data

### Outputs
- Reports
- Sign-off

### Business Rules
- No activation without sign-off

### Validations
- Rules

### Calculations
- Totals

### Workflow
Validated → Corrected → Signed off

### Search Requirements
- Errors

### Documents
- Sign-off

### Reports
- Reconciliation

### Notifications
- None

### Security
- Restricted

### Integrations
- None

### Dependencies
- F16-001

### Assumptions
- None

### Risks
- Multiple correction cycles

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Validation results | Medium | 6 |
| UI | Reconciliation report | Medium | 6 |
| UI | Sign-off | Easy | 4 |
| API | Run business validation | Complex | 8 |
| API | Reconciliation computation | Medium | 6 |
| API | Sign-off | Easy | 4 |
| Testing | Validation rule tests | Medium | 6 |
| Documentation | Reconciliation report templates | Easy | 2 |

**Feature Total: 42 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 18 | 0 | 0 | 6 | 2 | **42** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Validation rated Complex
- No external integration channel in this feature; Integration row omitted.
