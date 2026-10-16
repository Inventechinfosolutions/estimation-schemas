# F13-004 — BDA Web GIS Map Integration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F13-004 |
| Feature Name | BDA Web GIS Map Integration |
| Module | 13 — Integration Hub |
| Module Type | Technical |
| Release | Go-live |

### Description
Integration with BDA Web GIS to display the location and boundary of awarded sites on maps in the case file, verification workbench and bidder portal, using site identifiers, with fallback to coordinates.

### Business Objective
Show site location visually to officials and bidders.

### Actors
- All staff roles
- Successful Bidder

### User Journey
1. **Who creates:** Maps are loaded by the system.
2. **How they create:** Users open the map tab.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Not applicable.

### Functional Capabilities
- Map widget
- Site boundary overlay
- Fallback to point location

### UI Screens
- Map widget

### Logical API Operations
- Fetch site geometry
- Cache geometry

### Inputs
- Site ID

### Outputs
- Map

### Business Rules
- Read-only

### Validations
- Geometry present

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Read-only access

### Integrations
- BDA Web GIS

### Dependencies
- F13-001

### Assumptions
- GIS service available

### Risks
- Missing geometries

### Non Functional Requirements
- Map loads within 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Map widget | Medium | 6 |
| API | Fetch site geometry | Medium | 6 |
| API | Cache geometry | Easy | 4 |
| Database | Geometry cache | Simple | 1 |
| Integration | BDA Web GIS service (WMS / WFS or API) | Medium | 16 |
| Testing | Map integration tests | Easy | 4 |
| Documentation | GIS interface note | Simple | 1 |

**Feature Total: 38 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 10 | 1 | 16 | 4 | 1 | **38** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- One Medium integration row
