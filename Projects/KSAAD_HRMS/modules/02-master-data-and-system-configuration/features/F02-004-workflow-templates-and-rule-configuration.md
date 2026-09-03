# F02-004 — Workflow Templates and Rule Configuration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-004 |
| **Feature Name** | Workflow Templates and Rule Configuration |
| **Module** | 02 — Master Data & System Configuration |

### Description
Administrator defines which supervising Post (or Role) approves which transaction type, including SLA hours.

### Business Objective
Make approval routing configurable without changing each module.

### Actors
Maker: Workflow Administrator. Checker: Workflow Checker.

### User Journey
1. Who creates: Workflow Administrator.
2. How they create: Opens Workflow templates → New, selects transaction type (leave, TA/DA, indent, audit report), default route (supervising Post), optional amount threshold, SLA hours.
3. How they edit: Version the template; in-flight transactions keep the version they were submitted on.
4. How they send for approval: Submit new version to checker before it applies to new submissions.
5. How the approver sees pending items: Checker template inbox.
6. How the approver decides: Approve or reject the new version.
7. How the maker sees history: Template version history.
8. How the checker / auditor sees history: Same for checker.

### Functional Capabilities
- Authorised administrator creates and updates the workflow template.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Workflow template register and search | Medium |
| Workflow template create / edit form | Very High |
| Workflow template change history | Medium |
| Workflow template maker–checker inbox | Medium |
| Workflow template approval panel | Easy |
| Template version comparison | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create workflow template | Medium |
| Update workflow template | Medium |
| Search workflow template register | Medium |
| Read workflow template change history | Easy |
| Submit workflow template change for checker | Complex |
| Approve or reject workflow template change | Complex |

### Inputs
Transaction type, route rule, threshold, SLA hours, version, status.

### Outputs
Current workflow template record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.
- Existing submitted records do not silently change route when a new version is approved.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit new version to checker before it applies to new submissions.

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
Poor unique-identity control on the workflow template would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Workflow template register and search | UI | Medium | 6 |
| Workflow template create / edit form | UI | Very High | 16 |
| Workflow template change history | UI | Medium | 6 |
| Workflow template maker–checker inbox | UI | Medium | 6 |
| Workflow template approval panel | UI | Easy | 4 |
| Template version comparison | UI | Medium | 6 |
| Create workflow template | API | Medium | 6 |
| Update workflow template | API | Medium | 6 |
| Search workflow template register | API | Medium | 6 |
| Read workflow template change history | API | Easy | 4 |
| Submit workflow template change for checker | API | Complex | 8 |
| Approve or reject workflow template change | API | Complex | 8 |
| Workflow template record and change history | DB | Medium | 4 |
| Internal handoff of workflow template to consuming modules | Integration | Simple | 4 |
| Workflow Templates and Rule Configuration feature tests | Testing | Complex | 8 |
| Workflow Templates and Rule Configuration implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **101** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
