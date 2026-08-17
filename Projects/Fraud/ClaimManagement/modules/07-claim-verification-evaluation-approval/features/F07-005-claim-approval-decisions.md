# F07-005 — Claim approval decisions

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-005 |
| **Feature Name** | Claim approval decisions |
| **Module** | 07 — Claim Verification, Evaluation & Approval |

### Description
The Competent Authority opens the verification report, selects Approved, Partially Approved, Rejected or Pending Clarification, enters remarks, and saves. The decision, Person, Post, date/time and remarks are stored on the claim and visible to settlement. Pending Clarification returns the claim for further Officer work.

### Business Objective
Record a complete, attributable CA decision so settlement sees approved liability and Pending Clarification returns to the Officer.

### Actors
Competent Authority; Officer (on Pending Clarification).

### User Journey
1. Competent Authority opens the verification report (F07-004).
2. CA selects Approved, Partially Approved, Rejected or Pending Clarification, enters remarks, and saves.
3. Decision, Person, Post, date/time and remarks are stored on the claim and visible to settlement (Module 08).
4. Pending Clarification returns the claim for further Officer work.

### Functional Capabilities
- Record one of the four CA decisions with remarks.
- Store actor Person, Post, date/time.
- Expose decision to settlement except where Pending Clarification.
- Return Pending Clarification to Officer evaluation.

### Inputs
Verification report, decision value, remarks.

### Outputs
Decision on the claim; settlement visibility; return-to-Officer when pending.

### Business Rules
- Decisions and remarks are complete, attributable and audited.
- Pending Clarification is not a settlement-ready approval.
- No generative remarks compose.

### Validations
- Decision is one of the four values.
- Remarks are mandatory.

### Calculations
None (net payable is F08-001 on approved liability).

### Workflow
CA review → decision → (settlement-ready or return to Officer). Stage audit: Role/Post, action, status, remarks, date/time, supporting documents.

### Search Requirements
Claims by CA decision, FE, window.

### Documents
Supporting documents on the stage audit as attached.

### Reports
Decision counts appear on F09-004 dashboards.

### Notifications
In-application return to Officer on Pending Clarification.

### Security
Only Competent Authority Post records these decisions. Forensic audit of approval events.

### Integrations
None (Legal petitions out of scope).

### Dependencies
F07-004; Module 01 CA Post; Module 08 consumes approved decisions.

### Assumptions
- Partial approval amount treatment for settlement is confirmed with the Authority if not explicit in the checklist.

### Risks
- Unattributed decisions would fail forensic audit of approval.

### Non Functional Requirements
Approval events retrievable. Human decision only.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| CA decision form | UI | Complex | 12 |
| Decision workflow operations | API | Very High | 16 |
| Decision persistence | DB | Medium | 4 |
| CA decision tests | Testing | Very High | 12 |
| CA decision guide | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
- Uses Estimation Master values only.
- API Very High is decision workflow including Pending Clarification return, not a simple CRUD status.
