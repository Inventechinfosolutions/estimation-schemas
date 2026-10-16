# F11-006 — Public Certificate Verification

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-006 |
| Feature Name | Public Certificate Verification |
| Module | 11 — Evaluation, Results & Digital Certification |
| Module Type | Business |
| Release | Go-live |

### Description
Public verification page and API: verification by certificate number plus date of birth or by QR scan, showing validity, masked holder name, issue date and status (valid / revoked), with rate limiting and verification logs; legacy certificates verifiable after porting.

### Business Objective
Enable departments and employers to verify certificates instantly.

### Actors
- Public verifier
- Department

### User Journey
1. **Who creates:** A verifier opens the verification page or scans QR.
2. **How they create:** The verifier enters number or scans.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Administrators see verification logs.

### Functional Capabilities
- Verification by number or QR
- Masked display
- Revocation status
- Legacy certificate support
- Rate limiting

### UI Screens
- Public verification page
- Verification result

### Logical API Operations
- Verify certificate
- Verification log

### Inputs
- Certificate number / QR

### Outputs
- Verification result

### Business Rules
- Masked data only

### Validations
- CAPTCHA

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- Verification volumes

### Notifications
- None

### Security
- Rate limiting

### Integrations
- None

### Dependencies
- F11-004
- F18-001

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Under 1 second

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Public verification page | Easy | 4 |
| UI | Verification result | Easy | 4 |
| API | Verify certificate | Easy | 4 |
| API | Verification log | Simple | 2 |
| Database | Verification log | Simple | 1 |
| Testing | Verification tests | Easy | 4 |
| Documentation | Verification guide | Simple | 1 |

**Feature Total: 20 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 6 | 1 | 0 | 4 | 1 | **20** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small
- No external integration channel in this feature; Integration row omitted.
