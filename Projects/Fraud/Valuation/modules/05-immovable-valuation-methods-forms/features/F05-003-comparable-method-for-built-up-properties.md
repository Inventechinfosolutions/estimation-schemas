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
1. Valuer records comparable sales for flats/shops/offices with built-up area, date of sale, plot area, FSI/FAR, land appurtenant, consideration, parties and register no.
2. Valuer applies adjustment factors (location, situation, area, floor difference, specifications, facilities, time-gap, lease/freehold, building area, floor disposition).
3. Fewer than the Authority’s minimum comparables requires a recorded reason. Generative AI shall not invent comparables.

### Functional Capabilities
- Comparable sales table for built-up properties
- Apply listed adjustment factors
- Require reason if below minimum comparables
- No generative comparable invention

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
|---|---|---|---:|
| Built-up comparables grid | UI | Complex | 12 |
| Comparable adjustments | API | Complex | 8 |
| Comparables store | Database | Medium | 4 |
| Internal form consume | Integration | Simple | 4 |
| Comparables tests | Testing | Complex | 8 |
| Comparables method guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Land-and-building comparables (min. 3) are F05-005.
