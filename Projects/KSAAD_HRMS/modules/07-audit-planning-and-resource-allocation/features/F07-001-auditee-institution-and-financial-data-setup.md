# F07-001 — Auditee Institution and Financial Data Setup

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | Auditee Institution and Financial Data Setup |
| **Module** | 07 — Audit Planning & Resource Allocation |

### Description
Audit planning officer creates/updates auditee institution master and financial-year data used in planning.

### Business Objective
System of record for who is audited.

### Actors
Maker: Audit Planning Officer. Checker: Planning Supervisor / Audit Superintendent.

### User Journey
1. Who creates: Audit Planning Officer.
2. How they create: Opens Auditee register → New: code, name, type, office of jurisdiction, contacts, Save draft.
3. How they edit: Draft editable. Approved master changes are checked. Financial-year snapshots (turnover etc.) added as child records, not by overwriting last year.
4. How they send for approval: Submit institution or FY data to checker.
5. How the approver sees pending items: Checker auditee inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Institution and FY data history.
8. How the checker / auditor sees history: Same for checker.

### Functional Capabilities
- Authorised administrator creates and updates the auditee institution.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Auditee institution register and search | Medium |
| Auditee institution create / edit form | Complex |
| Auditee institution change history | Medium |
| Auditee institution maker–checker inbox | Medium |
| Auditee institution approval panel | Easy |
| Financial year data form | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create auditee institution | Medium |
| Update auditee institution | Medium |
| Search auditee institution register | Medium |
| Read auditee institution change history | Easy |
| Submit auditee institution change for checker | Complex |
| Approve or reject auditee institution change | Complex |
| Save FY financial snapshot | Medium |

### Inputs
Code, name, type, jurisdiction office, FY financial fields.

### Outputs
Current auditee institution record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Code unique.
- Jurisdiction office mandatory.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit institution or FY data to checker.

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
Poor unique-identity control on the auditee institution would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Auditee institution register and search | UI | Medium | 6 |
| Auditee institution create / edit form | UI | Complex | 12 |
| Auditee institution change history | UI | Medium | 6 |
| Auditee institution maker–checker inbox | UI | Medium | 6 |
| Auditee institution approval panel | UI | Easy | 4 |
| Financial year data form | UI | Complex | 12 |
| Create auditee institution | API | Medium | 6 |
| Update auditee institution | API | Medium | 6 |
| Search auditee institution register | API | Medium | 6 |
| Read auditee institution change history | API | Easy | 4 |
| Submit auditee institution change for checker | API | Complex | 8 |
| Approve or reject auditee institution change | API | Complex | 8 |
| Save FY financial snapshot | API | Medium | 6 |
| Auditee institution record and change history | DB | Medium | 4 |
| Internal handoff of auditee institution to consuming modules | Integration | Simple | 4 |
| Auditee Institution and Financial Data Setup feature tests | Testing | Complex | 8 |
| Auditee Institution and Financial Data Setup implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **109** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
