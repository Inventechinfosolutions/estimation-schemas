# F02-002 — Site Visit Attribute Masters

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-002 |
| Feature Name | Site Visit Attribute Masters |
| Module | 02 — Master Data & System Configuration |
| Description | Maintain dropdown/coded values for CDR capture: site category/type, shape, road type, surrounding feature types. |
| Business Objective | Standardize field capture values for consistent CDR records. |
| Actors | Super Admin |

### User Journey

- Super Admin maintains attribute lists → engineers select values on mobile forms.

### Functional Capabilities

- Masters for category/type, shape (regular/odd), road type, surrounding types
- Activate/deactivate codes

### Inputs

- Code
- Label
- Master type
- Status

### Outputs

- Coded lists for capture

### Business Rules

- Inactive codes not offered on new captures

### Validations

- Unique code per master type

### Calculations

- None

### Workflow

- None

### Search Requirements

- Filter by master type

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

- Final code lists agreed in workshops

### Risks

- Incomplete lists block capture

### Non Functional Requirements

- Synced to mobile for online use

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Attribute master admin screens | Complex | 8 |
| API | Attribute master CRUD by type | Medium | 6 |
| Database | Persistence / constraints for this feature | Medium | 4 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 27 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
