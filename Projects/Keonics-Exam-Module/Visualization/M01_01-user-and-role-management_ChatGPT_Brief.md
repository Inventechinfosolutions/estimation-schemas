# ChatGPT Visualization Brief — Module 01: User & Role Management

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 01 User & Role Management
**Features:** 12 (F01-007 … F01-020)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 01 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Role/permission matrix heatmap (Candidate / Admin / Invigilator / Public)
2. Staff login sequence + session policy state machine
3. Centre-scoped authorization decision tree for invigilator
4. Password policy + reset flow swimlane
5. IAM ERD and audit event flow
6. Downstream authorization hook integration map to modules 03–12
7. Feature relationship / dependency graph within this module and to other modules
8. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** User & Role Management
**Purpose:** Define platform roles (Candidate, Examination Administrator, Centre Invigilator, Verifier/Public), permission catalogues, staff accounts, password/session policy, audit, and authorization hooks used by all downstream modules.

**Actors (union across features):**
- Candidate
- Examination Administrator
- Examination Centre/Invigilator User
- System
- Verifier/Public User

**Feature list:**
- **F01-007** — Candidate Role and Portal Permission Catalogue
- **F01-008** — Examination Administrator Role and Organisation-Wide Permissions
- **F01-009** — Centre Invigilator Role and Centre-Scoped Access Model
- **F01-010** — Verifier Public Role and Anonymous Verification Access Policy
- **F01-011** — Staff Password Authentication and Login Session
- **F01-014** — Examination Administrator User Register and Account Lifecycle
- **F01-015** — Centre Invigilator User Register Centre Binding and Lifecycle
- **F01-016** — Role and Permission Matrix Administration
- **F01-017** — Session Timeout Idle Lock and Concurrent Session Controls
- **F01-018** — Password Credential Policy Configuration and Reset Flows
- **F01-019** — User Access Audit Register and Security Event Trace
- **F01-020** — Downstream Module Actor Authorization Integration Hooks

### DATA MODEL (from EXAM DB design v2.1)

- `platform_role`
- `permission`
- `role_permission`
- `permission_snapshot`
- `staff_user`
- `staff_user_role`
- `staff_user_centre`
- `staff_session`
- `session_policy`
- `credential_policy`
- `staff_password_history`
- `staff_password_reset`
- `iam_security_event`
- `authorization_hook_registration`
- `rate_limit_bucket`

### FEATURE CATALOGUE

#### F01-007 — Candidate Role and Portal Permission Catalogue

**One-liner / description:** Establishes the Candidate platform role aligned to SOW §3.1 and maps granular portal permissions for registration, document upload, centre preference, fee payment, hall ticket access, examination credential use,…

**Business objective:** Give downstream modules a single authoritative Candidate permission catalogue so portal capabilities are enforced consistently while keeping authentication mechanics in Candidate Registration.

**Actors:** Examination Administrator; System; Candidate

**User journey (9 steps):**
1. Administrator opens User and Role Management and selects the Candidate role.
2. Administrator views read-only role summary describing portal scope per SOW §3.1.
3. Administrator opens the portal permission catalogue grouped by journey stage: registration, scheduling artefacts, examination conduct, results, and certificate.
4. Administrator reviews each atomic permission (submit registration, upload documents, select centres, pay fees, download hall ticket, use exam credentials, view results, download certificate, share certificate via QR).
5. Administrator toggles optional permission grants where policy allows deviation from baseline.
6. System validates mandatory baseline permissions cannot be removed.
7. Administrator saves changes.
8. System publishes an effective-dated permission snapshot consumable by Modules 05, 06, 09, 10, and 11.
9. Downstream portal screens hide or disable actions when the Candidate role lacks the corresponding grant.

**Functional capabilities:**
- Maintain Candidate role metadata aligned to SOW §3.1 actor definition
- Catalogue portal permissions by registration, scheduling, conduct, results, and certificate stages
- Display permission descriptions tied to each candidate-facing capability named in the SOW
- Allow administrator adjustment of non-mandatory permission grants
- Block removal of baseline permissions required for statutory portal operation
- Publish effective-dated Candidate permission snapshot for downstream enforcement
- Expose read-only Candidate role summary for audit and onboarding

**Inputs:** Candidate role identifier; Permission grant toggles per portal capability; Effective date for permission change; Administrator user identity performing change

**Outputs:** Candidate role definition record; Grouped portal permission catalogue; Published permission snapshot version; Change confirmation with effective date

