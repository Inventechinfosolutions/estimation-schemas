# F03-001 — Housing Project Register

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Housing Project Register |
| **Module** | 03 — Housing Project Management |

### Description
Create and maintain housing projects with approved attributes, counts, amenities, booking window, completion date, and status.

### Business Objective
Establish an authoritative project record before units and notifications are published.

### Actors
Engineering Section; Housing officers; Approvers; Auditor.

### User Journey
Officer opens Project Register, creates or edits a project using active masters, records project details and planned availability, and saves it for the configured lifecycle.

### Functional Capabilities
Project create/edit/view; project code; location/layout/phase/zone; counts; amenities; booking window; completion date; status; project register export.

### Inputs
Project identity, type, location, layout, phase, zone, counts, amenities, dates, status.

### Outputs
Project record and Project Register.

### Business Rules
Project is not citizen-visible until approved/published; unit inventory is maintained separately; active master values only.

### Validations
Unique project code; required project/location/type; valid booking and completion dates; non-negative counts.

### Calculations
None.

### Workflow
Draft → submit for project approval → approved/published status handled with F03-003.

### Search Requirements
Project code/name, type, layout, zone, status, booking window, completion date.

### Documents
Project media and supporting files are embedded in F03-002.

### Reports
Project Register export.

### Notifications
Configured alerts on project submission/status movement.

### Security
RBAC by section; project change audit.

### Integrations
None.

### Dependencies
Modules 01–02; F03-003.

### Assumptions
No GIS mapping platform is included.

### Risks
Incorrect project availability counts can mislead downstream planning.

### Non Functional Requirements
Responsive officer views; traceable changes; pagination/filter performance.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Project Register + advanced filters | UI | Complex | 8 |
| Project create/edit form | UI | Very High | 16 |
| Project register operations | API | Complex | 8 |
| Project persistence and constraints | Database | Complex | 6 |
| Project register tests | Testing | Very High | 12 |
| Project management guide | Documentation | Medium | 3 |
| **Total** | | | **53** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
