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
1. Who creates: Officer
2. How they create: If a document is missing or unclear after the complete first Submit, Officer raises an additional-document request on the claim.
3. How they edit: OOK claimant or in-KA assisting staff uploads the papers.
4. How they send for approval: Officer reopens the claim, continues the checklist from where it stopped, and saves; prior ticks are not lost. Request → upload → reopen checklist (ticks retained) → continue evaluation. Embedded workflow.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Raise additional-document request on a submitted claim.
- Accept upload from OOK or in-KA assisting staff.
- Resume checklist without losing prior ticks.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Additional-document request screen | Complex |
| Claimant/staff additional upload return | Medium |
| Additional document request loop history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Additional-document loop workflow operations | Very High |
| Update additional document request loop | Medium |
| Search additional document request loop | Medium |
| Read additional document request loop history | Easy |

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
| Additional document request loop history | UI | Medium | 6 |
| Additional-document loop workflow operations | API | Very High | 16 |
| Update additional document request loop | API | Medium | 6 |
| Search additional document request loop | API | Medium | 6 |
| Read additional document request loop history | API | Easy | 4 |
| Request and resume persistence | DB | Medium | 4 |
| Additional document request loop feature tests | Testing | Complex | 8 |
| Additional document request loop implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
