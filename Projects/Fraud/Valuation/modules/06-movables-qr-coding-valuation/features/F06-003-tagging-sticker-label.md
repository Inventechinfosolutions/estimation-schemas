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
1. Who creates: Office user
2. How they create: User generates sticker/label dataset: category, name, serial number, condition.
3. How they edit: User confirms the printed/attached tag matches the on-screen row.
4. How they send for approval: Item without a tag dataset cannot be marked inspection-complete. Generate dataset → confirm match → allow inspection-complete.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Generate sticker/label dataset from the coded row
- Confirm match to physical tag
- Block inspection-complete without tag dataset

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My tagging sticker / label list / queue | Medium |
| Sticker/label preview | Medium |
| Tagging sticker / label history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Label dataset generate | Easy |
| Update tagging sticker / label | Medium |
| Search tagging sticker / label | Medium |
| Read tagging sticker / label history | Easy |

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
|---|---|---|---|
| My tagging sticker / label list / queue | UI | Medium | 6 |
| Sticker/label preview | UI | Medium | 6 |
| Tagging sticker / label history | UI | Medium | 6 |
| Label dataset generate | API | Easy | 4 |
| Update tagging sticker / label | API | Medium | 6 |
| Search tagging sticker / label | API | Medium | 6 |
| Read tagging sticker / label history | API | Easy | 4 |
| Tagging sticker / label persistence | DB | Medium | 4 |
| Internal print-dataset consume | Integration | Simple | 4 |
| Tagging sticker / label feature tests | Testing | Easy | 4 |
| Tagging sticker / label implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
