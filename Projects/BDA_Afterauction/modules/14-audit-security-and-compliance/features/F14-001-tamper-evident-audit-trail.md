# F14-001 — Tamper-Evident Audit Trail

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F14-001 |
| Feature Name | Tamper-Evident Audit Trail |
| Module | 14 — Audit, Security & Compliance |
| Module Type | Technical |
| Release | Go-live |

### Description
Audit trail of every create, update, delete, view of sensitive data, approval, signature, login and configuration change, with before / after values, user, role, IP, device and NTP-sourced timestamp, chained by cryptographic hashes so that any alteration is detectable, and read-only for every role including Super Admin.

### Business Objective
Meet the RFP requirement of a tamper-evident audit trail suitable for Section 63 certification.

### Actors
- System

### User Journey
1. **Who creates:** Audit records are created by the system for every action.
2. **How they create:** Each action writes an audit record with hash of the previous record.
3. **How they edit:** Records cannot be edited or deleted by anyone.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors view and verify records in F14-002.

### Functional Capabilities
- Central audit library used by all modules
- Before / after values
- Hash chaining (SHA-256)
- NTP time synchronisation
- Append-only storage
- Periodic anchoring of chain hash

### UI Screens
- None (no user interface in this feature)

### Logical API Operations
- Write audit record with hash chain
- Capture before / after values
- Periodic chain anchoring job
- NTP time source check

### Inputs
- Actions

### Outputs
- Audit records

### Business Rules
- No update / delete on audit store
- Audit write failure blocks the action

### Validations
- Time sync

### Calculations
- Hash = SHA-256(previous hash + record)

### Workflow
Written → Anchored

### Search Requirements
- Via F14-002

### Documents
- None

### Reports
- Via F14-002

### Notifications
- Alert on time sync failure

### Security
- Database permissions deny update / delete

### Integrations
- NTP

### Dependencies
- All modules

### Assumptions
- NTP source available in hosting

### Risks
- Storage growth; partitioning

### Non Functional Requirements
- Audit write under 20 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Write audit record with hash chain | Complex | 8 |
| API | Capture before / after values | Medium | 6 |
| API | Periodic chain anchoring job | Medium | 6 |
| API | NTP time source check | Easy | 4 |
| Database | Append-only audit store with partitioning | Complex | 6 |
| Testing | Audit coverage and tamper detection tests | Complex | 8 |
| Documentation | Audit design note | Medium | 3 |

**Feature Total: 41 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 24 | 6 | 0 | 8 | 3 | **41** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Core library rated Complex
- No external integration channel in this feature; Integration row omitted.
