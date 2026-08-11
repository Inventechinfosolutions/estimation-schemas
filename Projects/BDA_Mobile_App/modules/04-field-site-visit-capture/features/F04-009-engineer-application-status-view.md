# F04-009 — Engineer Application Status View

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-009 |
| Feature Name | Engineer Application Status View |
| Module | 04 — Field Site Visit Capture |
| Description | Engineer views own applications and statuses. |
| Business Objective | Give engineers visibility of draft/submitted/returned/verified/rejected items. |
| Actors | Engineer |

### User Journey

- Engineer opens My Applications → filters by status → opens detail.

### Functional Capabilities

- List own applications
- Status display
- Open returned for edit

### Inputs

- Status filter

### Outputs

- Application list/detail

### Business Rules

- Only own applications

### Validations

- None

### Calculations

- None

### Workflow

- Reflects latest status

### Search Requirements

- By status, date, application number

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Owner only

### Integrations

- None

### Dependencies

- F04-001
- F05-003

### Assumptions

- Statuses from master

### Risks

- Stale list if offline — N/A online-only

### Non Functional Requirements

- Responsive list

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | My applications list/detail mobile | Easy | 4 |
| API | List/get own applications | Medium | 6 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Easy | 4 |
| Documentation | Feature documentation | Simple | 1 |

**Feature Total: 17 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
