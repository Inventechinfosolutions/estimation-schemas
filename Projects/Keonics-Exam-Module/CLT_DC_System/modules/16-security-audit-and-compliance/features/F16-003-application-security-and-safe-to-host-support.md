# F16-003 — Application Security & Safe-to-Host Support

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F16-003 |
| Feature Name | Application Security & Safe-to-Host Support |
| Module | 16 — Security, Audit & Compliance |
| Module Type | Technical |
| Release | Go-live |

### Description
Application security controls (input validation, output encoding, CSRF, secure headers, rate limiting, file scanning), dependency and code scanning in pipelines, pre-audit internal VAPT, support to CERT-In empanelled auditor for Safe-to-Host, remediation tracking, and IPv6 readiness checks.

### Business Objective
Obtain Safe-to-Host certification before go-live and annually.

### Actors
- Service Provider security
- CERT-In auditor
- KEONICS

### User Journey
1. **Who creates:** Security team runs scans and audits.
2. **How they create:** Findings logged with severity.
3. **How they edit:** Remediation tracked.
4. **How they send for approval:** Closure verified by auditor.
5. **How the approver sees pending items:** KEONICS sees status.
6. **How the approver decides:** KEONICS accepts certificate.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see findings history.

### Functional Capabilities
- OWASP top 10 controls
- Secure headers and WAF rules
- Code and dependency scanning
- Internal VAPT
- Finding tracker
- IPv6 readiness

### UI Screens
- Security findings tracker

### Logical API Operations
- Security middleware (validation, headers, rate limits)
- File malware scanning
- Finding tracker

### Inputs
- Scan results

### Outputs
- Remediated findings

### Business Rules
- No high findings open at go-live

### Validations
- None

### Calculations
- None

### Workflow
Open → Fixed → Verified

### Search Requirements
- Findings

### Documents
- Audit reports

### Reports
- Security status

### Notifications
- Critical findings

### Security
- As listed

### Integrations
- None

### Dependencies
- F17-001

### Assumptions
- Audit fee is a commercial item

### Risks
- Late findings

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Security findings tracker | Easy | 4 |
| API | Security middleware (validation, headers, rate limits) | Medium | 6 |
| API | File malware scanning | Medium | 6 |
| API | Finding tracker | Easy | 4 |
| Database | Findings | Simple | 1 |
| Testing | Internal VAPT and remediation tests | Very High | 12 |
| Documentation | Security controls document | Medium | 3 |
| Documentation | Safe-to-Host evidence pack | Medium | 3 |

**Feature Total: 39 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 16 | 1 | 0 | 12 | 6 | **39** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Internal VAPT rated Very High
- No external integration channel in this feature; Integration row omitted.