**Business rules:**
- Candidate role must exist as a platform role distinct from staff roles
- Baseline permissions covering registration submission, hall ticket download, examination credential use, result view, and certificate download cannot be fully revoked
- OTP-based login permission flag references Module 05 but is catalogued here for completeness
- Permission changes apply forward from effective date without retroactively altering completed transactions
- Only Examination Administrator role holders may modify Candidate permission grants

**Validations:**
- Permission code must exist in the master catalogue before grant change
- At least one registration-stage permission must remain granted
- At least one post-registration portal permission must remain granted when examination lifecycle is active
- Effective date cannot precede current published snapshot date
- Administrator performing change must hold role-management permission

**Workflow / states:** DRAFT_CATALOGUE → REVIEWED → PUBLISHED → SUPERSEDED when a newer snapshot is published

**Dependencies:**
- F05-001 OTP-Based Candidate Portal Login owns authentication execution
- F01-008 Role and Permission Matrix Administration provides shared matrix shell
- F01-012 Downstream Module Actor Authorization Integration Hooks propagates snapshots

**Risks:** Over-permissive grants could expose administrative actions on the candidate portal if downstream checks are skipped; Under-permissive grants could block legitimate post-registration self-service

**Notes:** Defines Candidate actor permissions for portal journeys; OTP login implementation remains in Module 05.

---

#### F01-008 — Examination Administrator Role and Organisation-Wide Permissions

**One-liner / description:** Defines the Examination Administrator platform role per SOW §3.2 with organisation-wide permission grants covering examinations, schedules, centres, registrations, question banks, exam parameters, paper versions,…

**Business objective:** Provide a single administrator role model with full-scope permissions so departmental staff can operate all back-office modules without centre scoping constraints.

**Actors:** Examination Administrator; System

**User journey (8 steps):**
1. Administrator opens role management and selects Examination Administrator role.
2. Administrator views organisation-wide scope indicator confirming non-centre-restricted access.
3. Administrator browses permission groups: examination configuration, centre management, registration oversight, question bank, scheduling, conduct monitoring, evaluation, certification, and reporting.
4. Administrator reviews each atomic permission mapped to SOW §3.2 responsibilities.
5. Administrator adjusts optional sub-permissions where departmental policy requires segregation of duties.
6. System prevents removal of core operational permissions needed for platform administration.
7. Administrator publishes updated administrator permission snapshot.
8. Staff users assigned this role receive updated claims on next session refresh.

**Functional capabilities:**
- Maintain Examination Administrator role with organisation-wide scope flag
- Catalogue permissions for examination master management
- Catalogue permissions for schedule and allocation administration
- Catalogue permissions for centre master and invigilator assignment oversight
- Catalogue permissions for registration review and document verification
- Catalogue permissions for question bank and examination configuration
- Catalogue permissions for session monitoring, results, certificates, and MIS reports
- Publish administrator permission snapshot without centre scoping attributes

**Inputs:** Examination Administrator role identifier; Permission grant selections per functional group; Segregation-of-duties override justification where required; Publishing administrator identity

**Outputs:** Organisation-wide administrator role definition; Grouped permission catalogue for administrator functions; Published administrator permission snapshot; Scope indicator showing non-centre-restricted access

**Business rules:**
- Examination Administrator role is organisation-wide and not centre-scoped
- Core permissions for examination lifecycle administration cannot all be revoked simultaneously
- Administrator users inherit this role through explicit assignment only
- Permission grants align to modules 03, 04, 05 oversight, 06, 08 monitoring, 10, 11, and 12 without re-implementing those workflows

**Validations:**
- At least one permission must remain in each mandatory functional group
- Organisation-wide scope flag cannot be disabled for this role
- Permission codes must map to registered downstream module operations
- Publisher must hold super-administrator or role-management permission

**Workflow / states:** CONFIGURED → VALIDATED → PUBLISHED → SUPERSEDED

**Dependencies:**
- F01-006 Examination Administrator User Register and Account Lifecycle for user assignment
- F01-008 Role and Permission Matrix Administration
- F01-012 Downstream Module Actor Authorization Integration Hooks

**Risks:** Broad organisation-wide grants increase impact of compromised administrator credentials

---

#### F01-009 — Centre Invigilator Role and Centre-Scoped Access Model

**One-liner / description:** Defines the Examination Centre/Invigilator User role per SOW §3.3 with centre-scoped permission enforcement so centre users access only examinations, candidates, and activities mapped to their assigned authorised centre.

**Business objective:** Prevent cross-centre data exposure while granting invigilator permissions for verification, session activation, attendance monitoring, and centre dashboard access described in Modules 08 and 09 handoffs.

