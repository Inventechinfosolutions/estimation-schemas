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
1. Who creates: Office user
2. How they create: Officer marks 3(2) prepared, confirms unique property code (F02-003), links office photograph and address/location, and saves.
3. How they edit: Asset becomes eligible for valuer assignment (F04-001).
4. How they send for approval: An asset without 3(2) prepared is not offered in the assignment list unless the Authority defines an exception. Complete office pack → mark 3(2) prepared → eligible for F04-001.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Mark 3(2) prepared
- Confirm unique property code and link office photograph and location
- Gate assignment eligibility on 3(2) prepared

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My 3 preparation, photograph and office location link list / queue | Medium |
| 3(2) preparation and eligibility workspace | Complex |
| 3 preparation, photograph and office location link history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| 3(2) gate and eligibility flag | Complex |
| Update 3 preparation, photograph and office location link | Medium |
| Search 3 preparation, photograph and office location link | Medium |
| Read 3 preparation, photograph and office location link history | Easy |

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
|---|---|---|---|
| My 3 preparation, photograph and office location link list / queue | UI | Medium | 6 |
| 3(2) preparation and eligibility workspace | UI | Complex | 12 |
| 3 preparation, photograph and office location link history | UI | Medium | 6 |
| 3(2) gate and eligibility flag | API | Complex | 8 |
| Update 3 preparation, photograph and office location link | API | Medium | 6 |
| Search 3 preparation, photograph and office location link | API | Medium | 6 |
| Read 3 preparation, photograph and office location link history | API | Easy | 4 |
| 3 preparation, photograph and office location link persistence | DB | Medium | 4 |
| Code and location bind consume | Integration | Easy | 8 |
| 3(2) preparation, photograph and office location link feature tests | Testing | Medium | 6 |
| 3(2) preparation, photograph and office location link implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **68** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
