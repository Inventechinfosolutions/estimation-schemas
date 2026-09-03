# F06-002 — Tabulate condition and value attributes

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Tabulate condition and value attributes |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
On that item the user completes serials, description (material and colour in order), make/brand if available, rating (Exclusive / High / Average / Low), condition (New / Unused / Working / Damaged with details / Scrap / Obsolete) and whether the item is appreciating or depreciating. A later Form V-6/V-7/V-8 reads these fields rather than asking them again.

### Business Objective
Tabulate condition and value attributes once so statutory movable forms reuse them.

### Actors
Office user; Approved Valuer.

### User Journey
1. Who creates: Office user
2. How they create: On the movable item the user completes group serial, description (material and colour in order), make/brand, rating, condition and appreciating/depreciating.
3. How they edit: Later V-6/V-7/V-8 read these fields rather than asking them again.
4. How they send for approval: Later V-6/V-7/V-8 read these fields rather than asking them again. Open item → tabulate → save → forms consume.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Tabulate serials, description, make/brand, rating, condition, appreciating/depreciating
- Reuse fields on V-6/V-7/V-8

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My tabulate condition and value attributes list / queue | Medium |
| Condition and value tabulation | Medium |
| Tabulate condition and value attributes history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Tabulation save | Medium |
| Update tabulate condition and value attributes | Medium |
| Search tabulate condition and value attributes | Medium |
| Read tabulate condition and value attributes history | Easy |

### Inputs
Group serial; item name; description (material & colour); make/brand; rating; condition (with damage details when Damaged); appreciating/depreciating.

### Outputs
Completed tabulation on the item.

### Business Rules
- Condition grades from F02-006 where configured
- Forms read these fields

### Validations
- Rating and condition from lists
- Damage details when condition is Damaged

### Calculations
None.

### Workflow
Open item → tabulate → save → forms consume.

### Search Requirements
Condition, rating, serial.

### Documents
None.

### Reports
Movable tabulation extract.

### Notifications
None.

### Security
Same as parent movable access.

### Integrations
Internal form consume.

### Dependencies
F06-001; F02-006; F06-005–F06-007.

### Assumptions
- Rating and condition lists match Annexure-01.

### Risks
Re-asking the same fields on V-6 would duplicate and diverge.

### Non Functional Requirements
Single store for tabulation.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My tabulate condition and value attributes list / queue | UI | Medium | 6 |
| Condition and value tabulation | UI | Medium | 6 |
| Tabulate condition and value attributes history | UI | Medium | 6 |
| Tabulation save | API | Medium | 6 |
| Update tabulate condition and value attributes | API | Medium | 6 |
| Search tabulate condition and value attributes | API | Medium | 6 |
| Read tabulate condition and value attributes history | API | Easy | 4 |
| Tabulate condition and value attributes persistence | DB | Medium | 4 |
| Internal form consume | Integration | Simple | 4 |
| Tabulate condition and value attributes feature tests | Testing | Easy | 4 |
| Tabulate condition and value attributes implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **54** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
