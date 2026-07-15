# F07-001 — Online Application Submission

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | Online Application Submission |
| **Module** | 07 — Application First Come Booking |

### Description
Capture a citizen’s selected published unit application, required supporting documents, declarations, and terms acceptance before it enters the common application workflow.

### Business Objective
Create a complete, traceable online application that can be verified and linked to booking payment.

### Actors
Citizen; Housing Officer; Configured Approver; Auditor.

### User Journey
A citizen selects an eligible published unit, reviews profile details, completes application declarations, uploads required documents, accepts terms, submits, and receives an application acknowledgement.

### Functional Capabilities
- Application wizard with selected-unit context, applicant details, declarations, document checklist, and final review.
- Application number generation, acknowledgement, and saved-draft recovery.
- Same downstream application state used by officer-assisted entries.

### Inputs
Citizen profile, selected unit, declarations, required documents, terms acceptance, and submission confirmation.

### Outputs
Application reference, submitted application package, document checklist status, and acknowledgement.

### Business Rules
Only a verified citizen may submit; an application uses a currently eligible published unit; mandatory declarations/documents must be complete; submission does not itself confirm booking.

### Validations
Citizen profile completeness, active unit visibility, required document types, declaration/terms acceptance, permitted file size/type, and duplicate active application rule as configured.

### Calculations
Application completeness percentage and document-checklist completion.

### Workflow
Draft → documents/declarations complete → submitted → verification pending → approved/rejected/clarification requested.

### Search Requirements
Application number, citizen, project, unit, submission date, channel, and application status.

### Documents
Application attachments, declarations, consent record, and acknowledgement.

### Reports
Online application register and incomplete-draft ageing.

### Notifications
Submission acknowledgement and later workflow events through Module 12.

### Security
Citizen may create/view only own applications; upload malware/file controls; immutable terms acceptance and audit history.

### Integrations
Citizen profile and inventory eligibility consumption (Medium); notification handoff (Easy).

### Dependencies
Modules 03–06, 12; F07-003.

### Assumptions
Eligibility/quota evaluation is out of baseline; required document rules are configured by BDA.

### Risks
Incomplete or poor-quality uploads can delay verification.

### Non Functional Requirements
Mobile-responsive guided journey, resumable drafts, and reliable upload feedback.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Application wizard and document checklist | UI | Very High | 16 |
| Application review and acknowledgement screens | UI | Complex | 8 |
| Submission, validation, and draft processing | API | Very High | 16 |
| Application and document-link persistence | Database | Complex | 6 |
| Profile, inventory, and notification handoffs | Integration | Medium | 16 |
| Online application tests | Testing | Very High | 12 |
| Citizen application guide | Documentation | Complex | 4 |
| **Total** | | | **78** |

### Estimation Assumptions
Booking payment and confirmation are separately estimated in F07-004 and Module 08.
