# F10-002 — Awarded Site Details & Stage Tracker

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-002 |
| Feature Name | Awarded Site Details & Stage Tracker |
| Module | 10 — Bidder Tracking Portal |
| Module Type | Business |
| Release | Go-live |

### Description
Site detail page with site information, location map, auction details, and the eleven-stage tracker showing completed, current and upcoming stages with dates, responsible office and expected timelines.

### Business Objective
Provide full transparency on where each site is in the process.

### Actors
- Successful Bidder

### User Journey
1. **Who creates:** Stages are updated by the system as events occur.
2. **How they create:** The bidder opens a site to see details and tracker.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The bidder sees the stage history with dates.
8. **How the approver / auditor sees history:** Auditors see access logs.

### Functional Capabilities
- Site details
- GIS map
- Eleven-stage tracker with dates
- Current stage explanation and next step

### UI Screens
- Site detail page
- Stage tracker
- Map view

### Logical API Operations
- Get site details for bidder
- Get stage tracker
- Get map data

### Inputs
- Site

### Outputs
- Details and tracker

### Business Rules
- Stage dates from audit events

### Validations
- Ownership

### Calculations
- Expected dates

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
- Bidder isolation

### Integrations
- GIS via F13-004

### Dependencies
- F13-004

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Mobile-friendly

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Site detail page | Medium | 6 |
| UI | Stage tracker | Medium | 6 |
| UI | Map view | Easy | 4 |
| API | Get site details for bidder | Easy | 4 |
| API | Get stage tracker | Medium | 6 |
| API | Get map data | Easy | 4 |
| Database | Stage history projection | Easy | 2 |
| Testing | Tracker accuracy tests | Medium | 6 |
| Documentation | Bidder help: tracker | Simple | 1 |

**Feature Total: 39 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 14 | 2 | 0 | 6 | 1 | **39** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Tracker projection
- No external integration channel in this feature; Integration row omitted.
