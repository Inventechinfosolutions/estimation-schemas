# F14-002 — Audit Viewer & Evidence Certificate Support

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F14-002 |
| Feature Name | Audit Viewer & Evidence Certificate Support |
| Module | 14 — Audit, Security & Compliance |
| Module Type | Technical |
| Release | Go-live |

### Description
Search and view of audit records by case, user, action and period, chain integrity verification, export of audit extracts with hash, and generation of a data sheet supporting certification of electronic records under Section 63 of the Bharatiya Sakshya Adhiniyam, 2023.

### Business Objective
Enable BDA to produce audit evidence for inquiries and courts.

### Actors
- Super Admin
- Auditor (read-only role)

### User Journey
1. **Who creates:** Auditors search records.
2. **How they create:** The auditor applies filters and views results.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors export extracts with integrity proof.

### Functional Capabilities
- Audit search
- Case audit history
- Integrity verification
- Extract export with hash
- Section 63 support data sheet

### UI Screens
- Audit search
- Audit record detail
- Integrity verification result
- Evidence extract and data sheet

### Logical API Operations
- Search audit
- Verify chain integrity
- Export extract with hash
- Generate data sheet

### Inputs
- Filters

### Outputs
- Extracts
- Data sheet

### Business Rules
- Exports are audited

### Validations
- Date range

### Calculations
- Hash verification

### Workflow
Not applicable

### Search Requirements
- By case, user, action, date

### Documents
- Extracts

### Reports
- Audit reports

### Notifications
- None

### Security
- Restricted roles

### Integrations
- None

### Dependencies
- F14-001

### Assumptions
- BDA's certifying officer signs the certificate

### Risks
- None

### Non Functional Requirements
- Search within 5 seconds for 1 year of data

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Audit search | Medium | 6 |
| UI | Audit record detail | Easy | 4 |
| UI | Integrity verification result | Easy | 4 |
| UI | Evidence extract and data sheet | Medium | 6 |
| API | Search audit | Medium | 6 |
| API | Verify chain integrity | Complex | 8 |
| API | Export extract with hash | Medium | 6 |
| API | Generate data sheet | Medium | 6 |
| Testing | Search, verification and export tests | Medium | 6 |
| Documentation | Audit and evidence procedure | Easy | 2 |

**Feature Total: 54 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 26 | 0 | 0 | 6 | 2 | **54** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Integrity verification rated Complex
- No external integration channel in this feature; Integration row omitted.
