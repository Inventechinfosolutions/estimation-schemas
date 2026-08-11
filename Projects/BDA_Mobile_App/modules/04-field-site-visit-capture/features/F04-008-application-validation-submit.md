# F04-008 — Application Validation & Submit

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-008 |
| Feature Name | Application Validation & Submit |
| Module | 04 — Field Site Visit Capture |
| Description | Validate mandatory data/media and submit application to CAO queue. |
| Business Objective | Ensure only complete CDR applications reach CAO. |
| Actors | Engineer |

### User Journey

- Engineer taps submit → validations run → on success status Submitted and locked for edit unless returned.

### Functional Capabilities

- Validate mandatory fields/media
- Submit to CAO
- Lock after submit

### Inputs

- Draft application

### Outputs

- Submitted application in CAO queue

### Business Rules

- Width, Check Bandi ack, surroundings, media rules mandatory
- Geo enforcement on submit

### Validations

- Show all validation errors

### Calculations

- None

### Workflow

- Draft → Submitted

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Engineer owner only

### Integrations

- None

### Dependencies

- F04-001
- F04-002
- F04-003
- F04-004
- F04-005
- F04-006
- F04-007
- F03-004

### Assumptions

- CAO queue consumes Submitted

### Risks

- Partial submit confusion

### Non Functional Requirements

- Atomic submit

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Submit & validation summary mobile UI | Medium | 6 |
| API | Validate and submit application | Complex | 8 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 26 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
