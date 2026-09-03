# F01-003 — RBAC menus and need-to-know visibility

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | RBAC menus and need-to-know visibility |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
After login, the staff member sees only menus and screens allowed for their current Post and Roles. If they try to open another officer’s restricted claim pack, depositor KYC, asset or payment record, the system refuses access and writes an audit event. Need-to-know applies across Claim and is reused by Legal and Valuation consumers of this IAM.

### Business Objective
Prevent unauthorised menu and record access and record every denied attempt against the acting Person and Post.

### Actors
Staff member acting in a mapped Post; Administrator (permission configuration via Roles); auditor.

### User Journey
1. Who creates: Staff member acting in a mapped Post
2. How they create: Staff member authenticates (F01-006) and the session resolves current Posts and Roles (F01-002).
3. How they edit: The staff web application shows only menus and screens allowed for those Roles.
4. How they send for approval: If the staff member opens a claim pack, depositor KYC, asset or payment record outside need-to-know, access is refused. Evaluated at login (menu) and on each restricted open (record). No approval workflow.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Staff member acting in a mapped Post works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Staff member acting in a mapped Post opens history on the record. The refusal is written as an audit event (Person, Post, resource, timestamp, channel). An auditor can later retrieve denied-access events from the forensic register (F01-010).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Compose staff menus from current Post/Role permissions.
- Enforce need-to-know on claim packs, depositor KYC, attached assets and payment records.
- Refuse unauthorised deep-links and write an audit event.
- Separate staff menus from the constrained OOK claimant shell (F01-008).

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Post-filtered staff menu composition | Complex |
| Need-to-know denial and audit notice | Easy |
| Rbac menus and need-to-know visibility history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Permission evaluation and record-scope operations | Very High |
| Update rbac menus and need-to-know visibility | Medium |
| Search rbac menus and need-to-know visibility | Medium |
| Read rbac menus and need-to-know visibility history | Easy |

### Inputs
Current Post/Role set; requested menu or record; channel (staff web).

### Outputs
Filtered menu; granted or denied access; audit event on denial.

### Business Rules
- Visibility follows Person → Post → Role → Permissions for the current effective mapping.
- Restricted claim, KYC, asset and payment records are not globally searchable for unauthorised Posts.
- OOK claimants never receive staff menus.

### Validations
- Session without a current Post mapping cannot open staff modules.
- Record-level checks run even when the menu item is hidden.

### Calculations
Permission evaluation against Role permission sets and record scope.

### Workflow
Evaluated at login (menu) and on each restricted open (record). No approval workflow.

### Search Requirements
Not a user-facing search feature; unauthorised records must not appear in staff search results.

### Documents
Document view/download rights are F01-009; this feature gates the screens that open the pack.

### Reports
Denied-access events appear in F01-010; not a standalone report here.

### Notifications
None to the denied user beyond an on-screen refusal.

### Security
Least privilege; denied attempts are auditable; no silent fallback to a shared role.

### Integrations
Internal authorisation evaluation used by all claim modules and by Legal / Valuation consumers.

### Dependencies
F01-001, F01-002; staff 2FA session (F01-006).

### Assumptions
- Permission catalogue covers claim, depositor, asset, payment, report and administration functions.
- Org-unit scoping beyond Post is not required unless the Authority later adds it.

### Risks
- Over-broad Role permissions would expose KYC and payment data.
- Menu hiding without record-level checks would leak data via direct open.

### Non Functional Requirements
This is the programme-wide identity product consumed by Legal Management and GIS field valuation; staff screens must remain usable during claim windows; privileged actions are attributable to a named Person acting in a Post; primary official hosting identity is an approved government domain, not .org. Permission checks must not prevent authorised Officers from working a claim window.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Post-filtered staff menu composition | UI | Complex | 12 |
| Need-to-know denial and audit notice | UI | Easy | 4 |
| Rbac menus and need-to-know visibility history | UI | Medium | 6 |
| Permission evaluation and record-scope operations | API | Very High | 16 |
| Update rbac menus and need-to-know visibility | API | Medium | 6 |
| Search rbac menus and need-to-know visibility | API | Medium | 6 |
| Read rbac menus and need-to-know visibility history | API | Easy | 4 |
| Permission and visibility persistence | DB | Complex | 6 |
| Internal authorisation handoff | Integration | Easy | 8 |
| RBAC menus and need-to-know visibility feature tests | Testing | Very High | 12 |
| RBAC menus and need-to-know visibility implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **83** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
