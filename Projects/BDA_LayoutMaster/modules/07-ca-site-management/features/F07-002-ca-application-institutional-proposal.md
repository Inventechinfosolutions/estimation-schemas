# F07-002 — CA Application & Institutional Proposal
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | CA Application & Institutional Proposal |
| **Module** | 07 — CA Site Management |
### Description
Register an institutional application or officer-received proposal against an available CA site and scrutinize its purpose, eligibility, and documents.
### Business Objective
Provide a complete recommendation case for CA allotment, assignment, or lease decisions.
### Actors
CA Site Section User; institutional applicant; scrutiny/committee user; Auditor.
### User Journey
Officer selects an available CA site, captures institution and project-purpose details, records requested tenure/terms, uploads constitutional and compliance documents, completes scrutiny, and submits a recommendation.
### Functional Capabilities
- Proposal register, institutional profile/proposal form, CA-site availability selection, document checklist, and scrutiny recommendation.
### Inputs
CA site, institution details, beneficiary type, project note, requested terms, certificates, and recommendation remarks.
### Outputs
CA proposal reference, scrutiny decision, and approval-ready recommendation.
### Business Rules
Only available CA sites are proposed; one active proposal may reserve a CA site; incomplete proposals cannot be recommended.
### Validations
CA eligibility, required institution/purpose data, mandatory documents, active site availability, and duplicate applicant/site check.
### Calculations
Proposal aging and available/reserved CA-site counts.
### Workflow
Draft → submitted → scrutiny/committee recommendation → approval in F07-003; returned proposals support resubmission.
### Search Requirements
Proposal reference, site, institution, purpose, zone, status, and submission date.
### Documents
Institution registration, project purpose note, certificates, and scrutiny note.
### Reports
CA proposal and scrutiny-pendency registers.
### Notifications
Submission, return, and recommendation alerts via Module 11.
### Security
CA role scope; institutional documents restricted to decision makers.
### Integrations
Optional portal intake via Module 10 (Simple).
### Dependencies
F07-001, Modules 02, 10–11.
### Assumptions
Institutional proposal fields and checklist are BDA-configured.
### Risks
Unclear beneficiary eligibility can delay committee recommendations.
### Non Functional Requirements
Secure document access, auditable case history, responsive proposal entry.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Proposal register and filters | UI | Complex | 8 |
| Institutional proposal and term request form | UI | Very High | 16 |
| Scrutiny checklist and recommendation view | UI | Complex | 8 |
| Proposal, reservation and scrutiny processing | API | Very High | 16 |
| Proposal and document-checklist persistence | Database | Complex | 6 |
| Portal intake handoff | Integration | Simple | 4 |
| Proposal lifecycle tests | Testing | Very High | 12 |
| Proposal guide | Documentation | Medium | 3 |
| **Total** | | | **73** |
