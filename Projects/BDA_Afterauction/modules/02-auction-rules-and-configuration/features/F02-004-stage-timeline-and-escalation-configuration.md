# F02-004 — Stage Timeline & Escalation Configuration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-004 |
| Feature Name | Stage Timeline & Escalation Configuration |
| Module | 02 — Auction Rules & Configuration |
| Module Type | Business |
| Release | Go-live |

### Description
Configuration of time limits for each stage of the eleven-stage process and for each task type, with working-day or calendar-day basis, reminder points, escalation levels and escalation recipients.

### Business Objective
Make pendency visible and drive timely action by the responsible officer, with automatic escalation when limits are crossed.

### Actors
- Auction Admin
- Approving Authority (approval)

### User Journey
1. **Who creates:** The Auction Admin sets stage timelines and escalation rules.
2. **How they create:** The Auction Admin opens Timelines, selects a stage or task type, enters the limit, day basis, reminder points and escalation chain, and saves as draft.
3. **How they edit:** The Auction Admin edits values; a preview shows due and escalation dates for a sample start date with holidays applied.
4. **How they send for approval:** The Auction Admin submits the configuration for approval.
5. **How the approver sees pending items:** The Approving Authority sees pending timeline changes.
6. **How the approver decides:** The Approving Authority approves or returns.
7. **How the applicant / maker sees history:** Officers see due dates and RAG status on their tasks.
8. **How the approver / auditor sees history:** Auditors see versions and which version applied to each task.

### Functional Capabilities
- Time limit per stage and task type
- Working-day calendar using holiday master; calendar-day option
- Reminder points (e.g., 50% and 80% of limit)
- Multi-level escalation chain by role
- Pause rules (e.g., waiting for bidder documents)
- Preview with holiday calendar
- Versioning and approval

### UI Screens
- Stage timeline list
- Timeline and escalation editor
- Preview with holidays
- Approval and versions

### Logical API Operations
- Save timeline draft
- Approve / return timelines
- Compute due and escalation dates
- Resolve pause rules
- Preview timeline

### Inputs
- Stage / task type
- Limit and basis
- Reminder points
- Escalation roles
- Pause conditions

### Outputs
- Active timelines
- Computed due and escalation dates

### Business Rules
- Escalation date must follow reminder dates
- Paused time is excluded from elapsed time
- New versions apply to tasks started after activation

### Validations
- Limits positive
- Escalation roles exist

### Calculations
- Due date = start + limit in working days excluding holidays and pause periods

### Workflow
Draft → Submitted → Active → Superseded

### Search Requirements
- Timelines by stage

### Documents
- None

### Reports
- Timeline configuration export

### Notifications
- Approval request and outcome

### Security
- Only Auction Admin edits

### Integrations
- None

### Dependencies
- F02-006 (holidays)
- F07-005
- F12-002

### Assumptions
- BDA provides target timelines per stage

### Risks
- Over-strict limits causing alert fatigue

### Non Functional Requirements
- Due date computation under 100 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Stage timeline list | Easy | 4 |
| UI | Timeline and escalation editor | Medium | 6 |
| UI | Preview with holidays | Easy | 4 |
| UI | Approval and versions | Easy | 4 |
| API | Save timeline draft | Medium | 6 |
| API | Approve / return timelines | Easy | 4 |
| API | Compute due and escalation dates | Complex | 8 |
| API | Resolve pause rules | Medium | 6 |
| API | Preview timeline | Easy | 4 |
| Database | Timeline and escalation configuration with versions | Easy | 2 |
| Testing | Due date calculation with holidays and pauses | Complex | 8 |
| Testing | Escalation chain configuration tests | Easy | 4 |
| Documentation | Timeline configuration guide | Easy | 2 |

**Feature Total: 62 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 28 | 2 | 0 | 12 | 2 | **62** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Working-day and pause-aware date engine rated Complex
- No external integration channel in this feature; Integration row omitted.
