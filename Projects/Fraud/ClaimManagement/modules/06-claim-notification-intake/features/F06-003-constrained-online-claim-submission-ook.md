# F06-003 — Constrained online claim submission (OOK)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-003 |
| **Feature Name** | Constrained online claim submission (OOK) |
| **Module** | 06 — Claim Notification & Intake |

### Description
An out-of-Karnataka claimant logs into the constrained path during an open window, selects imported FE, scheme and investment, confirms personal, investment and refund-bank details, and uploads the same mandatory document pack as F06-002 (identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable). Submit is allowed only when that full pack and the mandatory fields are present. The system applies the same block-and-list-gaps behaviour as staff-mediated intake.

### Business Objective
Let OOK claimants submit only their own pack during an open window, with the same complete-pack Submit rule as the counter.

### Actors
OOK claimant; Officer (does not replace OOK submit).

### User Journey
1. Who creates: OOK claimant
2. How they create: OOK claimant logs into the constrained path (F01-008) during an open window.
3. How they edit: Claimant selects imported FE, scheme and investment and confirms personal, investment and refund-bank details.
4. How they send for approval: Claimant uploads the same mandatory pack as F06-002: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable. OOK login → capture → shared validate → Submit or block.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. OOK claimant works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: OOK claimant opens history on the record. Submit is allowed only when that full pack and mandatory fields are present; otherwise gaps are listed and Submit is blocked.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Constrained OOK submit wizard.
- Same mandatory pack and fields as in-KA staff intake.
- Same block-and-list-gaps behaviour.
- Own pack only; no staff menus.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| OOK submit wizard | Very High |
| OOK own-pack status | Medium |
| Constrained online claim submission history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| OOK submit and gap-list operations | Very High |
| Update constrained online claim submission | Medium |
| Search constrained online claim submission | Medium |
| Read constrained online claim submission history | Easy |

### Inputs
OOK session, imported FE/scheme/investment, confirmed fields, document files.

### Outputs
Submitted claim if complete; otherwise blocked Submit with gap list.

### Business Rules
- Submit requires the full mandatory pack: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable.
- Same Submit rule as F06-002; F06-004 is the shared engine.
- Cannot file after the window closes; cannot see other claimants’ packs.

### Validations
- Open window and own-pack scope (F01-008).
- Mandatory fields and document types identical to staff-mediated intake.

### Calculations
Gap list of missing types and fields.

### Workflow
OOK login → capture → shared validate → Submit or block.

### Search Requirements
Claimant has no cross-claimant search; selects own FE/scheme/investment only as allowed.

### Documents
Same mandatory pack: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable.

### Reports
None for the claimant.

### Notifications
On-screen gap list.

### Security
Constrained path only. No staff 2FA enrolment. Need-to-know is own pack.

### Integrations
None (F06-005 covers existing limited online access outcomes).

### Dependencies
F01-008, F06-001, F06-004, F04, F05, F02.

### Assumptions
- Not a rebuild of sploca.org as a mass public portal.

### Risks
- A weaker OOK pack rule than the counter would create two Submit standards.

### Non Functional Requirements
OOK path is limited and simple. Official domain is not .org as primary hosting identity.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| OOK submit wizard | UI | Very High | 16 |
| OOK own-pack status | UI | Medium | 6 |
| Constrained online claim submission history | UI | Medium | 6 |
| OOK submit and gap-list operations | API | Very High | 16 |
| Update constrained online claim submission | API | Medium | 6 |
| Search constrained online claim submission | API | Medium | 6 |
| Read constrained online claim submission history | API | Easy | 4 |
| OOK submit persistence | DB | Complex | 6 |
| Constrained online claim submission (OOK) feature tests | Testing | Very High | 12 |
| Constrained online claim submission (OOK) implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **82** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
