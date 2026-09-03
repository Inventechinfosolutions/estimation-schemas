# F01-001 — Person master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Person master |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
An Administrator maintains each official as a unique Person with legal name and a unique identifier. The Administrator opens Person administration, creates a Person, or searches an existing Person and updates particulars. The Administrator cannot create a second Person for the same official. Every later claim action (verify, approve, pay, close) is stored against this Person, not against a shared login. This Person master is the shared identity directory for Claim, Legal and Valuation.

### Business Objective
Ensure every official action in the claim programme (and consuming Legal / Valuation applications) is attributable to one named Person.

### Actors
Administrator (Person/Post administration); auditor (read-only Person register).

### User Journey
1. Who creates: Administrator (Person
2. How they create: Administrator opens the Person register and searches by legal name, unique ID, official email or credential status.
3. How they edit: If no Person exists, Administrator enters legal name, unique ID, official contacts and saves a new Person.
4. How they send for approval: If a Person already exists for that official, the system blocks a duplicate create and shows the existing record.
5. How the approver sees pending items: Checker opens the pending change inbox.
6. How the approver decides: Checker approves or rejects with remarks.
7. How the maker sees history: Administrator (Person opens change history on the record (who changed what, when).
8. How the checker / auditor sees history: Auditor (and checker if used) open the same history.

### Functional Capabilities
- Person register with search, create, view and update.
- Enforce one Person per official; refuse a second Person for the same official.
- Retain Person identity after deactivation so historical claim, legal and valuation actions remain attributable.
- Expose Person as the identity consumed by Post mapping (F01-002) and by Legal / Valuation without a second user directory.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Person register + search | Complex |
| Person create/edit form | Medium |
| Person master change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Person uniqueness and lifecycle operations | Complex |
| Update person master | Medium |
| Search person master register | Medium |
| Read person master change history | Easy |

### Inputs
Legal name, Person unique ID, official email and mobile, credential status, Administrator remarks.

### Outputs
Unique Person record; searchable Person register; identity used on all subsequent privileged actions.

### Business Rules
- Access model is Person → Post → Role → Permissions; this feature creates the Person only.
- A second Person for the same official is not allowed.
- Claim, legal and valuation actions store the acting Person, not a shared login name.
- Deactivation (F01-007) does not delete the Person or historical attribution.

### Validations
- Legal name and unique ID are mandatory.
- Unique ID is unique across the Person master.
- Official email, when entered here, must be consistent with official-identity rules in F01-004.

### Calculations
None beyond uniqueness checks.

### Workflow
Direct administration with audit. No maker-checker is assumed unless the Authority later requires it.

### Search Requirements
Legal name, unique ID, official email, mobile, credential status (Active / Inactive / Locked).

### Documents
None as Person identity papers; staff identity proof is not a claimant KYC pack.

### Reports
Person register export for administrators and auditors.

### Notifications
None required on Person create; activation notifications belong to F01-005.

### Security
Only an Administrator Post may create or update Persons. Person records are need-to-know. Every create/update is audited with actor Person, Post, timestamp and before/after values.

### Integrations
Internal identity service consumed by Legal and Valuation (no second user directory in those SOWs).

### Dependencies
None (foundational). Consumed by F01-002 mapping and by all later modules.

### Assumptions
- SSO/Active Directory is out of scope unless later ordered.
- OOK claimants are not Persons in this master (F01-008).
- Legal and Valuation reuse this Person master rather than rebuilding it.

### Risks
- Duplicate Persons would split audit attribution across claim, legal and valuation actions.
- Treating a shared login as a Person would break forensic audit.

### Non Functional Requirements
This is the programme-wide identity product consumed by Legal Management and GIS field valuation; staff screens must remain usable during claim windows; privileged actions are attributable to a named Person acting in a Post; primary official hosting identity is an approved government domain, not .org.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Person register + search | UI | Complex | 12 |
| Person create/edit form | UI | Medium | 6 |
| Person master change history | UI | Medium | 6 |
| Person uniqueness and lifecycle operations | API | Complex | 8 |
| Update person master | API | Medium | 6 |
| Search person master register | API | Medium | 6 |
| Read person master change history | API | Easy | 4 |
| Person identity persistence | DB | Medium | 4 |
| Internal identity handoff to Legal and Valuation | Integration | Simple | 4 |
| Person master feature tests | Testing | Complex | 8 |
| Person master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
