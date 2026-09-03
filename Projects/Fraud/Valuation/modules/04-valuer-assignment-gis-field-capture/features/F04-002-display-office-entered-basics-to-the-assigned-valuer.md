# F04-002 — Display office-entered basics to the assigned valuer

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Display office-entered basics to the assigned valuer |
| **Module** | 04 — Valuer Assignment & GIS Field Capture (Data Capturing – I) |

### Description
The Valuer opens the application, selects the assigned asset from the dropdown. The page shows Asset Name, Details, Address, Asset Measure, Asset Registration number, CA Name, Designation, Mobile, Office Address, and FE Name & Code as entered by the office. The valuer cannot blank those office fields; remaining valuation fields are entered later (Module 05).

### Business Objective
On select, show office-entered basics so the valuer cannot invent the asset.

### Actors
Approved Valuer.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer opens the application and selects the assigned asset from the dropdown (only assigned assets).
3. How they edit: Page shows Asset Name, Details, Address, Asset Measure, Asset Registration number, CA Name, Designation, Mobile, Office Address, and FE Name & Code as entered by the office.
4. How they send for approval: Valuer cannot blank those office fields. Remaining valuation fields are Module 05. Open assigned list → select → display office basics.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Dropdown of assets already created and assigned to this Person
- Display office basics without re-entry
- Lock office fields against valuer blanking

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My display office-entered basics to the assigned valuer list / queue | Medium |
| Assigned-asset basics (read-only) | Easy |
| Display office-entered basics to the assigned valuer history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Populate assigned-asset basics | Easy |
| Update display office-entered basics to the assigned valuer | Medium |
| Search display office-entered basics to the assigned valuer | Medium |
| Read display office-entered basics to the assigned valuer history | Easy |

### Inputs
Selected assigned asset.

### Outputs
Read-only basics panel.

### Business Rules
- Unassigned assets shall not appear
- Office fields are display-only for the valuer

### Validations
- Asset is assigned to this valuer Person

### Calculations
None.

### Workflow
Open assigned list → select → display office basics.

### Search Requirements
Assigned-asset dropdown (not a general office search).

### Documents
None on this panel (View deeds is F04-003).

### Reports
None.

### Notifications
None.

### Security
Assignment-scoped; F01-003.

### Integrations
Internal office asset consume.

### Dependencies
F04-001; F03-001; F03-002.

### Assumptions
- CA mobile/office address shown are as stored on the programme CA reference / office record.

### Risks
Stale basics if office edits after assignment without refresh.

### Non Functional Requirements
Refresh from current office record on open.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My display office-entered basics to the assigned valuer list / queue | UI | Medium | 6 |
| Assigned-asset basics (read-only) | UI | Easy | 4 |
| Display office-entered basics to the assigned valuer history | UI | Medium | 6 |
| Populate assigned-asset basics | API | Easy | 4 |
| Update display office-entered basics to the assigned valuer | API | Medium | 6 |
| Search display office-entered basics to the assigned valuer | API | Medium | 6 |
| Read display office-entered basics to the assigned valuer history | API | Easy | 4 |
| Display office-entered basics to the assigned valuer persistence | DB | Medium | 4 |
| Office-record consume | Integration | Simple | 4 |
| Display office-entered basics to the assigned valuer feature tests | Testing | Easy | 4 |
| Display office-entered basics to the assigned valuer implementation documentation | Documentation | Simple | 1 |
| **Total** | | | **49** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
