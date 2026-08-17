# F02-002 — Immovable asset category master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Immovable asset category master |
| **Module** | 02 — Valuation Masters, Property Coding & References |

### Description
An Administrator maintains categories Land, Property, Building, Lease Holding and Other. An Officer creating an asset must select a category from this list. Adding a category the Authority names makes it available on the next asset create, without a code change request for that list alone.

### Business Objective
Keep immovable category spelling consistent on 3(2) assets and later CA assessment.

### Actors
Administrator; Office user.

### User Journey
1. Administrator maintains Land, Property, Building, Lease Holding and Other (and Authority-named additions).
2. Officer creating an asset (F03-001/F03-002) must pick from this list.
3. A newly added category is available on the next asset create without a software change request for the list alone.

### Functional Capabilities
- Maintain immovable categories as in the FRS, extendable by the Authority
- Require category on asset create from this list only

### Inputs
Category name; active flag; Authority add request.

### Outputs
Category list consumed by asset create and CA assessment.

### Business Rules
- Asset create cannot type a free-text category
- Inactive categories are not offered on new assets

### Validations
- Name unique
- At least the FRS five exist unless the Authority retires one with reason

### Calculations
None.

### Workflow
Maintain list → asset create consumes current active list.

### Search Requirements
Category name, active.

### Documents
None.

### Reports
Immovable category list.

### Notifications
None.

### Security
Administrator maintains; Office users consume.

### Integrations
Internal consume by Module 03 asset create.

### Dependencies
None other than Module 01 access.

### Assumptions
- Authority names any extra categories in writing.

### Risks
Retiring a category still used on existing assets needs a mapping rule.

### Non Functional Requirements
List change does not require a code release for values alone.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Immovable category list maintenance | UI | Easy | 4 |
| Category lookup and save | API | Easy | 4 |
| Category list | Database | Simple | 1 |
| Internal category consume | Integration | Simple | 4 |
| Category master tests | Testing | Easy | 4 |
| Category list note | Documentation | Simple | 1 |
| **Total** | | | **18** |

### Estimation Assumptions
- Movable tree is F02-004, not this list.
