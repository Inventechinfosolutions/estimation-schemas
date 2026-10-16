# F07-002 — Case Re-assignment

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-002 |
| Feature Name | Case Re-assignment |
| Module | 07 — Case Forwarding & Deputy Secretary Processing |
| Module Type | Business |
| Release | Go-live |

### Description
Re-assignment of a case between DS offices by the Auction Admin, and between case workers within a DS office by the Deputy Secretary, with mandatory reason, optional approval, transfer of open tasks and timers, and complete assignment history.

### Business Objective
Allow workload balancing and jurisdiction corrections without losing history or control.

### Actors
- Auction Admin
- Deputy Secretary
- Case Worker

### User Journey
1. **Who creates:** The Auction Admin (between DS offices) or Deputy Secretary (within office) initiates re-assignment.
2. **How they create:** They select cases, choose the target DS office or case worker, enter reason and submit; bulk selection is supported.
3. **How they edit:** A pending re-assignment can be cancelled before approval.
4. **How they send for approval:** Inter-DS re-assignment can require approval by the receiving DS (configurable).
5. **How the approver sees pending items:** The receiving DS sees incoming re-assignment requests.
6. **How the approver decides:** The receiving DS accepts or declines with remarks.
7. **How the applicant / maker sees history:** Users see current and previous assignees in the case file.
8. **How the approver / auditor sees history:** Auditors see full assignment history.

### Functional Capabilities
- Inter-DS and intra-DS re-assignment
- Bulk re-assignment
- Optional acceptance by receiving DS
- Transfer of open tasks and timers
- Assignment history

### UI Screens
- Re-assignment dialog (single / bulk)
- Incoming re-assignment requests
- Assignment history

### Logical API Operations
- Request re-assignment
- Accept / decline re-assignment
- Transfer tasks and timers
- Assignment history
- Case worker allocation within DS

### Inputs
- Cases
- Target
- Reason

### Outputs
- Updated assignment
- History

### Business Rules
- Reason mandatory
- Cases in signing stage cannot be moved until signing completes

### Validations
- Target active

### Calculations
- None

### Workflow
Requested → Accepted → Re-assigned | Declined

### Search Requirements
- By case, DS, assignee

### Documents
- None

### Reports
- Re-assignment report

### Notifications
- To both offices and new assignee

### Security
- Role-restricted

### Integrations
- None

### Dependencies
- F07-001
- F01-003

### Assumptions
- None

### Risks
- None significant

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Re-assignment dialog (single / bulk) | Medium | 6 |
| UI | Incoming re-assignment requests | Easy | 4 |
| UI | Assignment history | Simple | 2 |
| API | Request re-assignment | Medium | 6 |
| API | Accept / decline re-assignment | Easy | 4 |
| API | Transfer tasks and timers | Medium | 6 |
| API | Assignment history | Simple | 2 |
| API | Case worker allocation within DS | Easy | 4 |
| Database | Assignment history | Easy | 2 |
| Testing | Re-assignment and isolation tests | Medium | 6 |
| Documentation | Re-assignment guide | Simple | 1 |

**Feature Total: 43 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 22 | 2 | 0 | 6 | 1 | **43** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Moderate workflow
- No external integration channel in this feature; Integration row omitted.
