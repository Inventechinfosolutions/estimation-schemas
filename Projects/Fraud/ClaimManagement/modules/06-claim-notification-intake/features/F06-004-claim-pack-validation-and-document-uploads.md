# F06-004 — Claim pack validation and document uploads

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-004 |
| **Feature Name** | Claim pack validation and document uploads |
| **Module** | 06 — Claim Notification & Intake |

### Description
Shared Submit rule for both F06-002 (Officer) and F06-003 (OOK claimant): the claim is accepted as submitted only when identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable are present, together with mandatory fields (FE, scheme, personal, investment, refund bank). If any mandatory item is missing, the system blocks submission and lists the gaps. Only a complete pack is stored as a submitted claim. Additional documents requested later (F07-002) are after this first Submit, not a substitute for it.

### Business Objective
Enforce one complete-pack Submit rule for counter and OOK so incomplete packs are never stored as submitted claims.

### Actors
Officer (F06-002); OOK claimant (F06-003); system validation.

### User Journey
1. Who creates: Officer (F06-002)
2. How they create: User (Officer or OOK claimant) attempts Submit.
3. How they edit: System checks mandatory fields and the pack: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable.
4. How they send for approval: If any mandatory item is missing, Submit is blocked and gaps are listed. Upload → validate → block or accept as submitted.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer (F06-002) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer (F06-002) opens history on the record. Only a complete pack is stored as a submitted claim. Later F07-002 additional documents cannot replace this first complete Submit.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Shared document upload for the mandatory pack types.
- Shared field and pack validation.
- Block Submit and list gaps.
- Store as submitted only when complete.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Mandatory document upload pack | Complex |
| Submit gap list | Medium |
| Claim pack validation and document uploads history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Pack validation engine | Very High |
| Update claim pack validation and document uploads | Medium |
| Search claim pack validation and document uploads | Medium |
| Read claim pack validation and document uploads history | Easy |

### Inputs
Uploaded files by type, mandatory field set, applicability of nominee/heir.

### Outputs
Gap list; submitted claim record only when complete.

### Business Rules
- Mandatory pack: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable.
- Mandatory fields: FE, scheme, personal, investment, refund bank.
- F07-002 additional documents are after first Submit, not a substitute.
- Same rule for Officer and OOK claimant.

### Validations
- Each required type present (heir/nominee if applicable).
- File present and of allowed type per slot.

### Calculations
Gap list composition.

### Workflow
Upload → validate → block or accept as submitted.

### Search Requirements
Not a search feature; gap list is on the submit attempt.

### Documents
identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable.

### Reports
None; completeness is enforced, not reported as a substitute.

### Notifications
Gap list on Submit attempt.

### Security
Uploads follow document rights once submitted. Originals unaltered.

### Integrations
None.

### Dependencies
F06-002, F06-003; F04 identity; F05 investment.

### Assumptions
- Nominee/heir applicability is determined from KYC/special situation flags (F04-003/F04-008).

### Risks
- Treating F07-002 as a way to Submit incomplete packs would void this control.

### Non Functional Requirements
Validation must be identical on both channels at Submit time.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Mandatory document upload pack | UI | Complex | 12 |
| Submit gap list | UI | Medium | 6 |
| Claim pack validation and document uploads history | UI | Medium | 6 |
| Pack validation engine | API | Very High | 16 |
| Update claim pack validation and document uploads | API | Medium | 6 |
| Search claim pack validation and document uploads | API | Medium | 6 |
| Read claim pack validation and document uploads history | API | Easy | 4 |
| Submitted-pack persistence | DB | Complex | 6 |
| Claim pack validation and document uploads feature tests | Testing | Very High | 12 |
| Claim pack validation and document uploads implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **78** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
