# F01-001 — Project Staff Accounts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Project Staff Accounts |
| **Module** | 01 — User and Access Management |

### Description
Supervisor (and Department, as agreed) creates accounts for Service Provider operators/supervisors and Department authorised officers with name, designation and ID for the DMG Bengaluru Urban scanning site.

### Business Objective
Only named people may touch files or the operational tool during the two-month job.

### Actors
Maker: Service Provider Supervisor (SP staff); Department Officer (Department staff if they maintain their side). Approver: none.

### User Journey
1. Who creates: Supervisor creates SP accounts; Department Officer may confirm Department officer accounts.
2. How they create: Staff register → New → name, designation, ID, role (Operator / Supervisor / Department Officer) → Save.
3. How they edit: Open the account and update name, designation, ID or role. History is kept.
4. How they send for approval: Does not apply. Save is final.
5. How the approver sees pending items: There is no approver inbox.
6. How the approver decides: There is no approval decision.
7. How the maker sees history: Account change history (who, when).
8. How the auditor sees history: Supervisor and Department Officer use the same history.

### Functional Capabilities
- Create SP and Department accounts
- Edit profile and role
- Search by name, ID, role
- View change history

### UI Screens
| Screen | Complexity |
|---|---|
| Project staff register | Medium |
| Staff account form | Medium |
| Account change history | Easy |

### Logical API operations
| Operation | Complexity |
|---|---|
| Create staff account | Medium |
| Update staff account | Medium |
| Search staff accounts | Medium |
| Read account history | Easy |

### Inputs
Name, designation, ID, role.

### Outputs
Persisted accounts used on logs.

### Business Rules
- ID unique per project site.
- One role per account.
- Files never attributed to an unnamed person.

### Validations
- Name, ID and role mandatory.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
Name, designation, ID, role, enabled/disabled.

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
Supervisor maintains SP staff; Department Officer sees Department list.

### Integrations
None.

### Dependencies
None.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Enable/disable is included as status on this account (no separate feature).

### Risks
Shared logins would break custody; process must forbid them.

### Non Functional Requirements
Usable on site PCs; changes attributable.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Project staff register | UI | Medium | 6 |
| Staff account form | UI | Medium | 6 |
| Account change history | UI | Easy | 4 |
| Create staff account | API | Medium | 6 |
| Update staff account | API | Medium | 6 |
| Search staff accounts | API | Medium | 6 |
| Read account history | API | Easy | 4 |
| Staff account records | DB | Medium | 4 |
| Project staff accounts tests | Testing | Medium | 6 |
| Project staff accounts implementation documentation | Documentation | Easy | 2 |

**Feature total: 50 hours**
