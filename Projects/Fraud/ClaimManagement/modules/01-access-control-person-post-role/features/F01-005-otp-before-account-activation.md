# F01-005 — OTP before account activation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-005 |
| **Feature Name** | OTP before account activation |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
The staff member (or Administrator triggering provisioning) enters official email and mobile. The system sends OTP to both. The user enters the OTPs. Only after both succeed does the Administrator (or the system) mark the account Active. The user cannot log in as Active if OTP is skipped or done after a “registration successful” message.

### Business Objective
Make email and mobile OTP complete before activation so staff accounts cannot go live on an unverified contact.

### Actors
Administrator; staff member being activated.

### User Journey
1. Who creates: Administrator
2. How they create: Administrator (or staff member) enters official email and mobile on the activation path.
3. How they edit: The system sends OTP to email and to mobile.
4. How they send for approval: The user enters both OTPs on the OTP entry screens. Provisioning → OTP send → dual verify → Active. No staff module access before Active.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record. Only after both OTPs succeed can the account be marked Active. If OTP is skipped, or attempted after a premature success message, login as Active is refused.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Send OTP to official email and mobile.
- Capture and verify both OTPs before activation.
- Block Active status and staff login until both succeed.
- Record OTP success/failure for forensic audit (F01-010).

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My otp before account activation list / queue | Medium |
| Email and mobile OTP entry screens | Medium |
| Otp before account activation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| OTP send, verify and activation-gate operations | Complex |
| Update otp before account activation | Medium |
| Search otp before account activation | Medium |
| Read otp before account activation history | Easy |

### Inputs
Official email, mobile, OTP values, resend requests.

### Outputs
Verified contacts; account Active only after both OTPs; OTP attempt history.

### Business Rules
- OTP after an already-successful registration message is not acceptable.
- Both email and mobile OTP are required before Active.
- OOK claimant OTP, if any, is not this staff activation path.

### Validations
- Email and mobile must be present and match the Person’s official identity (F01-004).
- OTP expiry and attempt limits apply.
- Mismatched OTP does not activate the account.

### Calculations
OTP expiry window and remaining attempts.

### Workflow
Provisioning → OTP send → dual verify → Active. No staff module access before Active.

### Search Requirements
Person, official email/mobile, OTP/activation status.

### Documents
None.

### Reports
Activation pending / failed OTP list for Administrator.

### Notifications
OTP messages to official email and mobile.

### Security
OTP values are not stored in recoverable form. Attempt and lock events are audited. Only the Person’s official contacts receive OTP.

### Integrations
SMS and email OTP delivery channels.

### Dependencies
F01-001, F01-004.

### Assumptions
- Authority-approved SMS and email gateways are available.
- 2FA at login is a separate control (F01-006).

### Risks
- Activating before OTP would recreate the website-review gap.
- OTP delivery failure could stall joiner provisioning.

### Non Functional Requirements
This is the programme-wide identity product consumed by Legal Management and GIS field valuation; staff screens must remain usable during claim windows; privileged actions are attributable to a named Person acting in a Post; primary official hosting identity is an approved government domain, not .org. OTP delivery and verification must complete within an agreed operational window for joiners.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My otp before account activation list / queue | UI | Medium | 6 |
| Email and mobile OTP entry screens | UI | Medium | 6 |
| Otp before account activation history | UI | Medium | 6 |
| OTP send, verify and activation-gate operations | API | Complex | 8 |
| Update otp before account activation | API | Medium | 6 |
| Search otp before account activation | API | Medium | 6 |
| Read otp before account activation history | API | Easy | 4 |
| OTP attempt persistence | DB | Easy | 2 |
| SMS/email OTP delivery | Integration | Medium | 16 |
| OTP before account activation feature tests | Testing | Complex | 8 |
| OTP before account activation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
