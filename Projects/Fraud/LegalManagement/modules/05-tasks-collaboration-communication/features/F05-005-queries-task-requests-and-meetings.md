# F05-005 — Queries, task requests and meetings

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-005 |
| **Feature Name** | Queries, task requests and meetings |
| **Module** | 05 — Tasks, Collaboration & Communication |

### Description
A client-side authorised user (or Legal Cell on their behalf) raises a query, requests a task, or schedules a meeting on the matter. Legal Cell responds or accepts the slot; the thread stays on the matter.

### Business Objective
Support client–legal collaboration: queries, task requests and meeting slots recorded on the matter.

### Actors
Authorised client-side user; Legal Cell (on behalf or responding); Advocate.

### User Journey
1. Client-side authorised user (or Legal Cell on their behalf) raises a query, requests a task, or schedules a meeting.
2. Legal Cell responds or accepts the slot.
3. The thread stays on the matter.

### Functional Capabilities
- Query / Task Request form
- Meeting Scheduler on the matter
- Response/accept slot
- Thread retained on the matter
- Not a public portal

### Inputs
Query text; requested task; meeting slot; responders.

### Outputs
Query thread; task request (may create F05-001 task); meeting record.

### Business Rules
- Client-side users are authorised Persons on shared IAM, not anonymous public users.
- Threads stay on the matter.
- AV group meetings with operational units are F05-009.

### Validations
Matter required; meeting slot conflict warning; task request maps to an assignable Post.

### Calculations
None.

### Workflow
Raise query/request/meeting → Legal Cell respond/accept → thread on matter.

### Search Requirements
Queries by matter, Person, date, open/closed.

### Documents
Optional query attachments.

### Reports
Open queries/meetings on matter.

### Notifications
New query; meeting accepted/rejected.

### Security
Need-to-know; Limited space if the thread is Limited.

### Integrations
Matter attachment (Simple).

### Dependencies
F04-001; F05-001; F01-002.

### Assumptions
‘Client’ is authorised collaboration user per SOW, not citizen CMS.

### Risks
Meetings booked without Legal Cell acceptance.

### Non Functional Requirements
Thread searchable with F05-007.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Query / Task Request form | UI | Medium | 6 |
| Meeting Scheduler on the matter | UI | Complex | 12 |
| Query and meeting thread operations | API | Complex | 8 |
| Thread entities | Database | Medium | 4 |
| Matter attachment | Integration | Simple | 4 |
| Query/meeting tests | Testing | Medium | 6 |
| Queries, task requests and meetings guide | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- Email sync calendar is F05-008.
- Operational-unit AV is F05-009.
