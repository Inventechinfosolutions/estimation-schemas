# F04-006 — Differently-Abled Candidate Support Requests

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-006 |
| Feature Name | Differently-Abled Candidate Support Requests |
| Module | 04 — Candidate Registration & eKYC |
| Module Type | Business |
| Release | Go-live |

### Description
Differently-abled candidates request scribe, guardian or helper and compensatory time as per Government Order, upload disability certificate; officers verify and approve; approved support is reflected in seat allocation, hall ticket and exam timer.

### Business Objective
Provide inclusive access as required by the RFP.

### Actors
- Candidate
- Scrutiny Officer
- Proctor

### User Journey
1. **Who creates:** The candidate raises the request during registration or before booking.
2. **How they create:** The candidate selects support type and uploads the certificate.
3. **How they edit:** The candidate edits before decision.
4. **How they send for approval:** Request goes to the Scrutiny Officer.
5. **How the approver sees pending items:** The officer sees pending requests.
6. **How the approver decides:** The officer approves (with support details) or rejects.
7. **How the applicant / maker sees history:** The candidate sees approval on dashboard and hall ticket.
8. **How the approver / auditor sees history:** Proctors see approved support for their session.

### Functional Capabilities
- Support types: scribe, guardian, helper, extra time
- Certificate upload
- Approval
- Accessible seat flag
- Extra time applied to timer
- Proctor list of supported candidates

### UI Screens
- Support request form
- Officer review
- Proctor support list

### Logical API Operations
- Save support request
- Approve / reject
- Apply support to booking and timer

### Inputs
- Support type
- Certificate

### Outputs
- Approved support

### Business Rules
- Extra time per Government Order

### Validations
- Certificate mandatory

### Calculations
- Extra time minutes per hour

### Workflow
Requested → Approved / Rejected

### Search Requirements
- Requests by status

### Documents
- Disability certificate

### Reports
- Supported candidates

### Notifications
- Decision notice

### Security
- Sensitive data restricted

### Integrations
- None

### Dependencies
- F05-001
- F09-003

### Assumptions
- Government Order rules provided

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Support request form | Easy | 4 |
| UI | Officer review | Easy | 4 |
| UI | Proctor support list | Easy | 4 |
| API | Save support request | Easy | 4 |
| API | Approve / reject | Easy | 4 |
| API | Apply support to booking and timer | Medium | 6 |
| Database | Support requests | Easy | 2 |
| Testing | Support flow tests | Easy | 4 |
| Documentation | Support request guide | Simple | 1 |

**Feature Total: 33 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 14 | 2 | 0 | 4 | 1 | **33** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small
- No external integration channel in this feature; Integration row omitted.
