# F16-001 — Data Encryption & Key Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F16-001 |
| Feature Name | Data Encryption & Key Management |
| Module | 16 — Security, Audit & Compliance |
| Module Type | Technical |
| Release | Go-live |

### Description
Encryption framework: AES-256-GCM field and object encryption for credentials, question components, answer keys, candidate responses, results and recordings, envelope encryption with data keys wrapped by HSM, asymmetric encryption for paper distribution, TLS 1.2+ everywhere, and key rotation with re-encryption jobs.

### Business Objective
Meet the RFP encryption requirements end to end.

### Actors
- System
- Security Officer

### User Journey
1. **Who creates:** Encryption applies automatically to classified data.
2. **How they create:** Classification configured per data type.
3. **How they edit:** Changes versioned.
4. **How they send for approval:** Changes need Security Officer approval.
5. **How the approver sees pending items:** Officer sees pending changes.
6. **How the approver decides:** Officer approves.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see key usage and re-encryption logs.

### Functional Capabilities
- Field and object encryption
- Envelope encryption with HSM
- Asymmetric encryption for papers
- TLS enforcement
- Rotation and re-encryption
- Data classification register

### UI Screens
- Encryption classification register

### Logical API Operations
- Encryption service
- Re-encryption job
- Key usage logging

### Inputs
- Data

### Outputs
- Encrypted data

### Business Rules
- No plaintext sensitive data at rest

### Validations
- Algorithm policy

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- Encryption coverage

### Notifications
- Rotation reminders

### Security
- AES-256, RSA / ECC

### Integrations
- HSM via F15-005

### Dependencies
- F15-005

### Assumptions
- None

### Risks
- Performance overhead

### Non Functional Requirements
- Under 5 ms per operation

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Encryption classification register | Easy | 4 |
| API | Encryption service | Complex | 8 |
| API | Re-encryption job | Medium | 6 |
| API | Key usage logging | Easy | 4 |
| Database | Encrypted columns and key references | Medium | 4 |
| Testing | Encryption verification tests | Complex | 8 |
| Documentation | Cryptography design document | Medium | 3 |

**Feature Total: 37 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 18 | 4 | 0 | 8 | 3 | **37** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Core security
- No external integration channel in this feature; Integration row omitted.
