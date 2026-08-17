# F03-004 — 3(2) preparation, photograph and office location link

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-004 |
| **Feature Name** | 3(2) preparation, photograph and office location link |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
The Officer marks 3(2) prepared, confirms the unique property code (F02-003), links the office photograph and address/location, and saves. The asset is then eligible for valuer assignment. An asset without 3(2) prepared is not offered in the valuer assignment list unless the Authority defines an exception.

### Business Objective
Make 3(2) prepared the gate to valuer assignment, with code, office photograph and location linked.

### Actors
Office user.

### User Journey
1. Officer marks 3(2) prepared, confirms unique property code (F02-003), links office photograph and address/location, and saves.
2. Asset becomes eligible for valuer assignment (F04-001).
3. An asset without 3(2) prepared is not offered in the assignment list unless the Authority defines an exception.

### Functional Capabilities
- Mark 3(2) prepared
- Confirm unique property code and link office photograph and location
- Gate assignment eligibility on 3(2) prepared

### Inputs
3(2) prepared flag; property code confirmation; office photograph; address/location already bound.

### Outputs
Assignment-eligible asset; ineligible if 3(2) not prepared.

### Business Rules
- 3(2) prepared is the gate to assignment
- Exception only if the Authority defines it
- Office photograph is the office-side link, not the valuer’s minimum four GIS field photographs (F04-006)

### Validations
- Unique code present
- Location linked
- 3(2) flag explicit

### Calculations
None.

### Workflow
Complete office pack → mark 3(2) prepared → eligible for F04-001.

### Search Requirements
3(2) prepared yes/no; eligible for assignment.

### Documents
Office photograph on the asset.

### Reports
3(2) prepared vs pending list.

### Notifications
None.

### Security
Office Post marks 3(2); assignment list respects the gate.

### Integrations
Property code (F02-003) and location (F02-008) bind.

### Dependencies
F02-003; F02-008; F03-001; F04-001.

### Assumptions
- Authority states any exception to the 3(2) gate in writing.

### Risks
Marking 3(2) prepared without deeds uploaded still allows assignment unless the Authority adds that check.

### Non Functional Requirements
Gate is enforced on the assignment list, not only on the UI.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| 3(2) preparation and eligibility workspace | UI | Complex | 12 |
| 3(2) gate and eligibility flag | API | Complex | 8 |
| 3(2) and office photo link | Database | Easy | 2 |
| Code and location bind consume | Integration | Easy | 8 |
| 3(2) eligibility tests | Testing | Medium | 6 |
| 3(2) gate note | Documentation | Easy | 2 |
| **Total** | | | **38** |

### Estimation Assumptions
- Field GIS four-photo set is F04-006, not the office photograph.
