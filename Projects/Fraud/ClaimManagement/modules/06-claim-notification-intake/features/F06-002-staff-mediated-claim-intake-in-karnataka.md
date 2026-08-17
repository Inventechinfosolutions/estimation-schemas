# F06-002 — Staff-mediated claim intake (in-Karnataka)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Staff-mediated claim intake (in-Karnataka) |
| **Module** | 06 — Claim Notification & Intake |

### Description
An in-Karnataka claimant presents original documents at the counter. The Officer selects imported FE, scheme and investment record, confirms personal, investment and refund-bank details, and uploads the pack from the originals. At Submit, the Officer must have all mandatory documents: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable — plus all mandatory fields. If any of these is missing, the Officer cannot submit; the system blocks submission and lists the gaps. The claimant does not self-file online.

### Business Objective
Take in-KA claims only from originals at the counter, and refuse Submit until the full mandatory pack and fields are present.

### Actors
Officer; in-KA claimant (presents originals; no self-service account).

### User Journey
1. In-Karnataka claimant presents original documents at the counter (BSA 2023).
2. Officer confirms an Active claim window (F06-001) and selects imported FE, scheme and investment record.
3. Officer confirms personal, investment and refund-bank details and uploads the pack from the originals.
4. At Submit, the system requires identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable, plus mandatory fields.
5. If anything is missing, Submit is blocked and gaps are listed; the claimant does not self-file online.

### Functional Capabilities
- Staff-mediated counter intake from originals.
- Select imported FE, scheme and investment.
- Confirm personal, investment and refund-bank details.
- Block Submit and list gaps when the mandatory pack or fields are incomplete.
- No in-KA self-service filing account.

### Inputs
Originals at counter, imported FE/scheme/investment, personal/investment/refund-bank fields, document files.

### Outputs
Submitted claim only when complete; otherwise blocked Submit with gap list.

### Business Rules
- Submit requires the full mandatory pack: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable.
- Additional documents requested later (F07-002) are after this first Submit, not a substitute for it.
- Channel split is statutory (BSA 2023 originals for in-KA).

### Validations
- Window must be Active.
- Mandatory fields: FE, scheme, personal, investment, refund bank.
- Each mandatory document type present (nominee/heir if applicable).

### Calculations
Gap list of missing types and fields.

### Workflow
Counter capture → validate pack (F06-004 shared rule) → Submit or block. Embedded workflow.

### Search Requirements
Officer searches depositor, investment, FE, scheme during intake.

### Documents
Mandatory pack: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable.

### Reports
Intake gap list on-screen; submitted claim enters F07.

### Notifications
On-screen gap list; no claimant self-service mail required.

### Security
Officer Person/Post attributed. Originals digitised; source files immutable. Need-to-know on the pack.

### Integrations
None (existing limited online access is F06-005).

### Dependencies
F06-001, F06-004, F04, F05, F02, F01.

### Assumptions
- Scanning at the counter is by Officers/assisting staff; a scanning bureau is out of scope unless ordered.

### Risks
- Allowing in-KA self-file would break the statutory originals requirement.
- Accepting incomplete Submit would shift mandatory papers into F07-002 incorrectly.

### Non Functional Requirements
Staff-mediated intake must be usable with original physical documents. Searchable dropdowns for FE/scheme.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Counter intake wizard | UI | Very High | 16 |
| Mandatory pack checklist (in-KA) | UI | Complex | 12 |
| Intake submit and gap-list operations | API | Very High | 16 |
| Staff-intake persistence | DB | Complex | 6 |
| In-KA intake tests | Testing | Very High | 12 |
| Staff-mediated intake guide | Documentation | Complex | 4 |
| **Total** | | | **66** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Shared pack-validation engine is also estimated in F06-004; this feature estimates the counter wizard and in-KA channel rules.
