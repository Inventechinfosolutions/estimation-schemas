# F02-003 — Court-approved legal templates

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-003 |
| **Feature Name** | Court-approved legal templates |
| **Module** | 02 — Legal Masters, Keywords & Templates |

### Description
An authorised user uploads or maintains a template (5(2), notice as per rules, 7(1), 8(1), SOB, PWR, Caveat, IA, SLP, letter, freezing order, warrant) with the court-approved font and spacing, and marks it available for drafting.

### Business Objective
Hold stored court-approved templates so drafts are produced from Authority-approved forms, not free composition or generative AI.

### Actors
Administrator; authorised Legal Cell.

### User Journey
1. Who creates: Administrator
2. How they create: User opens the Legal Template Register.
3. How they edit: Uploads or replaces a template of a listed type with court-approved font and spacing.
4. How they send for approval: Marks it available for drafting (F02-004). Upload/maintain → record font/spacing → mark available → consume in F02-004.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record. Unavailable templates cannot be selected on Generate Draft.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Legal Template Register by type (5(2), notice, 7(1), 8(1), SOB, PWR, Caveat, IA, SLP, letter, freezing order, warrant)
- Template Upload/Maintain screen (font and spacing metadata)
- Available / withdrawn lifecycle
- No generative-AI template authoring
- Market-intelligence investigation process remains out of scope except these notice/form types

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Legal Template Register | Medium |
| Template Upload/Maintain screen (type, font, spacing) | Complex |
| Court-approved legal templates history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Template lifecycle operations | Complex |
| Update court-approved legal templates | Medium |
| Search court-approved legal templates | Medium |
| Read court-approved legal templates history | Easy |

### Inputs
Template type, file, court font/spacing notes, version, available flag, optional description.

### Outputs
Stored template version; availability flag for Generate Draft.

### Business Rules
- Listed types only unless SPLOCA adds a type via central masters.
- Font and spacing must match court-approved values supplied by SPLOCA.
- Human verification before issue is enforced at F02-004, not skipped here.
- Claim settlement notices that belong to the Claim SOW are not maintained here except where they are the listed legal template types.
- IP of stored templates and the application remains with SPLOCA.

### Validations
- Type required; file required; available flag only if font/spacing recorded; withdrawn templates hidden from Generate Draft.

### Calculations
None.

### Workflow
Upload/maintain → record font/spacing → mark available → consume in F02-004.

### Search Requirements
Template type, name, version, available status.

### Documents
Template files (court forms).

### Reports
Template inventory with version and availability.

### Notifications
None required.

### Security
Upload restricted; version history retained; no public website publish.

### Integrations
Document store for template files (Easy).

### Dependencies
F01-001; F02-004 generates drafts; F02-005 may hold type list.

### Assumptions
- SPLOCA supplies court-approved font and spacing; vendor does not invent court form layout.

### Risks
Wrong font/spacing causes court rejection; unapproved type slips into production.

### Non Functional Requirements
Template files stored with backup policy; version retrieve for audit.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Legal Template Register | UI | Medium | 6 |
| Template Upload/Maintain screen (type, font, spacing) | UI | Complex | 12 |
| Court-approved legal templates history | UI | Medium | 6 |
| Template lifecycle operations | API | Complex | 8 |
| Update court-approved legal templates | API | Medium | 6 |
| Search court-approved legal templates | API | Medium | 6 |
| Read court-approved legal templates history | API | Easy | 4 |
| Court-approved legal templates persistence | DB | Medium | 4 |
| Document store for template files | Integration | Easy | 8 |
| Court-approved legal templates feature tests | Testing | Complex | 8 |
| Court-approved legal templates implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
