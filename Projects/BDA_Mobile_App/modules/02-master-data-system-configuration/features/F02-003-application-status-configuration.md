# F02-003 — Application Status Configuration

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-003 |
| Feature Name | Application Status Configuration |
| Module | 02 — Master Data & System Configuration |
| Description | Maintain application statuses: Draft, Submitted, Returned, Verified, Rejected. |
| Business Objective | Keep CDR application lifecycle statuses configurable and consistent. |
| Actors | Super Admin |

### User Journey

- Super Admin reviews/maintains status codes used across mobile and CAO flows.

### Functional Capabilities

- Status list aligned to lifecycle
- Labels for display

### Inputs

- Status code
- Label

### Outputs

- Status catalogue

### Business Rules

- Baseline statuses required for Phase 1

### Validations

- System statuses not deletable if in use

### Calculations

- None

### Workflow

- Draft→Submitted→Returned/Verified/Rejected

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Super Admin

### Integrations

- None

### Dependencies

- F01-001

### Assumptions

- Baseline five statuses

### Risks

- Renaming confuses users mid-flight

### Non Functional Requirements

- Stable codes for integrations later

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Status master screen | Easy | 4 |
| API | Status master CRUD | Easy | 4 |
| Database | Persistence / constraints for this feature | Simple | 1 |
| Testing | Feature test coverage | Easy | 4 |
| Documentation | Feature documentation | Simple | 1 |

**Feature Total: 14 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
