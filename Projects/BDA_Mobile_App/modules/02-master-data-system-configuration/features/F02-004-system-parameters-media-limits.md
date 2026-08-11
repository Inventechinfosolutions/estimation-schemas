# F02-004 — System Parameters & Media Limits

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-004 |
| Feature Name | System Parameters & Media Limits |
| Module | 02 — Master Data & System Configuration |
| Description | Configure OTP validity, photo count/size (default 10 / 10 MB), video max size, session timeout, PDF template metadata. |
| Business Objective | Allow BDA to tune OTP and media rules without code change. |
| Actors | Super Admin |

### User Journey

- Super Admin opens parameters → updates limits → saves; mobile/web enforce new values.

### Functional Capabilities

- OTP parameters
- Media limits
- Session timeout
- PDF template version metadata

### Inputs

- Parameter key/value

### Outputs

- Effective system parameters

### Business Rules

- Photo max count default 10
- Photo max size default 10 MB
- Video default 50 MB unless changed

### Validations

- Numeric ranges validated

### Calculations

- None

### Workflow

- None

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

- Defaults from SOW until changed

### Risks

- Too-low limits block field capture

### Non Functional Requirements

- Parameters cached with refresh

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | System parameters screen | Medium | 6 |
| API | Read/update parameters | Medium | 6 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 22 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
