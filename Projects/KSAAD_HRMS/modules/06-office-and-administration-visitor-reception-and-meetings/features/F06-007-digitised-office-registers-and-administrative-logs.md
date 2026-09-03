# F06-007 — Digitised Office Registers and Administrative Logs

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-007 |
| **Feature Name** | Digitised Office Registers and Administrative Logs |
| **Module** | 06 — Office & Administration (Visitor, Reception and Meetings) |

### Description
Clerk records entries in a named office register (dak, peon book, etc.); supervisor may attest; history is the register log.

### Business Objective
Digitise named office registers.

### Actors
User: Office clerk creates entries. Supervising office Post attests if the register type requires it. Auditor: read-only history.

### User Journey
1. Who creates: Office clerk creates entries. Supervising office Post attests if the register type requires it.
2. How they create: Opens Registers → select type → New entry: date, reference, description, Save.
3. How they edit: Same-day draft edits. After attest, correction request to supervisor.
4. How they send for approval: If register type requires attest, Submit to supervisor; else Save is final.
5. How the approver sees pending items: Supervisor attest inbox for those register types.
6. How the approver decides: Attest or Return.
7. How the user sees history: Searchable log by register type and date.
8. How the supervisor / auditor sees history: Attestation history.

### Functional Capabilities
- Authorised user creates, edits and searches office register entry records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Office register entry register | Medium |
| Office register entry form (create and edit) | Complex |
| Office register entry history | Medium |
| Register type selector | Easy |
| Entry form | Medium |
| Register search | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create office register entry | Medium |
| Update office register entry | Medium |
| Search office register entry | Medium |
| Read office register entry history | Easy |

### Inputs
Register type, date, reference, description.

### Outputs
Persisted office register entry; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Register type and date mandatory.

### Calculations
None.

### Workflow
If register type requires attest, Submit to supervisor; else Save is final.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Optional scan of the paper page.

### Reports
Register dump by type/period.

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
| Office register entry register | UI | Medium | 6 |
| Office register entry form (create and edit) | UI | Complex | 12 |
| Office register entry history | UI | Medium | 6 |
| Register type selector | UI | Easy | 4 |
| Entry form | UI | Medium | 6 |
| Register search | UI | Medium | 6 |
| Create office register entry | API | Medium | 6 |
| Update office register entry | API | Medium | 6 |
| Search office register entry | API | Medium | 6 |
| Read office register entry history | API | Easy | 4 |
| Office register entry record and history | DB | Medium | 4 |
| Internal identity/document hooks for office register entry | Integration | Simple | 4 |
| Digitised Office Registers and Administrative Logs feature tests | Testing | Complex | 8 |
| Digitised Office Registers and Administrative Logs implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **81** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
