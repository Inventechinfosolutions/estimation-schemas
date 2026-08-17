# F04-003 — View sale deeds and court order

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | View sale deeds and court order |
| **Module** | 04 — Valuer Assignment & GIS Field Capture (Data Capturing – I) |

### Description
On the selected asset, the Valuer clicks View on sale deeds or court order and sees the files the office uploaded (F03-003). If no file was uploaded, View states that and the valuer records the gap in remarks rather than inventing a document.

### Business Objective
Let the assigned valuer open the same court order and sale deeds the office stored.

### Actors
Approved Valuer.

### User Journey
1. On the selected asset the Valuer clicks View on sale deeds or court order.
2. The files the office uploaded (F03-003) open.
3. If no file was uploaded, View states that; the valuer records the gap in remarks (F04-007) rather than inventing a document.

### Functional Capabilities
- View office-uploaded sale deeds and court order
- State clearly when no file was uploaded
- Respect need-to-know (F01-003)

### Inputs
View action on deed or court order.

### Outputs
Opened file or explicit missing-file state.

### Business Rules
- Valuer does not upload a substitute court order/deed as if it were the office original
- Generative AI shall not invent a document

### Validations
- Assignment present
- ACL allows view

### Calculations
None.

### Workflow
Click View → ACL → open file or missing state.

### Search Requirements
None beyond the selected asset.

### Documents
Sale deeds; court order (view).

### Reports
None.

### Notifications
None.

### Security
Assignment + document rights; access logged in F01-003.

### Integrations
Internal file open from F03-003 store.

### Dependencies
F03-003; F01-003; F04-002.

### Assumptions
- Viewer supports the office-uploaded formats SPLOCA uses (PDF/image).

### Risks
Missing files delay inspection; valuer must not fabricate.

### Non Functional Requirements
View does not grant office replace rights.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Deed and court-order viewer | UI | Medium | 6 |
| View/download with ACL | API | Medium | 6 |
| View pointer to office files | Database | Simple | 1 |
| Internal file open | Integration | Simple | 4 |
| View tests | Testing | Easy | 4 |
| Valuer View note | Documentation | Simple | 1 |
| **Total** | | | **22** |

### Estimation Assumptions
- Upload/replace remains F03-003.
