# F10-005 — Application Status & Document Download
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F10-005 |
| **Feature Name** | Application Status & Document Download |
| **Module** | 10 — Citizen & Public Portal |
### Description
Let applicants view their own status and download enabled acknowledgements or orders.
### Business Objective
Deliver the required Phase 1 BDA process with traceable decisions and operational visibility.
### Actors
Public Visitor; Citizen/Applicant; BDA Content Publisher.
### User Journey
Applicant opens My Applications, views permitted timeline, and downloads issued documents.
### Functional Capabilities
- Named register, detail workspace, status/history, authorised actions, and export.
### Inputs
Authorised action, source record, configured rules, status, evidence, and relevant documents.
### Outputs
Controlled result, searchable history, status, and permitted published/operational view.
### Business Rules
Applicant sees only their own records and BDA-permitted remarks/document versions.
### Validations
Required source, valid state transition, mandatory data/evidence, duplicate/conflict, and access checks.
### Calculations
Status counts, aging, and dates derived from authoritative records.
### Workflow
Draft/event → validate → process/approve as configured → outcome or visible exception.
### Search Requirements
Reference, layout/site or application, zone, status, date, and responsible user.
### Documents
Source evidence, approval/exception correspondence, and issued records where applicable.
### Reports
Feature register, status/exception summary, and export.
### Notifications
Relevant alerts use Module 11.
### Security
RBAC, zone/department scope, protected records/documents, and immutable audit.
### Integrations
Internal LMS service handoff (Simple).
### Dependencies
Modules 01, 03–04; owning source module and Module 11.
### Assumptions
BDA supplies final rules, integration access, and authoritative source data.
### Risks
Source data quality, changing policy, and external-service readiness may affect delivery.
### Non Functional Requirements
Responsive UI, auditability, error handling, secure access, and production logging.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Named operational register | UI | Complex | 8 |
| Named feature workspace | UI | Complex | 8 |
| Business processing | API | Complex | 8 |
| Business history | Database | Complex | 6 |
| Internal handoff | Integration | Simple | 4 |
| Feature tests | Testing | Complex | 8 |
| Operations guide | Documentation | Medium | 3 |
| **Total** | | | **42** |
