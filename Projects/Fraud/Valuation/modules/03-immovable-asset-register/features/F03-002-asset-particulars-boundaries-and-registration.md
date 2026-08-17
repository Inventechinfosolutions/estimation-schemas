# F03-002 — Asset particulars, boundaries and registration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Asset particulars, boundaries and registration |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
On that asset, the Officer records name, type, address, document boundaries (North, South, East, West), measure, registration date, parties, stamp duty paid and registration fee, and category (Land, Property, Building, Lease Holding, Other). Saving updates the record the valuer will later see as “basic details”.

### Business Objective
Capture document particulars so the assigned valuer sees office-entered basics without re-keying.

### Actors
Office user.

### User Journey
1. On the created asset the Officer records name, type, address, document boundaries N/S/E/W, measure, registration date, parties, stamp duty paid and registration fee, and category from F02-002.
2. Save updates the record the valuer later sees as basic details (F04-002).

### Functional Capabilities
- Record asset particulars, document boundaries, measure, registration and parties
- Require immovable category from F02-002
- Expose these fields as read-only basics to the assigned valuer

### Inputs
Asset Name; Type; Address; Boundaries N/S/E/W as per document; Asset Measure; Asset Registration Date; Parties; Stamp Duty Paid; Registration Fee; category.

### Outputs
Updated particulars pack used as valuer “basic details”.

### Business Rules
- Valuer cannot blank these office fields (F04-002)
- Category must come from F02-002

### Validations
- Boundaries labelled N/S/E/W
- Category from master
- Measure present when the Authority marks it mandatory

### Calculations
None.

### Workflow
Open asset → enter particulars → save → valuer display consumes.

### Search Requirements
Name, address, registration date, category (via F03-005).

### Documents
Particulars as per sale deed; deed files in F03-003.

### Reports
Particulars completeness checklist.

### Notifications
None.

### Security
Office Post only to edit; valuer read via assignment.

### Integrations
Internal consume by F04-002.

### Dependencies
F03-001; F02-002.

### Assumptions
- Document boundaries are as per deed, not a survey product.

### Risks
Incomplete particulars delay assignment-ready 3(2).

### Non Functional Requirements
History of particulars edits retained.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Asset particulars and boundaries form | UI | Complex | 12 |
| Particulars update | API | Medium | 6 |
| Particulars and boundary fields | Database | Easy | 2 |
| Internal basics consume | Integration | Simple | 4 |
| Particulars tests | Testing | Medium | 6 |
| Particulars entry note | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- Title/e-Khata/dues workflow remains Claim Module 03, not this form.
