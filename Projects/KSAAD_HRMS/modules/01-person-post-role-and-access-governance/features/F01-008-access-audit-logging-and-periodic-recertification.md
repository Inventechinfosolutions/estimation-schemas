# F01-008 — Access Audit, Logging and Periodic Recertification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-008 |
| **Feature Name** | Access Audit, Logging and Periodic Recertification |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
The system records access events. Periodically, a supervising Post recertifies that current mappings under them are still valid.

### Business Objective
Provide forensic access logs and a controlled recertification cycle.

### Actors
User: Access Administrator opens/starts a recertification campaign. Supervising Posts complete recertification. Auditor reads logs. Auditor: read-only history.

### User Journey
1. Who creates: Access Administrator opens/starts a recertification campaign. Supervising Posts complete recertification. Auditor reads logs.
2. How they create: Administrator opens Recertification → New campaign, selects office/Posts, due date, then Start. The system lists current mappings in scope.
3. How they edit: Campaign header (due date) can be edited before Start. After Start, mappings in the campaign cannot be deleted from the list; they must be certified or flagged.
4. How they send for approval: Each supervising Post opens their recertification inbox and Submit-certifies each mapping (Confirm or Revoke with reason). Revoke raises a JML leaver/mover draft (F01-007).
5. How the approver sees pending items: Supervising Post sees pending mappings to recertify. Administrator sees overdue campaigns.
6. How the approver decides: Supervisor marks Confirm or Revoke. Administrator closes the campaign when all items are decided or overdue items are escalated.
7. How the user sees history: Administrator opens campaign history and per-mapping decisions.
8. How the supervisor / auditor sees history: Supervisor sees their past recertification decisions. Auditor opens the access log (login, mapping change, permission change, recertification) filtered by Person, Post, period.

### Functional Capabilities
- Authorised user creates, edits and searches access recertification campaign records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Access recertification campaign register | Medium |
| Access recertification campaign form (create and edit) | Complex |
| Access recertification campaign history | Medium |
| Access log search (auditor) | Complex |
| Recertification campaign form | Medium |
| Supervisor recertification inbox | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create access recertification campaign | Medium |
| Update access recertification campaign | Medium |
| Search access recertification campaign | Medium |
| Read access recertification campaign history | Easy |
| Write access log event | Complex |
| Search access log | Medium |
| Start recertification campaign | Complex |
| Record recertification decision | Complex |

### Inputs
Campaign name, office scope, due date, mapping, decision, remarks.

### Outputs
Persisted access recertification campaign; searchable register; history.

### Business Rules
- Access logs are append-only and cannot be edited by Administrators.
- Recertification does not itself map a Person; Revoke triggers F01-007.

### Validations
- Campaign due date in the future.
- Confirm/Revoke requires identity of acting supervisor.

### Calculations
Overdue = now > due date and item still pending.

### Workflow
Each supervising Post opens their recertification inbox and Submit-certifies each mapping (Confirm or Revoke with reason). Revoke raises a JML leaver/mover draft (F01-007).

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Access log export; recertification completion by office.

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
| Access recertification campaign register | UI | Medium | 6 |
| Access recertification campaign form (create and edit) | UI | Complex | 12 |
| Access recertification campaign history | UI | Medium | 6 |
| Access log search (auditor) | UI | Complex | 12 |
| Recertification campaign form | UI | Medium | 6 |
| Supervisor recertification inbox | UI | Complex | 12 |
| Create access recertification campaign | API | Medium | 6 |
| Update access recertification campaign | API | Medium | 6 |
| Search access recertification campaign | API | Medium | 6 |
| Read access recertification campaign history | API | Easy | 4 |
| Write access log event | API | Complex | 8 |
| Search access log | API | Medium | 6 |
| Start recertification campaign | API | Complex | 8 |
| Record recertification decision | API | Complex | 8 |
| Access recertification campaign record and history | DB | Medium | 4 |
| Internal identity/document hooks for access recertification campaign | Integration | Simple | 4 |
| Access Audit, Logging and Periodic Recertification feature tests | Testing | Very High | 12 |
| Access Audit, Logging and Periodic Recertification implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **129** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
