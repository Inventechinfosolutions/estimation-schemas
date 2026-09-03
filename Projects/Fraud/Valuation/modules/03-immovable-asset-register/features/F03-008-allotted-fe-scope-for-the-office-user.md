# F03-008 — Allotted-FE scope for the office user

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-008 |
| **Feature Name** | Allotted-FE scope for the office user |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
An Administrator (on the shared component / valuation allotment) maps which FEs an Office user Person may work. That Officer’s Asset create and search list only those FEs. Attempting to save an asset against a non-allotted FE is refused. A CA or named admin override can open any FE.

### Business Objective
Restrict office create and search to FEs allotted to that Person/Post, with CA/admin override.

### Actors
Administrator; Office user; Competent Authority.

### User Journey
1. Who creates: Administrator
2. How they create: Administrator maps which FEs an Office user Person may work.
3. How they edit: That Officer’s Asset create and search list only those FEs.
4. How they send for approval: Save against a non-allotted FE is refused. Map allotment → create/search filter → refuse out-of-scope save → override path for CA/admin.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record. CA or named admin override can open any FE.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Map FEs to Office user Person/Post
- Filter Asset create and search to allotted FEs
- Refuse save on non-allotted FE
- Allow CA/named admin override

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My allotted-fe scope for the office user list / queue | Medium |
| FE allotment mapping | Medium |
| Allotted-fe scope for the office user history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Allotted-FE filter and refuse | Complex |
| Update allotted-fe scope for the office user | Medium |
| Search allotted-fe scope for the office user | Medium |
| Read allotted-fe scope for the office user history | Easy |

### Inputs
Person; FE list; override flag for CA/admin.

### Outputs
Allotment map; filtered lists; refused save.

### Business Rules
- Office user creates and searches immovable assets only for allotted FEs unless override applies
- Refusal is server-side, not only hidden in the dropdown
- Login create/update/delete of Persons remains Claim Module 01

### Validations
- FE exists in programme reference
- Person is Office user Post unless override

### Calculations
None.

### Workflow
Map allotment → create/search filter → refuse out-of-scope save → override path for CA/admin.

### Search Requirements
Person, FE, allotment active, override used.

### Documents
None.

### Reports
FE allotment matrix.

### Notifications
In-app refusal on out-of-scope save.

### Security
Allotment is an access control, not a suggestion. Override is attributable.

### Integrations
Shared Person/Post plus FE reference (F02-005).

### Dependencies
F01-001; F01-002; F02-005; F03-001; F03-005.

### Assumptions
- SPLOCA supplies which Officers are allotted to which FEs.

### Risks
Missing allotment blocks legitimate create; over-broad override weakens need-to-know.

### Non Functional Requirements
Enforce on API; audit allotment changes and override opens.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My allotted-fe scope for the office user list / queue | UI | Medium | 6 |
| FE allotment mapping | UI | Medium | 6 |
| Allotted-fe scope for the office user history | UI | Medium | 6 |
| Allotted-FE filter and refuse | API | Complex | 8 |
| Update allotted-fe scope for the office user | API | Medium | 6 |
| Search allotted-fe scope for the office user | API | Medium | 6 |
| Read allotted-fe scope for the office user history | API | Easy | 4 |
| Allotted-fe scope for the office user persistence | DB | Medium | 4 |
| Shared Person and FE-reference consume | Integration | Easy | 8 |
| Allotted-FE scope for the office user feature tests | Testing | Complex | 8 |
| Allotted-FE scope for the office user implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **65** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
