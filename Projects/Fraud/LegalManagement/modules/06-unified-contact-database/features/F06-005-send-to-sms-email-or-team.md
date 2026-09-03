# F06-005 — Send to SMS, email or team

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-005 |
| **Feature Name** | Send to SMS, email or team |
| **Module** | 06 — Unified Contact Database |

### Description
From the contact, the user chooses SMS, email or team, and sends the number or address for contacting. The action is recorded against the contact or matter where linked.

### Business Objective
Hand off a contact’s number or address to SMS, email or team and record the action on the contact or linked matter.

### Actors
Legal Cell; Advocate.

### User Journey
1. Who creates: Legal Cell
2. How they create: User opens a contact and chooses SMS, email or team.
3. How they edit: Sends the number or address for contacting.
4. How they send for approval: The action is recorded against the contact or matter where linked. Choose channel → confirm → send/handoff → log.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Contact Action bar (SMS / Email / Team)
- Send confirmation
- Record action on contact or linked matter
- Not a bulk marketing campaign tool

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Contact Action bar (SMS, Email, Team) | Medium |
| Send confirmation | Simple |
| Send to sms, email or team history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Send/handoff operations | Medium |
| Update send to sms, email or team | Medium |
| Search send to sms, email or team | Medium |
| Read send to sms, email or team history | Easy |

### Inputs
Contact; channel (SMS/email/team); optional linked matter; payload (number/address).

### Outputs
Handoff to channel; action log.

### Business Rules
- User can pass the number/email to SMS, email or team from the contact record.
- SMS is hand-off of numbers for contacting, not a full SMS marketing gateway product.
- Email here is send-to-address; mailbox sync is F05-008.

### Validations
- Channel required; destination present on the contact; matter link optional but recorded when used.

### Calculations
None.

### Workflow
Choose channel → confirm → send/handoff → log.

### Search Requirements
Action log by contact, channel, date, matter.

### Documents
None.

### Reports
Contact channel action log.

### Notifications
Team hand-off notice to the team inbox.

### Security
Numbers of sensitive contacts not copied to unauthorised team spaces.

### Integrations
SMS/email service (Medium — auth, mapping, retry).

### Dependencies
F06-001; F06-002; F05-007/F05-008; F01-002.

### Assumptions
- SMS/email providers are Authority-approved; this feature is the Legal hand-off and log.

### Risks
Wrong number sent to team; log must show actor.

### Non Functional Requirements
Action attributable to shared Person.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Contact Action bar (SMS, Email, Team) | UI | Medium | 6 |
| Send confirmation | UI | Simple | 2 |
| Send to sms, email or team history | UI | Medium | 6 |
| Send/handoff operations | API | Medium | 6 |
| Update send to sms, email or team | API | Medium | 6 |
| Search send to sms, email or team | API | Medium | 6 |
| Read send to sms, email or team history | API | Easy | 4 |
| Send to sms, email or team persistence | DB | Medium | 4 |
| SMS/email service | Integration | Medium | 16 |
| Send to SMS, email or team feature tests | Testing | Medium | 6 |
| Send to SMS, email or team implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **64** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
