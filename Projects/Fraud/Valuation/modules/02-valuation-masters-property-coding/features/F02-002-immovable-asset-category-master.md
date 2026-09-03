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
1. Who creates: Administrator
2. How they create: Administrator maintains Land, Property, Building, Lease Holding and Other (and Authority-named additions).
3. How they edit: Officer creating an asset (F03-001/F03-002) must pick from this list.
4. How they send for approval: Maintain list → asset create consumes current active list.
5. How the approver sees pending items: No approval inbox unless maker–checker is later required. Auditor opens the register.
6. How the approver decides: No decision on this master beyond save; auditor reads history.
7. How the maker sees history: Administrator opens change history on the record (who changed what, when).
8. How the checker / auditor sees history: Auditor (and checker if used) open the same history.

### Functional Capabilities
- Maintain immovable categories as in the FRS, extendable by the Authority
- Require category on asset create from this list only

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Immovable category list maintenance | Easy |
| Immovable asset category master create/edit form | Medium |
| Immovable asset category master change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Category lookup and save | Easy |
| Update immovable asset category master | Medium |
| Search immovable asset category master register | Medium |
| Read immovable asset category master change history | Easy |

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
|---|---|---|---|
| Immovable category list maintenance | UI | Easy | 4 |
| Immovable asset category master create/edit form | UI | Medium | 6 |
| Immovable asset category master change history | UI | Medium | 6 |
| Category lookup and save | API | Easy | 4 |
| Update immovable asset category master | API | Medium | 6 |
| Search immovable asset category master register | API | Medium | 6 |
| Read immovable asset category master change history | API | Easy | 4 |
| Immovable asset category master identity persistence | DB | Medium | 4 |
| Internal category consume | Integration | Simple | 4 |
| Immovable asset category master feature tests | Testing | Easy | 4 |
| Immovable asset category master implementation documentation | Documentation | Simple | 1 |
| **Total** | | | **49** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
