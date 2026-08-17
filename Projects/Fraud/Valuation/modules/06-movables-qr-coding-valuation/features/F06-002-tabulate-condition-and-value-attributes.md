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
1. On the movable item the user completes group serial, description (material and colour in order), make/brand, rating, condition and appreciating/depreciating.
2. Later V-6/V-7/V-8 read these fields rather than asking them again.

### Functional Capabilities
- Tabulate serials, description, make/brand, rating, condition, appreciating/depreciating
- Reuse fields on V-6/V-7/V-8

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
|---|---|---|---:|
| Condition and value tabulation | UI | Medium | 6 |
| Tabulation save | API | Medium | 6 |
| Tabulation fields | Database | Easy | 2 |
| Internal form consume | Integration | Simple | 4 |
| Tabulation tests | Testing | Easy | 4 |
| Tabulation note | Documentation | Easy | 2 |
| **Total** | | | **24** |

### Estimation Assumptions
- Jewellery purity methods are F06-006, not this generic tabulation.
