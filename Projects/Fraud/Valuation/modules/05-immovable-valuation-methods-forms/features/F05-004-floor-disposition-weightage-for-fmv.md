# F05-004 — Floor-disposition weightage for FMV

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-004 |
| **Feature Name** | Floor-disposition weightage for FMV |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
For a residential flat or commercial premises, the Valuer selects floor (basement storage / other basement / GF–1st–mezzanine / 2nd–5th / 6th–9th / 9th+) and applies the FRS weightage to average unit cost A. For Bangalore metropolitan reverse-trend, the valuer explicitly confirms or replaces the factor with local-trend justification; the system does not silently invert the table.

### Business Objective
Apply floor weightage to FMV with an explicit Bangalore reverse-trend decision, never a hidden default invert.

### Actors
Approved Valuer.

### User Journey
1. Who creates: Approved Valuer
2. How they create: For a residential flat or commercial premises, the Valuer selects floor band (basement storage / other basement / GF–1st–mezzanine / 2nd–5th / 6th–9th / 9th+).
3. How they edit: System applies the FRS weightage to average unit cost A.
4. How they send for approval: For Bangalore metropolitan reverse-trend, the valuer explicitly confirms or replaces the factor with local-trend justification. The system does not silently invert the table. Select floor → apply table → Bangalore confirm/replace if applicable → save.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Select FRS floor-disposition band
- Apply FRS weightage to average unit cost A
- Require explicit confirm or replace for Bangalore reverse-trend

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My floor-disposition weightage for fmv list / queue | Medium |
| Floor-weightage selector | Medium |
| Floor-disposition weightage for fmv history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Weightage apply with Bangalore confirm | Complex |
| Update floor-disposition weightage for fmv | Medium |
| Search floor-disposition weightage for fmv | Medium |
| Read floor-disposition weightage for fmv history | Easy |

### Inputs
Floor band; average unit cost A; Bangalore confirm/replace and justification when applicable.

### Outputs
Weighted FMV factor stored on the working.

### Business Rules
- Bangalore reverse-trend is a careful local decision, not a hidden default
- No silent invert of the table

### Validations
- Floor band selected
- Justification present if factor replaced

### Calculations
Weightage applied to average unit cost A per FRS table (and explicit local replacement if any).

### Workflow
Select floor → apply table → Bangalore confirm/replace if applicable → save.

### Search Requirements
Asset, floor band, Bangalore decision.

### Documents
None.

### Reports
Floor-weightage decision extract.

### Notifications
In-app prompt when Bangalore reverse-trend rule applies.

### Security
Assigned valuer; decision attributable.

### Integrations
Internal consume by F05-003 / F05-007.

### Dependencies
F05-003; F05-007; Authority confirmation of Bangalore practice.

### Assumptions
- Authority confirms Bangalore floor-weightage practice (SOW dependency).

### Risks
Silent invert would misstate FMV; this feature must not do that.

### Non Functional Requirements
Store the factor used and whether reverse-trend was confirmed or replaced.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My floor-disposition weightage for fmv list / queue | UI | Medium | 6 |
| Floor-weightage selector | UI | Medium | 6 |
| Floor-disposition weightage for fmv history | UI | Medium | 6 |
| Weightage apply with Bangalore confirm | API | Complex | 8 |
| Update floor-disposition weightage for fmv | API | Medium | 6 |
| Search floor-disposition weightage for fmv | API | Medium | 6 |
| Read floor-disposition weightage for fmv history | API | Easy | 4 |
| Floor-disposition weightage for fmv persistence | DB | Medium | 4 |
| Internal FMV consume | Integration | Simple | 4 |
| Floor-disposition weightage for FMV feature tests | Testing | Medium | 6 |
| Floor-disposition weightage for FMV implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **59** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
