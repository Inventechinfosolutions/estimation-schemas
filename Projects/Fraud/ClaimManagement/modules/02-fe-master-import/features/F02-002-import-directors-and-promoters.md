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
1. After FE details exist (F02-001), Officer or Administrator starts Directors and Promoters import for that FE.
2. The system stores names and identifying particulars linked to the imported FE.
3. Officer opens the Director/Promoter reference register and confirms the people against the FE.
4. Later, Officer uses those names in accused/colluder categorisation (F05-004) and lists (F09-003) without re-typing.

### Functional Capabilities
- Import Director and Promoter particulars linked to an imported FE.
- Maintain a read-only people reference register per FE.
- Make names available to categorisation and operational lists.

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
| Directors/Promoters import operations | API | Very High | 16 |
| People-reference persistence | DB | Medium | 4 |
| Existing FE application people import | Integration | Medium | 16 |
| Directors/Promoters import tests | Testing | Complex | 8 |
| Directors/Promoters import notes | Documentation | Medium | 3 |
| **Total** | | | **59** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Integration Medium (mapping + retry) because FE identity import Complex effort is in F02-001.
