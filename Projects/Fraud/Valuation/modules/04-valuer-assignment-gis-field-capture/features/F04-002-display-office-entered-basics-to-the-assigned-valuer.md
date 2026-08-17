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
1. Valuer opens the application and selects the assigned asset from the dropdown (only assigned assets).
2. Page shows Asset Name, Details, Address, Asset Measure, Asset Registration number, CA Name, Designation, Mobile, Office Address, and FE Name & Code as entered by the office.
3. Valuer cannot blank those office fields. Remaining valuation fields are Module 05.

### Functional Capabilities
- Dropdown of assets already created and assigned to this Person
- Display office basics without re-entry
- Lock office fields against valuer blanking

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
|---|---|---|---:|
| Assigned-asset basics (read-only) | UI | Easy | 4 |
| Populate assigned-asset basics | API | Easy | 4 |
| Read model for basics | Database | Simple | 1 |
| Office-record consume | Integration | Simple | 4 |
| Basics display tests | Testing | Easy | 4 |
| Valuer basics note | Documentation | Simple | 1 |
| **Total** | | | **18** |

### Estimation Assumptions
- Method remaining entry is Module 05 / F09-004.