**Actors:** Examination Administrator; Examination Centre/Invigilator User; System

**User journey (8 steps):**
1. Administrator selects Centre/Invigilator role definition.
2. Administrator views centre-scoped access model summary explaining data isolation rules.
3. Administrator configures permission grants for centre dashboard, candidate register, identity verification, session activation, live monitoring, and centre-level activities.
4. Administrator confirms each permission is tagged as centre-scoped requiring centre binding on user assignment.
5. Administrator publishes centre invigilator permission snapshot.
6. Invigilator user logs in and system resolves assigned centre identifiers into session claims.
7. Invigilator opens centre dashboard; system filters all data to assigned centre only.
8. Attempt to access another centre's examination session is denied with auditable rejection.

**Functional capabilities:**
- Maintain Centre/Invigilator role with mandatory centre-scope enforcement flag
- Catalogue permissions for centre examination day dashboard access
- Catalogue permissions for scheduled candidate register visibility
- Catalogue permissions for candidate identity verification and attendance marking
- Catalogue permissions for candidate examination session activation
- Catalogue permissions for live examination session monitoring
- Enforce centre identifier filter on all invigilator permission checks
- Deny cross-centre resource access with explicit audit reason

**Inputs:** Centre/Invigilator role identifier; Permission grant selections; Centre-scope enforcement policy flag; Assigned centre identifiers at user level

**Outputs:** Centre-scoped role definition; Invigilator permission catalogue; Centre-filtered authorization decision; Cross-centre access denial audit entry

**Business rules:**
- Every Centre/Invigilator permission evaluation must include assigned centre identifier
- Invigilator users without centre assignment cannot access operational centre screens
- Centre-scoped permissions align to Module 08 centre operations without re-implementing those screens
- Organisation-wide administrator permissions must not apply to invigilator role unless dual-assigned

**Validations:**
- Centre-scope flag cannot be disabled for this role
- Permission grant requires centre binding metadata on consuming operations
- Requested resource centre must match user assigned centre
- Inactive centre assignment blocks operational permissions

**Workflow / states:** ROLE_DEFINED → CENTRE_SCOPE_ENFORCED → USER_ASSIGNED → SESSION_SCOPED → ACCESS_GRANTED or ACCESS_DENIED

**Dependencies:**
- F03-003 Centre Invigilator User Assignment provides centre binding source
- F01-007 Centre Invigilator User Register Centre Binding and Lifecycle
- F01-012 Downstream Module Actor Authorization Integration Hooks

**Risks:** Missing centre filter in a downstream module could leak candidate data across centres

---

#### F01-010 — Verifier Public Role and Anonymous Verification Access Policy

**One-liner / description:** Defines the Verifier/Public User access model per SOW §3.4 and §36 enabling anonymous or lightly authenticated public users to scan certificate QR codes and verify departmental issuance without staff credentials.

**Business objective:** Separate public verification access from internal staff roles while controlling which certificate fields may be disclosed on the verification response.

**Actors:** Verifier/Public User; Examination Administrator; System

**User journey (8 steps):**
1. Administrator opens Verifier/Public role and access policy configuration.
2. Administrator reviews public verification scope: QR scan entry, certificate lookup, genuine/issued status display, cancelled/revoked status display.
3. Administrator configures publicly disclosable field set approved for verification page.
4. Administrator sets rate-limit and anonymous access policy flags.
5. Administrator publishes public verification access policy snapshot.
6. Public user scans certificate QR code on Module 11 verification portal.
7. System applies Verifier/Public policy to determine allowed response fields and denial messages.
8. Cancelled or revoked certificates return policy-defined status without staff login.

**Functional capabilities:**
- Maintain Verifier/Public role as non-staff anonymous access actor
- Define public verification permissions separate from candidate and administrator roles
- Configure publicly disclosable certificate verification fields
- Configure denied-access messaging for invalid or revoked certificates
- Apply rate-limit policy metadata for anonymous verification requests
- Publish public verification access policy for Module 11 consumption
- Support unauthenticated verification session without staff password login

**Inputs:** Public verification policy toggles; Disclosable field allow-list; Rate-limit thresholds; Revoked certificate response template

**Outputs:** Verifier/Public role definition; Public verification access policy snapshot; Field disclosure rules for verification responses; Anonymous access configuration metadata

**Business rules:**
- Public verification does not require staff user account provisioning
- Only approved certificate fields may appear on public verification responses
- Revoked or cancelled certificates must surface appropriate status per Module 11 rules
- Public role must not grant access to internal administrative functions

