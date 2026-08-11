# F02-005 — Status & Parameter Configuration

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-005 |
| Feature Name | Status & Parameter Configuration |
| Module | 02 — Master Data & System Configuration |
| Description | Configure complaint statuses and system parameters used across CMS. |
| Business Objective | Keep lifecycle statuses and operational parameters configurable. |
| Actors | Admin |

### User Journey

- Admin maintains status list and system parameters → saves → transactional modules consume values.

### Functional Capabilities

- Complaint status master maintenance
- System parameter key/value configuration

### Inputs

- Status code/name
- Parameter key/value
- Status flags

### Outputs

- Active statuses and parameters

### Business Rules

- Reserved system statuses not deletable if FRS marks them
- Parameter changes apply per FRS effective rules

### Validations

- Unique status codes
- Typed parameter values

### Calculations

- None

### Workflow

- Configure → consume in Modules 03–07

### Search Requirements

- By status/parameter name

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Admin only

### Integrations

- None

### Dependencies

- Module 01

### Assumptions

- FRS defines mandatory status set

### Risks

- Ad-hoc status proliferation without governance

### Non Functional Requirements

- Cached reads for hot parameters

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Status master and system parameter screens | Medium | 6 |
| API | Status/parameter CRUD | Easy | 4 |
| Database | Status and parameter tables | Easy | 2 |
| Testing | Status/parameter update cases | Easy | 4 |
| Documentation | Parameter config notes | Easy | 2 |

**Feature Total: 18 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
