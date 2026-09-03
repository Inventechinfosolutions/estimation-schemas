# F08-006 — Timeline, Reminder and Escalation Monitoring

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-006 |
| **Feature Name** | Timeline, Reminder and Escalation Monitoring |
| **Module** | 08 — Field Audit Execution & Reporting |

### Description
System computes SLA from plan/allocation/issue; officers see a dashboard; overdue items escalate to supervising Post.

### Business Objective
Pendency and escalation visibility.

### Actors
User: System generates alerts. Supervisors act by opening the underlying assignment. Admin may snooze with reason. Auditor: read-only history.

### User Journey
1. Who creates: System generates alerts. Supervisors act by opening the underlying assignment. Admin may snooze with reason.
2. How they create: Alerts are created by SLA jobs from plan dates and workflow timestamps — not typed by users. Admin may configure SLA in Module 02.
3. How they edit: Users do not edit SLA clocks. Snooze records a reason and new remind-on date.
4. How they send for approval: No approval of the alert itself. Escalation notifies the next supervising Post.
5. How the approver sees pending items: Supervisor Escalation inbox of overdue assignments/reports.
6. How the approver decides: Open the assignment and complete the delayed step; or snooze with reason (audited).
7. How the user sees history: Alert history on the assignment.
8. How the supervisor / auditor sees history: Escalation register.

### Functional Capabilities
- Authorised user creates, edits and searches audit timeline alert records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Audit timeline alert register | Medium |
| Audit timeline alert form (create and edit) | Complex |
| Audit timeline alert history | Medium |
| Pendency dashboard | Very High |
| Escalation inbox | Medium |
| Snooze dialog | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create audit timeline alert | Medium |
| Update audit timeline alert | Medium |
| Search audit timeline alert | Medium |
| Read audit timeline alert history | Easy |
| Compute SLA due dates | Very High |
| Raise escalation | Complex |
| Snooze alert | Easy |

### Inputs
Assignment, SLA type, due date, snooze reason.

### Outputs
Persisted audit timeline alert; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Snooze requires reason.

### Calculations
Overdue = now > due date for that step (allocation, visit, draft, review, issue).

### Workflow
No approval of the alert itself. Escalation notifies the next supervising Post.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Ageing by step.

### Notifications
On-screen confirmation. Optional notice to the user on save failure.

### Security
Need-to-know by Post. Actions attributed to Person acting in a Post.

### Integrations
Module 01 identity. Document store if attachments are used.

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

### Assumptions
- Hours use Estimation Master values only, at capability grain (not one billed row per screen).

### Risks
Unscoped access would expose records outside the user's office.

### Non Functional Requirements
Register and history remain searchable during office hours.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Audit timeline alert register | UI | Medium | 6 |
| Audit timeline alert form (create and edit) | UI | Complex | 12 |
| Audit timeline alert history | UI | Medium | 6 |
| Pendency dashboard | UI | Very High | 16 |
| Escalation inbox | UI | Medium | 6 |
| Snooze dialog | UI | Simple | 2 |
| Create audit timeline alert | API | Medium | 6 |
| Update audit timeline alert | API | Medium | 6 |
| Search audit timeline alert | API | Medium | 6 |
| Read audit timeline alert history | API | Easy | 4 |
| Compute SLA due dates | API | Very High | 16 |
| Raise escalation | API | Complex | 8 |
| Snooze alert | API | Easy | 4 |
| Audit timeline alert record and history | DB | Medium | 4 |
| Internal identity/document hooks for audit timeline alert | Integration | Simple | 4 |
| Timeline, Reminder and Escalation Monitoring feature tests | Testing | Very High | 12 |
| Timeline, Reminder and Escalation Monitoring implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **121** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
