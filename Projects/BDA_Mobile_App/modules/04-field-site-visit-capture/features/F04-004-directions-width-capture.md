# F04-004 — Directions & Width Capture

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-004 |
| Feature Name | Directions & Width Capture |
| Module | 04 — Field Site Visit Capture |
| Description | Capture narrative directions and mandatory approach/road width (optional road type/landmark). |
| Business Objective | Document how to reach the site and approach width for CDR. |
| Actors | Engineer |

### User Journey

- Engineer enters directions → optional landmark → mandatory width with unit → optional road type.

### Functional Capabilities

- Narrative directions
- Mandatory width + unit
- Optional landmark and road type

### Inputs

- Directions text
- Width
- Unit
- Road type

### Outputs

- Directions/width on application

### Business Rules

- Width mandatory at submit

### Validations

- Numeric width > 0

### Calculations

- None

### Workflow

- Part of draft/submit

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Engineer

### Integrations

- None

### Dependencies

- F04-001
- F02-002

### Assumptions

- Unit ft/m configurable

### Risks

- Incorrect width entry

### Non Functional Requirements

- Mobile friendly form

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Directions & width mobile section | Medium | 6 |
| API | Save directions & width | Medium | 6 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 22 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
