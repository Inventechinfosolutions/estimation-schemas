# F01-002 — Centre and Invigilator User Mapping

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Centre and Invigilator User Mapping |
| **Module** | 01 — Access Control and Staff User Management |

### Description
Examination Centre / Invigilator staff users are created and mapped only to their authorised examination centre(s). The Administrator opens the centre-user register, creates a centre/invigilator account, maps it to one or more authorised centres from the centre master, assigns Centre/Invigilator role privileges (centre dashboard, candidate verification, session activation, attendance and centre monitoring), and activates or deactivates the account. At runtime, a centre user can see and act only on candidates, sessions and monitoring data for the mapped centre(s)—never another centre’s examinations or candidates. Inactive centre users cannot log in.

### Business Objective
Enforce centre-scoped staff access so Invigilators and centre operators work only within authorised centres, preventing cross-centre visibility of candidates and examination-day operations.

### Actors
Examination Administrator (creates and maps centre users); Examination Centre / Invigilator user (consumes mapped access); Auditor (read-only mapping and access history).

### User Journey
1. Who creates: Examination Administrator with user-administration (or centre-user management) privilege.
2. How they create: Open Centre / Invigilator user register → New user → enter staff identity → select role Centre/Invigilator → map one or more authorised Active centres → assign centre-dashboard privileges → save and activate.
3. How they edit: Search register → open user → change contacts, remapping of centres, or privileges → save; removed centre mappings immediately revoke access to that centre’s work.
4. How they send for approval: Submit/approval does not apply; mapping is an administrative save under Administrator privilege.
5. How the approver sees pending items: There is no approver inbox; unmapped or inactive centre users appear as filter statuses on the register only.
6. How the approver decides: There is no approval decision; activate/deactivate and mapping changes are Administrator actions.
7. How the applicant / maker sees history: Administrator opens mapping and account history (centre add/remove, activation, privilege changes).
8. How the approver / auditor sees history: Auditor opens the same history and may filter by centre to see who was mapped when.

### Functional Capabilities
- Maintain Centre / Invigilator user register with create, view, update, search and Active/Inactive status.
- Capture centre staff identity (name, official mobile, official email, optional employee/reference id).
- Map each centre user to one or more authorised Active examination centres.
- Restrict centre dashboard, candidate lists, session activation and monitoring to mapped centre(s) only.
- Block a centre user from viewing examinations or candidates of an unmapped centre.
- Activate and deactivate centre users; refuse login when Inactive.
- Support remapping when a user moves between centres, with audit of prior mappings.
- Prevent activation of a centre user with zero centre mappings.
- Align privileges to centre functions only (dashboard, verification, activation, attendance, centre reports)—not full Administrator packs.
- Provide centre-scoped access preview so Administrator can confirm what the user will see.
- Enforce uniqueness of login identity within staff centre users.
- Expose mapped users list per centre for operational readiness before examination day.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Centre / Invigilator user register and search | Complex |
| Centre user create / edit form | Medium |
| Centre mapping assignment screen | Complex |
| Centre-scoped access preview | Medium |
| Centre user activate / deactivate confirmation | Easy |
| Mapping and access change history | Medium |
| Users-by-centre operational list | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create Centre / Invigilator user | Complex |
| Update centre user particulars | Medium |
| Map or unmap authorised centres | Complex |
| Enforce centre-scoped access check | Complex |
| Activate or deactivate centre user | Medium |
| Search centre users and mappings | Medium |
| List users by centre | Easy |
| Read mapping change history | Easy |

### Inputs
Centre user name; official email; official mobile; optional employee/reference id; role Centre/Invigilator; selected centre id(s); privilege selections for centre functions; activation status; remarks.

### Outputs
Persisted centre user account; centre mapping set; Active/Inactive status; centre-scoped authorisation usable by centre dashboard and examination-day modules; audited mapping history; users-by-centre list.

### Business Rules
- A centre user cannot see examinations or candidates of another (unmapped) centre.
- Centre users may be mapped only to Active authorised centres from the centre master (F03-002).
- An Inactive staff account cannot log in.
- Centre / Invigilator role must not receive full Examination Administrator privilege packs through this feature.
- At least one centre mapping is required before the account can be Active.
- Remapping removes access to the previous centre immediately for subsequent requests.
- Administrator accounts (F01-001) are not centre-mapped through this feature unless Department later defines dual-role accounts (out of default scope).

### Validations
- Mandatory identity fields and at least one centre mapping on activation.
- Centre ids must exist and be Active at mapping time.
- Duplicate login identity within centre staff users is rejected.
- Cannot map to a deactivated centre.
- Privilege set must be subset of Centre/Invigilator allowed privileges.

### Calculations
None beyond counts of users mapped per centre for operational lists.

### Workflow
Direct administration with audit. No maker–checker. Activation requires valid mapping; deactivation blocks login.

### Search Requirements
Name, mobile, email, centre name/code, mapping status, Active/Inactive, updated date range.

### Documents
None.

### Reports
Centre-wise mapped user list export for examination-day readiness and audit.

### Notifications
Optional notify centre user on activation or remapping if configured in Module 09; not required for core mapping behaviour.

### Security
Role- and centre-scoped access; every centre data request must pass centre-scope check; Inactive login denied; mapping and privilege changes audited with actor, centre ids and timestamp.

### Integrations
None for this feature (no SMS/KGID/payment). Centre master data is consumed internally from Module 03.

### Dependencies
F01-001 (distinct Administrator vs centre roles); F03-002 Authorised Examination Centre Master (centres to map). Consumed by Module 07 centre dashboard and invigilator activation.

### Assumptions
- One user may be mapped to multiple centres if the Department allows multi-centre invigilators; default UI supports multi-select.
- Centre master Active flag is the source of truth for mappable centres.
- Hours use Estimation Master; each named screen and logical API is billed independently.

### Risks
- Missing centre-scope checks on any centre API would leak other centres’ candidates.
- Mapping to inactive centres would allow preference/scheduling confusion later.
- Granting Administrator privileges to centre users would bypass centre isolation.

### Non Functional Requirements
Centre-scope enforcement must be consistent on every centre-scoped request; mapping changes must take effect without relying on stale client caches beyond configured session rules; register and users-by-centre lists must remain responsive for expected numbers of centres and invigilators; all privileged mapping actions attributable with audit.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Centre / Invigilator user register and search | UI | Complex | 12 |
| Centre user create / edit form | UI | Medium | 6 |
| Centre mapping assignment screen | UI | Complex | 12 |
| Centre-scoped access preview | UI | Medium | 6 |
| Centre user activate / deactivate confirmation | UI | Easy | 4 |
| Mapping and access change history | UI | Medium | 6 |
| Users-by-centre operational list | UI | Medium | 6 |
| Create Centre / Invigilator user | API | Complex | 8 |
| Update centre user particulars | API | Medium | 6 |
| Map or unmap authorised centres | API | Complex | 8 |
| Enforce centre-scoped access check | API | Complex | 8 |
| Activate or deactivate centre user | API | Medium | 6 |
| Search centre users and mappings | API | Medium | 6 |
| List users by centre | API | Easy | 4 |
| Read mapping change history | API | Easy | 4 |
| Centre user and mapping persistence | DB | Complex | 6 |
| Centre invigilator mapping feature tests | Testing | Very High | 12 |
| Centre invigilator mapping implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **123** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Centre-scope enforcement is estimated as its own logical API because incorrect scoping is a critical acceptance failure.
- No Integration row — no external channel in this feature.
- Testing is Very High due to cross-centre isolation scenarios.
