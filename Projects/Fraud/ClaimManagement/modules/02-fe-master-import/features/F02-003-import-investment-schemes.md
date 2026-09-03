# F02-003 — Import Investment Schemes

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-003 |
| **Feature Name** | Import Investment Schemes |
| **Module** | 02 — FE Master Import (from existing application) |

### Description
The Officer or Administrator imports the schemes configured on each FE in the existing application. When creating a claim notification, capturing an investment, or taking in a claim, the Officer (or OOK claimant) can select only those imported schemes, not free-text scheme names.

### Business Objective
Force notification, investment capture and intake to use only imported schemes.

### Actors
Officer; Administrator; later OOK claimant (selects imported scheme only).

### User Journey
1. Who creates: Officer
2. How they create: Officer or Administrator imports schemes configured on each FE in the existing application.
3. How they edit: Imported schemes appear on the scheme reference register against the FE.
4. How they send for approval: When creating a notification (F06-001), capturing an investment (F05-001) or taking a claim (F06-002/003), only imported schemes can be selected. Trigger import → store scheme references → constrain dropdowns in Modules 05–07.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Free-text scheme names are not accepted.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Import investment schemes per imported FE.
- Expose schemes as the only selectable scheme list on claim screens.
- Refuse free-text scheme entry on notification, investment and intake.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Scheme import review | Medium |
| Imported scheme reference register | Easy |
| Import investment schemes history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Scheme import operations | Very High |
| Update import investment schemes | Medium |
| Search import investment schemes | Medium |
| Read import investment schemes history | Easy |

### Inputs
Imported FE, source scheme identifiers and names.

### Outputs
Read-only scheme references; import run result.

### Business Rules
- Claim notification, intake, investment capture and verification use only imported schemes.
- Scheme configuration remains in the existing FE application.

### Validations
- Scheme import requires parent FE.
- Duplicate scheme identifiers on the same FE do not create a second scheme identity.

### Calculations
Import counts.

### Workflow
Trigger import → store scheme references → constrain dropdowns in Modules 05–07.

### Search Requirements
FE, scheme name/identifier on the imported scheme register.

### Documents
None.

### Reports
Scheme import run log.

### Notifications
On-screen import result.

### Security
Authorised import Posts only.

### Integrations
Existing FE Management application — Investment Schemes import.

### Dependencies
F02-001.

### Assumptions
- Scheme eligibility rules for a notification are entered in F06-001 against these imported schemes.

### Risks
- Missing scheme import would block intake and investment capture.

### Non Functional Requirements
Scheme dropdowns are searchable / type-ahead on staff and OOK screens.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Scheme import review | UI | Medium | 6 |
| Imported scheme reference register | UI | Easy | 4 |
| Import investment schemes history | UI | Medium | 6 |
| Scheme import operations | API | Very High | 16 |
| Update import investment schemes | API | Medium | 6 |
| Search import investment schemes | API | Medium | 6 |
| Read import investment schemes history | API | Easy | 4 |
| Scheme reference persistence | DB | Medium | 4 |
| Existing FE application scheme import | Integration | Medium | 16 |
| Import Investment Schemes feature tests | Testing | Complex | 8 |
| Import Investment Schemes implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **79** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
