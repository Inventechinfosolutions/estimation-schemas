# F11-004 — Digitally Signed Certificate Generation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-004 |
| Feature Name | Digitally Signed Certificate Generation |
| Module | 11 — Evaluation, Results & Digital Certification |
| Module Type | Business |
| Release | Go-live |

### Description
Generation of CLT qualifying certificates for qualified candidates from the approved template: unique certificate number, candidate details, score and date, security watermark, QR linking to verification, anti-duplication features, and digital signature of the competent authority via e-Sign / DSC; bulk generation per session.

### Business Objective
Issue tamper-proof certificates.

### Actors
- System
- Result Officer

### User Journey
1. **Who creates:** Certificates are generated after result approval.
2. **How they create:** Bulk generation runs per session.
3. **How they edit:** Regeneration for corrections with reason.
4. **How they send for approval:** Certificates go to issue workflow (F11-005).
5. **How the approver sees pending items:** Officer sees generation status.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Candidates see certificate after issue.
8. **How the approver / auditor sees history:** Auditors see certificate register.

### Functional Capabilities
- Unique certificate number
- Watermark and security background
- QR verification link
- Digital signature
- Bulk generation
- Certificate register
- Regeneration with revocation of old

### UI Screens
- Certificate generation status
- Certificate register

### Logical API Operations
- Generate certificate PDF
- Apply digital signature
- Bulk generation job
- Revoke and regenerate

### Inputs
- Approved results

### Outputs
- Signed certificates

### Business Rules
- Only qualified candidates
- One active certificate per qualifying attempt

### Validations
- Signature valid

### Calculations
- None

### Workflow
Generated → Signed → Issued / Revoked

### Search Requirements
- By certificate number

### Documents
- Certificate PDF

### Reports
- Certificates issued

### Notifications
- None

### Security
- PAdES signature

### Integrations
- e-Sign / DSC via F15-006

### Dependencies
- F02-005
- F11-003
- F15-006

### Assumptions
- Signing authority confirmed

### Risks
- None

### Non Functional Requirements
- 1,000 certificates per hour

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Certificate generation status | Easy | 4 |
| UI | Certificate register | Medium | 6 |
| API | Generate certificate PDF | Medium | 6 |
| API | Apply digital signature | Medium | 6 |
| API | Bulk generation job | Medium | 6 |
| API | Revoke and regenerate | Easy | 4 |
| Database | Certificate register | Easy | 2 |
| Testing | Certificate tests including signature validation | Medium | 6 |
| Documentation | Certificate specification | Easy | 2 |

**Feature Total: 42 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 22 | 2 | 0 | 6 | 2 | **42** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
