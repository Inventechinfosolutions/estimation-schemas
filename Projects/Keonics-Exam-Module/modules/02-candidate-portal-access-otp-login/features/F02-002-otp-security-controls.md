# F02-002 — OTP Security Controls

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | OTP Security Controls |
| **Module** | 02 — Candidate Portal Access (OTP Login) |

### Description
Configurable security controls govern candidate portal OTP login: OTP expiry, retry limits, resend control (cooldown and maximum resends), failed-attempt tracking and temporary lock, and portal session idle/absolute timeout. An Examination Administrator configures the OTP security policy. During candidate login (F02-001), the system applies these controls so that login succeeds only with a valid OTP within expiry and retry limits; excess failed attempts are blocked per policy; idle or expired sessions require a fresh OTP login. This feature also surfaces security event history for Administrators/auditors and candidate-facing messages for lock, expiry and resend-wait states. SMS delivery for controlled resends uses the SMS gateway.

### Business Objective
Prevent OTP abuse and session misuse on the candidate portal by enforcing Department-configured expiry, retry, resend, lockout and session-timeout rules consistently on every login attempt.

### Actors
Examination Administrator (configures policy; reviews security events); Candidate (experiences controls during login); Auditor (read-only security history).

### User Journey
1. Who creates: Examination Administrator creates or updates the OTP security policy configuration for the candidate portal.
2. How they create: Open OTP security policy screen → set expiry minutes, max verify attempts, resend cooldown, max resends per window, failed-attempt lock threshold and lock duration, idle and absolute session timeouts → save policy (effective for subsequent OTP challenges).
3. How they edit: Administrator revises policy values → save; optionally force expiry of outstanding challenges when tightening expiry (as configured).
4. How they send for approval: Submit/approval does not apply unless Department later mandates maker–checker for security policy; default is direct Administrator save with audit.
5. How the approver sees pending items: There is no approver inbox; locked mobiles and security events appear on the security event / lock status views for operations.
6. How the approver decides: There is no approval decision; Administrator may manually unlock a mobile if Department allows an unlock action with remarks (administrative control, not workflow approval of candidate login).
7. How the applicant / maker sees history: Candidate sees only real-time messages (OTP expired, attempts remaining, wait to resend, temporarily locked, session expired). Administrator who changed policy sees policy change history.
8. How the approver / auditor sees history: Auditor opens OTP security event history (sends, failures, locks, unlocks, session timeouts) filtered by mobile, date and event type.

### Functional Capabilities
- Configure OTP expiry duration for candidate portal challenges.
- Configure maximum OTP verification attempts per challenge or window.
- Configure resend cooldown and maximum resends per time window.
- Track failed verification attempts and apply temporary lock when threshold exceeded.
- Enforce portal session idle timeout and absolute session lifetime; require fresh OTP login after expiry.
- Apply all controls during F02-001 send, resend and verify paths.
- Allow Administrator manual unlock of a locked mobile with mandatory remarks where Department permits.
- Maintain security event history for sends, failures, locks, unlocks and session timeouts.
- Show candidate-safe messages for expired OTP, attempts exhausted, resend wait and locked state without leaking policy internals beyond necessary guidance.
- Invalidate outstanding OTP when expired or when max attempts reached.
- Support policy change history so auditors see who changed limits.
- Ensure locked mobiles cannot receive unlimited OTP spam beyond resend policy.
- Align SMS resend delivery with gateway integration under the same controls.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| OTP security policy configuration | Complex |
| Failed attempt and lock status view | Medium |
| Manual unlock with remarks | Easy |
| Candidate resend-wait and lock messages | Easy |
| Session timeout warning and re-login | Easy |
| OTP security event history | Medium |
| OTP policy change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save OTP security policy | Complex |
| Apply expiry and retry limits on verify | Complex |
| Track failed attempts and apply lock | Complex |
| Control resend eligibility and cooldown | Medium |
| Enforce portal session timeout | Medium |
| Manual unlock locked mobile | Medium |
| Search OTP security events | Medium |
| Read OTP policy change history | Easy |

### Inputs
Policy values (expiry, max attempts, resend cooldown, max resends, lock threshold, lock duration, idle timeout, absolute timeout); unlock remarks; mobile under lock; event search filters.

### Outputs
Active OTP security policy; enforced challenge and session behaviour on login; lock status; security event records; policy change history; candidate-facing control messages.

