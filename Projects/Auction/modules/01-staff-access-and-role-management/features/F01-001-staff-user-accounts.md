# F01-001 — Staff User Accounts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Staff User Accounts |
| **Module** | 01 — Staff Access and Role Management |

### Description
The System / Catalogue Administrator creates a named account for each person who will administer the catalogue, create auctions, approve them, evaluate bidders, monitor a live auction, finalise a result, or award. The account holds name, official email, department, and whether the person is active. Bidder portal accounts are not created here.

### Business Objective
Every later staff action can be attributed to a real, active person rather than a shared login.

### Actors
Maker: System / Catalogue Administrator. Approver: none. The account holder is the subject, not the approver.

### User Journey
1. Who creates: the System / Catalogue Administrator creates the staff account. A department user cannot create accounts for other people.
2. How they create: Staff accounts → New account → name, official email, department, active status → Save. The person does not yet have a role until F01-002.
3. How they edit: open the account from the register and change name, email, department, or active status. Email must stay unique.
4. How they send for approval: they do not. Saving an account is final. Role assignment is a separate action in F01-002.
5. How the approver sees pending items: there is no approver inbox for staff accounts.
6. How the approver decides: there is no approval decision on this feature.
7. How the maker sees history: the administrator opens account change history and sees who changed name, department, or active status, and when.
8. How the auditor sees history: the same history is available to the System / Catalogue Administrator. Other roles do not browse the staff register.

### Functional Capabilities
- Create a staff account with name, official email, and department
- Edit those details and deactivate or reactivate the account
- Search accounts by name, email, department, and active status
- Read the change history of an account
- Keep bidder accounts out of this register

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Full name
- Official email
- Department
- Active or inactive status

### Outputs
- An active or inactive staff account that can later receive roles
- Change history of the account

### Business Rules
- Email is unique across staff accounts.
- A new account is inactive for sign-in until F01-004 credentials exist and at least one role is assigned. The account record itself may be saved before that.
- Deactivating an account blocks sign-in immediately. It does not delete auctions that person already created.
- Department is required and must be an active department from F01-003.
- Bidder self-registration never writes a row in the staff register.

### Validations
- Name, email, and department are mandatory.
- Email must be a valid address and not already used by another staff account.
- Inactive department cannot be selected.

### Calculations
None.

### Workflow
No approval. Save, edit, and deactivate are immediate.

### Search Requirements
Name, email, department, active or inactive.

### Documents
None.

### Reports
None. The register is the operational list.

### Notifications
None on this feature. The person is told out of band how to set a password until F01-004 is used.

### Security
Only the System / Catalogue Administrator maintains this register. A staff user may see their own name and department, not the full register.

### Integrations
None.

### Dependencies
F01-003 department master should exist before a department can be chosen. The screen must still allow the administrator to create the department first.

### Assumptions
- One person, one staff account. Shared mailboxes are not a supported operating model.
- Hours follow the agreed effort catalogue: each named screen and each logical operation is counted on its own.

### Risks
Shared accounts would make approval and force-close history meaningless.

### Non Functional Requirements
Account deactivation takes effect on the next request, not only at the next sign-in.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Staff user register | UI | Medium | 6 |
| Staff account form | UI | Medium | 6 |
| Account change history | UI | Easy | 4 |
| Create staff account | API | Medium | 6 |
| Update staff account | API | Medium | 6 |
| Search staff accounts | API | Medium | 6 |
| Read account change history | API | Easy | 4 |
| Staff account records | DB | Medium | 4 |
| Staff user account tests | Testing | Medium | 6 |
| Staff user account notes | Documentation | Easy | 2 |

**Feature total: 50 hours**
