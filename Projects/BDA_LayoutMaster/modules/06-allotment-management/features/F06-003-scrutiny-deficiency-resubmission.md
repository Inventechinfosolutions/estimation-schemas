# F06-003 — Scrutiny, Deficiency & Resubmission
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F06-003 |
| **Feature Name** | Scrutiny, Deficiency & Resubmission |
| **Module** | 06 — Allotment Management |
### Description
Provide a section worklist to verify application eligibility, record deficiencies, and accept corrected resubmissions.
### Business Objective
Ensure only complete, eligible applications proceed to selection with an auditable applicant response cycle.
### Actors
Scrutiny Officer; Revenue/Allotment Section User; Applicant; Auditor.
### User Journey
Scrutiny officer opens a submitted application, completes the configured checklist, marks it eligible or issues a dated deficiency memo; applicant resubmits missing evidence; officer verifies the response and clears or rejects the application.
### Functional Capabilities
- Scrutiny worklist, checklist panel, deficiency memo composer, resubmission review, and decision history.
- Record eligibility decision, reviewer remarks, due date, and each resubmitted document version.
### Inputs
Submitted application, configured checklist, eligibility evidence, deficiency reason, due date, and resubmission files.
### Outputs
Eligible/rejected application or open/closed deficiency memo and selection-ready queue.
### Business Rules
Only submitted applications are scrutinized; applications with open deficiencies cannot be selected; a cleared application retains prior deficiency history.
### Validations
Checklist completion before final decision; deficiency reason and due date required; resubmission must target an open memo.
### Calculations
Deficiency aging and count of cleared/eligible applications by scheme.
### Workflow
Under scrutiny → deficiency issued → resubmitted → cleared or rejected; direct eligible decision is permitted when no deficiency exists.
### Search Requirements
Scheme, application reference, scrutiny status, deficiency due date, officer, and applicant.
### Documents
Scrutiny note, deficiency memo, resubmitted certificates, and rejection communication.
### Reports
Scrutiny pendency and deficiency-aging export.
### Notifications
Deficiency issue, reminder, resubmission, and decision alerts via Module 11.
### Security
Only assigned/allotted scrutiny users can decide; applicant sees only own memo and permitted remarks.
### Integrations
Citizen resubmission handoff from Module 10 (Simple).
### Dependencies
F06-002, Module 02 checklist rules, Modules 10–11.
### Assumptions
Deficiency response timelines are configured by BDA.
### Risks
Ambiguous eligibility evidence can create inconsistent decisions.
### Non Functional Requirements
Timestamped history, secure document version access, and aging-filter performance.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Scrutiny worklist and aging filters | UI | Complex | 8 |
| Checklist and decision screen | UI | Complex | 8 |
| Deficiency and resubmission review screens | UI | Very High | 16 |
| Scrutiny, memo and resubmission state processing | API | Very High | 16 |
| Checklist, memo and review persistence | Database | Complex | 6 |
| Portal resubmission handoff | Integration | Simple | 4 |
| Scrutiny lifecycle tests | Testing | Very High | 12 |
| Scrutiny procedure guide | Documentation | Medium | 3 |
| **Total** | | | **73** |
### Estimation Assumptions
Document storage is embedded in the application process; no standalone DMS is estimated.
