# F06-001 — Field task & checklist inbox

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-001 |
| Feature Name | Field task & checklist inbox |
| Module | 06 — Mobile Field Application |
| Description | View and update assigned field tasks and checklists on mobile |
| Business Objective | Give field personnel a single mobile inbox for campaign assignments and on-site checklist work. |
| Actors | Field Personnel; System |

### User Journey

- Field user opens mobile app → sees assigned tasks grouped by campaign/site → opens a task → completes checklist items → submits progress for sync.

### Functional Capabilities

- Assigned task list with status filters (pending, in progress, completed)
- Checklist item capture (yes/no, notes, mandatory photo where configured)
- Link from task to related PoD capture when required
- Pull-to-refresh when online

### Inputs

User session; assignment identifiers; checklist responses; optional notes

### Outputs

Updated task/checklist status visible to verifiers on web

### Business Rules

Only tasks assigned to the logged-in field user are shown
Completed mandatory checklist items required before PoD submission where configured

### Validations

Mandatory checklist fields enforced
Task must be in an updatable status

### Calculations

- None

### Workflow

- N/A

### Search Requirements

Filter by campaign, site, due date, and status on mobile inbox

### Documents

- None

### Reports

- None

### Notifications

New assignments surfaced via Module 08 in-app/mobile alerts

### Security

Field role RBAC; device-bound session from F06-005

### Integrations

Consumes campaign/task data from platform services (Modules 03, 05)

### Dependencies

F06-005; Modules 03, 05; Module 08 for assignment alerts

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | AMT Field Home with sync badge and assignment summary | Easy | 4 |
| UI | Field task inbox list with campaign/site/status filters | Complex | 12 |
| UI | Task detail header with due date and campaign context | Medium | 6 |
| UI | Checklist step panel with mandatory item markers | Medium | 6 |
| UI | Checklist item capture (yes/no, notes, optional photo gate) | Medium | 6 |
| UI | PoD launch shortcut from task when configured | Simple | 2 |
| UI | Pull-to-refresh and empty-state offline hint panel | Easy | 4 |
| API | List assigned field tasks with filters | Medium | 6 |
| API | Fetch task detail and checklist definition | Easy | 4 |
| API | Submit checklist item responses batch | Medium | 6 |
| API | Mark task in-progress/completed transitions | Easy | 4 |
| API | Validate mandatory checklist before PoD eligibility | Complex | 8 |
| Database | Checklist response progress store | Easy | 2 |
| Database | Task status transition audit fields | Easy | 2 |
| Testing | Assigned-only visibility and filter scenarios | Medium | 6 |
| Testing | Mandatory checklist negative before PoD | Medium | 6 |
| Testing | Checklist completion happy path | Easy | 4 |
| Documentation | Field inbox operator guide | Easy | 2 |
| Documentation | Checklist completion business rules appendix | Easy | 2 |

**Feature Total: 92 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
