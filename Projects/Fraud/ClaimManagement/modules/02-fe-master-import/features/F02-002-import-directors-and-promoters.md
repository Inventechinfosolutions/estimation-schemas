# F02-002 — Import Directors and Promoters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Import Directors and Promoters |
| **Module** | 02 — FE Master Import (from existing application) |

### Description
After FE details are imported, the Officer or Administrator imports Director and Promoter names and identifying particulars linked to that FE. An Officer later uses those names when running accused or colluder lists and related checks, without re-typing the FE people master.

### Business Objective
Reuse imported Director/Promoter names for categorisation and lists instead of a locally typed FE people master.

### Actors
Officer; Administrator.

### User Journey
1. Who creates: Officer
2. How they create: After FE details exist (F02-001), Officer or Administrator starts Directors and Promoters import for that FE.
3. How they edit: The system stores names and identifying particulars linked to the imported FE.
4. How they send for approval: Officer opens the Director/Promoter reference register and confirms the people against the FE. Trigger after FE details import → store references → consume in Modules 05 and 09.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Later, Officer uses those names in accused/colluder categorisation (F05-004) and lists (F09-003) without re-typing.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Import Director and Promoter particulars linked to an imported FE.
- Maintain a read-only people reference register per FE.
- Make names available to categorisation and operational lists.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Director/Promoter import review | Medium |
| Director/Promoter reference register | Medium |
| Import directors and promoters history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Directors/Promoters import operations | Very High |
| Update import directors and promoters | Medium |
| Search import directors and promoters | Medium |
| Read import directors and promoters history | Easy |

### Inputs
Imported FE, source Director/Promoter names and identifying particulars.

### Outputs
Read-only Director/Promoter references; import run result.

### Business Rules
- People master for FE directors/promoters is not re-keyed in this application.
- No local FE dossier screens for company officers beyond imported references.

### Validations
- Import requires a parent imported FE unique ID.
- Blank name rows are skipped or failed per import rules.

### Calculations
Import counts.

### Workflow
Trigger after FE details import → store references → consume in Modules 05 and 09.

### Search Requirements
FE, Director/Promoter name, identifying particular as supplied.

### Documents
None.

### Reports
Directors/Promoters import run log.

### Notifications
On-screen import result.

### Security
Authorised import Posts only. References used in lists remain subject to Module 01 visibility.

### Integrations
Existing FE Management application — Directors and Promoters import.

### Dependencies
F02-001.

### Assumptions
- Identifying particulars are those the existing application supplies; this SOW does not invent extra KYC for directors.

### Risks
- Stale director names would mis-fire colluder/accused lists until refresh (F02-004).

### Non Functional Requirements
Imported people references support type-ahead on later categorisation screens.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Director/Promoter import review | UI | Medium | 6 |
| Director/Promoter reference register | UI | Medium | 6 |
| Import directors and promoters history | UI | Medium | 6 |
| Directors/Promoters import operations | API | Very High | 16 |
| Update import directors and promoters | API | Medium | 6 |
| Search import directors and promoters | API | Medium | 6 |
| Read import directors and promoters history | API | Easy | 4 |
| People-reference persistence | DB | Medium | 4 |
| Existing FE application people import | Integration | Medium | 16 |
| Import Directors and Promoters feature tests | Testing | Complex | 8 |
| Import Directors and Promoters implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **81** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
