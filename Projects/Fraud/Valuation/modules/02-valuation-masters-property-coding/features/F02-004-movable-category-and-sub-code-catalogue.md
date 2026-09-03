# F02-004 — Movable category and sub-code catalogue

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-004 |
| **Feature Name** | Movable category and sub-code catalogue |
| **Module** | 02 — Valuation Masters, Property Coding & References |

### Description
An Administrator (or seeded catalogue) maintains the eValueM tree (for example AC-SPL, PCP-DT, VEH-CR-SUV). An Officer or valuer classifying a movable must pick from that tree so QR/sticker codes stay consistent across seizures.

### Business Objective
Keep movable QR/sticker codes consistent using the Annexure-01 category/sub-code/object/detail tree.

### Actors
Administrator; Office user; Approved Valuer.

### User Journey
1. Who creates: Administrator
2. How they create: Administrator maintains or loads the seeded eValueM tree (AC, PCP, EEG, FF, MTP, TXT, VEH, ANC and listed children, e.g. AC-SPL, PCP-DT, VEH-CR-SUV).
3. How they edit: Officer or valuer classifying a movable (F06-001) picks from that tree only.
4. How they send for approval: Maintain tree → F06-001 pick → sticker/QR uses same codes.
5. How the approver sees pending items: No approval inbox unless maker–checker is later required. Auditor opens the register.
6. How the approver decides: No decision on this master beyond save; auditor reads history.
7. How the maker sees history: Administrator opens change history on the record (who changed what, when).
8. How the checker / auditor sees history: Auditor (and checker if used) open the same history.

### Functional Capabilities
- Maintain category, sub-code, object code and detail code tree
- Require movable classification from the tree
- Seed Annexure-01 codes

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| eValueM code tree | Complex |
| Movable category and sub-code catalogue create/edit form | Medium |
| Movable category and sub-code catalogue change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Tree CRUD and pick-list | Medium |
| Update movable category and sub-code catalogue | Medium |
| Search movable category and sub-code catalogue register | Medium |
| Read movable category and sub-code catalogue change history | Easy |

### Inputs
Tree node (category/sub/object/detail); active flag.

### Outputs
Selectable eValueM tree; codes on movable rows.

### Business Rules
- Free-text codes are not allowed for classification
- Inactive nodes are not offered on new items

### Validations
- Parent-child consistency
- Code unique within parent

### Calculations
None.

### Workflow
Maintain tree → F06-001 pick → sticker/QR uses same codes.

### Search Requirements
Code, description, parent, active.

### Documents
None.

### Reports
eValueM code catalogue export.

### Notifications
None.

### Security
Administrator maintains tree; classifiers consume.

### Integrations
Internal consume by Module 06.

### Dependencies
Module 01 access.

### Assumptions
- Annexure-01 tree is seeded; Authority confirms additions.

### Risks
Incomplete children force incorrect parent-only tagging.

### Non Functional Requirements
Tree selectable on web; Android consumes the same catalogue (F09-004).

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| eValueM code tree | UI | Complex | 12 |
| Movable category and sub-code catalogue create/edit form | UI | Medium | 6 |
| Movable category and sub-code catalogue change history | UI | Medium | 6 |
| Tree CRUD and pick-list | API | Medium | 6 |
| Update movable category and sub-code catalogue | API | Medium | 6 |
| Search movable category and sub-code catalogue register | API | Medium | 6 |
| Read movable category and sub-code catalogue change history | API | Easy | 4 |
| Movable category and sub-code catalogue identity persistence | DB | Medium | 4 |
| Internal tree consume | Integration | Simple | 4 |
| Movable category and sub-code catalogue feature tests | Testing | Medium | 6 |
| Movable category and sub-code catalogue implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
