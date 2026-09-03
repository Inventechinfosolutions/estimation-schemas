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
1. Who creates: Competent Authority
2. How they create: While assessing, the CA or authorised officer opens the CAD/layout from F03-006.
3. How they edit: Absence of a drawing is visible.
4. How they send for approval: Absence does not by itself block Accept unless the Authority marks CAD mandatory for that category. During F07-002 → open CAD or see absence.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Competent Authority works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Competent Authority opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Open CAD/layout in CA assessment context
- Show absence clearly
- Optional mandatory-CAD-by-category rule if Authority marks it

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My cad / layout available during ca review list / queue | Medium |
| CAD viewer in CA review | Easy |
| Cad / layout available during ca review history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Open CAD in CA context | Simple |
| Update cad / layout available during ca review | Medium |
| Search cad / layout available during ca review | Medium |
| Read cad / layout available during ca review history | Easy |

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
|---|---|---|---|
| My cad / layout available during ca review list / queue | UI | Medium | 6 |
| CAD viewer in CA review | UI | Easy | 4 |
| Cad / layout available during ca review history | UI | Medium | 6 |
| Open CAD in CA context | API | Simple | 2 |
| Update cad / layout available during ca review | API | Medium | 6 |
| Search cad / layout available during ca review | API | Medium | 6 |
| Read cad / layout available during ca review history | API | Easy | 4 |
| Cad / layout available during ca review persistence | DB | Medium | 4 |
| F03-006 file consume | Integration | Simple | 4 |
| CAD / layout available during CA review feature tests | Testing | Simple | 2 |
| CAD / layout available during CA review implementation documentation | Documentation | Simple | 1 |
| **Total** | | | **45** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
