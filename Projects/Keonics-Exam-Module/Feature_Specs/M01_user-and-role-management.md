# Module 01: User & Role Management

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 12 (F01-007 … F01-020)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

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
