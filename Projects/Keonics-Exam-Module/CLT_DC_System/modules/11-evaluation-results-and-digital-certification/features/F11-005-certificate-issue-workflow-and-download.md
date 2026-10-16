# F11-005 — Certificate Issue Workflow & Download

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-005 |
| Feature Name | Certificate Issue Workflow & Download |
| Module | 11 — Evaluation, Results & Digital Certification |
| Module Type | Business |
| Release | Go-live |

### Description
Issue workflow as approved by KEONICS (bulk approval per session), release to candidate account with download on portal and app, e-mail / SMS notice, push of result and certificate reference to HRMS for employees, and duplicate certificate requests.

### Business Objective
Deliver certificates to candidates and update HRMS.

### Actors
- KEONICS Approver
- Candidate
- System

### User Journey
1. **Who creates:** Certificates arrive for issue after signing.
2. **How they create:** The approver reviews batch.
3. **How they edit:** Not editable.
4. **How they send for approval:** Batch issue needs approval.
5. **How the approver sees pending items:** The approver sees batches.
6. **How the approver decides:** The approver issues.
7. **How the applicant / maker sees history:** Candidates download certificates.
8. **How the approver / auditor sees history:** Auditors see issue and HRMS push logs.

### Functional Capabilities
- Batch issue approval
- Portal and app download
- Notifications
- HRMS push
- Duplicate requests
- Download log

### UI Screens
- Issue approval
- Candidate certificate download
- HRMS push status

### Logical API Operations
- Issue batch
- Download certificate
- Push result to HRMS
- Duplicate request

### Inputs
- Signed certificates

### Outputs
- Issued certificates
- HRMS updates

### Business Rules
- Employee certificates pushed to HRMS

### Validations
- None

### Calculations
- None

### Workflow
Signed → Issued → Pushed

### Search Requirements
- By candidate

### Documents
- Certificate

### Reports
- Issue status

### Notifications
- Certificate available notice

### Security
- Own certificates

### Integrations
- HRMS via F15-002

### Dependencies
- F11-004
- F15-002

### Assumptions
- HRMS accepts result push

### Risks
- HRMS availability

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Issue approval | Easy | 4 |
| UI | Candidate certificate download | Easy | 4 |
| UI | HRMS push status | Easy | 4 |
| API | Issue batch | Easy | 4 |
| API | Download certificate | Easy | 4 |
| API | Push result to HRMS | Medium | 6 |
| API | Duplicate request | Easy | 4 |
| Database | Issue and push log | Easy | 2 |
| Testing | Issue and HRMS push tests | Medium | 6 |
| Documentation | Certificate issue guide | Simple | 1 |

**Feature Total: 39 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 18 | 2 | 0 | 6 | 1 | **39** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
