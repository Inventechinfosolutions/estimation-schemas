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
1. Who creates: Approved Valuer
2. How they create: On the selected asset the Valuer clicks View on sale deeds or court order.
3. How they edit: The files the office uploaded (F03-003) open.
4. How they send for approval: If no file was uploaded, View states that; the valuer records the gap in remarks (F04-007) rather than inventing a document. Click View → ACL → open file or missing state.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- View office-uploaded sale deeds and court order
- State clearly when no file was uploaded
- Respect need-to-know (F01-003)

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My view sale deeds and court order list / queue | Medium |
| Deed and court-order viewer | Medium |
| View sale deeds and court order history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| View/download with ACL | Medium |
| Update view sale deeds and court order | Medium |
| Search view sale deeds and court order | Medium |
| Read view sale deeds and court order history | Easy |

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
|---|---|---|---|
| My view sale deeds and court order list / queue | UI | Medium | 6 |
| Deed and court-order viewer | UI | Medium | 6 |
| View sale deeds and court order history | UI | Medium | 6 |
| View/download with ACL | API | Medium | 6 |
| Update view sale deeds and court order | API | Medium | 6 |
| Search view sale deeds and court order | API | Medium | 6 |
| Read view sale deeds and court order history | API | Easy | 4 |
| View sale deeds and court order persistence | DB | Medium | 4 |
| Internal file open | Integration | Simple | 4 |
| View sale deeds and court order feature tests | Testing | Easy | 4 |
| View sale deeds and court order implementation documentation | Documentation | Simple | 1 |
| **Total** | | | **53** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
