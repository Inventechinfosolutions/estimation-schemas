# F06-004 — Selection Method Recording
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F06-004 |
| **Feature Name** | Selection Method Recording |
| **Module** | 06 — Allotment Management |
### Description
Record the BDA-approved selection outcome for a scheme using priority rules, lottery/draw, or committee recommendation.
### Business Objective
Produce a traceable recommended allottee list from scrutiny-cleared applications without hardcoding one selection method.
### Actors
Revenue/Allotment Officer; Selection Committee Secretary; Approver; Auditor.
### User Journey
Officer chooses the configured method for a closed scheme, reviews eligible applications and sites, records ranking/draw proceedings/committee recommendation, attaches evidence, and submits the recommendation list for allotment approval.
### Functional Capabilities
- Selection batch register, candidate/site matching grid, priority ranking view, draw-proceedings capture, and committee recommendation screen.
- Freeze an approved recommendation snapshot and retain excluded-candidate reasons.
### Inputs
Eligible application list, available sites, configured selection method, ranks/draw result/committee minutes, and remarks.
### Outputs
Recommended allottee-to-site list, selection proceedings, and approval-ready batch.
### Business Rules
Only scrutiny-cleared applications and available pool sites may be selected; a site and applicant cannot occur twice in an active selection batch; the selected method is recorded for audit.
### Validations
Full one-to-one mapping, no duplicate site/applicant, required method evidence, and selection only after scheme closure where configured.
### Calculations
Priority rank, selected/reserve/unselected counts, and remaining site count.
### Workflow
Prepare → validate → submit recommendation → approval in F06-005; changes after submission require return.
### Search Requirements
Scheme, selection batch, method, application reference, site, recommendation status.
### Documents
Draw proceedings, committee minutes, priority evidence, and selection note.
### Reports
Recommended, reserve, and unselected applicant lists.
### Notifications
Recommendation submitted/returned alerts through Module 11.
### Security
Restricted to selection roles; evidence and snapshot cannot be altered after approval submission.
### Integrations
None beyond internal application/site availability checks.
### Dependencies
F06-001, F06-003, Modules 02 and 04.
### Assumptions
BDA finalizes the applicable selection method per scheme.
### Risks
Unclear draw controls or committee criteria may require rules clarification.
### Non Functional Requirements
Auditable immutable snapshot and exportable selection records.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Selection batch register | UI | Complex | 8 |
| Candidate-to-site selection workspace | UI | Very High | 16 |
| Proceedings and recommendation screen | UI | Complex | 8 |
| Ranking, selection validation and snapshot processing | API | Very High | 16 |
| Selection batch and recommendation persistence | Database | Complex | 6 |
| Selection method regression tests | Testing | Very High | 12 |
| Selection operations guide | Documentation | Medium | 3 |
| **Total** | | | **69** |
### Estimation Assumptions
The feature records BDA-approved selection methods; it does not implement an external e-lottery service.
