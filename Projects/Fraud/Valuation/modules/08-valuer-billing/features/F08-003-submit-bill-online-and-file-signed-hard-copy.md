# F08-003 — Submit bill online and file signed hard copy

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-003 |
| **Feature Name** | Submit bill online and file signed hard copy |
| **Module** | 08 — Valuer Billing |

### Description
The officer submits the bill online against the assignment and uploads the signed hard-copy scan. Either missing item leaves the bill in incomplete status. The valuer and CA can see submitted status; payment execution remains outside this SOW unless the Authority later orders it.

### Business Objective
File both the online bill and the signed hard copy against the assignment.

### Actors
Billing officer; Approved Valuer (sees status); Competent Authority (sees status).

### User Journey
1. Officer submits the bill online against the assignment and uploads the signed hard-copy scan.
2. Either missing item leaves incomplete status.
3. Valuer and CA can see submitted status. Payment execution is not in this SOW.

### Functional Capabilities
- Online submit against the assignment
- Upload signed hard-copy scan
- Incomplete until both present
- Status visible to valuer and CA; no payment run

### Inputs
Online submit action; signed hard-copy file.

### Outputs
Submitted bill; uploaded scan; status complete/incomplete.

### Business Rules
- Both required for complete
- Payment execution out of scope

### Validations
- Bill exists (F08-002)
- File is a scan of the signed copy as uploaded

### Calculations
None.

### Workflow
Submit online → upload scan → complete when both stored.

### Search Requirements
Assignment, bill status, submit date.

### Documents
Signed hard-copy scan.

### Reports
Incomplete vs submitted bills.

### Notifications
In-app incomplete status.

### Security
Billing officer submits; valuer/CA read status.

### Integrations
Internal document storage for the scan.

### Dependencies
F08-002.

### Assumptions
- Payment/treasury is separately ordered if needed.

### Risks
Complete status without a readable signed scan.

### Non Functional Requirements
Both artefacts stored against the assignment.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Online submit and hard-copy upload | UI | Medium | 6 |
| Submit and incomplete status | API | Medium | 6 |
| Submit and scan metadata | Database | Easy | 2 |
| Internal scan storage | Integration | Simple | 4 |
| Submit/hard-copy tests | Testing | Medium | 6 |
| Bill submit note | Documentation | Easy | 2 |
| **Total** | | | **26** |

### Estimation Assumptions
- No payment-gateway Integration Very High.