**Validations:**
- Disclosable field list must be non-empty
- Sensitive internal identifiers must be excluded from public allow-list
- Rate-limit values must be positive integers
- Policy publisher must hold administrator role-management permission

**Workflow / states:** POLICY_DRAFT → POLICY_PUBLISHED → APPLIED_ON_VERIFICATION_REQUEST → RESPONSE_ALLOWED or RESPONSE_DENIED

**Dependencies:**
- F11-004 Public Online Certificate Verification Portal implements verification UI
- F01-012 Downstream Module Actor Authorization Integration Hooks

**Risks:** Over-disclosure in public field allow-list could expose personal data; Insufficient rate limiting could enable bulk certificate probing

**Notes:** Public QR verification UI is implemented in Module 11; this feature owns access policy and role definition.

---

#### F01-011 — Staff Password Authentication and Login Session

**One-liner / description:** Provides password-based authentication and authenticated session establishment for Examination Administrator and Centre/Invigilator staff users including login, logout, failed attempt handling, and role claim issuance.

**Business objective:** Give non-candidate staff a secure entry point to administrative and centre interfaces distinct from candidate OTP authentication.

**Actors:** Examination Administrator; Examination Centre/Invigilator User; System

**User journey (9 steps):**
1. Staff user navigates to staff login page.
2. User enters username or official email and password.
3. System validates account exists, is active, and is not locked.
4. System validates password against stored credential.
5. On failure, system increments failed attempt counter and displays generic error.
6. On lockout threshold, system blocks further attempts until lockout window expires.
7. On success, system creates authenticated session with role and centre scope claims.
8. User lands on role-appropriate home dashboard.
9. User selects logout; system terminates session and clears client tokens.

**Functional capabilities:**
- Present staff login screen separate from candidate OTP portal entry
- Authenticate administrator users with password credentials
- Authenticate centre invigilator users with password credentials
- Issue session token containing role identifiers and centre scope where applicable
- Track failed login attempts per user account
- Apply account lockout after configured failed attempt threshold
- Terminate session on explicit logout
- Reject login for deactivated user accounts

**Inputs:** Username or email; Password; Client device metadata; Requested portal context admin versus centre

**Outputs:** Authenticated session token; Role and scope claims payload; Login failure response with lockout status; Logout confirmation

**Business rules:**
- Candidate OTP login path is not handled in this feature
- Only active staff accounts may authenticate
- Lockout policy values come from password policy configuration feature
- Centre invigilator sessions must include assigned centre claims at login
- Concurrent session rules enforced by session management feature

**Validations:**
- Username or email must match registered staff account format
- Password must not be empty
- Deactivated account login rejected regardless of password correctness
- Locked account login rejected with remaining lockout duration
- Invigilator account without centre assignment rejected at login

**Workflow / states:** UNAUTHENTICATED → CREDENTIALS_SUBMITTED → VALIDATED → SESSION_ACTIVE → LOGGED_OUT or SESSION_EXPIRED

**Dependencies:**
- F01-006 Examination Administrator User Register and Account Lifecycle
- F01-007 Centre Invigilator User Register Centre Binding and Lifecycle
- F01-009 Session Timeout Idle Lock and Concurrent Session Controls
- F01-010 Password Credential Policy Configuration and Reset Flows

**Risks:** Shared centre workstation sessions require strict timeout enforcement

**Notes:** Candidate OTP login is out of scope; covered by Module 05.

---

#### F01-014 — Examination Administrator User Register and Account Lifecycle

**One-liner / description:** Manages full account lifecycle for Examination Administrator staff users including register listing, create, edit, activate, deactivate, and role assignment without centre binding.

**Business objective:** Enable departmental IT administrators to provision and retire back-office administrator accounts tied to organisation-wide role permissions.

**Actors:** Examination Administrator; System

**User journey (10 steps):**
1. Super-administrator opens administrator user register.
2. Register displays search filters for name, email, mobile, and active status.
3. Administrator selects create user.
4. Administrator enters display name, official email, mobile, employee identifier, and initial role assignment.
5. System validates uniqueness and format rules.
6. System creates inactive-pending or active account per policy and triggers initial credential workflow.
7. Administrator opens existing user edit form to update contact details or role assignment.
8. Administrator deactivates user via confirmation dialog; user cannot login but history remains.
9. Administrator reactivates previously deactivated user when required.
10. Register reflects status chips and last login timestamp.

**Functional capabilities:**
- List and search administrator user accounts with filters
- Create administrator user with unique email and employee identifier
- Edit administrator user profile fields
- Assign or change Examination Administrator role on user account
- Activate newly provisioned administrator account
- Deactivate administrator account without deleting audit history
- Reactivate deactivated administrator account
- Display administrator user status and last login metadata

