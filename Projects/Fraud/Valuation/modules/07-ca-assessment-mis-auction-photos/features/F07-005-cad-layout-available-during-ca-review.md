# F07-005 — CAD / layout available during CA review

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-005 |
| **Feature Name** | CAD / layout available during CA review |
| **Module** | 07 — CA Assessment, MIS Reports & Auction-Display Photos |

### Description
While assessing, the CA (or authorised officer) opens the CAD/layout uploaded in F03-006 for maintenance and security context. Absence of a drawing is visible; it does not by itself block Accept unless the Authority marks CAD mandatory for that category.

### Business Objective
Give CA review access to the office-uploaded CAD/layout without making absence an automatic Accept block.

### Actors
Competent Authority; authorised officer.

### User Journey
1. While assessing, the CA or authorised officer opens the CAD/layout from F03-006.
2. Absence of a drawing is visible.
3. Absence does not by itself block Accept unless the Authority marks CAD mandatory for that category.

### Functional Capabilities
- Open CAD/layout in CA assessment context
- Show absence clearly
- Optional mandatory-CAD-by-category rule if Authority marks it

### Inputs
Open CAD action; optional category-mandatory flag.

### Outputs
Viewed layout or visible absence.

### Business Rules
- Not a separate drawing product
- Default: absence does not block Accept

### Validations
- Authorised Post

### Calculations
None.

### Workflow
During F07-002 → open CAD or see absence.

### Search Requirements
None beyond the open assessment.

### Documents
CAD/layout (view).

### Reports
None.

### Notifications
None.

### Security
CA/authorised officer; need-to-know.

### Integrations
Internal file open from F03-006.

### Dependencies
F03-006; F07-002.

### Assumptions
- Mandatory-CAD-by-category is off unless Authority sets it.

### Risks
Missing CAD for complex sites.

### Non Functional Requirements
Absence is visible in the CA UI.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| CAD viewer in CA review | UI | Easy | 4 |
| Open CAD in CA context | API | Simple | 2 |
| CAD presence flag | Database | Simple | 1 |
| F03-006 file consume | Integration | Simple | 4 |
| CA CAD-view tests | Testing | Simple | 2 |
| CA CAD note | Documentation | Simple | 1 |
| **Total** | | | **14** |

### Estimation Assumptions
- Upload hours remain F03-006.
