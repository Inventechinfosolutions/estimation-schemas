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
1. Officer or Administrator imports schemes configured on each FE in the existing application.
2. Imported schemes appear on the scheme reference register against the FE.
3. When creating a notification (F06-001), capturing an investment (F05-001) or taking a claim (F06-002/003), only imported schemes can be selected.
4. Free-text scheme names are not accepted.

### Functional Capabilities
- Import investment schemes per imported FE.
- Expose schemes as the only selectable scheme list on claim screens.
- Refuse free-text scheme entry on notification, investment and intake.

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
| Scheme import operations | API | Very High | 16 |
| Scheme reference persistence | DB | Medium | 4 |
| Existing FE application scheme import | Integration | Medium | 16 |
| Scheme import tests | Testing | Complex | 8 |
| Scheme import notes | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Notification and intake screens are estimated in Module 06; this feature estimates import and the reference register.
