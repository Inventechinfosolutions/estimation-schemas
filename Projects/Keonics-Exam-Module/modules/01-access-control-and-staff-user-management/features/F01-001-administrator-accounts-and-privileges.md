# F01-001 — Administrator Accounts and Privileges

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Administrator Accounts and Privileges |
| **Module** | 01 — Access Control and Staff User Management |

### Description
Examination Administrators are created and maintained as staff accounts with role-based privileges over examinations, centres, schedules, registrations, question bank, examination parameters, results, certificates, reports and dashboards. An authorised Administrator (or bootstrap super-admin) opens the administrator register, creates or updates an Administrator account, assigns privilege sets aligned to Examination Administrator functions, and activates or deactivates the account. Inactive Administrator accounts cannot log in. Centre / Invigilator accounts are out of scope here and belong to F01-002. Candidate portal OTP identity is separate and not managed in this feature.

### Business Objective
Ensure only authorised Examination Administrator users can access and operate staff administration functions, with privileges that match Department-approved Administrator duties and with activation control so inactive accounts are blocked from login.

### Actors
Bootstrap / Super Administrator (initial setup); Examination Administrator (manage peer Administrator accounts where permitted); Auditor (read-only account and privilege history).

### User Journey
1. Who creates: A Super Administrator or an Examination Administrator with user-administration privilege creates Administrator accounts.
2. How they create: Open the Administrator user register → New Administrator → enter staff identity (name, official mobile, official email, employee/reference id if used) → assign Examination Administrator role and privilege groups (administration, centres, question bank, scheduling, results, certificates, reports) → save as Active or Pending Activation.
3. How they edit: Search the register → open the account → update contact details, privilege groups or role scope → save; privilege reductions take effect on next request or forced re-login as configured.
4. How they send for approval: Submit/approval does not apply for routine Administrator provisioning unless the Department later mandates maker–checker; the maker saves and activates directly under user-admin privilege.
5. How the approver sees pending items: There is no approver inbox for this feature; pending activation, if used, appears only as status on the Administrator register for the same privileged user.
6. How the approver decides: There is no separate approval decision; activate/deactivate is an administrative action on the account, not a workflow decision.
7. How the applicant / maker sees history: The creating Administrator opens account change history (who changed privileges, activation, contacts, when).
8. How the approver / auditor sees history: Auditor (or privileged Administrator) opens the same change history and activation timeline for forensic review.

### Functional Capabilities
- Maintain an Administrator user register with create, view, update, search and status filter (Active / Inactive).
- Capture staff identity fields required for Administrator login and contact (name, official email, official mobile, optional employee/reference id).
- Assign Examination Administrator role and privilege groups covering administration, centre masters, question bank, scheduling, registrations, results, certificates, reports and dashboards.
- Enforce that Administrator menus and actions appear only when the account holds the corresponding privilege.
- Activate and deactivate Administrator accounts; refuse login for Inactive accounts.
- Prevent removal of the last active Super/Administrator with user-admin privilege (or equivalent safety rule) so the system is not locked out.
- Record before/after values for privilege and activation changes for audit.
- Separate Administrator staff identity from candidate OTP portal identity and from centre-scoped Invigilator accounts (F01-002).
- Support forced session invalidation or re-login after privilege downgrade where configured.
- Allow read-only Auditor access to the register and history without edit rights.
- Validate uniqueness of login identifier / official mobile / email per Department identity rules.
- Display privilege summary on the account so operators can confirm what the Administrator can do before activation.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Administrator user register and search | Complex |
| Administrator create / edit form | Medium |
| Privilege and role assignment matrix | Complex |
| Activate / deactivate confirmation | Simple |
| Administrator account change history | Medium |
| Administrator privilege summary view | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create Administrator account | Complex |
| Update Administrator particulars | Medium |
| Assign or revise privilege groups | Complex |
| Activate or deactivate Administrator | Medium |
| Search Administrator register | Medium |
| Read Administrator change history | Easy |
| Enforce privilege check for staff action | Complex |

### Inputs
Administrator name; official email; official mobile; optional employee/reference id; role = Examination Administrator; privilege group selections; activation status; maker remarks.

