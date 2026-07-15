# F09-002 — Draft Sale Deed Generate, Revise & Approve

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Draft Sale Deed Generate, Revise & Approve |
| **Module** | 09 — Allotment Sale Deed Registration Possession |

### Description
Generate an in-system draft sale deed after full payment, enable authorised review and revision, and preserve every version and approval outcome before offline registration.

### Business Objective
Create a controlled, legally traceable deed package for the offline registration process.

### Actors
Housing Officer; Registration Section; Configured Approvers; Citizen; Auditor.

### User Journey
An officer opens a fully paid allotment, generates a draft using the approved template and transaction data, reviews/revises it with remarks, routes the selected version for approval, then releases the approved draft for the offline registration package and citizen download where enabled.

### Functional Capabilities
- Deed-eligible worklist, generation preview, version comparison/list, review/revise controls, and approval timeline.
- Template merge of parties, property measurements, consideration, payment details, schedule, and terms.
- Approved-draft release and preserved superseded-version history.

### Inputs
Fully paid booking/allotment, approved deed template, party/property details, measurements, consideration/payment data, review remarks, revised content, and approval actions.

### Outputs
Draft sale deed versions, approved version, approval history, released registration package, and status update.

### Business Rules
Draft deed can be generated only after full payment; only an approved version may be used for offline registration; revised versions never overwrite approved/superseded history; registration remains offline.

### Validations
Full-payment condition, complete party/property/measurement data, active template, authorised reviser/approver, and valid version state.

### Calculations
No independent pricing calculation; consideration and payment details are drawn from authoritative booking and ledger values.

### Workflow
Fully paid → draft generated → review/revise → approval → approved draft released → offline registration pending.

### Search Requirements
Deed number, booking/allotment, citizen, project, unit, version, approval state, generated date, and registration readiness.

### Documents
Draft deed versions, review remarks, approval note, and approved registration package.

### Reports
Draft deed register, version history, approval pendency, and registration-ready list.

### Notifications
Review/approval tasks and approved-draft availability through Module 12.

### Security
Strict role separation for drafting/revising/approving, version immutability, citizen access only to released approved draft, and full audit.

### Integrations
Booking/allotment/ledger data consumption (Medium) and notification handoff (Easy).

### Dependencies
F09-001, F09-003, Modules 02, 07, 08, and 12.

### Assumptions
BDA provides deed templates and legal review decisions; online Sub-Registrar/Kaveri integration is excluded.

### Risks
Incomplete legal or property data can delay approval; uncontrolled template changes risk inconsistent deed wording.

### Non Functional Requirements
Secure version handling, accurate document rendering, responsive review queues, and long-term audit retention.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Deed eligibility, editor/review, and version UI | UI | Very High | 16 |
| Deed generation, revision, and approval processing | API | Very High | 16 |
| Deed version and approval persistence | Database | Very High | 10 |
| Booking/ledger and notification handoffs | Integration | Medium | 16 |
| Deed lifecycle tests | Testing | Very High | 12 |
| Deed process guide | Documentation | Very High | 6 |
| **Total** | | | **76** |

### Estimation Assumptions
This estimate includes deed lifecycle and document versions; external legal drafting services and online registration integration are excluded.
