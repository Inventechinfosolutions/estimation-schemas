# F07-004 — Verification report for Competent Authority

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-004 |
| **Feature Name** | Verification report for Competent Authority |
| **Module** | 07 — Claim Verification, Evaluation & Approval |

### Description
When the Officer completes evaluation, the Officer generates the verification report from the checklist and remarks and marks the claim ready for CA review. The Competent Authority opens that report (not a blank claim) as the basis for decision.

### Business Objective
Give the Competent Authority a generated verification report from the checklist, not a blank claim file.

### Actors
Officer; Competent Authority.

### User Journey
1. Who creates: Officer
2. How they create: When evaluation is complete, Officer generates the verification report from the checklist and remarks.
3. How they edit: Officer marks the claim ready for CA review. Draft or returned records can be edited; decided records are not silently overwritten.
4. How they send for approval: Competent Authority opens that report (not a blank claim) as the basis for decision (F07-005). Complete evaluation → generate report → ready for CA. Pending Clarification returns from F07-005.
5. How the approver sees pending items: Competent Authority opens the pending inbox for this feature and opens a row.
6. How the approver decides: Competent Authority approves, rejects or returns with remarks.
7. How the applicant sees history: Officer opens history on the record (actor Person, Post, time, status, remarks).
8. How the approver / auditor sees history: Competent Authority and auditor open the same history for items in their scope.

### Functional Capabilities
- Generate verification report from checklist and remarks.
- Mark ready for CA review.
- CA inbox/open of the report, not a blank claim.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My verification report for competent authority register | Medium |
| Verification report generate and preview | Complex |
| Submit confirmation | Simple |
| Approver verification report for competent authority inbox | Complex |
| Verification report for competent authority decision panel (approve / reject / return) | Medium |
| My verification report for competent authority history | Medium |
| Team verification report for competent authority history (approver) | Medium |
| CA report inbox | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft verification report for competent authority | Medium |
| Update draft verification report for competent authority | Medium |
| Report generation operations | Complex |
| Withdraw verification report for competent authority | Easy |
| Approver inbox query | Medium |
| Approve, reject or return verification report for competent authority | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Completed checklist, remarks, claim identifiers.

### Outputs
Verification report linked on the claim; ready-for-CA status.

### Business Rules
- CA decision is based on this report.
- No generative drafting of the report; it is produced from structured checklist data.

### Validations
- Generate is refused if mandatory checklist items are unset per policy.

### Calculations
None beyond assembling stored checklist results.

### Workflow
Complete evaluation → generate report → ready for CA. Pending Clarification returns from F07-005.

### Search Requirements
Claims ready for CA; report by claim ID.

### Documents
Verification report as a generated artefact plus supporting pack.

### Reports
The verification report itself.

### Notifications
In-application ready-for-CA queue for the CA Post.

### Security
Only CA Post sees the CA queue. Report access need-to-know.

### Integrations
None.

### Dependencies
F07-001, F07-002.

### Assumptions
- Report layout follows Authority practice; it is not a Legal vakalat/caveat draft.

### Risks
- CA deciding on a blank claim would skip recorded verification.

### Non Functional Requirements
Report is from structured records, not a homepage PDF publish.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My verification report for competent authority register | UI | Medium | 6 |
| Verification report generate and preview | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver verification report for competent authority inbox | UI | Complex | 12 |
| Verification report for competent authority decision panel (approve / reject / return) | UI | Medium | 6 |
| My verification report for competent authority history | UI | Medium | 6 |
| Team verification report for competent authority history (approver) | UI | Medium | 6 |
| CA report inbox | UI | Medium | 6 |
| Save draft verification report for competent authority | API | Medium | 6 |
| Update draft verification report for competent authority | API | Medium | 6 |
| Report generation operations | API | Complex | 8 |
| Withdraw verification report for competent authority | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return verification report for competent authority | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Verification report persistence | DB | Medium | 4 |
| Verification report for Competent Authority feature tests | Testing | Medium | 6 |
| Verification report for Competent Authority implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