### Outputs
Persisted Administrator account; privilege assignment; Active/Inactive status enforceable at login; searchable register; audited change history; privilege summary for operators.

### Business Rules
- Only users with user-administration privilege may create or change Administrator accounts and privileges.
- Inactive Administrator accounts cannot log in to the staff application.
- Administrator functions (examinations, centres, question bank, scheduling, results, certificates, reports) are available only to authorised Administrator users.
- Centre-only Invigilator users are not created here; they are managed under F01-002 with centre mapping.
- Candidate portal OTP accounts are not Administrator accounts.
- At least one Active account with user-admin privilege must remain (lock-out prevention).
- Privilege changes must be auditable with actor, timestamp and before/after privilege set.

### Validations
- Name, official mobile and official email are mandatory for a new Administrator.
- Login identifier / mobile / email uniqueness within staff Administrator accounts.
- At least one privilege group must be assigned before activation, or Department-defined full Administrator pack.
- Deactivation of the last user-admin account is blocked.
- Status transitions only between allowed Active and Inactive values.

### Calculations
None beyond counts of Active Administrators and privilege-group membership used for lock-out prevention.

### Workflow
Direct administration with audit. No maker–checker approval inbox unless the Department later mandates it. Activation is an administrative toggle, not a multi-stage approval.

### Search Requirements
Name, official mobile, official email, employee/reference id, status (Active/Inactive), privilege group, created/updated date range.

### Documents
None required for this feature (no identity document pack for staff Administrator create in the SOW).

### Reports
Administrator register export (Active/Inactive, privilege summary) for operations and audit.

### Notifications
Optional staff notification on account activation or privilege change if configured in Module 09; not mandatory for this feature’s core behaviour.

### Security
Role- and privilege-based access; only user-admin may mutate Administrator accounts; Inactive accounts blocked at login; all create/update/activate/deactivate actions audited with actor and timestamp; privilege checks on every privileged staff action.

### Integrations
None for this feature (no SMS/KGID/payment channel). Staff authentication is internal to the Examination Module staff channel.

### Dependencies
Foundational for all later Administrator-facing modules (03–09). Consumed by F01-002 only insofar as roles are distinct; no hard dependency on F01-002 to create Administrators.

### Assumptions
- Staff access model is User → Role → Privileges (Administrator vs Centre/Invigilator), with centre scoping applied only in F01-002.
- Bootstrap Super Administrator exists for first go-live provisioning.
- SSO / Active Directory is out of scope unless later ordered.
- Hours use Estimation Master values; each named screen and logical API is billed independently.

### Risks
- Over-broad privilege packs could expose question bank or results functions to unintended Administrators.
- Accidental deactivation of all user-admin accounts would lock out administration (mitigated by last-admin rule).
- Confusing Administrator accounts with centre Invigilator accounts would break centre isolation expectations.

### Non Functional Requirements
Staff administration screens must be usable during registration and examination windows; privilege enforcement must apply consistently on every privileged request; activation and privilege changes must be attributable to a named Administrator with timestamp; response for register search should support operational volumes of staff users without multi-second delays under expected staff counts.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Administrator user register and search | UI | Complex | 12 |
| Administrator create / edit form | UI | Medium | 6 |
| Privilege and role assignment matrix | UI | Complex | 12 |
| Activate / deactivate confirmation | UI | Simple | 2 |
| Administrator account change history | UI | Medium | 6 |
| Administrator privilege summary view | UI | Easy | 4 |
| Create Administrator account | API | Complex | 8 |
| Update Administrator particulars | API | Medium | 6 |
| Assign or revise privilege groups | API | Complex | 8 |
| Activate or deactivate Administrator | API | Medium | 6 |
| Search Administrator register | API | Medium | 6 |
| Read Administrator change history | API | Easy | 4 |
| Enforce privilege check for staff action | API | Complex | 8 |
| Administrator account and privilege persistence | DB | Complex | 6 |
| Administrator accounts feature tests | Testing | Complex | 8 |
| Administrator accounts implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **105** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- No Integration row — no external SMS/KGID/payment channel in this feature.
- Screens assume production-quality enterprise build with validation, logging and security.
