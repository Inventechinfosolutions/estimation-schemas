# F18-002 — Ported Data Validation & Reconciliation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F18-002 |
| Feature Name | Ported Data Validation & Reconciliation |
| Module | 18 — Legacy CLT Data Porting |
| Module Type | Technical |
| Release | Go-live |

### Description
Validation of ported data: record count and checksum reconciliation with legacy sources, rule checks, sample verification by KEONICS, discrepancy register and sign-off report.

### Business Objective
Prove ported data is complete and accurate.

### Actors
- Service Provider porting team
- KEONICS

### User Journey
1. **Who creates:** Porting team runs validation.
2. **How they create:** Validation reports produced.
3. **How they edit:** Discrepancies fixed and re-validated.
4. **How they send for approval:** Sign-off requested.
5. **How the approver sees pending items:** KEONICS sees reports.
6. **How the approver decides:** KEONICS signs off.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see sign-off records.

### Functional Capabilities
- Count reconciliation
- Checksums
- Rule checks
- Sample verification
- Discrepancy register
- Sign-off

### UI Screens
- Reconciliation report
- Sign-off

### Logical API Operations
- Reconciliation engine
- Sign-off record

### Inputs
- Ported data

### Outputs
- Sign-off

### Business Rules
- Go-live requires sign-off

### Validations
- None

### Calculations
- Differences

### Workflow
Validated → Signed off

### Search Requirements
- Discrepancies

### Documents
- Sign-off report

### Reports
- Reconciliation

### Notifications
- None

### Security
- Restricted

### Integrations
- None

### Dependencies
- F18-001

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Reconciliation report | Medium | 6 |
| UI | Sign-off | Easy | 4 |
| API | Reconciliation engine | Medium | 6 |
| API | Sign-off record | Easy | 4 |
| Database | Reconciliation results | Easy | 2 |
| Testing | Reconciliation tests | Medium | 6 |
| Documentation | Porting sign-off report | Easy | 2 |

**Feature Total: 30 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 2 | 0 | 6 | 2 | **30** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