**Inputs:** Display name; Official email; Mobile number; Employee identifier; Role assignment selection; Active or inactive status

**Outputs:** Administrator user register rows; Created user account record; Updated profile record; Activation or deactivation confirmation; Initial credential dispatch trigger

**Business rules:**
- Administrator users are not centre-scoped
- Deactivation preserves historical audit attribution
- At least one active super-administrator must remain at all times
- Employee identifier unique among active administrator accounts

**Validations:**
- Email format validation and uniqueness among staff users
- Mobile number ten-digit format validation and uniqueness where required
- Employee identifier required and unique among active accounts
- Display name minimum length validation
- Cannot deactivate the last active super-administrator
- Cannot assign centre-scoped-only role without explicit dual-role policy

**Workflow / states:** DRAFT → ACTIVE → DEACTIVATED → REACTIVATED; ACTIVE → DEACTIVATED

**Dependencies:**
- F01-002 Examination Administrator Role and Organisation-Wide Permissions
- F01-005 Staff Password Authentication and Login Session
- F01-010 Password Credential Policy Configuration and Reset Flows

**Risks:** Orphaned active accounts after staff departure if deactivation process skipped

---

#### F01-015 — Centre Invigilator User Register Centre Binding and Lifecycle

**One-liner / description:** Manages Centre/Invigilator staff user accounts with mandatory authorised examination centre binding, covering register, create, edit, centre reassignment, activate, and deactivate lifecycle per SOW §3.3 and Module 03…

**Business objective:** Ensure every invigilator account is explicitly tied to an authorised centre before centre operational access is granted.

**Actors:** Examination Administrator; Examination Centre/Invigilator User; System

**User journey (10 steps):**
1. Administrator opens centre invigilator user register.
2. Register supports filters by centre name, user name, email, and status.
3. Administrator selects create invigilator user.
4. Administrator enters profile fields and selects exactly one authorised centre from active centre master.
5. System validates centre is active and user identifiers are unique.
6. System creates invigilator account with centre binding and pending or active status.
7. Administrator edits user to change mobile or reassign centre when invigilator transfers.
8. Centre reassignment requires confirmation showing previous and new centre.
9. Administrator deactivates invigilator no longer associated with centre operations.
10. Invigilator login resolves only the currently assigned active centre.

**Functional capabilities:**
- List and search invigilator users with centre filter
- Create invigilator user with mandatory centre selection
- Edit invigilator profile fields
- Reassign invigilator to different authorised centre
- Activate invigilator account after centre binding confirmed
- Deactivate invigilator account preserving audit history
- Validate centre is active before binding
- Display centre name and centre ID on register rows

**Inputs:** Display name; Email; Mobile number; Employee or staff identifier; Authorised centre selection; Account status

**Outputs:** Invigilator register listing with centre column; Created invigilator account with centre binding; Centre reassignment audit record; Activation or deactivation confirmation

**Business rules:**
- Invigilator account cannot be activated without centre assignment
- Only active authorised centres appear in centre selector
- Centre reassignment takes effect on next login session
- Deactivated invigilator immediately loses centre operational access

**Validations:**
- Centre selection required on create
- Selected centre must be active in centre master
- Email uniqueness among staff users
- Mobile format validation
- Cannot reassign to inactive centre
- Cannot deactivate invigilator mid-session without session termination handled by session feature

**Workflow / states:** PENDING_CENTRE_BINDING → ACTIVE → CENTRE_REASSIGNED → ACTIVE; ACTIVE → DEACTIVATED

**Dependencies:**
- F03-001 Authorised Examination Centre Master Lifecycle for centre selector source
- F03-003 Centre Invigilator User Assignment aligns operational assignment rules
- F01-003 Centre Invigilator Role and Centre-Scoped Access Model
- F01-005 Staff Password Authentication and Login Session

**Risks:** Stale centre binding if centre deactivated without invigilator reassignment

---

#### F01-016 — Role and Permission Matrix Administration

**One-liner / description:** Provides consolidated administration screens to view and maintain role-to-permission mappings across Candidate, Examination Administrator, Centre/Invigilator, and Verifier/Public roles with compare and publish controls.

**Business objective:** Give security administrators a single matrix workspace to govern platform access consistently across all actor types.

**Actors:** Examination Administrator; System

