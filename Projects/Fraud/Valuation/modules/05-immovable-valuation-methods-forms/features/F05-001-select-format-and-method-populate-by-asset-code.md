# F05-001 — Select format and method; populate by asset code

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Select format and method; populate by asset code |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
The Valuer opens Data Capturing – II, selects valuation format and method, and enters the asset code. Basics of that assigned asset populate the working form. The valuer then enters method-specific fields. A code that is not assigned to this valuer does not populate.

### Business Objective
Start method work from the assigned asset only, with office basics populated by code.

### Actors
Approved Valuer.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer opens Data Capturing – II, selects valuation format and method, and enters the asset code.
3. How they edit: Basics of that assigned asset populate the working form.
4. How they send for approval: Valuer enters method-specific fields (F05-002–F05-008 as applicable). Select format/method → enter code → populate or refuse → continue to method feature.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record. A code not assigned to this valuer does not populate.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Select valuation format and method
- Populate office basics by asset code if assigned to this Person
- Refuse populate for unassigned codes

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My select format and method; populate by asset code list / queue | Medium |
| Format and method selector | Medium |
| Select format and method; populate by asset code history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Populate working by assigned asset code | Medium |
| Update select format and method; populate by asset code | Medium |
| Search select format and method; populate by asset code | Medium |
| Read select format and method; populate by asset code history | Easy |

### Inputs
Valuation format; method; asset code.

### Outputs
Working form with populated basics; refusal if unassigned.

### Business Rules
- Office first, valuer second — code populate does not let the valuer invent the asset
- Unassigned code does not populate

### Validations
- Code exists
- Assignment to this valuer
- Method allowed for the asset category

### Calculations
None.

### Workflow
Select format/method → enter code → populate or refuse → continue to method feature.

### Search Requirements
Asset code (assigned only).

### Documents
None.

### Reports
None.

### Notifications
In-app refusal for unassigned code.

### Security
Assignment-scoped populate.

### Integrations
Internal asset/assignment consume.

### Dependencies
F04-001; F04-002; F03-001.

### Assumptions
- Format/method lists follow Annexure-01 Formats I–II and Land and Building.

### Risks
Wrong method selected for agri/forest/mine assets that need V-2–V-4.

### Non Functional Requirements
Populate is read of office fields, not an edit back to 3(2).

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My select format and method; populate by asset code list / queue | UI | Medium | 6 |
| Format and method selector | UI | Medium | 6 |
| Select format and method; populate by asset code history | UI | Medium | 6 |
| Populate working by assigned asset code | API | Medium | 6 |
| Update select format and method; populate by asset code | API | Medium | 6 |
| Search select format and method; populate by asset code | API | Medium | 6 |
| Read select format and method; populate by asset code history | API | Easy | 4 |
| Select format and method; populate by asset code persistence | DB | Medium | 4 |
| Assigned-asset consume | Integration | Simple | 4 |
| Select format and method; populate by asset code feature tests | Testing | Medium | 6 |
| Select format and method; populate by asset code implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **56** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
