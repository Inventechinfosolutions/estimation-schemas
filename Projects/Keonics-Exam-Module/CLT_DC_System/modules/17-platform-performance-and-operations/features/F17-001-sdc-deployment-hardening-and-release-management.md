# F17-001 — SDC Deployment, Hardening & Release Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F17-001 |
| Feature Name | SDC Deployment, Hardening & Release Management |
| Module | 17 — Platform, Performance & Operations |
| Module Type | Technical |
| Release | Go-live |

### Description
Setup of environments at SDC (UAT and production; development at vendor premises), container or VM deployment, CI/CD with approvals, infrastructure as code, configuration management, OS and middleware hardening per CIS benchmarks before each test cycle, release runbooks and rollback.

### Business Objective
Deploy and operate reliably at SDC.

### Actors
- Service Provider operations
- SDC
- KEONICS

### User Journey
1. **Who creates:** Operations prepare releases.
2. **How they create:** Pipeline builds, tests and packages.
3. **How they edit:** Releases corrected through new builds.
4. **How they send for approval:** Production releases need KEONICS approval.
5. **How the approver sees pending items:** KEONICS sees release notes.
6. **How the approver decides:** KEONICS approves window.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see release history.

### Functional Capabilities
- Environment setup
- CI/CD pipeline
- Infrastructure as code
- Hardening checklists
- Release approval
- Rollback

### UI Screens
- Release register

### Logical API Operations
- Deployment pipeline
- Configuration management
- Hardening automation

### Inputs
- Builds

### Outputs
- Deployed releases

### Business Rules
- No production change without approval

### Validations
- Pipeline gates

### Calculations
- None

### Workflow
Built → UAT → Approved → Production

### Search Requirements
- Releases

### Documents
- Release notes

### Reports
- Release history

### Notifications
- Release notices

### Security
- Hardened servers

### Integrations
- SDC

### Dependencies
- SDC provisioning

### Assumptions
- SDC provides servers, network and storage

### Risks
- SDC provisioning delays

### Non Functional Requirements
- Release under 1 hour

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Release register | Easy | 4 |
| API | Deployment pipeline | Complex | 8 |
| API | Configuration management | Medium | 6 |
| API | Hardening automation | Medium | 6 |
| Database | Release register | Simple | 1 |
| Testing | Deployment and rollback tests | Medium | 6 |
| Documentation | Deployment architecture and server requirements document | Complex | 4 |
| Documentation | Release runbook | Medium | 3 |

**Feature Total: 38 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 20 | 1 | 0 | 6 | 7 | **38** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
