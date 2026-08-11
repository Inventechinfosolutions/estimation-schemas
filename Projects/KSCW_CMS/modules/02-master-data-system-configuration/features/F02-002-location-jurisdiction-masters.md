# F02-002 — Location / Jurisdiction Masters

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-002 |
| Feature Name | Location / Jurisdiction Masters |
| Module | 02 — Master Data & System Configuration |
| Description | Maintain location / jurisdiction hierarchy used for complaint routing and MIS. |
| Business Objective | Enable consistent geo/jurisdiction referencing across channels and reports. |
| Actors | Admin |

### User Journey

- Admin maintains location hierarchy → links child jurisdictions → activates codes for intake and routing.

### Functional Capabilities

- Hierarchical location master maintenance
- Search and activate/deactivate locations

### Inputs

- Location code/name
- Parent location
- Status

### Outputs

- Jurisdiction tree for intake, routing, dashboards

### Business Rules

- Hierarchy depth as approved in FRS
- Inactive locations excluded from new routing

### Validations

- Unique code
- Valid parent reference

### Calculations

- None

### Workflow

- Maintain hierarchy → consume in Modules 03–07

### Search Requirements

- By name, code, parent, status

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

- KSCW supplies jurisdiction list

### Risks

- Incomplete hierarchy delays routing rules

### Non Functional Requirements

- Efficient tree/list load for large master

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Location hierarchy tree/list and edit form | Complex | 8 |
| API | Location CRUD and hierarchy lookup | Medium | 6 |
| Database | Location hierarchy with indexes and FK integrity | Complex | 6 |
| Testing | Hierarchy CRUD and inactive exclusion | Medium | 6 |
| Documentation | Location master notes | Easy | 2 |

**Feature Total: 28 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
