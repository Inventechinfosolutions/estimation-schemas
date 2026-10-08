# Feature specification — Exam

**Prepared for:** Exam  
**Prepared by:** App Admin's workspace  
**Date:** 9 Sept 2026  
**Basis:** Current estimate  
**Version:** EST-2026-09-09

> Context pack for implementation. Hours come from the standard area and complexity table. Empty spec fields are omitted. Do not invent tasks or hours.

## Snapshot

- Modules: **12**
- Features: **87**
- Tasks: **1812**
- All-in: **10,164.6 hours**

Full captured specification for each feature, then the implementation tasks. Use this pack with developers and AI coding agents.

## 01 User & Role Management

1,291.45 hours · 237 tasks · Foundation

Platform identity, authentication framework, and role-based access for candidates, administrators, centre invigilators, and public verifiers.

### F01-007 Candidate Role and Portal Permission Catalogue

79.35 hours · Go-live · 18 tasks

##### Description

Establishes the Candidate platform role aligned to SOW §3.1 and maps granular portal permissions for registration, document upload, centre preference, fee payment, hall ticket access, examination credential use, results, certificate download, and certificate QR sharing without implementing OTP login or registration workflows.

##### Business objective

Give downstream modules a single authoritative Candidate permission catalogue so portal capabilities are enforced consistently while keeping authentication mechanics in Candidate Registration.

##### Actors

- Examination Administrator
- System
- Candidate

##### User journey

1. Administrator opens User and Role Management and selects the Candidate role.
2. Administrator views read-only role summary describing portal scope per SOW §3.1.
3. Administrator opens the portal permission catalogue grouped by journey stage: registration, scheduling artefacts, examination conduct, results, and certificate.
4. Administrator reviews each atomic permission (submit registration, upload documents, select centres, pay fees, download hall ticket, use exam credentials, view results, download certificate, share certificate via QR).
5. Administrator toggles optional permission grants where policy allows deviation from baseline.
6. System validates mandatory baseline permissions cannot be removed.
7. Administrator saves changes.
8. System publishes an effective-dated permission snapshot consumable by Modules 05, 06, 09, 10, and 11.
9. Downstream portal screens hide or disable actions when the Candidate role lacks the corresponding grant.

##### Functional capabilities

- Maintain Candidate role metadata aligned to SOW §3.1 actor definition
- Catalogue portal permissions by registration, scheduling, conduct, results, and certificate stages
- Display permission descriptions tied to each candidate-facing capability named in the SOW
- Allow administrator adjustment of non-mandatory permission grants
- Block removal of baseline permissions required for statutory portal operation
- Publish effective-dated Candidate permission snapshot for downstream enforcement
- Expose read-only Candidate role summary for audit and onboarding

##### Inputs

- Candidate role identifier
- Permission grant toggles per portal capability
- Effective date for permission change
- Administrator user identity performing change

##### Outputs

- Candidate role definition record
- Grouped portal permission catalogue
- Published permission snapshot version
- Change confirmation with effective date

##### Business rules

- Candidate role must exist as a platform role distinct from staff roles
- Baseline permissions covering registration submission, hall ticket download, examination credential use, result view, and certificate download cannot be fully revoked
- OTP-based login permission flag references Module 05 but is catalogued here for completeness
- Permission changes apply forward from effective date without retroactively altering completed transactions
- Only Examination Administrator role holders may modify Candidate permission grants

##### Validations

- Permission code must exist in the master catalogue before grant change
- At least one registration-stage permission must remain granted
- At least one post-registration portal permission must remain granted when examination lifecycle is active
- Effective date cannot precede current published snapshot date
- Administrator performing change must hold role-management permission

##### Calculations

- None; permission catalogue is declarative

##### Workflow

DRAFT_CATALOGUE → REVIEWED → PUBLISHED → SUPERSEDED when a newer snapshot is published

##### Search requirements

- Filter permission catalogue by journey stage
- Search permission by keyword within Candidate role context

##### Documents

- Permission catalogue export for requirements walkthrough

##### Reports

- Candidate role permission listing for compliance review

##### Notifications

- Optional in-app alert to administrators when Candidate permission snapshot is republished

##### Security

- Only authorised administrators may view or edit Candidate permission grants
- All permission changes are attributable to administrator identity
- Published snapshots are immutable; changes create new versions

##### Integrations

- Permission snapshot consumption by Module 05 Candidate Registration portal
- Permission snapshot consumption by Module 06 hall ticket access
- Permission snapshot consumption by Modules 09, 10, and 11 for conduct, results, and certificate actions

##### Dependencies

- F05-001 OTP-Based Candidate Portal Login owns authentication execution
- F01-008 Role and Permission Matrix Administration provides shared matrix shell
- F01-012 Downstream Module Actor Authorization Integration Hooks propagates snapshots

##### Assumptions

- Candidate accounts are provisioned through registration flows in Module 05
- Portal menu visibility is driven by permission grants rather than hard-coded module logic

##### Risks

- Over-permissive grants could expose administrative actions on the candidate portal if downstream checks are skipped
- Under-permissive grants could block legitimate post-registration self-service

##### Non-functional requirements

- Permission snapshot retrieval must be cacheable for portal page loads
- Catalogue changes must be auditable for government compliance

##### Notes

Defines Candidate actor permissions for portal journeys; OTP login implementation remains in Module 05.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate role read-only summary panel with SOW capability list | Simple | 5 |
| UI | Candidate portal permission catalogue list grouped by journey stage | Medium | 16 |
| UI | Permission grant toggle row with mandatory baseline indicator | Easy | 14 |
| UI | Permission catalogue empty state when no grants configured | Simple | 5 |
| UI | Publish permission snapshot confirmation dialog | Simple | 5 |
| API | Retrieve Candidate role definition with metadata | Easy | 4 |
| API | List Candidate portal permissions grouped by stage | Medium | 6 |
| API | Update individual Candidate permission grant | Medium | 6 |
| API | Validate mandatory baseline permissions before publish | Complex | 8 |
| API | Publish effective-dated Candidate permission snapshot | Complex | 8 |
| Database | Candidate role core record | Simple | 0.1 |
| Database | Portal permission catalogue entries | Medium | 0.3 |
| Database | Role-permission mapping with effective dating | Medium | 0.3 |
| Testing | Happy path load and publish Candidate permission snapshot | Medium | 0.3 |
| Testing | Mandatory baseline permission removal rejection cases | Medium | 0.3 |
| Testing | Effective-date supersede edge cases for concurrent publishes | Complex | 0.5 |
| Documentation | Administrator runbook for Candidate permission tuning | Medium | 0.3 |
| Documentation | Technical notes for downstream permission consumption | Easy | 0.25 |

### F01-008 Examination Administrator Role and Organisation-Wide Permissions

103.4 hours · Go-live · 18 tasks

##### Description

Defines the Examination Administrator platform role per SOW §3.2 with organisation-wide permission grants covering examinations, schedules, centres, registrations, question banks, exam parameters, paper versions, session monitoring, results, certificates, and reports.

##### Business objective

Provide a single administrator role model with full-scope permissions so departmental staff can operate all back-office modules without centre scoping constraints.

##### Actors

- Examination Administrator
- System

##### User journey

1. Administrator opens role management and selects Examination Administrator role.
2. Administrator views organisation-wide scope indicator confirming non-centre-restricted access.
3. Administrator browses permission groups: examination configuration, centre management, registration oversight, question bank, scheduling, conduct monitoring, evaluation, certification, and reporting.
4. Administrator reviews each atomic permission mapped to SOW §3.2 responsibilities.
5. Administrator adjusts optional sub-permissions where departmental policy requires segregation of duties.
6. System prevents removal of core operational permissions needed for platform administration.
7. Administrator publishes updated administrator permission snapshot.
8. Staff users assigned this role receive updated claims on next session refresh.

##### Functional capabilities

- Maintain Examination Administrator role with organisation-wide scope flag
- Catalogue permissions for examination master management
- Catalogue permissions for schedule and allocation administration
- Catalogue permissions for centre master and invigilator assignment oversight
- Catalogue permissions for registration review and document verification
- Catalogue permissions for question bank and examination configuration
- Catalogue permissions for session monitoring, results, certificates, and MIS reports
- Publish administrator permission snapshot without centre scoping attributes

##### Inputs

- Examination Administrator role identifier
- Permission grant selections per functional group
- Segregation-of-duties override justification where required
- Publishing administrator identity

##### Outputs

- Organisation-wide administrator role definition
- Grouped permission catalogue for administrator functions
- Published administrator permission snapshot
- Scope indicator showing non-centre-restricted access

##### Business rules

- Examination Administrator role is organisation-wide and not centre-scoped
- Core permissions for examination lifecycle administration cannot all be revoked simultaneously
- Administrator users inherit this role through explicit assignment only
- Permission grants align to modules 03, 04, 05 oversight, 06, 08 monitoring, 10, 11, and 12 without re-implementing those workflows

##### Validations

- At least one permission must remain in each mandatory functional group
- Organisation-wide scope flag cannot be disabled for this role
- Permission codes must map to registered downstream module operations
- Publisher must hold super-administrator or role-management permission

##### Calculations

- None

##### Workflow

CONFIGURED → VALIDATED → PUBLISHED → SUPERSEDED

##### Search requirements

- Search administrator permissions by module name
- Filter permissions by functional group

##### Documents

- Administrator permission matrix export for security review

##### Reports

- Examination Administrator effective permission listing

##### Notifications

- Notify security team when administrator permission snapshot changes materially

##### Security

- Organisation-wide grants must never include centre-only invigilator operational permissions unless explicitly dual-assigned
- All changes require authenticated administrator identity
- Immutable snapshot history retained

##### Integrations

- Permission consumption by Modules 03, 04, 06, 08, 10, 11, and 12 administrative functions

##### Dependencies

- F01-006 Examination Administrator User Register and Account Lifecycle for user assignment
- F01-008 Role and Permission Matrix Administration
- F01-012 Downstream Module Actor Authorization Integration Hooks

##### Assumptions

- Single departmental administrator persona is sufficient; sub-administrator variants use permission toggles not separate roles

##### Risks

- Broad organisation-wide grants increase impact of compromised administrator credentials

##### Non-functional requirements

- Administrator permission resolution must complete within portal navigation thresholds
- Snapshot versioning supports rollback analysis after security incidents

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination Administrator role summary with organisation-wide scope badge | Easy | 14 |
| UI | Administrator permission group tabs by module responsibility | Complex | 18 |
| UI | Permission row with mandatory group indicator and description tooltip | Medium | 16 |
| UI | Segregation-of-duties warning banner on sensitive grant changes | Medium | 16 |
| UI | Publish administrator snapshot confirmation dialog | Simple | 5 |
| API | Retrieve Examination Administrator role with scope metadata | Easy | 4 |
| API | List organisation-wide permissions grouped by functional area | Medium | 6 |
| API | Update administrator permission grant with mandatory group guard | Complex | 8 |
| API | Publish administrator permission snapshot | Complex | 8 |
| API | Resolve organisation-wide claims for assigned administrator users | Medium | 6 |
| Database | Examination Administrator role record with org-wide scope flag | Simple | 0.1 |
| Database | Administrator permission catalogue entries by module group | Medium | 0.3 |
| Database | Administrator role-permission mapping history | Medium | 0.3 |
| Testing | Happy path publish organisation-wide administrator snapshot | Medium | 0.3 |
| Testing | Mandatory group empty-set rejection cases | Medium | 0.3 |
| Testing | Security case preventing centre-scope attribute on administrator role | Complex | 0.5 |
| Documentation | Administrator permission matrix administrator guide | Medium | 0.3 |
| Documentation | Technical mapping notes from permissions to downstream modules | Medium | 0.3 |

### F01-009 Centre Invigilator Role and Centre-Scoped Access Model

93.4 hours · Go-live · 19 tasks

##### Description

Defines the Examination Centre/Invigilator User role per SOW §3.3 with centre-scoped permission enforcement so centre users access only examinations, candidates, and activities mapped to their assigned authorised centre.

##### Business objective

Prevent cross-centre data exposure while granting invigilator permissions for verification, session activation, attendance monitoring, and centre dashboard access described in Modules 08 and 09 handoffs.

##### Actors

- Examination Administrator
- Examination Centre/Invigilator User
- System

##### User journey

1. Administrator selects Centre/Invigilator role definition.
2. Administrator views centre-scoped access model summary explaining data isolation rules.
3. Administrator configures permission grants for centre dashboard, candidate register, identity verification, session activation, live monitoring, and centre-level activities.
4. Administrator confirms each permission is tagged as centre-scoped requiring centre binding on user assignment.
5. Administrator publishes centre invigilator permission snapshot.
6. Invigilator user logs in and system resolves assigned centre identifiers into session claims.
7. Invigilator opens centre dashboard; system filters all data to assigned centre only.
8. Attempt to access another centre's examination session is denied with auditable rejection.

##### Functional capabilities

- Maintain Centre/Invigilator role with mandatory centre-scope enforcement flag
- Catalogue permissions for centre examination day dashboard access
- Catalogue permissions for scheduled candidate register visibility
- Catalogue permissions for candidate identity verification and attendance marking
- Catalogue permissions for candidate examination session activation
- Catalogue permissions for live examination session monitoring
- Enforce centre identifier filter on all invigilator permission checks
- Deny cross-centre resource access with explicit audit reason

##### Inputs

- Centre/Invigilator role identifier
- Permission grant selections
- Centre-scope enforcement policy flag
- Assigned centre identifiers at user level

##### Outputs

- Centre-scoped role definition
- Invigilator permission catalogue
- Centre-filtered authorization decision
- Cross-centre access denial audit entry

##### Business rules

- Every Centre/Invigilator permission evaluation must include assigned centre identifier
- Invigilator users without centre assignment cannot access operational centre screens
- Centre-scoped permissions align to Module 08 centre operations without re-implementing those screens
- Organisation-wide administrator permissions must not apply to invigilator role unless dual-assigned

##### Validations

- Centre-scope flag cannot be disabled for this role
- Permission grant requires centre binding metadata on consuming operations
- Requested resource centre must match user assigned centre
- Inactive centre assignment blocks operational permissions

##### Calculations

- None

##### Workflow

ROLE_DEFINED → CENTRE_SCOPE_ENFORCED → USER_ASSIGNED → SESSION_SCOPED → ACCESS_GRANTED or ACCESS_DENIED

##### Search requirements

- Filter invigilator permissions applicable to centre operations only

##### Documents

- Centre-scoped access policy summary for centre onboarding

##### Reports

- Centre invigilator effective permission listing by assigned centre

##### Notifications

- Alert administrator when invigilator user lacks centre assignment at login

##### Security

- Mandatory centre isolation on every authorization check
- Cross-centre access attempts logged as security events
- Session claims include centre identifiers immutable for session lifetime unless re-authenticated

##### Integrations

- Centre assignment data from Module 03 Centre Invigilator User Assignment
- Authorization enforcement for Module 08 Centre Operations screens

##### Dependencies

- F03-003 Centre Invigilator User Assignment provides centre binding source
- F01-007 Centre Invigilator User Register Centre Binding and Lifecycle
- F01-012 Downstream Module Actor Authorization Integration Hooks

##### Assumptions

- Each invigilator user is assigned to exactly one primary centre unless future multi-centre assignment is approved

##### Risks

- Missing centre filter in a downstream module could leak candidate data across centres

##### Non-functional requirements

- Centre scope resolution must add negligible latency to dashboard queries
- Authorization denials must be traceable for audit

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre invigilator role summary with centre-scope enforcement badge | Easy | 14 |
| UI | Centre-scoped permission catalogue list for dashboard and verification functions | Medium | 16 |
| UI | Centre binding requirement indicator on each invigilator permission row | Easy | 14 |
| UI | Cross-centre access denial message panel for invigilator users | Simple | 5 |
| API | Retrieve Centre/Invigilator role with centre-scope metadata | Easy | 4 |
| API | List centre-scoped invigilator permissions | Medium | 6 |
| API | Update invigilator permission grant with scope enforcement tag | Medium | 6 |
| API | Resolve centre-scoped claims for invigilator session | Complex | 8 |
| API | Evaluate centre-filtered authorization decision for resource access | Complex | 8 |
| API | Record cross-centre access denial audit event | Medium | 6 |
| Database | Centre/Invigilator role record with scope enforcement flag | Simple | 0.1 |
| Database | Centre-scoped permission catalogue entries | Medium | 0.3 |
| Database | User-centre assignment linkage for invigilator scope resolution | Medium | 0.3 |
| Integration | Consume centre assignment identifiers from Module 03 for scope binding | Simple | 4 |
| Testing | Happy path invigilator access within assigned centre | Medium | 0.3 |
| Testing | Cross-centre resource access rejection cases | Complex | 0.5 |
| Testing | Invigilator login without centre assignment blocked cases | Medium | 0.3 |
| Documentation | Centre-scoped access administrator runbook | Medium | 0.3 |
| Documentation | Technical centre-scope enforcement notes for Module 08 integrators | Medium | 0.3 |

### F01-010 Verifier Public Role and Anonymous Verification Access Policy

88.3 hours · Go-live · 18 tasks

##### Description

Defines the Verifier/Public User access model per SOW §3.4 and §36 enabling anonymous or lightly authenticated public users to scan certificate QR codes and verify departmental issuance without staff credentials.

##### Business objective

Separate public verification access from internal staff roles while controlling which certificate fields may be disclosed on the verification response.

##### Actors

- Verifier/Public User
- Examination Administrator
- System

##### User journey

1. Administrator opens Verifier/Public role and access policy configuration.
2. Administrator reviews public verification scope: QR scan entry, certificate lookup, genuine/issued status display, cancelled/revoked status display.
3. Administrator configures publicly disclosable field set approved for verification page.
4. Administrator sets rate-limit and anonymous access policy flags.
5. Administrator publishes public verification access policy snapshot.
6. Public user scans certificate QR code on Module 11 verification portal.
7. System applies Verifier/Public policy to determine allowed response fields and denial messages.
8. Cancelled or revoked certificates return policy-defined status without staff login.

##### Functional capabilities

- Maintain Verifier/Public role as non-staff anonymous access actor
- Define public verification permissions separate from candidate and administrator roles
- Configure publicly disclosable certificate verification fields
- Configure denied-access messaging for invalid or revoked certificates
- Apply rate-limit policy metadata for anonymous verification requests
- Publish public verification access policy for Module 11 consumption
- Support unauthenticated verification session without staff password login

##### Inputs

- Public verification policy toggles
- Disclosable field allow-list
- Rate-limit thresholds
- Revoked certificate response template

##### Outputs

- Verifier/Public role definition
- Public verification access policy snapshot
- Field disclosure rules for verification responses
- Anonymous access configuration metadata

##### Business rules

- Public verification does not require staff user account provisioning
- Only approved certificate fields may appear on public verification responses
- Revoked or cancelled certificates must surface appropriate status per Module 11 rules
- Public role must not grant access to internal administrative functions

##### Validations

- Disclosable field list must be non-empty
- Sensitive internal identifiers must be excluded from public allow-list
- Rate-limit values must be positive integers
- Policy publisher must hold administrator role-management permission

##### Calculations

- None

##### Workflow

POLICY_DRAFT → POLICY_PUBLISHED → APPLIED_ON_VERIFICATION_REQUEST → RESPONSE_ALLOWED or RESPONSE_DENIED

##### Search requirements

- Search public policy fields by disclosure category

##### Documents

- Public verification privacy disclosure summary

##### Reports

- Public verification policy effective configuration listing

##### Notifications

- None for anonymous public users

##### Security

- Anonymous access limited strictly to verification endpoints
- Rate limiting mitigates enumeration attacks
- No staff session created for public verification actor

##### Integrations

- Policy consumption by Module 11 Public Online Certificate Verification Portal

##### Dependencies

- F11-004 Public Online Certificate Verification Portal implements verification UI
- F01-012 Downstream Module Actor Authorization Integration Hooks

##### Assumptions

- Public users interact via mobile QR scan without registration

##### Risks

- Over-disclosure in public field allow-list could expose personal data
- Insufficient rate limiting could enable bulk certificate probing

##### Non-functional requirements

- Policy snapshot must be lightweight for high-volume anonymous traffic
- Verification policy changes apply without redeploying Module 11 UI

##### Notes

Public QR verification UI is implemented in Module 11; this feature owns access policy and role definition.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Verifier/Public role read-only summary for anonymous access model | Simple | 5 |
| UI | Public verification disclosable field allow-list editor | Medium | 16 |
| UI | Revoked certificate public response template editor | Easy | 14 |
| UI | Anonymous rate-limit policy configuration form | Medium | 16 |
| UI | Publish public verification policy confirmation dialog | Simple | 5 |
| API | Retrieve Verifier/Public role and access policy definition | Easy | 4 |
| API | Update public disclosable field allow-list | Medium | 6 |
| API | Update anonymous rate-limit policy settings | Medium | 6 |
| API | Publish public verification access policy snapshot | Complex | 8 |
| API | Resolve anonymous verification authorization decision | Medium | 6 |
| Database | Verifier/Public role record for anonymous actor | Simple | 0.1 |
| Database | Public field disclosure allow-list storage | Easy | 0.25 |
| Database | Public verification policy snapshot versioning | Medium | 0.3 |
| Testing | Happy path anonymous verification policy publish and apply | Medium | 0.3 |
| Testing | Sensitive field exclusion validation rejection cases | Medium | 0.3 |
| Testing | Rate-limit threshold edge and security abuse cases | Complex | 0.5 |
| Documentation | Public verification privacy administrator runbook | Medium | 0.3 |
| Documentation | Technical policy consumption notes for Module 11 | Easy | 0.25 |

### F01-011 Staff Password Authentication and Login Session

85.5 hours · Go-live · 20 tasks

##### Description

Provides password-based authentication and authenticated session establishment for Examination Administrator and Centre/Invigilator staff users including login, logout, failed attempt handling, and role claim issuance.

##### Business objective

Give non-candidate staff a secure entry point to administrative and centre interfaces distinct from candidate OTP authentication.

##### Actors

- Examination Administrator
- Examination Centre/Invigilator User
- System

##### User journey

1. Staff user navigates to staff login page.
2. User enters username or official email and password.
3. System validates account exists, is active, and is not locked.
4. System validates password against stored credential.
5. On failure, system increments failed attempt counter and displays generic error.
6. On lockout threshold, system blocks further attempts until lockout window expires.
7. On success, system creates authenticated session with role and centre scope claims.
8. User lands on role-appropriate home dashboard.
9. User selects logout; system terminates session and clears client tokens.

##### Functional capabilities

- Present staff login screen separate from candidate OTP portal entry
- Authenticate administrator users with password credentials
- Authenticate centre invigilator users with password credentials
- Issue session token containing role identifiers and centre scope where applicable
- Track failed login attempts per user account
- Apply account lockout after configured failed attempt threshold
- Terminate session on explicit logout
- Reject login for deactivated user accounts

##### Inputs

- Username or email
- Password
- Client device metadata
- Requested portal context admin versus centre

##### Outputs

- Authenticated session token
- Role and scope claims payload
- Login failure response with lockout status
- Logout confirmation

##### Business rules

- Candidate OTP login path is not handled in this feature
- Only active staff accounts may authenticate
- Lockout policy values come from password policy configuration feature
- Centre invigilator sessions must include assigned centre claims at login
- Concurrent session rules enforced by session management feature

##### Validations

- Username or email must match registered staff account format
- Password must not be empty
- Deactivated account login rejected regardless of password correctness
- Locked account login rejected with remaining lockout duration
- Invigilator account without centre assignment rejected at login

##### Calculations

- Failed attempt count increment on each failed authentication
- Lockout expiry timestamp from policy lockout duration

##### Workflow

UNAUTHENTICATED → CREDENTIALS_SUBMITTED → VALIDATED → SESSION_ACTIVE → LOGGED_OUT or SESSION_EXPIRED

##### Search requirements

- None on login screen

##### Documents

- Staff login quick reference for centre onboarding

##### Reports

- Failed login attempt summary for security monitoring

##### Notifications

- Optional email alert to user after lockout trigger

##### Security

- Passwords stored using strong one-way hashing
- Generic error messages prevent account enumeration
- Session tokens signed and time-bound
- All login and logout events auditable

##### Integrations

- None external; internal credential validation only

##### Dependencies

- F01-006 Examination Administrator User Register and Account Lifecycle
- F01-007 Centre Invigilator User Register Centre Binding and Lifecycle
- F01-009 Session Timeout Idle Lock and Concurrent Session Controls
- F01-010 Password Credential Policy Configuration and Reset Flows

##### Assumptions

- Staff users receive initial credentials through administrator provisioning process

##### Risks

- Shared centre workstation sessions require strict timeout enforcement

##### Non-functional requirements

- Login response within acceptable enterprise portal thresholds
- Credential verification resistant to timing attacks

##### Notes

Candidate OTP login is out of scope; covered by Module 05.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Staff login screen with username email and password fields | Easy | 14 |
| UI | Login failure message panel with generic error text | Simple | 5 |
| UI | Account lockout message panel with retry countdown | Simple | 5 |
| UI | Post-login role-based landing redirect handler | Easy | 14 |
| UI | Staff logout confirmation control on header menu | Simple | 5 |
| API | Authenticate staff user with password verification | Complex | 8 |
| API | Issue authenticated session token with role claims | Complex | 8 |
| API | Resolve centre scope claims for invigilator at login | Medium | 6 |
| API | Increment failed login attempt counter | Easy | 4 |
| API | Apply account lockout when threshold exceeded | Medium | 6 |
| API | Reject login for deactivated staff accounts | Easy | 4 |
| API | Terminate session on logout | Easy | 4 |
| Database | Staff credential storage with hash metadata | Medium | 0.3 |
| Database | Failed login attempt counter and lockout timestamp | Easy | 0.25 |
| Database | Active session registry for staff users | Medium | 0.3 |
| Testing | Happy path administrator and invigilator login flows | Medium | 0.3 |
| Testing | Invalid password and deactivated account rejection cases | Medium | 0.3 |
| Testing | Lockout threshold and invigilator missing centre assignment edge cases | Complex | 0.5 |
| Documentation | Staff login administrator and centre user runbook | Easy | 0.25 |
| Documentation | Technical authentication flow notes for security review | Medium | 0.3 |

### F01-014 Examination Administrator User Register and Account Lifecycle

119.7 hours · Go-live · 22 tasks

##### Description

Manages full account lifecycle for Examination Administrator staff users including register listing, create, edit, activate, deactivate, and role assignment without centre binding.

##### Business objective

Enable departmental IT administrators to provision and retire back-office administrator accounts tied to organisation-wide role permissions.

##### Actors

- Examination Administrator
- System

##### User journey

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

##### Functional capabilities

- List and search administrator user accounts with filters
- Create administrator user with unique email and employee identifier
- Edit administrator user profile fields
- Assign or change Examination Administrator role on user account
- Activate newly provisioned administrator account
- Deactivate administrator account without deleting audit history
- Reactivate deactivated administrator account
- Display administrator user status and last login metadata

##### Inputs

- Display name
- Official email
- Mobile number
- Employee identifier
- Role assignment selection
- Active or inactive status

##### Outputs

- Administrator user register rows
- Created user account record
- Updated profile record
- Activation or deactivation confirmation
- Initial credential dispatch trigger

##### Business rules

- Administrator users are not centre-scoped
- Deactivation preserves historical audit attribution
- At least one active super-administrator must remain at all times
- Employee identifier unique among active administrator accounts

##### Validations

- Email format validation and uniqueness among staff users
- Mobile number ten-digit format validation and uniqueness where required
- Employee identifier required and unique among active accounts
- Display name minimum length validation
- Cannot deactivate the last active super-administrator
- Cannot assign centre-scoped-only role without explicit dual-role policy

##### Calculations

- None

##### Workflow

DRAFT → ACTIVE → DEACTIVATED → REACTIVATED; ACTIVE → DEACTIVATED

##### Search requirements

- Search by name substring
- Filter by email
- Filter by active inactive status
- Filter by role assignment

##### Documents

- Administrator user provisioning checklist

##### Reports

- Active administrator user listing export

##### Notifications

- Email notification to new administrator with initial credential instructions

##### Security

- Only privileged administrators may create or deactivate administrator accounts
- All lifecycle changes audit logged

##### Integrations

- Initial credential generation handoff to password reset feature

##### Dependencies

- F01-002 Examination Administrator Role and Organisation-Wide Permissions
- F01-005 Staff Password Authentication and Login Session
- F01-010 Password Credential Policy Configuration and Reset Flows

##### Assumptions

- Super-administrator is an administrator user with elevated role-management permissions

##### Risks

- Orphaned active accounts after staff departure if deactivation process skipped

##### Non-functional requirements

- Register pagination for large departmental user populations
- Optimistic concurrency on profile edits

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Administrator user register list with search filters and status chips | Medium | 16 |
| UI | Create administrator user form with email mobile and employee ID | Medium | 16 |
| UI | Edit administrator user profile form | Medium | 16 |
| UI | Administrator role assignment selector on user form | Easy | 14 |
| UI | Deactivate administrator user confirmation dialog | Simple | 5 |
| UI | Reactivate administrator user confirmation dialog | Simple | 5 |
| UI | Administrator register empty state when no users match filters | Simple | 5 |
| API | List and search administrator users with filters | Medium | 6 |
| API | Create administrator user with uniqueness validation | Complex | 8 |
| API | Update administrator user profile fields | Medium | 6 |
| API | Assign Examination Administrator role to user account | Medium | 6 |
| API | Activate administrator user account | Easy | 4 |
| API | Deactivate administrator user without history deletion | Medium | 6 |
| API | Export active administrator user listing | Easy | 4 |
| Database | Administrator user core entity | Medium | 0.3 |
| Database | Unique constraints on email and employee identifier | Complex | 0.5 |
| Database | Administrator user status and last login audit fields | Easy | 0.25 |
| Testing | Happy path create edit activate deactivate administrator user | Medium | 0.3 |
| Testing | Duplicate email employee ID and invalid mobile rejection cases | Medium | 0.3 |
| Testing | Last super-administrator deactivation blocked edge case | Complex | 0.5 |
| Documentation | Administrator user provisioning administrator runbook | Medium | 0.3 |
| Documentation | Technical administrator account lifecycle notes | Easy | 0.25 |

### F01-015 Centre Invigilator User Register Centre Binding and Lifecycle

130.45 hours · Go-live · 21 tasks

##### Description

Manages Centre/Invigilator staff user accounts with mandatory authorised examination centre binding, covering register, create, edit, centre reassignment, activate, and deactivate lifecycle per SOW §3.3 and Module 03 assignment handoff.

##### Business objective

Ensure every invigilator account is explicitly tied to an authorised centre before centre operational access is granted.

##### Actors

- Examination Administrator
- Examination Centre/Invigilator User
- System

##### User journey

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

##### Functional capabilities

- List and search invigilator users with centre filter
- Create invigilator user with mandatory centre selection
- Edit invigilator profile fields
- Reassign invigilator to different authorised centre
- Activate invigilator account after centre binding confirmed
- Deactivate invigilator account preserving audit history
- Validate centre is active before binding
- Display centre name and centre ID on register rows

##### Inputs

- Display name
- Email
- Mobile number
- Employee or staff identifier
- Authorised centre selection
- Account status

##### Outputs

- Invigilator register listing with centre column
- Created invigilator account with centre binding
- Centre reassignment audit record
- Activation or deactivation confirmation

##### Business rules

- Invigilator account cannot be activated without centre assignment
- Only active authorised centres appear in centre selector
- Centre reassignment takes effect on next login session
- Deactivated invigilator immediately loses centre operational access

##### Validations

- Centre selection required on create
- Selected centre must be active in centre master
- Email uniqueness among staff users
- Mobile format validation
- Cannot reassign to inactive centre
- Cannot deactivate invigilator mid-session without session termination handled by session feature

##### Calculations

- None

##### Workflow

PENDING_CENTRE_BINDING → ACTIVE → CENTRE_REASSIGNED → ACTIVE; ACTIVE → DEACTIVATED

##### Search requirements

- Search by invigilator name
- Filter by assigned centre
- Filter by account status

##### Documents

- Centre invigilator onboarding checklist

##### Reports

- Invigilator listing by centre export

##### Notifications

- Notify invigilator email on centre assignment or reassignment

##### Security

- Centre binding changes audit logged with before and after centre identifiers
- Only administrators with centre user management permission may reassign centres

##### Integrations

- Active centre list retrieval from Module 03 Authorised Examination Centre Master

##### Dependencies

- F03-001 Authorised Examination Centre Master Lifecycle for centre selector source
- F03-003 Centre Invigilator User Assignment aligns operational assignment rules
- F01-003 Centre Invigilator Role and Centre-Scoped Access Model
- F01-005 Staff Password Authentication and Login Session

##### Assumptions

- One primary centre per invigilator account at a time

##### Risks

- Stale centre binding if centre deactivated without invigilator reassignment

##### Non-functional requirements

- Centre selector performant against full authorised centre catalogue

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre invigilator user register list with centre column and filters | Medium | 16 |
| UI | Create invigilator user form with mandatory centre selector | Complex | 18 |
| UI | Edit invigilator user profile form | Medium | 16 |
| UI | Centre reassignment dialog showing previous and new centre | Medium | 16 |
| UI | Deactivate invigilator user confirmation dialog | Simple | 5 |
| UI | Invigilator register empty state for centre filter with no matches | Simple | 5 |
| API | List and search invigilator users with centre filter | Medium | 6 |
| API | Create invigilator user with centre binding validation | Complex | 8 |
| API | Update invigilator profile fields | Medium | 6 |
| API | Reassign invigilator to different authorised centre | Complex | 8 |
| API | Activate invigilator account after centre binding confirmed | Medium | 6 |
| API | Deactivate invigilator account preserving history | Medium | 6 |
| API | Export invigilator listing by centre | Easy | 4 |
| Database | Invigilator user core entity | Medium | 0.3 |
| Database | User-to-centre binding with reassignment history | Complex | 0.5 |
| Integration | Fetch active authorised centre list from Module 03 for selector | Easy | 8 |
| Testing | Happy path create bind activate invigilator user | Medium | 0.3 |
| Testing | Missing centre inactive centre and duplicate email rejection cases | Medium | 0.3 |
| Testing | Centre reassignment login scope update edge cases | Complex | 0.5 |
| Documentation | Centre invigilator provisioning administrator runbook | Medium | 0.3 |
| Documentation | Technical centre binding lifecycle notes | Easy | 0.25 |

### F01-016 Role and Permission Matrix Administration

141.9 hours · Go-live · 19 tasks

##### Description

Provides consolidated administration screens to view and maintain role-to-permission mappings across Candidate, Examination Administrator, Centre/Invigilator, and Verifier/Public roles with compare and publish controls.

##### Business objective

Give security administrators a single matrix workspace to govern platform access consistently across all actor types.

##### Actors

- Examination Administrator
- System

##### User journey

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

##### Functional capabilities

- Display cross-role permission matrix grid
- Filter matrix by module permission group
- Toggle editable permission grants per role intersection
- Show mandatory and read-only permission indicators
- Compare draft matrix against published snapshot
- Publish consolidated permission matrix snapshot
- Export matrix to file for audit
- Invalidate downstream authorization caches on publish

##### Inputs

- Role selection
- Permission group filter
- Cell grant toggle changes
- Publish effective timestamp

##### Outputs

- Matrix grid view
- Draft versus published diff summary
- Published matrix snapshot
- Exported audit file

##### Business rules

- Candidate OTP execution permissions remain read-only references to Module 05
- Mandatory permissions cannot be toggled off via matrix without override workflow
- Matrix publish supersedes individual role draft states atomically
- Verifier/Public row set limited to public verification permissions

##### Validations

- Draft matrix must pass mandatory permission guard before publish
- Effective timestamp cannot precede latest published matrix
- Publisher must hold role-management permission
- Cannot publish empty matrix

##### Calculations

- Diff count of added and removed grants between draft and published

##### Workflow

MATRIX_VIEW → DRAFT_EDITED → DIFF_REVIEWED → PUBLISHED → CACHE_INVALIDATED

##### Search requirements

- Search permission label within matrix
- Filter matrix rows by module group

##### Documents

- Exported permission matrix audit file

##### Reports

- Role permission diff report after publish

##### Notifications

- Notify security administrators on matrix publish

##### Security

- Matrix edit restricted to privileged administrators
- Full publish history immutable

##### Integrations

- Cache invalidation signal to F01-012 authorization hooks

##### Dependencies

- F01-001 Candidate Role and Portal Permission Catalogue
- F01-002 Examination Administrator Role and Organisation-Wide Permissions
- F01-003 Centre Invigilator Role and Centre-Scoped Access Model
- F01-004 Verifier Public Role and Anonymous Verification Access Policy

##### Assumptions

- Permission master catalogue pre-seeded from module capability registry

##### Risks

- Large matrix UI performance with hundreds of permissions

##### Non-functional requirements

- Matrix load paginated or grouped for usability
- Publish operation transactional

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Cross-role permission matrix grid with role columns | Very high | 24 |
| UI | Permission group row filter panel on matrix | Medium | 16 |
| UI | Editable permission cell toggle with mandatory read-only indicator | Medium | 16 |
| UI | Draft versus published matrix compare diff summary screen | Complex | 18 |
| UI | Publish matrix snapshot confirmation dialog | Simple | 5 |
| UI | Matrix export action with format selection | Easy | 14 |
| API | Retrieve cross-role permission matrix grid data | Complex | 8 |
| API | Update draft permission grant at role intersection | Medium | 6 |
| API | Generate draft versus published matrix diff summary | Complex | 8 |
| API | Publish consolidated permission matrix snapshot | Very high | 12 |
| API | Export permission matrix audit file | Medium | 6 |
| API | Trigger downstream authorization cache invalidation | Medium | 6 |
| Database | Draft matrix state storage | Medium | 0.3 |
| Database | Published matrix snapshot versioning | Complex | 0.5 |
| Testing | Happy path matrix edit compare and publish flow | Complex | 0.5 |
| Testing | Mandatory permission toggle rejection validation cases | Medium | 0.3 |
| Testing | Concurrent draft edit conflict edge cases | Complex | 0.5 |
| Documentation | Permission matrix administrator runbook | Complex | 0.5 |
| Documentation | Technical matrix publish and cache invalidation notes | Medium | 0.3 |

### F01-017 Session Timeout Idle Lock and Concurrent Session Controls

113.15 hours · Go-live · 21 tasks

##### Description

Configures and enforces session timeout, idle lock, absolute session lifetime, and concurrent session limits for Examination Administrator and Centre/Invigilator authenticated sessions per SOW session control expectations.

##### Business objective

Reduce credential misuse risk on shared centre workstations and unattended administrator terminals.

##### Actors

- Examination Administrator
- Examination Centre/Invigilator User
- System

##### User journey

1. Administrator opens session policy configuration for staff portals.
2. Administrator sets idle timeout duration, absolute session lifetime, and concurrent session limit per role type.
3. Administrator saves policy and publishes to active sessions on next request.
4. Staff user works in authenticated session; activity heartbeat refreshes idle timer.
5. On idle threshold breach, system displays session lock overlay requiring re-authentication.
6. On absolute lifetime expiry, system redirects to login with session expired message.
7. When concurrent session limit exceeded at login, system terminates oldest session or blocks new login per policy.
8. Administrator views active staff session register for forced logout if needed.

##### Functional capabilities

- Configure idle timeout duration for administrator sessions
- Configure idle timeout duration for invigilator sessions
- Configure absolute maximum session lifetime
- Configure concurrent session limit per user account
- Track session last activity timestamp
- Lock session on idle timeout pending re-authentication
- Expire session on absolute lifetime breach
- Enforce concurrent session policy at login
- List active staff sessions with forced logout action

##### Inputs

- Idle timeout minutes
- Absolute session lifetime minutes
- Concurrent session limit integer
- Role type specific overrides
- Session activity heartbeat events

##### Outputs

- Published session policy configuration
- Idle lock overlay trigger
- Session expired redirect
- Concurrent session termination or block decision
- Active session register listing

##### Business rules

- Session policies apply to staff users only; candidate OTP session rules remain in Module 05
- Invigilator idle timeout may be shorter than administrator default for shared devices
- Forced logout immediately invalidates session token
- Session expiry events are audit logged

##### Validations

- Idle timeout must be less than absolute session lifetime
- Timeout values must be positive integers within configured max bounds
- Concurrent session limit minimum of one
- Forced logout requires administrator privilege

##### Calculations

- Idle expiry timestamp from last activity plus idle timeout
- Absolute expiry timestamp from session start plus absolute lifetime

##### Workflow

SESSION_ACTIVE → IDLE_WARNING → IDLE_LOCKED → REAUTHENTICATED or SESSION_TERMINATED; SESSION_ACTIVE → ABSOLUTE_EXPIRED → TERMINATED

##### Search requirements

- Filter active session register by user name
- Filter active sessions by role type

##### Documents

- Session policy configuration guide for centre managers

##### Reports

- Active staff session listing export

##### Notifications

- Optional idle warning toast before lock threshold

##### Security

- Session tokens invalidated on forced logout
- Idle lock requires password re-entry not full re-provision
- Concurrent session enforcement prevents credential sharing abuse

##### Integrations

- None external

##### Dependencies

- F01-005 Staff Password Authentication and Login Session
- F01-010 Password Credential Policy Configuration and Reset Flows for re-auth

##### Assumptions

- Client sends periodic activity heartbeat while user interacts with portal

##### Risks

- Overly aggressive idle lock disrupts invigilator operations during live examinations

##### Non-functional requirements

- Session validation on each request with minimal overhead
- Policy changes apply without server restart

##### Notes

Applies to non-candidate staff sessions only.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Staff session policy configuration form by role type | Medium | 16 |
| UI | Idle session lock overlay with re-authentication prompt | Medium | 16 |
| UI | Session expired redirect page with re-login link | Simple | 5 |
| UI | Idle warning toast before lock threshold | Simple | 5 |
| UI | Active staff session register list with forced logout action | Medium | 16 |
| UI | Concurrent session blocked message panel at login | Simple | 5 |
| API | Retrieve staff session policy configuration | Easy | 4 |
| API | Update and publish staff session policy settings | Medium | 6 |
| API | Record session activity heartbeat timestamp | Easy | 4 |
| API | Evaluate idle and absolute session expiry on request | Complex | 8 |
| API | Re-authenticate locked session with password verification | Medium | 6 |
| API | Enforce concurrent session limit at login | Complex | 8 |
| API | List active staff sessions with metadata | Medium | 6 |
| API | Force logout selected active staff session | Medium | 6 |
| Database | Session policy configuration storage | Easy | 0.25 |
| Database | Active session registry with activity timestamps | Medium | 0.3 |
| Testing | Happy path idle lock re-auth and absolute expiry flows | Medium | 0.3 |
| Testing | Invalid policy value rejection cases | Easy | 0.25 |
| Testing | Concurrent session limit and forced logout edge cases | Complex | 0.5 |
| Documentation | Session policy administrator runbook | Medium | 0.3 |
| Documentation | Technical session enforcement notes for portal teams | Easy | 0.25 |

### F01-018 Password Credential Policy Configuration and Reset Flows

137.5 hours · Go-live · 23 tasks

##### Description

Defines configurable password and credential policies for staff users and implements self-service and administrator-assisted password reset flows including initial credential setup.

##### Business objective

Enforce departmental password standards and recover staff access without compromising candidate OTP authentication handled elsewhere.

##### Actors

- Examination Administrator
- Examination Centre/Invigilator User
- System

##### User journey

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

##### Functional capabilities

- Configure minimum password length rule
- Configure complexity requirements for uppercase lowercase digit special
- Configure password history depth preventing reuse
- Configure password expiry interval for staff accounts
- Configure lockout threshold linkage metadata
- Enforce policy on password set and change operations
- First-login forced password change workflow
- Self-service forgot password request and token validation
- Administrator-initiated forced password reset

##### Inputs

- Policy numeric thresholds
- Complexity rule toggles
- New password and confirmation
- Reset token
- Administrator force reset target user

##### Outputs

- Published password policy record
- Password validation result with field errors
- Reset token email dispatch
- Updated credential hash
- Force reset confirmation

##### Business rules

- Password policies apply to staff users only
- Expired password blocks login until changed via approved flow
- Reset tokens single-use and time-limited
- Password history prevents reuse of last N passwords

##### Validations

- Minimum length at least policy configured minimum
- Complexity rules each satisfied when enabled
- New password must differ from current password
- New password must not match entries in password history
- Reset token expiry validation
- Password confirmation must match new password

##### Calculations

- Password expiry date from last change plus expiry interval days
- Lockout threshold read from policy into login authentication

##### Workflow

POLICY_CONFIGURED → CREDENTIAL_SET → ACTIVE → EXPIRED → MUST_CHANGE → ACTIVE; RESET_REQUESTED → TOKEN_ISSUED → TOKEN_VALIDATED → CREDENTIAL_UPDATED

##### Search requirements

- None

##### Documents

- Staff password policy user guidance leaflet

##### Reports

- Staff accounts with expired passwords listing

##### Notifications

- Email with password reset link
- Email notification on administrator forced reset

##### Security

- Reset tokens hashed at rest
- Passwords never stored in plain text
- Rate limit on reset requests per email

##### Integrations

- Email dispatch via Module 07 Notification Service for reset messages

##### Dependencies

- F01-005 Staff Password Authentication and Login Session
- F07-004 Multi-Channel Notification Dispatch Engine for reset emails

##### Assumptions

- Staff users have registered official email for reset delivery

##### Risks

- Weak policy defaults could fail departmental security audit

##### Non-functional requirements

- Password hashing uses approved enterprise algorithm parameters
- Policy evaluation on change completes synchronously before confirmation

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Password policy configuration form with complexity toggles | Medium | 16 |
| UI | First-login forced password change screen with inline rule hints | Medium | 16 |
| UI | Forgot password request screen with email entry | Easy | 14 |
| UI | Password reset token entry and new password form | Medium | 16 |
| UI | Administrator force password reset confirmation dialog | Simple | 5 |
| UI | Expired password change required blocking screen after login | Easy | 14 |
| API | Retrieve published password policy configuration | Easy | 4 |
| API | Update and publish password policy settings | Medium | 6 |
| API | Validate new password against live policy rules | Complex | 8 |
| API | Change password with history reuse prevention | Complex | 8 |
| API | Initiate self-service forgot password reset request | Medium | 6 |
| API | Validate reset token and set new password | Complex | 8 |
| API | Administrator force password reset for target user | Medium | 6 |
| API | List staff accounts with expired passwords | Easy | 4 |
| Database | Password policy configuration record | Easy | 0.25 |
| Database | Password history storage per staff user | Medium | 0.3 |
| Database | Reset token storage with expiry metadata | Medium | 0.3 |
| Integration | Dispatch password reset email through Module 07 notification engine | Simple | 4 |
| Testing | Happy path first login change and self-service reset flows | Medium | 0.3 |
| Testing | Complexity history reuse and expired token rejection cases | Complex | 0.5 |
| Testing | Reset request rate limit security cases | Medium | 0.3 |
| Documentation | Password policy administrator runbook | Medium | 0.3 |
| Documentation | Staff password reset user guide | Easy | 0.25 |

### F01-019 User Access Audit Register and Security Event Trace

113.45 hours · Go-live · 19 tasks

##### Description

Captures and presents auditable records of user lifecycle changes, role assignment changes, login logout events, permission publishes, and authorization denials for staff and role administration aligned to SOW §41 audit expectations for identity activities.

##### Business objective

Provide examination administrators forensic visibility into identity and access control changes supporting compliance and incident investigation.

##### Actors

- Examination Administrator
- System

##### User journey

1. Administrator opens user access audit register.
2. Register defaults to recent identity events with timestamp descending sort.
3. Administrator applies filters for event type, actor, target user, date range, and centre where applicable.
4. Administrator opens event detail drawer showing before and after values for change events.
5. Administrator exports filtered audit slice for compliance submission.
6. Security reviewer searches failed login and cross-centre denial events.
7. System automatically records events from user lifecycle, login, permission publish, and authorization hook denials without manual entry.

##### Functional capabilities

- Record user account create update activate deactivate events
- Record role assignment and centre binding change events
- Record staff login logout success and failure events
- Record permission matrix publish events
- Record authorization denial events from integration hooks
- List audit events with multi-field filters
- Display event detail with before and after payload
- Export filtered audit register slice

##### Inputs

- Event type filter selections
- Date range
- Actor user identifier
- Target user identifier
- Centre filter
- Automatic event payloads from platform actions

##### Outputs

- Audit register paginated listing
- Event detail view
- Exported audit file
- Security event counts by type

##### Business rules

- Audit records are append-only and cannot be edited or deleted via UI
- Candidate OTP events captured in Module 05 may be cross-referenced but not duplicated here except role changes affecting candidate permissions
- Authorization denial events include resource type and denial reason code
- Retention period configurable by administrator policy

##### Validations

- Date range end must be after start
- Export row limit enforced to prevent unbounded extracts
- Audit viewer must hold audit-read permission

##### Calculations

- Event count aggregates by type for filtered result set

##### Workflow

EVENT_OCCURRED → RECORD_APPENDED → REGISTER_VIEWED → DETAIL_INSPECTED → EXPORTED

##### Search requirements

- Search audit narrative text
- Filter by event category identity login permission authorization
- Filter by affected user
- Filter by performing administrator

##### Documents

- Exported audit extract for compliance review

##### Reports

- Failed login and authorization denial summary report

##### Notifications

- Optional alert on threshold of authorization denials per hour

##### Security

- Audit register read access restricted to privileged administrators
- Tamper-evident append-only storage model
- Sensitive password values never logged

##### Integrations

- Ingest authorization denial events from F01-012 hooks

##### Dependencies

- F01-005 Staff Password Authentication and Login Session
- F01-006 Examination Administrator User Register and Account Lifecycle
- F01-007 Centre Invigilator User Register Centre Binding and Lifecycle
- F01-008 Role and Permission Matrix Administration
- F01-012 Downstream Module Actor Authorization Integration Hooks

##### Assumptions

- Platform server clock synchronised for trustworthy timestamps

##### Risks

- High event volume during examination days requires performant indexing

##### Non-functional requirements

- Audit write must not block primary user operation completion
- Register queries return within enterprise reporting thresholds for typical filters

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | User access audit register list with multi-field filters | Complex | 18 |
| UI | Audit event detail drawer with before and after values | Medium | 16 |
| UI | Audit register empty state for filter with no matches | Simple | 5 |
| UI | Audit export action with row limit confirmation dialog | Easy | 14 |
| UI | Security event summary tiles by event category | Medium | 16 |
| API | List and search audit events with filters | Complex | 8 |
| API | Retrieve single audit event detail payload | Easy | 4 |
| API | Append user lifecycle change audit event | Medium | 6 |
| API | Append staff login logout audit event | Medium | 6 |
| API | Append permission publish audit event | Medium | 6 |
| API | Append authorization denial audit event from hooks | Medium | 6 |
| API | Export filtered audit register slice | Medium | 6 |
| Database | Append-only audit event core storage | Medium | 0.3 |
| Database | Audit event indexes for date actor and event type queries | Complex | 0.5 |
| Testing | Happy path audit capture and filtered register retrieval | Medium | 0.3 |
| Testing | Invalid date range and unauthorized viewer rejection cases | Easy | 0.25 |
| Testing | High-volume append and export limit edge cases | Complex | 0.5 |
| Documentation | Audit register administrator runbook for compliance reviews | Medium | 0.3 |
| Documentation | Technical audit event taxonomy reference | Medium | 0.3 |

### F01-020 Downstream Module Actor Authorization Integration Hooks

85.35 hours · Go-live · 19 tasks

##### Description

Delivers reusable authorization integration hooks enabling downstream business modules to enforce actor-based access checks using resolved role, permission, and centre scope claims without re-implementing identity logic.

##### Business objective

Centralise authorization decisions so Modules 03 through 12 consistently honour platform roles and centre scoping rules.

##### Actors

- System
- Examination Administrator
- Examination Centre/Invigilator User

##### User journey

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

##### Functional capabilities

- Resolve authenticated actor identity from session context
- Load effective permission snapshot by role and version
- Evaluate single permission grant check for requested operation
- Evaluate centre scope check for invigilator resource access
- Return structured allow or deny authorization decision with reason code
- Emit authorization denial audit event when configured
- Expose permission snapshot cache with invalidation on publish
- Provide batch permission check for menu rendering use cases
- Document hook contract for downstream module integrators

##### Inputs

- Session token or actor context
- Requested permission code
- Resource centre identifier for scoped checks
- Optional batch permission code list

##### Outputs

- Authorization allow decision with claims
- Authorization deny decision with reason code
- Cached permission snapshot reference
- Denial audit event when enabled

##### Business rules

- All downstream modules must use hooks for staff and candidate permission enforcement
- Centre scope check mandatory when actor holds invigilator role
- Public verification endpoints use Verifier/Public policy not staff session hooks
- Snapshot version mismatch triggers cache refresh not silent allow

##### Validations

- Requested permission code must exist in master catalogue
- Missing session context returns unauthenticated denial
- Missing centre identifier on scoped operation returns scope denial
- Deactivated user always denied regardless of stale token

##### Calculations

- None

##### Workflow

HOOK_INVOKED → CLAIMS_RESOLVED → PERMISSION_EVALUATED → SCOPE_EVALUATED → ALLOWED or DENIED → AUDIT_OPTIONAL

##### Search requirements

- None

##### Documents

- Downstream integrator authorization hook guide

##### Reports

- Authorization denial counts by module and reason code

##### Notifications

- None directly; feeds audit alerts in F01-011

##### Security

- Deny-by-default when permission or scope cannot be confirmed
- Claims resolution rejects tampered session tokens
- Cache invalidation immediate on permission publish

##### Integrations

- Consumed by Module 03 centre management operations
- Consumed by Module 04 question bank administration
- Consumed by Module 05 candidate portal permission gating
- Consumed by Modules 06 through 12 protected operations

##### Dependencies

- F01-001 through F01-004 role permission catalogues
- F01-008 Role and Permission Matrix Administration for snapshot publish
- F01-011 User Access Audit Register for denial event ingestion

##### Assumptions

- Downstream modules pass stable permission codes agreed in integration catalogue
- Internal service call latency acceptable within request path

##### Risks

- Inconsistent hook adoption in a module creates authorization bypass gaps

##### Non-functional requirements

- Hook evaluation completes within low milliseconds for typical permission check
- Cache supports high read volume during examination days

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Authorization hook health status read-only panel for administrators | Simple | 5 |
| UI | Permission cache invalidation manual trigger button for break-glass | Simple | 5 |
| API | Resolve authenticated actor claims from session context | Complex | 8 |
| API | Load effective permission snapshot by role and version | Medium | 6 |
| API | Evaluate single permission grant authorization check | Complex | 8 |
| API | Evaluate centre scope authorization check for invigilator actors | Complex | 8 |
| API | Batch permission check for menu visibility rendering | Medium | 6 |
| API | Invalidate permission snapshot cache on matrix publish | Medium | 6 |
| API | Emit structured authorization denial audit payload | Medium | 6 |
| Database | Permission snapshot cache storage with version key | Medium | 0.3 |
| Database | Authorization denial counter aggregates by module | Easy | 0.25 |
| Integration | Internal authorization hook callable from Module 03 centre operations | Simple | 4 |
| Integration | Internal authorization hook callable from Module 05 candidate portal | Simple | 4 |
| Integration | Internal authorization hook callable from Modules 06 through 12 protected operations | Medium | 16 |
| Testing | Happy path allow decisions for administrator and scoped invigilator | Medium | 0.3 |
| Testing | Missing permission and cross-centre scope denial cases | Complex | 0.5 |
| Testing | Stale token deactivated user and cache invalidation edge cases | Very high | 1 |
| Documentation | Downstream module integrator authorization hook guide | Complex | 0.5 |
| Documentation | Technical permission code catalogue reference for module teams | Complex | 0.5 |

## 02 API Integration Hub

451.8 hours · 87 tasks · Platform

External system connectivity for KGID employee lookup and online examination fee payment processing.

### F02-001 KGID Government Employee Lookup Integration

66.7 hours · Go-live · 17 tasks

##### Description

Implements the technical integration layer that accepts a government employee KGID number, validates it, calls the external KGID system, maps returned employee attributes into a canonical employee-detail payload, persists an auditable lookup record, and exposes lookup outcomes (found, not found, unavailable) to downstream registration flows. Subject to API and data availability as stated in the source document.

##### Business objective

Automate retrieval of government department employee information during Type 1 registration without manual data entry, while preserving audit evidence and controlled failure behavior when the KGID service is unavailable.

##### Actors

- Examination Administrator
- System Integration Service
- Candidate Registration module consumer

##### User journey

1. Candidate Registration module receives a KGID number entered by a government department employee candidate during registration (presentation handled outside this feature).
2. System Integration Service validates KGID number format and normalizes input before any external call.
3. Service resolves active KGID integration configuration (endpoint, credentials, timeout, retry policy) from Integration Configuration administration.
4. Service authenticates to the external KGID API using configured credentials.
5. Service submits KGID lookup request with a generated correlation identifier.
6. On successful response, service maps available fields (employee name, KGID number, employee details) into the canonical employee-detail structure.
7. Service persists request metadata, response snapshot, outcome status, and correlation identifier for audit.
8. Service returns mapped employee details to the registration consumer for candidate confirmation (confirmation UI is outside this feature).
9. If KGID record is not found, service returns a structured not-found outcome without partial employee data.
10. If KGID API returns transient errors, service applies configured retry policy via the integration retry framework and either succeeds or returns service-unavailable after retry exhaustion.
11. If KGID API returns permanent errors (invalid credentials, authorization denied), service logs classified error, skips further retry, and returns a controlled failure outcome.
12. Examination Administrator may later review KGID lookup logs through Integration Observability when investigating registration failures.

##### Functional capabilities

- Accept KGID lookup requests from authorized internal registration consumers
- Validate KGID number format prior to external invocation
- Authenticate against configured KGID external API credentials
- Invoke external KGID lookup by KGID number
- Map external KGID response fields into canonical employee name, KGID number, and employee details structure
- Return structured found outcome with mapped employee attributes when data is available
- Return structured not-found outcome when KGID has no matching employee record
- Return structured service-unavailable outcome when external API is down or retry is exhausted
- Persist auditable KGID lookup request and response snapshot with correlation identifier
- Emit integration call records to shared logging and retry framework
- Apply KGID-specific timeout and retry binding using shared retry policy engine

##### Inputs

- KGID number
- Registration correlation or session reference from consuming module
- Active KGID integration configuration profile
- Encrypted KGID API credentials
- Retry and timeout policy parameters

##### Outputs

- Canonical employee detail payload (employee name, KGID number, employee details when available)
- Structured not-found outcome
- Structured service-unavailable outcome
- Structured permanent integration failure outcome
- KGID lookup audit record with correlation identifier
- Integration call log entry with timing and classified error

##### Business rules

- KGID lookup is mandatory input path for government department employee registration flows; this feature does not determine registration eligibility
- Only fields returned by the external KGID API and mapped by configuration shall be included; missing fields are omitted rather than invented
- Retrieved information availability is subject to external API and data availability as stated in the source document
- Lookup outcomes must be auditable and traceable by correlation identifier
- External KGID credentials must never be returned to registration consumers or written unredacted to operational logs
- Not-found and unavailable outcomes must be distinguishable for downstream registration handling

##### Validations

- KGID number must be present and non-blank
- KGID number must match approved format pattern before external call
- KGID number length must fall within configured minimum and maximum bounds
- KGID number must not contain disallowed characters after normalization
- Integration configuration for KGID type must be active before lookup is attempted
- External response must contain minimum identifiable employee reference before mapped as found
- Mapped employee name must not be empty when found outcome is returned
- Duplicate concurrent lookup for same KGID within same correlation context must reuse or reject per idempotency rule without duplicate external calls

##### Calculations

- None; this feature performs retrieval and mapping only and does not compute registration fees or attempt history

##### Workflow

States: LOOKUP_REQUESTED → FORMAT_VALIDATED → CONFIG_RESOLVED → EXTERNAL_CALL_IN_PROGRESS → (MAPPING_COMPLETED | NOT_FOUND | TRANSIENT_ERROR | PERMANENT_ERROR | SERVICE_UNAVAILABLE). Transitions: LOOKUP_REQUESTED to FORMAT_VALIDATED on successful field validation; FORMAT_VALIDATED to CONFIG_RESOLVED when active KGID profile loaded; CONFIG_RESOLVED to EXTERNAL_CALL_IN_PROGRESS on authenticated outbound call; EXTERNAL_CALL_IN_PROGRESS to MAPPING_COMPLETED when employee record returned and mapped; EXTERNAL_CALL_IN_PROGRESS to NOT_FOUND when external system reports no record; EXTERNAL_CALL_IN_PROGRESS to TRANSIENT_ERROR on timeout or retryable HTTP or gateway fault; TRANSIENT_ERROR to EXTERNAL_CALL_IN_PROGRESS on retry attempt; TRANSIENT_ERROR to SERVICE_UNAVAILABLE when retry maximum exceeded; EXTERNAL_CALL_IN_PROGRESS to PERMANENT_ERROR on authentication or authorization failure; MAPPING_COMPLETED, NOT_FOUND, PERMANENT_ERROR, and SERVICE_UNAVAILABLE to AUDIT_PERSISTED on log write completion.

##### Search requirements

- Examination Administrator search of KGID lookup audit records by KGID number, correlation identifier, outcome status, and date range via Integration Observability feature

##### Documents

- KGID integration technical specification for developers
- Operations runbook for KGID API outage handling

##### Reports

- None within this feature; operational review uses integration call log register from F02-004

##### Notifications

- None; registration module handles candidate-facing messaging

##### Security

- KGID credentials retrieved only from encrypted credential store at runtime
- Internal lookup operations restricted to authorized registration service identities
- Response snapshots stored with field-level redaction policy for sensitive attributes if present in external payload
- All lookup attempts logged with actor or service identity and correlation identifier

##### Integrations

- External KGID government employee information API

##### Dependencies

- F01 Platform Role and Permission Catalog for Examination Administrator access to related configuration and logs
- F01 Staff Authentication Session and Credential Policy for administrator sessions
- F02-003 Integration Endpoint and Credential Administration for KGID endpoint and credential profiles
- F02-004 Integration Retry Logging and Error Observability for retry execution and call logging
- Module 05 Candidate Registration consumes lookup outcomes; registration confirmation UI is out of scope for this feature

##### Assumptions

- External KGID API exposes authenticated lookup by KGID number with employee name and employee details fields or equivalents mappable to canonical structure
- KGID API availability and field completeness may vary; partial payloads are handled without failing entire registration integration contract
- Network egress to KGID endpoints is permitted from application runtime environment
- Canonical employee detail schema is agreed with Candidate Registration module consumers before go-live

##### Risks

- KGID API downtime blocks automated employee verification for government department candidates
- External schema changes may require mapping updates
- Incomplete external data may limit auto-population despite successful lookup

##### Non-functional requirements

- Lookup operations must complete within configured timeout with retry for transient failures
- Audit records retained per enterprise retention policy
- Integration must support concurrent lookup volume during registration peaks
- Structured error codes suitable for downstream registration UX handling

##### Notes

Provides backend KGID connectivity consumed by Candidate Registration; does not include registration UI or fee logic.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| Integration | Authenticate with external KGID API using configured credentials | Medium | 16 |
| Integration | Fetch government employee record by KGID number from external KGID API | Easy | 8 |
| Integration | Map external KGID response fields to canonical employee detail structure | Medium | 16 |
| Integration | KGID-specific timeout and retry policy binding to shared retry engine | Simple | 4 |
| API | Lookup government employee by KGID number for registration consumers | Medium | 6 |
| API | Validate KGID number format before external lookup invocation | Easy | 4 |
| API | Return structured not-found outcome when KGID has no employee record | Easy | 4 |
| API | Return structured service-unavailable outcome when KGID API is unreachable after retry | Medium | 6 |
| Database | KGID lookup transaction log with correlation identifier and outcome status | Easy | 0.25 |
| Database | KGID lookup response snapshot storage for audit review | Medium | 0.3 |
| Testing | Successful employee retrieval with all available mapped fields | Medium | 0.3 |
| Testing | KGID not found in external system response handling | Easy | 0.25 |
| Testing | Malformed and out-of-pattern KGID number rejection | Easy | 0.25 |
| Testing | External API timeout with retry exhaustion to service-unavailable | Complex | 0.5 |
| Testing | KGID API authentication and authorization failure without retry | Medium | 0.3 |
| Documentation | KGID integration technical specification for developers | Medium | 0.3 |
| Documentation | Operations runbook for KGID API outage and recovery | Easy | 0.25 |

### F02-002 Payment Gateway Fee Transaction Integration

120.1 hours · Go-live · 23 tasks

##### Description

Implements payment gateway connectivity for online examination fee processing including payment session initiation, capture of gateway transaction references, asynchronous success and failure callback processing with signature verification, payment status retrieval, idempotent callback handling, and auditable payment transaction persistence for registration flows where payment is mandatory.

##### Business objective

Enable secure, traceable online examination fee collection through an external payment gateway with reliable status synchronization so registration can complete only after confirmed successful payment where applicable.

##### Actors

- Examination Administrator
- System Integration Service
- Candidate Registration module consumer
- External payment gateway

##### User journey

1. Candidate Registration module determines that payment is mandatory and supplies payable amount and registration payment reference to this integration (fee rules are outside this feature).
2. System Integration Service validates payment initiation input including positive amount and registration reference presence.
3. Service loads active payment gateway configuration and decrypts credentials.
4. Service authenticates with payment gateway and creates payment initiation request.
5. Service receives gateway session or redirect payload including gateway transaction reference.
6. Service persists payment transaction record in initiated state with internal reference and gateway transaction reference.
7. Candidate completes payment on gateway channel (gateway-hosted flow; presentation outside this feature).
8. Payment gateway posts asynchronous status callback to integration callback endpoint.
9. Service verifies callback authenticity using gateway signature or shared secret rules.
10. Service classifies callback as success or failure and locates matching initiated transaction by gateway reference.
11. On success callback, service transitions transaction to successful state, captures final gateway transaction reference and timestamp, and notifies registration consumer.
12. On failure callback, service transitions transaction to failed state with failure reason code and notifies registration consumer.
13. If callback is delayed, registration consumer may request current payment status by internal reference; service queries gateway status endpoint when supported and reconciles local state.
14. Duplicate success callbacks for the same gateway reference are processed idempotently without duplicate financial completion signals.
15. Examination Administrator reviews payment integration logs and transaction audit via observability and configuration features when resolving reconciliation issues.

##### Functional capabilities

- Initiate examination fee payment session with external payment gateway
- Persist internal payment transaction with initiated status and registration reference
- Capture gateway transaction reference at initiation
- Receive asynchronous payment gateway status callbacks
- Verify payment callback authenticity signature or checksum
- Transition payment transaction to successful state on verified success callback
- Transition payment transaction to failed state on verified failure callback
- Retrieve payment transaction status by internal registration payment reference
- Query payment gateway for current status when callback is delayed
- Enforce idempotent processing for duplicate callbacks sharing the same gateway transaction reference
- Persist callback event history for each payment transaction
- Return structured outcomes for initiation failure, callback rejection, and unknown transaction reference

##### Inputs

- Registration payment reference from Candidate Registration module
- Payable fee amount
- Candidate redirect return URLs supplied by registration consumer
- Active payment gateway integration configuration
- Encrypted payment gateway credentials
- Gateway callback payload with transaction reference and status
- Gateway callback signature or authentication headers

##### Outputs

- Payment initiation payload for candidate redirect or gateway session
- Internal payment transaction identifier
- Gateway transaction reference
- Payment status outcome (initiated, successful, failed, unknown)
- Callback event audit entries
- Structured reconciliation detail for registration confirmation storage

##### Business rules

- Registration completion after payment is enforced by Candidate Registration; this feature supplies authoritative payment status only
- Payment transaction reference and gateway transaction reference must be captured for successful payments
- Failed payment must not mark transaction as successful
- Duplicate success callbacks must not create duplicate successful financial completion events
- Payment amount at initiation must match amount supplied by registration consumer; this feature does not calculate applicable fee
- All callback processing must occur only after signature or authenticity verification passes
- Transaction state transitions must be monotonic: initiated to successful or initiated to failed; successful cannot revert to failed without manual administrative intervention outside automated callback flow

##### Validations

- Registration payment reference must be present
- Payable amount must be greater than zero for chargeable registrations
- Payable amount must not exceed configured maximum single-transaction limit
- Payment gateway configuration must be active before initiation
- Callback payload must include gateway transaction reference
- Callback signature must match gateway verification rules
- Callback referencing unknown gateway transaction reference must be rejected and logged
- Callback amount must match persisted initiated transaction amount when amount is present in callback
- Callback currency must match configured gateway currency when currency is present
- Status query request must include valid internal payment transaction reference

##### Calculations

- None; payable amount is supplied by Candidate Registration module

##### Workflow

States: PAYMENT_INITIATED → (PAYMENT_SUCCESSFUL | PAYMENT_FAILED | PAYMENT_UNKNOWN). Transitions: PAYMENT_INITIATED created on successful gateway session creation; PAYMENT_INITIATED to PAYMENT_SUCCESSFUL on verified success callback or reconciled success status query; PAYMENT_INITIATED to PAYMENT_FAILED on verified failure callback or reconciled failure status query; PAYMENT_INITIATED remains PAYMENT_UNKNOWN when callback not yet received and status query inconclusive; duplicate success callback while already PAYMENT_SUCCESSFUL transitions to IDEMPOTENT_NOOP with audit entry only.

##### Search requirements

- Examination Administrator search of payment transactions by internal reference, gateway transaction reference, status, and date range through integration logs and transaction audit views

##### Documents

- Payment gateway integration technical notes
- Finance reconciliation runbook for examination fee transactions

##### Reports

- None dedicated; reconciliation uses persisted transaction and callback history accessible to administrators

##### Notifications

- None within this feature; Candidate Registration and Notification Service handle candidate-facing payment confirmations

##### Security

- Payment gateway credentials stored encrypted and never logged in plaintext
- Callback endpoint protected against replay using signature verification and idempotency keys
- Internal status APIs restricted to authorized registration service identities
- PCI-sensitive card data never stored; gateway-hosted collection assumed

##### Integrations

- External online payment gateway for fee initiation
- External payment gateway asynchronous status callback channel
- External payment gateway transaction status query when supported by provider

##### Dependencies

- F01 Platform Role and Permission Catalog for administrator access to related logs and configuration
- F01 Staff Authentication Session and Credential Policy
- F02-003 Integration Endpoint and Credential Administration for payment gateway profiles
- F02-004 Integration Retry Logging and Error Observability for initiation and status query logging
- Module 05 Candidate Registration supplies payable amount and consumes payment outcomes; fee rule determination and attempt history are out of scope

##### Assumptions

- Selected payment gateway supports server-to-server initiation and asynchronous callback notification
- Gateway provides verifiable callback signature mechanism
- Registration module persists payment details only after receiving successful status from this integration
- Single currency configuration per examination fee payment context

##### Risks

- Delayed or lost callbacks may leave transactions in unknown state until status query reconciliation
- Gateway schema or signature rule changes require urgent mapping updates
- Duplicate or out-of-order callbacks may cause reconciliation complexity without strict idempotency

##### Non-functional requirements

- Callback processing must be durable and idempotent under at-least-once delivery
- Initiation and callback handling must support registration peak load
- End-to-end audit trail linking registration reference, internal transaction id, and gateway reference
- Configurable timeout for status query reconciliation

##### Notes

Covers fee payment initiation, asynchronous status callback, and transaction reference capture; fee amount determination remains in Candidate Registration.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| Integration | Authenticate with payment gateway for transaction session creation | Medium | 16 |
| Integration | Initiate examination fee payment transaction with external payment gateway | Medium | 16 |
| Integration | Parse payment gateway success callback payload fields | Medium | 16 |
| Integration | Parse payment gateway failure callback payload fields | Easy | 8 |
| Integration | Verify payment gateway callback authenticity signature | Medium | 16 |
| Integration | Query payment status by gateway transaction reference | Easy | 8 |
| API | Create payment initiation request with registration reference and amount | Complex | 8 |
| API | Receive asynchronous payment status callback from gateway | Complex | 8 |
| API | Retrieve payment transaction status by internal registration payment reference | Medium | 6 |
| API | Persist gateway transaction reference on successful initiation response | Easy | 4 |
| API | Mark payment transaction failed from verified gateway failure callback | Easy | 4 |
| API | Mark payment transaction successful from verified gateway success callback | Medium | 6 |
| Database | Payment transaction core entity with status and reference fields | Medium | 0.3 |
| Database | Payment callback event history for idempotent callback processing | Medium | 0.3 |
| Database | Unique constraints on gateway transaction reference | Complex | 0.5 |
| Testing | Successful payment initiation followed by verified success callback | Complex | 0.5 |
| Testing | Payment initiation input validation for missing reference and invalid amount | Medium | 0.3 |
| Testing | Verified failure callback transitions transaction to failed state | Medium | 0.3 |
| Testing | Duplicate success callback idempotency without duplicate completion signal | Complex | 0.5 |
| Testing | Invalid or tampered callback signature rejection | Complex | 0.5 |
| Testing | Delayed callback reconciliation via status query endpoint | Medium | 0.3 |
| Documentation | Payment gateway integration technical notes for developers | Medium | 0.3 |
| Documentation | Finance reconciliation runbook for examination administrators | Medium | 0.3 |

### F02-003 Integration Endpoint and Credential Administration

175 hours · Go-live · 28 tasks

##### Description

Provides Examination Administrator capabilities to configure, update, and test KGID and payment gateway integration profiles including endpoint URLs, timeout and retry parameters, active status, and encrypted credential storage with rotation support and configuration change audit.

##### Business objective

Allow authorized administrators to manage external integration connectivity settings securely without code deployments, enabling environment-specific endpoints and credential lifecycle control for KGID lookup and fee payment flows.

##### Actors

- Examination Administrator

##### User journey

1. Examination Administrator signs in through staff authentication governed by User and Role Management.
2. Administrator opens Integration Configuration register listing KGID and payment gateway profiles with active or inactive status.
3. If no profiles exist, administrator sees empty state guidance to create first integration profile.
4. Administrator selects KGID profile to create or edit endpoint URL, timeout seconds, retry attempt limit, and active flag.
5. Administrator enters or rotates KGID API credentials in masked credential form and confirms rotation in confirmation dialog.
6. Administrator saves KGID configuration; system validates URL format and numeric timeout bounds and persists encrypted credentials.
7. Administrator runs KGID connection test; system displays success or structured failure message in connection test result dialog.
8. Administrator selects payment gateway profile to create or edit initiation URL, callback path identifier, status query URL if applicable, timeout, and active flag.
9. Administrator enters or rotates payment gateway merchant credentials and callback signing secret in masked form.
10. Administrator saves payment gateway configuration with field-level validation errors shown inline on failure.
11. Administrator runs payment gateway connection test; system displays test outcome dialog.
12. Each save or credential rotation writes configuration change audit entry with administrator identity and timestamp.
13. Administrator returns to register to verify updated status chips and last-tested timestamp if displayed.

##### Functional capabilities

- List integration configuration profiles by integration type and active status
- Display empty state when no integration profiles are configured
- Create KGID integration endpoint configuration profile
- Update KGID integration endpoint configuration profile
- Create payment gateway integration endpoint configuration profile
- Update payment gateway integration endpoint configuration profile
- Store integration credentials encrypted at rest
- Rotate integration credentials without exposing prior secret values in UI
- Execute live connectivity test against KGID endpoint using stored credentials
- Execute live connectivity test against payment gateway endpoint using stored credentials
- Record configuration change audit trail for create, update, and credential rotation events
- Restrict configuration management to authorized Examination Administrator roles

##### Inputs

- KGID endpoint URL
- KGID API key or client credentials
- KGID timeout seconds
- KGID retry attempt limit
- Payment gateway initiation endpoint URL
- Payment gateway status query endpoint URL
- Payment gateway merchant identifier and secret
- Payment gateway callback signing secret
- Payment gateway timeout seconds
- Active or inactive status flag per profile

##### Outputs

- Saved integration configuration profiles
- Masked credential metadata showing rotation timestamp without secret exposure
- Connection test success or failure result messages
- Configuration change audit records
- Validation error messages for invalid URLs and out-of-range timeout values

##### Business rules

- Only one active KGID profile and one active payment gateway profile may be designated per environment unless explicitly configured otherwise
- Credential values must never be returned in full after initial save; UI shows masked placeholders only
- Deactivating a profile prevents new lookup or payment initiation calls from using that profile
- Configuration changes must be auditable with administrator identity
- Connection test must not mutate production financial state for payment gateway beyond provider-permitted ping or token exchange

##### Validations

- Endpoint URL must be valid HTTPS URL format
- Timeout seconds must be positive integer within configured maximum
- Retry attempt limit must be non-negative integer within configured maximum
- KGID credentials must be provided on create and on rotation
- Payment gateway merchant identifier must be non-blank
- Payment gateway secret must be provided on create and on rotation
- Callback signing secret must meet minimum length requirement
- Active flag must be boolean
- Duplicate integration type profile name must be rejected if name uniqueness is enforced
- Administrator must hold integration configuration permission to save or rotate credentials

##### Calculations

- None

##### Workflow

Configuration states: DRAFT → ACTIVE → INACTIVE. Transitions: DRAFT to ACTIVE when administrator activates saved valid profile; ACTIVE to INACTIVE when administrator deactivates profile; INACTIVE to ACTIVE on reactivation after validation; credential rotation while ACTIVE creates new credential version then retires prior version on successful save.

##### Search requirements

- Filter integration configuration register by integration type (KGID, payment gateway)
- Filter by active or inactive status
- Sort by last updated timestamp

##### Documents

- Administrator guide for integration setup and activation
- Credential rotation and security procedures for examination administrators

##### Reports

- Configuration change audit listing exportable for compliance review

##### Notifications

- Optional in-application success or failure toast on save and connection test; no candidate notifications

##### Security

- Role-based access limited to Examination Administrator with integration configuration permission
- Credentials encrypted at rest with environment-specific encryption keys
- Connection test responses scrubbed of sensitive tokens before display
- Audit log captures administrator user identifier for every mutation

##### Integrations

- External KGID API for administrator-initiated connectivity test
- External payment gateway for administrator-initiated connectivity test

##### Dependencies

- F01 Platform Role and Permission Catalog defining Examination Administrator integration configuration permissions
- F01 Examination Administrator Account Lifecycle for administrator identities
- F01 Staff Authentication Session and Credential Policy
- F01 Downstream Module Authorization Integration Hooks for permission enforcement on configuration APIs
- F02-001 KGID Government Employee Lookup Integration consumes KGID profiles
- F02-002 Payment Gateway Fee Transaction Integration consumes payment gateway profiles

##### Assumptions

- Examination Administrator role from Module 01 includes distinct permission for integration configuration separate from registration operations
- Encryption key management is provided by platform infrastructure
- Payment gateway provider exposes a non-financial connectivity or token test operation suitable for administrator test action

##### Risks

- Misconfigured endpoints or expired credentials cause registration KGID lookup or payment outages
- Credential rotation errors may invalidate in-flight payment sessions if coordinated downtime is not observed

##### Non-functional requirements

- Configuration changes effective for new integration calls without application restart
- Save and test operations complete within administrator-acceptable interactive latency
- Audit records immutable after creation

##### Notes

Administrator-facing configuration for KGID and payment gateway connectivity; excludes registration business parameters.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Integration configuration register list with type and status filters | Medium | 16 |
| UI | Empty state when no integration profiles exist | Simple | 5 |
| UI | KGID integration endpoint configuration form | Medium | 16 |
| UI | Payment gateway integration endpoint configuration form | Medium | 16 |
| UI | Credential entry form with masked secret fields | Medium | 16 |
| UI | Credential rotation confirmation dialog | Simple | 5 |
| UI | KGID connection test result dialog | Easy | 14 |
| UI | Payment gateway connection test result dialog | Easy | 14 |
| UI | Configuration save validation error state on forms | Easy | 14 |
| API | List integration configuration profiles | Easy | 4 |
| API | Retrieve KGID integration configuration detail | Easy | 4 |
| API | Retrieve payment gateway integration configuration detail | Easy | 4 |
| API | Create KGID integration configuration profile | Medium | 6 |
| API | Update KGID integration configuration profile | Medium | 6 |
| API | Create payment gateway integration configuration profile | Medium | 6 |
| API | Update payment gateway integration configuration profile | Medium | 6 |
| API | Store and rotate encrypted integration credentials | Complex | 8 |
| API | Execute connectivity test against KGID endpoint | Medium | 6 |
| API | Execute connectivity test against payment gateway endpoint | Medium | 6 |
| Database | Integration configuration profile entity | Easy | 0.25 |
| Database | Encrypted credential blob storage per integration profile | Complex | 0.5 |
| Database | Integration configuration change audit trail | Medium | 0.3 |
| Testing | Examination Administrator authorized access to configuration save operations | Medium | 0.3 |
| Testing | Unauthorized role blocked from credential rotation | Medium | 0.3 |
| Testing | Invalid HTTPS URL and out-of-range timeout validation rejection | Easy | 0.25 |
| Testing | Credential encryption at rest and masked API responses | Complex | 0.5 |
| Documentation | Administrator guide for KGID and payment gateway setup | Medium | 0.3 |
| Documentation | Credential rotation and security procedures for administrators | Medium | 0.3 |

### F02-004 Integration Retry Logging and Error Observability

90 hours · Go-live · 19 tasks

##### Description

Delivers shared integration observability and resilience capabilities including structured call logging with correlation identifiers, transient versus permanent error classification, configurable retry execution for registration and payment integration calls, administrator log register with detail view and export, and sensitive field redaction suitable for production troubleshooting.

##### Business objective

Ensure KGID and payment integrations operate reliably under failure conditions with auditable evidence and administrator visibility into errors, retries, and outcomes without exposing secrets.

##### Actors

- Examination Administrator
- System Integration Service

##### User journey

1. System Integration Service initiates any KGID lookup or payment gateway call and assigns correlation identifier propagated from registration context where supplied.
2. Service records call attempt with integration type, endpoint, start time, and requesting service identity.
3. On transient failure such as timeout or gateway error, service classifies error as transient and schedules retry according to active profile retry limit.
4. Each retry attempt appends retry history linked to parent call with attempt number and outcome.
5. On permanent failure such as authentication rejection, service classifies error as permanent, skips further retry, and marks call failed.
6. On success, service records completion timing and outcome status with redacted request and response payload excerpts.
7. Examination Administrator opens Integration Call Log register filtered by date range, integration type, outcome status, and correlation identifier fragment.
8. Administrator selects a log row to open read-only detail view showing attempt timeline, error classification, and redacted payload excerpts.
9. If no logs match filters, administrator sees empty state message.
10. Administrator exports filtered log result set to file for incident analysis or audit request.
11. Administrator uses log evidence to coordinate credential rotation or endpoint correction in Integration Configuration administration.

##### Functional capabilities

- Record integration call attempt with correlation identifier and integration type
- Append retry attempt history records linked to parent integration call
- Classify integration errors as transient or permanent
- Execute retry policy for transient errors until success or retry limit exceeded
- Skip retry for permanent errors
- Redact credentials and secrets from persisted log payloads
- List integration call logs with date, type, status, and correlation filters
- Retrieve integration call log detail with attempt timeline
- Export filtered integration call logs for administrator download
- Restrict log register and export to authorized Examination Administrator roles

##### Inputs

- Integration type (KGID lookup or payment gateway operation)
- Correlation identifier from consuming flow
- Request metadata and redacted payload excerpts
- HTTP or gateway status codes and error messages
- Retry policy parameters from integration configuration profile
- Administrator filter criteria for log register

##### Outputs

- Integration call log entries with outcome status
- Retry attempt history records
- Error classification label per failed attempt
- Administrator log register rows
- Exported log file for filtered result set
- Structured permanent versus transient failure signals to calling integration features

##### Business rules

- Every external KGID and payment gateway call must produce a log record regardless of outcome
- Retry attempts must not exceed configured maximum for the active integration profile
- Permanent errors must never trigger automatic retry
- Secrets, API keys, and card-related data must be redacted before persistence
- Log export must respect same authorization scope as log register viewing
- Correlation identifier must be preserved across retry attempts for a single logical operation

##### Validations

- Correlation identifier must be non-blank when supplied by consumer
- Integration type must be one of supported values (KGID, payment gateway)
- Retry attempt number must increment monotonically per parent call
- Log list date-from must be before or equal to date-to
- Export row limit must not exceed configured maximum export size
- Administrator must hold integration observability permission to access log detail and export

##### Calculations

- Retry remaining attempts equals configured retry limit minus completed retry count

##### Workflow

Call lifecycle states: CALL_STARTED → (CALL_SUCCEEDED | RETRY_SCHEDULED | CALL_FAILED_PERMANENT | CALL_FAILED_EXHAUSTED). Transitions: CALL_STARTED to CALL_SUCCEEDED on successful external response; CALL_STARTED to RETRY_SCHEDULED on transient error when retries remain; RETRY_SCHEDULED to CALL_STARTED on next attempt execution; RETRY_SCHEDULED to CALL_FAILED_EXHAUSTED when retry limit reached; CALL_STARTED to CALL_FAILED_PERMANENT on permanent error classification without entering RETRY_SCHEDULED.

##### Search requirements

- Search integration call logs by correlation identifier partial match
- Filter by integration type KGID or payment gateway
- Filter by outcome status success, failed permanent, failed exhausted, or in progress
- Filter by date and time range
- Sort by call start time descending

##### Documents

- Integration troubleshooting guide for support staff
- Retry policy configuration technical notes for implementers

##### Reports

- Exported integration call log file for incident and audit analysis

##### Notifications

- None; administrators proactively review logs during incidents

##### Security

- Log access restricted to Examination Administrator with observability permission
- Automatic redaction of credential and PCI-related fields in stored payloads
- Export files exclude redacted secret placeholders replaced with non-reversible tokens only

##### Integrations

- Internal consumption by F02-001 KGID lookup calls
- Internal consumption by F02-002 payment gateway initiation, callback, and status query calls

##### Dependencies

- F01 Platform Role and Permission Catalog for observability permission
- F01 Staff Authentication Session and Credential Policy
- F02-003 Integration Endpoint and Credential Administration for retry limit and timeout parameters
- F02-001 KGID Government Employee Lookup Integration emits and consumes logging and retry behavior
- F02-002 Payment Gateway Fee Transaction Integration emits and consumes logging and retry behavior

##### Assumptions

- Registration and payment flows propagate correlation identifiers suitable for cross-module tracing
- Log retention period aligns with enterprise audit policy configured at platform level
- Export format is standard delimited or spreadsheet format acceptable to administrators

##### Risks

- High registration volume may produce large log volume requiring archival strategy outside this feature
- Incorrect transient classification may cause unnecessary load on failing external systems
- Insufficient redaction rules may expose secrets if gateway payloads change format

##### Non-functional requirements

- Logging must not materially block integration call completion path
- Log register queries must remain responsive for typical administrator filter combinations
- Retry scheduling must be safe under concurrent calls sharing similar failure windows

##### Notes

Shared cross-cutting capability supporting KGID lookup and payment gateway flows with administrator log review.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Integration call log register with date, type, and status filters | Medium | 16 |
| UI | Integration call log detail read-only view with redacted payloads | Medium | 16 |
| UI | Integration log register empty state for no matching records | Simple | 5 |
| UI | Export integration call logs download action | Easy | 14 |
| API | List integration call logs with search and filter parameters | Medium | 6 |
| API | Retrieve integration call log detail by correlation identifier | Easy | 4 |
| API | Export filtered integration call logs to downloadable file | Medium | 6 |
| API | Record integration call attempt with timing and outcome | Medium | 6 |
| API | Execute retry policy for classified transient integration errors | Complex | 8 |
| API | Classify integration errors as transient versus permanent | Medium | 6 |
| Database | Integration call log entity with correlation identifier | Medium | 0.3 |
| Database | Per-attempt retry history linked to parent integration call | Easy | 0.25 |
| Testing | Successful call logging with correlation identifier propagation across retries | Medium | 0.3 |
| Testing | Retry stops after configured maximum attempts with exhausted outcome | Complex | 0.5 |
| Testing | Permanent error classification skips retry scheduling | Medium | 0.3 |
| Testing | Sensitive credential redaction in stored log payloads | Complex | 0.5 |
| Testing | Unauthorized user blocked from log register and export | Medium | 0.3 |
| Documentation | Integration troubleshooting guide for support staff | Medium | 0.3 |
| Documentation | Retry policy configuration technical notes for implementers | Easy | 0.25 |

## 03 Examination Centre Management

904.85 hours · 177 tasks · Business

Master management of authorised examination centres, capacity, centre users, and centre-level access configuration.

### F03-006 Authorised Examination Centre Register and Search

90.7 hours · Go-live · 18 tasks

##### Description

Provides Examination Administrators with a searchable register of all authorised examination centres showing centre identifier, name, location, approved capacity, active status, and bound invigilator count so only configured centres are visible for downstream scheduling and preference selection.

##### Business objective

Maintain a single authoritative list of department-approved examination centres and enable administrators to locate centres quickly by identifier, name, district, or operational status.

##### Actors

- Examination Administrator

##### User journey

1. Examination Administrator opens Examination Centre Management from the administration menu.
2. System displays the authorised centre register with default sort by centre name.
3. Administrator enters search text matching centre ID, centre name, or city.
4. Administrator applies status filter (Active, Inactive, All).
5. Administrator applies district or region filter when configured.
6. System refreshes the grid with matching centres and total record count.
7. Administrator clicks a centre row to open the centre detail read-only summary panel.
8. Administrator uses pagination to browse additional pages.
9. Administrator clears filters to return to the full register.
10. Administrator navigates to Add Centre or Edit Centre actions from register row actions.

##### Functional capabilities

- Display paginated authorised centre register with centre ID, name, address summary, approved capacity, active flag, and last modified timestamp
- Search centres by centre ID partial match, centre name, and city or district
- Filter register by active, inactive, or all status
- Filter register by district or region when master data exists
- Open read-only centre summary panel from register row selection
- Expose register row actions for edit, activate/deactivate, and child configuration shortcuts
- Restrict register access to Examination Administrator role
- Exclude inactive centres from downstream scheduling picklists while retaining register visibility

##### Inputs

- Search text
- Status filter value
- District or region filter
- Page number and page size
- Sort column and direction

##### Outputs

- Paginated centre register rows
- Total matching record count
- Read-only centre summary panel data
- Empty-state message when no centres match

##### Business rules

- Only Examination Administrators may view the full centre register
- Inactive centres remain visible in the register but are flagged and excluded from active scheduling picklists
- Centre ID must be displayed on every register row and is immutable after creation
- Register defaults to active centres first when no filter is applied

##### Validations

- Reject unauthenticated access to the register
- Reject page size values outside configured maximum
- Sanitise search text to prevent injection in search parameters
- Return empty result set without error when no centres match filters

##### Calculations

- Compute total matching centre count for pagination footer

##### Workflow

REGISTER_VIEWED → FILTER_APPLIED → RESULTS_DISPLAYED → ROW_SELECTED → SUMMARY_VIEWED

##### Search requirements

- Partial match on centre ID
- Partial match on centre name
- Partial match on city or district
- Exact match on active or inactive status

##### Security

- Role-gated access for Examination Administrator only
- Audit log entry when register export is invoked if export is enabled

##### Integrations

- Read centre master records from MySQL as source of truth

##### Dependencies

- F01-002 Examination Administrator Role and Organisation-Wide Permissions
- F01-005 Staff Password Authentication and Login Session

##### Assumptions

- District or region master exists or is optional text filter
- Centre register volume is moderate and server-side pagination is sufficient

##### Risks

- Large centre volumes may require additional index tuning for search responsiveness

##### Non-functional requirements

- Register search response within acceptable admin UI latency
- Accessible table headers and filter controls

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Authorised centre register list with centre ID, name, address summary, capacity, and status chips | Medium | 16 |
| UI | Centre register search bar with ID, name, and city partial match | Easy | 14 |
| UI | Centre register status filter control for active, inactive, and all | Simple | 5 |
| UI | Centre register district or region filter dropdown | Easy | 14 |
| UI | Centre register empty state when no centres match filters | Simple | 5 |
| UI | Read-only centre summary side panel opened from register row | Easy | 14 |
| UI | Centre register pagination footer with total count | Simple | 5 |
| API | List authorised centres with pagination defaults | Easy | 4 |
| API | Search authorised centres by ID, name, city, and district | Medium | 6 |
| API | Filter authorised centres by active or inactive status | Easy | 4 |
| API | Fetch single centre summary for register row detail panel | Simple | 2 |
| Database | Authorised examination centre core entity persistence | Medium | 0.3 |
| Database | Search indexes on centre ID, name, city, and active flag | Easy | 0.25 |
| Testing | Register list, search, and filter happy-path scenarios | Medium | 0.3 |
| Testing | Unauthorized role rejection for centre register access | Easy | 0.25 |
| Testing | Empty search result and invalid pagination parameter handling | Easy | 0.25 |
| Documentation | Administrator runbook for centre register search and filters | Easy | 0.25 |
| Documentation | Technical notes for centre register query and indexing | Simple | 0.1 |

### F03-007 Add Authorised Examination Centre Profile

70.95 hours · Go-live · 16 tasks

##### Description

Allows Examination Administrators to onboard a new authorised examination centre by capturing unique centre ID, centre name, full address, contact details, and initial active status as the foundation profile required by §18.1 centre-based examination access configuration.

##### Business objective

Enable controlled creation of new department-approved examination centres with unique identifiers before capacity, infrastructure, user binding, and restriction configuration.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Add Examination Centre from the centre register.
2. System presents the add centre form with mandatory centre ID and name fields.
3. Administrator enters unique centre ID following department format rules.
4. Administrator enters centre display name.
5. Administrator enters address line, city, district, state, and PIN code.
6. Administrator enters optional contact phone and email for centre coordination.
7. Administrator selects initial status as Active or Inactive.
8. System validates uniqueness of centre ID and mandatory address fields.
9. Administrator submits the form.
10. System persists the centre profile and displays success confirmation with centre ID.
11. System redirects administrator to centre detail or offers shortcuts to capacity and restriction configuration.

##### Functional capabilities

- Capture unique centre ID with format validation
- Capture centre name and full postal address components
- Capture optional centre contact phone and email
- Set initial active or inactive status on creation
- Validate centre ID uniqueness before persistence
- Persist new centre profile to MySQL as source of truth
- Display post-create confirmation with created centre identifier
- Emit audit record for centre creation event

##### Inputs

- Centre ID
- Centre name
- Address line
- City
- District
- State
- PIN code
- Contact phone
- Contact email
- Initial active flag

##### Outputs

- Created centre profile record
- Success confirmation message
- Audit log entry for centre creation

##### Business rules

- Centre ID must be unique across all centres and immutable after save
- Centre name is mandatory
- Full address including city, district, state, and PIN is mandatory
- Newly created inactive centres are not offered in scheduling picklists
- Only Examination Administrators may create centres

##### Validations

- Reject duplicate centre ID on create
- Reject blank centre name
- Reject blank city, district, state, or PIN code
- Validate PIN code numeric format and length
- Validate contact email format when provided
- Validate contact phone numeric length when provided

##### Workflow

DRAFT_FORM → VALIDATED → CREATED → CONFIRMATION_DISPLAYED

##### Search requirements

- Duplicate centre ID check on blur or submit

##### Security

- Examination Administrator role required
- Audit trail for centre creation with actor and timestamp

##### Dependencies

- F03-001 Authorised Examination Centre Register and Search
- F01-002 Examination Administrator Role and Organisation-Wide Permissions

##### Assumptions

- Centre ID format rules are defined by department policy
- No bulk import of centres in this module scope

##### Risks

- Manual centre ID entry errors if format rules are not enforced strictly

##### Non-functional requirements

- Form submission completes within standard admin transaction time
- Clear inline validation messages on field blur

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Add authorised examination centre form with centre ID and name fields | Medium | 16 |
| UI | Add centre address section with city, district, state, and PIN fields | Medium | 16 |
| UI | Add centre optional contact phone and email fields | Easy | 14 |
| UI | Add centre initial active or inactive status selector | Simple | 5 |
| UI | Add centre duplicate ID inline error display | Simple | 5 |
| UI | Add centre success confirmation dialog with created centre ID | Simple | 5 |
| API | Create authorised examination centre with uniqueness validation | Medium | 6 |
| API | Lookup centre ID availability before create submit | Simple | 2 |
| Database | Authorised centre profile insert with address and contact columns | Easy | 0.25 |
| Database | Unique constraint on centre ID column | Easy | 0.25 |
| Database | Centre creation audit history record | Easy | 0.25 |
| Testing | Successful centre create with all mandatory fields happy path | Medium | 0.3 |
| Testing | Duplicate centre ID and missing address field rejection cases | Medium | 0.3 |
| Testing | Unauthorized create attempt and audit log verification | Easy | 0.25 |
| Documentation | Administrator runbook for adding a new authorised centre | Easy | 0.25 |
| Documentation | Technical notes for centre ID uniqueness and audit persistence | Simple | 0.1 |

### F03-008 Edit Authorised Examination Centre Profile

67.7 hours · Go-live · 14 tasks

##### Description

Allows Examination Administrators to update an existing authorised examination centre's name, address, and contact details while preserving immutable centre ID and maintaining audit history of profile changes.

##### Business objective

Keep authorised centre master data accurate when locations, contact points, or display names change without recreating centre records or breaking downstream allocations.

##### Actors

- Examination Administrator

##### User journey

1. Administrator locates centre in the register and selects Edit.
2. System loads edit form pre-populated with current centre profile.
3. Centre ID field is displayed read-only.
4. Administrator updates centre name if required.
5. Administrator updates address lines, city, district, state, or PIN.
6. Administrator updates contact phone or email.
7. System validates updated fields on submit.
8. Administrator saves changes.
9. System persists updates and writes audit history.
10. System displays update confirmation and returns to register or detail view.

##### Functional capabilities

- Load existing centre profile for edit pre-population
- Display centre ID as read-only on edit form
- Update centre name, address components, and contact details
- Validate mandatory address fields on update
- Persist profile changes to MySQL
- Record before-and-after audit history for profile edits
- Block edit of centre ID after creation

##### Inputs

- Centre record identifier
- Updated centre name
- Updated address fields
- Updated contact phone
- Updated contact email

##### Outputs

- Updated centre profile
- Profile change audit record
- Update confirmation message

##### Business rules

- Centre ID cannot be changed after creation
- Edited centres retain existing capacity, user bindings, and restriction configuration
- Profile edits do not automatically change active or inactive status
- Audit history must capture changed fields and modifying administrator

##### Validations

- Reject edit when centre record not found
- Reject blank centre name on update
- Reject blank mandatory address components
- Validate PIN code format on update
- Validate email and phone formats when provided

##### Workflow

EDIT_LOADED → MODIFIED → VALIDATED → UPDATED → CONFIRMATION_DISPLAYED

##### Security

- Examination Administrator role required
- Audit trail for each profile field change

##### Dependencies

- F03-001 Authorised Examination Centre Register and Search
- F03-002 Add Authorised Examination Centre Profile

##### Assumptions

- Concurrent edit by two administrators is rare; last-save-wins acceptable

##### Risks

- Address changes may desynchronise printed hall ticket address until hall ticket regeneration in Module 06

##### Non-functional requirements

- Edit form load within standard admin latency
- Optimistic UI feedback on save

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Edit authorised examination centre form with read-only centre ID | Medium | 16 |
| UI | Edit centre address section with validation messages | Medium | 16 |
| UI | Edit centre contact phone and email fields | Easy | 14 |
| UI | Edit centre unsaved changes navigation warning dialog | Simple | 5 |
| UI | Edit centre save success toast or confirmation banner | Simple | 5 |
| API | Fetch centre profile by identifier for edit pre-population | Easy | 4 |
| API | Update centre profile with field-level validation | Medium | 6 |
| Database | Centre profile update persistence for name, address, and contact | Easy | 0.25 |
| Database | Centre profile change audit history with before and after values | Medium | 0.3 |
| Testing | Successful profile update happy path with audit verification | Medium | 0.3 |
| Testing | Missing mandatory address field rejection on update | Easy | 0.25 |
| Testing | Centre ID immutability enforcement on edit submit | Easy | 0.25 |
| Documentation | Administrator runbook for editing centre profile details | Easy | 0.25 |
| Documentation | Technical notes for centre profile audit history | Simple | 0.1 |

### F03-009 Activate and Deactivate Examination Centre

44.5 hours · Go-live · 14 tasks

##### Description

Provides Examination Administrators with controlled activate and deactivate actions on authorised examination centres so only active centres appear in scheduling, preference selection, and allocation workflows while preserving historical centre records.

##### Business objective

Allow departments to temporarily or permanently withdraw centres from operational use without deleting master data or breaking audit and allocation history.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre register and locates target centre.
2. Administrator selects Activate or Deactivate action based on current status.
3. System displays confirmation dialog explaining downstream impact.
4. For deactivate, dialog warns that centre will be removed from scheduling picklists and new allocations.
5. Administrator confirms action.
6. System updates centre active flag.
7. System records status change audit entry.
8. Register refreshes showing updated status chip.
9. If centre has future scheduled sessions, system displays advisory warning listing affected session count without blocking unless policy requires.

##### Functional capabilities

- Activate inactive centre to make it available for scheduling picklists
- Deactivate active centre to exclude from new scheduling and preferences
- Display confirmation dialog before status change
- Show advisory warning when deactivating centre with future approved session mappings
- Persist active flag change with audit history
- Reflect status change immediately in centre register

##### Inputs

- Centre record identifier
- Target active or inactive status
- Administrator confirmation

##### Outputs

- Updated centre active flag
- Status change audit record
- Confirmation message
- Advisory warning for future session mappings when applicable

##### Business rules

- Deactivated centres remain in register with inactive status
- Only active centres are offered in candidate preference and scheduling picklists
- Deactivation does not delete centre profile, capacity, or restriction configuration
- Reactivation restores centre to active picklists without data loss
- Existing candidate allocations to a deactivated centre are not auto-migrated in this module

##### Validations

- Reject activate when centre is already active
- Reject deactivate when centre is already inactive
- Require explicit administrator confirmation before status change
- Reject status change by unauthorized roles

##### Calculations

- Count future approved session mappings for deactivate advisory warning

##### Workflow

ACTIVE ↔ INACTIVE via ADMIN_CONFIRMED_STATUS_CHANGE

##### Security

- Examination Administrator role required
- Audit log for every activate and deactivate action

##### Dependencies

- F03-001 Authorised Examination Centre Register and Search
- F03-007 Approved Examination Session to Centre Mapping

##### Assumptions

- Policy allows deactivation with existing future mappings subject to manual rescheduling in Module 06

##### Risks

- Deactivating centres with pending allocations may require manual intervention in scheduling module

##### Non-functional requirements

- Status change reflected in register within one refresh cycle

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Deactivate examination centre confirmation dialog with impact summary | Simple | 5 |
| UI | Activate examination centre confirmation dialog | Simple | 5 |
| UI | Centre status chip toggle refresh on register row after action | Simple | 5 |
| UI | Future session mapping advisory warning panel on deactivate | Easy | 14 |
| API | Activate authorised examination centre status flag | Easy | 4 |
| API | Deactivate authorised examination centre status flag | Easy | 4 |
| API | Fetch future session mapping count for deactivate advisory | Medium | 6 |
| Database | Centre active flag update persistence | Simple | 0.1 |
| Database | Centre status change audit history record | Easy | 0.25 |
| Testing | Activate and deactivate happy-path status transitions | Medium | 0.3 |
| Testing | Duplicate activate or deactivate rejection cases | Easy | 0.25 |
| Testing | Unauthorized status change attempt rejection | Easy | 0.25 |
| Documentation | Administrator runbook for centre activation and deactivation policy | Easy | 0.25 |
| Documentation | Technical notes for centre status flag downstream picklist exclusion | Simple | 0.1 |

### F03-010 Centre Approved Capacity Configuration

80.95 hours · Go-live · 14 tasks

##### Description

Allows Examination Administrators to configure approved candidate capacity and per-session seat limits for each authorised examination centre as required by §17 and §18.1 approved capacity attributes supporting allocation and scheduling constraints.

##### Business objective

Define how many candidates each centre can accommodate overall and per examination session so scheduling and allocation modules enforce capacity limits.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre detail and selects Capacity Configuration.
2. System displays current approved total capacity and per-session capacity values.
3. Administrator enters approved total candidate capacity for the centre.
4. Administrator enters default maximum seats per examination session at the centre.
5. Administrator optionally enters concurrent session capacity limit if multiple parallel sessions are supported.
6. System validates capacity values are positive integers and per-session capacity does not exceed total capacity.
7. Administrator saves capacity configuration.
8. System persists values and displays confirmation.
9. System shows current allocated candidate count versus capacity for awareness.

##### Functional capabilities

- Configure approved total candidate capacity per centre
- Configure default maximum seats per examination session at centre
- Configure concurrent session capacity limit when applicable
- Display current allocated candidate count against configured capacity
- Validate capacity values against business rules before save
- Persist capacity configuration to MySQL
- Expose capacity values to scheduling and allocation modules

##### Inputs

- Centre record identifier
- Approved total capacity
- Per-session seat capacity
- Concurrent session limit
- Effective date optional

##### Outputs

- Updated capacity configuration
- Capacity utilisation summary display
- Audit record for capacity changes

##### Business rules

- Approved total capacity must be a positive integer
- Per-session seat capacity must not exceed approved total capacity
- Capacity configuration applies only to active centres for new allocations
- Reducing capacity below current allocated count displays warning but does not auto-reallocate
- Capacity values are used by Module 06 allocation engine as constraints

##### Validations

- Reject zero or negative capacity values
- Reject non-integer capacity entries
- Reject per-session capacity greater than total approved capacity
- Reject capacity update for non-existent centre

##### Calculations

- Compute remaining capacity as approved total minus current allocated count
- Compute utilisation percentage for display

##### Workflow

CAPACITY_VIEWED → VALUES_ENTERED → VALIDATED → SAVED → UTILISATION_DISPLAYED

##### Security

- Examination Administrator role required
- Audit log for capacity configuration changes

##### Integrations

- Read current allocated candidate count from scheduling allocation data

##### Dependencies

- F03-002 Add Authorised Examination Centre Profile
- F06-002 Candidate Centre and Session Allocation

##### Assumptions

- Allocated count is read-only summary sourced from Module 06
- Concurrent session limit is optional based on centre infrastructure

##### Risks

- Capacity reduction after allocations may cause scheduling conflicts requiring manual resolution

##### Non-functional requirements

- Capacity save transaction is atomic
- Utilisation summary refreshes on save

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre approved total capacity configuration form | Medium | 16 |
| UI | Centre per-session seat capacity configuration field | Easy | 14 |
| UI | Centre concurrent session capacity limit field | Easy | 14 |
| UI | Centre capacity utilisation summary bar showing allocated versus approved | Medium | 16 |
| UI | Capacity reduction below allocated count warning dialog | Simple | 5 |
| API | Fetch centre capacity configuration and utilisation summary | Medium | 6 |
| API | Update centre approved total and per-session capacity with validation | Complex | 8 |
| Database | Centre capacity configuration entity with total and session limits | Medium | 0.3 |
| Database | Centre capacity change audit history | Easy | 0.25 |
| Testing | Capacity save happy path with utilisation display refresh | Medium | 0.3 |
| Testing | Per-session capacity exceeding total capacity rejection | Medium | 0.3 |
| Testing | Zero and negative capacity value rejection cases | Easy | 0.25 |
| Documentation | Administrator runbook for centre capacity configuration rules | Easy | 0.25 |
| Documentation | Technical notes for capacity constraint handoff to allocation module | Medium | 0.3 |

### F03-011 Centre Infrastructure Details Configuration

65.7 hours · Go-live · 14 tasks

##### Description

Allows Examination Administrators to record centre infrastructure attributes such as number of examination rooms, computer terminals, backup power, internet connectivity, and accessibility features supporting operational planning and centre approval decisions per §17 infrastructure detail configuration.

##### Business objective

Capture structured infrastructure metadata for each authorised centre to support capacity planning, centre approval reviews, and operational readiness assessment.

##### Actors

- Examination Administrator

##### User journey

1. Administrator navigates to centre detail Infrastructure tab.
2. System displays current infrastructure profile or empty state for new centres.
3. Administrator enters number of examination rooms.
4. Administrator enters total authorised computer terminals available.
5. Administrator selects backup power availability yes or no.
6. Administrator selects internet connectivity type and bandwidth category.
7. Administrator enters accessibility and special facility notes.
8. Administrator enters optional infrastructure remarks for audit reviewers.
9. System validates numeric fields and mandatory selections.
10. Administrator saves infrastructure profile.
11. System persists configuration and shows confirmation.

##### Functional capabilities

- Capture number of examination rooms per centre
- Capture total authorised computer terminal count
- Record backup power availability flag
- Record internet connectivity type and bandwidth category
- Capture accessibility and facility notes as free text
- Capture infrastructure remarks for administrative review
- Validate terminal count against per-session capacity when both configured
- Persist infrastructure profile linked to centre master

##### Inputs

- Centre record identifier
- Examination room count
- Computer terminal count
- Backup power flag
- Internet connectivity type
- Bandwidth category
- Accessibility notes
- Infrastructure remarks

##### Outputs

- Updated centre infrastructure profile
- Infrastructure validation warnings
- Audit record for infrastructure changes

##### Business rules

- Computer terminal count should not be less than per-session seat capacity when both are configured
- Infrastructure details are informational for administration and do not enforce runtime access
- All infrastructure fields may be updated independently of centre active status
- Empty infrastructure profile is allowed for newly created centres

##### Validations

- Reject negative room or terminal counts
- Reject non-integer room and terminal counts
- Warn when terminal count is less than configured per-session capacity
- Validate connectivity type against allowed enumeration

##### Calculations

- Compute advisory ratio of terminals to per-session capacity

##### Workflow

INFRASTRUCTURE_VIEWED → FIELDS_ENTERED → VALIDATED → SAVED

##### Security

- Examination Administrator role required
- Audit log for infrastructure profile changes

##### Dependencies

- F03-002 Add Authorised Examination Centre Profile
- F03-005 Centre Approved Capacity Configuration

##### Assumptions

- Connectivity and bandwidth categories are configurable enumerations
- Infrastructure data supports admin review not runtime enforcement

##### Risks

- Stale infrastructure data if centres upgrade hardware without admin update

##### Non-functional requirements

- Infrastructure tab loads independently of restriction configuration tabs

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre infrastructure details tab with room and terminal count fields | Medium | 16 |
| UI | Centre backup power and internet connectivity selection controls | Easy | 14 |
| UI | Centre accessibility notes and infrastructure remarks text areas | Easy | 14 |
| UI | Terminal count versus session capacity advisory warning banner | Simple | 5 |
| UI | Centre infrastructure empty state for unconfigured centres | Simple | 5 |
| API | Fetch centre infrastructure profile by centre identifier | Easy | 4 |
| API | Update centre infrastructure profile with numeric validation | Medium | 6 |
| Database | Centre infrastructure details entity linked to centre master | Medium | 0.3 |
| Database | Centre infrastructure change audit history | Easy | 0.25 |
| Testing | Infrastructure profile save happy path with all field types | Medium | 0.3 |
| Testing | Negative room count and invalid connectivity enum rejection | Easy | 0.25 |
| Testing | Terminal count below session capacity advisory trigger case | Easy | 0.25 |
| Documentation | Administrator runbook for centre infrastructure data capture | Easy | 0.25 |
| Documentation | Technical notes for infrastructure profile persistence model | Simple | 0.1 |

### F03-012 Approved Examination Session to Centre Mapping

77.95 hours · Go-live · 16 tasks

##### Description

Allows Examination Administrators to define which examination sessions each authorised centre is approved to host, fulfilling §17 map examination sessions to centres and §18.1 approved examination sessions requirement so scheduling only assigns sessions to approved centre pairings.

##### Business objective

Establish explicit approval matrix between centres and examination sessions preventing unapproved centre-session combinations during scheduling and allocation.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre detail Approved Sessions tab.
2. System lists examination sessions currently approved for the centre.
3. Administrator clicks Add Approved Session.
4. System displays searchable list of available examination sessions from examination master excluding already mapped sessions.
5. Administrator selects one or more sessions to approve for the centre.
6. System validates centre is active and session is open for scheduling.
7. Administrator confirms mapping.
8. System persists centre-session approval records.
9. Administrator may remove an approved session mapping via remove action with confirmation.
10. Removed mappings no longer appear in scheduling picklists for that centre.

##### Functional capabilities

- List approved examination sessions for a selected centre
- Search available examination sessions for approval mapping
- Add approved session mapping between centre and examination session
- Remove approved session mapping with confirmation
- Validate centre active status before new mapping
- Exclude already mapped sessions from add picker
- Expose approved session list to scheduling module picklists
- Audit all mapping add and remove actions

##### Inputs

- Centre record identifier
- Examination session identifier
- Mapping effective date optional
- Remove mapping confirmation

##### Outputs

- Centre-session approval mapping list
- Updated mapping after add or remove
- Mapping change audit records

##### Business rules

- Only active centres may receive new session approvals
- A centre-session pair may be mapped only once
- Removed mappings do not delete historical scheduling records
- Approved sessions determine which sessions appear when scheduling at this centre
- Examination session master originates from Module 04 and Module 06

##### Validations

- Reject duplicate centre-session mapping
- Reject mapping to inactive centre
- Reject mapping when examination session not found or closed
- Require confirmation before removing mapping with future scheduled instances

##### Calculations

- Count approved sessions per centre for summary display

##### Workflow

MAPPING_LIST_VIEWED → SESSION_SELECTED → MAPPING_CREATED → MAPPING_LIST_UPDATED; MAPPING_REMOVED via ADMIN_CONFIRMED_REMOVE

##### Search requirements

- Search examination sessions by name and date for approval picker

##### Security

- Examination Administrator role required
- Audit log for mapping add and remove

##### Integrations

- Read examination session master from examination configuration module

##### Dependencies

- F03-001 Authorised Examination Centre Register and Search
- F04-004 Examination Master Configuration
- F06-001 Examination Schedule Creation and Maintenance

##### Assumptions

- Examination session records exist before centre approval mapping
- Mapping is many-to-many between centres and session templates

##### Risks

- Removing approval for sessions with existing schedules may cause scheduling inconsistencies

##### Non-functional requirements

- Session picker search returns results within admin UI latency

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre approved examination session mapping list grid | Medium | 16 |
| UI | Add approved session lookup dialog with session search | Medium | 16 |
| UI | Remove approved session mapping confirmation dialog | Simple | 5 |
| UI | Approved session mapping empty state when no sessions mapped | Simple | 5 |
| UI | Future scheduled instance warning on session mapping removal | Easy | 14 |
| API | List approved examination sessions for a centre | Easy | 4 |
| API | Search available examination sessions for centre approval picker | Medium | 6 |
| API | Create centre to examination session approval mapping | Medium | 6 |
| API | Remove centre to examination session approval mapping | Easy | 4 |
| Database | Centre session approval mapping entity with unique centre-session constraint | Medium | 0.3 |
| Database | Centre session mapping change audit history | Easy | 0.25 |
| Testing | Add and remove session mapping happy-path flows | Medium | 0.3 |
| Testing | Duplicate mapping and inactive centre mapping rejection | Medium | 0.3 |
| Testing | Remove mapping with future schedule advisory display case | Easy | 0.25 |
| Documentation | Administrator runbook for centre session approval mapping | Easy | 0.25 |
| Documentation | Technical notes for approved session picklist integration with scheduling | Medium | 0.3 |

### F03-013 Centre Invigilator and Administrator User Binding

85.2 hours · Go-live · 18 tasks

##### Description

Allows Examination Administrators to bind centre invigilator and centre administrator users to a specific authorised examination centre fulfilling §17 configure centre-specific users and §18.1 centre administrator or invigilator user assignment, integrating with the shared user register without duplicating user lifecycle management.

##### Business objective

Ensure each authorised centre has designated invigilator and administrator users who receive centre-scoped access for centre operations while user account creation remains in User and Role Management.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre detail Centre Users tab.
2. System lists currently bound invigilator and administrator users for the centre.
3. Administrator clicks Bind User.
4. System opens searchable picker of existing centre invigilator role users from user register.
5. Administrator selects user and assigns binding role type as Invigilator or Centre Administrator.
6. System validates user is active and not already bound to the same centre with same role.
7. Administrator confirms binding.
8. System persists centre-user binding record.
9. Administrator may unbind a user via remove action with confirmation when no active centre-day session dependency exists.
10. Bound users gain centre-scoped visibility per access model in Module 01.

##### Functional capabilities

- List centre-bound invigilator and administrator users for a centre
- Search existing centre invigilator role users for binding picker
- Bind user to centre with Invigilator or Centre Administrator role type
- Unbind user from centre with confirmation
- Prevent duplicate binding of same user to same centre
- Validate bound user account is active in user register
- Expose binding data to centre-scoped access enforcement in Module 01 and Module 08
- Audit bind and unbind actions

##### Inputs

- Centre record identifier
- User account identifier
- Binding role type Invigilator or Centre Administrator
- Unbind confirmation

##### Outputs

- Centre-user binding list
- New or removed binding records
- Binding change audit entries

##### Business rules

- User account must exist in centre invigilator user register before binding
- A user may be bound to multiple centres if policy allows
- Same user cannot have duplicate binding role at same centre
- At least one invigilator binding is recommended before centre activation for operations
- Unbinding does not delete user account in Module 01

##### Validations

- Reject binding inactive or locked user accounts
- Reject duplicate centre-user-role binding
- Reject binding users without centre invigilator role assignment
- Warn on unbind when user has scheduled centre-day duties

##### Calculations

- Count bound invigilators and administrators per centre

##### Workflow

BINDING_LIST_VIEWED → USER_SELECTED → BINDING_CREATED → BINDING_LIST_UPDATED; BINDING_REMOVED via ADMIN_CONFIRMED_UNBIND

##### Search requirements

- Search users by name, employee ID, and mobile for binding picker

##### Security

- Examination Administrator role required
- Binding changes audited
- Bound users receive centre-scoped permissions via Module 01 access model

##### Integrations

- Read centre invigilator user register from User and Role Management module

##### Dependencies

- F01-003 Centre Invigilator Role and Centre-Scoped Access Model
- F01-007 Centre Invigilator User Register Centre Binding and Lifecycle
- F03-002 Add Authorised Examination Centre Profile

##### Assumptions

- User creation and password lifecycle remain in Module 01
- Binding role types are Invigilator and Centre Administrator only

##### Risks

- Unbinding sole invigilator before examination day may block centre operations

##### Non-functional requirements

- User picker search responsive for large user registers

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre bound user list grid with role type and status columns | Medium | 16 |
| UI | Bind centre user lookup dialog with user search | Medium | 16 |
| UI | Centre user binding role type selector for invigilator or administrator | Simple | 5 |
| UI | Unbind centre user confirmation dialog | Simple | 5 |
| UI | Centre user binding empty state when no users bound | Simple | 5 |
| UI | Scheduled centre-day duty warning on user unbind attempt | Easy | 14 |
| API | List centre-bound invigilator and administrator users | Easy | 4 |
| API | Search eligible centre invigilator role users for binding picker | Medium | 6 |
| API | Create centre to user binding with role type validation | Medium | 6 |
| API | Remove centre to user binding with dependency check | Medium | 6 |
| Database | Centre user binding entity with centre, user, and role type | Medium | 0.3 |
| Database | Unique constraint preventing duplicate centre-user-role binding | Easy | 0.25 |
| Database | Centre user binding change audit history | Easy | 0.25 |
| Testing | Bind and unbind centre user happy-path flows | Medium | 0.3 |
| Testing | Duplicate binding and inactive user binding rejection | Medium | 0.3 |
| Testing | Unbind user without centre invigilator role rejection case | Easy | 0.25 |
| Documentation | Administrator runbook for centre invigilator binding procedures | Easy | 0.25 |
| Documentation | Technical notes for centre-scoped access binding handoff to Module 01 | Medium | 0.3 |

### F03-014 Authorised Centre Network Restriction Configuration

82 hours · Go-live · 16 tasks

##### Description

Allows Examination Administrators to configure authorised network identifiers such as IP ranges or network tags for each examination centre as part of §18.1 authorised systems, devices, and network configuration, storing restriction data consumed at runtime by Secure Examination Conduct without implementing enforcement in this module.

##### Business objective

Capture centre-specific authorised network parameters so examination access can be restricted to approved centre networks during secure examination conduct.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre detail Network Restrictions tab.
2. System lists configured network entries for the centre.
3. Administrator clicks Add Network Entry.
4. Administrator selects restriction type as single IP, IP range, or CIDR block.
5. Administrator enters network value and optional descriptive label.
6. System validates IP and CIDR format.
7. Administrator saves network entry.
8. System persists entry linked to centre.
9. Administrator may deactivate or delete a network entry with confirmation.
10. Configured entries are flagged as active or inactive for downstream enforcement handoff.

##### Functional capabilities

- List authorised network restriction entries per centre
- Add single IP, IP range, or CIDR network restriction entry
- Edit network entry label and value
- Deactivate network entry without deleting audit history
- Validate IP address and CIDR format on entry
- Prevent overlapping duplicate network entries for same centre
- Expose active network restriction set to Secure Examination Conduct module
- Audit network configuration changes

##### Inputs

- Centre record identifier
- Restriction type
- IP address or range or CIDR value
- Descriptive label
- Active flag

##### Outputs

- Centre network restriction entry list
- Validated network configuration records
- Network configuration audit entries

##### Business rules

- Network restriction configuration is stored here and enforced at runtime in Module 09
- At least one active network entry is recommended before centre examination conduct
- Inactive network entries are retained for audit but excluded from enforcement handoff
- Network configuration is centre-specific and not shared across centres
- Final technical mechanism may combine network with device restrictions per client infrastructure

##### Validations

- Validate IPv4 address format for single IP entries
- Validate CIDR notation format and prefix length bounds
- Validate IP range start is less than or equal to range end
- Reject duplicate identical network entry for same centre
- Reject blank network value

##### Workflow

NETWORK_LIST_VIEWED → ENTRY_ADDED → VALIDATED → SAVED → ACTIVE_FOR_ENFORCEMENT_HANDOFF; ENTRY_DEACTIVATED via ADMIN_ACTION

##### Security

- Examination Administrator role required
- Network configuration changes fully audited
- Restriction values visible only to authorised administrators

##### Integrations

- Publish active network restriction set for Module 09 runtime validation handoff

##### Dependencies

- F03-002 Add Authorised Examination Centre Profile
- F09-002 Authorised Centre Device and Network Enforcement

##### Assumptions

- IPv4 is primary; IPv6 support depends on client infrastructure decision
- Enforcement logic resides entirely in Module 09

##### Risks

- Incorrect IP or CIDR entry may block all centre candidates at examination time

##### Non-functional requirements

- Network entry validation provides immediate inline feedback

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre authorised network restriction entry list grid | Medium | 16 |
| UI | Add network restriction entry form with type selector | Medium | 16 |
| UI | Edit network restriction entry form | Medium | 16 |
| UI | Deactivate network restriction entry confirmation dialog | Simple | 5 |
| UI | Invalid IP or CIDR format inline validation display | Simple | 5 |
| API | List centre network restriction entries with active flag | Easy | 4 |
| API | Create centre network restriction entry with format validation | Complex | 8 |
| API | Update centre network restriction entry label and value | Medium | 6 |
| API | Deactivate centre network restriction entry | Easy | 4 |
| Database | Centre network restriction entry entity with type and value columns | Medium | 0.3 |
| Database | Centre network restriction change audit history | Easy | 0.25 |
| Testing | Add single IP and CIDR network entry happy-path cases | Medium | 0.3 |
| Testing | Invalid IP format and duplicate network entry rejection | Medium | 0.3 |
| Testing | Deactivate network entry exclusion from enforcement handoff case | Easy | 0.25 |
| Documentation | Administrator runbook for centre network restriction setup | Medium | 0.3 |
| Documentation | Technical notes for network restriction handoff to secure conduct module | Medium | 0.3 |

### F03-015 Authorised Centre Device and System Restriction Configuration

117.55 hours · Go-live · 19 tasks

##### Description

Allows Examination Administrators to register authorised examination devices or system identifiers such as hostname, MAC address, or asset tag for each centre per §18.1 authorised systems and devices configuration, providing whitelist data for runtime device enforcement elsewhere.

##### Business objective

Maintain a centre-specific authorised device inventory so candidates can attempt examinations only from approved centre computers.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre detail Authorised Devices tab.
2. System lists registered devices for the centre with identifier, label, and status.
3. Administrator clicks Register Device.
4. Administrator selects device identifier type as MAC address, hostname, or asset tag.
5. Administrator enters identifier value and optional seat or room label.
6. System validates identifier format based on type.
7. Administrator saves device entry.
8. System persists device record linked to centre.
9. Administrator may bulk import device list via file upload when many terminals exist.
10. Administrator may deactivate device entry when hardware is retired.
11. Active device list is available for Module 09 enforcement handoff.

##### Functional capabilities

- List authorised device entries per centre with status
- Register single device with MAC, hostname, or asset tag identifier
- Edit device label and seat or room assignment
- Deactivate device entry preserving audit history
- Bulk import device identifiers from approved file format
- Validate MAC address and hostname formats
- Prevent duplicate device identifier within same centre
- Expose active device whitelist to Secure Examination Conduct module

##### Inputs

- Centre record identifier
- Device identifier type
- Identifier value
- Seat or room label
- Bulk import file
- Active flag

##### Outputs

- Centre device register list
- Imported device registration results summary
- Device configuration audit records

##### Business rules

- Device restriction configuration is stored here and enforced at runtime in Module 09
- Device identifier must be unique within a centre
- Deactivated devices are excluded from enforcement whitelist
- Bulk import validates each row and reports failures without partial silent skip
- Device count should align with infrastructure terminal count for operational readiness

##### Validations

- Validate MAC address format XX:XX:XX:XX:XX:XX or equivalent
- Validate hostname length and allowed character set
- Reject duplicate device identifier at same centre
- Validate bulk import file format and row-level identifier formats
- Reject blank identifier value

##### Calculations

- Count active authorised devices versus infrastructure terminal count for advisory

##### Workflow

DEVICE_LIST_VIEWED → DEVICE_REGISTERED → VALIDATED → SAVED; BULK_IMPORT_SUBMITTED → ROWS_VALIDATED → IMPORT_COMPLETED; DEVICE_DEACTIVATED

##### Search requirements

- Search devices by identifier, label, or seat within centre device list

##### Documents

- Bulk device import template file for administrator download

##### Security

- Examination Administrator role required
- Device whitelist changes audited
- Bulk import file scanned for size and type limits

##### Integrations

- Publish active device whitelist for Module 09 runtime validation handoff

##### Dependencies

- F03-002 Add Authorised Examination Centre Profile
- F03-006 Centre Infrastructure Details Configuration
- F09-002 Authorised Centre Device and Network Enforcement

##### Assumptions

- Device fingerprint mechanism at runtime is defined in Module 09
- Bulk import template format is CSV with defined columns

##### Risks

- Incorrect MAC or hostname entries may deny legitimate centre devices at examination time

##### Non-functional requirements

- Bulk import processes moderate device lists within acceptable admin wait time

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre authorised device register list with search and status filter | Medium | 16 |
| UI | Register single authorised device form with identifier type selector | Medium | 16 |
| UI | Edit authorised device label and seat assignment form | Easy | 14 |
| UI | Deactivate authorised device confirmation dialog | Simple | 5 |
| UI | Bulk device import upload dialog with template download link | Medium | 16 |
| UI | Bulk device import result summary with row error listing | Medium | 16 |
| API | List centre authorised devices with search and status filter | Medium | 6 |
| API | Create single centre authorised device with format validation | Medium | 6 |
| API | Update centre authorised device label and seat assignment | Easy | 4 |
| API | Deactivate centre authorised device entry | Easy | 4 |
| API | Bulk import centre authorised devices with row-level validation | Very high | 12 |
| Database | Centre authorised device entity with identifier type and value | Medium | 0.3 |
| Database | Unique constraint on centre plus device identifier value | Easy | 0.25 |
| Database | Centre device configuration and bulk import audit history | Medium | 0.3 |
| Testing | Single device register and deactivate happy-path flows | Medium | 0.3 |
| Testing | Invalid MAC format and duplicate device identifier rejection | Medium | 0.3 |
| Testing | Bulk import partial failure row error reporting cases | Complex | 0.5 |
| Documentation | Administrator runbook for centre device whitelist management | Medium | 0.3 |
| Documentation | Technical notes for device whitelist handoff and bulk import format | Medium | 0.3 |

### F03-016 Centre Candidate Allocation Summary View

121.65 hours · Go-live · 18 tasks

##### Description

Provides Examination Administrators with read-only visibility of candidate allocation summaries per authorised examination centre including allocated candidate counts by examination and session as required by §17 view candidate allocation for each centre, sourcing allocation data from scheduling without executing allocation in this module.

##### Business objective

Enable administrators to monitor how candidates are distributed across centres for operational planning without performing allocation actions in the centre management module.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre detail Allocation Summary tab or selects View Allocations from register.
2. System displays summary cards with total allocated candidates, upcoming session count, and capacity utilisation.
3. Administrator selects examination filter to narrow summary.
4. System refreshes allocation grid showing examination name, session date, allocated count, and remaining seats.
5. Administrator clicks a session row to expand candidate count breakdown by category if available.
6. Administrator exports allocation summary to spreadsheet when required.
7. Administrator navigates to scheduling module via link for allocation changes.
8. Summary reflects latest allocation state from scheduling module data.

##### Functional capabilities

- Display total allocated candidate count per centre
- Display allocation breakdown by examination and session
- Show remaining seat capacity per session against centre capacity configuration
- Filter allocation summary by examination and date range
- Expand session row for category-wise allocated count when data available
- Export allocation summary to approved spreadsheet format
- Provide deep link to scheduling module for allocation management
- Refresh summary from current scheduling allocation records

##### Inputs

- Centre record identifier
- Examination filter
- Date range filter
- Export format selection

##### Outputs

- Centre allocation summary cards
- Session-wise allocation grid
- Category breakdown when available
- Exported allocation summary file

##### Business rules

- Allocation summary is read-only in this module
- Allocation execution and changes occur in Module 06
- Utilisation compares allocated count to centre capacity from Module 03 configuration
- Only allocated candidates for active and scheduled sessions appear
- Summary excludes candidates with only preferences not yet allocated

##### Validations

- Reject access by non-administrator roles
- Validate date range filter start precedes end
- Return empty grid without error when no allocations exist for centre

##### Calculations

- Compute remaining seats as session capacity minus allocated count
- Compute centre utilisation percentage across upcoming sessions

##### Workflow

SUMMARY_LOADED → FILTER_APPLIED → GRID_DISPLAYED → ROW_EXPANDED → EXPORT_GENERATED

##### Search requirements

- Filter allocations by examination name
- Filter allocations by session date range

##### Reports

- Centre-wise candidate allocation summary export

##### Security

- Examination Administrator role required
- Read-only access; no allocation mutation in this feature

##### Integrations

- Read candidate allocation records from Examination Scheduling and Allocation module

##### Dependencies

- F03-005 Centre Approved Capacity Configuration
- F06-002 Candidate Centre and Session Allocation

##### Assumptions

- Allocation records include examination, session, and candidate category fields
- Export format is Excel or CSV per department standard

##### Risks

- Summary staleness if allocation changes occur during viewing; refresh on tab focus mitigates

##### Non-functional requirements

- Summary grid loads within acceptable time for centres with high candidate volume

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre allocation summary dashboard cards for total allocated and utilisation | Medium | 16 |
| UI | Centre session-wise allocation grid with examination and date columns | Medium | 16 |
| UI | Allocation summary examination and date range filter controls | Easy | 14 |
| UI | Session row expandable category allocation breakdown panel | Medium | 16 |
| UI | Allocation summary empty state when no candidates allocated | Simple | 5 |
| UI | Deep link button to scheduling module allocation management | Simple | 5 |
| UI | Allocation summary export action with format selection | Easy | 14 |
| API | Fetch centre allocation summary totals and utilisation metrics | Medium | 6 |
| API | List centre session-wise allocation rows with filters | Medium | 6 |
| API | Fetch session category-wise allocated count breakdown | Medium | 6 |
| API | Export centre allocation summary to spreadsheet format | Complex | 8 |
| Database | Read-only query access to allocation summary aggregate views | Medium | 0.3 |
| Integration | Read candidate allocation records from scheduling module data store | Easy | 8 |
| Testing | Allocation summary display and filter happy-path scenarios | Medium | 0.3 |
| Testing | Empty allocation and invalid date range filter handling | Easy | 0.25 |
| Testing | Unauthorized access rejection for allocation summary view | Easy | 0.25 |
| Documentation | Administrator runbook for interpreting centre allocation summary | Easy | 0.25 |
| Documentation | Technical notes for read-only allocation data integration | Medium | 0.3 |

## 04 Question Bank & Examination Configuration

996.85 hours · 174 tasks · Business

Examination definition, question bank administration, and configurable rules for paper generation, scoring, and outcomes.

### F04-001 Question Category & Taxonomy Management

106.45 hours · Go-live · 20 tasks

##### Description

Examination Administrators maintain a hierarchical or flat catalogue of question categories used to classify bank items and to drive category-wise question counts during paper-generation rule configuration.

##### Business objective

Provide a controlled, reusable category structure so questions can be grouped consistently and random-selection rules can allocate counts per category without manual ad hoc tagging.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Question Categories from the Question Bank administration menu. 2. System displays the category register with search, status filter, and parent-category filter when hierarchy is enabled. 3. Administrator clicks Add Category. 4. Administrator enters category code, display name, optional description, optional parent category, and display order. 5. System validates uniqueness of code and name within the same parent scope. 6. Administrator saves; category transitions to Active. 7. Administrator returns to the register and verifies the new category appears with Active status chip. 8. Administrator selects an existing category and opens Edit. 9. Administrator updates name, description, parent, or display order but not code after first use. 10. System warns if the category is referenced by live questions or active examination rules before allowing parent change. 11. Administrator opens Deactivate and confirms; category transitions to Inactive and is excluded from new question assignment and new rule configuration. 12. Administrator views empty register state when no categories match filters.

##### Functional capabilities

- Display paginated question category register with text search on code and name
- Filter category register by status Active or Inactive
- Filter category register by parent category when hierarchy is used
- Create question category with code, name, description, parent, and display order
- Edit question category metadata except immutable code after first save
- Deactivate category without deleting historical references
- Block deactivation when category is required by an active examination paper rule unless administrator reassigns dependencies first
- Show empty-state guidance when no categories exist or search returns no rows
- Show inline validation errors on create and edit forms
- Expose active category lookup for downstream question and rule screens

##### Inputs

- Category code
- Category display name
- Optional description
- Optional parent category identifier
- Display order integer
- Status selection on deactivate

##### Outputs

- Category register list rows with code, name, parent, status, question count summary
- Created or updated category record
- Deactivation confirmation outcome
- Active category lookup results for dependent screens

##### Business rules

- Category code must be unique within the examination tenant scope
- Category name must be unique among siblings under the same parent
- Inactive categories cannot be assigned to new questions or new examination rules
- Existing questions and historical papers retain reference to inactive categories for audit
- Parent category cannot be a descendant of the current category
- Only Examination Administrator role may create, edit, or deactivate categories

##### Validations

- Category code required, alphanumeric with optional hyphen, 2–20 characters
- Category name required, 3–100 characters, no leading or trailing whitespace
- Description optional, maximum 500 characters
- Display order required, non-negative integer, maximum 9999
- Parent category must reference an Active category when supplied
- Reject circular parent assignment
- Reject duplicate code on create
- Reject duplicate name under same parent on create and edit
- Reject deactivation when category has Active child categories unless children are deactivated first
- Reject parent change that would orphan active examination rules referencing the category

##### Calculations

- Derived question count per category for register display
- Derived full hierarchical path label for nested categories in register and lookup

##### Workflow

Draft-on-create → Active on successful save; Active → Inactive on administrator deactivate; Inactive remains terminal for new assignments; Active → Active on successful edit

##### Search requirements

- Partial match search on category code
- Partial match search on category name
- Exact filter on status
- Exact filter on parent category

##### Security

- Restrict category administration to Examination Administrator permissions from Module 01
- Audit log entry on create, edit, and deactivate with administrator identity and timestamp
- Prevent unauthenticated access to category register and forms

##### Integrations

- Consume Module 01 authorization hooks to gate category screens and operations

##### Dependencies

- F01 — Platform Role and Permission Catalog
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Category depth is limited to a practical hierarchy of up to three levels
- Question counts shown in register are informational and refreshed on list load

##### Risks

- Late category restructuring may require re-mapping questions and active paper rules
- Large category trees may require pagination tuning in lookup dialogs used by question forms

##### Non-functional requirements

- Category register loads within acceptable enterprise UI response for up to several thousand categories
- All category mutations are persisted in MySQL as system of record
- Deactivation is logical, not physical delete

##### Notes

Prerequisite taxonomy for question bank categorisation and category-wise paper rules in later features.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Question category register with search, status filter, and parent filter | Medium | 16 |
| UI | Create question category form with parent picker and display order | Medium | 16 |
| UI | Edit question category form with code read-only after first use | Medium | 16 |
| UI | Deactivate category confirmation dialog with dependency warning | Simple | 5 |
| UI | Category register empty state when no rows match filters | Simple | 5 |
| UI | Active category lookup dialog for downstream question assignment | Easy | 14 |
| API | List and search question categories with pagination and filters | Medium | 6 |
| API | Create question category with uniqueness and hierarchy validation | Medium | 6 |
| API | Update question category metadata with parent-change guardrails | Complex | 8 |
| API | Deactivate question category without deleting historical references | Medium | 6 |
| API | Active category lookup for question and rule configuration screens | Simple | 2 |
| Database | Question category core entity with parent self-reference | Easy | 0.25 |
| Database | Category uniqueness constraints and status indexes | Complex | 0.5 |
| Database | Category change audit history records | Medium | 0.3 |
| Integration | Module 01 authorization check hook for category administration actions | Simple | 4 |
| Testing | Happy-path create, edit, list, and deactivate category scenarios | Easy | 0.25 |
| Testing | Duplicate code, duplicate sibling name, and invalid parent validation cases | Medium | 0.3 |
| Testing | Circular parent, active-child deactivation block, and authorization denial cases | Complex | 0.5 |
| Documentation | Administrator runbook for maintaining question categories | Easy | 0.25 |
| Documentation | Technical notes for category hierarchy rules and audit behaviour | Simple | 0.1 |

### F04-002 Question Bank Item Lifecycle & Answer Key Management

154.5 hours · Go-live · 26 tasks

##### Description

Examination Administrators create, edit, deactivate, and manage individual question bank items including stem text, options, marks, category assignment, difficulty metadata where applicable, and authoritative answer keys for objective items.

##### Business objective

Maintain a sufficient, quality-controlled pool of examination questions with correct marking keys so downstream random-selection and multi-version paper rules can draw from a validated bank.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Question Bank register. 2. System lists questions with search, category filter, status filter, and marks range filter. 3. Administrator clicks Add Question. 4. Administrator selects question type such as single-correct MCQ, multiple-correct MCQ, or true/false as supported by scope. 5. Administrator enters question stem, assigns category, enters marks, and optionally difficulty label. 6. Administrator adds answer options with option text and marks-as-key indicators per type rules. 7. Administrator designates correct answer key mapping for scorable types. 8. System validates minimum options, key completeness, and positive marks. 9. Administrator saves; question transitions to Active. 10. Administrator opens a question from the register in read-only preview. 11. Administrator opens Edit on an Active question, updates stem, options, marks, category, or answer key. 12. System warns if the question is referenced by active examination configurations before destructive option removal. 13. Administrator opens Deactivate, confirms, and question transitions to Inactive. 14. Inactive questions remain visible in register with Inactive chip but cannot be assigned to new paper rules. 15. Administrator views register empty state when filters yield no results.

##### Functional capabilities

- Display paginated question bank register with text search on stem snippet and question identifier
- Filter register by category, status, question type, and marks range
- Create single-correct MCQ question with stem, options, marks, category, and answer key
- Create multiple-correct MCQ question with partial-key rules as configured
- Create true/false question with binary options and answer key
- Edit existing question content, marks, category, options, and answer key
- Read-only question preview with formatted stem and options
- Deactivate question without physical delete
- Block assignment of inactive questions to new examination paper rules
- Show dependency warning when editing questions referenced by active examinations
- Maintain authoritative answer key separate from display option order
- Show empty and error states on register and forms

##### Inputs

- Question type
- Question stem rich text or plain text
- Category selection
- Marks value
- Optional difficulty label
- Answer option rows with option label and text
- Correct answer key selection per question type
- Status on deactivate

##### Outputs

- Question register rows with identifier, type, category, marks, status, last modified metadata
- Created or updated question and answer key records
- Read-only preview rendering
- Deactivation outcome and dependency warnings

##### Business rules

- Each question belongs to exactly one active category at creation time
- Marks must be greater than zero for scorable questions
- Single-correct MCQ must have exactly one designated correct option in the answer key
- Multiple-correct MCQ must have at least one correct option and at least one incorrect option
- True/false questions must have exactly two options
- Inactive questions remain in bank history and prior paper definitions but are excluded from new rule pools
- Answer key is authoritative for evaluation modules; display order may differ after randomisation at runtime
- Only Examination Administrator role may manage question bank items

##### Validations

- Question stem required, minimum 10 characters, maximum configurable upper bound such as 2000 characters
- Category required and must reference Active category
- Marks required, positive numeric, maximum two decimal places, upper bound per department policy field
- Minimum option count per type: at least four for MCQ unless policy allows three
- Option text required for each option row, non-duplicate within the question
- Answer key must reference valid option identifiers for the question
- Reject save when no correct option is designated for scorable types
- Reject duplicate question stem hash within same category when duplicate detection is enabled
- Reject deactivation when it would leave an active examination rule with insufficient pool depth unless administrator acknowledges override
- Reject edit that removes options referenced by locked examination configurations

##### Calculations

- Per-question maximum obtainable marks equals assigned marks for standard items
- Register display snippet derived from stem first N characters

##### Workflow

Draft-on-create → Active on successful save; Active → Active on edit; Active → Inactive on deactivate; Inactive terminal for new pool inclusion

##### Search requirements

- Partial text search on question stem
- Exact filter on question identifier
- Exact filter on category
- Exact filter on status
- Exact filter on question type
- Numeric range filter on marks

##### Security

- Restrict question bank screens to Examination Administrator permissions
- Audit create, edit, deactivate, and answer key changes with before/after summary
- Prevent exposure of answer key in candidate-facing channels; admin-only views

##### Integrations

- Consume Module 01 authorization hooks
- Provide question and key metadata to Module 10 Evaluation & Results as downstream consumer without runtime paper generation here

##### Dependencies

- F04-001 — Question Category & Taxonomy Management
- F01 — Platform Role and Permission Catalog
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Subjective or essay question types are out of scope unless explicitly added later
- Rich text support is limited to basic formatting acceptable for examination stems

##### Risks

- Answer key errors propagate to scoring in Module 10
- Editing questions after examinations are scheduled may affect consistency unless configurations are locked elsewhere

##### Non-functional requirements

- Question register performant for banks up to tens of thousands of items with indexed search
- MySQL remains authoritative store for questions and answer keys
- Forms handle validation feedback without losing entered option rows

##### Notes

Core question bank administration excluding bulk import handled in F04-003.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Question bank register with search, category filter, type filter, marks range, and status chips | Medium | 16 |
| UI | Create single-correct MCQ question form with dynamic option rows and answer key picker | Complex | 18 |
| UI | Create multiple-correct MCQ question form with multi-select answer key | Complex | 18 |
| UI | Create true/false question form with fixed two-option layout | Easy | 14 |
| UI | Edit question form reusing type-specific layouts with dependency warning banner | Complex | 18 |
| UI | Read-only question preview panel with stem and shuffled-safe option display | Easy | 14 |
| UI | Deactivate question confirmation dialog with pool-depth warning | Simple | 5 |
| UI | Question register empty state when no items match filters | Simple | 5 |
| UI | Question form server-side validation error summary panel | Simple | 5 |
| API | List and search questions with pagination and multi-filter support | Medium | 6 |
| API | Retrieve single question with options and answer key for admin views | Easy | 4 |
| API | Create question with type-specific option and answer key validation | Complex | 8 |
| API | Update question content, marks, category, options, and answer key with dependency checks | Complex | 8 |
| API | Deactivate question without deleting historical references | Medium | 6 |
| API | Question preview payload for read-only rendering | Simple | 2 |
| Database | Question core entity linked to category and type | Medium | 0.3 |
| Database | Question option rows with ordering metadata | Easy | 0.25 |
| Database | Answer key mapping entity separate from display order | Medium | 0.3 |
| Database | Question status indexes and stem search support | Complex | 0.5 |
| Database | Question and answer key change audit history | Medium | 0.3 |
| Integration | Module 01 authorization hook for question bank mutations | Simple | 4 |
| Testing | Happy-path create, edit, preview, list, and deactivate for each supported question type | Complex | 0.5 |
| Testing | Missing stem, invalid marks, insufficient options, and missing answer key rejection cases | Medium | 0.3 |
| Testing | Inactive category assignment block, dependency warning on edit, and answer key exposure security cases | Complex | 0.5 |
| Documentation | Administrator runbook for question authoring and answer key maintenance | Medium | 0.3 |
| Documentation | Technical notes on question types, key storage, and deactivation semantics | Easy | 0.25 |

### F04-003 Question Bank Bulk Import

132.95 hours · Go-live · 25 tasks

##### Description

Examination Administrators import batches of questions from a structured file template into the question bank with pre-commit validation, row-level error reporting, and controlled activation of successfully validated rows.

##### Business objective

Accelerate establishment of a deep question pool required for randomisation and multiple paper versions while preserving data quality through validation before commit.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Question Bank Import from the administration menu. 2. System displays import history register with batch status, uploaded by, row counts, and timestamps. 3. Administrator clicks New Import. 4. Administrator downloads the approved import template reference document link shown on screen. 5. Administrator uploads completed file selecting target default category and question type constraints if applicable. 6. System parses file and transitions batch to Validating. 7. Administrator views validation preview grid listing each row with pass/fail indicator and error messages. 8. Administrator filters preview to failed rows only. 9. Administrator corrects source file offline and re-uploads or excludes failed rows per policy. 10. Administrator clicks Commit Valid Rows when at least one row passed validation. 11. System creates Active questions and answer keys for valid rows and marks batch Committed. 12. Administrator downloads error report file for failed rows. 13. Administrator opens a committed batch detail read-only view showing created question identifiers. 14. Administrator views empty import history state on first use.

##### Functional capabilities

- Display import batch history register with status and counts
- Upload structured import file against template constraints
- Parse and validate each row for required fields, category reference, marks, options, and answer key
- Show validation preview grid with row numbers and error messages
- Filter validation preview to failed rows
- Commit only validated rows into Active questions
- Generate downloadable error report for failed rows
- Show import batch detail with created question cross-reference
- Prevent commit when zero rows pass validation
- Record importing administrator and batch metadata for audit

##### Inputs

- Import file in approved template format
- Optional default category for rows missing explicit category code
- Optional default question type when uniform per file
- Commit confirmation action
- Re-upload replacement file for same draft batch when supported

##### Outputs

- Import batch record with status Validating, Committed, or Failed
- Row-level validation results
- Created question identifiers for committed rows
- Downloadable error report artifact
- Import history register rows

##### Business rules

- Only validated rows are persisted as Active questions on commit
- Failed rows never partially create question records
- Category codes in file must resolve to Active categories
- Duplicate question stems within the same import batch are rejected
- Committed batches are immutable; corrections require new import or manual edit via F04-002
- Maximum row count per batch governed by configured enterprise limit
- Import does not auto-link questions to examination rules; administrator configures rules separately

##### Validations

- File format must match approved template columns and encoding
- Reject empty file upload
- Row-level stem required and length within limits
- Row-level category code must exist and be Active
- Row-level marks must be positive numeric
- Row-level options must meet minimum count for declared type
- Row-level answer key must map to provided option labels
- Reject rows referencing inactive categories
- Reject commit when batch status is not ValidationComplete with at least one valid row
- Reject upload exceeding configured maximum file size or row count

##### Calculations

- Valid row count, failed row count, and committed row count per batch
- Batch progress percentage during validation preview

##### Workflow

Uploaded → Validating → ValidationComplete → Committed; Uploaded or Validating → Failed on fatal parse error; Committed is terminal

##### Search requirements

- Filter import history by batch status
- Filter import history by upload date range
- Text search on batch identifier or uploading administrator

##### Documents

- Downloadable question import template specification reference

##### Reports

- Row-level import error report export per batch

##### Security

- Restrict import screens and commit action to Examination Administrator role
- Audit file upload, validation, and commit events with batch identifier
- Scan or restrict file types to approved template formats only

##### Integrations

- Module 01 authorization hook for import operations
- Resolve category codes against F04-001 category catalogue

##### Dependencies

- F04-001 — Question Category & Taxonomy Management
- F04-002 — Question Bank Item Lifecycle & Answer Key Management
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Template format is agreed CSV or Excel variant documented to administrators
- Large imports may run asynchronously with progress polling on preview screen

##### Risks

- Bulk import of incorrect answer keys affects scoring at scale
- Very large files may require batch size tuning for validation performance

##### Non-functional requirements

- Validation preview returns within acceptable time for batches up to configured row limit
- Imported questions persisted in MySQL with traceability to import batch
- Error report generation available immediately after validation completes

##### Notes

Bulk load path for initial bank population; does not include runtime paper generation.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Question import history register with status and count columns | Easy | 14 |
| UI | New import upload screen with template link and default category selector | Medium | 16 |
| UI | Import validation preview grid with pass/fail indicators per row | Complex | 18 |
| UI | Failed-rows-only filter control on validation preview | Simple | 5 |
| UI | Commit valid rows confirmation dialog with row count summary | Simple | 5 |
| UI | Committed batch detail read-only view with created question identifiers | Easy | 14 |
| UI | Import history empty state on first use | Simple | 5 |
| UI | Import fatal parse error screen with retry guidance | Simple | 5 |
| API | List import batches with filters and pagination | Easy | 4 |
| API | Upload import file and create batch in Uploaded state | Medium | 6 |
| API | Validate import batch rows and return row-level results | Complex | 8 |
| API | Commit validated rows into Active questions and answer keys | Very high | 12 |
| API | Retrieve import batch detail with created question cross-references | Easy | 4 |
| API | Export import error report for failed rows | Medium | 6 |
| Database | Import batch header entity with status and counts | Easy | 0.25 |
| Database | Import row staging entity with validation messages | Medium | 0.3 |
| Database | Batch-to-created-question linkage for traceability | Easy | 0.25 |
| Database | Import audit history for upload, validate, and commit events | Medium | 0.3 |
| Integration | Category code resolution against active taxonomy during validation | Simple | 4 |
| Integration | Module 01 authorization hook for import upload and commit | Simple | 4 |
| Testing | Happy-path upload, validate, preview, commit, and history list scenarios | Complex | 0.5 |
| Testing | Invalid file format, missing columns, bad category code, and bad answer key row rejection cases | Complex | 0.5 |
| Testing | Zero valid rows commit block, duplicate stem in batch, and authorization denial edge cases | Medium | 0.3 |
| Documentation | Administrator runbook for template preparation and import commit | Medium | 0.3 |
| Documentation | Technical notes for batch states, staging cleanup, and error report format | Easy | 0.25 |

### F04-004 Examination Master Configuration

123.5 hours · Go-live · 22 tasks

##### Description

Examination Administrators define and maintain examination master records specifying examination identity, duration, total marks structure reference, passing criteria, negative marking policy, and candidate-facing instructions used by downstream scheduling, conduct, and evaluation modules.

##### Business objective

Centralise authoritative examination parameters so registration, scheduling, secure conduct, and evaluation consume consistent duration, marking, and pass rules.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Examination Master register. 2. System lists examinations with search, status filter, and code filter. 3. Administrator clicks Create Examination. 4. Administrator enters examination code, name, description, duration in minutes, total marks, passing marks or passing percentage mode, negative marking enabled flag, negative mark deduction value, and instructions text. 5. System validates numeric relationships between total and passing marks. 6. Administrator saves; examination transitions to Draft. 7. Administrator reviews Draft examination in read-only summary. 8. Administrator clicks Activate; examination transitions to Active when mandatory fields are complete. 9. Downstream modules may reference Active examinations only. 10. Administrator opens Edit on Draft or Active examination to adjust instructions or marking parameters subject to lock rules. 11. Administrator deactivates examination when retires; transitions to Inactive. 12. Administrator sees empty register state when no examinations exist.

##### Functional capabilities

- Display examination master register with search and status filters
- Create examination master with duration, marks, pass criteria, negative marking, and instructions
- Edit examination master fields with state-aware restrictions
- Read-only examination summary view
- Activate examination when configuration is complete
- Deactivate examination without deleting historical reference
- Enforce negative marking parameters only when feature enabled
- Show validation errors for inconsistent marks configuration
- Expose Active examination lookup to downstream modules
- Show empty register state

##### Inputs

- Examination code
- Examination name
- Optional description
- Duration minutes
- Total marks
- Passing marks or passing percentage according to selected mode
- Negative marking enabled flag
- Negative mark deduction value per wrong answer when enabled
- Examination instructions text
- Activate or deactivate action

##### Outputs

- Examination master register rows
- Draft, Active, or Inactive examination records
- Read-only summary for confirmation
- Active examination lookup results

##### Business rules

- Examination code unique within tenant scope
- Passing threshold cannot exceed total marks
- Negative marking deduction applies only when negative marking enabled
- Inactive examinations cannot be selected for new schedules or registrations
- Historical schedules retain reference to examination version effective at activation time
- Instructions text published to candidate-facing artefacts by downstream modules
- Only Examination Administrator may manage examination master records

##### Validations

- Examination code required, unique, alphanumeric 3–20 characters
- Examination name required, 5–150 characters
- Duration required, positive integer minutes within configured maximum
- Total marks required, positive numeric with up to two decimals
- Passing marks required when mode is absolute marks and must be less than or equal to total marks
- Passing percentage required when mode is percentage and must be between 1 and 100
- Negative deduction value required and positive when negative marking enabled
- Instructions optional, maximum length per policy such as 4000 characters
- Reject activation when any mandatory field fails validation
- Reject deactivation when open future schedules exist unless force-confirm override policy applies

##### Calculations

- Derived passing marks from percentage mode using total marks
- Effective maximum negative deduction exposure informational display based on question count from linked rules in later features

##### Workflow

Draft on create → Active on activate; Active → Active on edit where permitted; Active → Inactive on deactivate; Draft → Inactive on cancel draft if supported

##### Search requirements

- Partial search on examination code and name
- Exact filter on status Draft Active Inactive
- Sort by name, code, and last modified date

##### Security

- Examination master administration restricted to Examination Administrator role
- Audit activation, deactivation, and changes to passing and negative marking parameters
- Prevent unauthenticated register access

##### Integrations

- Module 01 authorization hooks
- Provide Active examination metadata to Module 05 Candidate Registration and Module 06 Examination Scheduling as consumers

##### Dependencies

- F01 — Platform Role and Permission Catalog
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Examination master does not embed question lists; paper rules are configured in F04-005 and F04-006
- Locking edits after schedules exist may be enforced in Module 06 rather than here with warning-only in this module

##### Risks

- Changing passing or negative marking after registrations may affect candidate expectations
- Missing instructions content impacts hall ticket and conduct modules

##### Non-functional requirements

- Examination register responsive for typical catalogue sizes
- MySQL authoritative storage for examination master
- Activation action is atomic

##### Notes

Examination definition master only; scheduling, conduct, and registration flows are out of module scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination master register with search and status filters | Medium | 16 |
| UI | Create examination master form with duration, marks, pass mode, and negative marking section | Complex | 18 |
| UI | Edit examination master form with state-aware field restrictions | Complex | 18 |
| UI | Examination master read-only summary panel | Easy | 14 |
| UI | Activate examination confirmation dialog | Simple | 5 |
| UI | Deactivate examination confirmation dialog with schedule dependency warning | Simple | 5 |
| UI | Examination register empty state | Simple | 5 |
| API | List and search examination masters with pagination | Medium | 6 |
| API | Create examination master in Draft with field validation | Complex | 8 |
| API | Update examination master with pass and negative marking validation | Complex | 8 |
| API | Activate examination master when mandatory fields complete | Medium | 6 |
| API | Deactivate examination master without deleting history | Medium | 6 |
| API | Active examination lookup for downstream registration and scheduling | Simple | 2 |
| Database | Examination master core entity with status lifecycle | Medium | 0.3 |
| Database | Examination code uniqueness and status indexes | Easy | 0.25 |
| Database | Examination master change audit history | Medium | 0.3 |
| Integration | Module 01 authorization hook for examination master mutations | Simple | 4 |
| Testing | Happy-path create, edit, activate, list, and deactivate examination master flows | Medium | 0.3 |
| Testing | Pass marks greater than total, invalid duration, and negative marking missing deduction validation cases | Medium | 0.3 |
| Testing | Activation gating, deactivation with schedule dependency warning, and authorization denial edge cases | Complex | 0.5 |
| Documentation | Administrator runbook for examination master setup and activation | Medium | 0.3 |
| Documentation | Technical notes on examination status lifecycle and downstream consumption | Easy | 0.25 |

### F04-005 Random Question Selection Rules

162.2 hours · Go-live · 27 tasks

##### Description

Examination Administrators configure per-examination random question selection rules specifying total questions to draw, category-wise question counts, eligible difficulty filters if used, and minimum pool depth checks against the active question bank.

##### Business objective

Ensure each examination has explicit, validated rules for drawing questions randomly from the bank by category so sufficient pool depth exists for multi-version randomisation downstream.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens an Active examination from the master register and navigates to Question Selection Rules. 2. System shows existing rule set status Draft or Active or displays empty state prompting first configuration. 3. Administrator clicks Configure Rules. 4. Administrator enters total question count for the paper. 5. Administrator adds category allocation rows specifying category, required count, and optional difficulty filter. 6. System live-calculates sum of category counts versus total and available pool per category from Active questions. 7. System flags insufficient pool depth when available Active questions in a category are less than required count multiplied by configured version multiplier from F04-006 when linked. 8. Administrator adjusts counts or adds bank questions until validation passes. 9. Administrator saves rules as Draft. 10. Administrator reviews read-only rule summary with pool depth indicators. 11. Administrator activates rules; status transitions to Active. 12. Administrator edits Draft rules or creates new Draft superseding prior Active per policy. 13. Administrator deactivates rules when examination retires.

##### Functional capabilities

- Display question selection rule summary per examination
- Configure total question count for examination paper
- Add and edit category-wise question count allocation rows
- Optional per-row difficulty filter when bank items carry difficulty metadata
- Live sum validation of category counts against total
- Pool depth check against Active questions per category
- Cross-check pool depth against multiple version count when version settings exist
- Save rules in Draft status
- Activate rules for downstream paper generation consumers
- Deactivate rules without deleting audit history
- Show insufficient pool warning panel with counts required versus available
- Empty state when examination has no rules configured

##### Inputs

- Examination identifier
- Total question count
- Category allocation rows with category, count, optional difficulty
- Draft save action
- Activate action
- Deactivate action

##### Outputs

- Rule set with Draft or Active status
- Category allocation table
- Pool depth validation results
- Active rule set consumable by secure conduct module
- Administrator warnings for insufficient pool

##### Business rules

- Sum of category counts must equal total question count
- Only Active questions in referenced categories count toward pool depth
- Inactive categories cannot appear in allocation rows
- Active rule set required before examination can be scheduled with random papers
- Pool depth must meet or exceed required count times paper version count configured in F04-006
- One Active rule set per examination at a time
- Editing Active rules creates new Draft superseding on activation unless direct edit permitted in Draft only

##### Validations

- Total question count required, positive integer, within examination policy maximum
- Each allocation row category required and must be Active
- Each allocation count required, positive integer
- Sum of allocation counts must equal total question count exactly
- Reject duplicate category row with same difficulty filter combination
- Reject activation when any category pool depth insufficient
- Reject allocation referencing category with zero Active questions
- Optional difficulty filter must match allowed enumeration when provided
- Reject deactivate when future scheduled sessions depend on Active rules unless confirmed

##### Calculations

- Sum of category allocation counts
- Available pool count per category from Active questions minus optional difficulty filter
- Required pool depth equals allocation count multiplied by paper version count from linked settings
- Remaining pool margin per category for administrator guidance

##### Workflow

NoRules → Draft on first save → Active on activate; Active → Draft on new draft creation; Active → Inactive on deactivate

##### Search requirements

- Not applicable beyond examination context navigation
- Category lookup search within allocation row picker

##### Security

- Restrict rule configuration to Examination Administrator role
- Audit rule activation and material count changes
- Read-only view of pool counts without exposing answer keys

##### Integrations

- Read Active question counts from F04-002 bank
- Read paper version count from F04-006 when present for depth calculation
- Module 01 authorization hooks
- Expose Active rule set metadata to Module 09 Secure Examination Conduct as consumer without performing runtime selection here

##### Dependencies

- F04-001 — Question Category & Taxonomy Management
- F04-002 — Question Bank Item Lifecycle & Answer Key Management
- F04-004 — Examination Master Configuration
- F04-006 — Multiple Question Paper Version & Randomisation Settings
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Random selection algorithm execution occurs in Module 09; this feature defines rules only
- Difficulty filter is optional and ignored when questions lack difficulty metadata

##### Risks

- Insufficient pool discovered late blocks scheduling until bank is expanded
- Category rebalancing requires coordinated updates with bank content

##### Non-functional requirements

- Pool depth checks perform within interactive UI tolerance using indexed counts
- Rule sets stored in MySQL with version identifier for audit
- Activation validates atomically

##### Notes

Configures selection rules and pool depth validation only; candidate-specific paper assembly at exam time is out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination question selection rule summary panel with status chip | Easy | 14 |
| UI | Configure selection rules form with total count and category allocation grid | Complex | 18 |
| UI | Category allocation row add and inline edit controls | Medium | 16 |
| UI | Live pool depth indicator panel per category row | Medium | 16 |
| UI | Insufficient pool depth warning banner with required versus available counts | Easy | 14 |
| UI | Rule set read-only review screen before activation | Easy | 14 |
| UI | Activate rule set confirmation dialog | Simple | 5 |
| UI | Deactivate rule set confirmation dialog | Simple | 5 |
| UI | No rules configured empty state on examination rules tab | Simple | 5 |
| API | Retrieve question selection rule set for an examination | Easy | 4 |
| API | Save Draft question selection rule set with allocation rows | Complex | 8 |
| API | Validate category allocation sums and pool depth for an examination | Complex | 8 |
| API | Activate question selection rule set with sufficiency checks | Complex | 8 |
| API | Deactivate question selection rule set | Medium | 6 |
| API | Category pool availability counts for allocation picker | Medium | 6 |
| Database | Question selection rule set header linked to examination | Medium | 0.3 |
| Database | Category allocation line entities with counts and optional difficulty | Easy | 0.25 |
| Database | Rule set status indexes and activation uniqueness constraints | Complex | 0.5 |
| Database | Rule set change audit history | Medium | 0.3 |
| Integration | Active question bank count aggregation by category for pool depth | Simple | 4 |
| Integration | Read paper version count from examination version settings for depth multiplier | Simple | 4 |
| Integration | Module 01 authorization hook for rule set mutations | Simple | 4 |
| Testing | Happy-path draft save, pool display, activate, and retrieve active rules scenarios | Complex | 0.5 |
| Testing | Allocation sum mismatch, duplicate category row, and zero-count category rejection cases | Medium | 0.3 |
| Testing | Insufficient pool activation block, version multiplier depth check, and authorization denial edge cases | Complex | 0.5 |
| Documentation | Administrator runbook for category allocation and pool depth planning | Medium | 0.3 |
| Documentation | Technical notes on rule set lifecycle and downstream consumption contract | Easy | 0.25 |

### F04-006 Multiple Question Paper Version & Randomisation Settings

131.3 hours · Go-live · 23 tasks

##### Description

Examination Administrators configure the number of distinct question paper versions per examination and define randomisation rules for question order and answer-option order applied when papers are materialised downstream.

##### Business objective

Reduce collusion risk and satisfy examination integrity requirements by supporting multiple paper versions with configurable shuffling behaviour while keeping configuration separate from live conduct.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens an Active examination and navigates to Paper Version Settings. 2. System displays current version count, question order randomisation flag, and answer option randomisation flag or empty defaults. 3. Administrator enters desired number of paper versions as a positive integer. 4. Administrator toggles randomise question order within each version according to policy. 5. Administrator toggles randomise answer option order for applicable objective question types. 6. System recalculates required minimum pool depth using active selection rules from F04-005 multiplied by version count. 7. System shows warning if pool depth is insufficient for requested versions. 8. Administrator saves settings as Draft. 9. Administrator reviews read-only summary of version and randomisation settings. 10. Administrator activates settings; status becomes Active. 11. Administrator edits Draft settings before activation or creates superseding Draft from Active. 12. Administrator deactivates settings when examination retires.

##### Functional capabilities

- Display paper version and randomisation settings summary per examination
- Configure number of distinct paper versions
- Toggle question order randomisation per examination
- Toggle answer option order randomisation per examination
- Recalculate and display pool depth requirement based on version count and F04-005 rules
- Save settings in Draft status
- Activate settings for downstream consumers
- Deactivate settings preserving audit trail
- Block activation when pool depth insufficient for configured versions
- Show empty defaults state before first configuration

##### Inputs

- Examination identifier
- Paper version count
- Question order randomisation enabled flag
- Answer option randomisation enabled flag
- Draft save action
- Activate action
- Deactivate action

##### Outputs

- Draft or Active version settings record
- Pool depth requirement summary
- Activation warnings
- Settings metadata for Module 09 paper materialisation

##### Business rules

- Paper version count must be at least one
- Increasing version count increases required pool depth defined by F04-005 allocations
- Answer option randomisation applies only to question types with multiple options
- One Active settings record per examination
- Inactive examinations cannot activate new version settings
- Runtime paper generation and candidate-specific assembly remain out of scope in this module

##### Validations

- Version count required, integer between 1 and configured policy maximum such as 20
- Reject activation when linked selection rules are not Active
- Reject activation when pool depth check fails for version count multiplied by per-category allocations
- Question order randomisation flag required boolean
- Answer option randomisation flag required boolean
- Reject version count reduction below already generated version inventory in downstream module when lock signal present
- Reject settings for Inactive examination

##### Calculations

- Required pool depth per category equals allocation count multiplied by version count
- Total distinct paper slots equals version count for scheduling guidance display

##### Workflow

Unset → Draft on save → Active on activate; Active → Draft on superseding draft; Active → Inactive on deactivate

##### Security

- Restrict version settings to Examination Administrator role
- Audit activation and changes to version count and randomisation flags

##### Integrations

- Read Active selection rules from F04-005 for depth calculation
- Module 01 authorization hooks
- Expose Active settings to Module 09 Secure Examination Conduct

##### Dependencies

- F04-004 — Examination Master Configuration
- F04-005 — Random Question Selection Rules
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Downstream module stores materialised version catalog; this feature stores configuration intent only
- Randomisation seed strategy is owned by conduct module

##### Risks

- High version counts exhaust category pools quickly
- Changing randomisation flags after papers materialised may cause inconsistency without downstream lock rules

##### Non-functional requirements

- Pool depth recalculation responsive on settings form change
- Settings persisted in MySQL with examination foreign key
- Activation is atomic with validation

##### Notes

Configures version count and randomisation flags only; runtime paper assembly is out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Paper version settings summary panel with version count and randomisation flags | Easy | 14 |
| UI | Configure paper version count and randomisation toggles form | Medium | 16 |
| UI | Pool depth requirement recap panel driven by version count change | Medium | 16 |
| UI | Insufficient pool for version count warning banner | Easy | 14 |
| UI | Version settings read-only review screen before activation | Easy | 14 |
| UI | Activate version settings confirmation dialog | Simple | 5 |
| UI | Deactivate version settings confirmation dialog | Simple | 5 |
| UI | Unset version settings empty state defaults | Simple | 5 |
| API | Retrieve paper version and randomisation settings for an examination | Easy | 4 |
| API | Save Draft paper version and randomisation settings | Medium | 6 |
| API | Validate pool sufficiency for configured version count against active selection rules | Complex | 8 |
| API | Activate paper version and randomisation settings | Complex | 8 |
| API | Deactivate paper version and randomisation settings | Medium | 6 |
| Database | Paper version settings entity linked to examination with randomisation flags | Medium | 0.3 |
| Database | Active settings uniqueness and status indexes per examination | Easy | 0.25 |
| Database | Version settings change audit history | Medium | 0.3 |
| Integration | Selection rule allocation read for pool depth multiplier calculation | Simple | 4 |
| Integration | Module 01 authorization hook for version settings mutations | Simple | 4 |
| Testing | Happy-path save, pool recap update, activate, and retrieve active settings flows | Medium | 0.3 |
| Testing | Invalid version count bounds and missing active selection rules rejection cases | Medium | 0.3 |
| Testing | Insufficient pool activation block and authorization denial edge cases | Complex | 0.5 |
| Documentation | Administrator runbook for choosing version counts and randomisation options | Easy | 0.25 |
| Documentation | Technical notes on randomisation flags and conduct module handoff | Simple | 0.1 |

### F04-007 Result Display, Certificate Eligibility & Examination Fee Configuration

185.95 hours · Go-live · 31 tasks

##### Description

Examination Administrators configure per-examination rules governing how results are displayed to candidates, minimum outcomes required for certificate eligibility, and administrator-maintained examination fee amounts referenced by candidate registration flows by category and attempt type.

##### Business objective

Allow the department to tune candidate-facing result presentation and certificate thresholds without code changes and to maintain authoritative fee amounts consumed by registration without implementing payment processing in this module.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens an Active examination and navigates to Outcome & Fee Settings. 2. System shows tabs or sections for Result Display Rules, Certificate Eligibility Rules, and Examination Fee Amounts. 3. Under Result Display Rules, administrator chooses whether to show numeric score, pass/fail status, sectional breakdown if applicable, and immediate versus delayed display flag as supported. 4. Administrator saves result display Draft. 5. Under Certificate Eligibility Rules, administrator sets minimum pass requirement reference aligned with examination passing criteria and optional minimum score threshold for certificate issuance. 6. Administrator toggles certificate eligibility requires pass only or pass plus minimum score. 7. Administrator saves eligibility Draft. 8. Under Examination Fee Amounts, administrator opens fee rule list showing candidate category such as government employee first attempt, government employee subsequent attempt, and other organisation candidate. 9. Administrator clicks Add Fee Rule and selects category, attempt type first or subsequent, currency, and amount. 10. System validates non-negative amount and unique category-plus-attempt combination per examination. 11. Administrator edits existing fee rule amounts. 12. Administrator deactivates obsolete fee rule row. 13. Administrator reviews combined read-only summary. 14. Administrator activates all outcome and fee settings as a bundle or per section per policy. 15. Module 05 registration consumes Active fee amounts; Module 10 and Module 11 consume eligibility and display rules.

##### Functional capabilities

- Configure result display flags for numeric score visibility
- Configure result display flags for pass/fail visibility
- Configure immediate versus delayed result display policy flag
- Configure certificate eligibility requires pass aligned to examination master
- Configure optional minimum score threshold for certificate eligibility
- Maintain examination fee amount rules by candidate category and attempt type
- Create fee rule row with category, attempt type, and amount
- Edit fee rule amount
- Deactivate fee rule row without deleting history
- List fee rules with filters by category and attempt type
- Activate outcome and fee configuration for downstream consumption
- Validate fee rule uniqueness per examination category and attempt combination
- Show read-only combined summary for examination outcome settings
- Empty states for examinations without fee rules or outcome settings

##### Inputs

- Examination identifier
- Show numeric score flag
- Show pass fail flag
- Immediate display flag
- Certificate eligibility pass required flag
- Optional certificate minimum score
- Fee rule candidate category
- Fee rule attempt type first or subsequent
- Fee amount currency and value
- Activate and deactivate actions

##### Outputs

- Active result display rule set
- Active certificate eligibility rule set
- Active fee rule rows exposed to registration
- Draft settings per section where applicable
- Administrator confirmation summaries

##### Business rules

- Certificate eligibility cannot require score below examination passing threshold
- Fee amount zero explicitly represents free registration for matching category and attempt
- First-time government employee registration fee defaults to zero per SOW unless administrator overrides
- Subsequent attempt and other organisation categories use administrator-configured positive or zero amounts
- Inactive fee rules are ignored by registration fee lookup
- Only one Active fee rule per examination category and attempt type combination
- Result display and eligibility rules apply to Module 10 publication behaviour; certificate layout remains Module 11
- Payment processing and fee collection are out of scope; only amount configuration is in scope

##### Validations

- At least one result display element must be selected when result display section activated
- Certificate minimum score when provided must be numeric and greater than or equal to passing marks and less than or equal to total marks
- Fee amount required, non-negative numeric with two decimal places
- Candidate category required from controlled enumeration matching registration module categories
- Attempt type required as first or subsequent enumeration
- Reject duplicate fee rule for same examination category and attempt type when Active
- Reject eligibility activation when examination master is not Active
- Reject negative fee amounts
- Currency code required from allowed list

##### Calculations

- Effective registration fee lookup key equals examination plus category plus attempt type
- Certificate eligibility evaluation uses max of passing threshold and optional minimum score threshold

##### Workflow

Per section Draft → Active on activate; Active fee row → Inactive on deactivate; Active outcome section → Draft on superseding edit

##### Search requirements

- Filter fee rules by candidate category
- Filter fee rules by attempt type
- Filter fee rules by Active or Inactive status

##### Security

- Restrict outcome and fee configuration to Examination Administrator role
- Audit fee amount changes and eligibility threshold changes
- Fee configuration readable by registration service accounts through authorized integration only

##### Integrations

- Expose Active fee amounts to Module 05 Candidate Registration fee calculation
- Expose result display and certificate eligibility rules to Module 10 Evaluation & Results and Module 11 Certificate Management
- Module 01 authorization hooks

##### Dependencies

- F04-004 — Examination Master Configuration
- F05 — Candidate Registration examination selection and fee flows
- F10 — Evaluation & Results publication behaviour
- F11 — Certificate Management eligibility enforcement
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Candidate category enumerations align with Module 05 registration categories
- Delayed result display scheduling is enforced in Module 10; this module stores the flag only
- Certificate layout and QR embedding are not configured here

##### Risks

- Fee misconfiguration affects registration revenue or blocks valid registrations
- Eligibility threshold misalignment with passing criteria causes certificate disputes
- Changing fee amounts mid-registration window may require effective-date policy outside this scope

##### Non-functional requirements

- Fee lookup by examination category attempt returns within registration flow tolerance
- All settings stored in MySQL as authoritative configuration
- Activation of fee rules is atomic per row

##### Notes

Configures display and eligibility rules and fee amounts only; result publication UI, certificate layout, and payment processing are out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination outcome and fee settings landing tabbed layout | Medium | 16 |
| UI | Result display rules form with score, pass/fail, and immediate display toggles | Medium | 16 |
| UI | Certificate eligibility rules form with pass requirement and optional minimum score | Medium | 16 |
| UI | Examination fee rule register list with category and attempt type filters | Medium | 16 |
| UI | Create examination fee rule form with category, attempt type, currency, and amount | Medium | 16 |
| UI | Edit examination fee rule amount form | Easy | 14 |
| UI | Deactivate fee rule confirmation dialog | Simple | 5 |
| UI | Combined outcome and fee settings read-only summary panel | Easy | 14 |
| UI | Activate outcome settings confirmation dialog | Simple | 5 |
| UI | Fee rules empty state when no rows configured | Simple | 5 |
| API | Retrieve result display rules for an examination | Easy | 4 |
| API | Save and activate result display rules with validation | Medium | 6 |
| API | Retrieve certificate eligibility rules for an examination | Easy | 4 |
| API | Save and activate certificate eligibility rules with pass alignment validation | Complex | 8 |
| API | List examination fee rules with category and attempt filters | Medium | 6 |
| API | Create examination fee rule with uniqueness validation | Medium | 6 |
| API | Update examination fee rule amount | Easy | 4 |
| API | Deactivate examination fee rule row | Easy | 4 |
| API | Registration fee lookup by examination category and attempt type | Medium | 6 |
| Database | Result display rules entity linked to examination | Easy | 0.25 |
| Database | Certificate eligibility rules entity linked to examination | Easy | 0.25 |
| Database | Examination fee rule entity with category attempt uniqueness | Medium | 0.3 |
| Database | Outcome and fee configuration change audit history | Medium | 0.3 |
| Integration | Registration module fee lookup consumption hook | Simple | 4 |
| Integration | Results and certificate modules eligibility and display rule consumption hook | Simple | 4 |
| Integration | Module 01 authorization hook for outcome and fee mutations | Simple | 4 |
| Testing | Happy-path configure and activate result display, eligibility, and fee rules plus lookup scenarios | Complex | 0.5 |
| Testing | Minimum score below pass, duplicate fee rule, and negative fee amount rejection cases | Medium | 0.3 |
| Testing | Inactive examination block, fee lookup returns zero free rule, and unauthorized access edge cases | Complex | 0.5 |
| Documentation | Administrator runbook for result display, certificate eligibility, and fee maintenance | Medium | 0.3 |
| Documentation | Technical notes for registration fee lookup and downstream rule consumption | Easy | 0.25 |

## 05 Candidate Registration

1,466.5 hours · 253 tasks · Business

End-to-end candidate portal access and examination registration for government and non-government employee categories.

### F05-021 Candidate OTP Login and Portal Session Security

93.7 hours · Go-live · 21 tasks

##### Description

Provides mobile-number-based OTP authentication for candidates accessing the examination registration portal, including OTP generation, delivery handoff, verification, resend controls, expiry enforcement, failed-attempt tracking, retry limits, and post-login session timeout handling.

##### Business objective

Ensure only candidates with access to the registered mobile number can enter the portal while enforcing enterprise-grade OTP and session security controls mandated for government examination registration.

##### Actors

- Candidate

##### User journey

1. Candidate opens the examination candidate portal landing page. 2. Candidate enters registered mobile number on the login screen. 3. System validates mobile number format and eligibility for portal access. 4. Candidate submits mobile number to request OTP. 5. System generates time-bound OTP and dispatches via notification channel (Module 07). 6. Candidate receives OTP on mobile device. 7. Candidate enters OTP on verification screen. 8. On successful verification, system creates authenticated candidate session and redirects to portal home or in-progress registration. 9. If OTP is incorrect, system increments failed-attempt counter and displays remaining attempts. 10. If retry limit exceeded, system blocks further attempts for configured cooldown period. 11. Candidate may request OTP resend subject to resend interval and maximum resend count. 12. If OTP expires before entry, candidate must request new OTP. 13. During active session, idle timeout locks session and requires re-authentication.

##### Functional capabilities

- Mobile number entry screen for login initiation
- Mobile number format and portal-eligibility validation
- OTP generation with configurable expiry duration
- OTP dispatch request to notification service
- OTP entry and verification screen
- Failed OTP attempt counter with retry limit enforcement
- OTP resend with interval and maximum resend controls
- Session creation upon successful OTP verification
- Idle session timeout and forced re-login
- Login audit event recording for security trace
- Blocked-state messaging when retry or resend limits exceeded
- Portal redirect for authenticated candidate with existing registration context

##### Inputs

- Mobile number
- OTP code
- Resend OTP request
- Session idle activity signals

##### Outputs

- Authenticated candidate session token
- OTP delivery status
- Failed-attempt and block status messages
- Security audit events

##### Business rules

- Candidate login shall occur exclusively through OTP; password login is out of scope for candidates
- OTP shall expire after configured duration
- Failed OTP attempts shall be tracked and limited
- OTP resend shall be rate-limited
- Active candidate sessions shall timeout after configured idle period
- Concurrent session policy shall align with Module 01 session controls

##### Validations

- Mobile number required and must match approved national mobile format pattern
- Mobile number must correspond to a candidate-permitted portal identity
- OTP must be numeric and match length configured for the portal
- Expired OTP rejected with explicit expiry message
- Incorrect OTP rejected and failed-attempt counter incremented
- Resend blocked until minimum interval elapsed
- Verification blocked when retry limit or resend limit exceeded

##### Calculations

- OTP expiry timestamp from generation time plus configured TTL
- Remaining OTP retry attempts = configured limit minus failed attempts
- Remaining resend attempts = configured resend limit minus resends used
- Session idle expiry from last activity timestamp plus timeout duration

##### Workflow

UNAUTHENTICATED → MOBILE_ENTERED → OTP_REQUESTED → OTP_PENDING → OTP_VERIFIED → SESSION_ACTIVE → SESSION_IDLE_WARNING (optional) → SESSION_EXPIRED → UNAUTHENTICATED; OTP_PENDING → OTP_FAILED (increment attempts) → OTP_BLOCKED when limit exceeded; OTP_PENDING → OTP_EXPIRED → OTP_REQUESTED on resend

##### Notifications

- OTP SMS/delivery via Module 07 Notification Service

##### Security

- OTP values stored hashed or single-use with short TTL
- Failed-attempt and resend counters protected against bypass
- Session token bound to candidate identity and timeout policy
- Login security events available to Module 01 audit register

##### Integrations

- Module 07 Notification Service for OTP dispatch
- Module 01 Candidate Role and session/concurrent-session policy hooks

##### Dependencies

- Module 01 — Candidate Role and Portal Permission Catalogue
- Module 01 — Session Timeout Idle Lock and Concurrent Session Controls
- Module 01 — User Access Audit Register and Security Event Trace
- Module 07 — Multi-Channel Notification Dispatch Engine

##### Assumptions

- Candidate mobile numbers are pre-validated or captured during first registration journey in later features
- OTP channel provider configuration is managed in Module 07
- Session timeout duration aligns with Module 01 global policy

##### Risks

- SMS delivery delays may cause OTP expiry before candidate entry
- Shared mobile devices may expose OTP to unauthorised viewers
- Brute-force OTP guessing if retry limits set too high

##### Non-functional requirements

- OTP generation and verification response within acceptable portal latency
- Security controls configurable without code deployment
- Login flow usable on mobile browsers used by candidates

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate portal login landing with mobile number entry | Easy | 14 |
| UI | OTP entry screen with expiry countdown and attempt remaining indicator | Medium | 16 |
| UI | OTP resend action with cooldown timer and max-resend messaging | Simple | 5 |
| UI | Retry-limit and account-blocked error state screen | Simple | 5 |
| UI | Session idle timeout warning and re-login redirect screen | Simple | 5 |
| API | Validate mobile number format and portal login eligibility | Medium | 6 |
| API | Generate OTP with expiry and persist hashed OTP challenge | Complex | 8 |
| API | Verify OTP with attempt increment and lockout enforcement | Complex | 8 |
| API | Resend OTP with interval and maximum resend validation | Medium | 6 |
| API | Create candidate authenticated session with idle timeout binding | Medium | 6 |
| API | Terminate or refresh session on idle timeout breach | Easy | 4 |
| Database | OTP challenge store with expiry and attempt counters | Medium | 0.3 |
| Database | Candidate login attempt and resend audit history | Easy | 0.25 |
| Integration | OTP dispatch request to Module 07 notification engine | Simple | 4 |
| Integration | Session policy alignment hook with Module 01 concurrent session controls | Simple | 4 |
| Testing | Happy-path mobile login through OTP verification to active session | Medium | 0.3 |
| Testing | Incorrect OTP, expiry, and retry-limit rejection cases | Complex | 0.5 |
| Testing | Resend interval, max resend, and idle session timeout edge cases | Complex | 0.5 |
| Testing | Security audit event emission for failed and successful login | Medium | 0.3 |
| Documentation | Candidate portal login and OTP troubleshooting user guide | Easy | 0.25 |
| Documentation | Administrator OTP policy configuration and security runbook | Medium | 0.3 |

### F05-022 Registration Category Type Selection

63.7 hours · Go-live · 15 tasks

##### Description

Allows an authenticated candidate to choose between Registration Type 1 (Government Department Employee) and Registration Type 2 (PSU/Board/Corporation/Society/Other eligible organisation) at the start of a new examination registration, persisting the selection for downstream profile, document, and fee paths.

##### Business objective

Route each candidate into the correct registration path with distinct data capture, document, and fee rules before any category-specific steps begin.

##### Actors

- Candidate

##### User journey

1. Authenticated candidate initiates new examination registration from portal home. 2. System presents registration category type selection screen with two paths: Government Department Employee and Other Organisation Employee. 3. Candidate reads category descriptions and eligibility guidance. 4. Candidate selects one registration type. 5. System validates selection is allowed for candidate context. 6. System persists registration type on draft registration record. 7. System routes candidate to Government KGID path (F05-003) or Other Organisation manual path (F05-005). 8. If candidate navigates back, system warns that changing type may reset captured data.

##### Functional capabilities

- Registration type selection screen with two distinct paths
- Eligibility guidance text per registration category
- Persist selected registration type on draft registration
- Route to government or other-organisation downstream features
- Back-navigation guard when type change would invalidate captured data
- Display previously selected type when resuming incomplete registration

##### Inputs

- Selected registration type
- Draft registration identifier

##### Outputs

- Persisted registration category type
- Route decision to government or other-organisation flow

##### Business rules

- Exactly one registration type must be selected before profile capture begins
- Registration type determines mandatory KGID path versus manual detail path
- Registration type determines fee rules and competent authority document requirement
- Changing registration type after downstream data capture may require draft reset per policy

##### Validations

- Registration type selection required before proceeding
- Selected type must be one of configured enum values
- Draft registration must belong to authenticated candidate
- Type change blocked or confirmed when dependent data already captured

##### Workflow

DRAFT_CREATED → TYPE_UNSELECTED → TYPE_SELECTED_GOV or TYPE_SELECTED_OTHER → routed to category path; TYPE_SELECTED_* → TYPE_CHANGE_PENDING (if back) → TYPE_UNSELECTED or retained with confirmation

##### Security

- Only authenticated candidate may set type on own draft registration

##### Dependencies

- F05-001 — Candidate OTP Login and Portal Session Security
- Module 04 — Examination Master Configuration for open registration context

##### Assumptions

- Candidate self-declares category; cross-check for other-org occurs via competent authority document

##### Risks

- Candidate selects wrong category requiring restart or administrator intervention

##### Non-functional requirements

- Type selection screen readable on mobile browsers
- Category labels configurable by administrator

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Registration type selection screen with government and other-organisation cards | Medium | 16 |
| UI | Category eligibility guidance panel per registration type | Simple | 5 |
| UI | Registration type change confirmation dialog when downstream data exists | Simple | 5 |
| UI | Resume incomplete registration type display on draft continuation | Easy | 14 |
| API | Create draft registration shell for authenticated candidate | Easy | 4 |
| API | Persist registration category type on draft registration | Medium | 6 |
| API | Validate type change impact and reset dependent draft sections when confirmed | Complex | 8 |
| API | Fetch draft registration with current type for resume flow | Easy | 4 |
| Database | Draft registration header with category type and workflow state | Easy | 0.25 |
| Testing | Happy-path type selection routing to government path | Easy | 0.25 |
| Testing | Happy-path type selection routing to other-organisation path | Easy | 0.25 |
| Testing | Type change with existing captured data confirmation and reset behaviour | Medium | 0.3 |
| Testing | Unauthenticated or cross-candidate draft access rejection | Medium | 0.3 |
| Documentation | Candidate registration category selection guidance | Easy | 0.25 |
| Documentation | Technical notes on draft registration type state transitions | Simple | 0.1 |

### F05-023 Government Employee KGID Lookup and Detail Retrieval

103.45 hours · Go-live · 19 tasks

##### Description

Captures mandatory KGID number for government department employee registrations, invokes KGID integration to retrieve available employee information, and displays retrieved details for candidate review before confirmation.

##### Business objective

Automate government employee identity and employment detail retrieval through authoritative KGID integration while ensuring candidates review system-fetched data before proceeding.

##### Actors

- Candidate

##### User journey

1. Candidate on government registration path reaches KGID entry step. 2. Candidate enters KGID number. 3. System validates KGID format. 4. Candidate submits KGID for lookup. 5. System calls KGID integration hub with KGID number. 6. On success, system displays retrieved fields: employee name, KGID number, department, and other available employment details. 7. On integration failure or not-found, system shows error with retry option. 8. On partial data, system displays available fields and flags missing attributes. 9. Candidate proceeds to confirmation step (F05-004) with retrieved payload attached to draft.

##### Functional capabilities

- KGID number entry form for government path
- KGID format validation before lookup
- KGID integration lookup invocation
- Retrieved employee detail read-only display panel
- Integration error and not-found handling with retry
- Partial retrieval display with missing-field indicators
- Attach retrieved KGID payload to draft registration
- Lookup attempt logging for audit

##### Inputs

- KGID number
- Draft registration identifier

##### Outputs

- Retrieved employee detail snapshot
- KGID lookup status
- Integration error messages

##### Business rules

- KGID number is mandatory for government department employee registrations
- Retrieved KGID details must be displayed before candidate may confirm
- KGID lookup result is subject to data availability from external KGID system
- Duplicate KGID use across active registrations may be restricted per department policy

##### Validations

- KGID number required on government path
- KGID must match configured format pattern
- Lookup blocked when integration unavailable if policy requires live verification
- Retrieved KGID must match entered KGID
- Draft registration must be government category type

##### Workflow

KGID_PENDING → KGID_SUBMITTED → KGID_LOOKUP_IN_PROGRESS → KGID_RETRIEVED or KGID_NOT_FOUND or KGID_INTEGRATION_ERROR → KGID_RETRIEVED proceeds to confirmation

##### Security

- KGID lookup requests scoped to authenticated candidate draft
- Integration credentials managed in Module 02 only

##### Integrations

- Module 02 — KGID Government Employee Lookup Integration

##### Dependencies

- F05-002 — Registration Category Type Selection
- Module 02 — KGID Government Employee Lookup Integration
- Module 02 — Integration Retry Logging and Error Observability

##### Assumptions

- KGID API returns subset of fields listed in FRS; UI adapts to available attributes
- KGID integration retry handled by Module 02 hub

##### Risks

- KGID service downtime blocks government registration path
- Stale KGID data if source system not updated

##### Non-functional requirements

- Lookup feedback with loading state during integration call
- Graceful degradation messaging on timeout

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | KGID number entry form with format hint and submit action | Medium | 16 |
| UI | KGID lookup in-progress loading state | Simple | 5 |
| UI | Retrieved government employee detail read-only review panel | Medium | 16 |
| UI | KGID not-found error state with retry action | Simple | 5 |
| UI | KGID integration failure error state with support guidance | Simple | 5 |
| UI | Partial KGID retrieval display with missing-field indicators | Easy | 14 |
| API | Validate KGID format and government path eligibility | Medium | 6 |
| API | Invoke KGID lookup and map response to registration draft snapshot | Complex | 8 |
| API | Persist KGID lookup result and lookup timestamp on draft | Medium | 6 |
| API | Record KGID lookup attempt outcome for audit trace | Easy | 4 |
| Database | Government employee KGID lookup snapshot on draft registration | Medium | 0.3 |
| Database | KGID lookup attempt log with status and error code | Easy | 0.25 |
| Integration | KGID employee lookup call through Module 02 integration hub | Medium | 16 |
| Testing | Happy-path KGID lookup with full field display | Medium | 0.3 |
| Testing | Invalid KGID format and not-found rejection cases | Medium | 0.3 |
| Testing | Integration timeout and retry error presentation cases | Complex | 0.5 |
| Testing | Non-government draft blocked from KGID lookup | Easy | 0.25 |
| Documentation | Candidate KGID entry and lookup troubleshooting guide | Easy | 0.25 |
| Documentation | Technical KGID mapping and error-code handling notes | Medium | 0.3 |

### F05-024 Government Employee Detail Confirmation and Supplementary Capture

84 hours · Go-live · 16 tasks

##### Description

Enables government department employee candidates to confirm retrieved KGID details as correct and capture additional registration fields such as mobile number and other required information before saving validated candidate profile to the draft registration.

##### Business objective

Ensure government candidates explicitly attest to KGID-retrieved identity data and supply any registration fields not available from KGID before examination selection.

##### Actors

- Candidate

##### User journey

1. Candidate views retrieved KGID details from prior step. 2. Candidate confirms details are correct via explicit confirmation control. 3. If details incorrect, candidate returns to KGID re-entry or support guidance. 4. Upon confirmation, system unlocks supplementary detail form. 5. Candidate enters mobile number and other required registration fields. 6. System validates all supplementary fields. 7. Candidate submits profile section. 8. System saves validated government employee profile to draft registration. 9. System advances candidate to examination selection (F05-007).

##### Functional capabilities

- KGID retrieved detail confirmation checkbox or attestation control
- Incorrect-detail escalation guidance and return-to-KGID navigation
- Supplementary registration field form post-confirmation
- Mobile number capture and validation on government path
- Configurable additional field capture per approved requirements
- Profile save with validation summary errors
- Mark government profile section complete on draft

##### Inputs

- KGID confirmation attestation
- Mobile number
- Additional configurable registration fields

##### Outputs

- Validated government employee profile on draft
- Profile section completion status

##### Business rules

- Candidate must confirm KGID retrieved details before supplementary capture
- Mobile number required for government registrations as applicable
- Confirmed KGID snapshot retained even if supplementary fields edited later before submission
- Profile must pass validation before examination selection unlocked

##### Validations

- KGID confirmation attestation required
- Mobile number required and valid format
- Mobile number uniqueness policy per registration rules if enforced
- Configurable additional fields requiredness enforced per field definition
- Cannot confirm without successful prior KGID retrieval

##### Workflow

KGID_RETRIEVED → AWAITING_CONFIRMATION → CONFIRMED → SUPPLEMENTARY_CAPTURE → PROFILE_VALIDATED → PROFILE_COMPLETE; AWAITING_CONFIRMATION → REJECTED returns to KGID step

##### Security

- Profile edits limited to authenticated owner draft

##### Dependencies

- F05-003 — Government Employee KGID Lookup and Detail Retrieval
- Module 04 — Configurable registration field definitions if centrally managed

##### Assumptions

- Exact supplementary field list finalised at requirements sign-off

##### Risks

- Candidate confirms incorrect KGID data without noticing discrepancies

##### Non-functional requirements

- Form supports mobile data entry
- Field-level inline validation messages

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | KGID retrieved detail confirmation attestation screen | Medium | 16 |
| UI | Incorrect KGID detail guidance with return-to-lookup navigation | Simple | 5 |
| UI | Government supplementary registration detail form | Complex | 18 |
| UI | Profile validation error summary panel | Simple | 5 |
| UI | Government profile section completion status indicator on registration stepper | Easy | 14 |
| API | Record KGID detail confirmation attestation with timestamp | Medium | 6 |
| API | Validate and save government supplementary profile fields | Complex | 8 |
| API | Enforce profile section completion gate before examination selection | Medium | 6 |
| API | Fetch government profile section for draft resume | Easy | 4 |
| Database | Government employee profile extension fields on draft registration | Medium | 0.3 |
| Database | KGID confirmation attestation audit record | Easy | 0.25 |
| Testing | Happy-path confirmation and supplementary profile save | Medium | 0.3 |
| Testing | Missing attestation and invalid mobile rejection cases | Medium | 0.3 |
| Testing | Attempt to skip confirmation or save without KGID retrieval blocked | Complex | 0.5 |
| Documentation | Candidate government profile confirmation instructions | Easy | 0.25 |
| Documentation | Configurable supplementary field administration notes | Simple | 0.1 |

### F05-025 Other Organisation Manual Candidate and Employment Detail Capture

121.15 hours · Go-live · 18 tasks

##### Description

Captures manual candidate and employment details for PSU, Board, Corporation, Society, and other eligible organisation employees including organisation category selection, candidate name, mobile number, employee ID, organisation or department, and other configurable fields.

##### Business objective

Collect complete identity and employment information for non-government candidates who cannot use KGID retrieval, enabling fee, document, and registration processing.

##### Actors

- Candidate

##### User journey

1. Candidate on other-organisation path reaches manual detail capture step. 2. Candidate selects organisation sub-category: PSU, Board, Corporation, Society, or Other eligible organisation. 3. Candidate enters candidate name. 4. Candidate enters mobile number. 5. Candidate enters employee ID. 6. Candidate enters organisation or department name. 7. Candidate completes other configurable required fields. 8. System validates all entries. 9. Candidate submits manual profile section. 10. System saves validated profile to draft registration. 11. System routes candidate to competent authority document steps (F05-006).

##### Functional capabilities

- Organisation sub-category selection control
- Manual candidate name capture
- Mobile number capture
- Employee ID capture
- Organisation or department name capture
- Configurable additional field rendering and validation
- Manual profile save to draft registration
- Profile section completion marker for other-organisation path

##### Inputs

- Organisation sub-category
- Candidate name
- Mobile number
- Employee ID
- Organisation or department
- Configurable additional fields

##### Outputs

- Validated other-organisation employee profile on draft
- Organisation sub-category persisted

##### Business rules

- Other-organisation path requires full manual detail capture
- Examination registration fee is mandatory for this category path
- Competent authority digitally signed document required before registration completion
- Field configurability subject to final approved requirements

##### Validations

- Organisation sub-category required
- Candidate name required with minimum length
- Mobile number required and valid format
- Employee ID required per configuration
- Organisation or department name required
- Configurable fields enforced for requiredness and format
- Draft must be other-organisation registration type

##### Workflow

MANUAL_PROFILE_PENDING → MANUAL_PROFILE_IN_PROGRESS → MANUAL_PROFILE_VALIDATED → MANUAL_PROFILE_COMPLETE

##### Security

- Profile data editable only by owning candidate on draft

##### Dependencies

- F05-002 — Registration Category Type Selection
- F05-006 — Competent Authority Document Template Download and Digitally Signed Upload

##### Assumptions

- Final field list and configurability confirmed at requirements freeze

##### Risks

- Manual entry errors without authoritative identity source
- Fraudulent organisation claims pending document verification

##### Non-functional requirements

- Form usable on mobile devices
- Configurable fields loaded without redeployment where supported

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Other-organisation sub-category selection control | Medium | 16 |
| UI | Manual candidate identity detail form | Complex | 18 |
| UI | Manual employment and organisation detail form | Complex | 18 |
| UI | Configurable dynamic field renderer for additional required attributes | Complex | 18 |
| UI | Manual profile validation error summary | Simple | 5 |
| UI | Other-organisation profile step completion indicator on registration stepper | Easy | 14 |
| API | Validate organisation sub-category against allowed enumeration | Easy | 4 |
| API | Validate and save manual candidate identity fields | Complex | 8 |
| API | Validate and save employment and organisation fields | Complex | 8 |
| API | Load configurable field definitions for other-organisation path | Medium | 6 |
| API | Mark manual profile section complete on draft registration | Easy | 4 |
| Database | Other-organisation candidate profile entity on draft registration | Medium | 0.3 |
| Database | Organisation sub-category and employee identifier indexes for lookup | Easy | 0.25 |
| Testing | Happy-path manual profile capture for each sub-category | Medium | 0.3 |
| Testing | Required field and format validation rejection cases | Complex | 0.5 |
| Testing | Government draft blocked from manual profile save | Easy | 0.25 |
| Documentation | Candidate manual detail entry guide for other-organisation employees | Easy | 0.25 |
| Documentation | Administrator configurable field setup notes | Medium | 0.3 |

### F05-026 Competent Authority Document Template Download and Digitally Signed Upload

116.7 hours · Go-live · 19 tasks

##### Description

Provides prescribed competent authority document template download, digitally signed document upload during other-organisation registration, file validation, registration association, and administrator review visibility linkage.

##### Business objective

Obtain legally attested employment confirmation from competent authority for non-government candidates and make uploaded evidence available for administrator verification.

##### Actors

- Candidate
- Examination Administrator

##### User journey

1. Other-organisation candidate reaches competent authority document step. 2. Candidate views document requirement instructions. 3. Candidate downloads prescribed competent authority document template. 4. Candidate completes template offline and obtains competent authority digital signature. 5. Candidate returns to portal upload screen. 6. Candidate selects digitally signed document file. 7. System validates file type, size, and digital signature presence per policy. 8. On success, system stores document linked to draft registration. 9. Candidate sees upload success with file name and timestamp. 10. On validation failure, candidate sees specific error and may re-upload. 11. Uploaded document associated for administrator review on registration record. 12. Candidate proceeds to examination selection once document requirement satisfied.

##### Functional capabilities

- Competent authority document requirement instruction panel
- Prescribed template download action
- Digitally signed document file upload control
- Upload file type and size validation
- Digital signature verification check on uploaded file
- Document storage linked to registration draft
- Upload success and failure feedback
- Replace document before registration submission
- Administrator review association flag on registration
- Document metadata visible in administrator registration context

##### Inputs

- Template download request
- Digitally signed document file

##### Outputs

- Stored competent authority document
- Upload validation result
- Document metadata for administrator review

##### Business rules

- Competent authority document mandatory for other-organisation registrations
- Document must be digitally signed by competent authority
- Template format prescribed by department and downloadable from portal
- Uploaded document associated with candidate registration for verification
- Document replace allowed until registration finalised

##### Validations

- Upload required before registration completion on other-organisation path
- File extension must match allowed signed document types
- File size within configured maximum
- Digital signature validation per approved technical policy
- Only one active competent authority document per draft unless replace flow used
- Upload blocked for government registration path

##### Workflow

DOCUMENT_PENDING → TEMPLATE_DOWNLOADED → UPLOAD_SELECTED → UPLOAD_VALIDATING → DOCUMENT_ACCEPTED or DOCUMENT_REJECTED → DOCUMENT_ACCEPTED enables next step; DOCUMENT_ACCEPTED → DOCUMENT_REPLACED on re-upload

##### Search requirements

- Administrator registration views must locate associated competent authority document by registration identifier

##### Documents

- Prescribed competent authority confirmation template
- Candidate-uploaded digitally signed competent authority document

##### Security

- Document access restricted to candidate owner and authorised administrators
- Stored document integrity checksum

##### Integrations

- Digital signature validation service or library per approved client infrastructure

##### Dependencies

- F05-005 — Other Organisation Manual Candidate and Employment Detail Capture
- Module 01 — Examination Administrator Role and Organisation-Wide Permissions
- F05-014 — Optional Registration Application Verification and Administrator Review Gate

##### Assumptions

- Digital signature validation mechanism finalised with client PKI policy
- Template file hosted and versioned by administrator

##### Risks

- Invalid or forged signatures if validation weak
- Large file uploads on slow mobile networks

##### Non-functional requirements

- Upload progress indicator
- Template download available without authentication loss mid-flow

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Competent authority document requirement instruction screen | Easy | 14 |
| UI | Prescribed template download button with version label | Simple | 5 |
| UI | Digitally signed document file upload form with drag-and-drop | Medium | 16 |
| UI | Upload validation error detail panel | Simple | 5 |
| UI | Upload success summary with file name and replace action | Easy | 14 |
| UI | Administrator registration document preview link in review context | Medium | 16 |
| API | Serve competent authority template file for download | Easy | 4 |
| API | Accept document upload with type and size validation | Complex | 8 |
| API | Verify digital signature on uploaded competent authority document | Very high | 12 |
| API | Persist document blob metadata linked to draft registration | Complex | 8 |
| API | Replace existing competent authority document on draft | Medium | 6 |
| API | Expose document metadata for administrator registration review | Medium | 6 |
| Database | Registration document metadata with signature validation outcome | Medium | 0.3 |
| Database | Document blob storage reference and checksum | Complex | 0.5 |
| Testing | Happy-path template download and valid signed upload | Medium | 0.3 |
| Testing | Oversized, wrong type, and unsigned document rejection cases | Complex | 0.5 |
| Testing | Document replace and administrator metadata visibility cases | Medium | 0.3 |
| Documentation | Candidate competent authority document preparation and upload guide | Complex | 0.5 |
| Documentation | Administrator template version and signature policy runbook | Medium | 0.3 |

### F05-027 Open Examination Selection for Registration

81.7 hours · Go-live · 15 tasks

##### Description

Displays examinations currently open for candidate registration, allows candidate to select target examination, view applicable examination details, and bind examination choice to the in-progress registration draft.

##### Business objective

Ensure candidates register only for examinations accepting registrations and understand examination parameters before centre preference and fee steps.

##### Actors

- Candidate

##### User journey

1. Candidate completes category-specific profile and document prerequisites. 2. Candidate reaches examination selection step. 3. System lists examinations with registration currently open. 4. Candidate browses examination name, schedule summary, and instructions excerpt. 5. Candidate selects one examination. 6. System displays full applicable examination details for selected item. 7. Candidate confirms examination selection. 8. System binds examination to draft registration. 9. System advances to centre preference selection (F05-008). 10. If no examinations open, candidate sees empty state with guidance.

##### Functional capabilities

- Open-for-registration examination list for candidates
- Examination summary card with key details
- Examination detail view for selected examination
- Single examination selection per registration draft
- Bind selected examination to draft registration
- Empty state when no examinations open
- Change examination selection before final submission if policy allows

##### Inputs

- Selected examination identifier
- Draft registration identifier

##### Outputs

- Examination bound to draft registration
- Examination detail display

##### Business rules

- Only examinations marked open for registration appear
- One examination selected per registration instance
- Examination selection required before centre preferences
- Examination eligibility may consider candidate category from Module 04 configuration

##### Validations

- Selected examination must be in open-for-registration state
- Selected examination must be eligible for candidate category
- Profile and document prerequisites must be complete before selection saved
- Draft must belong to authenticated candidate

##### Workflow

EXAM_UNSELECTED → EXAM_LIST_VIEWED → EXAM_SELECTED → EXAM_CONFIRMED → EXAM_BOUND; EXAM_CONFIRMED → EXAM_CHANGE_PENDING if change allowed → EXAM_SELECTED

##### Search requirements

- Filter open examinations by registration window and candidate category eligibility

##### Security

- Examination list respects candidate portal visibility rules

##### Dependencies

- Module 04 — Examination Master Configuration
- F05-004 or F05-005 — Profile completion features
- F05-006 — Competent authority document for other-organisation path

##### Assumptions

- Examination open/close windows maintained in Module 04

##### Risks

- Candidate selects wrong examination requiring draft amendment

##### Non-functional requirements

- Examination list performant for concurrent registration period

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Open examination list with registration status chips | Medium | 16 |
| UI | Examination summary card with schedule and instruction excerpt | Easy | 14 |
| UI | Selected examination detail panel with confirm action | Medium | 16 |
| UI | No open examinations empty state with guidance message | Simple | 5 |
| UI | Examination change confirmation dialog when preferences already captured | Simple | 5 |
| API | List examinations open for candidate registration with category filter | Medium | 6 |
| API | Fetch examination detail for candidate registration context | Easy | 4 |
| API | Bind selected examination to draft registration with eligibility check | Complex | 8 |
| API | Clear dependent centre preferences when examination changed | Medium | 6 |
| Database | Draft registration examination binding with selection timestamp | Easy | 0.25 |
| Testing | Happy-path examination selection and draft binding | Medium | 0.3 |
| Testing | Closed examination and category-ineligible selection rejection | Medium | 0.3 |
| Testing | Examination change clears downstream preferences validation | Complex | 0.5 |
| Documentation | Candidate examination selection guidance | Easy | 0.25 |
| Documentation | Technical notes on open-registration eligibility rules | Simple | 0.1 |

### F05-028 Examination Centre First and Second Preference Selection

81.4 hours · Go-live · 15 tasks

##### Description

Captures candidate's first and second preferred authorised examination centres from administrator-configured active centre list for use during downstream centre allocation while displaying selection rules and validation feedback.

##### Business objective

Collect candidate centre preferences to inform administrator and system centre allocation per capacity, schedule, and business rules without performing final allocation in this module.

##### Actors

- Candidate

##### User journey

1. Candidate completes examination selection. 2. Candidate reaches centre preference step. 3. System loads list of active authorised examination centres from Module 03. 4. Candidate selects Centre Preference 1 from dropdown or searchable list. 5. Candidate selects Centre Preference 2 from remaining centres. 6. System validates preferences are distinct and centres active. 7. Candidate submits preferences. 8. System persists both preferences on draft registration. 9. System advances to attempt and fee evaluation (F05-009). 10. Candidate may edit preferences until registration finalised.

##### Functional capabilities

- Active authorised centre list for preference selection
- Centre Preference 1 selection control
- Centre Preference 2 selection control
- Distinct preference validation
- Centre search or filter within preference pickers
- Persist both preferences on draft registration
- Display centre name and location summary in picker
- Edit preferences before registration submission

##### Inputs

- Centre Preference 1 identifier
- Centre Preference 2 identifier
- Draft registration identifier

##### Outputs

- Persisted centre preferences on draft
- Preference validation messages

##### Business rules

- Candidates must select exactly two preferred centres
- Preference 1 and Preference 2 must be different centres
- Only active authorised centres available for selection
- Final centre allocation performed in Module 06; preferences are inputs only
- Preferences used during allocation considering capacity and schedule

##### Validations

- Centre Preference 1 required
- Centre Preference 2 required
- Preferences must reference distinct centre identifiers
- Selected centres must be active and authorised
- Examination must be selected before preferences saved

##### Workflow

PREFERENCES_PENDING → PREFERENCE_1_SELECTED → PREFERENCE_2_SELECTED → PREFERENCES_VALIDATED → PREFERENCES_SAVED

##### Search requirements

- Searchable centre list by centre name or district where configured

##### Security

- Centre list exposes only candidate-visible active centres

##### Dependencies

- F05-007 — Open Examination Selection for Registration
- Module 03 — Authorised Examination Centre Register and Search

##### Assumptions

- Centre master maintained in Module 03
- Allocation engine in Module 06 consumes preferences

##### Risks

- Popular centres oversubscribed; candidate may not receive preferred centre

##### Non-functional requirements

- Centre picker performant for large centre catalogues

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre Preference 1 searchable dropdown selector | Medium | 16 |
| UI | Centre Preference 2 searchable dropdown selector excluding Preference 1 | Medium | 16 |
| UI | Centre preference summary review panel before submit | Easy | 14 |
| UI | Duplicate preference validation inline error display | Simple | 5 |
| UI | Inactive centre unavailable messaging in picker | Simple | 5 |
| API | List active authorised centres for examination registration context | Medium | 6 |
| API | Search centres by name or location facet | Medium | 6 |
| API | Validate and save dual centre preferences on draft registration | Complex | 8 |
| API | Fetch saved centre preferences for draft resume | Easy | 4 |
| Database | Draft registration centre preference 1 and preference 2 fields | Easy | 0.25 |
| Testing | Happy-path dual distinct preference save | Medium | 0.3 |
| Testing | Duplicate preference and inactive centre rejection cases | Easy | 0.25 |
| Testing | Preference save blocked without examination selection | Easy | 0.25 |
| Documentation | Candidate centre preference selection instructions | Easy | 0.25 |
| Documentation | Technical notes on preference consumption by allocation module | Simple | 0.1 |

### F05-029 Examination Attempt History and Category Fee Applicability Determination

90.7 hours · Go-live · 17 tasks

##### Description

Evaluates candidate prior examination attempt history against selected examination and category to determine applicable fee: free first attempt for government employees, fee for subsequent government attempts, and mandatory fee for other-organisation candidates per administrator-configured fee rules from Module 04.

##### Business objective

Apply correct category-based and attempt-based fee rules automatically before payment routing so candidates see accurate fee obligation and free-registration eligibility.

##### Actors

- Candidate

##### User journey

1. Candidate completes centre preferences. 2. System evaluates attempt history for candidate against selected examination. 3. System identifies registration category: government or other-organisation. 4. For government employee: system checks if first examination attempt for configured scope. 5. If first attempt, system marks fee as not applicable (free registration). 6. If subsequent attempt, system retrieves configured fee amount from Module 04. 7. For other-organisation: system retrieves mandatory configured fee amount. 8. System displays fee determination summary screen with amount, reason, and attempt count context. 9. Candidate acknowledges fee summary. 10. System routes to payment (F05-010) if fee applicable or directly toward confirmation path if free.

##### Functional capabilities

- Attempt history lookup for candidate and examination
- First-attempt versus subsequent-attempt classification for government employees
- Government first-attempt free registration rule application
- Government subsequent-attempt fee retrieval
- Other-organisation mandatory fee retrieval
- Fee determination summary display with explanatory reason
- Persist fee applicability outcome on draft registration
- Route to payment or skip payment based on determination

##### Inputs

- Candidate identifier
- Selected examination identifier
- Registration category type
- Historical registration and attempt records

##### Outputs

- Fee applicable flag
- Applicable fee amount
- Attempt classification label
- Fee determination audit record

##### Business rules

- Government department employees receive free registration for first examination attempt
- Fee applicable for second and subsequent government employee attempts
- Fee amounts configurable by administrator in Module 04
- Fee mandatory for eligible non-government organisation candidates
- Attempt history maintained to support fee determination
- Registration complete only after successful payment where payment mandatory

##### Validations

- Examination and category must be set before fee evaluation
- Fee configuration must exist when fee applicable
- Attempt history query scoped to authenticated candidate only
- Free path blocked if attempt history indicates subsequent attempt

##### Calculations

- Attempt count for candidate against examination or configured attempt scope
- Fee applicable = false when government and attempt count equals zero per rules
- Fee applicable = true when government subsequent attempt or other-organisation path
- Payable amount = configured fee rule amount when applicable else zero

##### Workflow

FEE_EVAL_PENDING → ATTEMPT_HISTORY_LOADED → FEE_NOT_APPLICABLE (government first) or FEE_APPLICABLE → FEE_DETERMINED → routes to PAYMENT_REQUIRED or PAYMENT_SKIPPED

##### Search requirements

- Attempt history query by candidate, examination, and registration category

##### Security

- Attempt history visible only to owning candidate and authorised administrators

##### Dependencies

- F05-002 — Registration Category Type Selection
- F05-007 — Open Examination Selection for Registration
- Module 04 — Certificate Eligibility and Examination Fee Configuration

##### Assumptions

- Attempt scope definition (per examination vs global) confirmed in Module 04 fee rules
- Prior attempts recorded from completed registrations in this system

##### Risks

- Incorrect attempt count if historical data incomplete
- Fee rule changes mid-registration handled by snapshot at determination time

##### Non-functional requirements

- Fee determination completes within portal step transition latency

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Fee determination summary screen with amount and attempt context | Medium | 16 |
| UI | Government first-attempt free registration informational panel | Simple | 5 |
| UI | Subsequent-attempt fee applicable notice for government employees | Easy | 14 |
| UI | Other-organisation mandatory fee notice panel | Easy | 14 |
| UI | Missing fee configuration error state for administrator escalation | Simple | 5 |
| API | Query candidate attempt history for selected examination scope | Complex | 8 |
| API | Classify first versus subsequent attempt for government category | Complex | 8 |
| API | Resolve applicable fee rule from Module 04 configuration | Complex | 8 |
| API | Persist fee applicability outcome and calculated amount on draft | Medium | 6 |
| API | Expose fee determination result for payment initiation feature | Easy | 4 |
| Database | Registration fee determination snapshot with attempt count | Medium | 0.3 |
| Database | Candidate examination attempt history index for fee lookup | Complex | 0.5 |
| Testing | Happy-path government first-attempt free determination | Medium | 0.3 |
| Testing | Government subsequent-attempt and other-organisation fee applicable cases | Complex | 0.5 |
| Testing | Missing fee configuration and attempt history edge cases | Medium | 0.3 |
| Documentation | Candidate fee rules explanation by category and attempt | Medium | 0.3 |
| Documentation | Technical attempt-count scope and fee rule resolution notes | Complex | 0.5 |

### F05-030 Registration Fee Payment Initiation and Success Completion

134.8 hours · Go-live · 21 tasks

##### Description

Initiates payment gateway transaction when registration fee is applicable, handles successful payment callback, records transaction and reference numbers, generates payment receipt, and progresses registration toward completion after successful payment confirmation.

##### Business objective

Collect mandatory examination registration fees through integrated payment gateway and mark registration fee-compliant upon successful payment as prerequisite to registration finalisation.

##### Actors

- Candidate

##### User journey

1. Fee determination indicates payment required (F05-009). 2. Candidate views payment summary with examination, fee amount, and candidate details. 3. Candidate initiates payment. 4. System creates payment transaction record and calls payment gateway via Module 02. 5. Candidate redirected to payment gateway hosted page or embedded flow. 6. Candidate completes payment on gateway. 7. System receives success callback with transaction reference. 8. System verifies callback authenticity and amount match. 9. System updates payment status to successful on draft registration. 10. System stores transaction and reference number. 11. Candidate views payment success confirmation. 12. Candidate downloads or views payment receipt. 13. System enables registration finalisation step (F05-012).

##### Functional capabilities

- Payment summary screen before gateway handoff
- Payment initiation with transaction record creation
- Payment gateway redirect or embed handoff
- Successful payment callback verification
- Transaction and reference number persistence
- Payment receipt display and download
- Registration fee-compliant status update on success
- Advance registration workflow after successful payment

##### Inputs

- Draft registration identifier
- Applicable fee amount
- Payment gateway callback payload

##### Outputs

- Payment transaction record
- Transaction reference number
- Payment receipt
- Fee-compliant registration status

##### Business rules

- Payment mandatory where fee determination marks fee applicable
- Registration not complete until successful payment when mandatory
- Successful payment callback must match initiated amount and registration
- Transaction reference stored for audit and receipt
- Free registrations skip this feature entirely

##### Validations

- Payment initiation blocked when fee not applicable
- Payment amount must match determined fee amount
- Callback signature or token verified per gateway policy
- Duplicate success callback idempotent handling
- Draft must be in payment-pending state for initiation

##### Calculations

- Payable amount equals fee determination snapshot amount
- Payment status derived from gateway callback outcome

##### Workflow

PAYMENT_PENDING → PAYMENT_INITIATED → GATEWAY_IN_PROGRESS → PAYMENT_SUCCESS → FEE_COMPLIANT → REGISTRATION_FINALISATION_ENABLED; PAYMENT_INITIATED → PAYMENT_ABANDONED if candidate returns without completion

##### Search requirements

- Candidate payment history by registration identifier

##### Documents

- Payment receipt PDF or printable view

##### Notifications

- Payment confirmation notification via Module 07 upon success

##### Security

- Payment callback verification prevents tampering
- PCI-sensitive data not stored beyond gateway references

##### Integrations

- Module 02 — Payment Gateway Fee Transaction Integration
- Module 07 — Payment confirmation notification dispatch

##### Dependencies

- F05-009 — Examination Attempt History and Category Fee Applicability Determination
- Module 02 — Payment Gateway Fee Transaction Integration
- F05-012 — Registration Confirmation Application Number and Status Visibility

##### Assumptions

- Payment gateway supports redirect and callback pattern configured in Module 02
- Receipt format approved by finance stakeholder

##### Risks

- Callback delay leaves registration in pending payment state
- Amount mismatch between initiation and callback

##### Non-functional requirements

- Payment handoff secure over HTTPS
- Idempotent callback processing for reliability

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Registration payment summary screen with fee breakdown | Medium | 16 |
| UI | Payment gateway redirect loading and return landing screen | Easy | 14 |
| UI | Payment success confirmation screen with reference number | Medium | 16 |
| UI | Payment receipt view and download screen | Medium | 16 |
| UI | Payment already completed informational read-only state | Simple | 5 |
| API | Initiate payment transaction with amount and registration binding | Complex | 8 |
| API | Process successful payment gateway callback with signature verification | Very high | 12 |
| API | Persist transaction reference and payment success status | Complex | 8 |
| API | Generate payment receipt data for candidate download | Medium | 6 |
| API | Mark registration fee-compliant and unlock finalisation | Medium | 6 |
| API | Fetch payment status for draft registration resume | Easy | 4 |
| Database | Registration payment transaction entity with gateway references | Complex | 0.5 |
| Database | Payment receipt metadata and issuance timestamp | Easy | 0.25 |
| Integration | Payment gateway initiation call via Module 02 hub | Medium | 16 |
| Integration | Payment success notification trigger to Module 07 | Simple | 4 |
| Testing | Happy-path payment initiation through success callback to receipt | Complex | 0.5 |
| Testing | Amount mismatch and invalid callback signature rejection | Very high | 1 |
| Testing | Duplicate success callback idempotent processing | Complex | 0.5 |
| Testing | Free registration path skips payment initiation | Easy | 0.25 |
| Documentation | Candidate payment and receipt download guide | Medium | 0.3 |
| Documentation | Technical payment callback verification and reconciliation notes | Complex | 0.5 |

### F05-031 Failed Payment Handling and Registration Recovery

115.15 hours · Go-live · 20 tasks

##### Description

Handles failed, declined, cancelled, and abandoned payment scenarios during registration including failure reason display, draft preservation in payment-pending state, retry payment initiation, duplicate-transaction safeguards, and clear guidance until successful payment or candidate exits.

##### Business objective

Prevent loss of registration progress on payment failure and give candidates a controlled recovery path to complete mandatory fee payment without duplicate charges or orphaned registrations.

##### Actors

- Candidate

##### User journey

1. Candidate initiates payment from F05-010. 2. Payment gateway returns failure, decline, cancellation, or timeout. 3. System receives failure callback or detects abandoned session. 4. System records failed payment attempt with reason code. 5. Candidate redirected to failed payment screen showing reason and registration summary. 6. Candidate reviews remaining fee amount due unchanged. 7. Candidate chooses retry payment action. 8. System validates no successful payment already recorded. 9. System initiates new payment transaction linked to same draft. 10. On repeated failures, system shows escalating guidance and support contact. 11. Registration remains incomplete and not confirmed until success. 12. Candidate may exit and resume payment later from registration status view (F05-013).

##### Functional capabilities

- Failed payment callback processing
- Abandoned payment session detection
- Failed payment reason display to candidate
- Preserve draft registration in payment-pending state
- Retry payment initiation from failure screen
- Prevent duplicate successful charges for same registration
- Failed attempt counter and audit trail
- Resume failed payment from registration status view
- Block registration finalisation while payment failed or pending

##### Inputs

- Payment failure callback payload
- Abandoned session signal
- Retry payment request

##### Outputs

- Failed payment attempt record
- Payment-pending draft state
- Retry payment transaction
- Candidate failure guidance messages

##### Business rules

- Registration incomplete when mandatory payment fails
- Candidate may retry payment without re-entering prior registration steps
- Each retry creates new gateway transaction unless policy reuses open session
- Successful payment on any attempt completes fee requirement
- Failed attempts logged for administrator reconciliation in Module 12 scope

##### Validations

- Failure callback authenticity verified
- Retry blocked if registration already fee-compliant
- Retry blocked if maximum retry count exceeded when configured
- Draft ownership verified on retry
- Concurrent retry initiation prevented

##### Calculations

- Failed attempt count incremented per distinct failure event
- Outstanding fee amount remains fee determination snapshot until success

##### Workflow

PAYMENT_INITIATED → PAYMENT_FAILED or PAYMENT_CANCELLED or PAYMENT_ABANDONED → PAYMENT_PENDING_RETRY → PAYMENT_INITIATED (retry) → PAYMENT_SUCCESS or PAYMENT_FAILED; PAYMENT_PENDING_RETRY → RESUMED_FROM_STATUS_VIEW

##### Search requirements

- Candidate views failed payment attempts on own registration

##### Notifications

- Optional payment failure alert via Module 07

##### Security

- Failure callbacks verified same as success callbacks
- Retry tokens bound to candidate session

##### Integrations

- Module 02 — Payment Gateway Fee Transaction Integration failure callbacks
- Module 07 — Optional payment failure notification

##### Dependencies

- F05-010 — Registration Fee Payment Initiation and Success Completion
- F05-013 — Candidate Registration Status Self-Service Visibility

##### Assumptions

- Gateway provides distinct failure reason codes mappable to user messages

##### Risks

- Multiple partial gateway sessions causing reconciliation complexity
- Candidate abandons registration indefinitely in payment-pending state

##### Non-functional requirements

- Failure screen displayed within seconds of gateway return
- Retry flow idempotent under double-click

##### Notes

Covers FRS §13 failed payment handling explicitly called out as prior coverage gap.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Payment failed screen with gateway reason and registration summary | Medium | 16 |
| UI | Payment cancelled or abandoned return screen with retry action | Medium | 16 |
| UI | Retry payment confirmation dialog with outstanding amount | Simple | 5 |
| UI | Maximum retry exceeded blocked state with support guidance | Simple | 5 |
| UI | Resume incomplete payment banner on registration status view | Easy | 14 |
| API | Process failed payment gateway callback with reason mapping | Complex | 8 |
| API | Detect and mark abandoned payment sessions after timeout | Complex | 8 |
| API | Initiate payment retry with duplicate-success guard | Complex | 8 |
| API | List failed payment attempts for candidate registration | Medium | 6 |
| API | Enforce registration finalisation block while payment unresolved | Medium | 6 |
| Database | Failed payment attempt log with reason code and timestamp | Medium | 0.3 |
| Database | Draft registration payment-pending state flag | Easy | 0.25 |
| Integration | Failure callback handling through Module 02 payment hub | Medium | 16 |
| Integration | Optional payment failure notification to Module 07 | Simple | 4 |
| Testing | Happy-path failure display and successful retry completion | Complex | 0.5 |
| Testing | Declined, cancelled, timeout, and abandoned session cases | Complex | 0.5 |
| Testing | Retry blocked when already paid and concurrent retry prevention | Complex | 0.5 |
| Testing | Registration finalisation blocked with unresolved failed payment | Medium | 0.3 |
| Documentation | Candidate failed payment recovery instructions | Medium | 0.3 |
| Documentation | Administrator failed transaction review and retry policy runbook | Complex | 0.5 |

### F05-032 Registration Confirmation and Unique Application Number Generation

125.35 hours · Go-live · 20 tasks

##### Description

Finalises eligible draft registrations by validating prerequisites, generating unique registration or application number, persisting complete application including examination, centre preferences, documents, and payment details, and displaying registration confirmation to the candidate.

##### Business objective

Provide candidates with definitive proof of completed examination registration and a unique reference for all downstream scheduling, allocation, and support interactions.

##### Actors

- Candidate

##### User journey

1. Candidate completes all mandatory steps: profile, documents (if applicable), examination, preferences, and payment (if applicable). 2. Candidate reaches registration review and submit step. 3. System displays registration summary for final review. 4. Candidate submits registration. 5. System validates all prerequisites complete and fee-compliant if required. 6. System generates unique application or registration number. 7. System persists complete registration record from draft. 8. System transitions registration status to submitted or confirmed per policy. 9. Candidate views confirmation screen with application number. 10. System triggers registration confirmation notification via Module 07. 11. Candidate may print or save confirmation summary.

##### Functional capabilities

- Registration final review summary screen
- Prerequisite completeness validation before submit
- Unique application number generation
- Persist complete registration from draft
- Store examination details on registration
- Store centre preferences on registration
- Store uploaded documents reference on registration
- Store payment details where applicable
- Registration confirmation display
- Registration confirmation notification trigger

##### Inputs

- Draft registration identifier
- Final submit action

##### Outputs

- Unique application or registration number
- Completed registration record
- Confirmation display
- Confirmation notification

##### Business rules

- Unique application number generated for each completed registration
- Registration complete only after successful payment where mandatory
- All mandatory sections must be complete before submission
- Complete application stored including examination, preferences, documents, payment
- Optional verification gate may change post-submit status (F05-014)

##### Validations

- Profile section complete for registration category
- Competent authority document present for other-organisation path
- Examination selected
- Both centre preferences captured
- Fee compliance verified when payment mandatory
- Draft not already finalised
- Application number uniqueness enforced

##### Calculations

- Application number generated per configured numbering scheme
- Registration status derived from submit outcome and optional verification policy

##### Workflow

DRAFT_READY → REVIEW_SUBMITTED → VALIDATING → CONFIRMED (application number issued) or VALIDATION_FAILED; CONFIRMED → PENDING_VERIFICATION if optional approval enabled

##### Documents

- Registration confirmation summary printable view

##### Notifications

- Registration confirmation via Module 07

##### Security

- Submit allowed only by owning authenticated candidate
- Application number generation concurrency-safe

##### Integrations

- Module 07 — Registration confirmation notification

##### Dependencies

- F05-004 or F05-005 — Profile features
- F05-006 — Competent authority document for other-organisation
- F05-007 — Examination selection
- F05-008 — Centre preferences
- F05-009 — Fee determination
- F05-010 or payment-skipped free path — Fee compliance
- F05-011 — No unresolved failed payment
- Module 07 — Examination Lifecycle Event Subscription

##### Assumptions

- Application numbering scheme provided by department
- Verification optional per F05-014

##### Risks

- Concurrent submit attempts could race without idempotency
- Numbering scheme exhaustion under high volume

##### Non-functional requirements

- Confirmation generated within acceptable submit latency
- Application number human-readable for candidate support

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Registration final review summary with all captured sections | Complex | 18 |
| UI | Submit registration confirmation dialog | Simple | 5 |
| UI | Registration confirmation success screen with application number | Medium | 16 |
| UI | Printable registration confirmation summary view | Easy | 14 |
| UI | Prerequisite incomplete validation error panel on submit | Medium | 16 |
| API | Validate all registration prerequisites before finalisation | Very high | 12 |
| API | Generate unique application number with concurrency control | Complex | 8 |
| API | Finalise draft into completed registration record | Very high | 12 |
| API | Persist examination, preferences, document, and payment snapshots on registration | Complex | 8 |
| API | Transition registration status to confirmed or pending verification | Complex | 8 |
| Database | Completed candidate registration entity with application number | Complex | 0.5 |
| Database | Application number uniqueness constraint and sequence | Complex | 0.5 |
| Database | Registration finalisation audit event | Easy | 0.25 |
| Integration | Registration confirmation notification dispatch to Module 07 | Simple | 4 |
| Testing | Happy-path full registration finalisation with application number | Complex | 0.5 |
| Testing | Submit blocked for incomplete profile, document, payment, or preferences | Very high | 1 |
| Testing | Concurrent submit idempotency and duplicate number prevention | Complex | 0.5 |
| Testing | Government free path finalisation without payment | Medium | 0.3 |
| Documentation | Candidate registration confirmation and application number guide | Medium | 0.3 |
| Documentation | Technical application numbering and finalisation state notes | Complex | 0.5 |

### F05-033 Candidate Registration Status Self-Service Visibility

122.1 hours · Go-live · 18 tasks

##### Description

Allows logged-in candidates to view list and detail of their examination registrations including application number, registration status, examination details, centre preferences, payment status, document status, and actions to resume incomplete registrations or retry pending payments.

##### Business objective

Give candidates continuous visibility into registration progress and outcomes from login without administrator intervention for standard status queries.

##### Actors

- Candidate

##### User journey

1. Authenticated candidate navigates to My Registrations from portal. 2. System lists candidate registrations with application number, examination name, status chip, and date. 3. Candidate filters or searches own registrations if list large. 4. Candidate selects one registration to view detail. 5. Detail view shows examination, preferences, fee and payment status, document status, and overall registration status. 6. For incomplete drafts, candidate sees resume action to continue registration. 7. For payment-pending registrations, candidate sees retry payment action linking to F05-011. 8. For confirmed registrations, candidate sees read-only summary. 9. Candidate returns to list or portal home.

##### Functional capabilities

- My Registrations list for authenticated candidate
- Registration status chips for submitted, pending payment, pending verification, confirmed
- Registration detail read-only view
- Examination and centre preference display on detail
- Payment status and receipt link on detail
- Document upload status on detail for other-organisation
- Resume incomplete draft registration action
- Retry pending payment shortcut
- Search or filter own registrations

##### Inputs

- Authenticated candidate identifier
- Registration search or filter criteria

##### Outputs

- Registration list
- Registration detail view
- Resume and retry payment deep links

##### Business rules

- Candidates view only own registrations
- Registration status reflects payment, verification, and submission state
- Incomplete drafts accessible for resume until expiry policy if any
- Final centre allocation and hall ticket not shown here; handled in Module 06

##### Validations

- List and detail scoped to authenticated candidate identity
- Resume action only for incomplete owned drafts
- Retry payment only when fee pending and not fee-compliant

##### Workflow

LIST_VIEW → DETAIL_VIEW → RESUME_DRAFT or RETRY_PAYMENT or READ_ONLY_CONFIRMED

##### Search requirements

- Search own registrations by application number
- Filter by registration status
- Filter by examination name

##### Documents

- Link to payment receipt where payment completed

##### Security

- Strict candidate ownership scoping on all queries
- No cross-candidate data leakage in search

##### Dependencies

- F05-001 — Candidate OTP Login
- F05-012 — Registration Confirmation
- F05-011 — Failed Payment Handling for retry links

##### Assumptions

- Status vocabulary aligned with optional verification feature when enabled

##### Risks

- Stale status if asynchronous payment callback delayed

##### Non-functional requirements

- List pagination for candidates with many registrations
- Mobile-friendly status views

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | My Registrations list with status chips and application numbers | Medium | 16 |
| UI | Registration search by application number filter bar | Easy | 14 |
| UI | Registration status filter dropdown | Simple | 5 |
| UI | Registration detail read-only view with section summaries | Complex | 18 |
| UI | Resume incomplete registration action button | Easy | 14 |
| UI | Retry pending payment action button on detail | Easy | 14 |
| UI | Empty registrations list first-time candidate state | Simple | 5 |
| API | List candidate registrations with status and summary fields | Medium | 6 |
| API | Search candidate registrations by application number | Medium | 6 |
| API | Filter candidate registrations by status and examination | Medium | 6 |
| API | Fetch registration detail with payment and document status | Complex | 8 |
| API | Resolve resume draft deep link to correct workflow step | Complex | 8 |
| Database | Registration list query indexes by candidate and status | Easy | 0.25 |
| Testing | Happy-path list and detail for confirmed registration | Medium | 0.3 |
| Testing | Resume draft and retry payment action availability rules | Complex | 0.5 |
| Testing | Cross-candidate registration access denied | Complex | 0.5 |
| Documentation | Candidate my registrations and status meanings guide | Medium | 0.3 |
| Documentation | Registration status vocabulary technical reference | Easy | 0.25 |

### F05-034 Optional Registration Application Verification and Administrator Review Gate

132.6 hours · Optional · 19 tasks

##### Description

Supports optional post-submission registration verification where examination administrators review candidate applications including KGID snapshot, manual details, and competent authority document before approving or rejecting registration for downstream scheduling eligibility.

##### Business objective

Provide controlled administrator verification gate for registrations requiring manual approval without standalone workflow engine module.

##### Actors

- Candidate
- Examination Administrator

##### User journey

1. Candidate completes registration submission (F05-012). 2. If verification enabled, registration status set to pending verification. 3. Candidate sees pending verification status in self-service view. 4. Administrator opens registration verification queue. 5. Administrator reviews application summary, profile data, KGID snapshot or manual details, competent authority document, and payment status. 6. Administrator approves or rejects with reason. 7. On approval, registration status transitions to verified or confirmed eligible for scheduling. 8. On rejection, candidate notified with reason and guidance. 9. Candidate views updated status in portal.

##### Functional capabilities

- Post-submit pending verification status assignment when enabled
- Administrator registration verification queue list
- Administrator application detail review screen
- Competent authority document review in verification context
- Approve registration action with audit
- Reject registration action with mandatory reason
- Candidate pending and outcome status visibility
- Verification outcome notification trigger

##### Inputs

- Submitted registration
- Administrator approve or reject action
- Rejection reason text

##### Outputs

- Updated registration verification status
- Verification audit record
- Candidate notification

##### Business rules

- Verification optional and configurable per examination or globally
- Rejected registrations not eligible for Module 06 scheduling until remediated per policy
- Administrator actions audited
- Competent authority document must be reviewable in verification context

##### Validations

- Approve or reject only by authorised examination administrator
- Rejection reason required on reject
- Verification actions only on pending verification registrations
- Candidate cannot self-approve

##### Workflow

CONFIRMED → PENDING_VERIFICATION → APPROVED or REJECTED; REJECTED → candidate notified; APPROVED → eligible for scheduling handoff to Module 06

##### Search requirements

- Administrator queue search by application number, candidate name, examination, status
- Filter pending verification registrations

##### Documents

- Competent authority document viewed in verification context

##### Notifications

- Verification outcome notification via Module 07

##### Security

- Administrator role required from Module 01
- Verification audit immutable

##### Integrations

- Module 07 — Verification outcome notifications

##### Dependencies

- F05-012 — Registration Confirmation
- F05-006 — Competent authority document
- Module 01 — Examination Administrator Role
- Module 06 — Scheduling eligibility consumes verification outcome

##### Assumptions

- Client confirms whether verification mandatory or disabled at go-live

##### Risks

- Verification backlog delays scheduling
- Inconsistent rejection reasons without structured codes

##### Non-functional requirements

- Verification queue pagination for high registration volume

##### Notes

Embedded optional approval per module notes; enable when client requires application verification before scheduling.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate pending verification status banner on registration detail | Simple | 5 |
| UI | Candidate registration rejected status view with administrator reason | Medium | 16 |
| UI | Administrator registration verification queue list with filters | Complex | 18 |
| UI | Administrator registration verification detail review screen | Very high | 24 |
| UI | Administrator approve registration confirmation dialog | Simple | 5 |
| UI | Administrator reject registration dialog with reason capture | Medium | 16 |
| API | Assign pending verification status on submit when policy enabled | Medium | 6 |
| API | List pending verification registrations for administrator queue | Medium | 6 |
| API | Search and filter verification queue by application and examination | Medium | 6 |
| API | Fetch registration verification detail bundle | Complex | 8 |
| API | Approve registration with audit trail | Complex | 8 |
| API | Reject registration with mandatory reason and audit trail | Complex | 8 |
| Database | Registration verification status and decision audit history | Complex | 0.5 |
| Integration | Verification outcome notification to Module 07 | Simple | 4 |
| Testing | Happy-path administrator approve to eligible status | Complex | 0.5 |
| Testing | Reject with reason and candidate visibility cases | Medium | 0.3 |
| Testing | Unauthorized user and double-decision prevention | Complex | 0.5 |
| Documentation | Administrator registration verification procedure runbook | Complex | 0.5 |
| Documentation | Candidate pending verification and rejection guidance | Medium | 0.3 |

## 06 Examination Scheduling & Allocation

759 hours · 126 tasks · Business

Examination schedule management, candidate-to-centre allocation, hall ticket issuance, and examination credential generation.

### F06-001 Examination Schedule Creation and Maintenance

136.7 hours · Go-live · 25 tasks

##### Description

Enables Examination Administrators to create, maintain, publish, and cancel examination session schedules linked to configured examinations and authorised centres. Each schedule captures session date, start time, duration, reporting time, applicable centre, seat capacity, and candidate-facing instructions. Schedules progress through controlled lifecycle states and become the anchor for downstream allocation, hall ticket, and credential generation.

##### Business objective

Provide authoritative, capacity-aware examination session schedules that govern when and where registered candidates may be allocated and examined, while preventing conflicting or invalid session definitions.

##### Actors

- Examination Administrator

##### User journey

1. Examination Administrator opens the Examination Schedule register from the scheduling menu.
2. Administrator applies filters for examination, centre, session date range, and schedule status (Draft, Published, Cancelled).
3. Administrator selects Create Schedule to open the create form.
4. Administrator selects the target examination from examinations open for scheduling (sourced from Examination Master Configuration).
5. Administrator selects the authorised examination centre from centres active for that examination (sourced from Centre Master).
6. Administrator enters session date, session start time, duration, reporting time, maximum seat capacity for the session, and examination instructions text.
7. System validates centre capacity ceiling, date/time rules, and non-overlapping session constraints for the same centre.
8. Administrator saves the schedule in Draft status.
9. Administrator opens the saved Draft schedule in edit mode to adjust fields before publication.
10. Administrator selects Publish/Finalise; system displays a confirmation dialog summarising session timing, centre, and capacity impact.
11. Administrator confirms publication; schedule transitions to Published and becomes eligible for candidate allocation.
12. For a Published schedule requiring change, Administrator either edits allowed fields per business policy or cancels the schedule with mandatory reason.
13. Administrator opens schedule detail read-only view to audit timing, centre, capacity, status history, and linked allocation counts.
14. When no schedules match filters, Administrator sees empty-state guidance to create the first session schedule.

##### Functional capabilities

- Display paginated examination schedule register with examination, centre, date range, and status filters
- Create draft examination session schedule with examination, centre, date, time, duration, reporting time, seat capacity, and instructions
- Edit draft examination session schedule fields before publication
- Publish/finalise draft schedule after validation of capacity and timing rules
- Cancel/deactivate published or draft schedule with mandatory reason capture
- View read-only schedule detail including status history and allocation summary counts
- Validate session does not exceed configured centre capacity for the examination
- Validate non-overlapping session times for the same centre on the same date
- Prevent publication when mandatory fields or centre-examination authorisation is missing
- Record schedule status transitions with audit metadata

##### Inputs

- Examination identifier (from Examination Master Configuration)
- Authorised examination centre identifier (from Centre Master)
- Session date
- Session start time
- Session duration (minutes)
- Reporting time
- Maximum seat capacity for session
- Examination instructions text
- Cancellation reason (on cancel action)

##### Outputs

- Draft schedule record
- Published schedule record eligible for allocation
- Cancelled schedule record with reason
- Schedule register search results
- Schedule detail view payload
- Schedule status transition audit entries
- Validation error messages for timing, capacity, and overlap conflicts

##### Business rules

- Only authorised examination-centre pairings configured in Centre Management may be scheduled
- Session seat capacity cannot exceed centre capacity configured for the examination
- Published schedules cannot be deleted; they may only be cancelled with reason
- Hall ticket and credential generation require Published schedule status (enforced in downstream features)
- Session date and start time must be in the future at time of publication unless administrator override policy allows same-day (configurable assumption)
- Reporting time must precede or equal session start time
- Cancelled schedules exclude new candidate allocations but retain historical audit

##### Validations

- Examination selection is mandatory and must reference an active examination open for scheduling
- Centre selection is mandatory and must be authorised for the selected examination
- Session date is mandatory and must be a valid calendar date
- Session start time is mandatory and valid 24-hour time format
- Duration is mandatory, positive integer minutes within configured min/max bounds
- Reporting time is mandatory and must not be after session start time
- Seat capacity is mandatory, positive integer, and less than or equal to centre capacity for examination
- Instructions text length within configured maximum character limit
- No overlapping Published sessions for same centre where session time ranges intersect
- Cancellation reason mandatory when transitioning Published or Draft to Cancelled

##### Calculations

- Derive session end time from start time plus duration
- Compute remaining allocatable seats as session capacity minus confirmed allocations (display only on detail view)

##### Workflow

Draft → Published (publish/finalise action) | Draft → Cancelled (cancel action) | Published → Cancelled (cancel action). Published schedules are not editable for core timing/centre fields without cancel-and-recreate policy (assumption: material fields locked after publish).

##### Search requirements

- Filter schedule register by examination name or code
- Filter by centre name or code
- Filter by session date range
- Filter by schedule status (Draft, Published, Cancelled)
- Sort by session date, centre, examination, status

##### Reports

- Schedule register export (CSV) for administrative review

##### Security

- Only Examination Administrator role with scheduling permission may create, publish, or cancel schedules
- Centre-scoped invigilator roles have no access to schedule maintenance screens
- All publish and cancel actions logged with administrator identity and timestamp

##### Dependencies

- Module 04 — Examination Master Configuration (examination definitions open for scheduling)
- Module 03 — Authorised Examination Centre Master and Centre Capacity Configuration
- Module 01 — Examination Administrator role and scheduling authorisation permissions

##### Assumptions

- Centre-examination authorisation and raw capacity values are maintained in Module 03
- Examination definitions and scheduling windows are maintained in Module 04
- Material schedule field edits after publication require cancel-and-recreate rather than in-place edit
- Complexity drivers: overlap detection across centre sessions, capacity cross-check against external centre master, and status-locked edit rules

##### Risks

- Late centre capacity changes in Module 03 may invalidate already-published schedules
- Overlapping session detection edge cases across midnight boundaries
- Administrators may publish schedules before registration cutoff causing allocation churn

##### Non-functional requirements

- Schedule register list/search response suitable for enterprise volumes (paginated)
- Audit history retained for compliance review
- Validation feedback field-level on create/edit forms

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination schedule register list with examination, centre, date range, and status filters | Medium | 16 |
| UI | Create examination schedule form with examination and centre dependent selectors | Medium | 16 |
| UI | Edit draft examination schedule form | Medium | 16 |
| UI | Schedule detail read-only view with status history and allocation summary | Easy | 14 |
| UI | Publish/finalise schedule confirmation dialog | Simple | 5 |
| UI | Cancel schedule confirmation dialog with mandatory reason field | Simple | 5 |
| UI | Schedule register empty state when no sessions exist | Simple | 5 |
| UI | Schedule form validation error state for overlap and capacity failures | Easy | 14 |
| UI | Schedule register CSV export action | Simple | 5 |
| API | List and search examination schedules with filters and pagination | Medium | 6 |
| API | Get examination schedule detail with status history | Easy | 4 |
| API | Create draft examination schedule with field and authorisation validation | Medium | 6 |
| API | Update draft examination schedule | Medium | 6 |
| API | Publish/finalise examination schedule with overlap and capacity checks | Complex | 8 |
| API | Cancel examination schedule with reason capture | Easy | 4 |
| API | Lookup examinations open for scheduling | Simple | 2 |
| API | Lookup authorised centres and capacity for selected examination | Simple | 2 |
| Database | Core examination session schedule entity persistence | Medium | 0.3 |
| Database | Schedule status transition audit and history persistence | Easy | 0.25 |
| Database | Centre session overlap constraints and capacity indexes | Complex | 0.5 |
| Testing | Happy-path draft create, edit, publish schedule lifecycle | Medium | 0.3 |
| Testing | Negative cases for capacity exceed, invalid reporting time, and overlap rejection | Medium | 0.3 |
| Testing | Edge and security cases for unauthorised centre, cancel audit, and locked published edits | Complex | 0.5 |
| Documentation | Examination Administrator runbook for schedule creation, publication, and cancellation | Medium | 0.3 |
| Documentation | Technical notes for schedule lifecycle states and overlap validation rules | Easy | 0.25 |

### F06-002 Candidate Centre and Session Allocation

187.75 hours · Go-live · 26 tasks

##### Description

Allocates registered candidates to published examination sessions and authorised centres using captured centre preferences, centre availability, session capacity, examination schedule, candidate category, and department business rules. Supports automated batch allocation with preview, exception handling, manual override, and finalisation that locks allocations for seat assignment and hall ticket generation.

##### Business objective

Fairly and deterministically assign each registered candidate to an examination session and centre consistent with their preferences and operational capacity while preserving an auditable allocation decision trail.

##### Actors

- Examination Administrator
- Candidate

##### User journey

1. Examination Administrator opens the Candidate Allocation workspace for a selected examination.
2. Administrator views the pending allocation register showing registered candidates without finalised allocation.
3. Administrator reviews each candidate's centre preference 1, centre preference 2, candidate category, and registration status.
4. Administrator selects Run Auto-Allocation to open the allocation wizard.
5. Wizard step 1: Administrator confirms target published session schedules and allocation scope (all pending or filtered subset).
6. Wizard step 2: System previews projected allocations showing preference match tier, centre, session, and unallocated exceptions.
7. Administrator confirms execution; system runs allocation batch and records run identifier.
8. Administrator reviews allocation results grid highlighting preference-satisfied, preference-fallback, and unallocated candidates.
9. For exceptions, Administrator opens manual override dialog, selects alternate centre and session, and enters override reason.
10. Administrator re-runs preview for remaining unallocated candidates if needed.
11. Administrator selects Finalise Allocation; confirmation dialog warns that hall ticket generation will require finalised allocation.
12. System transitions batch to Finalised; candidates become locked for centre-session assignment downstream.
13. Candidate logs into portal and opens Registration Status; allotted centre, session date, reporting time, and allocation status display.
14. Candidate sees not-yet-allocated empty state when allocation is pending.

##### Functional capabilities

- Display pending candidate allocation register with preference and category columns
- Filter allocation register by allocation status, category, centre preference, and registration completeness
- Preview automated allocation outcomes before committing batch
- Execute automated allocation applying preference order, capacity, schedule, and category rules
- Display allocation results with preference-match indicator and exception flags
- Manually override individual candidate centre and session assignment with reason
- Reallocate candidate from one finalised assignment to another prior to hall ticket generation lock
- Finalise allocation batch to lock candidate-centre-session mappings
- Expose candidate allotted centre and session on candidate portal registration status
- Record allocation batch run audit with rule version and outcome counts
- Block allocation against non-Published or Cancelled schedules

##### Inputs

- Examination identifier
- Published session schedule identifiers in scope
- Registered candidate identifiers with completed registration
- Centre preference 1 and preference 2 from registration
- Candidate category (Government employee, PSU/Board, etc.)
- Manual override centre identifier
- Manual override session schedule identifier
- Override reason text
- Allocation batch finalise confirmation

##### Outputs

- Candidate-to-centre-to-session allocation record
- Allocation preview result set
- Allocation batch run summary with allocated, fallback, and unallocated counts
- Finalised allocation lock state
- Candidate portal allotted centre and session display
- Exception/unallocated candidate list
- Allocation override audit entries

##### Business rules

- Allocation considers centre preference 1 before preference 2
- Candidate category may restrict eligible centres or sessions per department rules
- Session seat capacity reduced by confirmed allocations cannot be exceeded
- Only candidates with completed registration from Module 05 are eligible
- Finalised allocation required before seat assignment and hall ticket generation
- Manual override requires mandatory reason and administrator permission
- Cancelled schedules exclude new allocations; existing allocations flagged for administrator action

##### Validations

- Examination must have at least one Published session schedule before allocation
- Candidate registration status must be complete and payment satisfied where mandatory
- Manual override centre must be authorised for examination
- Manual override session must be Published and have remaining capacity
- Override reason mandatory and within maximum length
- Cannot finalise allocation batch while unallocated candidates remain unless administrator confirms force-finalise policy
- Candidate cannot receive duplicate allocation to multiple sessions for same examination
- Preference values must reference active centres at allocation time

##### Calculations

- Compute remaining session capacity during allocation preview and execution
- Derive preference satisfaction tier (Preference 1 matched, Preference 2 matched, Non-preference fallback)
- Count allocated, fallback-allocated, and unallocated candidates per batch run

##### Workflow

Pending → Allocated (auto or manual assignment) → Finalised (finalise batch action) | Allocated → Reallocated (manual override before hall ticket lock) | Finalised → Reopened (administrator reopen policy assumption for pre-hall-ticket corrections only).

##### Search requirements

- Search candidates in allocation register by name, registration number, mobile
- Filter by allocation status (Pending, Allocated, Finalised, Unallocated exception)
- Filter by candidate category
- Filter by allotted centre or session date
- Sort by preference match tier and registration date

##### Reports

- Allocation batch summary report with preference match statistics
- Unallocated candidate exception export

##### Security

- Only Examination Administrator with allocation permission may run batch, override, or finalise
- Candidates may view only their own allotted centre and session
- Override and batch run actions audit-logged with administrator identity

##### Dependencies

- F06-001 — Published examination session schedules
- Module 05 — Candidate Registration with centre preferences and registration completion status
- Module 03 — Authorised centres and capacity configuration
- Module 04 — Examination Master Configuration and category eligibility rules
- Module 01 — Examination Administrator allocation permissions

##### Assumptions

- Centre preferences captured during Module 05 registration are snapshot-read at allocation time
- Category-based centre restrictions are configurable via examination business rules from Module 04
- Complexity drivers: multi-rule batch engine, preview/commit pattern, and manual override audit
- Force-finalise with unallocated exceptions is policy-gated and off by default

##### Risks

- Preference saturation at popular centres causing high fallback rates
- Concurrent allocation runs against same session may cause capacity race conditions
- Registration data changes after allocation may desynchronise candidate category rules

##### Non-functional requirements

- Batch allocation preview completes within acceptable time for examination-sized candidate volumes
- Allocation decisions fully auditable for grievance review
- Candidate portal allotment view reflects finalised state within normal replication latency

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate allocation workspace landing with examination selector | Easy | 14 |
| UI | Pending allocation register with preference, category, and status columns | Medium | 16 |
| UI | Auto-allocation wizard step for scope and session selection | Medium | 16 |
| UI | Auto-allocation wizard preview step showing projected assignments and exceptions | Complex | 18 |
| UI | Allocation results review grid with preference-match and exception indicators | Medium | 16 |
| UI | Manual allocation override dialog with centre, session, and reason | Medium | 16 |
| UI | Finalise allocation batch confirmation dialog | Simple | 5 |
| UI | Unallocated exceptions list panel | Easy | 14 |
| UI | Candidate portal registration status allotted centre and session display | Easy | 14 |
| UI | Candidate portal allocation pending empty state | Simple | 5 |
| API | List and search candidates pending allocation with filters | Medium | 6 |
| API | Preview automated allocation batch without commit | Complex | 8 |
| API | Execute automated allocation batch with preference and capacity rules | Very high | 12 |
| API | Manual assign or reassign candidate to centre and session | Complex | 8 |
| API | Finalise allocation batch to lock assignments | Complex | 8 |
| API | Get candidate allocation status for administrator register | Easy | 4 |
| API | Get candidate portal allotted centre and session detail | Easy | 4 |
| Database | Candidate centre session allocation core entity persistence | Medium | 0.3 |
| Database | Allocation batch run and outcome audit persistence | Medium | 0.3 |
| Database | Allocation override reason and history persistence | Easy | 0.25 |
| Database | Preference snapshot and capacity reservation indexes | Complex | 0.5 |
| Testing | Happy-path auto-allocation with preference 1 and preference 2 matching | Complex | 0.5 |
| Testing | Negative validation for capacity exceed, incomplete registration, and invalid centre override | Medium | 0.3 |
| Testing | Edge cases for category restrictions, tie-breaking, concurrent batch guard, and finalise lock | Very high | 1 |
| Documentation | Examination Administrator runbook for auto-allocation, override, and finalisation | Medium | 0.3 |
| Documentation | Technical notes for allocation rule precedence and batch audit model | Medium | 0.3 |

### F06-003 Candidate Seat and Computer Assignment

123.55 hours · Go-live · 23 tasks

##### Description

Maps finalised candidate allocations to specific seat or computer identifiers within an examination session at an authorised centre. Supports automated seat assignment, manual reassignment, conflict detection, seating register views, and seat-map lock prior to hall ticket generation.

##### Business objective

Ensure each candidate has a unique, traceable seat or computer assignment within their allotted session to support orderly centre conduct and accurate hall ticket presentation.

##### Actors

- Examination Administrator

##### User journey

1. Examination Administrator opens Seat Assignment for a selected finalised session at a centre.
2. Administrator views the session seating register listing allocated candidates without seat assignment.
3. Administrator selects Auto-Assign Seats to fill available seat or computer identifiers from centre infrastructure configuration.
4. System displays auto-assignment summary showing assigned count and remaining unassigned candidates.
5. Administrator reviews seating list/grid showing candidate name, registration number, seat or computer identifier, and assignment status.
6. For conflicts or special accommodations, Administrator opens manual seat pick dialog and selects an available seat or computer.
7. System validates seat uniqueness and capacity bounds; Administrator saves reassignment with optional reason.
8. Administrator resolves seat conflict dialog when duplicate seat detected.
9. Administrator selects Lock Seat Map when all candidates are assigned; confirmation dialog warns that changes require unlock policy.
10. Locked seat map blocks further auto-assign and displays read-only seating register.
11. Administrator exports seating register for centre coordination.

##### Functional capabilities

- Display session seating register filtered by assignment status
- Auto-assign available seat or computer identifiers to unassigned candidates in a session
- Display seating list or grid with candidate and seat mapping
- Manually assign or reassign seat or computer to individual candidate
- Detect and surface duplicate seat assignment conflicts
- Lock seat map for session to freeze assignments before hall ticket generation
- Unlock seat map under administrator policy for pre-hall-ticket corrections
- Validate seat identifiers against centre infrastructure capacity configuration
- Export session seating register

##### Inputs

- Finalised session schedule identifier
- Centre identifier
- Candidate allocation identifiers within session
- Available seat or computer identifier pool from centre infrastructure
- Manual seat or computer selection
- Reassignment reason text
- Lock seat map confirmation

##### Outputs

- Candidate seat or computer assignment record per session
- Auto-assignment batch summary
- Seating register view data
- Seat map locked status flag
- Seat conflict error detail
- Seating register export file
- Seat assignment change audit entries

##### Business rules

- Seat assignment permitted only after allocation finalisation for the session
- Each seat or computer identifier may be assigned to at most one candidate per session
- Seat identifiers must exist within centre infrastructure capacity defined in Module 03
- Hall ticket generation requires locked seat map when seat/computer assignment is applicable for examination type
- Manual reassignment after lock requires unlock action with audit

##### Validations

- Session must have Finalised candidate allocations before seat assignment
- Seat or computer identifier mandatory on manual assign
- Seat identifier must be within configured centre seat or computer range
- Duplicate seat within same session rejected
- Cannot lock seat map while unassigned candidates remain unless force-lock policy confirmed
- Reassignment reason required when changing assigned seat after initial assignment

##### Calculations

- Count assigned versus unassigned candidates for session
- Compute next available seat identifier during auto-assign sequence

##### Workflow

Unassigned → Assigned (auto or manual assign) → Locked (lock seat map action) | Assigned → Reassigned (manual change before or after unlock) | Locked → Unlocked (administrator unlock for corrections).

##### Search requirements

- Search seating register by candidate name or registration number
- Filter by assignment status (Unassigned, Assigned)
- Filter by seat or computer identifier
- Sort by seat identifier or candidate name

##### Reports

- Session seating register export for centre invigilator coordination

##### Security

- Only Examination Administrator with seat assignment permission may assign or lock seats
- Centre invigilator roles receive read-only seating visibility via Module 08 dependency only
- All lock, unlock, and reassignment actions audit-logged

##### Dependencies

- F06-002 — Finalised candidate centre and session allocation
- Module 03 — Centre Capacity and Infrastructure Configuration (seat or computer inventory)
- F06-001 — Published session schedule context
- Module 01 — Examination Administrator seat assignment permissions

##### Assumptions

- Seat/computer identifiers are pre-configured numeric or labelled inventory in Module 03
- Examinations not requiring computer assignment still use seat numbering from same inventory model
- Complexity drivers: uniqueness enforcement, lock/unlock governance, and auto-assign sequencing

##### Risks

- Centre infrastructure changes after seat lock may invalidate assignments
- Auto-assign ordering may not respect special accommodation needs without manual override

##### Non-functional requirements

- Auto-assign completes for full session candidate count within operational time limits
- Seating register supports centre-scale candidate volumes with pagination

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Session seat assignment register with assignment status filters | Medium | 16 |
| UI | Auto-assign seats action panel with scope selection | Easy | 14 |
| UI | Seating list grid showing candidate and seat or computer mapping | Medium | 16 |
| UI | Manual seat pick dialog with available seat selector | Medium | 16 |
| UI | Seat conflict resolution dialog for duplicate assignment | Simple | 5 |
| UI | Lock seat map confirmation dialog | Simple | 5 |
| UI | Unlock seat map confirmation dialog for corrections | Simple | 5 |
| UI | Seating register empty state when no finalised allocations exist | Simple | 5 |
| UI | Seating register CSV export action | Simple | 5 |
| API | List session seat assignments with search and filters | Medium | 6 |
| API | Auto-assign seats for session from centre inventory pool | Complex | 8 |
| API | Manual assign or reassign seat or computer to candidate | Medium | 6 |
| API | Lock seat map for session | Easy | 4 |
| API | Unlock seat map for session under policy | Easy | 4 |
| API | Validate seat uniqueness and inventory bounds | Medium | 6 |
| Database | Candidate seat or computer assignment entity persistence | Medium | 0.3 |
| Database | Session seat map lock state persistence | Simple | 0.1 |
| Database | Seat assignment change history and uniqueness constraints | Complex | 0.5 |
| Testing | Happy-path auto-assign, manual assign, and lock seat map | Medium | 0.3 |
| Testing | Negative cases for duplicate seat, out-of-range identifier, and lock with unassigned | Medium | 0.3 |
| Testing | Edge cases for unlock reassignment audit and concurrent assign attempts | Complex | 0.5 |
| Documentation | Examination Administrator runbook for seat assignment and seat map lock | Medium | 0.3 |
| Documentation | Technical notes for seat uniqueness rules and lock prerequisites | Easy | 0.25 |

### F06-004 Digital Hall Ticket Generation and Candidate Access

156.75 hours · Go-live · 27 tasks

##### Description

Generates digital hall tickets for candidates after examination scheduling, centre allocation finalisation, and seat assignment prerequisites are satisfied. Provides Examination Administrator batch generation, regeneration, and status monitoring plus Candidate portal view, download, and print access to hall tickets containing examination, session, centre, reporting time, and seat details.

##### Business objective

Deliver authoritative, tamper-evident hall tickets digitally so candidates know exactly when, where, and how to report for their allotted examination session.

##### Actors

- Examination Administrator
- Candidate

##### User journey

1. Examination Administrator opens Hall Ticket Generation console for a selected examination.
2. System displays prerequisite checklist: Published schedules, Finalised allocations, Locked seat map (if applicable).
3. Administrator selects Generate Hall Tickets for scope (examination, session, or centre subset).
4. System queues generation batch and displays progress register.
5. Administrator opens sample hall ticket preview for template verification.
6. Upon completion, Administrator reviews generation status register showing success, failed, and pending rows per candidate.
7. For individual candidate detail changes, Administrator opens Regenerate Hall Ticket dialog with reason.
8. Candidate logs into portal and navigates to Hall Ticket section.
9. If prerequisites not met, Candidate sees not-yet-available message explaining pending scheduling or allocation.
10. When eligible, Candidate views hall ticket page showing candidate name, examination name, session date, reporting time, centre name and address, seat or computer number, and instructions.
11. Candidate selects Download PDF to save hall ticket document.
12. Candidate selects Print to open print-friendly view.
13. If generation failed for candidate, Administrator retries from failed queue row.

##### Functional capabilities

- Display hall ticket generation console with prerequisite checklist
- Trigger batch hall ticket generation for eligible candidates
- Monitor hall ticket generation job status per candidate
- Preview hall ticket document template with sample data
- Regenerate hall ticket for individual candidate with reason and version increment
- Retry failed hall ticket generation for candidate
- Determine candidate hall ticket eligibility based on scheduling and allocation state
- Display candidate hall ticket detail on portal
- Provide candidate hall ticket PDF download
- Provide candidate hall ticket print view
- Display not-eligible empty and error states on candidate portal
- Record hall ticket document storage reference and generation audit

##### Inputs

- Examination identifier
- Session schedule identifier scope
- Centre identifier scope
- Candidate identifier for regeneration
- Regeneration reason text
- Candidate authenticated portal session

##### Outputs

- Generated hall ticket PDF document per candidate
- Hall ticket generation batch status records
- Candidate portal hall ticket display payload
- Hall ticket eligibility boolean with reason codes
- Hall ticket version history on regeneration
- Failed generation error detail for administrator retry

##### Business rules

- Hall ticket generation blocked until candidate allocation is Finalised
- Hall ticket generation blocked until session schedule is Published
- When seat assignment applies, hall ticket generation blocked until seat map is Locked
- Regeneration supersedes prior hall ticket version; prior version retained in audit history
- Candidate may access only their own hall ticket
- Hall ticket must reflect final allotted centre, not merely preference
- Failed generation rows remain retryable without duplicating successful tickets

##### Validations

- Prerequisite checklist must pass before batch generation accepted
- Candidate must belong to generation scope examination
- Regeneration reason mandatory on administrator regenerate action
- Portal hall ticket request rejected when eligibility prerequisites unmet
- Download allowed only for successfully generated current version
- Candidate portal session must match hall ticket owner candidate identifier

##### Calculations

- Derive hall ticket eligibility from composite schedule, allocation, and seat lock states
- Increment hall ticket version number on regeneration

##### Workflow

Not Eligible → Eligible (prerequisites satisfied) → Generation Pending → Generated (success) | Generation Pending → Failed (error) → Generation Pending (retry) | Generated → Superseded (regeneration creates new current version).

##### Search requirements

- Administrator search generation register by candidate name, registration number, status
- Filter by examination, session date, centre, generation status
- Sort by generation timestamp and status

##### Documents

- Hall ticket PDF document with examination, centre, session, reporting time, seat, and instructions
- Print-friendly hall ticket render

##### Reports

- Hall ticket generation batch summary with success and failure counts

##### Security

- Candidate hall ticket access restricted to authenticated owner
- Hall ticket PDF served through authorised download token or session check
- Administrator regeneration and batch actions audit-logged
- Hall ticket document storage access limited to application document service

##### Integrations

- Internal document rendering service for PDF hall ticket generation

##### Dependencies

- F06-001 — Published examination session schedules
- F06-002 — Finalised candidate centre and session allocation
- F06-003 — Locked seat or computer assignment when applicable
- Module 05 — Candidate identity and registration details for hall ticket content
- Module 03 — Centre name and address for hall ticket display
- Module 04 — Examination name and instructions configuration
- Module 01 — Candidate portal authentication and administrator hall ticket permissions

##### Assumptions

- PDF template layout approved by department; branding fields supplied from configuration
- Document storage uses platform blob storage pattern
- Complexity drivers: prerequisite gating chain, batch generation monitoring, and PDF render integration

##### Risks

- Late allocation or seat changes after generation require mass regeneration
- PDF generation failures at scale may delay candidate access close to exam date
- Candidate downloads from shared devices pose informational disclosure risk mitigated by authentication

##### Non-functional requirements

- Batch generation supports examination-wide candidate volumes asynchronously
- PDF download responsive for candidate portal usage
- Generated documents retained per records retention policy

##### Notes

Hall ticket availability requires completed scheduling, finalised allocation, and locked seat map where seat assignment applies.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Hall ticket generation console with prerequisite checklist display | Medium | 16 |
| UI | Hall ticket generation batch progress and status register | Medium | 16 |
| UI | Hall ticket template preview dialog with sample candidate data | Easy | 14 |
| UI | Regenerate single candidate hall ticket dialog with reason | Simple | 5 |
| UI | Failed hall ticket generation retry action row control | Simple | 5 |
| UI | Candidate portal hall ticket detail view page | Medium | 16 |
| UI | Candidate portal hall ticket download PDF action | Easy | 14 |
| UI | Candidate portal hall ticket print-friendly view | Easy | 14 |
| UI | Candidate portal hall ticket not-yet-available empty state | Simple | 5 |
| UI | Candidate portal hall ticket generation failed error state | Simple | 5 |
| API | Evaluate candidate hall ticket eligibility with reason codes | Medium | 6 |
| API | Queue batch hall ticket generation for eligible candidates | Complex | 8 |
| API | List hall ticket generation status with filters | Medium | 6 |
| API | Regenerate hall ticket for single candidate with versioning | Medium | 6 |
| API | Retry failed hall ticket generation for candidate | Easy | 4 |
| API | Get candidate portal hall ticket display data | Easy | 4 |
| API | Download candidate hall ticket PDF document | Medium | 6 |
| Database | Hall ticket record with document reference and version persistence | Medium | 0.3 |
| Database | Hall ticket generation batch job status persistence | Easy | 0.25 |
| Database | Hall ticket regeneration history and audit persistence | Easy | 0.25 |
| Integration | Internal PDF document rendering service call for hall ticket template | Simple | 4 |
| Testing | Happy-path batch generation, candidate view, download, and print | Medium | 0.3 |
| Testing | Negative cases for blocked generation when allocation or seat lock missing | Medium | 0.3 |
| Testing | Edge and security cases for cross-candidate access denial, regeneration versioning, and retry | Complex | 0.5 |
| Documentation | Examination Administrator runbook for hall ticket batch generation and regeneration | Medium | 0.3 |
| Documentation | Candidate user guide for hall ticket download and print | Easy | 0.25 |
| Documentation | Technical notes for eligibility gating and document version model | Medium | 0.3 |

### F06-005 Examination Credential Generation and Secure Distribution Handoff

154.25 hours · Go-live · 25 tasks

##### Description

Generates unique examination login identifiers and passwords for candidates after schedule finalisation and eligible allocation state. Stores credentials securely, exposes administrator batch generation and regeneration controls, and hands off masked credential dispatch requests to the Notification Service via approved SMS and email channels without exposing plaintext passwords in administrative list views.

##### Business objective

Ensure each candidate receives unique, secure examination login credentials through approved communication channels only after scheduling and allocation are complete, enabling examination day login without administrator manual password handling.

##### Actors

- Examination Administrator
- Candidate

##### User journey

1. Examination Administrator opens Examination Credential Generation console for a selected examination.
2. System displays eligibility checklist: Published schedules, Finalised allocations, and schedule finalisation policy satisfied.
3. Administrator selects Generate Credentials for candidate scope.
4. System generates unique examination login ID and random password per eligible candidate, stores password using secure hashing, and queues credential records.
5. Administrator views credential generation status register showing generated, pending dispatch, dispatched, and failed rows with masked secret display only.
6. Administrator selects Initiate Distribution Handoff for batch; system publishes secure dispatch payload to Notification Service without logging plaintext password.
7. Module 07 dispatches SMS and/or email to candidate using configured templates; this feature records handoff correlation identifier and dispatch status callbacks.
8. For compromised or undelivered credentials, Administrator opens Regenerate Credentials dialog; system invalidates prior credential and creates new pair.
9. Administrator triggers Resend Distribution Handoff for individual candidate to Notification Service.
10. Candidate receives login ID and password via SMS/email from Notification Service (outside this feature UI).
11. Candidate uses credentials at examination login (Module 09 scope); this feature does not provide conduct interface.

##### Functional capabilities

- Display credential generation console with schedule finalisation eligibility checklist
- Generate unique examination login ID and password batch for eligible candidates
- Store examination password using secure one-way hashing
- Display credential generation and dispatch status register with masked secrets
- Initiate secure distribution handoff batch to Notification Service
- Receive and persist dispatch status callback updates from Notification Service
- Regenerate credentials for individual candidate invalidating prior active credential
- Trigger resend distribution handoff for individual candidate
- Block credential generation until schedule finalisation and allocation prerequisites met
- Audit all generate, regenerate, and handoff actions without plaintext password retention in logs

##### Inputs

- Examination identifier
- Published session schedule finalisation confirmation
- Candidate identifiers in eligible scope
- Regenerate credentials reason text
- Resend dispatch handoff confirmation
- Notification template routing identifiers from Module 07
- Dispatch status callback payload from Notification Service

##### Outputs

- Examination login ID per candidate
- Securely hashed examination password record
- Credential generation batch status
- Distribution handoff request with correlation identifier
- Dispatch status per candidate (Pending, Dispatched, Failed)
- Regenerated credential pair with prior credential invalidated flag
- Administrator masked credential status view

##### Business rules

- Credential generation permitted only after examination schedule finalisation policy is satisfied and allocations are Finalised
- Each candidate receives one active examination credential set per examination attempt
- Plaintext password shown only transiently during generation handoff to Notification Service, never in administrator registers
- Regeneration invalidates previous login password pair immediately
- Resend handoff uses current active credential without regenerating unless administrator explicitly regenerates
- Examination conduct login validation is out of scope; credentials prepared for Module 09 consumption

##### Validations

- Eligibility checklist must pass before batch generation accepted
- Login ID must be unique within examination scope
- Generated password meets configured complexity and length rules
- Regenerate reason mandatory on administrator regenerate action
- Handoff blocked when candidate missing registered mobile or email required by channel policy
- Resend allowed only when active credential exists
- Dispatch callback correlation identifier must match existing handoff record

##### Calculations

- Generate random password meeting complexity policy
- Derive credential eligibility from schedule finalisation and allocation composite state

##### Workflow

Not Eligible → Eligible (prerequisites met) → Generated (credential created) → Handoff Pending (dispatch request queued) → Dispatched (Notification Service success callback) | Handoff Pending → Handoff Failed (callback failure) → Handoff Pending (resend) | Generated → Invalidated (regenerate action) → Generated (new active credential).

##### Search requirements

- Administrator search credential register by candidate name, registration number, login ID
- Filter by generation status, dispatch status, examination, session
- Sort by generation timestamp and dispatch status

##### Reports

- Credential generation and dispatch status summary export for examination readiness review

##### Notifications

- Examination credential dispatch handoff event to Module 07 for SMS delivery
- Examination credential dispatch handoff event to Module 07 for email delivery
- Credential regeneration notification handoff when policy requires informing candidate

##### Security

- Passwords stored hashed; plaintext never persisted in database or audit tables
- Administrator views show login ID and masked password indicator only
- Handoff payload encrypted in transit to Notification Service
- Regenerate and handoff actions restricted to Examination Administrator credential permission
- Rate limit resend handoff to prevent abuse

##### Integrations

- Module 07 Notification Service secure credential dispatch handoff API
- Module 07 dispatch status callback ingestion

##### Dependencies

- F06-001 — Published and finalised examination session schedules
- F06-002 — Finalised candidate allocation
- Module 07 — Notification Template Catalog, channel configuration, and dispatch engine
- Module 05 — Candidate registered mobile and email contact points
- Module 01 — Examination Administrator credential management permissions
- Module 09 — Secure Examination Conduct consumes generated credentials at login time

##### Assumptions

- Notification Service owns template wording and channel provider delivery
- Schedule finalisation for credentials aligns with Published schedule state plus optional administrator explicit finalisation flag
- Complexity drivers: secure secret handling, handoff idempotency, and dispatch status callback reconciliation

##### Risks

- Credential delivery failure leaves candidates without login details near examination time
- Regeneration after dispatch may confuse candidates receiving multiple messages
- Misconfigured Notification templates may expose credentials improperly if template not masked

##### Non-functional requirements

- Batch credential generation completes for examination-wide volumes
- Handoff processing idempotent to avoid duplicate SMS/email sends
- Credential hash algorithm meets organisational security standards

##### Notes

Credential plaintext distribution executed by Module 07 Notification Service; this feature generates credentials and hands off secure dispatch requests.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination credential generation console with eligibility checklist | Medium | 16 |
| UI | Credential generation and dispatch status register with masked secrets | Medium | 16 |
| UI | Generate credentials batch confirmation dialog | Simple | 5 |
| UI | Regenerate candidate credentials dialog with mandatory reason | Simple | 5 |
| UI | Initiate distribution handoff batch confirmation dialog | Simple | 5 |
| UI | Resend distribution handoff single candidate confirmation dialog | Simple | 5 |
| UI | Credential register empty state when prerequisites unmet | Simple | 5 |
| UI | Dispatch failed error state row with retry handoff action | Easy | 14 |
| API | Evaluate credential generation eligibility with reason codes | Medium | 6 |
| API | Generate examination login ID and password batch with hashing | Complex | 8 |
| API | List credential generation and dispatch status with filters | Medium | 6 |
| API | Regenerate single candidate credentials invalidating prior active set | Complex | 8 |
| API | Initiate secure distribution handoff batch to Notification Service | Complex | 8 |
| API | Resend secure distribution handoff for single candidate | Medium | 6 |
| API | Ingest dispatch status callback from Notification Service | Medium | 6 |
| Database | Examination credential record with hashed password persistence | Medium | 0.3 |
| Database | Credential generation batch and invalidation history persistence | Easy | 0.25 |
| Database | Distribution handoff correlation and dispatch status persistence | Medium | 0.3 |
| Integration | Notification Service secure credential dispatch handoff publish | Medium | 16 |
| Integration | Notification Service dispatch status callback mapping and retry handling | Medium | 16 |
| Testing | Happy-path credential generate, handoff, and dispatch status update | Medium | 0.3 |
| Testing | Negative validation for missing contact channel, weak password policy, and blocked prerequisites | Medium | 0.3 |
| Testing | Edge and security cases for regenerate invalidation, masked admin views, idempotent handoff, and hash storage | Very high | 1 |
| Documentation | Examination Administrator runbook for credential generation, handoff, and resend | Medium | 0.3 |
| Documentation | Technical security notes for hashing, handoff payload, and callback reconciliation | Complex | 0.5 |

## 07 Notification Service

931.35 hours · 154 tasks · Platform

Configurable multi-channel notifications for registration, scheduling, conduct, results, and certificate lifecycle events.

### F07-001 Notification Template Catalog and Content Management

127.1 hours · Go-live · 23 tasks

##### Description

Examination Administrators configure reusable notification templates for each examination lifecycle event and delivery channel (SMS, email, in-app/portal). Templates define subject lines, message bodies, supported placeholder tokens, active status, and channel-specific variants so downstream dispatch can render consistent messages for registration confirmation, payment confirmation, schedule and allocation updates, hall ticket availability, examination reminders, credentials issuance, results publication, and certificate availability.

##### Business objective

Centralise configurable message content for all examination lifecycle notifications so message wording can be updated without code changes and each event-channel combination has a governed, auditable template before any outbound send occurs.

##### Actors

- Examination Administrator
- System Notification Service

##### User journey

1. Examination Administrator opens Notification Templates from examination administration settings.
2. Administrator views the template register filtered by lifecycle event type, channel, and active status.
3. Administrator selects Create Template.
4. Administrator chooses lifecycle event type (registration confirmation, payment confirmation, schedule update, allocation update, hall ticket available, examination reminder, credentials issued, results published, certificate available).
5. Administrator selects target channel (SMS, email, in-app/portal).
6. Administrator enters template name, optional description, email subject (email channel only), and message body with placeholder tokens from the reference panel.
7. Administrator saves; system validates uniqueness of event-type plus channel combination and placeholder syntax.
8. Administrator opens Preview, supplies sample candidate and examination values, and reviews rendered output per channel rules.
9. Administrator returns to register, edits an existing template to revise wording, and saves a new version while prior send history remains linked to earlier content snapshots.
10. Administrator deactivates an obsolete template after confirming no active event mapping depends on it (dependency check surfaced in confirmation dialog).
11. If register load fails, administrator sees error state with retry; if no templates exist, empty state prompts first template creation.

##### Functional capabilities

- Display paginated notification template register with event type, channel, name, active status, and last modified metadata
- Filter template register by lifecycle event type, channel, and active/inactive status
- Create notification template bound to one lifecycle event type and one channel
- Edit notification template content and metadata without deleting historical send references
- Deactivate notification template while retaining audit and delivery history
- Show placeholder token reference panel listing permitted tokens for selected event type
- Preview rendered template output using administrator-supplied sample placeholder values
- Validate unique active template per event-type and channel combination
- Validate mandatory subject line for email channel templates
- Validate message body length limits per channel policy
- Reject unknown or malformed placeholder tokens at save time
- Expose template register empty state and load-failure error state

##### Inputs

- Template name
- Template description
- Lifecycle event type selection
- Channel selection (SMS, email, in-app/portal)
- Email subject line (email channel)
- Message body with placeholder tokens
- Active flag
- Sample placeholder values for preview

##### Outputs

- Template register list rows
- Template detail record
- Rendered preview text per channel
- Validation error messages for duplicate or invalid templates
- Deactivation confirmation outcome
- Template version audit entries

##### Business rules

- Only one active template may exist per lifecycle event type and channel combination
- Deactivated templates cannot be selected for new event mappings but remain referenced by historical deliveries
- SMS templates must comply with configured maximum character length
- Email templates require non-empty subject and body
- In-app/portal templates store title and body suitable for inbox display
- Placeholder tokens must belong to the approved catalog for the selected event type
- Examination Administrator role is required for all template management actions

##### Validations

- Template name required; maximum 120 characters
- Lifecycle event type required; must be from approved examination lifecycle catalog
- Channel required; must be SMS, email, or in-app/portal
- Email subject required when channel is email; maximum 200 characters
- Message body required; minimum 1 non-whitespace character
- SMS body must not exceed configured character limit (validated at save)
- Placeholder tokens must match pattern {{token_name}} and exist in event-type token catalog
- Duplicate active event-type plus channel combination rejected on create and on activate
- Deactivation blocked when template is the sole active mapping for a subscribed event unless force-deactivate with warning

##### Calculations

- Preview rendering substitutes each {{token}} with supplied sample value or empty string when sample omitted
- SMS preview displays character count against configured limit

##### Workflow

DRAFT (on create before first save) → ACTIVE (saved and enabled) → INACTIVE (deactivated by administrator). ACTIVE → ACTIVE on content edit (version incremented). INACTIVE templates cannot transition to dispatch use without reactivation through edit save.

##### Search requirements

- Search templates by template name partial match
- Filter by lifecycle event type
- Filter by channel
- Filter by active or inactive status
- Sort by last modified date descending default

##### Security

- Restrict template management to Examination Administrator permissions from User and Role Management
- Audit log every create, update, deactivate, and preview action with administrator identity and timestamp
- Do not expose provider credentials on template screens

##### Dependencies

- F01 Platform Role and Permission Catalog — administrator authorization for template screens
- F01 Examination Administrator Account Lifecycle — authenticated administrator sessions
- F07-003 Examination Lifecycle Event Subscription and Template Routing — consumes templates via event mappings

##### Assumptions

- Final placeholder token catalog per event type will be confirmed during requirements workshops
- Channel-specific length limits for SMS will be supplied by selected SMS gateway constraints
- Template content localisation to multiple languages is out of scope unless added later

##### Risks

- Administrators may embed incorrect placeholders causing blank fields in live messages
- Deactivating widely used templates without updating event mappings may suppress notifications

##### Non-functional requirements

- Template register loads within 2 seconds for up to 500 templates
- Preview rendering completes within 1 second for standard templates
- All template changes must be auditable for compliance review

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Notification template register list with event type, channel, and active status filters | Easy | 14 |
| UI | Template register empty state when no templates exist | Simple | 5 |
| UI | Create notification template form with channel selector and subject/body fields | Medium | 16 |
| UI | Edit notification template form with last-modified metadata | Medium | 16 |
| UI | Placeholder token reference panel on template create and edit forms | Easy | 14 |
| UI | Deactivate template confirmation dialog with active mapping warning | Simple | 5 |
| UI | Template preview dialog with sample candidate and examination values | Medium | 16 |
| UI | Template register load failure error state with retry action | Simple | 5 |
| API | List and search notification templates with event, channel, and status filters | Medium | 6 |
| API | Get notification template detail by identifier | Easy | 4 |
| API | Create notification template with unique event-channel validation | Medium | 6 |
| API | Update notification template content and metadata with version increment | Medium | 6 |
| API | Deactivate notification template without deleting delivery history references | Easy | 4 |
| API | Preview rendered template with supplied placeholder sample values | Medium | 6 |
| API | List supported placeholder tokens for selected lifecycle event type | Simple | 2 |
| Database | Notification template core entity persistence | Simple | 0.1 |
| Database | Per-channel template content variant persistence | Easy | 0.25 |
| Database | Template change audit history persistence | Medium | 0.3 |
| Testing | Happy-path template create, edit, preview, and deactivate flows | Medium | 0.3 |
| Testing | Duplicate event-type plus channel active template rejection | Medium | 0.3 |
| Testing | Invalid placeholder syntax and missing email subject validation cases | Medium | 0.3 |
| Documentation | Examination Administrator notification template management runbook | Medium | 0.3 |
| Documentation | Technical placeholder token catalog and rendering rules | Easy | 0.25 |

### F07-002 SMS Email and In-App Channel Provider Configuration

152.4 hours · Go-live · 23 tasks

##### Description

Examination Administrators configure and maintain outbound channel providers for SMS, email, and in-app/portal notifications. Settings include gateway endpoints, sender identities, credential storage, TLS options, default retention for in-app messages, channel enablement flags, and test-send capability so each channel can be validated before lifecycle notifications are dispatched.

##### Business objective

Provide governed, secure configuration of multi-channel delivery infrastructure so examination lifecycle notifications can be sent reliably through department-approved SMS and email providers and surfaced in the candidate portal without embedding credentials in application code.

##### Actors

- Examination Administrator
- System Notification Service

##### User journey

1. Examination Administrator opens Channel Configuration under notification administration.
2. Administrator views read-only summary showing SMS, email, and in-app channel status (enabled/disabled, last test result).
3. Administrator selects Configure SMS.
4. Administrator enters gateway URL, sender ID, API credentials, and timeout settings; masked fields hide existing secrets.
5. Administrator saves SMS configuration; system validates mandatory fields and connectivity parameters format.
6. Administrator opens Test Send dialog, enters test mobile number, sends test SMS, and views success or failure message with provider response snippet.
7. Administrator selects Configure Email.
8. Administrator enters SMTP host, port, TLS mode, username, password, from-name, and from-address.
9. Administrator saves and runs email test send to a supplied test mailbox.
10. Administrator selects Configure In-App Channel and sets default inbox retention days and display title prefix.
11. Administrator disables a channel via confirmation dialog when maintenance is required; enabled channels resume after re-enable without data loss.
12. On validation failure, inline field errors and banner explain missing or invalid settings.

##### Functional capabilities

- Display channel configuration summary for SMS, email, and in-app channels
- Capture and update SMS gateway provider settings with credential masking on display
- Capture and update email SMTP settings including TLS and sender identity
- Capture and update in-app notification default retention and display settings
- Execute test send per channel with administrator-supplied test recipient
- Enable or disable each channel independently for outbound dispatch
- Validate host, port, email address, and mobile number formats before save or test
- Persist encrypted credentials separate from non-secret connection metadata
- Record last test send outcome and timestamp per channel

##### Inputs

- SMS gateway URL
- SMS sender ID
- SMS API key or credentials
- SMS request timeout
- SMTP host and port
- SMTP TLS mode
- SMTP username and password
- Email from name and from address
- In-app default retention days
- In-app display title prefix
- Test recipient mobile number
- Test recipient email address
- Channel enable/disable flag

##### Outputs

- Channel configuration summary
- Per-channel configuration detail with masked secrets
- Test send success or failure result with provider response code
- Validation errors for invalid connection settings
- Channel enabled/disabled status

##### Business rules

- At least one channel should remain enabled for production go-live (warning only, not hard block)
- Disabled channels must not be used for new dispatch attempts
- Credentials never returned in clear text after initial save
- Test send uses current saved configuration even if changed fields not yet saved (prompt to save first)
- Only Examination Administrator may view or change provider credentials

##### Validations

- SMS gateway URL required; must be valid HTTPS URL
- SMS sender ID required; alphanumeric length per gateway policy
- SMS API credential required on first save
- SMTP host required; valid hostname or IP
- SMTP port required; integer 1–65535
- From email address required; valid RFC email format
- Test mobile number required for SMS test; valid national mobile format
- Test email required for email test; valid RFC email format
- In-app retention days required; integer minimum 1 maximum 365

##### Workflow

CONFIGURED (settings saved) ↔ ENABLED (channel active for dispatch) ↔ DISABLED (channel inactive). Test send does not change workflow state but updates last_test_status metadata.

##### Security

- Encrypt provider credentials at rest
- Mask credential fields in UI and API responses
- Audit all configuration changes and test send actions
- Restrict access to Examination Administrator role

##### Integrations

- SMS gateway provider for connectivity test and live send
- SMTP mail server for connectivity test and live send

##### Dependencies

- F01 Platform Role and Permission Catalog — administrator authorization
- F01 Examination Administrator Account Lifecycle — authenticated sessions
- F07-004 Multi-Channel Notification Dispatch Engine — consumes channel settings for outbound send

##### Assumptions

- Department will nominate single primary SMS gateway and SMTP service for initial go-live
- Exact SMS gateway API shape will be finalised during integration confirmation
- Failover across multiple SMS providers is out of scope

##### Risks

- Incorrect SMTP TLS settings may block all email notifications until corrected
- Credential rotation requires administrator coordination to avoid dispatch outages

##### Non-functional requirements

- Configuration save completes within 2 seconds
- Test send returns result within 30 seconds or times out with clear error
- Credential encryption meets department security baseline

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Channel configuration summary overview for SMS, email, and in-app status | Easy | 14 |
| UI | SMS gateway provider configuration form with masked credential fields | Medium | 16 |
| UI | Email SMTP and sender identity configuration form | Medium | 16 |
| UI | In-app portal notification channel settings form | Easy | 14 |
| UI | Per-channel test send dialog with recipient input | Easy | 14 |
| UI | Channel enable disable confirmation dialog | Simple | 5 |
| UI | Channel configuration validation error banner and field errors | Simple | 5 |
| API | List channel configuration records | Easy | 4 |
| API | Get channel configuration detail by channel type with secret masking | Easy | 4 |
| API | Update SMS provider settings with encrypted credential storage | Medium | 6 |
| API | Update email channel settings with TLS and sender validation | Medium | 6 |
| API | Update in-app channel retention and display settings | Easy | 4 |
| API | Execute test send for selected channel | Medium | 6 |
| API | Enable or disable outbound channel without deleting configuration | Easy | 4 |
| Database | Channel provider configuration persistence | Easy | 0.25 |
| Database | Encrypted credential and connection parameter constraints | Complex | 0.5 |
| Integration | SMS gateway connectivity handshake for test send | Medium | 16 |
| Integration | SMTP server authentication handshake for test send | Medium | 16 |
| Testing | Happy-path save configuration and successful test send per channel | Complex | 0.5 |
| Testing | Invalid host, port, credential, and sender address rejection cases | Medium | 0.3 |
| Testing | Disabled channel blocks new dispatch enqueue for that channel | Medium | 0.3 |
| Documentation | Administrator channel provider setup runbook | Medium | 0.3 |
| Documentation | Technical credential storage and rotation notes | Easy | 0.25 |

### F07-003 Examination Lifecycle Event Subscription and Template Routing

255.95 hours · Go-live · 32 tasks

##### Description

The notification service subscribes to domain events emitted by registration, scheduling, conduct, results, and certificate modules, maps each event type to configured templates and channels, and enqueues dispatch jobs. Supported events include registration confirmation, payment confirmation, schedule updates, centre allocation updates, hall ticket availability, examination reminders, examination credentials issuance, results publication, and certificate availability. Administrators maintain event-to-template routing rules and monitor the inbound dispatch intake queue.

##### Business objective

Automate examination lifecycle notifications by reacting to authoritative business events from upstream modules without duplicating their approval or business logic, ensuring the correct template reaches the correct candidate channels whenever a lifecycle milestone occurs.

##### Actors

- Examination Administrator
- System Notification Service
- Candidate Registration module
- Examination Scheduling and Allocation module
- Secure Examination Conduct module
- Evaluation and Results module
- Certificate Management module

##### User journey

1. Examination Administrator opens Event Notification Mappings.
2. Administrator views mapping register filtered by lifecycle domain (registration, scheduling, conduct, results, certificate) and active status.
3. Administrator selects Create Mapping.
4. Administrator picks domain event type (e.g., payment confirmation, hall ticket available).
5. Administrator selects one or more channels and linked active templates with priority order when multiple channels apply.
6. Administrator saves mapping; system validates template availability and channel enablement.
7. When Candidate Registration completes registration, upstream module emits registration confirmation event with candidate contact details and registration number.
8. Notification service receives event, verifies idempotency key, resolves mapping, and enqueues per-channel dispatch jobs.
9. When payment succeeds, payment confirmation event triggers mapped templates similarly.
10. Scheduling module emits schedule update or allocation update events after administrator actions; service enqueues notifications without re-evaluating allocation logic.
11. Hall ticket generation emits hall ticket available event; service notifies candidate via configured channels.
12. Conduct module emits examination reminder and credentials issued events prior to session.
13. Results module emits results published event after publication.
14. Certificate module emits certificate available event after generation.
15. Administrator monitors dispatch intake queue for received events, mapping resolution status, and enqueue failures.
16. Unmapped or malformed events appear in queue with error status for investigation.

##### Functional capabilities

- Maintain catalog of examination lifecycle domain event types
- Create event-to-template routing mapping with multi-channel selection
- Edit and deactivate event routing mappings
- Receive registration confirmation domain event and enqueue notifications
- Receive payment confirmation domain event and enqueue notifications
- Receive schedule update domain event and enqueue notifications
- Receive centre allocation update domain event and enqueue notifications
- Receive hall ticket available domain event and enqueue notifications
- Receive examination reminder domain event and enqueue notifications
- Receive examination credentials issued domain event and enqueue notifications
- Receive results published domain event and enqueue notifications
- Receive certificate available domain event and enqueue notifications
- Enforce idempotent processing using upstream event identifier
- Log unmapped event types without dispatch
- Display dispatch intake queue monitor with event type and status filters

##### Inputs

- Domain event type code
- Domain event idempotency key
- Candidate identifier and contact channels (mobile, email)
- Registration number
- Examination name and schedule details
- Allocated centre name and address
- Hall ticket reference
- Examination credentials reference
- Result summary fields permitted for notification
- Certificate reference
- Event occurrence timestamp
- Selected template identifiers per channel
- Channel priority order

##### Outputs

- Event-to-template mapping register rows
- Enqueued dispatch job records per channel
- Idempotent duplicate suppression outcome
- Unmapped event error log entries
- Dispatch intake queue monitor rows

##### Business rules

- Notification service does not decide whether registration, payment, or allocation is approved—it reacts only to emitted events
- Each domain event type may have at most one active routing mapping
- Dispatch enqueue skipped for channels that are globally disabled
- Missing candidate contact channel skips that channel but may still enqueue others
- Duplicate event idempotency key must not create duplicate dispatch jobs
- Events must carry sufficient placeholder data for template rendering or enqueue fails with explicit error

##### Validations

- Event type required; must exist in lifecycle catalog
- Idempotency key required; non-empty string
- Mapping save requires at least one channel with linked active template
- Template channel must match mapping channel selection
- Registration events require registration number and candidate mobile
- Payment confirmation events require payment reference and amount placeholder source
- Hall ticket events require hall ticket download reference token
- Credentials events must not include plaintext password in payload—only notification-safe fields
- Malformed JSON payload rejected with logged error

##### Workflow

Event RECEIVED → MAPPING_RESOLVED → JOBS_ENQUEUED → HANDED_OFF_TO_DISPATCH. Event RECEIVED → UNMAPPED (no active mapping, terminal log). Event RECEIVED → DUPLICATE_SUPPRESSED (idempotency hit, terminal). Event RECEIVED → ENQUEUE_FAILED (validation or missing template, terminal with error detail).

##### Search requirements

- Filter event mappings by lifecycle domain
- Filter event mappings by event type
- Filter dispatch intake queue by event type, status, and received date range
- Search intake queue by registration number

##### Notifications

- Registration confirmation trigger
- Payment confirmation trigger
- Schedule update trigger
- Centre allocation update trigger
- Hall ticket availability trigger
- Examination reminder trigger
- Examination credentials availability trigger
- Results publication trigger
- Certificate availability trigger

##### Security

- Accept domain events only from authenticated internal module publishers
- Do not persist full payment instrument details from payment events
- Credentials events must exclude secrets from stored payload snapshots
- Administrator queue monitor requires Examination Administrator permission

##### Integrations

- Candidate Registration module event publication
- Examination Scheduling and Allocation module event publication
- Secure Examination Conduct module event publication
- Evaluation and Results module event publication
- Certificate Management module event publication

##### Dependencies

- F05 Candidate Registration — emits registration and payment confirmation events
- F06 Examination Scheduling and Allocation — emits schedule, allocation, and hall ticket events
- F09 Secure Examination Conduct — emits reminder and credentials events
- F10 Evaluation and Results — emits results published events
- F11 Certificate Management — emits certificate available events
- F07-001 Notification Template Catalog — templates referenced by mappings
- F07-002 Channel Provider Configuration — channel enablement governs enqueue
- F07-004 Multi-Channel Notification Dispatch Engine — processes enqueued jobs

##### Assumptions

- Upstream modules emit events after their business transactions commit successfully
- Exact event payload fields will be agreed in cross-module technical workshops
- OTP generation for candidate login remains in Candidate Registration module

##### Risks

- Event schema drift between modules may break placeholder resolution
- High-volume schedule bulk updates may spike intake queue requiring operational monitoring

##### Non-functional requirements

- Event intake and enqueue within 3 seconds under normal load
- Idempotency store retained minimum 90 days
- Intake queue monitor supports pagination for 10,000+ rows

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Event-to-template mapping register with lifecycle domain filters | Medium | 16 |
| UI | Create event mapping form with event type, template, and channel priority | Medium | 16 |
| UI | Edit event mapping form | Medium | 16 |
| UI | Event mapping detail read-only view with linked templates | Easy | 14 |
| UI | Deactivate event mapping confirmation dialog | Simple | 5 |
| UI | Dispatch intake queue monitor list with status and event type filters | Complex | 18 |
| API | List examination lifecycle event types catalog | Simple | 2 |
| API | List event-to-template mappings with search filters | Medium | 6 |
| API | Create event-to-template mapping with duplicate prevention | Medium | 6 |
| API | Update event-to-template mapping channels and priority | Medium | 6 |
| API | Deactivate event-to-template mapping | Easy | 4 |
| API | Intake registration confirmation event and enqueue notifications | Complex | 8 |
| API | Intake payment confirmation event and enqueue notifications | Complex | 8 |
| API | Intake schedule and allocation update event and enqueue notifications | Complex | 8 |
| API | Intake hall ticket availability event and enqueue notifications | Complex | 8 |
| API | Intake examination reminder event and enqueue notifications | Complex | 8 |
| API | Intake examination credentials issued event and enqueue notifications | Complex | 8 |
| API | Intake results publication event and enqueue notifications | Complex | 8 |
| API | Intake certificate availability event and enqueue notifications | Complex | 8 |
| Database | Event type reference catalog persistence | Simple | 0.1 |
| Database | Event-to-template routing mapping persistence | Easy | 0.25 |
| Database | Inbound domain event idempotency and dispatch job enqueue persistence | Complex | 0.5 |
| Integration | Subscribe to Candidate Registration module domain events | Medium | 16 |
| Integration | Subscribe to Examination Scheduling and Allocation module domain events | Medium | 16 |
| Integration | Subscribe to Secure Examination Conduct module domain events | Medium | 16 |
| Integration | Subscribe to Evaluation and Results module domain events | Medium | 16 |
| Integration | Subscribe to Certificate Management module domain events | Medium | 16 |
| Testing | Happy-path each lifecycle event type routes to configured templates | Complex | 0.5 |
| Testing | Unmapped event type logging and invalid payload rejection | Medium | 0.3 |
| Testing | Duplicate domain event idempotency suppresses duplicate dispatch jobs | Complex | 0.5 |
| Documentation | Administrator event mapping configuration guide | Medium | 0.3 |
| Documentation | Technical domain event payload contract per lifecycle event | Complex | 0.5 |

### F07-004 Multi-Channel Notification Dispatch Engine

117.45 hours · Go-live · 21 tasks

##### Description

Background dispatch processing dequeues notification jobs created by lifecycle event intake, renders template placeholders from event payload snapshots, sends SMS and email through configured providers, writes in-app notifications to candidate inboxes, records per-channel attempt outcomes, and applies retry with backoff for transient provider failures until terminal success or exhaustion.

##### Business objective

Reliably deliver examination lifecycle messages across SMS, email, and in-app channels with traceable attempt history and controlled retry so candidates receive timely registration, scheduling, conduct, results, and certificate notifications.

##### Actors

- System Notification Service
- Examination Administrator

##### User journey

1. Dispatch worker polls queued jobs in priority and received-time order.
2. Worker loads job, linked template snapshot, channel configuration, and recipient contact details.
3. Worker renders message body and subject by substituting placeholders from event payload.
4. For SMS jobs, worker calls SMS gateway with rendered text and records provider message ID or error.
5. For email jobs, worker sends SMTP message with rendered subject and HTML or plain body.
6. For in-app jobs, worker inserts inbox record for candidate with title and body.
7. Worker writes delivery attempt row with status SENT, FAILED, or RETRY_PENDING.
8. On transient failure, worker schedules retry according to backoff policy until max attempts.
9. After terminal outcome, worker marks dispatch job COMPLETED or EXhausted_FAILED.
10. Examination Administrator opens dispatch job detail from monitor to view channel attempt timeline and provider responses.
11. When queue has no pending jobs, monitor shows empty state.

##### Functional capabilities

- Dequeue pending dispatch jobs for worker processing
- Render template placeholders from stored event payload snapshot
- Send SMS through configured gateway with provider response capture
- Send email through configured SMTP with message ID capture
- Create candidate in-app inbox notification record
- Record each delivery attempt with timestamp, channel, status, and provider code
- Retry transient failures with configurable backoff and max attempts
- Mark dispatch job terminal success or exhausted failure
- Expose dispatch job detail with attempt timeline for administrators
- Handle missing placeholder values with configurable fail-or-blank policy

##### Inputs

- Dispatch job identifier
- Template snapshot reference
- Event payload snapshot
- Recipient mobile number
- Recipient email address
- Candidate portal user identifier for in-app
- Channel type
- Retry attempt count
- Provider credentials from channel configuration

##### Outputs

- Provider message identifier for SMS or email
- In-app inbox record identifier
- Per-attempt delivery log rows
- Terminal dispatch job status
- Administrator job detail with attempt timeline

##### Business rules

- Jobs for disabled channels fail fast without provider call
- Rendered messages must not include fields marked sensitive in event contract
- Retry applies only to classified transient provider errors
- Permanent failures (invalid number, hard bounce) do not retry
- Successful in-app write is terminal for that channel attempt even if SMS/email sibling fails
- Job processing must be idempotent per attempt number

##### Validations

- Recipient mobile required for SMS jobs; valid format or fail permanent
- Recipient email required for email jobs; valid RFC format or fail permanent
- Candidate identifier required for in-app jobs
- Template snapshot must exist and be readable at processing time
- Rendered SMS must not exceed configured length after substitution
- Missing mandatory placeholder when policy is FAIL aborts attempt with logged reason

##### Calculations

- Next retry time equals previous attempt time plus backoff interval for attempt number
- SMS rendered length counted after placeholder substitution

##### Workflow

Job PENDING → PROCESSING → ATTEMPT_SENT (per channel success) → COMPLETED (all channels terminal success or acceptable partial success per policy). Job PENDING → PROCESSING → ATTEMPT_FAILED → RETRY_PENDING → PROCESSING (loop) → EXHAUSTED_FAILED when max retries exceeded. Job PENDING → FAILED_FAST when channel disabled or permanent validation failure.

##### Search requirements

- Administrator job detail retrieved by dispatch job identifier
- Dispatch monitor filters jobs by status and received date

##### Security

- Worker credentials loaded from encrypted configuration only at runtime
- Do not log full message bodies containing credentials in application logs
- Restrict administrator job detail to Examination Administrator role

##### Integrations

- SMS gateway send API
- SMTP mail send
- Internal candidate inbox persistence

##### Dependencies

- F07-002 Channel Provider Configuration — provider settings and enable flags
- F07-001 Notification Template Catalog — template content snapshots
- F07-003 Examination Lifecycle Event Subscription — job enqueue source
- F07-005 Delivery Status Tracking — persists attempt outcomes
- F07-007 Candidate Portal In-App Notification Inbox — displays in-app records

##### Assumptions

- Single dispatch worker pool sufficient for initial examination volumes
- Provider transient error classification table supplied during gateway integration
- Partial success policy (e.g., in-app succeeds, SMS fails) acceptable unless department mandates all-channel success

##### Risks

- Provider outage may delay large batches until retries exhaust
- Template placeholder mismatch at dispatch time causes avoidable failures if event payload changes retroactively

##### Non-functional requirements

- Process standard job within 10 seconds excluding provider latency
- Support at least 500 concurrent queued jobs
- Retry backoff configurable without code deployment

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Dispatch job detail read-only view with channel attempt timeline | Medium | 16 |
| UI | Dispatch queue monitor empty state when no pending jobs | Simple | 5 |
| API | Dequeue pending dispatch job for worker processing | Medium | 6 |
| API | Render message body by resolving template placeholders from event payload | Complex | 8 |
| API | Dispatch SMS outbound message via configured gateway | Medium | 6 |
| API | Dispatch email outbound message via configured SMTP | Medium | 6 |
| API | Persist in-app portal notification record for candidate | Medium | 6 |
| API | Record per-channel dispatch attempt outcome on delivery log | Medium | 6 |
| API | Retry transient failure with configured backoff policy | Complex | 8 |
| API | Mark dispatch job terminal success or exhausted failure | Medium | 6 |
| API | Get dispatch job detail with channel attempt history | Medium | 6 |
| Database | Outbound dispatch worker job state persistence | Medium | 0.3 |
| Database | Per-recipient rendered message snapshot persistence | Easy | 0.25 |
| Integration | SMS gateway send message call with provider response mapping | Medium | 16 |
| Integration | SMTP send mail call with provider correlation identifier capture | Medium | 16 |
| Integration | Internal portal notification fan-out to candidate inbox store | Simple | 4 |
| Testing | Happy-path successful SMS, email, and in-app dispatch for single job | Complex | 0.5 |
| Testing | Provider timeout and invalid recipient permanent failure recording | Medium | 0.3 |
| Testing | Retry policy stops after max attempts with complete audit trail | Complex | 0.5 |
| Testing | Missing mandatory placeholder fail policy aborts dispatch safely | Medium | 0.3 |
| Documentation | Technical dispatch worker operations and retry policy notes | Medium | 0.3 |

### F07-005 Delivery Status Tracking and Notification Register

82.05 hours · Go-live · 17 tasks

##### Description

Examination Administrators monitor all outbound notification deliveries across SMS, email, and in-app channels through a searchable register with status filters, drill-down to attempt history and provider responses, correlation to source lifecycle events and registration numbers, and export for operational review.

##### Business objective

Give examination administrators full visibility into whether lifecycle notifications reached candidates, support troubleshooting of failed deliveries, and maintain auditable evidence of communication for registration through certificate milestones.

##### Actors

- Examination Administrator
- System Notification Service

##### User journey

1. Examination Administrator opens Notification Delivery Register.
2. Administrator applies filters for date range, channel, delivery status, and lifecycle event type.
3. Administrator searches by candidate registration number or mobile number.
4. Register lists deliveries with sent time, channel, event type, status chip, and recipient masked appropriately.
5. Administrator selects a row to open delivery detail view.
6. Detail view shows rendered message snapshot reference, each attempt timestamp, provider response code, and linked source event identifier.
7. Administrator exports current filtered result set to spreadsheet for offline review.
8. If no deliveries match filters, empty state explains criteria.
9. If register API fails, error state offers retry.

##### Functional capabilities

- List notification deliveries with pagination
- Filter deliveries by date range, channel, status, and event type
- Search deliveries by registration number or mobile number
- Display delivery detail with multi-attempt history
- Show provider response codes and correlation identifiers
- Link delivery row to source domain event and dispatch job
- Export filtered delivery register to spreadsheet format
- Mask recipient contact details partial display in list view

##### Inputs

- Date range filter
- Channel filter
- Delivery status filter
- Lifecycle event type filter
- Registration number search text
- Mobile number search text
- Export column selection default set

##### Outputs

- Delivery register paginated rows
- Delivery detail with attempt timeline
- Exported spreadsheet file
- Empty and error state messages

##### Business rules

- Delivery statuses include PENDING, SENT, DELIVERED (if provider confirms), FAILED, RETRY_PENDING, EXHAUSTED_FAILED for SMS/email; READ/UNREAD applies only to in-app channel display
- Historical deliveries remain visible after template deactivation
- Export limited to administrator authorized scope (department-wide for Examination Administrator)
- Provider response codes stored as received without alteration

##### Validations

- Date range start must be before or equal to end
- Registration number search minimum 3 characters when provided
- Mobile search must be numeric format when provided
- Export row limit enforced with message when exceeded

##### Workflow

Delivery attempt statuses transition PENDING → SENT → DELIVERED or FAILED → RETRY_PENDING → SENT/FAILED loops → EXHAUSTED_FAILED terminal. In-app deliveries transition UNREAD → READ when candidate opens notification (tracked in inbox feature).

##### Search requirements

- Filter by sent date range
- Filter by channel SMS, email, in-app
- Filter by status PENDING, SENT, FAILED, EXHAUSTED_FAILED
- Filter by lifecycle event type
- Search by registration number exact or partial
- Search by mobile number
- Default sort by sent timestamp descending

##### Security

- Examination Administrator role required
- Mask mobile and email in list view showing last four digits or local-part obscured
- Audit export actions with administrator identity and filter snapshot

##### Dependencies

- F07-004 Multi-Channel Notification Dispatch Engine — produces delivery attempts
- F01 Platform Role and Permission Catalog — administrator access control

##### Assumptions

- SMS delivery confirmation depends on gateway delivery receipt support; otherwise status remains SENT
- Export format is CSV or XLSX per department standard

##### Risks

- Large export queries may impact performance during peak examination periods

##### Non-functional requirements

- Register search returns within 3 seconds for 100,000 delivery rows indexed
- Export up to 10,000 rows per request

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Notification delivery register list with date, channel, status, and event type filters | Medium | 16 |
| UI | Delivery register empty state when no deliveries match filters | Simple | 5 |
| UI | Delivery detail read-only view with provider response codes | Medium | 16 |
| UI | Export delivery register to spreadsheet action | Easy | 14 |
| UI | Delivery register load failure error state | Simple | 5 |
| API | List notification deliveries with search and filter parameters | Medium | 6 |
| API | Get delivery detail including attempt history and message snapshot reference | Medium | 6 |
| API | Search deliveries by registration number or mobile number | Medium | 6 |
| API | Export filtered delivery register dataset | Medium | 6 |
| Database | Per-channel delivery attempt log persistence | Medium | 0.3 |
| Database | Delivery status indexing for register query performance | Easy | 0.25 |
| Database | Delivery to source domain event correlation persistence | Medium | 0.3 |
| Testing | Happy-path register list, detail drill-down, and filtered search | Medium | 0.3 |
| Testing | Export respects active filters and row limit enforcement | Easy | 0.25 |
| Testing | Unauthorized user denied access to delivery register | Medium | 0.3 |
| Documentation | Administrator delivery monitoring runbook | Easy | 0.25 |
| Documentation | Technical delivery status lifecycle definitions | Simple | 0.1 |

### F07-006 Resend Controls and Failed Delivery Recovery

108.45 hours · Go-live · 19 tasks

##### Description

Examination Administrators resend failed or exhausted lifecycle notifications individually or in bulk from the delivery register, with eligibility checks against active templates and enabled channels, mandatory reason capture, audit linkage to original deliveries, partial bulk outcome reporting, and ability to cancel pending resends before dispatch starts.

##### Business objective

Allow controlled recovery when SMS, email, or in-app notifications fail so candidates still receive registration, scheduling, hall ticket, reminder, credentials, results, or certificate messages without duplicating successful sends or bypassing governance rules.

##### Actors

- Examination Administrator
- System Notification Service
- Candidate

##### User journey

1. Examination Administrator opens Delivery Register and applies Failed or Exhausted status filter.
2. Administrator reviews failed delivery rows and opens detail to inspect last provider error.
3. Administrator selects Resend on a single delivery.
4. Resend dialog shows channel, recipient, linked event type, and requires reason text.
5. System validates template still active and channel enabled; if not, blocked reason dialog explains constraint.
6. Administrator confirms; system creates new dispatch job linked to original delivery and writes resend audit record.
7. Administrator selects multiple failed rows and chooses Bulk Resend.
8. Bulk confirmation shows count and requires reason; system processes each with eligibility check.
9. Results summary shows succeeded, skipped, and failed counts without duplicating already-resubmitted items.
10. Administrator views Resend History tab on original delivery detail showing each resend attempt linkage.
11. If resend still queued, administrator may cancel pending resend before worker picks up job.
12. Candidate receives message when resend dispatch succeeds through normal engine flow.

##### Functional capabilities

- Filter delivery register to failed and exhausted deliveries eligible for review
- Resend single failed notification with mandatory reason capture
- Bulk resend selected failed notifications with rate limit guard
- Validate resend eligibility against active template and enabled channel
- Block resend with explicit reason when template inactive or channel disabled
- Create resend audit record linked to original delivery identifier
- Display resend history on delivery detail
- Cancel pending resend job before dispatch starts
- Prevent duplicate resend while identical resend job already pending

##### Inputs

- Original delivery identifier
- Bulk selected delivery identifiers
- Resend reason text
- Optional channel override when original channel permanently failed and alternate configured
- Cancel pending resend job identifier

##### Outputs

- New dispatch job identifier for resend
- Resend audit entries
- Bulk resend outcome summary counts
- Blocked resend reason message
- Resend history list on delivery detail
- Cancel confirmation outcome

##### Business rules

- Resend reason mandatory minimum 10 characters
- Cannot resend deliveries that already reached SENT or DELIVERED terminal success unless department override flag enabled for duplicate resend warning
- Bulk resend maximum batch size enforced (configurable, e.g., 100)
- Resend uses current template content version active at resend time
- Each resend retains correlation to original source lifecycle event
- Cancel allowed only while resend job status is PENDING

##### Validations

- Original delivery must exist and be in FAILED or EXHAUSTED_FAILED status
- Reason text required; length 10–500 characters
- Bulk selection must not exceed configured maximum
- Template for event type and channel must be active
- Channel must be enabled
- Duplicate pending resend for same delivery rejected

##### Calculations

- Bulk resend summary counts succeeded, skipped_ineligible, and failed_enqueue per item

##### Workflow

Failed delivery → RESEND_REQUESTED → RESEND_PENDING (job queued) → RESEND_DISPATCHING → RESEND_SENT or RESEND_FAILED. RESEND_PENDING → RESEND_CANCELLED (administrator cancel). Bulk operation tracks per-item subprocess through same states.

##### Search requirements

- Filter failed deliveries eligible for resend
- Resend history listed by original delivery identifier

##### Security

- Examination Administrator permission required for resend and cancel
- Audit every resend and cancel with administrator, reason, and timestamp
- Bulk resend rate limit prevents abuse

##### Dependencies

- F07-005 Delivery Status Tracking — source failed delivery rows
- F07-004 Multi-Channel Notification Dispatch Engine — processes resend jobs
- F07-001 Notification Template Catalog — active template validation
- F07-002 Channel Provider Configuration — channel enable validation

##### Assumptions

- Administrators resend only after correcting recipient data upstream when failure was invalid contact
- Candidate-initiated resend is out of scope except via administrator action

##### Risks

- Bulk resend during misconfiguration may amplify provider errors
- Using updated template at resend time may confuse candidates if content differs materially

##### Non-functional requirements

- Single resend enqueue within 2 seconds
- Bulk resend of 100 items completes enqueue within 60 seconds

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Failed delivery subset filter view on delivery register | Easy | 14 |
| UI | Resend single delivery confirmation dialog with mandatory reason | Medium | 16 |
| UI | Bulk resend selected failed deliveries confirmation dialog | Medium | 16 |
| UI | Resend blocked reason dialog when template inactive or channel disabled | Simple | 5 |
| UI | Resend history tab on delivery detail view | Easy | 14 |
| UI | Cancel pending resend confirmation dialog | Simple | 5 |
| API | List failed deliveries eligible for resend | Medium | 6 |
| API | Resend single notification delivery with audit reason capture | Complex | 8 |
| API | Bulk resend failed deliveries with rate limit guard | Complex | 8 |
| API | Validate resend eligibility against template and channel availability | Medium | 6 |
| API | List resend history for original delivery identifier | Easy | 4 |
| API | Cancel pending resend queue entry before dispatch starts | Easy | 4 |
| Database | Resend audit record linked to original delivery persistence | Medium | 0.3 |
| Testing | Happy-path single and bulk resend creates new dispatch attempt | Complex | 0.5 |
| Testing | Resend rejected when template deactivated or channel disabled | Medium | 0.3 |
| Testing | Bulk resend partial failure reporting without duplicate pending resends | Complex | 0.5 |
| Testing | Resend reason mandatory validation and cancel pending resend flow | Medium | 0.3 |
| Documentation | Administrator resend policy and failure recovery runbook | Medium | 0.3 |
| Documentation | Technical resend idempotency and audit linkage notes | Easy | 0.25 |

### F07-007 Candidate Portal In-App Notification Inbox

87.95 hours · Go-live · 19 tasks

##### Description

Candidates view examination lifecycle notifications delivered to the portal in-app channel through a paginated inbox with unread badge, notification detail view, mark-read actions, empty and error states, and mobile-responsive layout. Covers registration confirmation, payment confirmation, schedule and allocation updates, hall ticket availability, examination reminders, credentials notices, results publication, and certificate availability messages.

##### Business objective

Ensure candidates have a durable in-portal record of examination communications when SMS or email is missed, with clear read status and secure access limited to their own notifications.

##### Actors

- Candidate
- System Notification Service

##### User journey

1. Candidate logs into examination portal (OTP login handled by Candidate Registration module).
2. Header shows unread in-app notification count badge when count greater than zero.
3. Candidate opens Notifications inbox from portal menu.
4. Inbox lists notifications with title, received date, and unread indicator sorted newest first.
5. Candidate taps a row to open notification detail showing full message body and related examination context fields.
6. Opening detail marks notification as read and decrements unread badge.
7. Candidate uses Mark all as read control to clear unread indicators.
8. If no notifications exist, empty state explains notifications will appear for registration and examination milestones.
9. If inbox load fails, error state with retry is shown.
10. On mobile viewport, list layout adapts for touch navigation without loss of content.

##### Functional capabilities

- List candidate in-app notifications with pagination
- Display unread count badge on portal header
- Show notification detail with title, body, and received timestamp
- Mark single notification as read on detail open
- Mark all notifications as read for logged-in candidate
- Hide notifications older than configured retention unless already opened
- Prevent candidate access to another candidate notification records
- Render mobile-responsive inbox list and detail layouts
- Show inbox empty state and load error state

##### Inputs

- Authenticated candidate session identifier
- Pagination page number and size
- Notification identifier for detail and mark-read
- Mark all as read action

##### Outputs

- Paginated inbox list rows
- Unread notification count
- Notification detail content
- Updated read status
- Empty and error state views

##### Business rules

- Candidates see only notifications addressed to their portal account
- Unread count includes notifications with read status UNREAD within retention window
- Mark all as read updates only notifications currently visible under retention policy
- In-app notifications created only by dispatch engine for mapped lifecycle events
- Deleted upstream registration does not delete historical notifications but may hide future relevance in UI footnote

##### Validations

- Session required for all inbox operations
- Notification identifier must belong to authenticated candidate or return not found
- Pagination page size maximum 50
- Mark-read on already read notification is idempotent success

##### Calculations

- Unread count equals count of inbox rows with read status UNREAD within retention days from channel configuration

##### Workflow

Notification UNREAD → READ on detail view open or explicit mark-read. Mark all transitions all UNREAD in retention window to READ. Archived notifications beyond retention hidden from list (terminal visibility state).

##### Search requirements

- Inbox sorted by received timestamp descending
- Optional future filter by unread only not in initial scope unless configured—default shows all within retention

##### Notifications

- In-app display of registration confirmation message
- In-app display of payment confirmation message
- In-app display of schedule and allocation update message
- In-app display of hall ticket availability message
- In-app display of examination reminder message
- In-app display of credentials notice message
- In-app display of results publication message
- In-app display of certificate availability message

##### Security

- Candidate session scoped data access only
- No exposure of other candidates notification identifiers through sequential ID guessing
- HTTPS required for inbox access

##### Dependencies

- F05 Candidate Registration — candidate portal authentication session
- F07-004 Multi-Channel Notification Dispatch Engine — creates inbox records
- F07-002 Channel Provider Configuration — in-app retention settings

##### Assumptions

- Candidate portal shell and navigation exist from registration module
- Push browser notifications are out of scope; inbox is pull-based only

##### Risks

- Candidates may rely solely on inbox and miss time-sensitive SMS if unread
- Long retention may clutter inbox unless titles are clear

##### Non-functional requirements

- Inbox first page loads within 2 seconds on mobile network
- Unread count API responds within 500 milliseconds
- Responsive layout supports minimum viewport 320px width

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate portal notification inbox list with unread indicators | Medium | 16 |
| UI | Candidate notification detail read-only view | Easy | 14 |
| UI | Mark single notification as read control on detail view | Simple | 5 |
| UI | Mark all notifications as read action on inbox | Simple | 5 |
| UI | Candidate inbox empty state when no notifications exist | Simple | 5 |
| UI | Candidate inbox load error state with retry | Simple | 5 |
| UI | Mobile-responsive notification list and detail layout | Medium | 16 |
| API | List candidate in-app notifications with pagination | Medium | 6 |
| API | Get candidate notification detail by identifier | Easy | 4 |
| API | Mark single notification as read | Easy | 4 |
| API | Mark all notifications as read for authenticated candidate | Easy | 4 |
| API | Count unread in-app notifications for portal header badge | Simple | 2 |
| Database | Candidate in-app notification inbox persistence | Easy | 0.25 |
| Database | Read status and received timestamp indexing for inbox queries | Easy | 0.25 |
| Testing | Happy-path inbox list, detail, mark read, and unread count badge | Medium | 0.3 |
| Testing | Candidate cannot access another candidate notification record | Complex | 0.5 |
| Testing | Expired notifications hidden per retention policy | Medium | 0.3 |
| Documentation | Candidate portal notification inbox user guide | Easy | 0.25 |
| Documentation | Technical in-app notification retention policy notes | Simple | 0.1 |

## 08 Centre Operations

659.5 hours · 104 tasks · Business

Examination-day centre dashboard and invigilator workflows for candidate verification, session activation, and monitoring.

### F08-001 Centre Examination Day Dashboard

108.75 hours · Go-live · 19 tasks

##### Description

Centre-scoped landing dashboard for invigilators showing today's and upcoming scheduled examination sessions for the logged-in authorised centre, with operational counts for registered candidates, attendance, identity verification, session activation, and in-progress session status distribution.

##### Business objective

Give examination centre invigilators a single operational view at the start of examination day so they can prioritise verification, attendance, activation, and monitoring tasks without accessing department-wide administration data.

##### Actors

- Examination Centre/Invigilator User

##### User journey

1. Invigilator logs in through centre-scoped staff authentication and lands on the Centre Examination Day Dashboard.
2. System resolves the invigilator's assigned authorised centre and loads only that centre's data.
3. Invigilator reviews today's examination session cards showing examination name, session slot, scheduled start time, and high-level status.
4. Invigilator reviews aggregate widgets showing total scheduled candidates, present count, verified count, activated count, and not-yet-arrived count per session.
5. Invigilator reviews session status chips showing counts in scheduled, verification-in-progress, activation-ready, in-progress, and completed states.
6. Invigilator scans the upcoming examination timeline for the next seven days to prepare staffing and logistics.
7. Invigilator selects a session card or quick-link to open the Scheduled Candidate Register filtered to that session.
8. Invigilator selects quick-link to Candidate Verification queue for the active session.
9. Invigilator selects quick-link to Session Activation list for the active session.
10. Invigilator selects quick-link to Live Session Monitoring when examinations are underway.
11. If no sessions are scheduled today, invigilator sees an empty-state message with upcoming session preview only.
12. If summary data fails to load, invigilator sees an error state with retry action.

##### Functional capabilities

- Display today examination session cards scoped to logged-in centre
- Display upcoming examination timeline for next seven days at centre
- Display per-session scheduled candidate count aggregate
- Display per-session present attendance count aggregate
- Display per-session identity verified count aggregate
- Display per-session session activated count aggregate
- Display session status distribution chips for scheduled through completed states
- Provide quick navigation to candidate register filtered by session
- Provide quick navigation to verification queue for selected session
- Provide quick navigation to activation list for selected session
- Provide quick navigation to live monitoring view for in-progress session
- Show empty state when no examinations scheduled today at centre
- Show error and retry state when dashboard summary load fails

##### Inputs

- Logged-in invigilator user identity and centre assignment
- Examination schedule and session slot dates from scheduling module
- Centre candidate allocation records for logged-in centre
- Candidate attendance marks for today's sessions
- Candidate identity verification records for today's sessions
- Candidate session activation records for today's sessions
- Live examination session status from secure conduct module

##### Outputs

- Today session summary cards with operational counts
- Upcoming session timeline list
- Session status distribution summary
- Navigation context to downstream centre operational screens

##### Business rules

- Dashboard data must be limited to the invigilator's assigned authorised examination centre only
- Only scheduled examination sessions allocated to the centre appear on the dashboard
- Counts reflect candidates allocated to the centre for each session regardless of other centres
- Activation and monitoring counts include only candidates in centre allocation for the session
- Upcoming timeline excludes sessions more than seven days in the future
- Completed session status applies when all allocated candidates have reached submitted or completed conduct state or session end time has passed per examination configuration

##### Validations

- Reject dashboard request when invigilator has no active centre assignment
- Reject dashboard request when invigilator centre assignment is inactive
- Validate requested date range parameters are not malformed
- Validate session identifier in drill-down navigation belongs to logged-in centre

##### Calculations

- Scheduled candidate count equals count of centre-allocated candidates for session
- Present count equals centre-allocated candidates with attendance status PRESENT
- Verified count equals centre-allocated candidates with verification status VERIFIED
- Activated count equals centre-allocated candidates with activation status ACTIVATED
- Not-yet-arrived count equals scheduled minus present minus explicitly marked absent
- In-progress session count equals sessions with at least one activated candidate and session end not reached

##### Workflow

Dashboard load: AUTHENTICATED -> CENTRE_RESOLVED -> SUMMARY_LOADED | SUMMARY_EMPTY | SUMMARY_ERROR. Session card drill-down: CARD_SELECTED -> REGISTER_FILTERED | VERIFICATION_QUEUE | ACTIVATION_LIST | MONITORING_VIEW.

##### Search requirements

- No free-text search on dashboard; filtering is by today default and upcoming date window only

##### Security

- Centre-scoped data isolation enforced on every dashboard aggregate query
- Invigilator role permission required to access centre operations dashboard
- No candidate PII beyond counts and session labels on dashboard widgets
- Audit log entry for dashboard access optional at platform policy level

##### Integrations

- Staff authentication and centre assignment resolution from Module 01 User and Role Management
- Examination schedule and centre allocation read from Module 06 Examination Scheduling and Allocation
- Live session status counts read from Module 09 Secure Examination Conduct

##### Dependencies

- F01 centre-scoped invigilator account lifecycle and authentication session
- F03 authorised examination centre master and invigilator user assignment to centre
- F06 examination schedule creation and candidate centre session allocation
- F09 secure examination conduct session state for in-progress monitoring counts

##### Assumptions

- Invigilator users are assigned to exactly one active centre for examination-day operations
- Schedule and allocation data is finalised before examination day dashboard use
- Dashboard aggregates are read-only operational views over upstream module data
- Seven-day upcoming window is sufficient for centre planning without department analytics

##### Risks

- Stale conduct module status may cause monitoring count lag without refresh interval agreement
- High candidate volume per session may require aggregate query optimisation
- Partial upstream data availability could produce incomplete widget counts

##### Non-functional requirements

- Dashboard summary should load within acceptable enterprise web response time for up to 500 allocated candidates per session
- Dashboard must remain usable on standard centre desktop browsers
- Widget counts must be consistent with downstream register and queue screens for same session

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre dashboard landing screen with today examination session cards | Medium | 16 |
| UI | Dashboard empty state when no examinations scheduled today | Simple | 5 |
| UI | Dashboard error state with retry action for failed summary load | Simple | 5 |
| UI | Session status summary widget with scheduled through completed count chips | Medium | 16 |
| UI | Candidate operational count widget for scheduled present verified activated | Medium | 16 |
| UI | Upcoming examination timeline panel for next seven days | Easy | 14 |
| UI | Quick navigation panel to register verification activation monitoring screens | Simple | 5 |
| API | Get centre-scoped today examination sessions summary | Medium | 6 |
| API | Get centre-scoped upcoming examination sessions list by date window | Medium | 6 |
| API | Get centre dashboard attendance aggregate counts by session | Complex | 8 |
| API | Get centre session status distribution counts for dashboard widgets | Medium | 6 |
| Database | Centre date session summary query indexes for dashboard aggregates | Easy | 0.25 |
| Database | Operational status aggregate read model over schedule allocation attendance verification activation | Medium | 0.3 |
| Integration | Resolve invigilator assigned centre scope from authorization service | Simple | 4 |
| Testing | Happy path dashboard metrics for multi-session examination day | Medium | 0.3 |
| Testing | Centre isolation prevents cross-centre dashboard data exposure | Medium | 0.3 |
| Testing | Empty schedule and zero-count widget edge cases | Easy | 0.25 |
| Documentation | Invigilator dashboard interpretation user runbook | Easy | 0.25 |
| Documentation | Centre scoping technical notes for dashboard aggregate queries | Simple | 0.1 |

### F08-002 Centre Scheduled Candidate Register

105.6 hours · Go-live · 18 tasks

##### Description

Centre-scoped searchable register of candidates scheduled and allocated to the logged-in examination centre, showing registration identity, hall ticket reference, session slot, and operational status flags for verification, attendance, and activation without exposing candidates allocated to other centres.

##### Business objective

Enable invigilators to locate and review every candidate expected at their centre for a given examination session before verification, attendance marking, and session activation activities begin.

##### Actors

- Examination Centre/Invigilator User

##### User journey

1. Invigilator opens Scheduled Candidate Register from dashboard or main navigation.
2. System loads paginated list of candidates allocated to invigilator's centre defaulting to today's sessions.
3. Invigilator selects examination name filter to narrow the register.
4. Invigilator selects session slot filter to narrow to one examination session.
5. Invigilator enters registration number, candidate name fragment, or hall ticket number in search bar.
6. System returns matching centre-allocated candidates only.
7. Invigilator applies verification status filter to find pending verifications.
8. Invigilator applies attendance status filter to find not-yet-marked candidates.
9. Invigilator applies activation status filter to find verified present but not activated candidates.
10. Invigilator clicks a candidate row to open read-only detail drawer with registration snapshot, allocated seat or computer if assigned, and current operational flags.
11. Invigilator initiates export action to download CSV day sheet for selected session filter.
12. Invigilator confirms export dialog and receives CSV file.
13. If session has zero allocated candidates, invigilator sees empty-state guidance to verify schedule and allocation.

##### Functional capabilities

- List paginated scheduled candidates allocated to logged-in centre
- Default register view to today sessions at centre
- Search candidates by registration number
- Search candidates by candidate name partial match
- Search candidates by hall ticket number
- Filter register by examination name
- Filter register by session slot
- Filter register by identity verification status
- Filter register by attendance status
- Filter register by session activation status
- Open read-only candidate schedule detail drawer
- Show empty state when session has zero centre-allocated candidates
- Export filtered register to CSV day sheet

##### Inputs

- Centre allocation records from scheduling module
- Candidate registration profile fields from registration module
- Hall ticket reference from scheduling module
- Seat or computer assignment when configured in scheduling module
- Verification attendance activation status from centre operations records

##### Outputs

- Paginated candidate register list with operational status columns
- Candidate detail drawer content
- CSV export file of filtered register rows

##### Business rules

- Register includes only candidates with centre allocation matching logged-in centre
- Candidates allocated to other centres never appear in register results
- Hall ticket number displayed only for candidates allocated to viewing centre
- Export includes only rows matching active filter set and centre scope
- Register is read-only; status changes occur in verification attendance activation features

##### Validations

- Reject list request when invigilator centre assignment missing or inactive
- Validate pagination page size within allowed maximum
- Validate examination filter identifier belongs to scheduled sessions at centre
- Validate session slot filter belongs to logged-in centre schedule
- Validate search registration number format when provided
- Validate hall ticket number format when provided
- Reject export when result set exceeds configured export row limit with user message

##### Workflow

Register view: OPEN -> LOAD_DEFAULT -> FILTERED | SEARCHED -> DETAIL_DRAWER_OPEN. Export: EXPORT_REQUESTED -> EXPORT_CONFIRMED -> CSV_DOWNLOADED.

##### Search requirements

- Partial match search on candidate name case-insensitive
- Exact or prefix match on registration number
- Exact match on hall ticket number
- Combined search with examination session verification attendance activation filters

##### Documents

- CSV day sheet export of scheduled candidate register

##### Security

- Centre-scoped query enforcement on all list search filter export operations
- Invigilator permission required for candidate register access
- CSV export restricted to same centre scope as on-screen register
- Sensitive registration fields masked per platform PII policy in list view if configured

##### Integrations

- Read examination schedule and centre allocation from Module 06 Examination Scheduling and Allocation
- Read candidate registration profile snapshot from Module 05 Candidate Registration
- Read hall ticket reference from Module 06 hall ticket generation handoff

##### Dependencies

- F06 candidate centre and session allocation
- F06 digital hall ticket generation and candidate access reference
- F06 candidate seat and computer assignment when seat assignment configured
- F05 candidate registration profile data for register display

##### Assumptions

- Centre allocation is authoritative before examination day register use
- Hall ticket numbers are unique within an examination schedule
- Register row counts align with dashboard scheduled candidate aggregates

##### Risks

- Late allocation changes after invigilator prints CSV day sheet may cause on-floor mismatch
- Large sessions may require pagination performance tuning

##### Non-functional requirements

- Search and filter should return first page within enterprise list response targets for up to 500 rows per session
- CSV export should complete for full session candidate list without timeout under normal centre hardware

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Scheduled candidate register list with default today session filter | Medium | 16 |
| UI | Candidate search bar for registration number name hall ticket | Easy | 14 |
| UI | Filter panel by examination session slot verification attendance activation status | Medium | 16 |
| UI | Read-only candidate schedule detail drawer | Easy | 14 |
| UI | Register empty state for session with zero allocated candidates | Simple | 5 |
| UI | Export scheduled candidate list confirmation dialog | Simple | 5 |
| API | List paginated scheduled candidates for logged-in centre | Medium | 6 |
| API | Search scheduled candidates by registration number name hall ticket | Medium | 6 |
| API | Filter scheduled candidates by examination session operational status | Medium | 6 |
| API | Get scheduled candidate detail for centre invigilator view | Easy | 4 |
| API | Export centre scheduled candidate register CSV | Complex | 8 |
| Database | Centre-scoped candidate allocation list query indexes | Easy | 0.25 |
| Database | Registration number and hall ticket search indexes for centre register | Easy | 0.25 |
| Integration | Read examination schedule and centre allocation from scheduling module | Simple | 4 |
| Testing | Happy path list search filter and detail drawer flow | Medium | 0.3 |
| Testing | Cross-centre candidate record exclusion from register results | Medium | 0.3 |
| Testing | CSV export column completeness for invigilator day sheet | Easy | 0.25 |
| Documentation | Scheduled candidate register invigilator user guide | Easy | 0.25 |

### F08-003 Candidate Identity Verification and Attendance Marking

159.65 hours · Go-live · 26 tasks

##### Description

Invigilator workflows at the examination centre to verify candidate identity against registration records, reject verification with documented reason when identity cannot be confirmed, mark candidate attendance as present or absent with mandatory absent reason, and correct mistaken attendance marks with audit history before session activation.

##### Business objective

Ensure only identity-confirmed and physically present candidates at the authorised centre proceed to examination session activation, creating an auditable pre-examination record for each allocated candidate.

##### Actors

- Examination Centre/Invigilator User

##### User journey

1. Invigilator opens Candidate Verification queue for a selected centre session.
2. System lists centre-allocated candidates with verification status UNVERIFIED or REJECTED at top of queue.
3. Invigilator selects a candidate row to open verification detail screen.
4. Invigilator compares displayed registration name, registration number, photograph if available, category, and hall ticket reference against candidate physical ID and hall ticket document.
5. Invigilator confirms identity and selects Mark Verified action.
6. System prompts confirmation dialog; invigilator confirms.
7. System transitions candidate verification status to VERIFIED with invigilator and timestamp audit.
8. Alternatively invigilator selects Reject Verification, enters mandatory rejection reason, and confirms.
9. System transitions candidate verification status to REJECTED and records reason.
10. Invigilator returns to queue or opens attendance action for verified candidate.
11. Invigilator selects Mark Present for candidate who has arrived; system records PRESENT with timestamp.
12. For candidate who did not arrive, invigilator selects Mark Absent, enters mandatory absent reason, and confirms.
13. System records ABSENT status blocking downstream activation.
14. If invigilator marked attendance incorrectly, invigilator opens attendance correction dialog, selects corrected status, enters mandatory correction reason, and confirms.
15. System writes correction audit entry preserving prior mark history.
16. When all candidates processed, queue shows empty state with counts of verified rejected present absent.

##### Functional capabilities

- List candidate verification queue for centre session ordered by pending status
- Display candidate verification detail with registration identity snapshot fields
- Mark candidate identity verified with invigilator audit stamp
- Reject candidate verification with mandatory rejection reason
- Display verification status badge on candidate rows
- Mark candidate attendance present with session timestamp
- Mark candidate attendance absent with mandatory absent reason
- Correct attendance mark with mandatory correction reason and audit history
- Display attendance status badge on candidate rows
- Show verification queue empty state when no pending candidates remain

##### Inputs

- Centre-allocated candidate list for session
- Candidate registration identity snapshot name registration number category photograph reference
- Hall ticket reference from scheduling module
- Invigilator user identity for audit
- Rejection reason text or selected reason code
- Absent reason text or selected reason code
- Attendance correction reason text

##### Outputs

- Updated verification status VERIFIED or REJECTED per candidate
- Verification rejection reason record
- Updated attendance status PRESENT or ABSENT per candidate
- Attendance correction audit history entries
- Updated operational flags visible in register and activation eligibility

##### Business rules

- Verification and attendance actions allowed only for candidates allocated to invigilator's centre for the session
- Verification can be marked only while session is in pre-start operational window per examination schedule
- Rejected verification prevents session activation for that candidate
- Absent attendance prevents session activation for that candidate
- Present attendance requires prior VERIFIED status before activation eligibility evaluation
- Attendance correction allowed only before candidate session activation
- Each verification and attendance change records invigilator user and timestamp
- Re-verification after VERIFIED requires supervisor policy if platform configures lock after verify

##### Validations

- Reject verification action when candidate not allocated to logged-in centre
- Reject verify when session not in allowed pre-start window
- Reject rejection submission when rejection reason is blank or below minimum length
- Reject present mark when candidate verification status is REJECTED
- Reject absent reason submission when absent reason is blank or below minimum length
- Reject attendance correction when candidate session already ACTIVATED
- Reject attendance correction when correction reason is blank
- Reject duplicate verify when candidate already VERIFIED unless correction policy enabled

##### Calculations

- Queue sort priority: UNVERIFIED first, then REJECTED awaiting review, then VERIFIED with UNMARKED attendance

##### Workflow

Verification: UNVERIFIED -> VERIFIED | REJECTED. Attendance: UNMARKED -> PRESENT | ABSENT. Correction: PRESENT <-> ABSENT with audit before ACTIVATED.

##### Search requirements

- Verification queue filter by verification status pending verified rejected
- Verification queue filter by attendance status unmarked present absent

##### Security

- Centre scope enforced on all verification and attendance mutations
- Invigilator role permission required for verify and attendance actions
- Immutable audit trail for verification rejection attendance and correction events
- Rejected candidates must not expose activation actions in downstream screens

##### Integrations

- Fetch candidate registration identity snapshot from Module 05 Candidate Registration
- Write audit events consumable by Module 12 Examination Administration reporting

##### Dependencies

- F08-002 centre scheduled candidate register for candidate selection context
- F05 candidate registration profile and confirmation data
- F06 candidate centre session allocation and hall ticket reference
- F01 invigilator authentication and centre-scoped authorization

##### Assumptions

- Registration photograph or identity fields are available from registration module when captured
- Invigilator performs physical ID check outside system; system records outcome only
- Session pre-start window defined by examination schedule start time from Module 06

##### Risks

- Incorrect manual verification could allow wrong candidate activation without biometric enforcement
- Concurrent invigilator actions on same candidate require optimistic locking
- Attendance correction disputes require clear audit history for administration review

##### Non-functional requirements

- Verification detail screen must load registration snapshot within standard form response time
- Audit records must be durable before activation eligibility reflects updated status

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate verification queue list for current centre session | Medium | 16 |
| UI | Candidate verification detail screen with registration identity fields | Complex | 18 |
| UI | Mark candidate identity verified confirmation dialog | Simple | 5 |
| UI | Reject verification dialog with mandatory reason field | Easy | 14 |
| UI | Mark candidate present action with timestamp display | Easy | 14 |
| UI | Mark candidate absent dialog with mandatory reason field | Easy | 14 |
| UI | Verification status badge on candidate register rows | Simple | 5 |
| UI | Attendance status badge with correction dialog for mistaken mark | Medium | 16 |
| UI | Verification queue empty state when all candidates processed | Simple | 5 |
| API | List candidates pending identity verification for centre session | Medium | 6 |
| API | Get candidate verification profile with registration snapshot fields | Medium | 6 |
| API | Mark candidate identity verified with invigilator audit stamp | Complex | 8 |
| API | Reject candidate verification with mandatory reason | Medium | 6 |
| API | Mark candidate attendance present with session timestamp | Medium | 6 |
| API | Mark candidate attendance absent with mandatory reason | Medium | 6 |
| API | Correct attendance mark with reason and audit history entry | Complex | 8 |
| Database | Candidate centre identity verification record persistence | Medium | 0.3 |
| Database | Candidate attendance record with correction audit history | Medium | 0.3 |
| Database | Verification rejection reason reference values | Simple | 0.1 |
| Integration | Fetch candidate registration identity snapshot from registration module | Simple | 4 |
| Testing | Happy path identity verify then mark present flow | Medium | 0.3 |
| Testing | Reject verification requires reason and blocks activation eligibility | Medium | 0.3 |
| Testing | Absent marking prevents downstream session activation | Medium | 0.3 |
| Testing | Attendance correction audit trail and duplicate verify rejection | Complex | 0.5 |
| Documentation | Invigilator identity verification checklist runbook | Medium | 0.3 |
| Documentation | Verification attendance audit technical notes | Easy | 0.25 |

### F08-004 Candidate Examination Session Activation

145.7 hours · Go-live · 22 tasks

##### Description

Centre invigilator activation of eligible candidate examination sessions immediately prior to examination start, enforcing registration completeness, fee compliance, schedule allocation, centre assignment, physical presence, and identity verification prerequisites, with single and batch activation support and explicit blocked-reason feedback for ineligible candidates.

##### Business objective

Allow authorised centre staff to start candidate examination sessions only for candidates who meet all pre-examination eligibility conditions, handing activated sessions to secure examination conduct without re-entering registration or scheduling data.

##### Actors

- Examination Centre/Invigilator User

##### User journey

1. Invigilator opens Session Activation list for selected centre examination session.
2. System displays centre-allocated candidates with eligibility indicator per row.
3. Invigilator filters list to show only activation-ready candidates.
4. Invigilator selects a candidate row to open activation detail with eligibility checklist.
5. Invigilator reviews checklist items: registration complete, fee compliant, scheduled for session, allocated to this centre, attendance PRESENT, verification VERIFIED, session not already activated.
6. For eligible candidate invigilator selects Activate Session action.
7. System shows confirmation dialog with candidate name and examination name.
8. Invigilator confirms activation.
9. System transitions activation status to ACTIVATED, records invigilator and timestamp, and sends handoff to secure examination conduct module.
10. For ineligible candidate invigilator views blocked detail panel listing each failed rule with plain-language reason.
11. Invigilator switches to batch activation screen, multi-selects eligible candidates, and submits batch activate.
12. System processes each candidate, activates eligible rows, and reports per-row success or block reason for failures.
13. Invigilator refreshes list to see updated activation statuses.
14. If no verified present candidates remain, empty state displays guidance to complete verification and attendance first.

##### Functional capabilities

- List centre-allocated candidates with activation eligibility indicator
- Filter activation list to activation-ready candidates only
- Display activation detail eligibility checklist for single candidate
- Evaluate registration complete flag for candidate
- Evaluate fee compliance flag for candidate
- Evaluate scheduled session match for candidate
- Evaluate centre allocation match for logged-in centre
- Evaluate attendance PRESENT requirement
- Evaluate identity VERIFIED requirement
- Activate single candidate examination session with audit
- Batch activate multiple eligible candidate examination sessions
- Return activation block reasons for ineligible candidate
- Show activation queue empty state when no eligible candidates
- Refresh candidate row activation status after successful activation

##### Inputs

- Candidate registration completion status from registration module
- Candidate fee payment compliance status from fee management
- Examination schedule and session allocation from scheduling module
- Centre allocation record for candidate
- Verification status from centre verification records
- Attendance status from centre attendance records
- Invigilator user identity
- Batch candidate selection list

##### Outputs

- Activation status ACTIVATED for eligible candidates
- Activation event with invigilator timestamp and eligibility snapshot
- Handoff signal to secure examination conduct for credential session readiness
- Per-candidate block reason list for ineligible candidates
- Batch activation result summary with success and failure counts

##### Business rules

- Activation permitted only for candidates allocated to invigilator's authorised centre
- Candidate registration must be complete and confirmed
- Candidate fee must be compliant including free first-attempt and paid subsequent rules where applicable
- Candidate must be scheduled for the selected examination session
- Candidate attendance must be PRESENT
- Candidate verification must be VERIFIED
- Already ACTIVATED candidates cannot be activated again
- REJECTED verification or ABSENT attendance permanently blocks activation for that session unless attendance corrected before activation
- Batch activation skips ineligible candidates without blocking eligible ones in same batch
- Activation allowed only within configured pre-start window before session official start time

##### Validations

- Reject activation when candidate not centre-allocated to logged-in centre
- Reject activation when registration status incomplete
- Reject activation when fee compliance flag false
- Reject activation when candidate not scheduled for requested session
- Reject activation when attendance not PRESENT
- Reject activation when verification not VERIFIED
- Reject activation when session already ACTIVATED
- Reject activation outside allowed pre-start time window
- Reject batch request when selection list empty
- Validate each batch item independently without failing entire batch on single invalid row

##### Calculations

- Eligibility ready flag equals all checklist rules true
- Batch success count equals activated rows
- Batch failure count equals rows with block reasons

##### Workflow

Activation eligibility: INACTIVE -> ELIGIBILITY_EVALUATED -> ELIGIBLE | BLOCKED. Activation execution: ELIGIBLE -> ACTIVATE_CONFIRMED -> ACTIVATED -> HANDOFF_TO_CONDUCT.

##### Search requirements

- Filter activation list by eligibility ready blocked already activated
- Search activation list by registration number or candidate name

##### Security

- Centre scope on all activation queries and mutations
- Invigilator permission required for session activation actions
- Activation audit log with eligibility snapshot for dispute resolution
- Idempotent activation request handling to prevent duplicate conduct sessions

##### Integrations

- Read fee compliance from Module 05 Candidate Registration and Module 02 Payment Gateway Fee Transaction Integration
- Push session activation handoff to Module 09 Secure Examination Conduct
- Read schedule allocation from Module 06 Examination Scheduling and Allocation

##### Dependencies

- F08-003 candidate identity verification and attendance marking statuses
- F05 registration confirmation and fee compliance determination
- F02 payment gateway fee transaction integration for paid registrations
- F06 examination schedule centre allocation and examination credentials handoff
- F09 secure examination conduct to receive activated session

##### Assumptions

- Examination credentials generation completed in Module 06 before activation handoff
- Fee compliance flag maintained upstream and read at activation time
- Conduct module creates examination session only upon successful activation handoff

##### Risks

- Partial batch failure may cause invigilator confusion without clear per-row feedback
- Handoff failure after local ACTIVATED record requires reconciliation procedure
- Clock skew between centre client and server may affect pre-start window validation

##### Non-functional requirements

- Single activation should complete including handoff within enterprise transaction response targets
- Batch activation of up to 50 candidates should provide progress feedback
- Activation state must be immediately visible in monitoring feature after handoff

##### Notes

Activation limited to registered fee-compliant scheduled centre-allocated present verified candidates per SOW centre-level activation rules.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Activation eligible candidate list with eligibility indicator icons | Medium | 16 |
| UI | Activation candidate detail with eligibility checklist panel | Complex | 18 |
| UI | Activate single candidate session confirmation dialog | Simple | 5 |
| UI | Multi-select batch activation screen for eligible candidates | Medium | 16 |
| UI | Activation blocked detail panel listing failed eligibility rules | Medium | 16 |
| UI | Activation queue empty state when no verified present candidates | Simple | 5 |
| UI | Post-activation status refresh on candidate register row | Simple | 5 |
| API | List candidates for session activation at centre with eligibility flags | Complex | 8 |
| API | Evaluate single candidate activation eligibility rule set | Complex | 8 |
| API | Activate single candidate examination session for centre | Complex | 8 |
| API | Batch activate multiple eligible candidate examination sessions | Very high | 12 |
| API | Get activation block reasons for ineligible candidate | Medium | 6 |
| Database | Centre session activation event record with invigilator timestamp | Medium | 0.3 |
| Database | Activation eligibility snapshot stored at activation time | Easy | 0.25 |
| Integration | Push session activation handoff to secure examination conduct module | Medium | 16 |
| Integration | Read candidate fee compliance flag from registration payment data | Simple | 4 |
| Testing | Happy path activation for registered fee-compliant scheduled verified present candidate | Medium | 0.3 |
| Testing | Block activation when candidate not identity verified | Medium | 0.3 |
| Testing | Block activation when absent or fee non-compliant or wrong centre | Complex | 0.5 |
| Testing | Batch activation partial failure per-row result and audit logging | Complex | 0.5 |
| Documentation | Session activation invigilator procedure runbook | Medium | 0.3 |
| Documentation | Activation eligibility rule technical reference notes | Easy | 0.25 |

### F08-005 Centre Live Examination Session Monitoring

139.8 hours · Go-live · 19 tasks

##### Description

Real-time centre-scoped monitoring view for invigilators to track examination progress of activated candidates through started, active, submitted, and completed conduct states during an in-progress session, with aggregate status header counts and drill-down read-only candidate session detail.

##### Business objective

Enable invigilators to supervise examination progress at their centre, identify candidates who have not started or submitted within expected timelines, and confirm session completion counts without accessing question content or department-wide analytics.

##### Actors

- Examination Centre/Invigilator User

##### User journey

1. Invigilator opens Live Session Monitoring from dashboard or navigation.
2. Invigilator selects in-progress examination session at their centre.
3. System loads monitoring landing screen with aggregate header counts for not-started, started, active, submitted, and completed candidates.
4. Invigilator reviews candidate status grid with one row per activated centre-allocated candidate.
5. Invigilator identifies candidates still in not-started column after activation.
6. Invigilator selects grid row to open read-only drill-down showing session start time, last activity timestamp, current conduct status, and submission timestamp if submitted.
7. Invigilator triggers manual refresh to pull latest status from conduct module.
8. Invigilator optionally enables auto-refresh interval to keep grid current during examination.
9. System displays abnormal session alert banner when candidate remains in started state without activity beyond configured threshold.
10. Invigilator continues monitoring until all candidates reach submitted or completed state.
11. Invigilator opens session end summary read-only screen showing final completion counts.
12. If no candidates activated yet, monitoring shows empty state directing invigilator to activation feature.

##### Functional capabilities

- Select in-progress centre examination session for monitoring
- Display monitoring aggregate header counts by conduct status
- Display candidate status grid with not-started started active submitted completed columns
- Open read-only candidate live session drill-down detail panel
- Manual refresh monitoring data on demand
- Configure auto-refresh interval for monitoring grid
- Display abnormal session alert banner for stuck inactive candidates
- Display monitoring empty state before first activation
- Display session end summary read-only screen with final counts

##### Inputs

- Centre-allocated activated candidate list
- Live examination conduct session status from secure conduct module
- Session start and end times from examination schedule
- Last activity timestamps from conduct activity recording
- Abnormal idle threshold from examination configuration

##### Outputs

- Live status grid per activated candidate
- Aggregate status counts header
- Candidate drill-down session progress detail
- Session end completion summary counts
- Abnormal session alert indicators

##### Business rules

- Monitoring includes only candidates activated at logged-in centre for selected session
- Non-activated candidates appear in not-started or excluded per monitoring configuration agreed with conduct module
- Question content and candidate answers are never displayed in monitoring views
- Status values map to conduct module states: NOT_STARTED, STARTED, ACTIVE, SUBMITTED, COMPLETED
- Abnormal alert triggers when candidate in STARTED state exceeds idle threshold without transition to ACTIVE
- Monitoring read-only; invigilator cannot modify conduct state from this feature
- Session end summary available when session end time reached or all candidates submitted or completed

##### Validations

- Reject monitoring request when session not allocated to logged-in centre
- Reject monitoring request when invigilator lacks centre monitoring permission
- Validate selected session identifier belongs to centre schedule
- Validate auto-refresh interval within allowed minimum and maximum seconds

##### Calculations

- Not-started count equals activated candidates with conduct status NOT_STARTED
- Completed count equals candidates with conduct status COMPLETED plus SUBMITTED if examination treats submitted as complete for monitoring
- Abnormal candidate flag equals STARTED with last activity older than idle threshold

##### Workflow

Conduct status progression monitored: NOT_STARTED -> STARTED -> ACTIVE -> SUBMITTED -> COMPLETED. Monitoring view: SESSION_SELECTED -> GRID_LOADED -> REFRESHED -> SESSION_END_SUMMARY.

##### Search requirements

- Filter monitoring grid by conduct status column
- Search monitoring grid by registration number or candidate name

##### Security

- Centre-scoped monitoring queries exclude other centres' candidates
- No examination question or answer content exposed in monitoring UI
- Invigilator read-only access to conduct status fields only
- Monitoring access logged for audit when platform policy requires

##### Integrations

- Poll or subscribe to examination session state updates from Module 09 Secure Examination Conduct
- Read examination session schedule window from Module 06 Examination Scheduling and Allocation
- Read idle threshold from Module 04 Examination Master Configuration

##### Dependencies

- F08-004 candidate examination session activation producing ACTIVATED candidates
- F09 secure examination conduct session states and activity recording
- F06 examination schedule session timing
- F04 examination master configuration for session parameters

##### Assumptions

- Conduct module is authoritative source for started active submitted completed states
- Monitoring refresh interval balances timeliness with conduct module load
- Invigilator intervention for abnormal sessions occurs operationally outside this read-only view

##### Risks

- Polling lag may delay abnormal alert visibility
- Conduct module downtime would leave monitoring grid stale with no status updates
- Definition of SUBMITTED versus COMPLETED for summary counts must align with conduct module

##### Non-functional requirements

- Manual refresh should return updated grid within enterprise response targets for up to 500 activated candidates
- Auto-refresh must not degrade centre client browser performance at minimum interval
- Monitoring grid counts must reconcile with dashboard in-progress aggregates

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Live session monitoring landing screen for selected examination session | Medium | 16 |
| UI | Candidate status grid with not-started started active submitted completed columns | Complex | 18 |
| UI | Candidate live session drill-down read-only detail panel | Medium | 16 |
| UI | Manual refresh control for monitoring data | Simple | 5 |
| UI | Auto-refresh interval selector for monitoring view | Easy | 14 |
| UI | Abnormal session alert banner for stuck inactive candidates | Medium | 16 |
| UI | Monitoring empty state before first candidate activation | Simple | 5 |
| UI | Session end summary read-only screen with completion counts | Easy | 14 |
| API | List centre candidates with live examination session status | Medium | 6 |
| API | Get single candidate live session progress detail | Medium | 6 |
| API | Get session monitoring aggregate counts for status header | Medium | 6 |
| Database | Centre live session status read access over examination conduct states | Medium | 0.3 |
| Integration | Poll examination session state updates from secure conduct module | Medium | 16 |
| Testing | Happy path status progression from activated through submitted completed | Medium | 0.3 |
| Testing | Centre isolation on live monitoring candidate list | Medium | 0.3 |
| Testing | Auto-refresh stale data and session end summary count accuracy | Easy | 0.25 |
| Testing | Monitoring view for candidate with not-started conduct state after activation | Easy | 0.25 |
| Documentation | Live monitoring invigilator runbook during examination | Medium | 0.3 |
| Documentation | Monitoring conduct status terminology technical notes | Simple | 0.1 |

## 09 Secure Examination Conduct

845.1 hours · 188 tasks · Business

Authorised-centre-only examination delivery including login validation, secure interface, timing, activity capture, and submission.

### F09-001 Examination Credential Login and Session Gate

115.5 hours · Go-live · 26 tasks

##### Description

Allows a candidate to authenticate for an allotted examination session using system-generated examination credentials, validating identity, centre, session, schedule window, allocation, and centre activation before granting access to the secure examination conduct flow.

##### Business objective

Ensure only the correctly allocated candidate can begin an examination at the authorised centre during the approved session window, using credentials issued for that specific attempt.

##### Actors

- Candidate
- Examination Centre/Invigilator User

##### User journey

1. Candidate arrives at the allotted authorised examination centre and opens the secure examination login page on the assigned centre computer.
2. Candidate enters examination credential fields provided via hall ticket or secure distribution (credential identifier and secret).
3. System validates credential authenticity against issued credential records from Module 06.
4. System validates that the candidate record linked to the credential matches the registration and allocation.
5. System validates that login is attempted from the candidate's allotted examination centre.
6. System validates that the candidate is assigned to the current examination session and seat/computer where applicable.
7. System validates current date-time against session reporting time, session start time, and late-entry policy if configured.
8. System checks whether the centre invigilator has activated the candidate session in Module 08.
9. If activation is pending, candidate sees a waiting state with session details and cannot enter the examination interface.
10. If all gates pass, system creates an examination conduct session and routes the candidate to question paper assembly.
11. If any gate fails, candidate sees a specific denial reason and guidance without exposing sensitive validation internals.

##### Functional capabilities

- Render secure examination credential login form
- Validate issued examination credential identifier and secret
- Match credential to candidate registration and allocation record
- Validate login centre against allotted centre
- Validate login against assigned examination session
- Validate login against seat or computer assignment when allocated
- Enforce session reporting-time and start-time window rules
- Detect cancelled or suspended examination session
- Check centre session activation status from centre operations
- Display waiting-for-activation state when session not yet activated
- Display field-level and rule-level login denial messages
- Persist login attempt outcome for audit
- Create candidate examination conduct session on successful gate

##### Inputs

- Examination credential identifier
- Examination credential secret
- Client centre context identifier
- Client session context identifier
- Client device identifier snapshot
- Client network identifier snapshot
- Current server timestamp

##### Outputs

- Examination conduct session token
- Login success confirmation with session metadata
- Login denial response with reason code
- Waiting-for-activation status view
- Login attempt audit record

##### Business rules

- Examination login is permitted only with system-generated credentials issued for the specific candidate attempt.
- Login is denied when the candidate is not allocated to the centre from which login is attempted.
- Login is denied when the candidate is not allocated to the active examination session.
- Login is denied outside the configured reporting-time and examination-start window unless a late-entry rule explicitly allows it.
- Login is denied when the examination session is cancelled or suspended.
- Login to the examination interface is blocked until centre invigilator activation is recorded in Module 08.
- Failed login attempts are recorded without revealing which individual validation rule failed beyond safe user messaging.

##### Validations

- Credential identifier is required and must match an active issued credential record.
- Credential secret is required and must match the stored hash for the issued credential.
- Credential must not be expired or revoked.
- Credential must belong to the candidate attempt in scheduled or in-progress state.
- Allotted centre identifier must match centre context supplied at login.
- Session identifier must match candidate session allocation.
- Seat or computer assignment must match assigned resource when seat-level allocation exists.
- Current timestamp must fall within reporting-time to end-of-late-entry window.
- Session status must not be cancelled or suspended.
- Activation status must be active before examination interface access is granted.

##### Calculations

- Remaining minutes until session start when candidate arrives before start time.
- Late-entry eligibility based on configured grace period from Module 04 examination configuration consumed at runtime.

##### Workflow

CredentialSubmitted → ValidatingCredential → ValidatingAllocation → ValidatingScheduleWindow → CheckingActivation → AwaitingActivation | SessionCreated → ReadyForPaperAssembly; any validation failure transitions to LoginDenied with immutable attempt log.

##### Search requirements

- Lookup issued credential by credential identifier for validation only; no candidate-facing search register in this feature.

##### Documents

- Hall ticket credential reference used by candidate at login; document generation is out of scope in Module 06.

##### Reports

- Login attempt outcomes available to downstream administration reporting in Module 12; no standalone report UI in this feature.

##### Notifications

- No direct candidate notification dispatch in this feature; failed login messaging is on-screen only.

##### Security

- Credential secret validated using stored secure hash comparison.
- Rate limiting on repeated failed login attempts per credential and client endpoint.
- Login denial messages avoid disclosing whether credential identifier or secret was incorrect.
- Examination conduct session token issued only after all gate validations pass.

##### Integrations

- Module 06 Examination Credential Generation and Secure Distribution Handoff for issued credential validation.
- Module 06 Candidate Centre and Session Allocation for centre and session matching.
- Module 03 Authorised Examination Centre Master for centre identity resolution.
- Module 08 Candidate Examination Session Activation for activation status check.

##### Dependencies

- F06-005 Examination Credential Generation and Secure Distribution Handoff
- F06-003 Candidate Centre and Session Allocation
- F08-004 Candidate Examination Session Activation
- F03-004 Authorised Centre Access Restriction Configuration

##### Assumptions

- Examination credentials are issued before examination day by Module 06.
- Centre context identifier is available from centre-locked examination client deployment.
- Late-entry grace rules are configured in Module 04 and readable at login validation time.

##### Risks

- Clock skew between centre clients and server may affect schedule window validation unless centrally synchronized.
- Shared hall ticket exposure could allow credential use from wrong centre if centre enforcement in Feature 002 fails.

##### Non-functional requirements

- Login validation response within 2 seconds under nominal centre load.
- Login gate available during entire scheduled session window with high availability matching examination conduct SLA.

##### Notes

Consumes system-generated credentials from Module 06; does not generate credentials or hall tickets.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination credential login form with identifier and secret fields | Easy | 14 |
| UI | Invalid credential denial screen with safe generic messaging | Simple | 5 |
| UI | Wrong centre denial screen with allotted centre reference | Simple | 5 |
| UI | Outside schedule window denial screen with reporting and start times | Simple | 5 |
| UI | Waiting-for-invigilator-activation read-only status page | Simple | 5 |
| UI | Cancelled or suspended session denial screen | Simple | 5 |
| API | Validate issued examination credential identifier and secret | Medium | 6 |
| API | Match credential to candidate registration and attempt record | Medium | 6 |
| API | Validate login centre against candidate allotted centre | Medium | 6 |
| API | Validate login against assigned examination session | Medium | 6 |
| API | Validate login against assigned seat or computer when allocated | Medium | 6 |
| API | Enforce reporting-time and examination-start schedule window | Complex | 8 |
| API | Reject login for cancelled or suspended session | Easy | 4 |
| API | Fetch centre session activation status gate | Easy | 4 |
| API | Create candidate examination conduct session on successful gate | Complex | 8 |
| Database | Examination login attempt persistence with outcome reason code | Easy | 0.25 |
| Database | Candidate examination conduct session core record | Medium | 0.3 |
| Integration | Issued credential lookup handoff from Module 06 | Easy | 8 |
| Integration | Candidate allocation lookup handoff from Module 06 | Easy | 8 |
| Integration | Centre activation status lookup handoff from Module 08 | Simple | 4 |
| Testing | Successful login at correct centre within schedule window | Medium | 0.3 |
| Testing | Invalid credential and revoked credential rejection cases | Medium | 0.3 |
| Testing | Wrong centre wrong session and wrong seat rejection cases | Complex | 0.5 |
| Testing | Out-of-window cancelled session and pre-activation blocking cases | Medium | 0.3 |
| Documentation | Candidate examination login user runbook | Easy | 0.25 |
| Documentation | Technical notes on login validation chain and reason codes | Medium | 0.3 |

### F09-002 Authorised Centre Device and Network Enforcement

106.75 hours · Go-live · 24 tasks

##### Description

Technically enforces that examination conduct occurs only from authorised examination centres, approved devices, and approved networks, validating at login and continuously during an active session with termination on persistent violation.

##### Business objective

Prevent candidates from taking examinations from home, personal devices, unauthorised networks, or centres other than their allotted authorised centre.

##### Actors

- Candidate
- Examination Centre/Invigilator User

##### User journey

1. After credential validation, system captures client centre identifier, device fingerprint, and network address snapshot.
2. System resolves centre identity against authorised centre registry from Module 03.
3. System confirms candidate-centre allocation mapping matches resolved centre.
4. System evaluates device against centre-approved device rules when configured.
5. System evaluates network address against centre-approved network rules when configured.
6. If enforcement fails at login, candidate sees access blocked screen with approved reason code.
7. If enforcement passes, candidate proceeds to examination conduct with enforcement token bound to session.
8. During active examination, system periodically re-validates centre, device, and network context.
9. On transient network blip, candidate sees reconnect warning with grace timer per policy.
10. On persistent enforcement failure, system transitions session to TerminatedEnforcement and blocks further responses.
11. Enforcement events are recorded for audit and centre monitoring visibility in Module 08.

##### Functional capabilities

- Capture client centre device and network snapshot at login
- Resolve centre identity against authorised centre registry
- Validate candidate-centre allocation against resolved centre
- Validate device against centre device allow rules
- Validate network against centre network allow rules
- Display access blocked screen with reason code at login
- Bind enforcement context token to active examination session
- Periodic re-validation of centre device network during active session
- Display reconnect warning on transient enforcement failure
- Terminate session on persistent enforcement violation
- Persist enforcement pass and fail events with snapshots

##### Inputs

- Client centre identifier
- Device fingerprint attributes
- Client IP address
- Network segment metadata when available
- Candidate examination conduct session identifier
- Authorised centre restriction rules from Module 03

##### Outputs

- Enforcement pass or fail decision
- Access blocked reason code
- Enforcement-bound session token
- Reconnect warning state
- Enforcement termination record
- Enforcement event audit entries

##### Business rules

- Examination access is denied when login centre cannot be resolved to an authorised active centre.
- Examination access is denied when resolved centre does not match candidate allotted centre.
- When centre device rules are configured, login device must match an approved centre device record.
- When centre network rules are configured, client network must match approved centre network ranges.
- Enforcement re-checks continue throughout active examination at configured interval.
- Transient network loss may allow grace period before session termination based on approved policy.
- Persistent enforcement failure terminates examination conduct session without manual submit.

##### Validations

- Centre identifier must resolve to an active authorised examination centre.
- Resolved centre must equal candidate allotted centre identifier.
- Device fingerprint must match at least one approved centre device when device restriction enabled.
- Client IP must fall within approved centre network CIDR list when network restriction enabled.
- Enforcement token must remain bound to original device fingerprint for session lifetime when binding enabled.
- Re-validation interval must not be bypassed by client-side timer manipulation.

##### Calculations

- Grace period remaining during transient network enforcement failure.
- Count of consecutive enforcement failures before session termination.

##### Workflow

CapturingContext → ValidatingCentre → ValidatingDevice → ValidatingNetwork → EnforcementPassed → ActiveMonitoring → TransientWarning | TerminatedEnforcement; login failure transitions to AccessBlocked.

##### Search requirements

- Resolve authorised centre by centre identifier.
- Lookup centre device allow list by centre identifier.
- Lookup centre network allow list by centre identifier.

##### Reports

- Enforcement failure events feed centre live monitoring in Module 08.

##### Notifications

- On-screen reconnect warning only; no outbound notification in this feature.

##### Security

- Enforcement decisions made server-side using client-reported and server-observed network attributes.
- Session termination on enforcement failure is immediate and cannot be reversed by candidate.
- Enforcement snapshots stored for post-examination audit.

##### Integrations

- Module 03 Authorised Examination Centre Master Lifecycle for centre resolution.
- Module 03 Authorised Centre Access Restriction Configuration for device and network rules.
- Module 08 Centre Live Examination Session Monitoring for enforcement alert visibility.

##### Dependencies

- F03-001 Authorised Examination Centre Master Lifecycle
- F03-004 Authorised Centre Access Restriction Configuration
- F03-002 Centre Capacity and Infrastructure Configuration
- F09-001 Examination Credential Login and Session Gate

##### Assumptions

- Centre examination clients are deployed on centre-managed computers with stable centre identifier provisioning.
- Network allow lists are maintained by examination administrators in Module 03 before examination day.

##### Risks

- Centre network reconfiguration on examination day may cause false enforcement failures.
- Device fingerprint drift after browser update may require centre IT intervention.

##### Non-functional requirements

- Initial enforcement check completes within 1 second of login gate completion.
- Periodic re-validation imposes negligible impact on examination interface responsiveness.

##### Notes

Technical enforcement during login and continuously during active examination; complements centre restriction configuration in Module 03.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Access blocked screen for unauthorised centre | Simple | 5 |
| UI | Access blocked screen for unapproved device | Simple | 5 |
| UI | Access blocked screen for unapproved network | Simple | 5 |
| UI | Transient network reconnect warning banner with grace countdown | Medium | 16 |
| UI | Enforcement termination full-screen lock with reason code | Simple | 5 |
| API | Resolve client centre identifier against authorised centre registry | Easy | 4 |
| API | Validate candidate-centre allocation against resolved centre | Medium | 6 |
| API | Validate client device against centre device allow rules | Medium | 6 |
| API | Validate client network against centre network allow rules | Medium | 6 |
| API | Bind enforcement context token to examination conduct session | Complex | 8 |
| API | Periodic centre device network re-validation during active session | Complex | 8 |
| API | Apply transient enforcement grace period policy | Medium | 6 |
| API | Terminate session on persistent enforcement violation | Complex | 8 |
| Database | Enforcement event log with device and network snapshots | Medium | 0.3 |
| Database | Session enforcement binding record with grace state | Easy | 0.25 |
| Integration | Authorised centre registry lookup from Module 03 | Simple | 4 |
| Integration | Centre device and network restriction rule lookup from Module 03 | Easy | 8 |
| Integration | Enforcement alert feed to Module 08 live monitoring | Simple | 4 |
| Testing | Approved centre device and network login happy path | Medium | 0.3 |
| Testing | Home network and wrong centre rejection at login | Complex | 0.5 |
| Testing | Mid-examination network loss grace and termination paths | Complex | 0.5 |
| Testing | Device fingerprint mismatch and bypass attempt cases | Medium | 0.3 |
| Documentation | Centre IT setup guide for device and network enforcement | Medium | 0.3 |
| Documentation | Technical troubleshooting notes for enforcement reason codes | Medium | 0.3 |

### F09-003 Dynamic Question Paper Assembly and Personalisation

83 hours · Go-live · 22 tasks

##### Description

Assembles a unique immutable question paper for each candidate examination session by applying configured random selection rules, version assignment, question order randomisation, and answer option randomisation at examination start.

##### Business objective

Deliver a fair, unpredictable, and auditably unique question paper per candidate while preserving examination integrity and immutability throughout the session.

##### Actors

- Candidate

##### User journey

1. After login gate and enforcement pass, candidate session transitions to paper assembly state.
2. Candidate sees question paper loading progress screen.
3. System reads examination random selection rules and version settings from Module 04 configuration.
4. System selects questions from approved question bank pool per category and count rules.
5. System assigns a question paper version identifier to the candidate session.
6. System randomises question display order per approved settings.
7. System randomises answer option order per question where applicable.
8. System persists a frozen paper snapshot bound to the session.
9. On success, candidate transitions to secure examination interface with assembled paper.
10. On assembly failure due to pool insufficiency or rule conflict, candidate sees failure screen with retry option.
11. On session refresh, candidate receives the same frozen paper without re-randomisation.

##### Functional capabilities

- Display question paper assembly progress screen
- Load examination random selection rules for session
- Select questions from approved pool per category counts
- Assign question paper version to candidate session
- Randomise question order for candidate session
- Randomise answer option order per question
- Persist frozen question paper snapshot
- Serve assembled paper to examination interface
- Display assembly failure screen with retry action
- Return existing frozen paper on session resume without re-randomisation

##### Inputs

- Candidate examination conduct session identifier
- Examination identifier
- Random selection rules from Module 04
- Multiple version and randomisation settings from Module 04
- Approved question bank items from Module 04
- Server-side random seed policy

##### Outputs

- Assigned question paper version identifier
- Ordered question list with randomised options
- Frozen paper snapshot identifier
- Assembly failure reason code
- Assembly audit record

##### Business rules

- Question paper is assembled once per candidate examination session.
- Assembled paper is immutable for the session lifetime.
- Random selection must satisfy all configured category count and difficulty rules.
- Version assignment follows configured multiple-version policy from Module 04.
- Re-login or refresh must not alter previously assigned paper content or order.
- Assembly failure blocks examination start until successful retry or administrator intervention.

##### Validations

- Question pool must contain sufficient approved items for each required category.
- Selected questions must be in approved active status from question bank.
- Version assignment must reference a valid configured version slot.
- Randomisation must produce unique option mapping per question without empty option sets.
- Frozen snapshot must include question identifiers, order indices, and option mappings.
- Retry is blocked when session is already in in-progress or submitted state.

##### Calculations

- Per-category question count fulfillment check against selection rules.
- Deterministic random seed derivation from session identifier and examination identifier for reproducible audit.

##### Workflow

AssemblyRequested → LoadingRules → SelectingQuestions → AssigningVersion → RandomisingOrder → RandomisingOptions → SnapshotPersisted → PaperReady; insufficient pool transitions to AssemblyFailed → RetryAssembly | AdministratorEscalation.

##### Search requirements

- Retrieve approved question pool filtered by examination and category for selection engine.
- Retrieve existing frozen snapshot by session identifier on resume.

##### Reports

- Assigned version and question identifiers available to downstream evaluation in Module 10.

##### Security

- Correct answer keys are not exposed to candidate client in assembled payload.
- Assembly random seed and snapshot identifiers stored for audit reconstruction.
- Paper content served only to authenticated active session token.

##### Integrations

- Module 04 Random Question Selection Rules for selection criteria.
- Module 04 Multiple Question Paper Version and Randomisation Settings for version and shuffle policy.
- Module 04 Question Bank Item Lifecycle for approved question retrieval.

##### Dependencies

- F04-005 Random Question Selection Rules
- F04-006 Multiple Question Paper Version and Randomisation Settings
- F04-002 Question Bank Item Lifecycle and Answer Key Management
- F09-001 Examination Credential Login and Session Gate

##### Assumptions

- Question bank contains sufficient approved items before examination day.
- Examination configuration in Module 04 defines all selection and randomisation parameters consumed at runtime.

##### Risks

- Insufficient pool depth may block examination start for late sessions if bank changes occur after scheduling.
- Randomisation defects could cause duplicate exposure patterns detectable by candidates if seed policy is weak.

##### Non-functional requirements

- Paper assembly completes within 5 seconds for standard examination size under nominal load.
- Snapshot storage supports concurrent assembly for full centre capacity.

##### Notes

Runtime assembly only; question bank maintenance and rule configuration remain in Module 04.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Question paper assembly progress screen | Simple | 5 |
| UI | Assembly failure screen with retry action | Simple | 5 |
| API | Load random selection rules for examination session | Easy | 4 |
| API | Select questions from approved pool per category rules | Very high | 12 |
| API | Assign question paper version to candidate session | Medium | 6 |
| API | Randomise question display order for session | Medium | 6 |
| API | Randomise answer option order per question | Medium | 6 |
| API | Persist frozen question paper snapshot | Complex | 8 |
| API | Serve assembled paper to examination interface | Medium | 6 |
| API | Return existing frozen paper on session resume | Medium | 6 |
| Database | Candidate session question paper assignment record | Medium | 0.3 |
| Database | Frozen question order and option mapping storage | Complex | 0.5 |
| Database | Version and selection rule reference linkage | Easy | 0.25 |
| Integration | Random selection rule retrieval from Module 04 | Simple | 4 |
| Integration | Version and randomisation setting retrieval from Module 04 | Simple | 4 |
| Integration | Approved question bank item retrieval from Module 04 | Easy | 8 |
| Testing | Happy path assembly with order and option randomisation | Complex | 0.5 |
| Testing | Insufficient pool and rule conflict failure cases | Medium | 0.3 |
| Testing | Session resume immutability without re-randomisation | Medium | 0.3 |
| Testing | Answer key non-exposure in client payload verification | Medium | 0.3 |
| Documentation | Administrator runbook on assembly behaviour and retry | Easy | 0.25 |
| Documentation | Technical notes on random seed and snapshot audit reconstruction | Medium | 0.3 |

### F09-004 Secure Examination Interface and Response Capture

180.35 hours · Go-live · 27 tasks

##### Description

Provides the secure candidate examination interface for navigating assembled questions, capturing and auto-saving responses, displaying progress and remaining time, and preparing for submission confirmation.

##### Business objective

Enable candidates to complete examinations reliably with continuous response preservation, clear navigation, and secure interaction constraints during the active session.

##### Actors

- Candidate

##### User journey

1. Candidate enters examination interface after paper assembly completes.
2. Candidate sees examination shell with question panel, navigation panel, timer area, and auto-save indicator.
3. Candidate views first question with response controls appropriate to question type.
4. Candidate selects or enters a response; system auto-saves draft within seconds.
5. Candidate navigates to another question using navigation panel or next/previous controls.
6. Candidate marks a question for review; navigation panel updates status chip.
7. Candidate clears a response via clear action and confirms in dialog.
8. Auto-save indicator shows saving, saved, or error retry state.
9. If connection is lost, candidate sees offline banner; responses queue until reconnect.
10. Candidate reviews navigation summary showing attempted, unattempted, and marked counts.
11. Candidate initiates submit flow routed to submission feature when ready or when timer expires.

##### Functional capabilities

- Render examination shell layout with timer and auto-save areas
- Render question navigation panel with status chips
- Render single-question view with type-specific response controls
- Capture single-choice response selection
- Capture multiple-choice response selection
- Capture numeric response entry where applicable
- Capture text response entry where applicable
- Toggle mark-for-review per question
- Clear response with confirmation dialog
- Auto-save draft response on change
- Display auto-save status indicator
- Display connection loss offline banner
- Recover queued responses after reconnect
- Display navigation summary counts
- Block interface interaction after response lock from submission

##### Inputs

- Assembled question paper payload
- Question identifier
- Response value by question type
- Mark-for-review flag
- Client connectivity state
- Session lock status

##### Outputs

- Saved draft response records
- Navigation summary counts
- Auto-save status events
- Offline queue recovery outcome
- Read-only locked interface state

##### Business rules

- Responses auto-save without requiring manual save action.
- Mark-for-review does not count as attempted unless a response exists.
- Clear response requires explicit confirmation.
- Interface becomes read-only immediately upon submission lock.
- Offline responses are queued client-side and replayed in order on reconnect.
- Navigation remains available unless session is locked or terminated.

##### Validations

- Single-choice response must contain exactly one selected option identifier.
- Multiple-choice response must contain one or more valid option identifiers without duplicates.
- Numeric response must match configured numeric format and range when defined.
- Text response must not exceed configured maximum length.
- Response save rejected when session is locked or terminated.
- Question identifier must belong to session frozen paper snapshot.

##### Calculations

- Attempted question count based on non-empty saved responses.
- Unattempted question count as total minus attempted.
- Marked-for-review count independent of attempt status.

##### Workflow

PaperReady → InProgress ↔ AutoSaving ↔ OfflineQueued → ReadyToSubmit; submission lock transitions to ResponseLocked read-only state.

##### Search requirements

- Retrieve current session paper state and saved responses by session identifier.

##### Security

- Response payload excludes correct answer key material.
- Examination interface disables copy paste and context menu per security feature coordination.
- Auto-save requests require active authenticated session token.

##### Integrations

- Module 04 question type metadata for response control rendering.
- Feature F09-003 frozen paper snapshot for question content.
- Feature F09-005 timer display sync for remaining time area.

##### Dependencies

- F09-003 Dynamic Question Paper Assembly and Personalisation
- F04-002 Question Bank Item Lifecycle and Answer Key Management
- F09-006 Examination Session Security Controls

##### Assumptions

- Supported question types are limited to those configured in Module 04 for the examination.
- Centre network may have brief intermittent connectivity; offline queue duration is bounded by examination policy.

##### Risks

- Extended offline period may cause response loss if queue exceeds client storage limits.
- Large text responses may affect auto-save performance on low-spec centre hardware.

##### Non-functional requirements

- Auto-save completes within 1 second of response change under nominal conditions.
- Examination interface remains responsive for papers up to configured maximum question count.

##### Notes

Candidate-facing examination UI; scoring and result display are out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination shell layout with header timer and question panel | Complex | 18 |
| UI | Question navigation panel with attempted unattempted marked chips | Medium | 16 |
| UI | Single-choice question response control | Easy | 14 |
| UI | Multiple-choice question response control | Easy | 14 |
| UI | Numeric question response input control | Easy | 14 |
| UI | Text question response input control | Easy | 14 |
| UI | Mark-for-review toggle control per question | Simple | 5 |
| UI | Clear response confirmation dialog | Simple | 5 |
| UI | Auto-save status indicator component | Simple | 5 |
| UI | Connection loss offline banner with retry state | Medium | 16 |
| UI | Navigation summary counts panel before submit handoff | Easy | 14 |
| UI | Read-only locked interface state after submission lock | Simple | 5 |
| API | Fetch current session paper and saved response state | Medium | 6 |
| API | Auto-save single question draft response | Medium | 6 |
| API | Batch replay queued offline draft responses | Complex | 8 |
| API | Toggle mark-for-review flag for question | Easy | 4 |
| API | Clear question draft response | Easy | 4 |
| API | Retrieve navigation summary counts for session | Easy | 4 |
| API | Validate response format by question type | Medium | 6 |
| Database | Draft response storage with save timestamps | Medium | 0.3 |
| Database | Mark-for-review flag storage per question | Simple | 0.1 |
| Testing | Happy path navigation auto-save and mark-for-review | Medium | 0.3 |
| Testing | Invalid response format rejection by question type | Medium | 0.3 |
| Testing | Offline queue replay and conflict handling | Complex | 0.5 |
| Testing | Read-only behaviour after session response lock | Easy | 0.25 |
| Documentation | Candidate secure examination interface user guide | Medium | 0.3 |
| Documentation | Technical notes on auto-save frequency and offline replay | Medium | 0.3 |

### F09-005 Centrally Controlled Examination Timer

71.45 hours · Go-live · 19 tasks

##### Description

Controls the official examination duration from a central server clock, displays remaining time to the candidate, warns on low time, stops the examination at expiry, and triggers automatic submission.

##### Business objective

Ensure uniform examination duration enforcement across all centres independent of client device clock manipulation.

##### Actors

- Candidate

##### User journey

1. When candidate enters in-progress state, system initialises timer from examination duration configuration.
2. Candidate sees countdown timer in examination shell header.
3. System periodically syncs remaining time from server on configured interval.
4. When remaining time crosses low-time threshold, candidate sees warning banner.
5. Candidate continues responding while timer counts down.
6. At zero remaining time, system transitions session to TimerExpired state.
7. Candidate sees time-expired overlay and auto-submit in-progress modal.
8. System invokes automatic submission workflow in Feature 008.
9. After auto-submit completes, candidate sees submission outcome screen from submission feature.
10. If candidate attempts action after expiry before auto-submit completes, action is blocked.

##### Functional capabilities

- Initialise examination timer from configured duration
- Calculate server-authoritative remaining time
- Expose remaining time sync endpoint for client display
- Correct client display for clock drift
- Display countdown timer in examination interface
- Display low-time warning banner at threshold
- Display time-expired overlay at zero remaining
- Display auto-submit in-progress modal during expiry handling
- Transition session to TimerExpired state at zero
- Trigger automatic submission on timer expiry
- Block candidate actions after expiry pending submission completion
- Persist timer anchor and sync audit events

##### Inputs

- Examination duration from Module 04 configuration
- Session official start timestamp
- Current server timestamp
- Client-reported local timestamp for drift detection
- Low-time warning threshold configuration

##### Outputs

- Remaining seconds value for client display
- TimerExpired state transition
- Auto-submission trigger event
- Timer sync audit entries
- Low-time warning display state

##### Business rules

- Examination timer starts from official session start timestamp, not client login time, unless configured otherwise.
- Remaining time is calculated only on server; client display is advisory.
- Examination automatically stops at zero remaining time with no manual extension by candidate.
- Automatic submission is mandatory on timer expiry.
- Timer continues during brief offline periods using last known server sync plus elapsed server time.
- Invigilator manual time extension is out of scope in this module.

##### Validations

- Timer initialisation requires valid examination duration greater than zero.
- Official start timestamp must be recorded before in-progress timer begins.
- Sync requests rejected for locked submitted or terminated sessions.
- Client drift beyond tolerance triggers forced resync without resetting remaining time.

##### Calculations

- Remaining seconds equals configured duration minus elapsed server time since official start.
- Low-time warning when remaining seconds less than or equal to configured threshold.

##### Workflow

TimerInitialised → InProgress → LowTimeWarning → TimerExpired → AutoSubmitting → Submitted; drift detection loops ResyncDisplay without altering RemainingSeconds authority.

##### Search requirements

- Retrieve session timer state by examination conduct session identifier.

##### Reports

- Timer start and expiry timestamps available in activity recording for audit.

##### Security

- Client cannot extend remaining time via manipulated local clock.
- Timer expiry transition is idempotent to prevent duplicate auto-submission triggers.

##### Integrations

- Module 04 Examination Master Configuration for duration and warning threshold.
- Feature F09-008 Examination Submission for auto-submit on expiry.

##### Dependencies

- F04-004 Examination Master Configuration
- F09-004 Secure Examination Interface and Response Capture
- F09-008 Examination Submission and Response Locking

##### Assumptions

- Official session start timestamp is set when candidate transitions to in-progress after paper assembly.
- Examination duration is fixed per examination configuration without per-candidate variation.

##### Risks

- Server clock issues could affect all concurrent sessions simultaneously.
- Auto-submit at expiry during unsaved response may lose last unsynced client draft if offline queue exhausted.

##### Non-functional requirements

- Timer sync endpoint responds within 200 milliseconds under nominal load.
- Timer expiry processing initiates auto-submission within 2 seconds of reaching zero.

##### Notes

Server-authoritative timer; auto-submission handoff to Feature 008 on expiry.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Countdown timer display in examination header | Easy | 14 |
| UI | Low-time warning banner at configured threshold | Simple | 5 |
| UI | Time-expired full-screen overlay | Simple | 5 |
| UI | Auto-submit in-progress modal during expiry handling | Simple | 5 |
| API | Initialise timer from examination duration configuration | Medium | 6 |
| API | Calculate server-authoritative remaining seconds | Medium | 6 |
| API | Remaining time sync endpoint for client display | Easy | 4 |
| API | Detect and correct client clock drift without resetting authority | Medium | 6 |
| API | Transition session to TimerExpired state at zero remaining | Medium | 6 |
| API | Trigger automatic submission workflow on timer expiry | Complex | 8 |
| API | Block candidate actions after expiry pending submission | Easy | 4 |
| Database | Timer start anchor and official duration storage | Easy | 0.25 |
| Database | Timer sync and expiry audit event storage | Easy | 0.25 |
| Testing | Happy path countdown display and expiry auto-submit trigger | Medium | 0.3 |
| Testing | Client clock drift forced resync cases | Medium | 0.3 |
| Testing | Expiry during unsaved draft edge handling | Complex | 0.5 |
| Testing | Idempotent TimerExpired transition under duplicate sync calls | Medium | 0.3 |
| Documentation | Administrator runbook on timer behaviour and thresholds | Easy | 0.25 |
| Documentation | Technical notes on server clock authority and sync protocol | Medium | 0.3 |

### F09-006 Examination Session Security Controls

103.8 hours · Go-live · 23 tasks

##### Description

Enforces examination security controls including single active session per candidate, browser and session restrictions as approved, focus and visibility monitoring, and forced termination on critical violations.

##### Business objective

Reduce examination malpractice risk by preventing concurrent sessions and detecting disallowed client behaviour during conduct.

##### Actors

- Candidate
- Examination Centre/Invigilator User

##### User journey

1. On successful login, system registers active examination session token bound to client.
2. If candidate attempts second login elsewhere, system rejects with single-session enforcement alert.
3. Candidate enters secure examination chrome with restricted copy paste and context menu.
4. If fullscreen is required by policy, candidate sees fullscreen prompt before questions display.
5. During examination, system monitors tab visibility and window focus loss events.
6. On first focus loss, candidate sees warning banner per policy.
7. On repeated violations exceeding threshold, system transitions to TerminatedSecurity state.
8. Candidate sees session termination security violation screen with reason code.
9. Security events stream to activity recording and centre monitoring in Module 08.
10. Terminated session responses remain locked per submission rules.

##### Functional capabilities

- Register active examination session token on login
- Reject second concurrent session for same candidate attempt
- Invalidate prior session when policy allows replacement login
- Bind session token to browser session fingerprint
- Disable copy paste in examination chrome
- Disable context menu in examination chrome
- Prompt fullscreen mode when policy requires
- Record tab visibility change events
- Record window focus loss events
- Display focus loss warning banner
- Evaluate security violation counts against threshold
- Force terminate session on critical violation threshold
- Display security termination screen with reason code
- Stream security events to activity recording

##### Inputs

- Candidate examination conduct session identifier
- Client browser session fingerprint
- Tab visibility state events
- Window focus state events
- Approved security policy configuration
- Violation threshold configuration

##### Outputs

- Active session registry entry
- Concurrent login rejection response
- Security violation events
- Warning banner state
- TerminatedSecurity session state
- Security termination reason code

##### Business rules

- Only one active examination conduct session is permitted per candidate attempt at a time.
- Second login attempt is blocked unless policy explicitly allows session takeover.
- Approved browser restrictions are enforced for entire in-progress session.
- Focus and tab visibility violations accumulate toward termination threshold.
- Critical violation immediate termination applies when configured for specific event types.
- Security termination locks responses and prevents manual submit without invigilator escalation path defined out of scope.

##### Validations

- Session token must match registered active token for request processing.
- Browser session fingerprint must match bound fingerprint when binding enabled.
- Concurrent session check compares candidate attempt identifier not merely credential.
- Violation count resets only on new attempt not mid-session refresh.
- Security events rejected when session already submitted or terminated.

##### Calculations

- Accumulated violation count by event type within session.
- Remaining warnings before termination equals threshold minus current count.

##### Workflow

SessionRegistered → SecuredChrome → Monitoring → WarningIssued → TerminatedSecurity; concurrent login attempt transitions to ConcurrentSessionBlocked.

##### Search requirements

- Lookup active session registry by candidate attempt identifier.

##### Reports

- Security violation summary visible on centre live monitoring in Module 08.

##### Security

- Session tokens are non-guessable and rotated on successful login.
- Security termination is server-authoritative and cannot be dismissed by client.
- Violation thresholds configurable per examination from Module 04 consumed at runtime.

##### Integrations

- Module 04 Examination Master Configuration for approved restriction policy flags.
- Module 08 Centre Live Examination Session Monitoring for violation visibility.
- Feature F09-007 Examination Activity Recording for security event persistence.

##### Dependencies

- F04-004 Examination Master Configuration
- F09-001 Examination Credential Login and Session Gate
- F09-007 Examination Activity Recording
- F08-005 Centre Live Examination Session Monitoring

##### Assumptions

- Examination clients use supported modern browsers capable of visibility and focus APIs.
- Approved restriction set is signed off by examination authority before go-live.

##### Risks

- False positives from legitimate invigilator interactions may trigger warnings if policy thresholds are too aggressive.
- Browser compatibility gaps may limit effectiveness of specific restrictions.

##### Non-functional requirements

- Security event ingestion handles burst events without examination interface lag.
- Concurrent session check completes within login gate time budget.

##### Notes

Implements approved browser and session restrictions; standalone audit-log product is out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Single-session enforcement alert on duplicate login attempt | Simple | 5 |
| UI | Fullscreen requirement prompt before examination start | Simple | 5 |
| UI | Tab visibility focus loss warning banner | Easy | 14 |
| UI | Security violation session termination screen | Simple | 5 |
| UI | Secure examination chrome with copy paste disabled | Medium | 16 |
| API | Register active examination session token | Medium | 6 |
| API | Reject second concurrent session for candidate attempt | Medium | 6 |
| API | Invalidate prior session on approved takeover login | Complex | 8 |
| API | Bind session token to browser session fingerprint | Medium | 6 |
| API | Ingest tab visibility change security events | Easy | 4 |
| API | Ingest window focus loss security events | Easy | 4 |
| API | Evaluate violation count against termination threshold | Medium | 6 |
| API | Force terminate session on critical security threshold | Complex | 8 |
| Database | Active session registry with device binding | Medium | 0.3 |
| Database | Security violation event stream storage | Medium | 0.3 |
| Integration | Security policy flag retrieval from Module 04 | Simple | 4 |
| Integration | Security alert feed to Module 08 live monitoring | Simple | 4 |
| Testing | Happy path single session maintained throughout examination | Medium | 0.3 |
| Testing | Duplicate login blocked and takeover policy path | Complex | 0.5 |
| Testing | Focus loss accumulation and termination threshold cases | Complex | 0.5 |
| Testing | Client restriction bypass attempt handling | Medium | 0.3 |
| Documentation | Approved security controls configuration guide for administrators | Medium | 0.3 |
| Documentation | Technical security event catalogue and threshold reference | Medium | 0.3 |

### F09-007 Examination Activity Recording

65.05 hours · Go-live · 22 tasks

##### Description

Records a comprehensive examination activity trail including login, start, response saves, navigation, version assignment, centre and device context, abnormal events, and submission timestamps for audit and monitoring.

##### Business objective

Provide defensible examination conduct evidence for dispute resolution, monitoring, and downstream administration reporting without relying on a separate audit product.

##### Actors

- Candidate
- Examination Centre/Invigilator User

##### User journey

1. System records login timestamp and credential context when login gate succeeds.
2. System records enforcement snapshot at session start.
3. System records official examination start timestamp when paper assembly completes and in-progress begins.
4. Each auto-save persists a response activity event with question identifier and timestamp.
5. Each navigation action records from-question and to-question identifiers.
6. System records assigned paper version and question identifiers at assembly time.
7. System records centre identifier, device snapshot, and network snapshot on material changes.
8. Security and enforcement abnormal events append to activity stream with classification.
9. System records manual or automatic submission timestamp with submission type.
10. Authorised invigilator monitoring in Module 08 reads abnormal indicators derived from this stream.
11. Authorised administrators query activity timeline through downstream reporting in Module 12.

##### Functional capabilities

- Record login timestamp with credential and centre context
- Record official examination start timestamp
- Record response save activity per question
- Record question navigation from-to events
- Record assigned paper version identifier
- Record assigned question identifier set reference
- Record centre identifier on session events
- Record device snapshot on material changes
- Record network snapshot on material changes
- Record security abnormal events with classification
- Record enforcement abnormal events with classification
- Record manual submission timestamp
- Record automatic submission timestamp
- Expose activity timeline query for authorised audit consumers
- Maintain append-only immutability for recorded events

##### Inputs

- Examination conduct session identifier
- Event type code
- Event timestamp
- Question identifier when applicable
- Response snapshot hash when applicable
- Paper version identifier
- Centre device network snapshots
- Abnormal event classification
- Submission type manual or automatic

##### Outputs

- Append-only activity event records
- Abnormal event flags for centre monitoring
- Activity timeline query results for audit consumers
- Response change history references

##### Business rules

- All material examination conduct actions generate an activity event.
- Activity events are append-only and cannot be edited or deleted by candidates.
- Response activity stores content hash or reference not necessarily full text for large entries per policy.
- Abnormal events include security violations, enforcement failures, and repeated auto-save errors.
- Activity recording continues until session reaches terminal submitted or terminated state.
- Activity data is retained per platform retention policy for examination records.

##### Validations

- Event timestamp must be server-generated or server-validated.
- Session identifier must exist and be in non-terminal state except for terminal event recording.
- Question identifier must belong to session frozen paper for question-scoped events.
- Event type must be from approved examination activity catalogue.
- Query access restricted to authorised roles via Module 01 authorization hooks.

##### Calculations

- Response change count per question from save event stream.
- Time between login and official start.
- Time between official start and submission.

##### Workflow

EventIngested → Appended → AvailableForMonitoring → ArchivedPerRetention; abnormal classification triggers AbnormalFlagged substate visible to Module 08.

##### Search requirements

- Query activity events by session identifier ordered by timestamp.
- Filter activity events by abnormal classification for monitoring feeds.
- Query response change history by session and question identifier.

##### Reports

- Activity timeline underpins Module 12 examination administration reporting.

##### Security

- Activity query endpoints enforce role permissions from Module 01.
- Sensitive credential secrets never stored in activity payloads.
- Append-only storage prevents tampering by application users.

##### Integrations

- Module 08 Centre Live Examination Session Monitoring for abnormal event indicators.
- Module 01 Downstream Module Authorization Integration Hooks for query access control.
- Module 12 Examination Administration and Reporting as downstream consumer.

##### Dependencies

- F09-001 Examination Credential Login and Session Gate
- F09-002 Authorised Centre Device and Network Enforcement
- F09-003 Dynamic Question Paper Assembly and Personalisation
- F09-004 Secure Examination Interface and Response Capture
- F09-006 Examination Session Security Controls
- F09-008 Examination Submission and Response Locking
- F01-006 Downstream Module Authorization Integration Hooks

##### Assumptions

- Event ingestion is synchronous for critical events and asynchronous for high-volume navigation events if performance requires.
- Module 12 provides reporting UI; this feature provides recording and query capability only.

##### Risks

- High-volume navigation logging may increase storage costs for large candidate counts.
- Incomplete event ingestion during server outage may create audit gaps.

##### Non-functional requirements

- Critical event ingestion adds less than 50 milliseconds to request path under nominal load.
- Activity query by session returns within 3 seconds for full examination timeline.

##### Notes

Records conduct audit trail; standalone audit-log product and scoring are out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| API | Record login timestamp with credential and centre context | Easy | 4 |
| API | Record official examination start timestamp | Easy | 4 |
| API | Record response save activity per question | Medium | 6 |
| API | Record question navigation from-to event | Easy | 4 |
| API | Record assigned paper version identifier at assembly | Easy | 4 |
| API | Record centre device network snapshot on material change | Medium | 6 |
| API | Record security abnormal event with classification | Medium | 6 |
| API | Record enforcement abnormal event with classification | Medium | 6 |
| API | Record manual submission timestamp event | Easy | 4 |
| API | Record automatic submission timestamp event | Easy | 4 |
| API | Query activity timeline by session for authorised auditors | Medium | 6 |
| Database | Append-only examination activity event store | Complex | 0.5 |
| Database | Response change history per question reference | Medium | 0.3 |
| Database | Abnormal event classification indexes | Easy | 0.25 |
| Integration | Abnormal event indicator feed to Module 08 monitoring | Simple | 4 |
| Integration | Authorisation hook for activity query from Module 01 | Simple | 4 |
| Testing | Happy path complete activity trail from login through submit | Complex | 0.5 |
| Testing | Event ordering immutability and append-only enforcement | Medium | 0.3 |
| Testing | Missing event resilience under transient failure | Medium | 0.3 |
| Testing | Unauthorised activity query rejection cases | Medium | 0.3 |
| Documentation | Activity record field guide for auditors and invigilators | Medium | 0.3 |
| Documentation | Technical notes on retention event catalogue and query access | Medium | 0.3 |

### F09-008 Examination Submission and Response Locking

119.2 hours · Go-live · 25 tasks

##### Description

Supports manual candidate submission with review and confirmation as well as automatic submission on timer expiry or approved termination paths, locking all responses upon submission completion.

##### Business objective

Finalise candidate examination attempts with immutable response locking suitable for downstream evaluation while giving candidates clear submission confirmation.

##### Actors

- Candidate

##### User journey

1. Candidate selects submit examination action from navigation summary.
2. Candidate sees review summary with attempted, unattempted, and marked counts.
3. If unattempted questions exist, candidate sees unattempted questions warning dialog.
4. Candidate confirms final submission in confirmation dialog.
5. System validates submission eligibility including session state and timer not already expired in conflicting manner.
6. System locks all responses preventing further edits.
7. System persists final response snapshot with submission type manual.
8. Candidate sees submission success read-only confirmation page.
9. If timer expires, system automatically initiates submission without candidate confirmation.
10. During auto-submit, candidate sees auto-submitted banner on confirmation page.
11. If submission fails due to transient error, candidate sees retry dialog until success or invigilator escalation.
12. Locked responses become available for Module 10 evaluation handoff.

##### Functional capabilities

- Display pre-submit review summary with question counts
- Display unattempted questions warning dialog
- Display final submission confirmation dialog
- Validate submission eligibility for session state
- Lock all responses on submit initiation
- Persist final response snapshot
- Record manual submission type
- Initiate automatic submission on timer expiry
- Initiate automatic submission on approved termination path when policy requires
- Record automatic submission type
- Generate submission receipt metadata
- Prevent further response updates after lock
- Display submission success confirmation page
- Display auto-submitted banner for expiry path
- Display submission failed retry dialog

##### Inputs

- Candidate examination conduct session identifier
- Current draft responses
- Submission trigger type manual automatic or termination
- Session timer state
- Session security or enforcement termination state

##### Outputs

- Submission record with type and timestamp
- Final locked response snapshot
- Submission receipt metadata for candidate display
- Response lock flags
- Evaluation handoff readiness status

##### Business rules

- Manual submission requires explicit candidate confirmation.
- Unattempted question warning is informational; submission may proceed if candidate confirms.
- Automatic submission on timer expiry does not require candidate confirmation.
- Once submitted, responses are immutable for the attempt.
- Double submission attempts are idempotent returning existing submission receipt.
- Submission blocked when session already terminated for enforcement unless policy allows salvage submit.
- Evaluation handoff occurs only after successful submission persistence.

##### Validations

- Submission rejected when session not in in-progress or timer-expired eligible state.
- Submission rejected when responses already locked.
- Final snapshot must include all saved draft responses at lock time.
- Submission receipt must include session identifier submission timestamp and type.
- Retry allowed only when prior submit attempt did not persist lock record.

##### Calculations

- Final attempted count at lock time.
- Final unattempted count at lock time.

##### Workflow

ReadyToSubmit → ReviewSummary → ConfirmSubmit → LockingResponses → PersistingFinal → Submitted; timer expiry transitions TimerExpired → AutoSubmitting → Submitted; transient failure transitions to SubmitFailed → RetrySubmit.

##### Search requirements

- Retrieve submission status by session identifier to enforce idempotency.

##### Documents

- Submission receipt metadata displayed to candidate; printable certificate is out of scope in Module 11.

##### Reports

- Submission counts and timestamps feed Module 12 administration reporting.

##### Notifications

- Optional examination lifecycle notification handoff to Module 07 on submission event subscription.

##### Security

- Submission lock is server-authoritative; client cannot unlock responses.
- Submission endpoints require active session token until lock completes.

##### Integrations

- Feature F09-005 Centrally Controlled Examination Timer for expiry trigger.
- Feature F09-007 Examination Activity Recording for submit events.
- Module 10 Evaluation and Results for locked response handoff.
- Module 07 Examination Lifecycle Event Subscription for optional submit notification.

##### Dependencies

- F09-004 Secure Examination Interface and Response Capture
- F09-005 Centrally Controlled Examination Timer
- F09-007 Examination Activity Recording
- F10-001 Evaluation and Results
- F07-003 Examination Lifecycle Event Subscription and Template Routing

##### Assumptions

- Module 10 consumes locked final snapshot via agreed handoff interface without scoring logic in this module.
- Transient submission failures are rare; retry UI sufficient for centre recovery.

##### Risks

- Partial lock during server failure could leave ambiguous state without idempotent retry design.
- Auto-submit at expiry with pending offline drafts may submit last synced state only.

##### Non-functional requirements

- Manual submission completes within 3 seconds under nominal load.
- Submission lock is strongly consistent before success confirmation displayed to candidate.

##### Notes

Manual and automatic submission; scoring in Module 10 is out of scope but locked responses must be handoff-ready.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Pre-submit review summary screen with question counts | Medium | 16 |
| UI | Unattempted questions warning dialog | Simple | 5 |
| UI | Final submission confirmation dialog | Simple | 5 |
| UI | Submission success read-only confirmation page | Easy | 14 |
| UI | Auto-submitted banner on expiry submission confirmation page | Simple | 5 |
| UI | Submission failed retry dialog | Simple | 5 |
| API | Validate submission eligibility for session state | Medium | 6 |
| API | Lock all responses on submit initiation | Complex | 8 |
| API | Persist final response snapshot for manual submit | Complex | 8 |
| API | Persist final response snapshot for automatic submit on timer expiry | Complex | 8 |
| API | Persist final response snapshot for approved termination auto-submit path | Complex | 8 |
| API | Generate submission receipt metadata | Easy | 4 |
| API | Prevent further response updates after lock | Medium | 6 |
| API | Idempotent resubmit returning existing receipt | Medium | 6 |
| Database | Submission record with manual or automatic type | Medium | 0.3 |
| Database | Final locked response snapshot storage | Complex | 0.5 |
| Database | Response lock flag persistence per session | Easy | 0.25 |
| Integration | Locked response handoff readiness signal to Module 10 | Easy | 8 |
| Integration | Optional submission event publish to Module 07 notification routing | Simple | 4 |
| Testing | Happy path manual submit with response lock verification | Complex | 0.5 |
| Testing | Automatic submit on timer expiry path | Medium | 0.3 |
| Testing | Submit blocked for invalid session state cases | Medium | 0.3 |
| Testing | Double submit idempotency and transient retry cases | Complex | 0.5 |
| Documentation | Candidate submission process user guide | Easy | 0.25 |
| Documentation | Technical notes on submission state machine and lock semantics | Medium | 0.3 |

## 10 Evaluation & Results

478.1 hours · 100 tasks · Business

Automatic objective examination evaluation, scoring, pass/fail determination, and governed result publication to candidates.

### F10-001 Post-Submission Objective Answer Evaluation

128.3 hours · Go-live · 25 tasks

##### Description

Automatically evaluates a candidate's locked objective examination responses immediately after submission by matching each recorded response against the configured answer key for the candidate's assembled question paper version, producing per-question outcomes and aggregate response counts without manual marking.

##### Business objective

Eliminate manual marking delay for objective examinations by producing auditable evaluation outcomes at submission time so downstream scoring, pass/fail determination, and governed publication can proceed without administrator intervention.

##### Actors

- Examination Administrator
- Candidate

##### User journey

1. Candidate completes secure examination conduct in Module 09 and submits responses, triggering response lock.
2. System receives submission-completed signal with candidate session, examination, and assembled paper version identifiers.
3. System validates that the session is in SUBMITTED state and that no prior successful evaluation exists for the same submission.
4. System loads the answer key aligned to the candidate's question paper version from Module 04 configuration.
5. System iterates each objective question on the paper and compares the candidate's selected or entered response to the configured correct answer(s).
6. System classifies each item as CORRECT, INCORRECT, or UNANSWERED according to examination evaluation rules.
7. System persists per-question evaluation outcomes and aggregate counts (correct, incorrect, unanswered).
8. System transitions evaluation status from PENDING to EVALUATED on success or to EVALUATION_FAILED on unrecoverable error.
9. Examination Administrator opens the evaluation monitoring register, filters by examination or session, and reviews evaluation status for submitted candidates.
10. Administrator opens evaluation detail to view per-question outcome summary without editing candidate responses.
11. If evaluation failed, Administrator reviews failure reason and initiates retry after underlying data issue is resolved.
12. On successful evaluation, system hands off to scoring feature for marks and pass/fail calculation.

##### Functional capabilities

- Accept post-submission evaluation trigger only for locked objective examination sessions
- Resolve answer key for the candidate's specific assembled question paper version
- Compare single-select objective responses against configured correct option
- Compare multi-select objective responses against configured correct option set with partial-match rules from examination configuration
- Classify blank or null responses as UNANSWERED
- Classify non-blank responses that do not match the key as INCORRECT
- Persist per-question evaluation outcome with question identifier and outcome code
- Persist aggregate correct, incorrect, and unanswered counts for the submission
- Enforce idempotent evaluation so duplicate submission signals do not create duplicate evaluation records
- Record evaluation start time, completion time, and triggering submission reference
- Expose evaluation status lifecycle for administrator monitoring
- Support administrator-initiated retry for failed evaluations after corrective action
- Block evaluation when submission is not in SUBMITTED or locked state
- Block evaluation when answer key is missing for the paper version

##### Inputs

- Submitted examination session identifier
- Candidate identifier
- Examination identifier
- Assembled question paper version identifier
- Locked candidate response set per question
- Answer key per question from examination configuration
- Examination evaluation rules reference from Module 04
- Submission timestamp and submission lock reference from Module 09

##### Outputs

- Evaluation record with status PENDING, EVALUATED, or EVALUATION_FAILED
- Per-question outcome list (CORRECT, INCORRECT, UNANSWERED)
- Aggregate correct count
- Aggregate incorrect count
- Aggregate unanswered count
- Evaluation failure reason code and message when applicable
- Evaluation completion timestamp

##### Business rules

- Evaluation runs automatically immediately after submission wherever the examination type is objective and auto-evaluation is enabled in examination configuration
- Subjective or manually marked items are out of scope and must not be auto-evaluated
- Each submission produces at most one successful evaluation record; retries replace or supersede failed attempts per policy without duplicating successful outcomes
- UNANSWERED applies when no response is recorded for a mandatory objective item
- Evaluation must use the answer key tied to the candidate's paper version, not a generic examination-level key
- Evaluation cannot proceed if submission locking from Module 09 is incomplete

##### Validations

- Submission session must exist and be in SUBMITTED state
- Response lock flag must be true before evaluation starts
- Assembled paper version identifier must be present and resolvable
- Answer key must exist for every objective question on the paper
- Question type must be objective; non-objective items are skipped or cause controlled failure based on examination configuration flag
- Duplicate evaluation request for an already EVALUATED submission must be rejected
- Retry is permitted only when current evaluation status is EVALUATION_FAILED

##### Calculations

- Correct count equals number of questions classified CORRECT
- Incorrect count equals number of questions classified INCORRECT
- Unanswered count equals number of questions classified UNANSWERED

##### Workflow

Submission SUBMITTED → Evaluation PENDING → Evaluation EVALUATED on success; Submission SUBMITTED → Evaluation PENDING → Evaluation EVALUATION_FAILED on error; Evaluation EVALUATION_FAILED → Evaluation PENDING on administrator retry → Evaluation EVALUATED or EVALUATION_FAILED

##### Search requirements

- Administrator register filter by examination name or identifier
- Filter by examination session or schedule date
- Filter by evaluation status (PENDING, EVALUATED, EVALUATION_FAILED)
- Filter by candidate registration number or name
- Sort by submission time and evaluation completion time

##### Security

- Only Examination Administrator role may view evaluation monitoring register and retry failed evaluations
- Candidates cannot access raw per-question key comparison until result publication rules allow
- Evaluation trigger endpoint accepts only internal service calls from examination conduct submission flow
- Audit log records evaluation trigger source, administrator retry actor, and timestamp

##### Integrations

- Examination submission and response lock handoff from Module 09 Secure Examination Conduct
- Answer key and paper version resolution from Module 04 Question Bank and Examination Configuration

##### Dependencies

- F09 — Secure Examination Conduct: Examination Submission and Response Locking
- F04 — Question Bank and Examination Configuration: Question Bank Item Lifecycle and Answer Key Management
- F04 — Question Bank and Examination Configuration: Multiple Question Paper Version and Randomisation Settings
- F04 — Question Bank and Examination Configuration: Examination Master Configuration
- F01 — User and Role Management: Downstream Module Authorization Integration Hooks

##### Assumptions

- Answer keys are maintained in Module 04 and available synchronously at evaluation time
- Only objective question types defined in the examination configuration participate in auto-evaluation
- Immediate evaluation is synchronous or near-synchronous from the candidate submission perspective; long-running batch reprocessing is out of scope

##### Risks

- Paper version mismatch between assembled paper and answer key could cause incorrect classification
- High concurrent submission volume at session end may require queueing not described in source document
- Partial multi-select scoring nuances depend on Module 04 rule completeness

##### Non-functional requirements

- Evaluation for a typical objective paper should complete within seconds of submission under normal load
- Evaluation operations must be idempotent and safe to retry on transient failure
- All evaluation steps must be logged for audit without storing sensitive answer key material in client-visible logs

##### Notes

Triggers immediately after examination submission from Module 09 wherever applicable; objective-type items only.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Administrator evaluation monitoring register with examination, session, status, and candidate filters | Medium | 16 |
| UI | Administrator evaluation detail read-only view with per-question outcome summary | Complex | 18 |
| UI | Evaluation register empty state when no submissions exist for selected filters | Simple | 5 |
| UI | Evaluation failed status error panel with failure reason display | Simple | 5 |
| UI | Administrator retry failed evaluation confirmation dialog | Simple | 5 |
| API | Internal post-submission evaluation trigger for locked objective sessions | Complex | 8 |
| API | List and search evaluation records with administrator filters | Medium | 6 |
| API | Fetch evaluation detail with per-question outcomes for administrator | Medium | 6 |
| API | Retry failed evaluation with idempotency guard | Medium | 6 |
| API | Single-select objective response comparison against answer key | Medium | 6 |
| API | Multi-select objective response comparison with configured partial-match rule | Complex | 8 |
| API | Aggregate correct incorrect and unanswered count computation | Easy | 4 |
| Database | Core examination evaluation header entity with status and submission reference | Medium | 0.3 |
| Database | Per-question evaluation outcome entity linked to evaluation header | Medium | 0.3 |
| Database | Evaluation status indexes for examination session and candidate lookup | Easy | 0.25 |
| Database | Evaluation retry and failure reason audit fields | Easy | 0.25 |
| Integration | Submission completed and response lock event consumption from examination conduct | Medium | 16 |
| Integration | Answer key fetch mapped to assembled paper version from examination configuration | Medium | 16 |
| Testing | Happy-path all-correct objective paper immediate evaluation after submission | Medium | 0.3 |
| Testing | Mixed correct incorrect and unanswered classification cases | Complex | 0.5 |
| Testing | Duplicate submission trigger idempotency rejection | Medium | 0.3 |
| Testing | Missing answer key and unsubmitted session negative validation cases | Medium | 0.3 |
| Testing | Administrator unauthorized access and cross-candidate evaluation detail denial | Easy | 0.25 |
| Documentation | Technical notes for objective evaluation matching and idempotency behaviour | Medium | 0.3 |
| Documentation | Administrator runbook for monitoring and retrying failed evaluations | Easy | 0.25 |

### F10-002 Examination Scoring and Pass Fail Determination

74.8 hours · Go-live · 20 tasks

##### Description

Calculates marks awarded per question, applies negative marking and examination-level scoring rules from configuration, derives total score, maximum marks, percentage, and pass or fail status for each evaluated objective submission.

##### Business objective

Provide consistent, rule-driven scoring and pass/fail outcomes aligned to each examination's configured marking scheme so results reflect department policy without manual calculation.

##### Actors

- Examination Administrator
- Candidate

##### User journey

1. System receives evaluation-completed event with per-question CORRECT, INCORRECT, and UNANSWERED outcomes.
2. System loads examination scoring configuration including per-question marks, negative mark value, and pass threshold from Module 04.
3. For each question, system applies marks for CORRECT responses per configured weight.
4. For each INCORRECT response where negative marking is enabled, system deducts configured negative marks floored at zero total per question policy.
5. For UNANSWERED responses, system applies zero marks unless configuration specifies alternate treatment.
6. System sums awarded marks and deducts aggregate negative marks to produce total score.
7. System calculates maximum attainable marks from the objective paper configuration.
8. System calculates percentage as total score divided by maximum marks rounded per configuration precision.
9. System compares percentage or absolute score against configured pass threshold to set PASS or FAIL status.
10. System persists score summary linked to the evaluation record.
11. Examination Administrator opens score summary on evaluation detail to review marks breakdown and pass/fail outcome.
12. Score summary becomes input to result publication when display rules include marks or pass/fail fields.

##### Functional capabilities

- Load per-question mark weight from examination configuration
- Apply full marks for CORRECT outcomes per question weight
- Apply zero marks for UNANSWERED outcomes unless alternate rule configured
- Apply configured negative mark deduction for INCORRECT outcomes when negative marking enabled
- Enforce per-question floor preventing negative question score where configured
- Sum total score across all evaluated objective questions
- Calculate maximum marks from configured question weights on the paper
- Calculate percentage with configured decimal precision
- Determine PASS or FAIL against configured cut-off threshold
- Persist score summary linked to evaluation record
- Expose read-only score breakdown to authorized administrators
- Block scoring when evaluation status is not EVALUATED

##### Inputs

- Evaluation record with EVALUATED status
- Per-question outcome codes from evaluation
- Per-question mark weight from examination configuration
- Negative marking enabled flag and negative mark value
- Pass threshold percentage or absolute score from examination configuration
- Percentage rounding precision from examination configuration

##### Outputs

- Per-question marks awarded
- Per-question negative marks deducted where applicable
- Total score
- Maximum marks
- Percentage score
- Pass or fail status flag
- Scoring completion timestamp

##### Business rules

- Scoring executes automatically immediately after successful objective evaluation
- Negative marks apply only when negative marking is enabled for the examination
- Total score cannot fall below zero for the examination unless configuration explicitly allows
- Pass/fail uses examination-configured threshold; absent threshold defaults to policy defined in Module 04 configuration
- UNANSWERED items score zero marks in default configuration
- Scoring uses only objective items evaluated in F10-001

##### Validations

- Evaluation must be in EVALUATED status before scoring starts
- Per-question mark weight must be non-negative numeric
- Negative mark value must be non-negative when negative marking enabled
- Pass threshold must be within valid percentage range 0–100 when percentage-based
- Maximum marks must be greater than zero for percentage calculation
- Duplicate scoring request for already scored evaluation must return existing summary without recalculation unless administrator override defined out of scope

##### Calculations

- Question marks awarded equals full weight for CORRECT else zero plus negative deduction for INCORRECT
- Total score equals sum of per-question net marks
- Maximum marks equals sum of per-question weights for evaluated objective items
- Percentage equals total score divided by maximum marks multiplied by 100 rounded per precision rule
- Pass/fail equals PASS when percentage or absolute score meets or exceeds threshold else FAIL

##### Workflow

Evaluation EVALUATED → Scoring PENDING → Scoring COMPLETED with PASS or FAIL outcome; Scoring blocked when evaluation not EVALUATED

##### Search requirements

- Administrator score summary accessible from evaluation detail by evaluation identifier
- Filter evaluation register by pass/fail status after scoring

##### Security

- Score breakdown visible to Examination Administrator only until publication display rules expose fields to candidates
- Scoring recalculation endpoints restricted to internal pipeline; manual override out of scope

##### Integrations

- Examination marking scheme and pass threshold from Module 04 Examination Master Configuration
- Evaluation outcome handoff from F10-001 post-submission evaluation

##### Dependencies

- F10-001 — Post-Submission Objective Answer Evaluation
- F04 — Question Bank and Examination Configuration: Examination Master Configuration
- F04 — Question Bank and Examination Configuration: Result Display, Certificate Eligibility and Examination Fee Configuration

##### Assumptions

- Examination configuration defines complete marking scheme for all objective questions on the paper
- Pass threshold is configured per examination in Module 04 before evaluation cycle
- Section-wise or subject-wise scoring splits are not in scope unless defined in examination configuration consumed as flat question list

##### Risks

- Configuration change after evaluation could cause inconsistency if scores are not snapshotted at evaluation time
- Floating-point rounding discrepancies may affect borderline pass/fail unless fixed precision enforced

##### Non-functional requirements

- Scoring must complete as part of immediate post-submission pipeline without separate batch delay
- Score results must be deterministic for identical inputs and configuration

##### Notes

Consumes evaluation outcomes from F10-001; applies marks and pass rules from Module 04 examination configuration.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Administrator score breakdown panel on evaluation detail with per-question marks | Medium | 16 |
| UI | Pass or fail status chip on evaluation monitoring register | Simple | 5 |
| UI | Total score and percentage summary header on evaluation detail | Simple | 5 |
| API | Execute scoring pipeline for evaluated submission | Complex | 8 |
| API | Apply per-question positive marks for correct outcomes | Medium | 6 |
| API | Apply negative mark deduction for incorrect outcomes when enabled | Complex | 8 |
| API | Compute total score maximum marks and percentage | Medium | 6 |
| API | Determine pass or fail against configured threshold | Medium | 6 |
| API | Fetch score summary for administrator by evaluation identifier | Easy | 4 |
| API | Load examination scoring rules from configuration at scoring time | Easy | 4 |
| Database | Score summary entity linked to evaluation with total percentage and pass flag | Medium | 0.3 |
| Database | Per-question marks awarded and negative marks deducted storage | Medium | 0.3 |
| Database | Configuration snapshot reference or denormalised scoring parameters on score summary | Easy | 0.25 |
| Integration | Examination marking scheme and pass threshold retrieval from configuration service | Simple | 4 |
| Testing | Happy-path scoring for all-correct paper with full marks and pass | Medium | 0.3 |
| Testing | Negative marking deduction and zero-floor boundary cases | Complex | 0.5 |
| Testing | Pass fail threshold boundary equal above and below cases | Medium | 0.3 |
| Testing | Unanswered zero marks and missing threshold validation rejection | Medium | 0.3 |
| Documentation | Technical notes for scoring formulas negative marking and rounding | Medium | 0.3 |
| Documentation | Administrator reference for interpreting score breakdown and pass fail status | Easy | 0.25 |

### F10-003 Evaluation Rules Configuration Alignment

50.25 hours · Go-live · 13 tasks

##### Description

Ensures automatic evaluation and scoring in Module 10 honour examination-specific evaluation rules configured in Module 04, including auto-evaluation eligibility, negative marking parameters, unanswered handling, partial-match behaviour, and immediate evaluation flags, with pre-flight validation before processing.

##### Business objective

Guarantee that post-submission evaluation behaviour matches each examination's approved configuration so departments can vary policies per examination without code changes.

##### Actors

- Examination Administrator

##### User journey

1. Examination submission triggers evaluation pre-flight check.
2. System loads evaluation rules bundle for the examination from Module 04 configuration.
3. System verifies auto-evaluation is enabled for the examination type.
4. System verifies required scoring parameters exist including mark weights and pass threshold.
5. System applies unanswered-handling rule when classifying responses during evaluation handoff.
6. System applies partial-match rule flag for multi-select items during answer comparison handoff.
7. System applies negative marking enabled flag during scoring handoff.
8. System records configuration rule version or snapshot identifier on evaluation record for traceability.
9. If any mandatory rule is missing, system marks evaluation as EVALUATION_FAILED with configuration error reason.
10. Administrator views configuration alignment status on evaluation detail showing rule snapshot summary.
11. Administrator resolves missing configuration in Module 04 and retries failed evaluation from F10-001.

##### Functional capabilities

- Load evaluation rules bundle by examination identifier at evaluation time
- Validate auto-evaluation enabled flag before starting evaluation
- Validate presence of answer key mapping for paper version before evaluation
- Validate presence of mark weights and pass threshold before scoring
- Apply unanswered handling rule during outcome classification
- Apply multi-select partial-match rule during answer comparison
- Apply negative marking enabled flag and value during scoring
- Persist configuration snapshot identifier on evaluation and score records
- Surface configuration misalignment errors to administrator on evaluation detail
- Reject evaluation when examination configuration is incomplete for objective auto-evaluation

##### Inputs

- Examination identifier
- Evaluation rules bundle from Module 04
- Auto-evaluation enabled flag
- Negative marking parameters
- Unanswered handling rule
- Multi-select partial-match rule
- Pass threshold and mark weights

##### Outputs

- Resolved rule set applied to evaluation and scoring pipeline
- Configuration snapshot identifier stored on evaluation record
- Configuration validation error codes when pre-flight fails

##### Business rules

- Evaluation rules are read-only at evaluation time; changes occur only in Module 04
- Examination without auto-evaluation enabled must not enter objective auto-evaluation pipeline
- Rule snapshot reference must be stored with each evaluation for audit
- Missing mandatory scoring parameters block scoring and surface administrator-actionable errors

##### Validations

- Auto-evaluation flag must be true for pipeline to proceed
- Mark weight must exist for every objective question on paper
- Pass threshold must be present when pass/fail determination is enabled
- Negative mark value required when negative marking flag is true
- Partial-match rule enum must be recognised value when multi-select questions present

##### Workflow

Configuration LOADED → Configuration VALIDATED → Evaluation PROCEED; Configuration LOADED → Configuration VALIDATION_FAILED → Evaluation EVALUATION_FAILED

##### Search requirements

- Administrator filter evaluation register by configuration error reason code

##### Security

- Evaluation rules bundle readable only by internal evaluation service and authorized administrators

##### Integrations

- Examination evaluation and result display rule bundle from Module 04 configuration service

##### Dependencies

- F04 — Question Bank and Examination Configuration: Examination Master Configuration
- F04 — Question Bank and Examination Configuration: Result Display, Certificate Eligibility and Examination Fee Configuration
- F10-001 — Post-Submission Objective Answer Evaluation
- F10-002 — Examination Scoring and Pass Fail Determination

##### Assumptions

- Module 04 exposes a consolidated evaluation rules view per examination
- Configuration changes after evaluation do not retroactively alter stored outcomes unless retry explicitly re-reads rules

##### Risks

- Undocumented rule combinations in Module 04 may not map cleanly to evaluation pipeline
- Configuration drift between paper assembly and rule bundle could cause failures at scale

##### Non-functional requirements

- Rule loading must not add perceptible delay to immediate post-submission evaluation
- Configuration validation errors must be explicit enough for administrator correction without developer intervention

##### Notes

Applies evaluation and scoring rules authored in Module 04; does not duplicate configuration editing screens.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Administrator configuration rule snapshot summary panel on evaluation detail | Easy | 14 |
| UI | Configuration misalignment error banner with missing rule field labels | Simple | 5 |
| API | Load evaluation rules bundle by examination identifier | Easy | 4 |
| API | Pre-flight validate auto-evaluation eligibility and required parameters | Medium | 6 |
| API | Apply unanswered handling rule during outcome classification handoff | Medium | 6 |
| API | Apply multi-select partial-match rule during comparison handoff | Medium | 6 |
| API | Persist configuration snapshot identifier on evaluation record | Easy | 4 |
| Database | Configuration snapshot reference column on evaluation header | Simple | 0.1 |
| Integration | Examination configuration service rules bundle fetch | Simple | 4 |
| Testing | Happy-path rule bundle load and successful pipeline proceed | Easy | 0.25 |
| Testing | Missing pass threshold and negative mark value validation failures | Medium | 0.3 |
| Testing | Auto-evaluation disabled examination rejection case | Medium | 0.3 |
| Documentation | Technical notes mapping Module 04 rule fields to evaluation pipeline behaviour | Medium | 0.3 |

### F10-004 Governed Result Publication and Display Rule Enforcement

121.9 hours · Go-live · 24 tasks

##### Description

Governs when evaluated examination results become visible to candidates by applying result publication controls and Module 04 display rules, including field-level masking of marks, counts, percentage, and pass/fail until publication, with administrator oversight for publish and withhold actions.

##### Business objective

Allow departments to control result release timing and visible content per examination policy while ensuring candidates see only approved fields after publication.

##### Actors

- Examination Administrator
- Candidate

##### User journey

1. System marks result record as EVALUATED_NOT_PUBLISHED after scoring completes.
2. Examination Administrator opens result publication register filtered by examination and publication status.
3. Administrator selects one or more evaluated results and reviews display rule preview for the examination.
4. Administrator confirms publish action for selected results.
5. System loads result display rules from Module 04 for the examination.
6. System snapshots applicable display rules onto the result publication record.
7. System transitions result status from EVALUATED_NOT_PUBLISHED to PUBLISHED and records publisher and timestamp.
8. Candidate portal result queries return published results only with fields masked per snapshotted display rules.
9. Administrator may select published results and confirm withhold action when policy allows retraction before certificate issuance.
10. System transitions result status from PUBLISHED to WITHHELD and records reason.
11. Candidate previously seeing result now receives not-published empty state on refresh.
12. Administrator may re-publish withheld result through publish action returning status to PUBLISHED.

##### Functional capabilities

- Maintain result publication status separate from evaluation completion
- List evaluated results with publication status for administrator
- Publish individual evaluated result with display rule snapshot
- Bulk publish multiple results for an examination session
- Withhold published result with reason capture
- Load result display field visibility rules from Module 04
- Snapshot display rules at publish time for immutable candidate view
- Mask marks counts percentage pass/fail fields not enabled in display rules
- Block candidate access to unpublished results
- Record publication and withhold audit trail with actor and timestamp
- Preview effective candidate-visible fields before publish

##### Inputs

- Evaluation and score summary from F10-002
- Result display rules from Module 04
- Administrator publish or withhold action
- Withhold reason text when applicable
- Examination and session filters for register

##### Outputs

- Result publication record with status EVALUATED_NOT_PUBLISHED, PUBLISHED, or WITHHELD
- Display rule snapshot attached to publication record
- Publication timestamp and publishing administrator identifier
- Withhold timestamp reason and actor when applicable
- Candidate-visible field subset per display rules

##### Business rules

- Candidates cannot view results until status is PUBLISHED
- Display rules configured in Module 04 determine which score fields appear after publication
- Display rule snapshot at publish time governs candidate view even if Module 04 rules later change
- Withhold removes candidate visibility but retains evaluation data for administrators
- Bulk publish limited to results in EVALUATED_NOT_PUBLISHED status
- Departmental report exports are out of scope

##### Validations

- Publish permitted only when evaluation status is EVALUATED and scoring is complete
- Publish rejected when result already PUBLISHED unless idempotent acknowledge
- Withhold permitted only when current status is PUBLISHED
- Withhold reason required when department policy flag mandates
- Bulk publish selection must reject mixed examinations without confirmation per examination batch
- Display rules must resolve at least one visible field for candidate result view

##### Workflow

Result EVALUATED_NOT_PUBLISHED → PUBLISHED on administrator publish; Result PUBLISHED → WITHHELD on administrator withhold; Result WITHHELD → PUBLISHED on administrator re-publish

##### Search requirements

- Administrator register search by examination name
- Filter by publication status EVALUATED_NOT_PUBLISHED PUBLISHED WITHHELD
- Filter by examination session date
- Filter by candidate registration number or name
- Filter by pass or fail status

##### Security

- Only Examination Administrator may publish or withhold results
- Publication audit log immutable to administrator users
- Candidate API returns only own published results with masked fields

##### Integrations

- Result display field rules from Module 04 Result Display configuration
- Optional result published event emission to Module 07 Notification Service when subscribed

##### Dependencies

- F10-002 — Examination Scoring and Pass Fail Determination
- F04 — Question Bank and Examination Configuration: Result Display, Certificate Eligibility and Examination Fee Configuration
- F01 — User and Role Management: Examination Administrator Account Lifecycle
- F07 — Notification Service: Examination Lifecycle Event Subscription and Template Routing

##### Assumptions

- Immediate automatic publish on evaluation is controlled by a display or publication flag in Module 04; manual publish path remains available
- Certificate generation in Module 11 consumes published results separately and is out of scope here

##### Risks

- Accidental bulk publish without review could release results prematurely
- Display rule snapshot divergence from live Module 04 rules may confuse administrators

##### Non-functional requirements

- Bulk publish of session results should complete within operational time limits for typical session sizes
- Publication state changes must be immediately effective for candidate portal reads

##### Notes

Display field catalog configured in Module 04; this feature governs publication state and candidate-visible field masking.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Administrator result publication register with examination session and status filters | Medium | 16 |
| UI | Result publication detail view with evaluation summary and display rule preview | Medium | 16 |
| UI | Single result publish confirmation dialog | Simple | 5 |
| UI | Bulk result publish confirmation dialog with selected count | Simple | 5 |
| UI | Withhold published result confirmation dialog with reason field | Medium | 16 |
| UI | Publication register empty state when no evaluated results exist | Simple | 5 |
| API | List and search results by publication status and examination filters | Medium | 6 |
| API | Publish single evaluated result with display rule snapshot | Complex | 8 |
| API | Bulk publish evaluated results for selected identifiers | Complex | 8 |
| API | Withhold published result with reason capture | Medium | 6 |
| API | Fetch publication detail with snapshotted display rules for administrator | Medium | 6 |
| API | Apply display rule field masking for candidate-visible result payload | Complex | 8 |
| API | Validate publish preconditions including evaluation and scoring completeness | Medium | 6 |
| Database | Result publication entity with status publisher and timestamps | Medium | 0.3 |
| Database | Display rule snapshot storage on publication record | Medium | 0.3 |
| Database | Publication and withhold audit history records | Medium | 0.3 |
| Integration | Result display rules fetch from examination configuration service | Simple | 4 |
| Integration | Optional result published event dispatch to notification service | Simple | 4 |
| Testing | Happy-path publish and candidate visible field masking per display rules | Medium | 0.3 |
| Testing | Unpublished result blocked from candidate access negative case | Medium | 0.3 |
| Testing | Withhold removes candidate visibility while administrator retains access | Medium | 0.3 |
| Testing | Bulk publish partial selection validation and unauthorized role denial | Complex | 0.5 |
| Documentation | Administrator runbook for publish withhold and display rule preview | Medium | 0.3 |
| Documentation | Technical notes for display rule snapshot and field masking logic | Medium | 0.3 |

### F10-005 Candidate Portal Examination Result Access

102.85 hours · Go-live · 18 tasks

##### Description

Provides candidates authenticated through the candidate portal with a register and detail view of their published examination results, honouring Module 04 display rules for visible fields, and clear empty and error states when results are not yet published or withheld.

##### Business objective

Enable candidates to self-service view official examination outcomes online immediately after department publication without administrator manual distribution.

##### Actors

- Candidate

##### User journey

1. Candidate logs into candidate portal using registered mobile OTP from platform login.
2. Candidate navigates to My Examination Results section from portal home.
3. System lists candidate's examinations with published results showing examination name, date, and pass/fail or summary per display rules.
4. Candidate selects one examination result row to open detail view.
5. System loads published result for authenticated candidate only.
6. System applies snapshotted display rules to show permitted fields such as total score, percentage, correct count, or pass/fail only.
7. Candidate reviews result detail and returns to list.
8. If result is evaluated but not yet published, list shows examination row with not published status and detail shows not available empty state.
9. If result was withheld after prior publication, detail shows result unavailable message.
10. If no examinations completed, list shows no results empty state.

##### Functional capabilities

- List published examination results for authenticated candidate only
- Show examination name schedule date and high-level outcome per display rules in list
- Open result detail for selected published examination
- Render detail fields masked per snapshotted display rules from publication
- Show not published status for evaluated but unpublished examinations
- Show result unavailable state for withheld publications
- Show empty state when candidate has no completed examinations
- Prevent cross-candidate result access
- Support read-only mobile-friendly result layouts for candidate portal web access

##### Inputs

- Authenticated candidate session
- Published result records for candidate
- Display rule snapshot from publication record
- Examination metadata name and date from scheduling module

##### Outputs

- Candidate result list with publication-aware status labels
- Candidate result detail with field-level masked score summary
- Empty and not available user messages

##### Business rules

- Candidate may view only own results
- Unpublished evaluated results show status label but not score fields
- Withheld results behave as unavailable to candidate
- Field visibility strictly follows publication snapshot not live Module 04 edits
- Certificate download links are out of scope in this module

##### Validations

- Candidate session must be valid and active
- Result detail request must match authenticated candidate identifier
- Non-published result detail requests return not available without score leakage
- Unknown examination identifier returns not found without revealing other candidates' data

##### Workflow

Candidate authenticated → Result list LOADED → Detail VIEW when PUBLISHED; Evaluated not published → NOT_AVAILABLE view; Withheld → UNAVAILABLE view

##### Search requirements

- Candidate result list sorted by examination date descending
- Optional text filter by examination name within own result list

##### Security

- Strict candidate ownership check on every result list and detail request
- No per-question answer key or correct option exposure in candidate views unless explicitly enabled in display rules out of scope for typical configuration
- Rate limiting on result detail requests to reduce scraping

##### Integrations

- Candidate authentication session from platform candidate login
- Published result and display snapshot from F10-004
- Examination schedule metadata from Module 06 for display labels

##### Dependencies

- F10-004 — Governed Result Publication and Display Rule Enforcement
- F05 — Candidate Registration: candidate portal authentication context
- F06 — Examination Scheduling and Allocation: examination schedule metadata
- F04 — Question Bank and Examination Configuration: Result Display, Certificate Eligibility and Examination Fee Configuration

##### Assumptions

- Candidate portal is web-based; native mobile app separate views are out of scope unless same responsive web suffices
- Hall ticket and registration modules provide examination labels linked by registration identifier

##### Risks

- Overly permissive display rules could expose more detail than department intends
- Candidate confusion when immediate evaluation occurs but publication delayed without clear not published messaging

##### Non-functional requirements

- Result list and detail must load within portal performance standards under concurrent post-publication traffic
- Result views must be read-only with no client-side score manipulation

##### Notes

Candidate OTP portal from registration module; shows only published results per F10-004 display rules.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate my examination results list with publication status labels | Easy | 14 |
| UI | Candidate examination result detail view with display-rule-driven fields | Medium | 16 |
| UI | Candidate result list empty state when no completed examinations | Simple | 5 |
| UI | Candidate result not yet published empty state on detail view | Simple | 5 |
| UI | Candidate result withheld unavailable state on detail view | Simple | 5 |
| UI | Candidate result list examination name filter control | Easy | 14 |
| UI | Mobile-responsive layout for candidate result list and detail | Medium | 16 |
| API | List published and status-labelled results for authenticated candidate | Medium | 6 |
| API | Fetch candidate result detail with display rule field masking | Medium | 6 |
| API | Reject result detail request for unpublished or withheld results without score leakage | Medium | 6 |
| API | Enforce candidate ownership on result list and detail queries | Easy | 4 |
| Database | Candidate result list query indexes by candidate and publication status | Easy | 0.25 |
| Integration | Examination schedule metadata enrichment for result list labels | Simple | 4 |
| Testing | Happy-path candidate views published result with masked fields per display rules | Medium | 0.3 |
| Testing | Not published and withheld result empty unavailable states | Medium | 0.3 |
| Testing | Cross-candidate result access denial and invalid session rejection | Complex | 0.5 |
| Documentation | Candidate user guide for viewing examination results and status meanings | Easy | 0.25 |
| Documentation | Technical notes for candidate result ownership and field masking | Easy | 0.25 |

## 11 Certificate Management

634.6 hours · 128 tasks · Business

Digital certificate issuance for eligible candidates, QR-enabled authenticity, and public online verification.

### F11-001 Eligibility-Triggered Certificate Issuance and Numbering

106.65 hours · Go-live · 25 tasks

##### Description

Automatically creates certificate lifecycle records when a candidate's published examination result satisfies Module 04 certificate eligibility and pass criteria. Assigns a unique certificate number and secure verification token, captures an approved public disclosure field snapshot, and exposes administrator monitoring with per-candidate retry for failed issuance rows.

##### Business objective

Ensure only eligible passed candidates receive department-issued digital certificates with unique numbering and verifiable tokens immediately after governed result publication, without manual re-entry of result data.

##### Actors

- Examination Administrator
- System (batch issuance job)

##### User journey

1. Examination Administrator completes governed result publication in Evaluation & Results (Module 10).
2. Certificate issuance batch job receives the set of candidates with published pass outcomes for the examination.
3. For each candidate, the system reads certificate eligibility rules configured in Question Bank & Examination Configuration (Module 04).
4. System evaluates pass status, eligibility flag, and absence of an existing active certificate for the same examination attempt.
5. Eligible candidates enter ISSUANCE_QUEUED; ineligible or duplicate-attempt candidates are recorded as ISSUANCE_SKIPPED with reason.
6. System allocates the next certificate number from the examination-specific numbering sequence.
7. System generates a secure verification token bound to the certificate record.
8. System persists the certificate lifecycle record with status ISSUED, issue date, links to candidate, examination, result, certificate number, token reference, and disclosure field snapshot.
9. System emits a certificate-available notification event to Notification Service (Module 07) when issuance succeeds.
10. Examination Administrator opens the issuance monitoring register filtered by examination and batch run.
11. Administrator reviews failed rows (e.g., missing mandatory disclosure source field, sequence exhaustion).
12. Administrator corrects upstream data if needed and triggers individual retry for a failed row.
13. Retry re-evaluates eligibility and either transitions the row to ISSUED or remains ISSUANCE_FAILED with updated reason.

##### Functional capabilities

- Evaluate certificate eligibility against published pass result and Module 04 eligibility configuration
- Skip issuance when an active certificate already exists for the same examination attempt
- Allocate unique certificate numbers from a per-examination sequence
- Generate secure verification tokens bound to certificate records
- Persist certificate lifecycle records with issue date and ISSUED status
- Capture approved public disclosure field snapshot at time of issuance
- Batch-process all eligible candidates immediately after result publication
- Record per-candidate issuance outcome with skip or failure reason
- Display issuance monitoring register with batch and row-level status
- Retry failed single-candidate issuance after prerequisite correction
- Emit certificate-available notification event on successful issuance

##### Inputs

- Published examination result identifier and pass/fail outcome
- Certificate eligibility configuration from Module 04
- Candidate profile fields required for certificate record and disclosure snapshot
- Examination master identifier and display name
- Examination-specific certificate numbering sequence configuration
- Batch run identifier and result publication timestamp

##### Outputs

- Certificate lifecycle record with unique certificate number
- Secure verification token reference linked to certificate
- Public disclosure field snapshot stored on certificate record
- Per-candidate issuance outcome log entry (ISSUED, ISSUANCE_SKIPPED, ISSUANCE_FAILED)
- Certificate-available notification event payload to Module 07

##### Business rules

- Issuance occurs only after results are in published state per Module 10 governance
- Candidate must meet both pass criteria and certificate eligibility flag from Module 04
- At most one active (non-revoked) certificate per candidate per examination attempt
- Certificate numbers must be unique within the examination numbering scope
- Verification tokens must not be reversible to internal primary keys in public contexts
- Failed issuance rows do not delete partial records; they remain auditable until resolved or marked permanent failure
- Disclosure snapshot is immutable after issuance; later configuration changes apply only to new certificates

##### Validations

- Published result must exist and show PASS before issuance proceeds
- Certificate eligibility flag from Module 04 must be true for the examination
- Candidate identifier must resolve to an active registration profile
- Duplicate active certificate check must pass for candidate plus examination attempt
- Mandatory disclosure source fields (e.g., candidate legal name, examination title, issue date) must be non-empty
- Certificate number sequence must not exceed configured maximum if a cap exists
- Retry allowed only from ISSUANCE_FAILED state, not from ISSUED or REVOKED

##### Calculations

- Next certificate number = previous sequence value + 1 formatted per examination numbering pattern
- Eligible candidate count = published pass candidates minus ineligible, duplicate, and failed rows

##### Workflow

RESULT_PUBLISHED → ELIGIBILITY_EVALUATED → ISSUANCE_QUEUED → NUMBER_ASSIGNED → TOKEN_GENERATED → ISSUED; alternate paths: ELIGIBILITY_EVALUATED → ISSUANCE_SKIPPED; ISSUANCE_QUEUED → ISSUANCE_FAILED → RETRY_PENDING → ISSUED | PERMANENT_FAILURE

##### Search requirements

- Issuance monitoring register searchable by examination name, batch run date, and row status
- Filter failed and skipped rows by failure reason code

##### Reports

- Issuance batch summary counts (issued, skipped, failed) exposed as register aggregates for Module 12 reporting hooks

##### Notifications

- Certificate-available event dispatched to Module 07 upon successful ISSUED transition

##### Security

- Only Examination Administrator role may view issuance monitoring and trigger retry
- Verification tokens stored using one-way hashing or secure vault reference; plain token never logged
- Batch job execution authenticated as system service account with least-privilege scope

##### Integrations

- Consume published result and pass outcome from Module 10 Evaluation & Results
- Read certificate eligibility configuration from Module 04 Question Bank & Examination Configuration
- Emit certificate-available notification event to Module 07 Notification Service

##### Dependencies

- F10-00x Governed Result Publication and Display (Module 10)
- F04-00x Certificate Eligibility Configuration (Module 04)
- F05-00x Candidate Registration profile fields (Module 05)
- F01-00x Examination Administrator authorization (Module 01)
- F07-00x Notification event subscription and dispatch (Module 07)

##### Assumptions

- Certificate numbering sequence and format are configured in Module 04 or examination master before first issuance
- Mandatory fields for disclosure snapshot are present on candidate profile or result record at publication time
- Batch job infrastructure handles examination-wide candidate volumes without manual intervention for happy path
- Notification template for certificate availability is configured in Module 07 prior to go-live

##### Risks

- Large candidate volumes may require batch throttling not explicitly sized in SOW
- Missing candidate photograph or optional fields may block PDF generation downstream if treated as mandatory
- Sequence exhaustion under high attempt volume requires administrator intervention

##### Non-functional requirements

- Issuance batch for a single examination should complete within operational SLA agreed at integration testing
- Issuance operations must be idempotent to prevent duplicate certificates on batch retry
- All issuance state transitions must be audit-logged with actor, timestamp, and reason

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Issuance monitoring register with batch status chips and failure reason column | Medium | 16 |
| UI | Issuance row failure detail read-only panel with candidate and examination context | Simple | 5 |
| UI | Individual issuance retry confirmation dialog | Simple | 5 |
| UI | Issuance monitoring empty state when no batches exist for selected examination | Simple | 5 |
| API | Evaluate certificate eligibility for candidate-examination pair against published result | Complex | 8 |
| API | Batch queue certificate issuance for all eligible candidates after result publication | Complex | 8 |
| API | Allocate next unique certificate number with sequence boundary handling | Medium | 6 |
| API | Generate secure verification token bound to certificate record | Medium | 6 |
| API | Create certificate lifecycle record with issue metadata and disclosure snapshot | Complex | 8 |
| API | List issuance batch outcomes with examination and status filters | Medium | 6 |
| API | Retry failed single-candidate issuance after prerequisite correction | Medium | 6 |
| Database | Core certificate entity with candidate examination and result linkage | Medium | 0.3 |
| Database | Certificate number uniqueness constraints and sequence allocation indexes | Complex | 0.5 |
| Database | Verification token secure reference storage | Medium | 0.3 |
| Database | Issuance batch run and per-candidate outcome audit persistence | Medium | 0.3 |
| Integration | Consume published pass result signal from Evaluation module | Medium | 16 |
| Integration | Read certificate eligibility configuration from Examination Configuration module | Simple | 4 |
| Integration | Emit certificate-available notification event to Notification Service | Simple | 4 |
| Testing | Happy path batch issuance for multiple eligible passed candidates | Medium | 0.3 |
| Testing | Duplicate active certificate rejection for same examination attempt | Medium | 0.3 |
| Testing | Certificate number sequence boundary and collision edge cases | Complex | 0.5 |
| Testing | Issuance failure when mandatory disclosure source fields are missing | Medium | 0.3 |
| Testing | Unauthorized role blocked from issuance monitoring and retry operations | Easy | 0.25 |
| Documentation | Administrator runbook for issuance monitoring and failure recovery | Medium | 0.3 |
| Documentation | Technical notes for numbering scheme token security and batch idempotency | Medium | 0.3 |

### F11-002 Digital Certificate PDF Generation with QR Embedding

83.65 hours · Go-live · 21 tasks

##### Description

Renders department-approved digital certificate PDF documents for issued certificate records, dynamically populating candidate and examination fields, embedding a QR code linked to the verification token URL, versioning generated documents, and supporting administrator-triggered regeneration when template or source data changes.

##### Business objective

Provide candidates and verifiers with a tamper-evident printable certificate document that embeds machine-readable QR verification aligned to the department's certificate template standards.

##### Actors

- Examination Administrator
- System (document generation job)
- Candidate

##### User journey

1. Certificate lifecycle record reaches ISSUED state (Feature F11-001).
2. System queues PDF generation job for the certificate record.
3. System resolves candidate name, examination title, issue date, certificate number, and photograph from upstream modules.
4. System renders PDF using the active certificate template version.
5. System generates QR code image encoding the public verification URL with verification token.
6. System embeds QR code at the configured position on the certificate PDF.
7. System persists the PDF binary reference, template version, checksum, and generation timestamp.
8. Certificate generation status transitions to DOCUMENT_READY on success or DOCUMENT_FAILED on error.
9. Examination Administrator opens certificate detail and views generation status indicator.
10. Administrator optionally opens template preview read-only page to validate field placement against sample data.
11. If source data or template was corrected, administrator initiates regeneration via confirmation dialog.
12. Regeneration creates a new document version while retaining prior version in history.
13. Candidate sees certificate as downloadable once DOCUMENT_READY (handled in Feature F11-003).

##### Functional capabilities

- Queue PDF generation automatically upon ISSUED transition
- Render certificate PDF from approved template with dynamic field binding
- Resolve candidate photograph from registration profile for template placement
- Generate QR code image from verification token URL
- Embed QR code into certificate PDF at configured coordinates
- Persist generated PDF with version checksum and template version reference
- Expose certificate document generation status on administrator detail view
- Regenerate certificate PDF on administrator request with version increment
- Retain superseded PDF versions in document history
- Surface generation failure reason to administrator detail view

##### Inputs

- Certificate record with certificate number issue date verification token reference
- Active certificate template version and field mapping configuration
- Candidate legal name and photograph from Module 05 profile
- Examination display name and completion or result date from Module 10
- QR placement coordinates and public verification base URL configuration

##### Outputs

- Generated certificate PDF binary stored with file reference
- QR code embedded within PDF document
- Document version record with template version checksum and timestamp
- Generation status DOCUMENT_READY or DOCUMENT_FAILED on certificate record

##### Business rules

- PDF generation executes only for certificates in ISSUED status
- Each regeneration increments document version; prior versions remain auditable
- QR code must encode the same verification token issued at certificate creation
- Template version active at generation time is recorded immutably on the document record
- Revoked certificates do not auto-regenerate; regeneration blocked while status is REVOKED

##### Validations

- Certificate record must exist and be in ISSUED status before generation starts
- Mandatory template fields (candidate name, examination name, certificate number, issue date) must resolve to non-empty values
- Photograph file reference must be valid format or fall back to configured placeholder image
- Template version identifier must reference an active approved template
- Regeneration request must be authorized to Examination Administrator role
- Public verification base URL must be configured before QR embedding proceeds

##### Calculations

- Document checksum computed over generated PDF bytes for integrity verification

##### Workflow

ISSUED → DOCUMENT_QUEUED → DOCUMENT_GENERATING → DOCUMENT_READY; alternate: DOCUMENT_GENERATING → DOCUMENT_FAILED → DOCUMENT_QUEUED (retry) → DOCUMENT_READY

##### Documents

- Digital certificate PDF with embedded QR code
- Certificate template version referenced at generation time

##### Security

- PDF storage access restricted to authorized administrators and owning candidate
- Verification token must not appear in plain text within PDF body outside QR encoding
- Regeneration actions audit-logged with administrator identity and reason

##### Integrations

- Resolve candidate photograph and profile fields from Candidate Registration module
- Resolve examination and result metadata from Evaluation & Results module
- QR code image generation library or internal service

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F05-00x Candidate profile and photograph storage (Module 05)
- F10-00x Published result metadata (Module 10)
- F04-00x Certificate template configuration (Module 04)

##### Assumptions

- Approved certificate template artwork and field map are supplied by client before UAT
- Public verification base URL is stable across environments with environment-specific configuration
- Photograph absence is handled via placeholder rather than blocking all issuances unless client mandates otherwise

##### Risks

- Template changes after bulk issuance may require mass regeneration outside initial scope
- Large photograph files may impact PDF render performance
- QR print quality at small sizes may affect scan success on low-resolution prints

##### Non-functional requirements

- Single certificate PDF generation should complete within interactive SLA for administrator-triggered regeneration
- Generated PDFs must meet print-ready resolution for QR scanning
- Document storage must support retention policy aligned with certificate lifecycle records

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Certificate template preview read-only page for administrators | Medium | 16 |
| UI | Certificate generation status indicator on administrator certificate detail view | Simple | 5 |
| UI | Regenerate certificate PDF confirmation dialog for administrators | Simple | 5 |
| UI | Certificate generation failure alert banner on administrator detail view | Simple | 5 |
| API | Render certificate PDF from template with dynamic candidate and examination fields | Complex | 8 |
| API | Embed QR code encoding verification URL into certificate PDF output | Medium | 6 |
| API | Persist generated certificate PDF with version checksum and template reference | Medium | 6 |
| API | Regenerate certificate PDF for single record with version increment | Medium | 6 |
| API | Fetch certificate document generation status for administrator detail view | Easy | 4 |
| Database | Certificate document file reference and storage metadata entity | Easy | 0.25 |
| Database | Certificate document version history per certificate record | Medium | 0.3 |
| Database | Template version identifier stored on each generated document row | Simple | 0.1 |
| Integration | Resolve candidate photograph from registration profile for PDF rendering | Medium | 16 |
| Integration | QR code image generation library integration | Simple | 4 |
| Testing | Happy path PDF contains mandatory fields and scannable QR code | Medium | 0.3 |
| Testing | Template version upgrade produces distinguishable document version history | Medium | 0.3 |
| Testing | Missing candidate photograph renders configured placeholder image | Easy | 0.25 |
| Testing | PDF generation failure surfaces actionable error on administrator detail view | Medium | 0.3 |
| Testing | Unauthorized regeneration attempt rejected for non-administrator roles | Medium | 0.3 |
| Documentation | Administrator runbook for certificate regeneration after template or data correction | Easy | 0.25 |
| Documentation | Technical notes for PDF template field binding and QR placement configuration | Medium | 0.3 |

### F11-003 Candidate Portal Certificate List and Download

107.9 hours · Go-live · 19 tasks

##### Description

Enables authenticated candidates to view a portal list of their issued digital certificates per examination, inspect certificate metadata, and download the generated PDF when document status is ready and certificate status remains active.

##### Business objective

Allow eligible candidates to self-service download digitally generated examination certificates from their OTP-authenticated portal login without administrator intervention.

##### Actors

- Candidate

##### User journey

1. Candidate logs into the examination portal using OTP authentication (Module 01 / SOW Section 4.1).
2. Candidate navigates to the Certificates section from portal navigation.
3. System loads certificate list scoped strictly to the authenticated candidate identifier.
4. Candidate sees each row with examination name, certificate number, issue date, and status badge (ISSUED, DOCUMENT_PENDING, REVOKED).
5. If no certificates exist yet, candidate sees empty state messaging explaining certificates appear after results and issuance processing.
6. If list retrieval fails, candidate sees error state with retry action.
7. Candidate selects a certificate row to open read-only detail panel showing examination name, issue date, certificate number, and download eligibility indicator.
8. When status is ISSUED and document is DOCUMENT_READY, candidate clicks download.
9. System streams PDF to candidate browser and logs download event.
10. If certificate is REVOKED, download control is disabled with explanation tooltip.
11. If document is still generating, detail panel shows pending message without download action.

##### Functional capabilities

- List all certificate records belonging to authenticated candidate
- Display examination name issue date certificate number and status on list rows
- Show empty state when candidate has no issued certificates
- Show error state with retry when list retrieval fails
- Display read-only certificate detail panel with metadata before download
- Stream certificate PDF download for ISSUED certificates with ready documents
- Block download for REVOKED or cancelled certificates
- Block download while document generation is pending or failed
- Log each candidate download event with timestamp
- Enforce candidate-scoped access preventing cross-candidate record access

##### Inputs

- Authenticated candidate session token from OTP login
- Certificate list query parameters (optional examination filter)
- Certificate identifier selected for detail or download

##### Outputs

- Candidate-scoped certificate list with status badges
- Certificate metadata detail payload
- Downloaded certificate PDF file stream
- Candidate download audit log entry

##### Business rules

- Candidates may view and download only their own certificate records
- Download permitted only when certificate status is ISSUED and document status is DOCUMENT_READY
- Revoked certificates remain visible in list with REVOKED badge but download is disabled
- Certificates for examinations where results are not yet published must not appear in list
- Each download event is recorded for audit; repeated downloads are allowed

##### Validations

- Session must belong to valid authenticated candidate
- Requested certificate identifier must belong to session candidate identifier
- Download request rejected when certificate status is REVOKED or CANCELLED
- Download request rejected when document status is not DOCUMENT_READY
- Certificate identifier must be well-formed and exist or return not-found without leaking other candidates' data

##### Workflow

PORTAL_LOGIN → CERTIFICATE_LIST_LOADED → DETAIL_VIEWED → DOWNLOAD_REQUESTED → DOWNLOAD_STREAMED; alternate: DETAIL_VIEWED → DOWNLOAD_BLOCKED (revoked or pending document)

##### Search requirements

- Optional filter certificate list by examination name on client-side or lightweight server filter

##### Documents

- Downloaded digital certificate PDF from candidate portal

##### Security

- All list detail and download operations scoped to authenticated candidate identity
- Direct object reference attempts by tampered certificate identifier return generic not-found
- Download responses include cache-control headers discouraging unintended public caching

##### Integrations

- Validate candidate OTP portal session from User authentication module

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F11-002 Digital Certificate PDF Generation with QR Embedding
- F01-00x Candidate OTP authentication session (Module 01)
- SOW Section 4.1 OTP-Based Candidate Login

##### Assumptions

- Portal navigation includes a Certificates entry point agreed in overall portal UX
- Candidates access portal primarily via web browser; responsive layout covers mobile browsers
- Certificate PDF file size is suitable for direct browser download on typical mobile networks

##### Risks

- Candidates may attempt to share portal credentials to download on behalf of others
- Pending document state may generate support queries if issuance-to-PDF delay is long

##### Non-functional requirements

- Certificate list should load within portal performance targets under concurrent login peaks
- Download streaming must support standard mobile and desktop browsers
- Portal certificate views must be readable on mobile screen widths

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate portal certificate list with examination name issue date and status badges | Easy | 14 |
| UI | Candidate certificate list empty state with pending issuance messaging | Simple | 5 |
| UI | Candidate certificate list error state with retry action | Simple | 5 |
| UI | Candidate certificate detail read-only panel with download eligibility indicator | Medium | 16 |
| UI | Candidate certificate PDF download button with in-progress indicator | Easy | 14 |
| UI | Revoked certificate row with download disabled and explanation tooltip | Easy | 14 |
| UI | Mobile-responsive layout for candidate certificate list and detail views | Medium | 16 |
| API | List certificates scoped to authenticated candidate identity | Easy | 4 |
| API | Get single certificate metadata for authenticated candidate | Easy | 4 |
| API | Stream certificate PDF download with issued-status and document-ready enforcement | Medium | 6 |
| API | Log candidate certificate download event with timestamp | Easy | 4 |
| Database | Candidate certificate download audit log persistence | Easy | 0.25 |
| Integration | Validate candidate portal session from authentication module | Simple | 4 |
| Testing | Happy path list and download for issued certificate with ready document | Easy | 0.25 |
| Testing | Revoked certificate download blocked with user-facing explanation message | Medium | 0.3 |
| Testing | Cross-candidate certificate identifier tampering returns not-found without data leak | Complex | 0.5 |
| Testing | Empty list when results published but certificate issuance not yet complete | Easy | 0.25 |
| Documentation | Candidate user guide for locating and downloading examination certificates | Easy | 0.25 |
| Documentation | Technical notes for candidate-scoped certificate authorization checks | Simple | 0.1 |

### F11-004 Public Online Certificate Verification Portal

127.7 hours · Go-live · 23 tasks

##### Description

Provides a public-facing verification experience for verifiers and third parties to confirm certificate authenticity by scanning the QR code or entering a certificate number, returning valid, not-found, or revoked/cancelled outcomes while displaying only administrator-approved public disclosure fields.

##### Business objective

Enable third parties to independently confirm that a certificate was issued by the department and determine whether it is currently valid, without exposing non-approved personal information.

##### Actors

- Verifier/Public User

##### User journey

1. Verifier scans QR code on printed certificate using mobile device camera or QR app.
2. QR encodes public verification URL with verification token parameter; browser opens verification landing page.
3. Landing page automatically submits token verification request without requiring login.
4. Alternatively, verifier navigates directly to public verification site and enters certificate number manually.
5. Verifier submits certificate number entry form.
6. System validates token or number format before lookup.
7. For valid active certificate, system displays approved disclosure fields only (e.g., candidate name, examination name, issue date, certificate number, pass status label).
8. For unknown token or certificate number, system displays uniform not-found outcome without revealing whether number format was partially matched.
9. For revoked or cancelled certificate, system displays revoked outcome with status explanation and issue date if approved for disclosure, suppressing other sensitive fields.
10. If rate limit threshold exceeded, verifier sees cooldown or challenge message before further attempts.
11. Verification request is audit-logged with outcome category without storing unnecessary PII.

##### Functional capabilities

- Verify certificate authenticity by QR verification token deep link
- Verify certificate authenticity by manual certificate number entry
- Display valid verification outcome with approved public disclosure fields only
- Display not-found outcome for unknown token or certificate number
- Display revoked or cancelled outcome with status explanation
- Validate token and certificate number format before lookup
- Apply rate limiting on public verification requests
- Audit-log verification requests with outcome category
- Auto-submit verification on QR deep link landing page
- Render mobile-responsive verification results for field scanning use case

##### Inputs

- Verification token from QR-encoded URL parameter
- Certificate number entered on public form
- Client IP address and request timestamp for rate limiting
- Approved public disclosure field snapshot stored on certificate record

##### Outputs

- Valid verification result panel with approved disclosure field values
- Not-found verification result panel
- Revoked or cancelled verification result panel
- Verification audit log entry with outcome category VALID NOT_FOUND or REVOKED

##### Business rules

- Public verification requires no authentication
- Only fields approved for public disclosure and captured in issuance snapshot may be displayed on valid outcome
- Revoked certificates must never present as valid regardless of token possession
- Not-found responses must be uniform for invalid token and unknown certificate number to reduce enumeration
- Verification displays department branding confirming issuer identity
- Disclosure snapshot on certificate record governs displayed fields; live profile changes do not alter verification output

##### Validations

- Verification token must match expected length and character set before database lookup
- Certificate number entry must match configured format pattern
- Empty token and empty certificate number submissions rejected with inline field message
- Rate limit counter enforced per client IP or token bucket configuration
- Revoked status checked after record match before returning valid outcome

##### Workflow

VERIFY_REQUESTED → TOKEN_OR_NUMBER_VALIDATED → LOOKUP_EXECUTED → OUTCOME_VALID | OUTCOME_NOT_FOUND | OUTCOME_REVOKED

##### Search requirements

- Exact match lookup by verification token
- Exact match lookup by certificate number within examination scope or global scope per configuration

##### Reports

- Verification volume and outcome counts exposed as reporting hook aggregates for Module 12

##### Security

- Public endpoints require no session but enforce rate limiting and abuse monitoring
- Responses must not expose internal identifiers candidate primary keys or audit internals
- Timing-safe comparison used for token validation to reduce side-channel leakage
- Verification audit logs store outcome category without full disclosure field payload

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering (verification token and disclosure snapshot)
- F04-00x Approved public disclosure field configuration (Module 04)
- F11-005 Certificate Cancellation and Revocation (revoked status propagation)
- SOW Sections 35 QR Code on Certificate and 36 Online Certificate Verification

##### Assumptions

- Public verification base URL is published on department website and embedded in QR codes
- Approved disclosure field set is finalized before UAT and snapshotted at issuance
- Rate limit thresholds are agreed with client security team prior to production

##### Risks

- Certificate number enumeration attempts despite uniform not-found responses
- Over-disclosure if disclosure configuration includes fields later deemed sensitive
- High QR scan traffic during result season may require CDN caching constraints review

##### Non-functional requirements

- Verification response must render within sub-second target for typical lookup under load
- Public verification page must be mobile-first for QR scan workflows
- Service must remain available during peak post-result verification spikes

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Public verification landing page with certificate number entry form | Easy | 14 |
| UI | QR deep link landing page auto-submitting token verification on load | Medium | 16 |
| UI | Valid verification result panel showing approved disclosure fields only | Medium | 16 |
| UI | Not-found verification result panel for unknown token or certificate number | Simple | 5 |
| UI | Revoked or cancelled verification result panel with status explanation | Simple | 5 |
| UI | Inline validation message for malformed token or certificate number entry | Simple | 5 |
| UI | Public verification rate-limit cooldown message screen | Medium | 16 |
| UI | Mobile-responsive layout for public verification pages | Easy | 14 |
| API | Verify certificate by QR verification token parameter | Medium | 6 |
| API | Verify certificate by public certificate number lookup | Medium | 6 |
| API | Return approved disclosure field snapshot for valid active certificate outcome | Medium | 6 |
| API | Return revoked outcome suppressing non-approved sensitive fields | Medium | 6 |
| API | Return uniform not-found outcome for unknown token and unknown number | Easy | 4 |
| API | Enforce rate limiting on public verification requests per client IP | Medium | 6 |
| Database | Public verification request audit log with outcome category | Easy | 0.25 |
| Database | Read-optimized indexes supporting token and certificate number verification lookup | Easy | 0.25 |
| Testing | Happy path valid QR token displays only approved disclosure fields | Medium | 0.3 |
| Testing | Revoked certificate verification shows revoked outcome without PII leakage | Medium | 0.3 |
| Testing | Unknown token and unknown certificate number both return identical not-found outcome | Easy | 0.25 |
| Testing | Tampered verification token rejected without record disclosure | Complex | 0.5 |
| Testing | Rate limit blocks excessive verification attempts from single client IP | Medium | 0.3 |
| Documentation | Public verifier instruction content for QR scan and manual number entry | Easy | 0.25 |
| Documentation | Technical notes on disclosure minimization and enumeration-safe public responses | Medium | 0.3 |

### F11-005 Certificate Cancellation and Revocation Management

104.4 hours · Go-live · 21 tasks

##### Description

Allows Examination Administrators to cancel or revoke previously issued certificates with mandatory reason capture, immutable status transition history, immediate propagation to public verification and candidate download blocking, while preserving full certificate lifecycle records for audit.

##### Business objective

Provide governed certificate invalidation when issuance errors, disqualifications, or administrative decisions require a previously issued certificate to be treated as no longer valid, without deleting historical records.

##### Actors

- Examination Administrator

##### User journey

1. Examination Administrator opens certificate register and locates active ISSUED certificate (Feature F11-006) or receives directive to revoke specific record.
2. Administrator opens certificate administrator detail view with lifecycle timeline.
3. Administrator selects Revoke or Cancel action available only for ISSUED certificates.
4. System opens revocation reason dialog requiring reason code selection and mandatory notes text.
5. Administrator enters reason and confirms impact summary in confirmation dialog.
6. System transitions certificate status from ISSUED to REVOKED (or CANCELLED if configured as distinct outcome).
7. System appends immutable revocation event to certificate status history with actor timestamp reason code and notes.
8. Public verification immediately returns revoked outcome for associated token and certificate number.
9. Candidate portal download control becomes disabled for revoked certificate.
10. Administrator sees revoked badge on register row and may filter register to revoked status.
11. Attempt to revoke already-revoked certificate is rejected with inline message.

##### Functional capabilities

- Revoke or cancel active ISSUED certificate with mandatory reason capture
- Capture revocation reason code and free-text notes
- Transition certificate status ISSUED to REVOKED or CANCELLED
- Append immutable revocation event to certificate status history
- Propagate revoked status to public verification responses immediately
- Block candidate PDF download for revoked certificates
- Display revoked status badge on administrator register rows
- Filter administrator register by revoked or cancelled status
- Reject duplicate revocation on already-revoked certificate
- Preserve full certificate and document history without hard delete

##### Inputs

- Certificate identifier selected for revocation
- Revocation reason code from configured reference list
- Mandatory revocation notes text entered by administrator
- Administrator session identity and timestamp

##### Outputs

- Updated certificate status REVOKED or CANCELLED
- Revocation history event with reason actor and timestamp
- Revoked outcome on subsequent public verification requests
- Disabled download state on candidate portal certificate row

##### Business rules

- Only ISSUED certificates may be revoked; DOCUMENT_PENDING certificates follow separate cancellation path if needed
- Revocation does not delete certificate number token or document history records
- Revoked certificates cannot be reinstated to ISSUED within this module scope without separate client change request
- Revocation reason code must be selected from administrator-maintained reference list
- Public verification must reflect revoked status within same request cycle after commit
- Revocation action requires Examination Administrator authorization

##### Validations

- Certificate must exist and be in ISSUED status at time of revocation request
- Revocation reason code must be non-empty and valid reference value
- Revocation notes must meet minimum length threshold
- Administrator must hold permission for certificate revocation operation
- Duplicate revocation request on REVOKED certificate rejected with business error
- Revocation timestamp must not precede original issue date

##### Workflow

ISSUED → REVOKE_REQUESTED → REVOKE_CONFIRMED → REVOKED; alternate: REVOKED → REVOKE_REQUESTED → REVOKE_REJECTED (already revoked)

##### Search requirements

- Filter certificate register by REVOKED or CANCELLED status
- Search revoked certificates by revocation date range and reason code

##### Reports

- Revocation register export hook with reason code and date for Module 12 reporting

##### Notifications

- Optional revocation notification to candidate via Module 07 if client enables certificate-revoked template

##### Security

- Revocation restricted to authorized Examination Administrator roles
- Revocation history events are append-only and cannot be edited or deleted by administrators
- Revocation action audit includes source IP and session identifier

##### Integrations

- Emit optional certificate-revoked notification event to Notification Service

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F11-003 Candidate Portal Certificate List and Download
- F11-004 Public Online Certificate Verification Portal
- F01-00x Examination Administrator authorization (Module 01)
- SOW Section 37 Certificate Security

##### Assumptions

- Revocation reason code list is supplied by client before administrator training
- Certificate reinstatement after revocation is out of scope unless added by change request
- Cancelled and revoked may map to single REVOKED status with reason distinguishing administrative cancel vs fraud

##### Risks

- Delayed propagation to CDN-cached verification pages if caching introduced later
- Mass revocation after data correction event may require bulk tool outside current scope
- Candidates may retain previously downloaded PDF copies despite revocation

##### Non-functional requirements

- Revocation status must be immediately effective for verification and download enforcement
- Revocation history must satisfy audit retention requirements
- Revocation dialog must clearly communicate impact on verification and download

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Administrator certificate detail view with revoke action for ISSUED records | Medium | 16 |
| UI | Revocation reason capture dialog with mandatory reason code dropdown and notes field | Medium | 16 |
| UI | Revocation confirmation dialog summarizing verification and download impact | Simple | 5 |
| UI | Revoked status badge on administrator certificate register rows | Easy | 14 |
| UI | Certificate register status filter including revoked and cancelled values | Easy | 14 |
| UI | Inline rejection message when attempting to revoke already-revoked certificate | Simple | 5 |
| API | Revoke ISSUED certificate with reason code notes and actor audit | Complex | 8 |
| API | List revoked certificates with reason code and revocation timestamp for administrators | Medium | 6 |
| API | Propagate revoked status to public verification lookup responses | Medium | 6 |
| API | Enforce download block for revoked certificate on candidate portal stream endpoint | Easy | 4 |
| API | Reject duplicate revocation request for already-revoked certificate | Easy | 4 |
| Database | Certificate status transition history with reason actor and timestamp | Medium | 0.3 |
| Database | Revocation reason code reference values persistence | Simple | 0.1 |
| Integration | Emit optional certificate-revoked notification event to Notification Service | Simple | 4 |
| Testing | Happy path administrator revokes active ISSUED certificate with reason capture | Medium | 0.3 |
| Testing | Revoked certificate public verification returns revoked outcome immediately | Medium | 0.3 |
| Testing | Candidate download denied after revocation with explanatory message | Easy | 0.25 |
| Testing | Non-administrator role cannot execute revocation operation | Medium | 0.3 |
| Testing | Revocation history append-only behavior prevents modification of prior events | Medium | 0.3 |
| Documentation | Administrator runbook for certificate revocation policy and procedure | Medium | 0.3 |
| Documentation | Technical notes for revoked status propagation to verification and download endpoints | Easy | 0.25 |

### F11-006 Administrator Certificate Register Search and Export

104.3 hours · Go-live · 19 tasks

##### Description

Provides Examination Administrators with a searchable register of all certificate lifecycle records, advanced filtering, read-only detail with lifecycle timeline, and CSV export of filtered results to support operational oversight and Module 12 reporting hooks.

##### Business objective

Give examination administrators consolidated visibility into issued, pending, and revoked certificates across examinations for operational management audit response and downstream reporting.

##### Actors

- Examination Administrator

##### User journey

1. Examination Administrator navigates to Certificate Register from administration menu.
2. System loads paginated certificate register with default sort by issue date descending.
3. Administrator enters search text for certificate number or candidate name.
4. Administrator applies filters for examination, issue date range, status, and optionally allotted centre.
5. Register refreshes showing matching rows with certificate number candidate name examination issue date status and document status.
6. If no rows match, administrator sees empty state with guidance to adjust filters.
7. Administrator clicks row to open read-only certificate detail with lifecycle timeline showing issuance document generation and revocation events.
8. Administrator selects Export action to download CSV of currently filtered result set.
9. Export confirmation dialog warns row count and filter scope.
10. System generates CSV file with approved export columns and downloads to administrator browser.
11. Unauthorized roles attempting register access receive access denied outcome.

##### Functional capabilities

- Display paginated certificate register with sortable columns
- Search register by certificate number and candidate name
- Filter register by examination issue date range status and document status
- Show register empty state when no rows match criteria
- Open read-only administrator certificate detail with lifecycle timeline
- Export filtered certificate register to CSV file
- Confirm export scope and row count before download
- Enforce administrator role authorization for register access
- Expose register aggregates as reporting hooks for Module 12

##### Inputs

- Search text for certificate number or candidate name
- Filter values for examination identifier status issue date range document status
- Pagination page number and page size
- Sort column and direction
- Export request with current filter snapshot

##### Outputs

- Paginated certificate register row set
- Administrator certificate detail with lifecycle timeline events
- CSV export file of filtered certificate records
- Register aggregate counts by status for reporting hooks

##### Business rules

- Register includes ISSUED REVOKED DOCUMENT_PENDING and ISSUANCE_FAILED records within administrator visibility scope
- Export includes only columns approved for administrator operational use; verification tokens are never exported in plain form
- Export row set must match active filter criteria at time of export request
- Lifecycle timeline displays issuance document generation and revocation events in chronological order
- Register access limited to Examination Administrator and authorized oversight roles per Module 01

##### Validations

- Issue date range filter requires end date on or after start date
- Search text length must meet minimum threshold before server search executes
- Export request rejected when estimated row count exceeds configured export limit with administrator message
- Pagination parameters must be within allowed bounds
- Unauthorized session rejected before register data returned

##### Calculations

- Export row count equals count of records matching active filter at export time
- Register status aggregate counts computed per filter scope

##### Workflow

REGISTER_LOADED → SEARCH_OR_FILTER_APPLIED → ROW_SELECTED → DETAIL_VIEWED → EXPORT_REQUESTED → EXPORT_DOWNLOADED

##### Search requirements

- Partial match search on candidate name
- Exact or prefix match search on certificate number
- Combined filter by examination plus status plus issue date range
- Sort by issue date certificate number candidate name and status

##### Documents

- CSV export file of certificate register

##### Reports

- Certificate register status aggregate counts exposed for Module 12 Examination Administration and Reporting hooks

##### Security

- Register list detail and export require Examination Administrator authorization
- CSV export excludes verification token plain values and sensitive internal identifiers
- Export actions audit-logged with administrator identity filter snapshot and row count

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F11-002 Digital Certificate PDF Generation with QR Embedding
- F11-005 Certificate Cancellation and Revocation Management
- F01-00x Examination Administrator authorization (Module 01)
- F12-00x Examination Administration and Reporting hooks (Module 12)

##### Assumptions

- Administrator visibility is global across examinations unless client later requires centre-scoped restriction
- CSV export column set is agreed during requirements sign-off
- Export row limit threshold is configured to protect server performance

##### Risks

- Large export requests during peak season may require asynchronous export enhancement
- Centre-scoped visibility if added later increases authorization complexity
- PII in CSV exports requires client data handling policy compliance

##### Non-functional requirements

- Register search should return first page within interactive SLA under typical data volumes
- Export generation must complete or fail gracefully with clear message for oversized requests
- Register UI must support efficient navigation for thousands of certificate rows via pagination

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Certificate register list with search box and paginated sortable columns | Medium | 16 |
| UI | Certificate register advanced filter panel for examination date range and status | Medium | 16 |
| UI | Certificate register empty state when no rows match active filters | Simple | 5 |
| UI | Administrator certificate detail read-only view with lifecycle timeline | Complex | 18 |
| UI | Certificate register CSV export action button on register toolbar | Easy | 14 |
| UI | Certificate register export confirmation dialog showing row count and filter scope | Simple | 5 |
| API | Search and list certificates with pagination and column sorting | Medium | 6 |
| API | Filter certificates by examination issue date range status and document status | Medium | 6 |
| API | Get administrator certificate detail with lifecycle timeline events | Medium | 6 |
| API | Export filtered certificate register to CSV with column whitelist | Medium | 6 |
| API | Return register status aggregate counts for reporting hook consumers | Easy | 4 |
| Database | Composite indexes supporting register search filter and sort columns | Complex | 0.5 |
| Testing | Happy path search by certificate number returns matching single row | Easy | 0.25 |
| Testing | Combined status and issue date range filter returns accurate row set | Medium | 0.3 |
| Testing | CSV export row set matches on-screen filtered register results | Medium | 0.3 |
| Testing | Export row count limit exceeded returns administrator-facing rejection message | Medium | 0.3 |
| Testing | Unauthorized role blocked from register list detail and export operations | Medium | 0.3 |
| Documentation | Administrator guide for certificate register search filters and export | Easy | 0.25 |
| Documentation | Technical notes for register reporting hook aggregates and export audit logging | Simple | 0.1 |

## 12 Examination Administration & Reporting

745.5 hours · 84 tasks · Business

Department-wide administrator dashboard, operational oversight, and exportable examination MIS reports.

### F12-010 Centre-wise MIS Report Suite

245.15 hours · Go-live · 28 tasks

##### Description

Centre-wise MIS reports covering centre registration allocation summary, centre attendance summary, centre pass-fail summary, and centre session utilization report with filters, on-screen grids, and Excel and PDF export.

##### Business objective

Enable administrators to analyse examination operations and outcomes by authorised examination centre for capacity planning and centre performance review.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Centre-wise MIS Report Suite index.
2. Administrator selects Centre Allocation Summary Report.
3. Parameters include examination cycle, examination, and optional centre multi-select.
4. Grid lists each centre with configured capacity, allocated candidates, utilization percentage, and unallocated overflow count referred from other centres if applicable.
5. Administrator exports allocation summary.
6. Administrator selects Centre Attendance Summary Report.
7. Parameters add session date range.
8. Grid shows appeared, absent, and attendance rate per centre.
9. Administrator selects Centre Pass-Fail Summary Report.
10. Grid shows passed, failed, and pass rate per centre for evaluated candidates.
11. Administrator selects Centre Session Utilization Report.
12. Grid lists session slots per centre with activated versus scheduled counts.
13. Administrator exports each report to Excel and PDF as needed.
14. Empty state when no centres match filters.

##### Functional capabilities

- Centre-wise MIS report suite index
- Centre allocation summary report parameter form
- Centre allocation summary report grid
- Centre attendance summary report parameter form
- Centre attendance summary report grid
- Centre pass-fail summary report parameter form
- Centre pass-fail summary report grid
- Centre session utilization report parameter form
- Centre session utilization report grid
- Excel export per centre-wise report
- PDF export per centre-wise report
- Centre-wise report empty state

##### Inputs

- Examination cycle identifier
- Examination identifier
- Optional centre multi-select
- Optional session date range
- Pagination for large centre lists

##### Outputs

- Centre-wise summary grids
- Excel export files
- PDF export files

##### Business rules

- Only authorised centres from module 03 appear in centre-wise reports
- Allocation counts from module 06 per centre
- Attendance from module 08 per centre
- Pass-fail from module 10 attributed to allotted centre on attempt
- Session utilization compares module 08 activated sessions to module 06 scheduled slots per centre
- Utilization percentage capped at 100 unless overbooking flag configured

##### Validations

- Examination cycle and examination mandatory
- Session date range required for attendance and session utilization reports
- Centre multi-select values must be authorised centres
- Date range within schedule bounds

##### Calculations

- Centre utilization equals allocated divided by capacity multiplied by 100
- Centre attendance rate equals appeared divided by allocated multiplied by 100
- Centre pass rate equals passed divided by evaluated non-absent at centre multiplied by 100
- Session utilization equals activated sessions divided by scheduled sessions multiplied by 100

##### Workflow

Centre reporting flow: ParametersEntry → Generating → ResultsDisplayed → Exporting. Session utilization: Scheduled → Activated when module 08 activates candidate session at centre.

##### Search requirements

- Centre multi-select lookup with code and name search
- Examination lookup

##### Reports

- Centre allocation summary MIS report
- Centre attendance summary MIS report
- Centre pass-fail summary MIS report
- Centre session utilization MIS report

##### Security

- Examination Administrator role required
- Centre-wise reports scoped department-wide not centre-login restricted
- Export audit-logged

##### Dependencies

- Module 01 — User & Role Management: Administrator authorization
- Module 03 — Examination Centre Management: Centre master and capacity
- Module 06 — Examination Scheduling & Allocation: Allocations and schedules
- Module 08 — Centre Operations: Attendance and activation
- Module 10 — Evaluation & Results: Pass-fail by attempt centre

##### Assumptions

- Candidate attributed to centre based on final allocation not preference
- Up to 500 centres per examination supported with pagination

##### Risks

- Centres with zero capacity configuration cause division errors without validation guard
- Cross-centre reassignment after allocation rare; report uses final allocation only

##### Non-functional requirements

- Centre allocation summary for 500 centres generates within 12 seconds
- Paginated centre grid pages load within 3 seconds

##### Notes

SOW section 40 centre-wise reporting views.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre-wise MIS report suite index screen | Easy | 14 |
| UI | Centre allocation summary report parameter form | Medium | 16 |
| UI | Centre allocation summary report result grid | Medium | 16 |
| UI | Centre attendance summary report parameter form | Medium | 16 |
| UI | Centre attendance summary report result grid | Medium | 16 |
| UI | Centre pass-fail summary report parameter form | Medium | 16 |
| UI | Centre pass-fail summary report result grid | Medium | 16 |
| UI | Centre session utilization report parameter form | Medium | 16 |
| UI | Centre session utilization report result grid | Medium | 16 |
| UI | Centre-wise MIS report empty state | Simple | 5 |
| API | Generate centre allocation summary MIS report data | Complex | 8 |
| API | Generate centre attendance summary MIS report data | Complex | 8 |
| API | Generate centre pass-fail summary MIS report data | Complex | 8 |
| API | Generate centre session utilization MIS report data | Complex | 8 |
| API | Export centre allocation summary MIS report to Excel | Complex | 8 |
| API | Export centre allocation summary MIS report to PDF | Complex | 8 |
| API | Export centre attendance summary MIS report to Excel | Complex | 8 |
| API | Export centre attendance summary MIS report to PDF | Complex | 8 |
| API | Export centre pass-fail summary MIS report to Excel | Complex | 8 |
| API | Export centre pass-fail summary MIS report to PDF | Complex | 8 |
| API | Export centre session utilization MIS report to Excel | Complex | 8 |
| API | Export centre session utilization MIS report to PDF | Complex | 8 |
| Database | Reporting indexes for centre-wise allocation attendance pass-fail aggregates | Complex | 0.5 |
| Testing | Happy-path generation and exports for all four centre-wise MIS reports | Complex | 0.5 |
| Testing | Zero-capacity centre utilization guard and invalid date range cases | Medium | 0.3 |
| Testing | Centre pass rate denominator and pagination boundary cases | Medium | 0.3 |
| Documentation | Administrator runbook for centre-wise MIS report parameters and exports | Medium | 0.3 |
| Documentation | Technical notes for centre attribution and utilization calculations | Easy | 0.25 |

### F12-011 Category-wise and Department-wise MIS Report Suite

274.2 hours · Go-live · 30 tasks

##### Description

Category-wise and department-wise MIS reports covering registration counts, fee collection, attendance, and pass-fail outcomes grouped by candidate category and government department or organisation affiliation with parameter forms, on-screen grids, and Excel and PDF export.

##### Business objective

Support departmental management reporting on examination participation and outcomes segmented by candidate category and department or organisation for policy and workforce planning.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Category-wise and Department-wise MIS Report Suite index.
2. Administrator selects Category-wise Registration Summary Report.
3. Parameter form captures examination cycle, optional examination, and category multi-select.
4. Grid displays registration counts and percentage share per category with totals row.
5. Administrator exports category registration summary to Excel and PDF.
6. Administrator selects Department-wise Registration Summary Report.
7. Parameters include examination cycle, examination, and optional department multi-select.
8. Grid lists departments with registration counts sorted descending.
9. Administrator selects Category-wise Pass-Fail Report.
10. Grid shows appeared, passed, failed, and pass rate per category.
11. Administrator selects Department-wise Pass-Fail Report.
12. Grid shows pass-fail metrics per department for selected examination.
13. Administrator selects Category-wise Fee Collection Report.
14. Grid shows collected fee totals per category.
15. Administrator exports each report as needed.
16. Empty state when filters yield no rows.
17. Validation errors display for missing mandatory examination cycle.

##### Functional capabilities

- Category and department MIS report suite index
- Category-wise registration summary report parameter form
- Category-wise registration summary report grid
- Department-wise registration summary report parameter form
- Department-wise registration summary report grid
- Category-wise pass-fail report parameter form
- Category-wise pass-fail report grid
- Department-wise pass-fail report parameter form
- Department-wise pass-fail report grid
- Category-wise fee collection report parameter form
- Category-wise fee collection report grid
- Excel export per category and department report
- PDF export per category and department report
- Category and department report empty state
- Category and department report parameter validation display

##### Inputs

- Report identifier
- Examination cycle identifier
- Optional examination identifier
- Category multi-select filter
- Department multi-select filter
- Optional date range

##### Outputs

- Category-wise summary grids
- Department-wise summary grids
- Excel export files
- PDF export files

##### Business rules

- Candidate category sourced from module 05 registration category at time of registration
- Department attribution uses KGID department for government employees and organisation name for PSU and other categories
- Unclassified department bucket captures registrations missing department affiliation
- Pass-fail metrics include only evaluated attempts
- Fee collection category-wise totals include successful payments only
- Percentage share columns calculated against report totals row

##### Validations

- Examination cycle mandatory on all reports
- Category multi-select optional; empty means all categories
- Department multi-select optional; empty means all departments
- Date range within examination cycle bounds when provided
- Department filter ignored on category-only reports and vice versa where not applicable

##### Calculations

- Category registration share equals category count divided by total registrations multiplied by 100
- Department pass rate equals department passed divided by department evaluated non-absent multiplied by 100
- Category fee total sums successful payment amounts for registrations in that category

##### Workflow

Report flow: ParametersEntry → Validating → Generating → ResultsDisplayed → Exporting. Category assignment fixed at registration confirmation per module 05.

##### Search requirements

- Category multi-select lookup
- Department multi-select lookup with code and name search
- Examination lookup

##### Reports

- Category-wise registration summary MIS report
- Department-wise registration summary MIS report
- Category-wise pass-fail MIS report
- Department-wise pass-fail MIS report
- Category-wise fee collection MIS report

##### Security

- Examination Administrator role required
- Department-wise reports may contain workforce statistics subject to departmental data classification policy
- Export audit-logged with report type and filter snapshot

##### Dependencies

- Module 01 — User & Role Management: Administrator authorization
- Module 02 — API Integration Hub: KGID department fields on government employee registrations
- Module 05 — Candidate Registration: Category, department, and organisation affiliation
- Module 08 — Centre Operations: Attendance for pass-fail denominators
- Module 10 — Evaluation & Results: Pass-fail outcomes
- Module 02 — API Integration Hub: Payment records for category fee report

##### Assumptions

- Department master list aligns with KGID department codes for government employees
- PSU and other organisation candidates grouped by organisation name text field

##### Risks

- Inconsistent department naming for non-government candidates may fragment department-wise totals
- Large department master may require top-N filtering on reports

##### Non-functional requirements

- Department-wise pass-fail report for 200 departments generates within 10 seconds
- Category reports generate within 5 seconds for up to 20 categories

##### Notes

SOW section 40 category-wise and department-wise reporting views for government and other organisation candidates.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Category-wise and department-wise MIS report suite index screen | Easy | 14 |
| UI | Category-wise registration summary report parameter form | Medium | 16 |
| UI | Category-wise registration summary report result grid | Medium | 16 |
| UI | Department-wise registration summary report parameter form | Medium | 16 |
| UI | Department-wise registration summary report result grid | Medium | 16 |
| UI | Category-wise pass-fail report parameter form | Medium | 16 |
| UI | Category-wise pass-fail report result grid | Medium | 16 |
| UI | Department-wise pass-fail report parameter form | Medium | 16 |
| UI | Department-wise pass-fail report result grid | Medium | 16 |
| UI | Category-wise fee collection report parameter form | Medium | 16 |
| UI | Category-wise fee collection report result grid | Medium | 16 |
| UI | Category and department MIS report empty state | Simple | 5 |
| UI | Category and department MIS report parameter validation error display | Simple | 5 |
| API | Generate category-wise registration summary MIS report data | Complex | 8 |
| API | Generate department-wise registration summary MIS report data | Complex | 8 |
| API | Generate category-wise pass-fail MIS report data | Complex | 8 |
| API | Generate department-wise pass-fail MIS report data | Complex | 8 |
| API | Generate category-wise fee collection MIS report data | Complex | 8 |
| API | Export category-wise registration summary MIS report to Excel | Complex | 8 |
| API | Export category-wise registration summary MIS report to PDF | Complex | 8 |
| API | Export department-wise registration summary MIS report to Excel | Complex | 8 |
| API | Export department-wise registration summary MIS report to PDF | Complex | 8 |
| API | Export category-wise pass-fail MIS report to Excel | Complex | 8 |
| API | Export department-wise pass-fail MIS report to PDF | Complex | 8 |
| Database | Reporting indexes for category and department dimension aggregates | Complex | 0.5 |
| Testing | Happy-path generation and exports for all five category and department reports | Complex | 0.5 |
| Testing | Unclassified department bucket and empty multi-select all-categories cases | Medium | 0.3 |
| Testing | Category share percentage and pass rate denominator edge cases | Medium | 0.3 |
| Documentation | Administrator runbook for category-wise and department-wise MIS reports | Medium | 0.3 |
| Documentation | Technical notes for department attribution rules across candidate categories | Medium | 0.3 |

### F12-012 Certificate MIS Report Suite

226.15 hours · Go-live · 26 tasks

##### Description

Certificate MIS report suite covering certificate issuance summary, certificate eligibility backlog report, certificate status register report, and examination-wise certificate statistics with parameter forms, on-screen grids, and Excel and PDF export.

##### Business objective

Provide Examination Administrators MIS reporting on certificate issuance progress, eligibility backlog, and revoked certificates for departmental compliance reporting.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Certificate MIS Report Suite index.
2. Administrator selects Certificate Issuance Summary Report.
3. Parameter form requires examination cycle and optional examination multi-select.
4. Grid displays eligible, issued, pending issuance, and revoked counts per examination.
5. Administrator exports issuance summary to Excel and PDF.
6. Administrator selects Certificate Eligibility Backlog Report.
7. Parameters include examination cycle, examination, and optional days-pending threshold.
8. Grid lists candidates eligible but not yet issued with registration number, name, eligibility date, and days pending.
9. Administrator exports backlog listing to Excel.
10. Administrator selects Certificate Status Register Report.
11. Parameters allow filter by certificate status issued revoked cancelled.
12. Grid lists certificate number, candidate name, examination, issue date, status, and revocation date if applicable.
13. Administrator searches certificate register by certificate number or candidate name.
14. Administrator selects Examination-wise Certificate Statistics Report.
15. Grid shows issuance rate and revocation count per examination.
16. Administrator exports each report as needed.
17. Empty and validation error states display when applicable.

##### Functional capabilities

- Certificate MIS report suite index
- Certificate issuance summary report parameter form
- Certificate issuance summary report grid
- Certificate eligibility backlog report parameter form
- Certificate eligibility backlog report grid
- Certificate status register report parameter form
- Certificate status register report grid with search
- Examination-wise certificate statistics report parameter form
- Examination-wise certificate statistics report grid
- Excel export per certificate MIS report
- PDF export per certificate MIS report
- Certificate MIS report empty state
- Certificate MIS report parameter validation errors

##### Inputs

- Report identifier
- Examination cycle identifier
- Optional examination multi-select
- Certificate status filter
- Days-pending threshold for backlog report
- Search text for certificate register
- Pagination parameters

##### Outputs

- Certificate summary and register grids
- Excel export files
- PDF export files

##### Business rules

- Certificate eligibility determined by module 11 rules after module 10 pass outcome
- Issued count includes active certificates with issued status
- Revoked and cancelled certificates counted separately in status register
- Backlog report includes only eligible-not-issued records
- Certificate numbers displayed in register when issued
- Public verification portal functionality remains module 11 out of scope for this module

##### Validations

- Examination cycle mandatory
- Days-pending threshold must be non-negative integer
- Certificate status filter limited to issued, eligible-not-issued, revoked, cancelled
- Certificate number search requires minimum five characters
- Backlog export row limit enforced

##### Calculations

- Days pending equals current date minus eligibility date for backlog rows
- Issuance rate equals issued divided by eligible multiplied by 100
- Pending issuance equals eligible minus issued excluding revoked before issue

##### Workflow

Certificate display lifecycle: NotEligible → Eligible → Issued; Issued → Revoked or Cancelled. Report flow: ParametersEntry → Generating → ResultsDisplayed → Exporting.

##### Search requirements

- Certificate number partial and exact search
- Candidate name partial search on status register
- Examination multi-select lookup

##### Reports

- Certificate issuance summary MIS report
- Certificate eligibility backlog MIS report
- Certificate status register MIS report
- Examination-wise certificate statistics MIS report

##### Security

- Examination Administrator role required
- Certificate register export contains PII governed by masking policy
- Certificate report access audit-logged
- Revocation details visible to administrators only not public verification scope

##### Dependencies

- Module 01 — User & Role Management: Administrator authorization
- Module 05 — Candidate Registration: Candidate identity on certificate records
- Module 04 — Question Bank & Examination Configuration: Examination definitions
- Module 10 — Evaluation & Results: Pass outcome driving eligibility
- Module 11 — Certificate Management: Eligibility, issuance, numbering, and revocation states

##### Assumptions

- Certificate eligibility date stored when eligibility first determined in module 11
- QR code and PDF generation logic not duplicated; reports reference certificate metadata only

##### Risks

- Large backlog exports may expose significant PII volume requiring export approval workflow in future
- Eligibility backlog counts mismatch if batch issuance jobs lag

##### Non-functional requirements

- Certificate issuance summary generates within 8 seconds for 50,000 certificate records
- Status register search returns first page within 3 seconds

##### Notes

SOW section 40 certificate report suite; certificate transactional logic remains module 11.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Certificate MIS report suite index screen | Easy | 14 |
| UI | Certificate issuance summary report parameter form | Medium | 16 |
| UI | Certificate issuance summary report result grid | Medium | 16 |
| UI | Certificate eligibility backlog report parameter form | Medium | 16 |
| UI | Certificate eligibility backlog report result grid with days pending column | Medium | 16 |
| UI | Certificate status register report parameter form | Medium | 16 |
| UI | Certificate status register report searchable result grid | Medium | 16 |
| UI | Examination-wise certificate statistics report parameter form | Medium | 16 |
| UI | Examination-wise certificate statistics report result grid | Medium | 16 |
| UI | Certificate MIS report empty state | Simple | 5 |
| UI | Certificate MIS report parameter validation error display | Simple | 5 |
| API | Generate certificate issuance summary MIS report data | Complex | 8 |
| API | Generate certificate eligibility backlog MIS report data | Complex | 8 |
| API | Search and generate certificate status register MIS report data | Complex | 8 |
| API | Generate examination-wise certificate statistics MIS report data | Complex | 8 |
| API | Export certificate issuance summary MIS report to Excel | Complex | 8 |
| API | Export certificate issuance summary MIS report to PDF | Complex | 8 |
| API | Export certificate eligibility backlog MIS report to Excel | Complex | 8 |
| API | Export certificate status register MIS report to Excel | Complex | 8 |
| API | Export examination-wise certificate statistics MIS report to PDF | Complex | 8 |
| Database | Reporting indexes for certificate eligibility issuance and status aggregates | Complex | 0.5 |
| Testing | Happy-path generation search and exports for all four certificate MIS reports | Complex | 0.5 |
| Testing | Days pending calculation and certificate number search minimum length cases | Medium | 0.3 |
| Testing | Revoked certificate status display and PII masking in export cases | Medium | 0.3 |
| Documentation | Administrator runbook for certificate MIS reports and backlog monitoring | Medium | 0.3 |
| Documentation | Technical notes for certificate status enumerations aligned with module 11 | Easy | 0.25 |
