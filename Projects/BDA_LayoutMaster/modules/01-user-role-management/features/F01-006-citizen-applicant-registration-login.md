# F01-006 — Citizen & Applicant Registration/Login
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F01-006 |
| **Feature Name** | Citizen & Applicant Registration/Login |
| **Module** | 01 — User & Role Management |
### Description
Register citizen/applicant identities and provide authenticated portal access for enabled services.
### Business Objective
Establish a secure reusable identity for citizen-facing journeys.
### Actors
Citizen/Applicant; Super Administrator; support officer.
### User Journey
Citizen registers identity and contact information, verifies credentials as configured, signs in, and accesses only their permitted services and records.
### Functional Capabilities
Registration, profile maintenance, login, credential reset, account status management, and identity audit.
### Inputs
Name, contact details, login credentials, and consent/verification data as configured.
### Outputs
Citizen account, authenticated portal session, registration confirmation.
### Business Rules
Citizens can access only permitted published content and their own applications; optional eKYC is excluded.
### Validations
Required contact data, unique login identity, password policy, consent acknowledgement.
### Calculations
None.
### Workflow
Register → verify/activate as configured → authenticate → access eligible portal services.
### Search Requirements
Support staff search by name, mobile/email, account status.
### Documents
Identity/KYC documents, if required by a downstream business process, remain embedded there.
### Reports
Citizen registration activity export.
### Notifications
Registration and reset notifications.
### Security
PII protection, self-service access boundary, audit, and session protection.
### Integrations
Internal notification service (Simple).
### Dependencies
F01-004 and Module 10 portal experience.
### Assumptions
Registration is local; DigiLocker/Aadhaar eKYC is optional Module 12 scope.
### Risks
Duplicate or inaccurate citizen contact data affects access and notifications.
### Non Functional Requirements
Mobile-responsive UI; accessible registration; privacy controls.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Citizen registration and login | UI | Complex | 8 |
| Profile and credential recovery | UI | Complex | 8 |
| Registration and profile operations | API | Complex | 8 |
| Citizen identity persistence | Database | Complex | 6 |
| Internal notification handoff | Integration | Simple | 4 |
| Citizen identity tests | Testing | Very High | 12 |
| Citizen registration guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
Portal business journeys are estimated in their owning modules.
