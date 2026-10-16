# F02-002 — Test Centre, Seat & Terminal Master

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-002 |
| Feature Name | Test Centre, Seat & Terminal Master |
| Module | 02 — Examination Configuration & Masters |
| Module Type | Business |
| Release | Go-live |

### Description
Master of test centres across districts with address, map location, contact person and phone, seat layout, terminal list with IP / device identifiers for centre-only access, capacity, accessibility facilities and active status.

### Business Objective
Provide accurate centre and seat data for booking, seat allocation and secure test access.

### Actors
- KEONICS Administrator
- District Coordinator
- Centre Operator

### User Journey
1. **Who creates:** The KEONICS Administrator creates centres; district coordinators propose changes.
2. **How they create:** The administrator enters centre details, seat layout and terminal list (manual or Excel upload).
3. **How they edit:** Centre operators update terminal status (working / faulty); administrators edit details.
4. **How they send for approval:** Capacity or terminal list changes for scheduled sessions need administrator approval.
5. **How the approver sees pending items:** The administrator sees pending changes.
6. **How the approver decides:** The administrator approves or rejects.
7. **How the applicant / maker sees history:** Users see centre details; candidates see addresses on the portal.
8. **How the approver / auditor sees history:** Auditors see changes.

### Functional Capabilities
- Centre master by district
- Seat layout with seat numbers
- Terminal registry with IP / MAC / device ID
- Terminal status and faulty marking
- Accessibility facilities for differently abled candidates
- Excel upload
- Centre activation / deactivation with impact on bookings

### UI Screens
- Centre list
- Centre detail form
- Seat layout editor
- Terminal registry
- Change approval

### Logical API Operations
- Maintain centre
- Maintain seat layout
- Maintain terminals
- Upload centres / terminals
- Approve capacity change
- Deactivation impact check

### Inputs
- Centre details
- Seats
- Terminals

### Outputs
- Centre master

### Business Rules
- Capacity = working terminals
- Deactivation blocked while bookings exist unless moved

### Validations
- IP format, unique terminal IDs

### Calculations
- Available capacity = working terminals − reserved

### Workflow
Active ↔ Inactive

### Search Requirements
- Centres by district

### Documents
- None

### Reports
- Centre capacity report

### Notifications
- Change approvals

### Security
- Admin edits

### Integrations
- None

### Dependencies
- F05-001
- F08-005
- F09-007

### Assumptions
- Centres provided by KEONICS

### Risks
- Terminal changes on exam day

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Centre list | Easy | 4 |
| UI | Centre detail form | Medium | 6 |
| UI | Seat layout editor | Medium | 6 |
| UI | Terminal registry | Medium | 6 |
| UI | Change approval | Easy | 4 |
| API | Maintain centre | Easy | 4 |
| API | Maintain seat layout | Medium | 6 |
| API | Maintain terminals | Medium | 6 |
| API | Upload centres / terminals | Medium | 6 |
| API | Approve capacity change | Easy | 4 |
| API | Deactivation impact check | Medium | 6 |
| Database | Centre, seat and terminal master | Medium | 4 |
| Testing | Centre and terminal tests | Medium | 6 |
| Documentation | Centre setup guide | Easy | 2 |

**Feature Total: 70 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 32 | 4 | 0 | 6 | 2 | **70** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard master
- No external integration channel in this feature; Integration row omitted.
