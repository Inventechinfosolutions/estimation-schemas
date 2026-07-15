# F06-002 — Allotment Application Capture
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Allotment Application Capture |
| **Module** | 06 — Allotment Management |
### Description
Capture officer-assisted applications against a published scheme, including applicant details, preferences, eligibility declarations, and evidence.
### Business Objective
Create a complete application record that can enter scrutiny without rekeying or losing applicant evidence.
### Actors
Revenue/Allotment Section User; Data Entry Operator; Citizen/Applicant via Module 10; Auditor.
### User Journey
Officer selects an open scheme, searches or registers the applicant record, records category and site/layout preferences, uploads required certificates, reviews the declaration, and submits the application for scrutiny.
### Functional Capabilities
- Application register, create/edit form, applicant and preference panels, document checklist, and submission acknowledgement.
- Save draft, officer-assisted entry, portal-originated application intake, and duplicate application warning.
### Inputs
Scheme, applicant identity/contact details, category, preferences, declarations, and supporting certificates.
### Outputs
Application reference, acknowledgement, application register, and scrutiny-ready record.
### Business Rules
Applications are accepted only within the published window; one active application per applicant/scheme unless BDA permits otherwise; submitted applications are immutable except through deficiency resubmission.
### Validations
Open scheme, mandatory applicant data, allowed preference count, required documents, and duplicate applicant/scheme check.
### Calculations
Preference rank and application count by scheme/category.
### Workflow
Draft → submitted → under scrutiny; portal submissions enter the same scrutiny queue as officer entries.
### Search Requirements
Application reference, scheme, applicant name/mobile, category, submission date, and status.
### Documents
Application form, identity/KYC evidence, eligibility certificates, and declarations.
### Reports
Application register and category-wise received-count export.
### Notifications
Submission acknowledgement and scrutiny-status notification through Module 11.
### Security
Applicants access only their own submission; officers have allotted zone/section scope; PII and documents are role protected.
### Integrations
Citizen application intake from Module 10 (Simple).
### Dependencies
F06-001, Modules 01–02, Module 10, Module 11.
### Assumptions
Portal authentication and file upload channel are delivered by Module 10.
### Risks
Incomplete supporting evidence increases deficiency and resubmission volume.
### Non Functional Requirements
Responsive form, draft recovery, secure document access, acknowledgement traceability.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Application register and filters | UI | Complex | 8 |
| Officer application form with preferences | UI | Very High | 16 |
| Document checklist and acknowledgement view | UI | Complex | 8 |
| Application intake, duplicate and submission processing | API | Very High | 16 |
| Application, preference and checklist persistence | Database | Complex | 6 |
| Portal application intake | Integration | Simple | 4 |
| Application capture tests | Testing | Very High | 12 |
| Application user guide | Documentation | Medium | 3 |
| **Total** | | | **73** |
### Estimation Assumptions
Payment collection, if mandated, is owned by Module 12 and is not included.
