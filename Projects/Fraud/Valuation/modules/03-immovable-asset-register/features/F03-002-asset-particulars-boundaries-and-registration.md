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
1. Who creates: Office user
2. How they create: On the created asset the Officer records name, type, address, document boundaries N/S/E/W, measure, registration date, parties, stamp duty paid and registration fee, and category from F02-002.
3. How they edit: Save updates the record the valuer later sees as basic details (F04-002).
4. How they send for approval: Save updates the record the valuer later sees as basic details (F04-002). Open asset → enter particulars → save → valuer display consumes.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Record asset particulars, document boundaries, measure, registration and parties
- Require immovable category from F02-002
- Expose these fields as read-only basics to the assigned valuer

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My asset particulars, boundaries and registration list / queue | Medium |
| Asset particulars and boundaries form | Complex |
| Asset particulars, boundaries and registration history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Particulars update | Medium |
| Update asset particulars, boundaries and registration | Medium |
| Search asset particulars, boundaries and registration | Medium |
| Read asset particulars, boundaries and registration history | Easy |

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
|---|---|---|---|
| My asset particulars, boundaries and registration list / queue | UI | Medium | 6 |
| Asset particulars and boundaries form | UI | Complex | 12 |
| Asset particulars, boundaries and registration history | UI | Medium | 6 |
| Particulars update | API | Medium | 6 |
| Update asset particulars, boundaries and registration | API | Medium | 6 |
| Search asset particulars, boundaries and registration | API | Medium | 6 |
| Read asset particulars, boundaries and registration history | API | Easy | 4 |
| Asset particulars, boundaries and registration persistence | DB | Medium | 4 |
| Internal basics consume | Integration | Simple | 4 |
| Asset particulars, boundaries and registration feature tests | Testing | Medium | 6 |
| Asset particulars, boundaries and registration implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
