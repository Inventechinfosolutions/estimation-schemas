# F04-003 — Worklist & Assignment

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-003 |
| Feature Name | Worklist & Assignment |
| Module | 04 — Categorization, Auto-Routing & Assignment |
| Description | Present routed complaints in Supervisor/Operator worklists and support assignment. |
| Business Objective | Give staff a clear queue of work to process. |
| Actors | Supervisor; Operator |

### User Journey

- User opens worklist → filters pending items → opens complaint → assigns/claims as permitted.

### Functional Capabilities

- Role-based worklist
- Claim/assign actions
- Filters by status, SLA risk, category, location

### Inputs

- Filters
- Assignee selection

### Outputs

- Worklist view
- Assignment on complaint

### Business Rules

- Operators see assigned/allowed queues only
- Supervisors may assign within jurisdiction/rules

### Validations

- Assignee must have capacity/role

### Calculations

- None

### Workflow

- Route → appear in list → assign/claim → process in Module 05

### Search Requirements

- Reference, complainant, status, category, location, assignee

### Documents

- None

### Reports

- None

### Notifications

- Assignment notify via Module 06 if configured

### Security

- RBAC on worklist scope

### Integrations

- None

### Dependencies

- F04-002
- Module 01

### Assumptions

- Dashboard Design / UI-UX confirms columns

### Risks

- Large queues need pagination/performance tuning

### Non Functional Requirements

- Responsive list performance

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Supervisor/Operator worklist with filters and claim/assign | Very High | 16 |
| API | Worklist query and assignment actions | Complex | 8 |
| Database | Assignment fields and worklist indexes | Medium | 4 |
| Testing | Queue scoping and assignment cases | Complex | 8 |
| Documentation | Worklist feature notes | Easy | 2 |

**Feature Total: 38 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
