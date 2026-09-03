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
1. Who creates: Officer
2. How they create: Officer selects parameters such as FE, scheme, status, depositor type or geography.
3. How they edit: Officer generates claimant, accused, colluder, address or vendor lists.
4. How they send for approval: Officer views or exports only lists allowed for their Post. Select parameters → generate → view/export if allowed.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Parameterised list generation.
- Claimant, accused, colluder, address and vendor lists.
- Post-based restriction on which lists can be viewed or exported.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| List parameters and generate | Complex |
| List export | Easy |
| Parameterised operational lists history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Parameterised list query operations | Complex |
| Update parameterised operational lists | Medium |
| Search parameterised operational lists | Medium |
| Read parameterised operational lists history | Easy |

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
| Parameterised operational lists history | UI | Medium | 6 |
| Parameterised list query operations | API | Complex | 8 |
| Update parameterised operational lists | API | Medium | 6 |
| Search parameterised operational lists | API | Medium | 6 |
| Read parameterised operational lists history | API | Easy | 4 |
| List query support | DB | Complex | 6 |
| Parameterised operational lists feature tests | Testing | Complex | 8 |
| Parameterised operational lists implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
