# F16-002 — Tamper-Evident Audit Trail

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F16-002 |
| Feature Name | Tamper-Evident Audit Trail |
| Module | 16 — Security, Audit & Compliance |
| Module Type | Technical |
| Release | Go-live |

### Description
Central audit service recording events in the Annexure 9 JSON structure (event ID, timestamp, category, type, severity, user, role, session, IP, device, user agent, test ID, registration number, centre, terminal, event data, security event data), hash-chained and write-once, with viewer filtered by centre, IP and candidate, integrity verification, export, and retention.

### Business Objective
Provide complete audit trails as required by the RFP.

### Actors
- Auditor
- Super Admin
- EMU

### User Journey
1. **Who creates:** Events are written by all modules.
2. **How they create:** Not applicable.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Auditors see events.
6. **How the approver decides:** Auditors export evidence.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Integrity verification reports available.

### Functional Capabilities
- Annexure 9 schema
- Hash chain
- Write-once store
- Viewer with filters by centre, IP, candidate
- Integrity verification
- Export
- Retention

### UI Screens
- Audit viewer
- Integrity verification report

### Logical API Operations
- Audit event intake (high volume)
- Audit search
- Integrity verification
- Export

### Inputs
- Events

### Outputs
- Audit records

### Business Rules
- No role can modify or delete audit records

### Validations
- Schema

### Calculations
- Hash chain

### Workflow
Not applicable

### Search Requirements
- By centre, IP, candidate, time

### Documents
- Exports

### Reports
- Audit reports

### Notifications
- Integrity failure alert

### Security
- Read-only

### Integrations
- None

### Dependencies
- All modules

### Assumptions
- None

### Risks
- Volume during sessions

### Non Functional Requirements
- 10,000 events per second ingestion

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Audit viewer | Medium | 6 |
| UI | Integrity verification report | Easy | 4 |
| API | Audit event intake (high volume) | Very High | 16 |
| API | Audit search | Medium | 6 |
| API | Integrity verification | Medium | 6 |
| API | Export | Easy | 4 |
| Database | Audit store (partitioned, hash-chained) | Complex | 6 |
| Testing | Audit completeness and tamper tests | Complex | 8 |
| Documentation | Audit event catalogue | Medium | 3 |

**Feature Total: 59 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 32 | 6 | 0 | 8 | 3 | **59** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- High-volume intake rated Very High
- No external integration channel in this feature; Integration row omitted.
