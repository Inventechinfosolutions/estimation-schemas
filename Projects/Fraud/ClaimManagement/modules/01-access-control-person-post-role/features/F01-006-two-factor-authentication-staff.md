# F01-006 — Two-Factor Authentication (staff)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-006 |
| **Feature Name** | Two-Factor Authentication (staff) |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
A staff member enters user ID and password, then completes the second factor (for example OTP on the enrolled device/channel) before the session opens. Staff access without the second factor is refused. Claimants on the constrained OOK path are not given this staff 2FA enrolment. This 2FA is the programme staff control for Claim, Legal and Valuation.

### Business Objective
Require a second factor for every staff session so password-only staff access is impossible.

### Actors
Staff member; Administrator (enrolment support); auditor (2FA events).

### User Journey
1. Who creates: Staff member
2. How they create: Staff member opens staff login and enters user ID and password.
3. How they edit: If credentials are valid, the system presents the second-factor challenge for the enrolled device/channel.
4. How they send for approval: Staff member completes the second factor; only then does the staff session open. Password → 2FA challenge → session. Enrolment is a prerequisite administration step.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Staff member works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Staff member opens history on the record. If the second factor is skipped or fails, staff access is refused and the event is audited. OOK claimants never see this staff 2FA enrolment or challenge.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Staff 2FA enrolment against the Person’s official channel/device.
- Login challenge after password before session open.
- Refuse staff access without the second factor.
- Exclude OOK claimant accounts from staff 2FA.
- Audit 2FA success, failure and enrolment changes.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Staff login and 2FA challenge | Complex |
| Staff 2FA enrolment screen | Medium |
| Two-factor authentication history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| 2FA verify and session operations | Very High |
| Update two-factor authentication | Medium |
| Search two-factor authentication | Medium |
| Read two-factor authentication history | Easy |

### Inputs
User ID, password, second-factor response, enrolment channel.

### Outputs
Authenticated staff session; 2FA enrolment status; login/2FA audit events.

### Business Rules
- Two-factor authentication is required for all staff access.
- OOK constrained path is not staff 2FA.
- A Person without enrolment cannot open a staff session once 2FA is mandated.

### Validations
- Password-only success does not open the session.
- Second factor must match the enrolled channel for that Person.
- Lockout after repeated 2FA failures per policy.

### Calculations
Challenge expiry and lockout counters.

### Workflow
Password → 2FA challenge → session. Enrolment is a prerequisite administration step.

### Search Requirements
Person, 2FA enrolled/not enrolled, last 2FA event (administrator/auditor).

### Documents
None.

### Reports
2FA enrolment and failure extracts (full forensic view in F01-010).

### Notifications
Second-factor OTP/challenge to the enrolled channel.

### Security
Staff 2FA is mandatory. Enrolment changes are privileged and audited. OOK path cannot enrol in staff 2FA.

### Integrations
OTP / second-factor delivery channel for staff.

### Dependencies
F01-001, F01-004, F01-005 (account Active).

### Assumptions
- Second factor is OTP on an enrolled device/channel unless the Authority later specifies another factor.
- Legal and Valuation staff sessions reuse this 2FA rather than implementing another.

### Risks
- Bypassing 2FA for “break-glass” without audit would fail the website-review control.
- Enrolling OOK claimants in staff 2FA would mix channels.

### Non Functional Requirements
This is the programme-wide identity product consumed by Legal Management and GIS field valuation; staff screens must remain usable during claim windows; privileged actions are attributable to a named Person acting in a Post; primary official hosting identity is an approved government domain, not .org. 2FA challenge must complete within the login SLA agreed for official claim-window operations.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Staff login and 2FA challenge | UI | Complex | 12 |
| Staff 2FA enrolment screen | UI | Medium | 6 |
| Two-factor authentication history | UI | Medium | 6 |
| 2FA verify and session operations | API | Very High | 16 |
| Update two-factor authentication | API | Medium | 6 |
| Search two-factor authentication | API | Medium | 6 |
| Read two-factor authentication history | API | Easy | 4 |
| 2FA enrolment persistence | DB | Medium | 4 |
| OTP / 2FA channel delivery | Integration | Medium | 16 |
| Two-Factor Authentication (staff) feature tests | Testing | Very High | 12 |
| Two-Factor Authentication (staff) implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **92** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
