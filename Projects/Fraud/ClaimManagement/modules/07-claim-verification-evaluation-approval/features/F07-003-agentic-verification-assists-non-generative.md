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
1. While on the checklist, rule-based/agentic assists highlight mismatches or extracted values.
2. Officer confirms or rejects each suggestion; skipping human confirmation is not possible.
3. No generative-AI compose action is available.
4. Assists and Officer decisions are audited.

### Functional Capabilities
- Highlight mismatches or extracted values on the checklist.
- Require confirm or reject per suggestion.
- Prohibit generative compose.
- Audit assists and Officer decisions.

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
| Non-generative assist engine operations | API | Very High | 16 |
| Assist decision audit persistence | DB | Medium | 4 |
| Agentic assist tests | Testing | Very High | 12 |
| Non-generative assist guide | Documentation | Complex | 4 |
| **Total** | | | **52** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Hours include rule-based assists only; no generative-model licence or LLM integration is estimated.
