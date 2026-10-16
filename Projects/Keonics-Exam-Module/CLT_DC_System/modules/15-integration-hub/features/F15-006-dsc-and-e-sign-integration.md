# F15-006 — DSC & e-Sign Integration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F15-006 |
| Feature Name | DSC & e-Sign Integration |
| Module | 15 — Integration Hub |
| Module Type | Technical |
| Release | Go-live |

### Description
Signing service supporting server-side DSC (HSM-held organisational certificate) for bulk certificate and result signing and Aadhaar e-Sign / USB DSC for officer approvals, PAdES PDF signatures, signature verification and certificate validity checks.

### Business Objective
Provide digital signatures required for results and certificates.

### Actors
- System
- Result Officer
- KEONICS Approver

### User Journey
1. **Who creates:** Signing triggered by result and certificate workflows.
2. **How they create:** Service signs with configured method.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Operations see signing failures.
6. **How the approver decides:** Operations retry.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors verify signatures.

### Functional Capabilities
- Server-side bulk DSC signing
- e-Sign / USB DSC for officers
- PAdES signatures
- Verification
- Certificate validity checks

### UI Screens
- Signing status

### Logical API Operations
- Bulk sign adapter
- e-Sign adapter
- Verify signature

### Inputs
- Documents

### Outputs
- Signed documents

### Business Rules
- Valid certificate only

### Validations
- Certificate chain

### Calculations
- None

### Workflow
Requested → Signed / Failed

### Search Requirements
- Signing log

### Documents
- Signed PDFs

### Reports
- Signing statistics

### Notifications
- None

### Security
- Keys in HSM

### Integrations
- e-Sign ASP / DSC

### Dependencies
- F15-005

### Assumptions
- Signing certificates provided

### Risks
- None

### Non Functional Requirements
- Under 2 seconds per document

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Signing status | Easy | 4 |
| API | Bulk sign adapter | Medium | 6 |
| API | e-Sign adapter | Medium | 6 |
| API | Verify signature | Easy | 4 |
| Database | Signing log | Easy | 2 |
| Integration | DSC / e-Sign service | Complex | 24 |
| Testing | Signing tests | Medium | 6 |
| Documentation | Signing note | Easy | 2 |

**Feature Total: 54 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 16 | 2 | 24 | 6 | 2 | **54** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
