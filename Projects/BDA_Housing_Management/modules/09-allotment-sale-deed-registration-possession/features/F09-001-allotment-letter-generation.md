# F09-001 — Allotment Letter Generation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-001 |
| **Feature Name** | Allotment Letter Generation |
| **Module** | 09 — Allotment Sale Deed Registration Possession |

### Description
Generate and release the allotment letter for a confirmed booking after the required approvals, with a retrievable issue and reissue history.

### Business Objective
Provide the formal allotment artefact with correct applicant, property, financial, due-date, and policy details.

### Actors
Housing Officer; Configured Approver; Citizen; Auditor.

### User Journey
An officer selects an eligible confirmed booking, validates readiness, routes or confirms the required approval, generates the allotment letter from the approved template, releases it for citizen download, and records any later reissue.

### Functional Capabilities
- Eligible-booking worklist, readiness review, allotment-letter preview, issue, release, and reissue controls.
- Template-based letter content using booking, unit, payment, due-date, terms, cancellation policy, and signatory details.
- Issuance history and citizen download status.

### Inputs
Confirmed booking, approval outcome, BDA letter template, unit/project details, payment position, due date, signatory, and reissue reason.

### Outputs
Allotment letter, issue/reissue history, citizen release record, and updated lifecycle milestone.

### Business Rules
Letter issue requires confirmed booking and required approval; one current letter version is released; reissue preserves original traceability; financial and due-date content uses the authoritative booking/ledger values.

### Validations
Eligible booking state, approval completion, active template/signatory, required transaction data, and authorised reissue reason.

### Calculations
Displayed total cost, paid/remaining amount, and balance-payment due date from source records.

### Workflow
Booking confirmed → approval/readiness complete → letter generated → issued/released → citizen download; reissue retains history.

### Search Requirements
Allotment number, booking, citizen, project, unit, issue date, approval state, and reissue status.

### Documents
Allotment letter, approval note, and issue/reissue evidence.

### Reports
Allotment-letter issue register and pending-issuance report.

### Notifications
Letter-issued and release notices through Module 12.

### Security
Role-controlled generation/reissue, citizen-only own download, immutable issue history, and signatory/template access control.

### Integrations
Booking/ledger consumption (Medium) and notification handoff (Easy).

### Dependencies
Modules 02, 07, 08, and 12; F09-002.

### Assumptions
BDA supplies approved legal/business wording and signatory authority rules.

### Risks
Template or financial-data errors can require formal reissue.

### Non Functional Requirements
Reproducible document output, controlled access, and traceable issue timestamps.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Eligible booking, letter preview, and issue UI | UI | Complex | 8 |
| Readiness, generation, release, and reissue processing | API | Very High | 16 |
| Letter version and issue-history persistence | Database | Complex | 6 |
| Booking/ledger and notification handoffs | Integration | Medium | 16 |
| Allotment-letter tests | Testing | Very High | 12 |
| Letter issue guide | Documentation | Complex | 4 |
| **Total** | | | **62** |

### Estimation Assumptions
Template configuration is Module 02; this feature covers transaction-specific generation and release.
