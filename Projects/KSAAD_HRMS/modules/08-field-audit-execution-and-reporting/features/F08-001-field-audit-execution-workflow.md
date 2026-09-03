# F08-001 — Field Audit Execution Workflow

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Field Audit Execution Workflow |
| **Module** | 08 — Field Audit Execution & Reporting |

### Description
In-charge auditor runs the assignment checklist in the field; supervisor sees progress; history of task completion is kept.

### Business Objective
Controlled field execution after allocation.

### Actors
User: Allocated in-charge and members execute tasks. Supervising Post monitors and may return incomplete checklists. Auditor: read-only history.

### User Journey
1. Who creates: Allocated in-charge and members execute tasks. Supervising Post monitors and may return incomplete checklists.
2. How they create: On approved allocation, system creates the execution file. In-charge opens Field execution, starts visit (date, team present), ticks tasks, Save.
3. How they edit: Open tasks editable by the team. Closed assignment cannot add visits without supervisor reopen.
4. How they send for approval: In-charge Submit visit pack / mark execution complete → supervisor acknowledgement (not the audit report).
5. How the approver sees pending items: Supervisor execution inbox (pending acknowledgement, overdue visits).
6. How the approver decides: Acknowledge progress or Return tasks.
7. How the user sees history: Visit and task timeline on the assignment.
8. How the supervisor / auditor sees history: Supervisor sees team execution history.

### Functional Capabilities
- Authorised user creates, edits and searches field audit task records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Field audit task register | Medium |
| Field audit task form (create and edit) | Very High |
| Field audit task history | Medium |
| Execution checklist | Very High |
| Visit form | Medium |
| Supervisor execution inbox | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create field audit task | Medium |
| Update field audit task | Medium |
| Search field audit task | Medium |
| Read field audit task history | Easy |
| Save checklist progress | Complex |
| Submit visit pack | Complex |

### Inputs
Assignment, visit date, tasks, team present, remarks.

### Outputs
Persisted field audit task; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Assignment must be allocated.
- Visit date mandatory.

### Calculations
Progress % = completed tasks / total tasks.

### Workflow
In-charge Submit visit pack / mark execution complete → supervisor acknowledgement (not the audit report).

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Field notes attachments.

### Reports
Execution progress vs plan.

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
| Field audit task register | UI | Medium | 6 |
| Field audit task form (create and edit) | UI | Very High | 16 |
| Field audit task history | UI | Medium | 6 |
| Execution checklist | UI | Very High | 16 |
| Visit form | UI | Medium | 6 |
| Supervisor execution inbox | UI | Complex | 12 |
| Create field audit task | API | Medium | 6 |
| Update field audit task | API | Medium | 6 |
| Search field audit task | API | Medium | 6 |
| Read field audit task history | API | Easy | 4 |
| Save checklist progress | API | Complex | 8 |
| Submit visit pack | API | Complex | 8 |
| Field audit task record and history | DB | Medium | 4 |
| Internal identity/document hooks for field audit task | Integration | Simple | 4 |
| Field Audit Execution Workflow feature tests | Testing | Very High | 12 |
| Field Audit Execution Workflow implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **123** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
