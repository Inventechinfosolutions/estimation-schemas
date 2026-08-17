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
1. Administrator (or staff member) enters official email and mobile on the activation path.
2. The system sends OTP to email and to mobile.
3. The user enters both OTPs on the OTP entry screens.
4. Only after both OTPs succeed can the account be marked Active.
5. If OTP is skipped, or attempted after a premature success message, login as Active is refused.

### Functional Capabilities
- Send OTP to official email and mobile.
- Capture and verify both OTPs before activation.
- Block Active status and staff login until both succeed.
- Record OTP success/failure for forensic audit (F01-010).

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
| Email and mobile OTP entry screens | UI | Medium | 6 |
| OTP send, verify and activation-gate operations | API | Complex | 8 |
| OTP attempt persistence | DB | Easy | 2 |
| SMS/email OTP delivery | Integration | Medium | 16 |
| OTP-before-activation tests | Testing | Complex | 8 |
| Activation OTP guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Login 2FA challenge is estimated in F01-006, not as this activation OTP.
- Integration Medium covers OTP gateway mapping and retry, not a payment gateway.
