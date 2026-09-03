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
1. Who creates: Authorised client-side user
2. How they create: Client-side authorised user (or Legal Cell on their behalf) raises a query, requests a task, or schedules a meeting.
3. How they edit: Legal Cell responds or accepts the slot.
4. How they send for approval: The thread stays on the matter. Raise query/request/meeting → Legal Cell respond/accept → thread on matter.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Authorised client-side user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Authorised client-side user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Query / Task Request form
- Meeting Scheduler on the matter
- Response/accept slot
- Thread retained on the matter
- Not a public portal

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Query / Task Request form | Medium |
| Meeting Scheduler on the matter | Complex |
| Queries, task requests and meetings history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Query and meeting thread operations | Complex |
| Update queries, task requests and meetings | Medium |
| Search queries, task requests and meetings | Medium |
| Read queries, task requests and meetings history | Easy |

### Inputs
Query text; requested task; meeting slot; responders.

### Outputs
Query thread; task request (may create F05-001 task); meeting record.

### Business Rules
- Client-side users are authorised Persons on shared IAM, not anonymous public users.
- Threads stay on the matter.
- AV group meetings with operational units are F05-009.

### Validations
- Matter required; meeting slot conflict warning; task request maps to an assignable Post.

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
- ‘Client’ is authorised collaboration user per SOW, not citizen CMS.

### Risks
Meetings booked without Legal Cell acceptance.

### Non Functional Requirements
Thread searchable with F05-007.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Query / Task Request form | UI | Medium | 6 |
| Meeting Scheduler on the matter | UI | Complex | 12 |
| Queries, task requests and meetings history | UI | Medium | 6 |
| Query and meeting thread operations | API | Complex | 8 |
| Update queries, task requests and meetings | API | Medium | 6 |
| Search queries, task requests and meetings | API | Medium | 6 |
| Read queries, task requests and meetings history | API | Easy | 4 |
| Queries, task requests and meetings persistence | DB | Medium | 4 |
| Matter attachment | Integration | Simple | 4 |
| Queries, task requests and meetings feature tests | Testing | Medium | 6 |
| Queries, task requests and meetings implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **64** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
