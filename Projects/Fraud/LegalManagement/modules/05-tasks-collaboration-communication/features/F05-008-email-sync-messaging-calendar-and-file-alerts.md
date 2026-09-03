# F05-008 — Email sync, messaging, calendar and file alerts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-008 |
| **Feature Name** | Email sync, messaging, calendar and file alerts |
| **Module** | 05 — Tasks, Collaboration & Communication |

### Description
The user sends individual or group messages, syncs authorised email, uses the calendar for task overview, and shares files, bills, tasks or calendar with an alert to members.

### Business Objective
Provide authorised email sync plus individual/group messaging, task calendar overview, and file/bill/task/calendar share with alerts.

### Actors
Legal Cell; Advocate; authorised email account holders.

### User Journey
1. Who creates: Legal Cell
2. How they create: User sends individual or group messages in Legal.
3. How they edit: Connects/syncs authorised email (mailbox mapping, retry on failure).
4. How they send for approval: Uses the Task Calendar overview. Message and/or sync mail → calendar overview → share with alert.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. Shares files, bills, tasks or calendar entries with an alert to members. Synced items that belong on a matter are stored against that matter (F05-007 search).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Individual and Group Messaging screens
- Authorised Email Sync status / mailbox view
- Task Calendar overview
- Share files, bills, tasks or calendar with member alert
- No public consumer mail product; no second user directory for mail

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Individual and Group Messaging screens | Complex |
| Authorised Email Sync status / mailbox view | Very High |
| Task Calendar overview | Complex |
| Email sync, messaging, calendar and file alerts history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Email sync, message and calendar operations | Very High |
| Update email sync, messaging, calendar and file alerts | Medium |
| Search email sync, messaging, calendar and file alerts | Medium |
| Read email sync, messaging, calendar and file alerts history | Easy |

### Inputs
Message recipients; authorised mailbox credentials/consent as policy allows; calendar range; share payload (file/bill/task/calendar).

### Outputs
Sent messages; synced email items; calendar view; share alerts.

### Business Rules
- Email sync is authorised mail only, for matter communication.
- Hierarchy/need-to-know and Limited/Community still apply to shared files.
- Bills shared here remain linked to the matter when they are expense bills (Module 07).
- Not Claim settlement payment mail.
- IP of the Legal application remains with SPLOCA.

### Validations
- Mailbox must be authorised for the Person; sync failures retry and surface status; shares require members who can open the matter.

### Calculations
None.

### Workflow
Message and/or sync mail → calendar overview → share with alert.

### Search Requirements
Synced mail and messages by Person, date, matter, subject.

### Documents
Shared files and bills.

### Reports
Email sync status; share alert log.

### Notifications
Alert to members on file/bill/task/calendar share; sync-error notice to user.

### Security
Mailbox tokens protected; no credential sharing; sync audit against shared Person; AES-256 in transit.

### Integrations
Authorised email sync — auth, mapping and retry (Complex). SMS is F06-005, not this feature.

### Dependencies
F05-007; F01-001; F01-002; F07-004 for bills; F05-001 for tasks.

### Assumptions
- SPLOCA names the authorised mail system; this is not speculative multi-tenant Gmail for the public.

### Risks
Over-broad mailbox sync pulls personal mail; policy must constrain folders/labels. AV policy may tighten Limited/Community rules.

### Non Functional Requirements
Retry on sync failure; calendar usable for task overview; court-day messaging.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Individual and Group Messaging screens | UI | Complex | 12 |
| Authorised Email Sync status / mailbox view | UI | Very High | 16 |
| Task Calendar overview | UI | Complex | 12 |
| Email sync, messaging, calendar and file alerts history | UI | Medium | 6 |
| Email sync, message and calendar operations | API | Very High | 16 |
| Update email sync, messaging, calendar and file alerts | API | Medium | 6 |
| Search email sync, messaging, calendar and file alerts | API | Medium | 6 |
| Read email sync, messaging, calendar and file alerts history | API | Easy | 4 |
| Email sync, messaging, calendar and file alerts persistence | DB | Medium | 4 |
| Authorised email sync (auth, mapping, retry) | Integration | Complex | 24 |
| Email sync, messaging, calendar and file alerts feature tests | Testing | Very High | 12 |
| Email sync, messaging, calendar and file alerts implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **122** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
