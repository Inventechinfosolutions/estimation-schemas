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
1. For a residential flat or commercial premises, the Valuer selects floor band (basement storage / other basement / GF–1st–mezzanine / 2nd–5th / 6th–9th / 9th+).
2. System applies the FRS weightage to average unit cost A.
3. For Bangalore metropolitan reverse-trend, the valuer explicitly confirms or replaces the factor with local-trend justification. The system does not silently invert the table.

### Functional Capabilities
- Select FRS floor-disposition band
- Apply FRS weightage to average unit cost A
- Require explicit confirm or replace for Bangalore reverse-trend

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
|---|---|---|---:|
| Floor-weightage selector | UI | Medium | 6 |
| Weightage apply with Bangalore confirm | API | Complex | 8 |
| Floor-weightage decision | Database | Easy | 2 |
| Internal FMV consume | Integration | Simple | 4 |
| Floor-weightage tests | Testing | Medium | 6 |
| Floor-weightage guide | Documentation | Medium | 3 |
| **Total** | | | **29** |

### Estimation Assumptions
- Not a GIS feature; no Integration Very High.
