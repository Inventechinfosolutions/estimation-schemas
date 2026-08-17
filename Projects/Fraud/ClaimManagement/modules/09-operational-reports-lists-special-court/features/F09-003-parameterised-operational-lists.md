# F09-003 — Parameterised operational lists

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-003 |
| **Feature Name** | Parameterised operational lists |
| **Module** | 09 — Operational Reports, Lists & Special Court Outputs |

### Description
The Officer selects parameters (FE, scheme, status, depositor type, geography or similar) and generates claimant, accused, colluder, address or vendor lists. The Officer views or exports only lists allowed for their Post.

### Business Objective
Generate parameterised operational lists restricted by Module 01 visibility, without legal-draft lists from the Legal SOW.

### Actors
Officer; other authorised Posts as permitted.

### User Journey
1. Officer selects parameters such as FE, scheme, status, depositor type or geography.
2. Officer generates claimant, accused, colluder, address or vendor lists.
3. Officer views or exports only lists allowed for their Post.

### Functional Capabilities
- Parameterised list generation.
- Claimant, accused, colluder, address and vendor lists.
- Post-based restriction on which lists can be viewed or exported.

### Inputs
List type, parameters (FE, scheme, status, depositor type, geography).

### Outputs
On-screen list and authorised export.

### Business Rules
- Menu access and list slices follow Module 01.
- Vakalat/Caveat and similar legal drafts belong to Legal Management SOW.
- Accused/colluder lists use stored categories from F05-004.

### Validations
- Parameters required per list type.
- Unauthorised list types are refused.

### Calculations
None beyond filtering/counting.

### Workflow
Select parameters → generate → view/export if allowed.

### Search Requirements
The lists themselves are the search/filter result.

### Documents
None as legal drafts.

### Reports
The operational lists.

### Notifications
None.

### Security
Need-to-know; another Post does not see restricted slices. Export is audited.

### Integrations
None.

### Dependencies
F05-004 categories; F02 imported FE/scheme; F01 visibility; Modules 04–08 data.

### Assumptions
- Vendor list sources are operational records the Authority designates (not a separate procurement module).

### Risks
- Exporting accused lists beyond authorised Posts would leak investigation-adjacent data.

### Non Functional Requirements
Practical filters. Structured lists, not PDF-only publishing.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| List parameters and generate | UI | Complex | 12 |
| List export | UI | Easy | 4 |
| Parameterised list query operations | API | Complex | 8 |
| List query support | DB | Complex | 6 |
| Operational list tests | Testing | Complex | 8 |
| Operational lists guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Dashboard hours are F09-004; structured operational reports are F09-006.
