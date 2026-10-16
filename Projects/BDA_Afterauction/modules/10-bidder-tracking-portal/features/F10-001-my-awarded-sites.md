# F10-001 — My Awarded Sites

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-001 |
| Feature Name | My Awarded Sites |
| Module | 10 — Bidder Tracking Portal |
| Module Type | Business |
| Release | Go-live |

### Description
Bidder portal home listing all sites awarded to the bidder across auctions, with site number, layout, auction date, bid amount, current stage, next action and amount due, with search and filters.

### Business Objective
Give bidders an at-a-glance view of all their sites and pending actions.

### Actors
- Successful Bidder

### User Journey
1. **Who creates:** Sites are linked automatically on award (F05-001).
2. **How they create:** The bidder logs in and sees My Sites.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The bidder sees all current and completed sites.
8. **How the approver / auditor sees history:** Auditors see bidder access logs.

### Functional Capabilities
- Site cards with stage and next action
- Search and filters
- Pending action highlights
- Completed / cancelled tabs

### UI Screens
- My Sites dashboard
- Site list with filters

### Logical API Operations
- List bidder sites with stage and dues
- Compute next action

### Inputs
- Filters

### Outputs
- Site list

### Business Rules
- Own sites only

### Validations
- Session valid

### Calculations
- Amount due

### Workflow
Not applicable

### Search Requirements
- By site, layout, stage

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Bidder isolation

### Integrations
- None

### Dependencies
- F05-001
- F06-005

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Loads within 3 seconds on mobile

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | My Sites dashboard | Medium | 6 |
| UI | Site list with filters | Easy | 4 |
| API | List bidder sites with stage and dues | Medium | 6 |
| API | Compute next action | Medium | 6 |
| Testing | Bidder site list tests | Easy | 4 |
| Documentation | Bidder portal help: My Sites | Simple | 1 |

**Feature Total: 27 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 12 | 0 | 0 | 4 | 1 | **27** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Read-only views
- No external integration channel in this feature; Integration row omitted.
