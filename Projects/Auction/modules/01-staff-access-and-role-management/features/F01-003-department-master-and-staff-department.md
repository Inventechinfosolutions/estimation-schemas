# F01-003 — Department Master and Staff Department

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | Department Master and Staff Department |
| **Module** | 01 — Staff Access and Role Management |

### Description
Departments are the organisational attribute on a staff user and on an auction. The administrator maintains the department list. Auction creation later requires a department, and bidders can filter published auctions by department. This is a flat list, not an organisation tree or a post hierarchy.

### Business Objective
Auctions and staff can be separated by department without inventing a reporting structure the source does not describe.

### Actors
Maker: System / Catalogue Administrator. Approver: none.

### User Journey
1. Who creates: the System / Catalogue Administrator creates a department.
2. How they create: Departments → New → name and active status → Save.
3. How they edit: open the department and change the name or deactivate it. Existing auctions keep the department they were filed under.
4. How they send for approval: they do not. Department maintenance has no approval step.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: department change history shows name and active-status changes.
8. How the auditor sees history: the same history is limited to the System / Catalogue Administrator.

### Functional Capabilities
- Create, rename, activate, and deactivate a department
- Search the department list
- Supply the department list to staff accounts and to auction creation
- Keep a deactivated department on historical auctions while hiding it from new auctions

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Department name
- Active or inactive

### Outputs
- Department list used by staff accounts, auction drafts, and bidder search

### Business Rules
- Department name is unique.
- A deactivated department cannot be selected on a new staff account or a new auction.
- Deactivation does not move existing auctions to another department.
- There is no parent department and no post under the department.

### Validations
- Name is mandatory.
- Duplicate names are rejected.

### Calculations
None.

### Workflow
Immediate save. No approval.

### Search Requirements
Name and active status.

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
Only the System / Catalogue Administrator maintains departments. Auction creators may select an active department; they may not edit the master.

### Integrations
None.

### Dependencies
None. Staff accounts and auctions depend on this list.

### Assumptions
- The source uses Department as a field on the auction and as a search filter. A single-level list matches that field.
- Staff department is captured on F01-001; this feature owns the master those screens select.

### Risks
If the organisation later needs sub-departments, this master has to grow. That is a scope change.

### Non Functional Requirements
The active department list is available to auction creation and bidder search without a separate extract.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Department register | UI | Easy | 4 |
| Department form | UI | Easy | 4 |
| Save department | API | Easy | 4 |
| Search departments | API | Easy | 4 |
| Department master records | DB | Easy | 2 |
| Department master tests | Testing | Easy | 4 |
| Department master notes | Documentation | Easy | 2 |

**Feature total: 24 hours**
