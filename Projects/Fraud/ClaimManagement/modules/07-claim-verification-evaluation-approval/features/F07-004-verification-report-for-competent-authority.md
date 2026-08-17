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
1. When evaluation is complete, Officer generates the verification report from the checklist and remarks.
2. Officer marks the claim ready for CA review.
3. Competent Authority opens that report (not a blank claim) as the basis for decision (F07-005).

### Functional Capabilities
- Generate verification report from checklist and remarks.
- Mark ready for CA review.
- CA inbox/open of the report, not a blank claim.

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
| Verification report generate and preview | UI | Complex | 12 |
| CA report inbox | UI | Medium | 6 |
| Report generation operations | API | Complex | 8 |
| Verification report persistence | DB | Medium | 4 |
| Verification report tests | Testing | Medium | 6 |
| Verification report note | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Uses Estimation Master values only.
- CA decision control is F07-005.
