# F06-003 — Tagging sticker / label

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-003 |
| **Feature Name** | Tagging sticker / label |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
The user generates the tagging sticker/label dataset: category, name, serial number, condition. The user confirms the printed/attached tag matches the on-screen row. An item without a tag dataset cannot be marked inspection-complete.

### Business Objective
Produce a consistent QR/sticker dataset and require it before inspection-complete.

### Actors
Office user; Approved Valuer.

### User Journey
1. User generates sticker/label dataset: category, name, serial number, condition.
2. User confirms the printed/attached tag matches the on-screen row.
3. Item without a tag dataset cannot be marked inspection-complete.

### Functional Capabilities
- Generate sticker/label dataset from the coded row
- Confirm match to physical tag
- Block inspection-complete without tag dataset

### Inputs
Movable row; confirm-match action.

### Outputs
Sticker/label dataset; inspection-complete eligibility.

### Business Rules
- QR/sticker codes stay consistent with F02-004 / F06-001
- No tag dataset ⇒ not inspection-complete

### Validations
- Category, name, serial, condition present

### Calculations
None.

### Workflow
Generate dataset → confirm match → allow inspection-complete.

### Search Requirements
Serial, tagged yes/no.

### Documents
Sticker/label (print dataset).

### Reports
Untagged movables.

### Notifications
In-app block on inspection-complete.

### Security
Same as movable access.

### Integrations
Internal print-dataset consume (not a warehouse WMS).

### Dependencies
F06-001; F06-002.

### Assumptions
- Physical printer hardware is Authority-supplied; this feature is the dataset and confirmation.

### Risks
Physical tag mismatch if confirmation is skipped.

### Non Functional Requirements
Dataset stored with the row.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Sticker/label preview | UI | Medium | 6 |
| Label dataset generate | API | Easy | 4 |
| Label dataset | Database | Easy | 2 |
| Internal print-dataset consume | Integration | Simple | 4 |
| Sticker tests | Testing | Easy | 4 |
| Sticker/label note | Documentation | Easy | 2 |
| **Total** | | | **22** |

### Estimation Assumptions
- Not office IT asset tagging.
