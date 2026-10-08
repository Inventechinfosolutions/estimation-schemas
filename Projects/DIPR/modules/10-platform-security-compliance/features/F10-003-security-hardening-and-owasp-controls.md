# F10-003 — Security hardening & OWASP controls

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F10-003 |
| Feature Name | Security hardening & OWASP controls |
| Module | 10 — Platform Security & Compliance Controls |
| Description | Platform hardening aligned to OWASP Top 10 and DIPR security guidelines |
| Business Objective | Reduce exploitable attack surface across AMT with OWASP-aligned controls. |
| Actors | Platform Engineer; Security Officer; Developer |

### User Journey

- Security baseline applied → headers/CSP/input validation/safe defaults configured → periodic dependency scan → findings tracked to closure.

### Functional Capabilities

- OWASP Top 10 mitigations (injection, broken auth, XSS, misconfiguration, etc.)
- Secure HTTP headers and cookie flags
- Centralized input validation patterns
- Security logging for suspicious activity

### Inputs

Security baseline checklist; DIPR guideline annex

### Outputs

Hardened deployment profile; closed checklist items

### Business Rules

No production deployment without baseline checklist sign-off

### Validations

- N/A

### Calculations

- None

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

- None

### Dependencies

Module 01 auth; F09-001 external APIs

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

Defense-in-depth across web, mobile API, and integration endpoints

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Security headers/cookie diagnostic read-only panel | Simple | 2 |
| API | Central input validation middleware | Complex | 8 |
| API | CSRF and session hardening hooks | Medium | 6 |
| API | Security event capture emitters | Easy | 4 |
| Database | Security event log support fields | Easy | 2 |
| Testing | OWASP Top 10 oriented test pack | Very High | 12 |
| Testing | Scan finding remediation regression | Complex | 8 |
| Testing | Mobile API auth bypass negative | Medium | 6 |
| Documentation | Security hardening checklist for DIPR | Complex | 4 |
| Documentation | Middleware configuration reference | Easy | 2 |

**Feature Total: 54 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
