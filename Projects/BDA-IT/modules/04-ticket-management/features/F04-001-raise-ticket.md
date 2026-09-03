# F04-001 — Raise Ticket

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Raise Ticket |
| **Module** | 04 — Ticket Management |

### Description
A logged-in User submits an IT support ticket by selecting a **ticket category from the dropdown** (values created by Admin in F02-001), entering a short problem description, and optionally attaching one supporting file. The ticket is stored as **Open**.

### Business Objective
Give BDA employees and contractors one controlled place to report an IT issue or service need.

### Actors
Maker: User. Approver: none (Admin processing is F04-003).

### User Journey
1. Who creates: User (employee or contractor with User role). Admin may also raise as a User function.
2. How they create: Raise ticket form → select ticket category from the dropdown → enter description → optional attachment → submit. Ticket is saved as Open and shown in the user’s list (F04-002).
3. How they edit: After submit, the User cannot edit the ticket in this phase.
4. How they send for approval: Submit/approval does not apply. Submit only opens the ticket for Admin.
5. How the approver sees pending items: There is no approver inbox on this feature. Admin sees Open tickets under F04-003 / Module 05.
6. How the approver decides: There is no approval decision on this feature.
7. How the applicant / maker sees history: After submit, the User sees the new Open ticket in their status list (F04-002).
8. How the approver / auditor sees history: Admin sees the submitted ticket in the all-tickets register (F04-003).

### Functional Capabilities
- Raise ticket using the ticket-category dropdown only
- Capture description and optional single attachment
- Set initial status Open with requester and date/time
- Refuse submit without category and description

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Raise ticket form | Medium |
| Ticket submit confirmation | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Submit ticket | Complex |
| Validate ticket | Medium |
| Store supporting attachment | Medium |

### Inputs
Ticket category (dropdown), description, optional file.

### Outputs
Open ticket attributed to the signed-in user; confirmation.

### Business Rules
- Ticket category must be a value Admin created in F02-001.
- Requester is the signed-in account.
- One optional supporting file.
- Initial status is Open. User cannot set status. Rejected is not used for tickets.

### Validations
- Ticket category mandatory and from the dropdown.
- Description mandatory.
- Attachment type/size within a simple office-file limit.

### Calculations
None.

### Workflow
Submit creates Open. Status changes are F04-003.

### Search Requirements
None on the raise form (list/search is F04-002).

### Documents
Optional single supporting attachment, embedded on the ticket.

### Reports
None.

### Notifications
None.

### Security
Signed-in User or Admin. Attachment visible to requester and Admin only.

### Integrations
None.

### Dependencies
F01-003; F02-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Dropdown list API is billed under F02-001.
- User list/detail is F04-002.

### Risks
Users may raise duplicate tickets for the same issue; duplicate detection is out of scope.

### Non Functional Requirements
Form usable by non-technical staff; submit attributable to the signed-in account.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Raise ticket form | UI | Medium | 6 |
| Ticket submit confirmation | UI | Simple | 2 |
| Submit ticket | API | Complex | 8 |
| Validate ticket | API | Medium | 6 |
| Store supporting attachment | API | Medium | 6 |
| Ticket records | DB | Medium | 4 |
| Raise ticket tests | Testing | Medium | 6 |
| Raise ticket implementation documentation | Documentation | Easy | 2 |

**Feature total: 40 hours**
