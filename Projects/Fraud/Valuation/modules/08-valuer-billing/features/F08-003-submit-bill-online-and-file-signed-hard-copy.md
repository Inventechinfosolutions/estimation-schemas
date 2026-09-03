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
1. Who creates: Billing officer
2. How they create: Officer submits the bill online against the assignment and uploads the signed hard-copy scan.
3. How they edit: Either missing item leaves incomplete status.
4. How they send for approval: Valuer and CA can see submitted status. Payment execution is not in this SOW. Submit online → upload scan → complete when both stored.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Billing officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Billing officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Online submit against the assignment
- Upload signed hard-copy scan
- Incomplete until both present
- Status visible to valuer and CA; no payment run

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My submit bill online and file signed hard copy list / queue | Medium |
| Online submit and hard-copy upload | Medium |
| Submit bill online and file signed hard copy history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Submit and incomplete status | Medium |
| Update submit bill online and file signed hard copy | Medium |
| Search submit bill online and file signed hard copy | Medium |
| Read submit bill online and file signed hard copy history | Easy |

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
|---|---|---|---|
| My submit bill online and file signed hard copy list / queue | UI | Medium | 6 |
| Online submit and hard-copy upload | UI | Medium | 6 |
| Submit bill online and file signed hard copy history | UI | Medium | 6 |
| Submit and incomplete status | API | Medium | 6 |
| Update submit bill online and file signed hard copy | API | Medium | 6 |
| Search submit bill online and file signed hard copy | API | Medium | 6 |
| Read submit bill online and file signed hard copy history | API | Easy | 4 |
| Submit bill online and file signed hard copy persistence | DB | Medium | 4 |
| Internal scan storage | Integration | Simple | 4 |
| Submit bill online and file signed hard copy feature tests | Testing | Medium | 6 |
| Submit bill online and file signed hard copy implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **56** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
