# F01-003 — Engineer Credential & Geo Binding

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-003 |
| Feature Name | Engineer Credential & Geo Binding |
| Module | 01 — User & Access Management |
| Description | Provision engineer login credentials and bind each engineer to exactly one geo-location. |
| Business Objective | Enable field engineers to log in only for their assigned location. |
| Actors | Super Admin |

### User Journey

- Super Admin selects Engineer user → creates credentials → selects one geo-location → saves binding.

### Functional Capabilities

- Create engineer credentials
- Mandatory single geo-location assignment
- Change geo assignment with audit

### Inputs

- Engineer user
- Credential
- Geo-location

### Outputs

- Active engineer login bound to one geo

### Business Rules

- Engineer must have exactly one geo
- Cross-location write blocked using this binding

### Validations

- Geo mandatory for Engineer role

### Calculations

- None

### Workflow

- Provision → Active engineer

### Search Requirements

- Find engineers by geo

### Documents

- None

### Reports

- None

### Notifications

- Optional SMS of credentials — out of baseline

### Security

- Super Admin only
- Audit geo changes

### Integrations

- None

### Dependencies

- F01-001
- F01-002
- F02-001

### Assumptions

- Geo master populated before binding

### Risks

- Incorrect geo assignment blocks field work

### Non Functional Requirements

- Server-side enforcement of geo

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Engineer credential & geo binding screen | Medium | 6 |
| API | Provision credentials + geo bind | Medium | 6 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 22 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
