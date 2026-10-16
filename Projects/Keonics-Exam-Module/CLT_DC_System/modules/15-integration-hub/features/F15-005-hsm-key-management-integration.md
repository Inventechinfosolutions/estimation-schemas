# F15-005 — HSM Key Management Integration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F15-005 |
| Feature Name | HSM Key Management Integration |
| Module | 15 — Integration Hub |
| Module Type | Technical |
| Release | Go-live |

### Description
Integration with the CeG Hardware Security Module (PKCS#11 / KMIP or REST) for master key storage, data key wrapping, signing of result files and hall ticket tokens, key rotation and access logging.

### Business Objective
Protect encryption keys as required by the RFP.

### Actors
- System
- Security Officer

### User Journey
1. **Who creates:** Keys created by the Security Officer.
2. **How they create:** Keys generated inside HSM.
3. **How they edit:** Rotation scheduled.
4. **How they send for approval:** Rotation requires dual control.
5. **How the approver sees pending items:** Second officer sees rotation request.
6. **How the approver decides:** Second officer approves.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see key operations.

### Functional Capabilities
- PKCS#11 / KMIP client
- Key hierarchy (master, data keys)
- Wrapping and unwrapping
- Signing
- Rotation with dual control
- Operation logs

### UI Screens
- Key management console

### Logical API Operations
- HSM client adapter
- Data key wrap / unwrap
- Sign operations
- Rotation workflow

### Inputs
- Key requests

### Outputs
- Wrapped keys, signatures

### Business Rules
- Master keys never leave HSM
- Dual control

### Validations
- Access policies

### Calculations
- None

### Workflow
Active → Rotated → Retired

### Search Requirements
- Keys

### Documents
- None

### Reports
- Key operations

### Notifications
- Rotation reminders

### Security
- HSM partitions

### Integrations
- HSM

### Dependencies
- F15-001
- F16-001

### Assumptions
- CeG provides HSM partition and client

### Risks
- HSM availability during sessions

### Non Functional Requirements
- Under 50 ms per operation

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Key management console | Medium | 6 |
| API | HSM client adapter | Complex | 8 |
| API | Data key wrap / unwrap | Medium | 6 |
| API | Sign operations | Medium | 6 |
| API | Rotation workflow | Medium | 6 |
| Database | Key metadata | Easy | 2 |
| Integration | CeG HSM | Complex | 24 |
| Testing | HSM integration and failover tests | Complex | 8 |
| Documentation | Key management procedure | Easy | 2 |

**Feature Total: 68 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 26 | 2 | 24 | 8 | 2 | **68** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Security-critical
