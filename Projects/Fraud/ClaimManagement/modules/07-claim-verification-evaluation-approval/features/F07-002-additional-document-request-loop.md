# F07-002 — Additional document request loop

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | Additional document request loop |
| **Module** | 07 — Claim Verification, Evaluation & Approval |

### Description
If a document is missing or unclear, the Officer raises an additional-document request on the claim. The claimant (OOK) or assisting staff (in-KA) uploads the papers. The Officer reopens the claim, continues the checklist from where it stopped, and saves; prior ticks are not lost.

### Business Objective
Request additional documents after first Submit without losing prior checklist work and without replacing the mandatory first pack.

### Actors
Officer; OOK claimant (own pack); assisting staff (in-KA).

### User Journey
1. If a document is missing or unclear after the complete first Submit, Officer raises an additional-document request on the claim.
2. OOK claimant or in-KA assisting staff uploads the papers.
3. Officer reopens the claim, continues the checklist from where it stopped, and saves; prior ticks are not lost.

### Functional Capabilities
- Raise additional-document request on a submitted claim.
- Accept upload from OOK or in-KA assisting staff.
- Resume checklist without losing prior ticks.

### Inputs
Request text/types, uploaded additional papers.

### Outputs
Request status; additional papers on the claim; resumed checklist.

### Business Rules
- This loop is after first Submit; it is not a substitute for F06-004 mandatory pack.
- Prior checklist ticks are retained.
- In-KA still uses assisting staff, not a new mass portal.

### Validations
- Request requires at least one document type or instruction.
- Upload attaches to the same claim.

### Calculations
None.

### Workflow
Request → upload → reopen checklist (ticks retained) → continue evaluation. Embedded workflow.

### Search Requirements
Claims with open additional-document requests.

### Documents
Additional papers as requested (not a replacement for identity/investment/bank/affidavit/statement/heir-if-applicable at first Submit).

### Reports
Open additional-document request list.

### Notifications
In-application request to OOK own pack or staff queue.

### Security
Uploads need-to-know. Request and resume audited.

### Integrations
None.

### Dependencies
F07-001, F06-004, F01-008 for OOK.

### Assumptions
- First Submit already had the mandatory pack; this is for missing-or-unclear extras.

### Risks
- Using this loop to accept an incomplete first Submit would bypass F06-004.

### Non Functional Requirements
Resume must not lose prior checks. Usable for both channels.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Additional-document request screen | UI | Complex | 12 |
| Claimant/staff additional upload return | UI | Medium | 6 |
| Additional-document loop workflow operations | API | Very High | 16 |
| Request and resume persistence | DB | Medium | 4 |
| Additional-document loop tests | Testing | Complex | 8 |
| Additional-document loop guide | Documentation | Medium | 3 |
| **Total** | | | **49** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Workflow API Very High because resume-without-loss is not standard CRUD.
