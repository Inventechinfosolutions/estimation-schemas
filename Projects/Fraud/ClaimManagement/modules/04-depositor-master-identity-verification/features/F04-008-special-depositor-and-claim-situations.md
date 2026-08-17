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
1. Officer flags the depositor/claim as ineligible, deceased, legal heir, joint deposit, third-party payment, lost receipt or cash investment.
2. Officer attaches supporting papers.
3. The case is routed on that workflow until resolved per Authority policy.

### Functional Capabilities
- Flag special situations listed in the SOW.
- Attach supporting papers.
- Route until resolved per policy.

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
| Situation workflow operations | API | Very High | 16 |
| Situation and routing persistence | DB | Complex | 6 |
| Special-situation tests | Testing | Very High | 12 |
| Special-situation guide | Documentation | Complex | 4 |
| **Total** | | | **66** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Workflow UI Very High and API Very High reflect routing until resolution, not a single CRUD flag.
