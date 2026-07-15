# F07-002 — Officer-Assisted Application Entry

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | Officer-Assisted Application Entry |
| **Module** | 07 — Application First Come Booking |

### Description
Allow authorised BDA staff to enter an assisted application for a citizen, attach scanned evidence, and submit it into the same verification and booking process used by online applications.

### Business Objective
Support citizens needing office assistance without creating a parallel or less-controlled application path.

### Actors
Housing/Estate Officer; Data Entry Operator; Citizen; Auditor.

### User Journey
An officer registers or locates the citizen, selects the published unit, records the application details and scanned documents, captures required declarations, links the online payment initiation path, and submits for verification.

### Functional Capabilities
- Citizen lookup/registration handoff and assisted-application form.
- Channel flag, operator attribution, scanned-document checklist, and print acknowledgement.
- Controlled correction before verification and same workflow routing as online applications.

### Inputs
Citizen reference, selected unit, assisted-entry details, scanned documents, declaration confirmation, and operator remarks.

### Outputs
Officer-origin application, acknowledgement, audit trail, and common verification work item.

### Business Rules
Officer-assisted entry must use the same application status and approval path as online entry; payment remains online-only; the entering officer is recorded and cannot approve their own submission where segregation rules apply.

### Validations
Authorised officer role, citizen identity/reference, published eligible unit, mandatory documents/declarations, and duplicate active application rule.

### Calculations
Document-checklist completion and assisted-entry volume by operator.

### Workflow
Citizen located/registered → officer entry → documents attached → submitted → verification pending.

### Search Requirements
Application number, citizen, project, unit, entry officer, channel, date, and status.

### Documents
Scanned application support documents, declarations, and printed acknowledgement copy.

### Reports
Officer-assisted application register and operator productivity/exception list.

### Notifications
Citizen acknowledgement and workflow notifications through Module 12.

### Security
Role and section scope, operator audit, maker-checker segregation, and restricted access to citizen documents.

### Integrations
Citizen profile/inventory consumption (Medium) and notification handoff (Easy).

### Dependencies
F06-001, F07-001, F07-003, Modules 03–05 and 12.

### Assumptions
Physical document scanning is performed by BDA; this feature accepts supplied digital scans.

### Risks
Mis-keyed assisted entries or illegible scans may require correction cycles.

### Non Functional Requirements
Efficient office data entry, printable acknowledgement, and full operator traceability.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Officer-assisted entry and document screens | UI | Complex | 8 |
| Assisted application validation and routing | API | Complex | 8 |
| Channel and operator audit persistence | Database | Medium | 4 |
| Citizen/inventory and notification handoffs | Integration | Medium | 16 |
| Assisted-entry tests | Testing | Complex | 8 |
| Officer entry guide | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
This feature reuses the common application workflow but separately estimates officer-facing capture and channel controls.
