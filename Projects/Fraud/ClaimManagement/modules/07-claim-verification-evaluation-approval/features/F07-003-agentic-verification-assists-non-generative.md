# F07-003 — Agentic verification assists (non-generative)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | Agentic verification assists (non-generative) |
| **Module** | 07 — Claim Verification, Evaluation & Approval |

### Description
While the Officer is on the checklist, rule-based or agentic assists may highlight mismatches or extracted values. The Officer must confirm or reject each suggestion. The Officer cannot skip human confirmation. No generative-AI compose action is available. Assists and Officer decisions are audited.

### Business Objective
Assist extraction and checks without auto-finalising verification and without any generative AI.

### Actors
Officer.

### User Journey
1. Who creates: Officer
2. How they create: While on the checklist, rule-based/agentic assists highlight mismatches or extracted values.
3. How they edit: Officer confirms or rejects each suggestion; skipping human confirmation is not possible.
4. How they send for approval: No generative-AI compose action is available. Assist highlight → Officer confirm/reject → checklist item updated only after confirmation.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Assists and Officer decisions are audited.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Highlight mismatches or extracted values on the checklist.
- Require confirm or reject per suggestion.
- Prohibit generative compose.
- Audit assists and Officer decisions.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Assist highlight panel | Complex |
| Confirm/reject assist actions | Easy |
| Agentic verification assists history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Non-generative assist engine operations | Very High |
| Update agentic verification assists | Medium |
| Search agentic verification assists | Medium |
| Read agentic verification assists history | Easy |

### Inputs
Checklist context, extracted/matched values, Officer confirm/reject.

### Outputs
Accepted or rejected suggestions; audit rows.

### Business Rules
- Generative AI is prohibited.
- No assist may finalise a verification decision without human confirmation and audit.
- Agentic tools are limited to assistive extraction, matching, mismatch flags and calculations.

### Validations
- Unconfirmed suggestions cannot mark a checklist item pass by themselves.

### Calculations
Rule-based mismatch/extraction only.

### Workflow
Assist highlight → Officer confirm/reject → checklist item updated only after confirmation.

### Search Requirements
Claims with pending unconfirmed assists (Officer worklist).

### Documents
None created by a model; originals remain source.

### Reports
Assist decision audit extract.

### Notifications
On-screen highlights only.

### Security
Assists cannot run as unattended decisioning. Audit in F01-010.

### Integrations
None (no generative model vendor).

### Dependencies
F07-001; F04-001 OCR working copies may feed extraction.

### Assumptions
- No generative AI components are present in verification.

### Risks
- A compose-to-claimant or auto-pass assist would fail acceptance criteria.

### Non Functional Requirements
Human verify on every assist. No generative models.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Assist highlight panel | UI | Complex | 12 |
| Confirm/reject assist actions | UI | Easy | 4 |
| Agentic verification assists history | UI | Medium | 6 |
| Non-generative assist engine operations | API | Very High | 16 |
| Update agentic verification assists | API | Medium | 6 |
| Search agentic verification assists | API | Medium | 6 |
| Read agentic verification assists history | API | Easy | 4 |
| Assist decision audit persistence | DB | Medium | 4 |
| Agentic verification assists (non-generative) feature tests | Testing | Very High | 12 |
| Agentic verification assists (non-generative) implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **74** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
