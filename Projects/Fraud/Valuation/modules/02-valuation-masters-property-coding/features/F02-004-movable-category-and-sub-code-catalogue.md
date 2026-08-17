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
1. Administrator maintains or loads the seeded eValueM tree (AC, PCP, EEG, FF, MTP, TXT, VEH, ANC and listed children, e.g. AC-SPL, PCP-DT, VEH-CR-SUV).
2. Officer or valuer classifying a movable (F06-001) picks from that tree only.
3. QR/sticker codes (F06-003) use the selected codes.

### Functional Capabilities
- Maintain category, sub-code, object code and detail code tree
- Require movable classification from the tree
- Seed Annexure-01 codes

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
|---|---|---|---:|
| eValueM code tree | UI | Complex | 12 |
| Tree CRUD and pick-list | API | Medium | 6 |
| Hierarchical movable codes | Database | Medium | 4 |
| Internal tree consume | Integration | Simple | 4 |
| eValueM catalogue tests | Testing | Medium | 6 |
| Movable code-tree note | Documentation | Easy | 2 |
| **Total** | | | **34** |

### Estimation Assumptions
- Sticker print dataset is F06-003; office IT inventory is out of scope.
