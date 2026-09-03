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
1. Who creates: Officer (on Pending Clarification)
2. How they create: Competent Authority opens the verification report (F07-004).
3. How they edit: CA selects Approved, Partially Approved, Rejected or Pending Clarification, enters remarks, and saves. Draft or returned records can be edited; decided records are not silently overwritten.
4. How they send for approval: Decision, Person, Post, date/time and remarks are stored on the claim and visible to settlement (Module 08). CA review → decision → (settlement-ready or return to Officer). Stage audit: Role/Post, action, status, remarks, date/time, supporting documents.
5. How the approver sees pending items: Competent Authority opens the pending inbox for this feature and opens a row.
6. How the approver decides: Competent Authority approves, rejects or returns with remarks. Pending Clarification returns the claim for further Officer work.
7. How the applicant sees history: Officer (on Pending Clarification) opens history on the record (actor Person, Post, time, status, remarks).
8. How the approver / auditor sees history: Competent Authority and auditor open the same history for items in their scope.

### Functional Capabilities
- Record one of the four CA decisions with remarks.
- Store actor Person, Post, date/time.
- Expose decision to settlement except where Pending Clarification.
- Return Pending Clarification to Officer evaluation.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My claim approval decisions register | Medium |
| CA decision form | Complex |
| Submit confirmation | Simple |
| Approver claim approval decisions inbox | Complex |
| Claim approval decisions decision panel (approve / reject / return) | Medium |
| My claim approval decisions history | Medium |
| Team claim approval decisions history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft claim approval decisions | Medium |
| Update draft claim approval decisions | Medium |
| Decision workflow operations | Very High |
| Withdraw claim approval decisions | Easy |
| Approver inbox query | Medium |
| Approve, reject or return claim approval decisions | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

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
| My claim approval decisions register | UI | Medium | 6 |
| CA decision form | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver claim approval decisions inbox | UI | Complex | 12 |
| Claim approval decisions decision panel (approve / reject / return) | UI | Medium | 6 |
| My claim approval decisions history | UI | Medium | 6 |
| Team claim approval decisions history (approver) | UI | Medium | 6 |
| Save draft claim approval decisions | API | Medium | 6 |
| Update draft claim approval decisions | API | Medium | 6 |
| Decision workflow operations | API | Very High | 16 |
| Withdraw claim approval decisions | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return claim approval decisions | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Decision persistence | DB | Medium | 4 |
| Claim approval decisions feature tests | Testing | Very High | 12 |
| Claim approval decisions implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **127** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
