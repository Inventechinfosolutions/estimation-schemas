# F06-002 — Citizen Profile, Login & Password

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Citizen Profile, Login & Password |
| **Module** | 06 — Citizen Registration Portal |

### Description
Provide authenticated citizens with profile maintenance, secure login entry, password-change support, and a clear view of profile completeness for downstream applications.

### Business Objective
Keep citizen contact and profile information usable while respecting credential controls owned by the identity foundation.

### Actors
Citizen; Citizen Support Officer; Auditor.

### User Journey
A registered citizen signs in, reviews profile completeness, updates allowed contact/address details and image/signature where required, confirms the changes, or changes the password after credential verification.

### Functional Capabilities
- Citizen profile view/edit, completion indicator, and restricted-field guidance.
- Login landing, password-change form, and success/failure messages.
- Profile-change history and support-assisted correction pathway.

### Inputs
Authenticated citizen context, editable profile values, current password, new password, and supporting documents where configured.

### Outputs
Updated citizen profile, password-change confirmation, and profile-change audit trail.

### Business Rules
Only the account owner may change profile details; verified mobile is not replaced without the approved re-verification process; password policy and session controls remain governed by Module 01.

### Validations
Required profile fields, email/mobile formats, password policy, current-password confirmation, image/signature file controls.

### Calculations
Profile-completeness indicator based on BDA-required application fields.

### Workflow
Login → profile review → update submitted → profile updated; password change → policy validation → confirmation.

### Search Requirements
Citizen can view own profile-change history; authorised support can locate requests by citizen reference and change date.

### Documents
Replacement profile photograph, signature, and supporting change evidence where BDA requires it.

### Reports
Profile-completeness and profile-change audit register.

### Notifications
Profile update and password-change alert through Module 12.

### Security
Ownership isolation, session timeout, password-policy enforcement, sensitive-field masking, and immutable login/change audit.

### Integrations
Identity-service consumption from Module 01 (Simple) and event notification handoff to Module 12 (Easy).

### Dependencies
Module 01 user and credential management; F06-001; Module 12.

### Assumptions
Sensitive identity corrections follow BDA support policy rather than unrestricted self-edit.

### Risks
Overly broad editable fields can weaken identity assurance.

### Non Functional Requirements
Responsive self-service pages, secure session handling, and timely rendering of profile data.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Profile and password self-service screens | UI | Complex | 8 |
| Profile update and credential-request processing | API | Complex | 8 |
| Profile change history persistence | Database | Medium | 4 |
| Identity and notification handoffs | Integration | Easy | 8 |
| Profile and password tests | Testing | Complex | 8 |
| Citizen account guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
Credential store and authentication foundation are estimated in Module 01; this feature estimates citizen-facing consumption only.
