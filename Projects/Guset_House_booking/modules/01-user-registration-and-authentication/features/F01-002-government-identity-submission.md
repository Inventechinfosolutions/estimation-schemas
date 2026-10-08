# F01-002 — Government Identity Submission

| Field | Value |
|-------|-------|
| Feature ID | F01-002 |
| Feature Name | Government Identity Submission |
| Module | 01 — User Registration & Authentication |
| Type | Shared |
| Notes | Go-live |

## Feature Specification

### Description
Captures mandatory government identification from the registering employee and records validation status used for booking eligibility.

### Business Objective
Ensure only users who submit required government identity artefacts can become booking-eligible.

### Actors
- Employee Guest
- Platform Administrator

### User Journey
1. Employee Guest submits identity after OTP verification.
2. Employee uploads/enters government ID type, number, and document image/file as configured.
3. Employee may replace document while status is Pending Review or Rejected.
4. Where administrative verification is enabled, employee submits for admin review; if auto-accept policy is configured, approval does not apply.
5. Platform Administrator sees pending identity review queue when manual verification is enabled.
6. Administrator accepts or rejects with reason; rejection returns employee to resubmit.
7. Employee sees identity status history (Submitted, Under Review, Accepted, Rejected).
8. Auditor sees identity decision history with actor and timestamp (document access controlled).

### Functional Capabilities
- Capture ID type and number
- Upload identity document
- Submit for verification
- Admin accept/reject with reason
- Gate booking eligibility on Accepted status

### UI Screens
- Identity submission form
- Identity document upload dialog
- Admin identity review inbox
- Identity decision dialog
- Employee identity status history

### Logical API Operations
- Save identity draft
- Submit identity for review
- List pending identity reviews
- Decide identity review
- Get identity status history

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Government ID mandatory before booking eligibility
- Rejected identity blocks booking until resubmitted and accepted
- Document retention follows client policy

### Validations
- ID type mandatory
- ID number format per type
- File type/size limits
- Decision reason mandatory on reject

### Calculations
- None beyond display counters

### Workflow
Draft → Submitted → UnderReview → Accepted | Rejected → Draft

### Search Requirements
Admin filter queue by status, date, ID type

### Documents
Government ID document upload

### Reports
None

### Notifications
Optional notify employee on accept/reject

### Security
- Encrypt/restrict identity document access
- Role-gated admin review
- Audit all decisions

### Integrations
None direct (storage embedded)

### Dependencies
- F01-001

### Assumptions
- Phase 1 verification is document capture + admin status unless client enables lighter auto-accept
- Central directory match is future scope

### Risks
- Manual review backlog delays booking eligibility

### Non Functional Requirements
- Secure document download only for authorised roles

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Identity submission form | Complex | 12 |
| UI | Identity document upload dialog | Easy | 4 |
| UI | Admin identity review inbox | Medium | 6 |
| UI | Identity decision dialog | Easy | 4 |
| UI | Employee identity status history | Easy | 4 |
| API | Save identity draft | Medium | 6 |
| API | Submit identity for review | Complex | 8 |
| API | List pending identity reviews | Medium | 6 |
| API | Decide identity review | Complex | 8 |
| API | Get identity status history | Easy | 4 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 77 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Phase 1 verification is document capture + admin status unless client enables lighter auto-accept, Central directory match is future scope / Manual review backlog delays booking eligibility.
