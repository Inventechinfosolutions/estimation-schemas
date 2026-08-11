# F05-004 — Resolution & Closure

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-004 |
| Feature Name | Resolution & Closure |
| Module | 05 — Workflow Automation, Escalation & SLA Tracking |
| Description | Resolve and close complaints with reasons and evidence as configured. |
| Business Objective | Complete the complaint lifecycle with accountable closure. |
| Actors | Operator; Supervisor |

### User Journey

- Assignee completes work → selects resolve/close → enters reason and evidence → complaint closed → complainant notified if configured.

### Functional Capabilities

- Resolve/close action form
- Closure reason codes
- Evidence attachment at closure

### Inputs

- Closure reason
- Remarks
- Evidence files

### Outputs

- Closed complaint
- Closure record

### Business Rules

- Mandatory reason
- Supervisor approval if FRS requires for certain categories

### Validations

- Reason required
- Stage allows closure

### Calculations

- None

### Workflow

- Eligible stage → close → stop SLA → notify

### Search Requirements

- Closed complaints by date/reason

### Documents

- Closure evidence

### Reports

- Feeds MIS

### Notifications

- Closure notify via Module 06

### Security

- Role-gated closure

### Integrations

- None

### Dependencies

- F05-001
- F03-006
- Module 06

### Assumptions

- Closure reason master in F02-005 or embedded list

### Risks

- Premature closure without evidence

### Non Functional Requirements

- Immutable closure audit

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Resolve/close form with reason and evidence | Complex | 8 |
| API | Closure transaction stopping SLA and writing history | Complex | 8 |
| Database | Closure reason and evidence links | Medium | 4 |
| Testing | Closure permission and mandatory reason cases | Medium | 6 |
| Documentation | Resolution & closure notes | Easy | 2 |

**Feature Total: 28 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