### Business Rules
- Login succeeds only after a valid OTP within expiry and retry limits.
- Excess failed attempts are blocked per configured policy (temporary lock).
- Idle / expired sessions require a fresh OTP login.
- Resend is allowed only after cooldown and within max resend count for the window.
- Expired OTP cannot be verified; candidate must request a new OTP subject to resend rules.
- Manual unlock (if enabled) is audited and does not reveal prior OTP values.
- Policy changes do not weaken audit of past events.

### Validations
- Policy numeric fields mandatory and within Department-approved ranges (e.g. expiry > 0, attempts ≥ 1).
- Lock duration required when lock threshold is enabled.
- Unlock requires remarks and user-admin / security privilege.
- Cannot verify OTP for a locked mobile until unlock or lock expiry.
- Resend rejected when cooldown active or max resends exceeded.

### Calculations
Remaining expiry seconds; remaining verify attempts; remaining cooldown seconds; lock remaining duration; session idle remaining time.

### Workflow
Administrator configures policy → candidates attempt login under F02-001 → controls applied on send/verify/session → lock when threshold hit → auto-unlock after duration or manual unlock → audit events recorded. No maker–checker for candidate login.

### Search Requirements
Security events by mobile (masked as required), event type (send, fail, lock, unlock, timeout), date range, lock status; policy change history by date and actor.

### Documents
None.

### Reports
Locked mobiles list and OTP failure summary for Administrator operations (exportable if Module 09 later generalises; minimal list view in this feature).

### Notifications
SMS on controlled OTP resend (via SMS gateway); optional Administrator alert on repeated lock storms if later configured in Module 09.

### Security
OTP secrets not recoverable; locks prevent online guessing; session timeout reduces abandoned-session risk; only privileged Administrators change policy or unlock; all policy and unlock actions audited.

### Integrations
SMS gateway for policy-controlled OTP resend delivery (Complex: auth, template mapping, retry, coordination with lock/resend rules and failure handling under abuse conditions).

### Dependencies
F02-001 Mobile OTP Login (applies controls on the login path). Related audit dashboards may consume events in Module 09.

### Assumptions
- SMS gateway is the same channel as F02-001; this feature’s Integration covers control-aware resend and failure handling under lock/abuse scenarios (Complex).
- Default policy values are agreed with the Department before go-live.
- Hours use Estimation Master; each named screen and logical API billed independently.

### Risks
- Overly aggressive lock thresholds could block legitimate candidates during registration peaks.
- Overly long OTP expiry weakens security; overly short expiry increases SMS cost and support load.
- Missing session timeout would leave unattended portal sessions usable on shared devices.

### Non Functional Requirements
Control checks must add negligible latency to verify; lock and event writes must be reliable under concurrent login bursts; policy reads should be cache-safe with clear invalidation on change; security event retention per Department audit policy.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| OTP security policy configuration | UI | Complex | 12 |
| Failed attempt and lock status view | UI | Medium | 6 |
| Manual unlock with remarks | UI | Easy | 4 |
| Candidate resend-wait and lock messages | UI | Easy | 4 |
| Session timeout warning and re-login | UI | Easy | 4 |
| OTP security event history | UI | Medium | 6 |
| OTP policy change history | UI | Medium | 6 |
| Save OTP security policy | API | Complex | 8 |
| Apply expiry and retry limits on verify | API | Complex | 8 |
| Track failed attempts and apply lock | API | Complex | 8 |
| Control resend eligibility and cooldown | API | Medium | 6 |
| Enforce portal session timeout | API | Medium | 6 |
| Manual unlock locked mobile | API | Medium | 6 |
| Search OTP security events | API | Medium | 6 |
| Read OTP policy change history | API | Easy | 4 |
| OTP policy, lock and event persistence | DB | Complex | 6 |
| SMS gateway control-aware OTP resend | Integration | Complex | 24 |
| OTP security controls feature tests | Testing | Very High | 12 |
| OTP security controls implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **140** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- SMS Integration is Complex because resend must coordinate with lock, cooldown, max-resend and gateway retry under abuse scenarios.
- F02-001 bills the baseline OTP send Integration at Medium; this feature bills control-aware resend Integration at Complex.
- Testing is Very High for lock, expiry, resend and session-timeout matrix.
