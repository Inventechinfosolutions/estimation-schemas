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
1. Valuer opens Data Capturing – II, selects valuation format and method, and enters the asset code.
2. Basics of that assigned asset populate the working form.
3. Valuer enters method-specific fields (F05-002–F05-008 as applicable).
4. A code not assigned to this valuer does not populate.

### Functional Capabilities
- Select valuation format and method
- Populate office basics by asset code if assigned to this Person
- Refuse populate for unassigned codes

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
|---|---|---|---:|
| Format and method selector | UI | Medium | 6 |
| Populate working by assigned asset code | API | Medium | 6 |
| Working-form header | Database | Easy | 2 |
| Assigned-asset consume | Integration | Simple | 4 |
| Populate-by-code tests | Testing | Medium | 6 |
| Method selector note | Documentation | Easy | 2 |
| **Total** | | | **26** |

### Estimation Assumptions
- Method engines are F05-002 and F05-005; statutory forms F05-007/008.
