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
1. Who creates: Administrator
2. How they create: Administrator maintains lists such as locality HIG/MIG/LIG, zone types, and condition grades New/Unused/Working/Damaged/Scrap/Obsolete.
3. How they edit: Office and valuer screens consume those lists.
4. How they send for approval: Reports use the stored list values, not free spelling. Maintain list → screens consume → reports print stored values.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Maintain named static lists for valuation modules
- Force consume on office and valuer screens that use those lists

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My central static masters for valuation list / queue | Medium |
| Static list maintenance | Medium |
| Central static masters for valuation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Static list CRUD and consume | Easy |
| Update central static masters for valuation | Medium |
| Search central static masters for valuation | Medium |
| Read central static masters for valuation history | Easy |

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
|---|---|---|---|
| My central static masters for valuation list / queue | UI | Medium | 6 |
| Static list maintenance | UI | Medium | 6 |
| Central static masters for valuation history | UI | Medium | 6 |
| Static list CRUD and consume | API | Easy | 4 |
| Update central static masters for valuation | API | Medium | 6 |
| Search central static masters for valuation | API | Medium | 6 |
| Read central static masters for valuation history | API | Easy | 4 |
| Central static masters for valuation persistence | DB | Medium | 4 |
| Internal list consume | Integration | Simple | 4 |
| Central static masters for valuation feature tests | Testing | Easy | 4 |
| Central static masters for valuation implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
