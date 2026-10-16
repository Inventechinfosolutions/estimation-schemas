# F14-003 — Application Security Controls

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F14-003 |
| Feature Name | Application Security Controls |
| Module | 14 — Audit, Security & Compliance |
| Module Type | Technical |
| Release | Go-live |

### Description
Security controls across the Module: AES-256 encryption at rest for sensitive fields and documents, TLS 1.2+ in transit, OWASP Top 10 protections (input validation, output encoding, CSRF, secure headers, file upload checks with malware scan), rate limiting, CAPTCHA, secure secrets handling, and support for VAPT remediation.

### Business Objective
Protect bidder and financial data and pass VAPT before go-live.

### Actors
- System
- Super Admin

### User Journey
1. **Who creates:** Controls are applied by the system.
2. **How they create:** Not applicable.
3. **How they edit:** The Super Admin adjusts rate limits and upload settings.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see security events.

### Functional Capabilities
- Field and file encryption
- Secure headers and CSP
- Rate limiting and CAPTCHA
- Malware scanning of uploads
- Security event logging
- VAPT remediation support

### UI Screens
- Security settings

### Logical API Operations
- Encryption service
- Rate limiter
- Upload scanning
- Security event logging

### Inputs
- Settings

### Outputs
- Protected application

### Business Rules
- Sensitive fields encrypted
- Uploads scanned before storage

### Validations
- File types

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- Security events

### Documents
- None

### Reports
- Security events report

### Notifications
- Security alerts

### Security
- As described

### Integrations
- Antivirus engine

### Dependencies
- F13-001

### Assumptions
- VAPT by BDA-appointed auditor

### Risks
- VAPT findings late in schedule

### Non Functional Requirements
- High / critical findings fixed within 7 days

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Security settings | Easy | 4 |
| API | Encryption service | Medium | 6 |
| API | Rate limiter | Medium | 6 |
| API | Upload scanning | Medium | 6 |
| API | Security event logging | Easy | 4 |
| Database | Key references and security settings | Easy | 2 |
| Testing | Security testing (OWASP Top 10) | Very High | 12 |
| Testing | VAPT remediation retest | Complex | 8 |
| Documentation | Security controls document | Medium | 3 |

**Feature Total: 51 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 22 | 2 | 0 | 20 | 3 | **51** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- VAPT service excluded; remediation testing included
- No external integration channel in this feature; Integration row omitted.
