# F04-004 — Reassignment / Reclassification

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-004 |
| Feature Name | Reassignment / Reclassification |
| Module | 04 — Categorization, Auto-Routing & Assignment |
| Description | Support controlled reassignment and reclassification with full history. |
| Business Objective | Correct routing/classification mistakes without losing audit trail. |
| Actors | Supervisor; Admin |

### User Journey

- Supervisor opens complaint → reclassifies and/or reassigns → enters reason → history updated → new queue notified.

### Functional Capabilities

- Reassign to another user/queue
- Reclassify taxonomy fields
- Mandatory reason and history trail

### Inputs

- New assignee/queue
- New classification
- Reason

### Outputs

- Updated assignment/classification
- History entry

### Business Rules

- Reason mandatory
- May re-trigger routing/SLA rules per FRS

### Validations

- Reason required
- Target valid

### Calculations

- None

### Workflow

- Select action → reason → apply → history

### Search Requirements

- History by complaint

### Documents

- None

### Reports

- None

### Notifications

- Notify new assignee if configured

### Security

- Supervisor/Admin only

### Integrations

- None

### Dependencies

- F04-001
- F04-002
- F04-003

### Assumptions

- FRS defines who may reclassify after stage X

### Risks

- Frequent reclass churn distorts SLA

### Non Functional Requirements

- Complete audit of each change

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Reassign/reclassify dialog with reason | Medium | 6 |
| API | Reassignment/reclassification transaction with history | Complex | 8 |
| Database | Transfer history entities | Medium | 4 |
| Testing | Reassign and reclassify audit cases | Medium | 6 |
| Documentation | Reassignment notes | Easy | 2 |

**Feature Total: 26 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
