# F01-001 — Employee and Contractor Accounts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Employee and Contractor Accounts |
| **Module** | 01 — User Account and Access Management |

### Description
Admin creates and maintains every BDA login as either an **employee** or a **contractor**. Employee number is mandatory and unique for employees and is not captured for contractors. Each account is assigned exactly one role: User or Admin.

### Business Objective
All application access starts from an Admin-created account that distinguishes employees from contractors without a person or post directory.

### Actors
Maker: Admin. Applicant: none. Approver: none.

### User Journey
1. Who creates: Admin.
2. How they create: User account register → New account → choose Employee or Contractor → enter name and contact → for Employee enter employee number → assign User or Admin role → Save. Credentials are set under F01-002.
3. How they edit: Admin opens the account from the register and updates profile fields. Employee number remains required for employees; contractor records must not hold an employee number.
4. How they send for approval: Submit/approval does not apply. Saving the account is the complete action.
5. How the approver sees pending items: There is no approver inbox.
6. How the approver decides: There is no approval decision on this feature.
7. How the maker sees history: Admin opens account change history (who created or changed the profile, when).
8. How the approver / auditor sees history: Admin uses the same account change history. There is no separate auditor role.

### Functional Capabilities
- Create employee account with mandatory unique employee number
- Create contractor account without employee number
- Edit profile and role
- Search and list accounts by name, user type, role, and employee number

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| User account register | Medium |
| Employee and contractor account form | Medium |
| Account change history | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create user account | Medium |
| Update user account | Medium |
| Search user accounts | Medium |
| Read account history | Easy |
| Validate employee number uniqueness | Medium |

### Inputs
User type (Employee / Contractor), name, contact as captured, employee number (employees only), role (User / Admin).

### Outputs
Persisted account records; searchable register; change history visible to Admin.

### Business Rules
- Employee number is mandatory and unique among employees.
- Contractor accounts must not store an employee number.
- One role per account.
- Accounts are not deleted when access is withdrawn (disable is F01-004).

### Validations
- Employee number present and unique when type is Employee.
- Employee number absent when type is Contractor.
- Name and role mandatory.

### Calculations
None.

### Workflow
No approval. Admin save is final.

### Search Requirements
Search by name, user type, role, employee number (employees), and active/disabled status.

### Documents
None.

### Reports
None on this feature.

### Notifications
None. Email/SMS are out of scope.

### Security
Admin only for create, edit, and history. User role cannot open the register.

### Integrations
None. Employee number is not validated against HR.

### Dependencies
None.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Username and password set/reset are F01-002, not this feature.
- Enable/disable is F01-004.

### Risks
If BDA later requires live HR check of employee number, this feature and an integration would need extra hours.

### Non Functional Requirements
Usable by BDA IT Admin on the internal web application; create/change actions attributable to the Admin account.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| User account register | UI | Medium | 6 |
| Employee and contractor account form | UI | Medium | 6 |
| Account change history | UI | Easy | 4 |
| Create user account | API | Medium | 6 |
| Update user account | API | Medium | 6 |
| Search user accounts | API | Medium | 6 |
| Read account history | API | Easy | 4 |
| Validate employee number uniqueness | API | Medium | 6 |
| User account records | DB | Medium | 4 |
| Employee and contractor account tests | Testing | Complex | 8 |
| Employee and contractor accounts implementation documentation | Documentation | Easy | 2 |

**Feature total: 58 hours**
