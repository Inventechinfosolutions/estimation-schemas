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
1. User opens a contact and chooses SMS, email or team.
2. Sends the number or address for contacting.
3. The action is recorded against the contact or matter where linked.

### Functional Capabilities
- Contact Action bar (SMS / Email / Team)
- Send confirmation
- Record action on contact or linked matter
- Not a bulk marketing campaign tool

### Inputs
Contact; channel (SMS/email/team); optional linked matter; payload (number/address).

### Outputs
Handoff to channel; action log.

### Business Rules
- User can pass the number/email to SMS, email or team from the contact record.
- SMS is hand-off of numbers for contacting, not a full SMS marketing gateway product.
- Email here is send-to-address; mailbox sync is F05-008.

### Validations
Channel required; destination present on the contact; matter link optional but recorded when used.

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
SMS/email providers are Authority-approved; this feature is the Legal hand-off and log.

### Risks
Wrong number sent to team; log must show actor.

### Non Functional Requirements
Action attributable to shared Person.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Contact Action bar (SMS, Email, Team) | UI | Medium | 6 |
| Send confirmation | UI | Simple | 2 |
| Send/handoff operations | API | Medium | 6 |
| Action log | Database | Easy | 2 |
| SMS/email service | Integration | Medium | 16 |
| Send-action tests | Testing | Medium | 6 |
| Contact SMS/email/team guide | Documentation | Easy | 2 |
| **Total** | | | **40** |

### Estimation Assumptions
- Does not rebuild the SMS gateway; Integration Medium is connector consumption.