**User journey (10 steps):**
1. Administrator opens role and permission matrix home.
2. Matrix displays roles as columns and permission groups as rows.
3. Administrator selects role column to highlight effective grants.
4. Administrator toggles permission intersection cells where editable.
5. System marks read-only cells for mandatory or externally owned permissions.
6. Administrator opens compare view between current published and draft matrix.
7. Administrator reviews diff summary listing added and removed grants.
8. Administrator publishes draft matrix with effective timestamp.
9. System invalidates downstream permission caches.
10. Administrator exports matrix snapshot for security audit file.

**Functional capabilities:**
- Display cross-role permission matrix grid
- Filter matrix by module permission group
- Toggle editable permission grants per role intersection
- Show mandatory and read-only permission indicators
- Compare draft matrix against published snapshot
- Publish consolidated permission matrix snapshot
- Export matrix to file for audit
- Invalidate downstream authorization caches on publish

**Inputs:** Role selection; Permission group filter; Cell grant toggle changes; Publish effective timestamp

**Outputs:** Matrix grid view; Draft versus published diff summary; Published matrix snapshot; Exported audit file

**Business rules:**
- Candidate OTP execution permissions remain read-only references to Module 05
- Mandatory permissions cannot be toggled off via matrix without override workflow
- Matrix publish supersedes individual role draft states atomically
- Verifier/Public row set limited to public verification permissions

**Validations:**
- Draft matrix must pass mandatory permission guard before publish
- Effective timestamp cannot precede latest published matrix
- Publisher must hold role-management permission
- Cannot publish empty matrix

**Workflow / states:** MATRIX_VIEW → DRAFT_EDITED → DIFF_REVIEWED → PUBLISHED → CACHE_INVALIDATED

**Dependencies:**
- F01-001 Candidate Role and Portal Permission Catalogue
- F01-002 Examination Administrator Role and Organisation-Wide Permissions
- F01-003 Centre Invigilator Role and Centre-Scoped Access Model
- F01-004 Verifier Public Role and Anonymous Verification Access Policy

**Risks:** Large matrix UI performance with hundreds of permissions

---

#### F01-017 — Session Timeout Idle Lock and Concurrent Session Controls

**One-liner / description:** Configures and enforces session timeout, idle lock, absolute session lifetime, and concurrent session limits for Examination Administrator and Centre/Invigilator authenticated sessions per SOW session control…

**Business objective:** Reduce credential misuse risk on shared centre workstations and unattended administrator terminals.

**Actors:** Examination Administrator; Examination Centre/Invigilator User; System

**User journey (8 steps):**
1. Administrator opens session policy configuration for staff portals.
2. Administrator sets idle timeout duration, absolute session lifetime, and concurrent session limit per role type.
3. Administrator saves policy and publishes to active sessions on next request.
4. Staff user works in authenticated session; activity heartbeat refreshes idle timer.
5. On idle threshold breach, system displays session lock overlay requiring re-authentication.
6. On absolute lifetime expiry, system redirects to login with session expired message.
7. When concurrent session limit exceeded at login, system terminates oldest session or blocks new login per policy.
8. Administrator views active staff session register for forced logout if needed.

**Functional capabilities:**
- Configure idle timeout duration for administrator sessions
- Configure idle timeout duration for invigilator sessions
- Configure absolute maximum session lifetime
- Configure concurrent session limit per user account
- Track session last activity timestamp
- Lock session on idle timeout pending re-authentication
- Expire session on absolute lifetime breach
- Enforce concurrent session policy at login
- List active staff sessions with forced logout action

**Inputs:** Idle timeout minutes; Absolute session lifetime minutes; Concurrent session limit integer; Role type specific overrides; Session activity heartbeat events

**Outputs:** Published session policy configuration; Idle lock overlay trigger; Session expired redirect; Concurrent session termination or block decision; Active session register listing

**Business rules:**
- Session policies apply to staff users only; candidate OTP session rules remain in Module 05
- Invigilator idle timeout may be shorter than administrator default for shared devices
- Forced logout immediately invalidates session token
- Session expiry events are audit logged

**Validations:**
- Idle timeout must be less than absolute session lifetime
- Timeout values must be positive integers within configured max bounds
- Concurrent session limit minimum of one
- Forced logout requires administrator privilege

**Workflow / states:** SESSION_ACTIVE → IDLE_WARNING → IDLE_LOCKED → REAUTHENTICATED or SESSION_TERMINATED; SESSION_ACTIVE → ABSOLUTE_EXPIRED → TERMINATED

**Dependencies:**
- F01-005 Staff Password Authentication and Login Session
- F01-010 Password Credential Policy Configuration and Reset Flows for re-auth

**Risks:** Overly aggressive idle lock disrupts invigilator operations during live examinations

**Notes:** Applies to non-candidate staff sessions only.

