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
1. OOK claimant logs into the constrained path (F01-008) during an open window.
2. Claimant selects imported FE, scheme and investment and confirms personal, investment and refund-bank details.
3. Claimant uploads the same mandatory pack as F06-002: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable.
4. Submit is allowed only when that full pack and mandatory fields are present; otherwise gaps are listed and Submit is blocked.

### Functional Capabilities
- Constrained OOK submit wizard.
- Same mandatory pack and fields as in-KA staff intake.
- Same block-and-list-gaps behaviour.
- Own pack only; no staff menus.

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
| OOK submit and gap-list operations | API | Very High | 16 |
| OOK submit persistence | DB | Complex | 6 |
| OOK submit tests | Testing | Very High | 12 |
| OOK submit guide | Documentation | Complex | 4 |
| **Total** | | | **60** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Shared validation engine hours are in F06-004; this feature estimates the OOK wizard and channel constraints.
