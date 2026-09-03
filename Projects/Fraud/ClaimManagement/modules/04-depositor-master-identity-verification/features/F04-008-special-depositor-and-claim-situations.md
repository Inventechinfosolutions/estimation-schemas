# F04-008 — Special depositor and claim situations

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-008 |
| **Feature Name** | Special depositor and claim situations |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
The Officer flags the depositor/claim as ineligible, deceased, legal heir, joint deposit, third-party payment, lost receipt or cash investment, attaches the supporting papers, and routes the case on that workflow until it is resolved per Authority policy.

### Business Objective
Handle special situations on a recorded workflow with papers, instead of informal side notes.

### Actors
Officer; Competent Authority (as policy requires); assisting staff.

### User Journey
1. Who creates: Officer
2. How they create: Officer flags the depositor/claim as ineligible, deceased, legal heir, joint deposit, third-party payment, lost receipt or cash investment.
3. How they edit: Officer attaches supporting papers.
4. How they send for approval: The case is routed on that workflow until resolved per Authority policy. Flag → attach papers → route → resolve. Embedded workflow, not a standalone BPM product.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Flag special situations listed in the SOW.
- Attach supporting papers.
- Route until resolved per policy.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Special-situation flags and papers | Complex |
| Special-situation workflow screens | Very High |
| Special depositor and claim situations history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Situation workflow operations | Very High |
| Update special depositor and claim situations | Medium |
| Search special depositor and claim situations | Medium |
| Read special depositor and claim situations history | Easy |

### Inputs
Situation type, papers, remarks, routing target.

### Outputs
Flagged situation, workflow status, resolution record.

### Business Rules
- Each listed situation follows Authority policy (dependency on policy clarification).
- Nominee/heir papers remain mandatory on submit when applicable (F06-004).
- No generative drafting of legal-heir narratives.

### Validations
- Situation type from the closed list.
- Supporting papers required per type as policy specifies.

### Calculations
None.

### Workflow
Flag → attach papers → route → resolve. Embedded workflow, not a standalone BPM product.

### Search Requirements
Situation type, status, depositor, claim.

### Documents
Heir, death, joint, third-party, lost-receipt, cash-investment papers as applicable.

### Reports
Open special-situation caseload.

### Notifications
In-application routing to the next Post.

### Security
Situation flags and papers are need-to-know. Routing is attributable.

### Integrations
None (Legal CMS petitions are out of this SOW).

### Dependencies
F04-002/F04-003; F06 pack rules; Authority special-situation policy.

### Assumptions
- Policy for ineligible / deceased / heir / joint / third-party / lost-receipt / cash-investment is clarified by the Authority.

### Risks
- Paying a deceased or third-party case without this workflow would fail settlement controls.

### Non Functional Requirements
Workflow remains usable for Officers during claim windows.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Special-situation flags and papers | UI | Complex | 12 |
| Special-situation workflow screens | UI | Very High | 16 |
| Special depositor and claim situations history | UI | Medium | 6 |
| Situation workflow operations | API | Very High | 16 |
| Update special depositor and claim situations | API | Medium | 6 |
| Search special depositor and claim situations | API | Medium | 6 |
| Read special depositor and claim situations history | API | Easy | 4 |
| Situation and routing persistence | DB | Complex | 6 |
| Special depositor and claim situations feature tests | Testing | Very High | 12 |
| Special depositor and claim situations implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **88** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
