# F06-002 — Visitor Registration and Access

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Visitor Registration and Access |
| **Module** | 06 — Office & Administration (Visitor, Reception and Meetings) |

### Description
Reception creates a visitor pass, host Post acknowledges, reception checks out; both see history.

### Business Objective
Traceable visitor access.

### Actors
User: Reception clerk creates the pass. Host (Person/Post visited) acknowledges. Reception checks out. Auditor: read-only history.

### User Journey
1. Who creates: Reception clerk creates the pass. Host (Person/Post visited) acknowledges. Reception checks out.
2. How they create: Reception → New visitor: name, ID proof type/number, host Post/Person, purpose, time in, Save. Pass number generated.
3. How they edit: Open pass (not yet checked out) can be edited. After checkout, only a correction with supervisor approval.
4. How they send for approval: Host receives a notification to Acknowledge visitor. Checkout is reception Save of time out.
5. How the approver sees pending items: Host sees Visitors waiting acknowledgement. Supervisor sees overdue open passes.
6. How the approver decides: Host Acknowledge or Deny (deny records reason, pass cancelled).
7. How the user sees history: Reception search by date, visitor name, host.
8. How the supervisor / auditor sees history: Host sees visitors they acknowledged.

### Functional Capabilities
- Authorised user creates, edits and searches visitor pass records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Visitor pass register | Medium |
| Visitor pass form (create and edit) | Complex |
| Visitor pass history | Medium |
| Visitor pass form | Medium |
| Host visitor inbox | Easy |
| Open passes register | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create visitor pass | Medium |
| Update visitor pass | Medium |
| Search visitor pass | Medium |
| Read visitor pass history | Easy |
| Issue pass number | Easy |
| Acknowledge visitor | Easy |
| Check out visitor | Easy |

### Inputs
Visitor name, ID proof, host, purpose, in/out time.

### Outputs
Persisted visitor pass; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Host mandatory.
- Name mandatory.

### Calculations
None.

### Workflow
Host receives a notification to Acknowledge visitor. Checkout is reception Save of time out.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Optional ID scan via DMS.

### Reports
Visitors by day/host.

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
| Visitor pass register | UI | Medium | 6 |
| Visitor pass form (create and edit) | UI | Complex | 12 |
| Visitor pass history | UI | Medium | 6 |
| Visitor pass form | UI | Medium | 6 |
| Host visitor inbox | UI | Easy | 4 |
| Open passes register | UI | Medium | 6 |
| Create visitor pass | API | Medium | 6 |
| Update visitor pass | API | Medium | 6 |
| Search visitor pass | API | Medium | 6 |
| Read visitor pass history | API | Easy | 4 |
| Issue pass number | API | Easy | 4 |
| Acknowledge visitor | API | Easy | 4 |
| Check out visitor | API | Easy | 4 |
| Visitor pass record and history | DB | Medium | 4 |
| Internal identity/document hooks for visitor pass | Integration | Simple | 4 |
| Visitor Registration and Access feature tests | Testing | Complex | 8 |
| Visitor Registration and Access implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **93** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
