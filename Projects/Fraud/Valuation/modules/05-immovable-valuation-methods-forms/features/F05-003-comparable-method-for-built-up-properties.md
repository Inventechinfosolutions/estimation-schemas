# F05-003 — Comparable method for built-up properties

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-003 |
| **Feature Name** | Comparable method for built-up properties |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
The Valuer records comparable sales for flats/shops/offices (built-up area, date of sale, plot area, FSI/FAR, land appurtenant, consideration, parties, register no.) and applies adjustment factors (location, situation, area, floor difference, specifications, facilities, time-gap, lease/freehold, building area, floor disposition). Fewer than the Authority’s minimum comparables requires a recorded reason.

### Business Objective
Capture comparable sales and valuer-applied adjustments for built-up properties without inventing sales.

### Actors
Approved Valuer.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer records comparable sales for flats/shops/offices with built-up area, date of sale, plot area, FSI/FAR, land appurtenant, consideration, parties and register no.
3. How they edit: Valuer applies adjustment factors (location, situation, area, floor difference, specifications, facilities, time-gap, lease/freehold, building area, floor disposition).
4. How they send for approval: Fewer than the Authority’s minimum comparables requires a recorded reason. Generative AI shall not invent comparables. Add comparables → apply factors → reason if short → save working.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Comparable sales table for built-up properties
- Apply listed adjustment factors
- Require reason if below minimum comparables
- No generative comparable invention

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My comparable method for built-up properties list / queue | Medium |
| Built-up comparables grid | Complex |
| Comparable method for built-up properties history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Comparable adjustments | Complex |
| Update comparable method for built-up properties | Medium |
| Search comparable method for built-up properties | Medium |
| Read comparable method for built-up properties history | Easy |

### Inputs
Comparable rows; adjustment factors; reason if short.

### Outputs
Comparables working for the statutory form.

### Business Rules
- Comparables are entered or selected by the valuer, then human-verified
- No generative AI
- Minimum count with recorded reason if short

### Validations
- Each comparable has sale date and consideration
- Reason if count below minimum

### Calculations
Adjusted unit/consideration per FRS comparable method (valuer-applied factors, not AI).

### Workflow
Add comparables → apply factors → reason if short → save working.

### Search Requirements
Asset, comparable register no., sale date.

### Documents
Optional sale-instance copies embedded.

### Reports
Comparables working extract.

### Notifications
None.

### Security
Assigned valuer.

### Integrations
Internal working store for F05-007.

### Dependencies
F05-001; F05-004 (floor disposition may apply); F05-007.

### Assumptions
- Authority confirms minimum comparable count.

### Risks
Thin market; invented comparables if controls fail.

### Non Functional Requirements
Each override/factor is stored with the working.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My comparable method for built-up properties list / queue | UI | Medium | 6 |
| Built-up comparables grid | UI | Complex | 12 |
| Comparable method for built-up properties history | UI | Medium | 6 |
| Comparable adjustments | API | Complex | 8 |
| Update comparable method for built-up properties | API | Medium | 6 |
| Search comparable method for built-up properties | API | Medium | 6 |
| Read comparable method for built-up properties history | API | Easy | 4 |
| Comparable method for built-up properties persistence | DB | Medium | 4 |
| Internal form consume | Integration | Simple | 4 |
| Comparable method for built-up properties feature tests | Testing | Complex | 8 |
| Comparable method for built-up properties implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
