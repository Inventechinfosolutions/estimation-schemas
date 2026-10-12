# F01-002 — Role Assignment and Permissions

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Role Assignment and Permissions |
| **Module** | 01 — Staff Access and Role Management |

### Description
The administrator attaches one or more staff roles to an account and the system limits later actions to those roles. The roles are System / Catalogue Administrator, Auction Creator, Reviewing / Approving Authority, Evaluation Authority, Auctioning Authority, Finalisation Authority, and Awarding Authority. Bidder is not a role on this screen.

### Business Objective
A person can perform only the auction duties their roles allow, and a single person may hold more than one duty when the organisation chooses.

### Actors
Maker: System / Catalogue Administrator. Approver: none. Affected user: the staff account being changed.

### User Journey
1. Who creates: the System / Catalogue Administrator assigns roles. The staff user cannot grant roles to themselves.
2. How they create: open the staff account → Assign roles → tick one or more of the seven staff roles → Save.
3. How they edit: open the same assignment and add or remove roles. Removal takes effect on the next action.
4. How they send for approval: they do not. Role assignment is an administrative save, not an auction approval.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: role-change history shows previous roles, new roles, who changed them, and when.
8. How the auditor sees history: the System / Catalogue Administrator reads that same history. Other roles see only the effect (a button is absent), not the assignment log.

### Functional Capabilities
- List the seven staff roles and what each may do
- Assign or remove one or more roles on a staff account
- Enforce the role on create, approve, evaluate, monitor, force close, finalise, and award
- Record role-change history

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Staff account
- One or more staff roles

### Outputs
- Effective permissions used by every later staff screen
- Role-change history

### Business Rules
- Only the seven named staff roles exist. A free-text role cannot be invented on the screen.
- System / Catalogue Administrator is the only role that may maintain accounts, roles, departments, categories, and catalogue items across departments.
- Auction Creator, reviewer, evaluator, auctioning authority, finalisation authority, and awarding authority act on auctions of their own department.
- Removing the last role does not delete the account. The person can sign in only if F01-004 allows, but will have no working menu.
- Holding several roles does not bypass department scope, except for System / Catalogue Administrator.

### Validations
- At least the account must exist.
- Unknown role codes are rejected.
- A deactivated account can keep stored roles, but those roles do nothing until reactivation.

### Calculations
None.

### Workflow
Immediate save. No approval chain.

### Search Requirements
Find an account, then see its roles. Filter the register by role.

### Documents
None.

### Reports
None.

### Notifications
None. The affected person sees the new menu on the next sign-in or refresh.

### Security
Only System / Catalogue Administrator can change roles. A user cannot elevate themselves.

### Integrations
None.

### Dependencies
F01-001 staff account.

### Assumptions
- Separation of duties is achieved by giving roles to different people. The system does not forbid one person from holding creator and approver roles, because the source allows the organisation to assign roles to people.
- Permission checks are applied on the action, not only by hiding a menu.

### Risks
If the only administrator locks themselves out of the role, recovery needs an operational procedure outside this feature.

### Non Functional Requirements
A role change applies to the next business action of that user, including a session that is already open.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Role catalogue | UI | Medium | 6 |
| Role assignment screen | UI | Complex | 12 |
| Role change history | UI | Easy | 4 |
| Read role catalogue | API | Easy | 4 |
| Save role assignment | API | Complex | 8 |
| Read effective permissions | API | Medium | 6 |
| Role and permission records | DB | Complex | 6 |
| Role assignment tests | Testing | Complex | 8 |
| Role assignment notes | Documentation | Medium | 3 |

**Feature total: 57 hours**
