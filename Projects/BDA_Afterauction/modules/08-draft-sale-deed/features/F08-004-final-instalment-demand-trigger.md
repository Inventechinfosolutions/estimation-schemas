# F08-004 — Final Instalment Demand Trigger

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-004 |
| Feature Name | Final Instalment Demand Trigger |
| Module | 08 — Draft Sale Deed |
| Module Type | Business |
| Release | Go-live |

### Description
Automatic raising of the final 25% instalment demand when the draft sale deed is approved (where configured), with due date computation, demand notice and bidder notification, and the 100% Payment Completed milestone on confirmed credit.

### Business Objective
Link the final payment to the draft deed stage as per BDA rules without manual steps.

### Actors
- System
- Finance Officer

### User Journey
1. **Who creates:** The system raises the demand on draft deed approval.
2. **How they create:** The event handler creates the demand from the schedule and generates the notice.
3. **How they edit:** Not editable; corrections via schedule revision.
4. **How they send for approval:** No approval.
5. **How the approver sees pending items:** The Finance Officer sees new final demands.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The bidder sees the demand.
8. **How the approver / auditor sees history:** Auditors see the trigger event.

### Functional Capabilities
- Event-based demand
- Notice generation
- Notification
- 100% milestone propagation

### UI Screens
- Final demand list

### Logical API Operations
- Handle draft-approved event
- Raise final demand
- Publish 100% milestone

### Inputs
- Approval event

### Outputs
- Final demand

### Business Rules
- Raise once per case

### Validations
- Schedule present

### Calculations
- Due date

### Workflow
Approved → Demand raised → Paid

### Search Requirements
- None

### Documents
- Demand notice

### Reports
- None

### Notifications
- Demand notice

### Security
- System

### Integrations
- None

### Dependencies
- F06-001
- F08-002

### Assumptions
- None

### Risks
- None significant

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Final demand list | Easy | 4 |
| API | Handle draft-approved event | Medium | 6 |
| API | Raise final demand | Easy | 4 |
| API | Publish 100% milestone | Easy | 4 |
| Testing | Trigger tests | Easy | 4 |
| Documentation | Note | Simple | 1 |

**Feature Total: 23 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 14 | 0 | 0 | 4 | 1 | **23** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small event handler
- No external integration channel in this feature; Integration row omitted.
