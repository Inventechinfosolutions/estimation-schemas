# F06-001 — Citizen OTP Registration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | Citizen OTP Registration |
| **Module** | 06 — Citizen Registration Portal |

### Description
Register a citizen using the mandated identity, contact, address, photograph, and signature details, with mobile verification before the account is activated.

### Business Objective
Establish a verified citizen record before any housing transaction can be initiated.

### Actors
Prospective Citizen; Citizen Support Officer; Auditor.

### User Journey
A visitor enters the registration details, requests a one-time password on the declared mobile number, verifies it within the allowed attempt window, accepts the portal terms, and receives a registered-account acknowledgement.

### Functional Capabilities
- Responsive registration form with staged identity/contact capture and document/image attachment.
- OTP request, verification, resend, expiry, and attempt-status feedback.
- Duplicate-registration guidance without exposing existing citizen information.

### Inputs
Name, date of birth, gender, Aadhaar, PAN, mobile, email, address, photograph, signature, consent, and OTP.

### Outputs
Verified citizen profile, registration reference, audit entry, and acknowledgement.

### Business Rules
Registration completes only after a successful mobile OTP; one active portal identity is permitted per verified mobile; Aadhaar and PAN handling follows BDA-approved masking and access policy.

### Validations
Mandatory demographic fields, date-of-birth plausibility, mobile/email format, OTP expiry/attempt limit, consent acceptance, permitted file type and size.

### Calculations
OTP expiry countdown and remaining verification-attempt count.

### Workflow
Draft registration → OTP requested → OTP verified → registration complete; expired or failed verification returns to pending verification.

### Search Requirements
Support users may search the masked registration reference, verified mobile suffix, name, and registration date within authorised scope.

### Documents
Citizen photograph, signature, and any identity support documents retained against the citizen profile.

### Reports
Citizen registration and OTP-verification exception register.

### Notifications
OTP and registration-completion acknowledgement through Module 12.

### Security
Public registration rate controls; masked sensitive identifiers; citizen record access only after authenticated login; all verification events audited.

### Integrations
OTP dispatch consumption through Module 12 (Easy).

### Dependencies
Module 01 citizen credential foundation; Module 12 notification service; configured identity/document rules in Module 02.

### Assumptions
BDA approves the final mandatory-field list and consent text; optional eKYC is excluded.

### Risks
SMS delivery delay or recycled mobile numbers can increase failed registrations.

### Non Functional Requirements
Mobile-responsive registration, clear retry messaging, protected personally identifiable information, and auditable OTP events.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Registration and verification journey | UI | Complex | 8 |
| Identity and OTP registration processing | API | Complex | 8 |
| Citizen registration persistence | Database | Medium | 4 |
| OTP notification handoff | Integration | Easy | 8 |
| Registration and OTP tests | Testing | Complex | 8 |
| Citizen registration guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
OTP delivery is consumed from Module 12; optional Aadhaar/eKYC connector work is not included.
