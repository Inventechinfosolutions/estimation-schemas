# F16-004 — DPDP Compliance & Aadhaar Data Vault

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F16-004 |
| Feature Name | DPDP Compliance & Aadhaar Data Vault |
| Module | 16 — Security, Audit & Compliance |
| Module Type | Technical |
| Release | Go-live |

### Description
DPDP Act controls: consent notices and records, purpose tagging, data principal request handling (access, correction, grievance), masking and minimisation, retention and deletion schedules, breach logging, and an Aadhaar Data Vault storing Aadhaar numbers encrypted with reference tokens.

### Business Objective
Comply with DPDP Act and UIDAI regulations.

### Actors
- Candidate
- Data Protection Officer

### User Journey
1. **Who creates:** Candidates raise requests from their account.
2. **How they create:** Candidate selects request type.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Requests go to the DPO.
5. **How the approver sees pending items:** DPO sees requests with deadlines.
6. **How the approver decides:** DPO resolves.
7. **How the applicant / maker sees history:** Candidates see status.
8. **How the approver / auditor sees history:** Auditors see request handling.

### Functional Capabilities
- Consent register
- Data principal requests
- Masking
- Retention schedules
- Breach log
- Aadhaar Data Vault

### UI Screens
- Privacy request form
- DPO request queue
- Retention settings

### Logical API Operations
- Consent register
- Privacy request workflow
- Retention and deletion job
- Aadhaar vault store / token

### Inputs
- Requests

### Outputs
- Resolutions

### Business Rules
- Aadhaar numbers only in vault

### Validations
- Identity verification

### Calculations
- Deadlines

### Workflow
Open → Resolved

### Search Requirements
- Requests

### Documents
- None

### Reports
- Privacy requests

### Notifications
- Request updates

### Security
- Vault separate keys

### Integrations
- None

### Dependencies
- F16-001
- F15-003

### Assumptions
- DPO nominated by KEONICS

### Risks
- Rules evolving

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Privacy request form | Easy | 4 |
| UI | DPO request queue | Medium | 6 |
| UI | Retention settings | Easy | 4 |
| API | Consent register | Easy | 4 |
| API | Privacy request workflow | Medium | 6 |
| API | Retention and deletion job | Medium | 6 |
| API | Aadhaar vault store / token | Complex | 8 |
| Database | Privacy records and vault | Medium | 4 |
| Testing | Privacy and vault tests | Medium | 6 |
| Documentation | Privacy notice and DPDP compliance note | Easy | 2 |

**Feature Total: 50 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 24 | 4 | 0 | 6 | 2 | **50** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
