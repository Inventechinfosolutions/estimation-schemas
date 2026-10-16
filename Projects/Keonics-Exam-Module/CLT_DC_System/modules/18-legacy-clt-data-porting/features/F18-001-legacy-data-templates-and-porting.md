# F18-001 — Legacy Data Templates & Porting

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F18-001 |
| Feature Name | Legacy Data Templates & Porting |
| Module | 18 — Legacy CLT Data Porting |
| Module Type | Technical |
| Release | Go-live |

### Description
Porting of legacy CLT data: templates for candidates, attempts, scores, results and certificates; staging import; mapping to new structures (KGID, categories, centres); de-duplication; loading as historical records so attempts count for fee rules and certificates are verifiable.

### Business Objective
Bring previous CLT data into the new system.

### Actors
- Service Provider porting team
- KEONICS

### User Journey
1. **Who creates:** KEONICS provides legacy data in templates.
2. **How they create:** Porting team loads data to staging.
3. **How they edit:** Errors corrected by KEONICS and re-loaded.
4. **How they send for approval:** Final load requires KEONICS sign-off.
5. **How the approver sees pending items:** KEONICS sees porting reports.
6. **How the approver decides:** KEONICS signs off.
7. **How the applicant / maker sees history:** Candidates see historical attempts.
8. **How the approver / auditor sees history:** Auditors see porting logs.

### Functional Capabilities
- Templates
- Staging
- Mapping rules
- De-duplication
- Historical record load
- Porting logs

### UI Screens
- Porting console
- Staging error report

### Logical API Operations
- Staging import
- Mapping and transformation
- De-duplication
- Final load

### Inputs
- Legacy data

### Outputs
- Historical records

### Business Rules
- Ported data read-only

### Validations
- Template formats

### Calculations
- None

### Workflow
Staged → Validated → Loaded

### Search Requirements
- Ported records

### Documents
- Templates

### Reports
- Porting report

### Notifications
- None

### Security
- Encrypted staging

### Integrations
- None

### Dependencies
- F04-002
- F11-006
- F02-004

### Assumptions
- Legacy data available in exportable form

### Risks
- Legacy data quality

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Porting console | Medium | 6 |
| UI | Staging error report | Medium | 6 |
| API | Staging import | Medium | 6 |
| API | Mapping and transformation | Complex | 8 |
| API | De-duplication | Medium | 6 |
| API | Final load | Medium | 6 |
| Database | Staging and historical tables | Medium | 4 |
| Testing | Porting tests with sample data | Complex | 8 |
| Documentation | Data migration document | Medium | 3 |

**Feature Total: 53 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 26 | 4 | 0 | 8 | 3 | **53** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
