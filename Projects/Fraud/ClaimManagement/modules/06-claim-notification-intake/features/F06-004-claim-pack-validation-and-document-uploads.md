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
1. User (Officer or OOK claimant) attempts Submit.
2. System checks mandatory fields and the pack: identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable.
3. If any mandatory item is missing, Submit is blocked and gaps are listed.
4. Only a complete pack is stored as a submitted claim.
5. Later F07-002 additional documents cannot replace this first complete Submit.

### Functional Capabilities
- Shared document upload for the mandatory pack types.
- Shared field and pack validation.
- Block Submit and list gaps.
- Store as submitted only when complete.

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
| Pack validation engine | API | Very High | 16 |
| Submitted-pack persistence | DB | Complex | 6 |
| Pack validation tests | Testing | Very High | 12 |
| Mandatory pack rule guide | Documentation | Complex | 4 |
| **Total** | | | **56** |

### Estimation Assumptions
- Uses Estimation Master values only.
- This is the shared Submit engine; channel shells are F06-002/F06-003.