---

#### F01-018 — Password Credential Policy Configuration and Reset Flows

**One-liner / description:** Defines configurable password and credential policies for staff users and implements self-service and administrator-assisted password reset flows including initial credential setup.

**Business objective:** Enforce departmental password standards and recover staff access without compromising candidate OTP authentication handled elsewhere.

**Actors:** Examination Administrator; Examination Centre/Invigilator User; System

**User journey (11 steps):**
1. Administrator opens password policy configuration screen.
2. Administrator sets minimum length, complexity rules, password history depth, expiry days, and lockout thresholds linked to login feature.
3. Administrator publishes password policy.
4. New staff user receives initial setup link or temporary password requiring change on first login.
5. User opens first-login forced password change screen.
6. User enters new password satisfying live policy rules with inline validation hints.
7. Forgot-password user requests reset via registered email.
8. System sends time-limited reset token.
9. User opens reset link, enters token and new password.
10. System invalidates reset token and updates credential hash.
11. Administrator may trigger forced password reset for compromised account.

**Functional capabilities:**
- Configure minimum password length rule
- Configure complexity requirements for uppercase lowercase digit special
- Configure password history depth preventing reuse
- Configure password expiry interval for staff accounts
- Configure lockout threshold linkage metadata
- Enforce policy on password set and change operations
- First-login forced password change workflow
- Self-service forgot password request and token validation
- Administrator-initiated forced password reset

**Inputs:** Policy numeric thresholds; Complexity rule toggles; New password and confirmation; Reset token; Administrator force reset target user

**Outputs:** Published password policy record; Password validation result with field errors; Reset token email dispatch; Updated credential hash; Force reset confirmation

**Business rules:**
- Password policies apply to staff users only
- Expired password blocks login until changed via approved flow
- Reset tokens single-use and time-limited
- Password history prevents reuse of last N passwords

**Validations:**
- Minimum length at least policy configured minimum
- Complexity rules each satisfied when enabled
- New password must differ from current password
- New password must not match entries in password history
- Reset token expiry validation
- Password confirmation must match new password

**Workflow / states:** POLICY_CONFIGURED → CREDENTIAL_SET → ACTIVE → EXPIRED → MUST_CHANGE → ACTIVE; RESET_REQUESTED → TOKEN_ISSUED → TOKEN_VALIDATED → CREDENTIAL_UPDATED

**Dependencies:**
- F01-005 Staff Password Authentication and Login Session
- F07-004 Multi-Channel Notification Dispatch Engine for reset emails

**Risks:** Weak policy defaults could fail departmental security audit

---

#### F01-019 — User Access Audit Register and Security Event Trace

**One-liner / description:** Captures and presents auditable records of user lifecycle changes, role assignment changes, login logout events, permission publishes, and authorization denials for staff and role administration aligned to SOW §41…

**Business objective:** Provide examination administrators forensic visibility into identity and access control changes supporting compliance and incident investigation.

**Actors:** Examination Administrator; System

**User journey (7 steps):**
1. Administrator opens user access audit register.
2. Register defaults to recent identity events with timestamp descending sort.
3. Administrator applies filters for event type, actor, target user, date range, and centre where applicable.
4. Administrator opens event detail drawer showing before and after values for change events.
5. Administrator exports filtered audit slice for compliance submission.
6. Security reviewer searches failed login and cross-centre denial events.
7. System automatically records events from user lifecycle, login, permission publish, and authorization hook denials without manual entry.

**Functional capabilities:**
- Record user account create update activate deactivate events
- Record role assignment and centre binding change events
- Record staff login logout success and failure events
- Record permission matrix publish events
- Record authorization denial events from integration hooks
- List audit events with multi-field filters
- Display event detail with before and after payload
- Export filtered audit register slice

**Inputs:** Event type filter selections; Date range; Actor user identifier; Target user identifier; Centre filter; Automatic event payloads from platform actions

**Outputs:** Audit register paginated listing; Event detail view; Exported audit file; Security event counts by type

**Business rules:**
- Audit records are append-only and cannot be edited or deleted via UI
- Candidate OTP events captured in Module 05 may be cross-referenced but not duplicated here except role changes affecting candidate permissions
- Authorization denial events include resource type and denial reason code
- Retention period configurable by administrator policy

**Validations:**
- Date range end must be after start
- Export row limit enforced to prevent unbounded extracts
- Audit viewer must hold audit-read permission

**Workflow / states:** EVENT_OCCURRED → RECORD_APPENDED → REGISTER_VIEWED → DETAIL_INSPECTED → EXPORTED

