# F01-003 — Assignment and need-to-know on valuation documents

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | Assignment and need-to-know on valuation documents |
| **Module** | 01 — Shared User & Access Control (consumed) |

### Description
An Officer assigns an asset to a valuer Person. That valuer opens sale deeds, court orders, photographs and the report for that asset. Another valuer not assigned cannot open those files. The system records who viewed or downloaded which valuation document and when.

### Business Objective
Enforce need-to-know on valuation packs so only the assigned valuer (or CA/office override) can open deeds, orders, photographs and reports.

### Actors
Office user; Approved Valuer; Competent Authority; Administrator.

### User Journey
1. Officer assigns an asset to a valuer Person (assignment recorded in F04-001).
2. That valuer opens sale deeds, court orders, photographs or the report for that asset.
3. A valuer who is not assigned is refused; CA or named office override may open as the Authority defines.
4. Each view or download is recorded against the shared Person, document and time.

### Functional Capabilities
- Restrict view/download of sale deeds, court orders, photographs, CAD and valuation reports by Post and assignment
- Apply CA/office override when the Authority defines it
- Record who viewed or downloaded which valuation document and when

### Inputs
Asset id; valuer Person; document type; view or download action; optional CA/office override.

### Outputs
Permitted open or refused open; document access event.

### Business Rules
- A valuer sees only assets assigned to that Person unless a CA/office override applies
- Document rights follow Post and assignment
- Access events are attributable and not silently deleted

### Validations
- Asset is assigned to the requesting valuer Person, or override is authorised
- Document exists on the asset
- Post is allowed to view/download that document type

### Calculations
None.

### Workflow
Request open → check Post → check assignment/override → permit or refuse → write access event.

### Search Requirements
Person, asset, document type, view vs download, date range.

### Documents
Sale deeds, court orders, photographs, CAD, valuation reports — access controlled here; files themselves are stored on the asset (Modules 03–05).

### Reports
Valuation document access log.

### Notifications
In-app refusal when the valuer is not assigned.

### Security
Need-to-know ACL; immutable access log; no anonymous download.

### Integrations
Internal assignment and document store (F03-003, F04-001, F04-003, F04-006).

### Dependencies
F01-001; F01-002; F04-001 assignment; document uploads in Module 03.

### Assumptions
- Override rules (CA/office) are named by the Authority before go-live.

### Risks
Missing assignment sync could leak documents to a previously assigned valuer after reassignment.

### Non Functional Requirements
Access check on every view/download; audit retained with the pack.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Valuation document access log | UI | Complex | 12 |
| Document ACL and view/download audit | API | Complex | 8 |
| Document access events | Database | Medium | 4 |
| Assignment-to-document ACL (internal) | Integration | Simple | 4 |
| Need-to-know access tests | Testing | Complex | 8 |
| Valuation document-rights guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Assignment capture remains F04-001; this feature is rights and access log
- Not a standalone DMS product
