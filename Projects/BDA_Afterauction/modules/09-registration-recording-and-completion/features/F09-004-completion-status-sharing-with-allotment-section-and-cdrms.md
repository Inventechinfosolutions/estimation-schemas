# F09-004 — Completion Status Sharing with Allotment Section & CDRMS

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-004 |
| Feature Name | Completion Status Sharing with Allotment Section & CDRMS |
| Module | 09 — Registration Recording & Completion |
| Module Type | Business |
| Release | Go-live |

### Description
Outbound update of site status to CDRMS (completed, cancelled, returned for re-auction) through API, with acknowledgement, retry and reconciliation, and intimation to the allotment section.

### Business Objective
Keep BDA's site master accurate without manual updates.

### Actors
- System
- Auction Admin

### User Journey
1. **Who creates:** The system sends updates automatically on completion or cancellation.
2. **How they create:** The connector posts status to CDRMS and records acknowledgement.
3. **How they edit:** Not editable; failed updates are retried.
4. **How they send for approval:** No approval.
5. **How the approver sees pending items:** The Auction Admin sees failed updates in the integration error queue.
6. **How the approver decides:** The Auction Admin retries or marks as manually updated with reference.
7. **How the applicant / maker sees history:** Users see the update status in the case file.
8. **How the approver / auditor sees history:** Auditors see requests and acknowledgements.

### Functional Capabilities
- Status update API client
- Acknowledgement and retry
- Monthly reconciliation of statuses
- Allotment section intimation

### UI Screens
- CDRMS update status list
- Status reconciliation report

### Logical API Operations
- Post status to CDRMS
- Handle acknowledgement
- Retry failed updates
- Reconcile statuses

### Inputs
- Status events

### Outputs
- CDRMS updates

### Business Rules
- Idempotent updates

### Validations
- Acknowledgement received

### Calculations
- None

### Workflow
Queued → Sent → Acknowledged | Failed → Retried

### Search Requirements
- By site and status

### Documents
- None

### Reports
- Update reconciliation

### Notifications
- Intimation to allotment section

### Security
- Service credentials

### Integrations
- CDRMS

### Dependencies
- F09-003
- F06-008
- F04-005
- F13-001

### Assumptions
- CDRMS update API available

### Risks
- CDRMS changes

### Non Functional Requirements
- Update within 15 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | CDRMS update status list | Easy | 4 |
| UI | Status reconciliation report | Easy | 4 |
| API | Post status to CDRMS | Medium | 6 |
| API | Handle acknowledgement | Easy | 4 |
| API | Retry failed updates | Easy | 4 |
| API | Reconcile statuses | Medium | 6 |
| Database | Update log | Simple | 1 |
| Integration | CDRMS site status update API | Medium | 16 |
| Testing | Update and retry tests | Medium | 6 |
| Documentation | CDRMS update interface note | Easy | 2 |

**Feature Total: 53 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 20 | 1 | 16 | 6 | 2 | **53** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- One Medium integration row
