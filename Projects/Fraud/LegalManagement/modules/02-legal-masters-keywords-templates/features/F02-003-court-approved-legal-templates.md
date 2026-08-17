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
1. User opens the Legal Template Register.
2. Uploads or replaces a template of a listed type with court-approved font and spacing.
3. Marks it available for drafting (F02-004).
4. Unavailable templates cannot be selected on Generate Draft.

### Functional Capabilities
- Legal Template Register by type (5(2), notice, 7(1), 8(1), SOB, PWR, Caveat, IA, SLP, letter, freezing order, warrant)
- Template Upload/Maintain screen (font and spacing metadata)
- Available / withdrawn lifecycle
- No generative-AI template authoring
- Market-intelligence investigation process remains out of scope except these notice/form types

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
Type required; file required; available flag only if font/spacing recorded; withdrawn templates hidden from Generate Draft.

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
SPLOCA supplies court-approved font and spacing; vendor does not invent court form layout.

### Risks
Wrong font/spacing causes court rejection; unapproved type slips into production.

### Non Functional Requirements
Template files stored with backup policy; version retrieve for audit.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Legal Template Register | UI | Medium | 6 |
| Template Upload/Maintain screen (type, font, spacing) | UI | Complex | 12 |
| Template lifecycle operations | API | Complex | 8 |
| Template store and font/spacing metadata | Database | Medium | 4 |
| Document store for template files | Integration | Easy | 8 |
| Template administration tests | Testing | Complex | 8 |
| Court-approved template guide | Documentation | Medium | 3 |
| **Total** | | | **49** |

### Estimation Assumptions
- Draft merge and human verify are F02-004.
- No generative AI hours.
