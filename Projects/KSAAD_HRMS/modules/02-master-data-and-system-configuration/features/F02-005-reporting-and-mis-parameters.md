# F02-005 — Reporting and MIS Parameters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-005 |
| **Feature Name** | Reporting and MIS Parameters |
| **Module** | 02 — Master Data & System Configuration |

### Description
Administrator sets default filters, export formats and alert thresholds used by Module 14.

### Business Objective
Standardise MIS defaults per office/role.

### Actors
Maker: MIS Administrator. Checker: MIS Checker.

### User Journey
1. Who creates: MIS Administrator.
2. How they create: Opens MIS parameters → New set for an office or Role, sets default period, export format, alert thresholds.
3. How they edit: Edit draft; submit to checker.
4. How they send for approval: Checker approval before defaults apply.
5. How the approver sees pending items: Checker MIS-parameter inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Parameter change history.
8. How the checker / auditor sees history: Same for checker.

### Functional Capabilities
- Authorised administrator creates and updates the MIS parameter set.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Mis parameter set register and search | Medium |
| Mis parameter set create / edit form | Complex |
| Mis parameter set change history | Medium |
| Mis parameter set maker–checker inbox | Medium |
| Mis parameter set approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create MIS parameter set | Medium |
| Update MIS parameter set | Medium |
| Search MIS parameter set register | Medium |
| Read MIS parameter set change history | Easy |
| Submit MIS parameter set change for checker | Complex |
| Approve or reject MIS parameter set change | Complex |

### Inputs
Office/Role scope, default period, export format, alert thresholds.

### Outputs
Current MIS parameter set record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Checker approval before defaults apply.

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
Poor unique-identity control on the MIS parameter set would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Mis parameter set register and search | UI | Medium | 6 |
| Mis parameter set create / edit form | UI | Complex | 12 |
| Mis parameter set change history | UI | Medium | 6 |
| Mis parameter set maker–checker inbox | UI | Medium | 6 |
| Mis parameter set approval panel | UI | Easy | 4 |
| Create MIS parameter set | API | Medium | 6 |
| Update MIS parameter set | API | Medium | 6 |
| Search MIS parameter set register | API | Medium | 6 |
| Read MIS parameter set change history | API | Easy | 4 |
| Submit MIS parameter set change for checker | API | Complex | 8 |
| Approve or reject MIS parameter set change | API | Complex | 8 |
| Mis parameter set record and change history | DB | Medium | 4 |
| Internal handoff of MIS parameter set to consuming modules | Integration | Simple | 4 |
| Reporting and MIS Parameters feature tests | Testing | Complex | 8 |
| Reporting and MIS Parameters implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
