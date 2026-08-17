# F02-006 — Central static masters for valuation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-006 |
| **Feature Name** | Central static masters for valuation |
| **Module** | 02 — Valuation Masters, Property Coding & References |

### Description
An Administrator maintains static lists used across valuation (for example locality classification HIG/MIG/LIG, zone types, condition grades New/Unused/Working/Damaged/Scrap/Obsolete). Office and valuer screens consume those lists so spelling does not fragment reports.

### Business Objective
Centralise static lists so reports and Forms V-1–V-8 do not fragment on spelling.

### Actors
Administrator; Office user; Approved Valuer.

### User Journey
1. Administrator maintains lists such as locality HIG/MIG/LIG, zone types, and condition grades New/Unused/Working/Damaged/Scrap/Obsolete.
2. Office and valuer screens consume those lists.
3. Reports use the stored list values, not free spelling.

### Functional Capabilities
- Maintain named static lists for valuation modules
- Force consume on office and valuer screens that use those lists

### Inputs
List name; list value; sort; active.

### Outputs
Pick-lists on consuming screens; consistent report labels.

### Business Rules
- Consuming screens do not accept free text for these lists
- Inactive values hidden on new entry

### Validations
- Value unique within list

### Calculations
None.

### Workflow
Maintain list → screens consume → reports print stored values.

### Search Requirements
List name, value, active.

### Documents
None.

### Reports
Static master export.

### Notifications
None.

### Security
Administrator maintains.

### Integrations
Internal consume by Modules 03–07.

### Dependencies
Module 01 access.

### Assumptions
- Initial values follow Annexure-01 / Authority confirmation.

### Risks
Changing a value in use on submitted forms needs history, not silent rewrite of issued forms.

### Non Functional Requirements
Issued forms keep the value as at submit; lists affect new entry.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Static list maintenance | UI | Medium | 6 |
| Static list CRUD and consume | API | Easy | 4 |
| Static list values | Database | Easy | 2 |
| Internal list consume | Integration | Simple | 4 |
| Static master tests | Testing | Easy | 4 |
| Static masters note | Documentation | Easy | 2 |
| **Total** | | | **22** |

### Estimation Assumptions
- Structure classification (life/residual) is F02-007, not a generic list.
