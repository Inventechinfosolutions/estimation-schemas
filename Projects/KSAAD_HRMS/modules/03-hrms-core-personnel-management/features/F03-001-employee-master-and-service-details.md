# F03-001 — Employee Master and Service Details

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Employee Master and Service Details |
| **Module** | 03 — HRMS Core Personnel Management |

### Description
HR Establishment Officer maintains service particulars on the Person (joining date, cadre, office of posting as HR data). This is not a second login identity.

### Business Objective
Hold HR service data against the same Person used for access.

### Actors
Maker: HR Establishment Officer. Checker: HR Checker / Establishment supervisor.

### User Journey
1. Who creates: HR Establishment Officer.
2. How they create: Officer opens Employee register, searches the Person (F01-001). If none, they must request Person create first. Then opens Service details and enters joining date, cadre, GPF/PRAN, current office (HR view).
3. How they edit: Draft service updates can be edited. Approved fields (joining date) change only via checked amendment.
4. How they send for approval: Submit service-data changes to HR Checker.
5. How the approver sees pending items: HR Checker inbox of pending service amendments.
6. How the approver decides: Approve or reject with remarks.
7. How the maker sees history: Officer opens the Person's service history tab.
8. How the checker / auditor sees history: Checker/auditor open the same tab.

### Functional Capabilities
- Authorised administrator creates and updates the employee service record.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Employee service record register and search | Medium |
| Employee service record create / edit form | Complex |
| Employee service record change history | Medium |
| Employee service record maker–checker inbox | Medium |
| Employee service record approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create employee service record | Medium |
| Update employee service record | Medium |
| Search employee service record register | Medium |
| Read employee service record change history | Easy |
| Submit employee service record change for checker | Complex |
| Approve or reject employee service record change | Complex |

### Inputs
Person, joining date, cadre, GPF/PRAN, HR office, remarks.

### Outputs
Current employee service record record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.
- Does not create a login. Login identity remains Person + Post mapping.
- Post occupancy remains F01-003; this screen stores HR service attributes.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Person must already exist.
- Joining date mandatory.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit service-data changes to HR Checker.

### Search Requirements
Search by identifier, name, office, status and effective date.

### Documents
None required unless the administrator attaches a supporting office order.

### Reports
Register export for administrators and auditors.

### Notifications
Checker is notified when a change is submitted. Maker is notified on approve or reject.

### Security
Need-to-know. Only authorised Posts may create, edit or approve. History is read-only for auditors.

### Integrations
Consumed by later modules as the system of record for this master.

### Dependencies
Module 01 access. Downstream modules consume this master; they do not recreate it.

### Assumptions
- Hours use Estimation Master values only, at capability grain (not one billed row per screen).
- Named screens in the journey are not billed one-for-one; Section 2 uses capability artefacts.

### Risks
Poor unique-identity control on the employee service record would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Employee service record register and search | UI | Medium | 6 |
| Employee service record create / edit form | UI | Complex | 12 |
| Employee service record change history | UI | Medium | 6 |
| Employee service record maker–checker inbox | UI | Medium | 6 |
| Employee service record approval panel | UI | Easy | 4 |
| Create employee service record | API | Medium | 6 |
| Update employee service record | API | Medium | 6 |
| Search employee service record register | API | Medium | 6 |
| Read employee service record change history | API | Easy | 4 |
| Submit employee service record change for checker | API | Complex | 8 |
| Approve or reject employee service record change | API | Complex | 8 |
| Employee service record record and change history | DB | Medium | 4 |
| Internal handoff of employee service record to consuming modules | Integration | Simple | 4 |
| Employee Master and Service Details feature tests | Testing | Complex | 8 |
| Employee Master and Service Details implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