**Dependencies:**
- F01-005 Staff Password Authentication and Login Session
- F01-006 Examination Administrator User Register and Account Lifecycle
- F01-007 Centre Invigilator User Register Centre Binding and Lifecycle
- F01-008 Role and Permission Matrix Administration
- F01-012 Downstream Module Actor Authorization Integration Hooks

**Risks:** High event volume during examination days requires performant indexing

---

#### F01-020 — Downstream Module Actor Authorization Integration Hooks

**One-liner / description:** Delivers reusable authorization integration hooks enabling downstream business modules to enforce actor-based access checks using resolved role, permission, and centre scope claims without re-implementing identity logic.

**Business objective:** Centralise authorization decisions so Modules 03 through 12 consistently honour platform roles and centre scoping rules.

**Actors:** System; Examination Administrator; Examination Centre/Invigilator User

**User journey (10 steps):**
1. Downstream module invokes authorization hook before serving protected operation.
2. Hook extracts authenticated actor identity and session claims from staff or candidate session context.
3. Hook loads effective permission snapshot version applicable to actor role.
4. Hook evaluates requested permission code against grants.
5. For invigilator actors hook additionally validates resource centre against assigned centre scope.
6. Hook returns allow decision with resolved claims payload or deny decision with reason code.
7. Downstream module proceeds or returns forbidden response.
8. Deny decisions optionally emit audit event to F01-011 register.
9. Platform administrator invalidates permission cache after matrix publish from F01-008.
10. Downstream modules receive updated snapshot on subsequent hook calls.

**Functional capabilities:**
- Resolve authenticated actor identity from session context
- Load effective permission snapshot by role and version
- Evaluate single permission grant check for requested operation
- Evaluate centre scope check for invigilator resource access
- Return structured allow or deny authorization decision with reason code
- Emit authorization denial audit event when configured
- Expose permission snapshot cache with invalidation on publish
- Provide batch permission check for menu rendering use cases
- Document hook contract for downstream module integrators

**Inputs:** Session token or actor context; Requested permission code; Resource centre identifier for scoped checks; Optional batch permission code list

**Outputs:** Authorization allow decision with claims; Authorization deny decision with reason code; Cached permission snapshot reference; Denial audit event when enabled

**Business rules:**
- All downstream modules must use hooks for staff and candidate permission enforcement
- Centre scope check mandatory when actor holds invigilator role
- Public verification endpoints use Verifier/Public policy not staff session hooks
- Snapshot version mismatch triggers cache refresh not silent allow

**Validations:**
- Requested permission code must exist in master catalogue
- Missing session context returns unauthenticated denial
- Missing centre identifier on scoped operation returns scope denial
- Deactivated user always denied regardless of stale token

**Workflow / states:** HOOK_INVOKED → CLAIMS_RESOLVED → PERMISSION_EVALUATED → SCOPE_EVALUATED → ALLOWED or DENIED → AUDIT_OPTIONAL

**Dependencies:**
- F01-001 through F01-004 role permission catalogues
- F01-008 Role and Permission Matrix Administration for snapshot publish
- F01-011 User Access Audit Register for denial event ingestion

**Risks:** Inconsistent hook adoption in a module creates authorization bypass gaps

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 01 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 01 User & Role Management** (12 features).
> Features: F01-007 Candidate Role and Portal Permission Catalogue; F01-008 Examination Administrator Role and Organisation-Wide Permissions; F01-009 Centre Invigilator Role and Centre-Scoped Access Model; F01-010 Verifier Public Role and Anonymous Verification Access Policy; F01-011 Staff Password Authentication and Login Session; F01-014 Examination Administrator User Register and Account Lifecycle; F01-015 Centre Invigilator User Register Centre Binding and Lifecycle; F01-016 Role and Permission Matrix Administration; F01-017 Session Timeout Idle Lock and Concurrent Session Controls; F01-018 Password Credential Policy Configuration and Reset Flows; F01-019 User Access Audit Register and Security Event Trace; F01-020 Downstream Module Actor Authorization Integration Hooks.
> Purpose: Define platform roles (Candidate, Examination Administrator, Centre Invigilator, Verifier/Public), permission catalogues, staff accounts, password/session policy, audit, and authorization hooks used by all downstream modules.
> Draw: Role/permission matrix heatmap (Candidate / Admin / Invigilator / Public); Staff login sequence + session policy state machine; Centre-scoped authorization decision tree for invigilator; Password policy + reset flow swimlane; ERD for `platform_role`, `permission`, `role_permission`, `permission_snapshot`, `staff_user`, `staff_user_role`.
