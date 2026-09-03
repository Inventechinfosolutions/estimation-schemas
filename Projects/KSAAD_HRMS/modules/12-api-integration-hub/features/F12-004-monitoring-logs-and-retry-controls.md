# F12-004 — Monitoring, Logs and Retry Controls

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-004 |
| **Feature Name** | Monitoring, Logs and Retry Controls |
| **Module** | 12 — API Integration Hub |

### Description
Operator watches dashboards, opens failed runs, retries or raises incident; history of retries is kept.

### Business Objective
Operate integrations with an inbox, not only server logs.

### Actors
User: Integration operator. Checker if abandon requires approval. Auditor: read-only history.

### User Journey
1. Who creates: Integration operator. Checker if abandon requires approval.
2. How they create: Incidents are created from failed runs or manually New incident: run, error, Save.
3. How they edit: Add notes. Cannot edit past retry results.
4. How they send for approval: Retry from the incident. Abandon Submit to checker if required.
5. How the approver sees pending items: Failed runs / open incidents inbox. Dashboard is supervisory.
6. How the approver decides: Retry, escalate, or abandon (checked).
7. How the user sees history: Retries and notes on the incident.
8. How the supervisor / auditor sees history: Abandoned incidents.

### Functional Capabilities
- Authorised user creates, edits and searches integration incident records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Integration incident register | Medium |
| Integration incident form (create and edit) | Complex |
| Integration incident history | Medium |
| Integration dashboard | Very High |
| Failed-run inbox | Complex |
| Incident form | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create integration incident | Medium |
| Update integration incident | Medium |
| Search integration incident | Medium |
| Read integration incident history | Easy |
| Query run health | Medium |
| Retry from incident | Complex |

### Inputs
Run, error, action, notes.

### Outputs
Persisted integration incident; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Abandon requires reason.

### Calculations
Error rate = errors / attempted.

### Workflow
Retry from the incident. Abandon Submit to checker if required.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Incident ageing.

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
| Integration incident register | UI | Medium | 6 |
| Integration incident form (create and edit) | UI | Complex | 12 |
| Integration incident history | UI | Medium | 6 |
| Integration dashboard | UI | Very High | 16 |
| Failed-run inbox | UI | Complex | 12 |
| Incident form | UI | Medium | 6 |
| Create integration incident | API | Medium | 6 |
| Update integration incident | API | Medium | 6 |
| Search integration incident | API | Medium | 6 |
| Read integration incident history | API | Easy | 4 |
| Query run health | API | Medium | 6 |
| Retry from incident | API | Complex | 8 |
| Integration incident record and history | DB | Medium | 4 |
| Internal identity/document hooks for integration incident | Integration | Easy | 8 |
| Monitoring, Logs and Retry Controls feature tests | Testing | Very High | 12 |
| Monitoring, Logs and Retry Controls implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **121** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
