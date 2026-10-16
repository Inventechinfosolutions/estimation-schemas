# F15-003 — Aadhaar Authentication & eKYC Integration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F15-003 |
| Feature Name | Aadhaar Authentication & eKYC Integration |
| Module | 15 — Integration Hub |
| Module Type | Technical |
| Release | Go-live |

### Description
Integration with Aadhaar authentication and eKYC through the state AUA / KUA (for example via CeG): OTP and biometric authentication, eKYC XML parsing, consent capture, reference token from Aadhaar Data Vault, and error handling per UIDAI codes.

### Business Objective
Verify identity of candidates without KGID and support biometric checks.

### Actors
- System

### User Journey
1. **Who creates:** Calls triggered by registration and centre authentication.
2. **How they create:** Connector calls AUA / KUA.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Operations see failure rates.
6. **How the approver decides:** Operations escalate to AUA.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see transaction references (no Aadhaar numbers).

### Functional Capabilities
- OTP authentication
- Biometric authentication
- eKYC
- Consent
- Vault tokenisation
- UIDAI error mapping

### UI Screens
- None (no user interface in this feature)

### Logical API Operations
- Aadhaar OTP adapter
- eKYC adapter and parser
- Biometric authentication adapter
- Vault tokenisation

### Inputs
- Aadhaar OTP / biometrics

### Outputs
- Authentication / eKYC data

### Business Rules
- UIDAI regulations

### Validations
- Consent

### Calculations
- None

### Workflow
Requested → Success / Failed

### Search Requirements
- Transactions

### Documents
- None

### Reports
- eKYC success rates

### Notifications
- None

### Security
- Aadhaar vault; no storage of numbers

### Integrations
- UIDAI via AUA / KUA

### Dependencies
- F15-001
- F16-004

### Assumptions
- KEONICS / CeG provides AUA / KUA access

### Risks
- Onboarding timelines

### Non Functional Requirements
- Under 10 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Aadhaar OTP adapter | Medium | 6 |
| API | eKYC adapter and parser | Medium | 6 |
| API | Biometric authentication adapter | Medium | 6 |
| API | Vault tokenisation | Medium | 6 |
| Database | eKYC transaction log | Easy | 2 |
| Integration | Aadhaar AUA / KUA services | Very High | 40 |
| Testing | Aadhaar integration tests | Complex | 8 |
| Documentation | Aadhaar integration note | Easy | 2 |

**Feature Total: 76 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 24 | 2 | 40 | 8 | 2 | **76** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Rated Very High given compliance
