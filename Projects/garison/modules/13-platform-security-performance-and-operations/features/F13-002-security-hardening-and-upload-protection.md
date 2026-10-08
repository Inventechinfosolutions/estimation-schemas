# F13-002 — Security Hardening & Upload Protection

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F13-002 |
| Feature Name | Security Hardening & Upload Protection |
| Module | 13 — Platform Security, Performance & Operations |
| Module Type | Technical |
| Release | Go-live |

### Description
Platform-wide security controls: OWASP Top 10 protections, HTTPS and HSTS, security headers and content security policy, CSRF protection, rich-text sanitisation, upload content validation and malware scanning, rate limiting and bot protection on public endpoints, and a security settings screen.

### Business Objective
Protect Garrison's catalogue, administrators and visitors against common web attacks.

### Actors
- Super Administrator
- System

### User Journey
1. **Who creates:** Security controls are created by the delivery team; the Super Administrator maintains limited settings (allowed file types, size limits, rate limits).
2. **How they create:** The Super Administrator edits values in Security settings within safe bounds.
3. **How they edit:** Settings can be changed at any time and are audited.
4. **How they send for approval:** No approval applies.
5. **How the approver sees pending items:** There is no approver inbox; security events are visible in the security event log.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see setting changes and security events (blocked uploads, rate-limit hits) in logs.

### Functional Capabilities
- Security headers, CSP, HSTS
- CSRF and input validation framework
- Rich-text sanitisation for descriptions
- Upload content sniffing and malware scanning
- Rate limiting on sign-in, search, suggestions and enquiry
- Security event log
- Security settings screen

### UI Screens
- Security settings

### Logical API Operations
- Validate and scan uploaded content
- Apply rate limiting and bot protection
- Apply security headers and content security policy
- Sanitise rich-text input

### Inputs
- Uploads, public requests, security settings

### Outputs
- Blocked or accepted requests and files
- Security events

### Business Rules
- Executable and unknown file types always rejected
- Infected files quarantined and never stored in public storage

### Validations
- Settings within safe bounds (for example max upload ≤ 50 MB)

### Calculations
- Rate-limit windows

### Workflow
Not applicable

### Search Requirements
- Security event log by type and date

### Documents
- Security controls document

### Reports
- Security test report

### Notifications
- Alert on malware detection (F13-003)

### Security
- This feature is the security baseline

### Integrations
- Malware scanning (for example ClamAV or a hosted scanning API)

### Dependencies
- F01-001
- F04-004
- F04-005
- F10-001
- F12-001
- F12-002

### Assumptions
- Independent third-party penetration testing, if required by Garrison, is outside this estimate

### Risks
- Hosting constraints on running a scanner; a hosted API is the alternative

### Non Functional Requirements
- Security controls add under 50 ms latency to normal requests

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Security settings | Easy | 4 |
| API | Validate and scan uploaded content | Complex | 8 |
| API | Apply rate limiting and bot protection | Medium | 6 |
| API | Apply security headers and content security policy | Medium | 6 |
| API | Sanitise rich-text input | Medium | 6 |
| Database | Security event log | Simple | 1 |
| Integration | Malware scanning service integration | Easy | 8 |
| Testing | OWASP Top 10 verification | Very High | 12 |
| Testing | Upload attack cases | Medium | 6 |
| Documentation | Security controls document | Medium | 3 |

**Feature Total: 60 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 26 | 1 | 8 | 18 | 3 | **60** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- OWASP verification estimated Very High in testing
- No independent VAPT included
