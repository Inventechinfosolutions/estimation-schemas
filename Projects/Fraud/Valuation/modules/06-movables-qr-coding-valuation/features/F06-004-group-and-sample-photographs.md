# F06-004 — Group and sample photographs

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-004 |
| **Feature Name** | Group and sample photographs |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
The user uploads a photograph of the group of similar items placed together and individual sample photographs. Photos inherit GIS/date rules where capture is on Android (Module 09). The CA can later open the group photo without opening every sample.

### Business Objective
Evidence movables with a group photograph plus samples, inheriting GIS/date rules on Android capture.

### Actors
Office user; Approved Valuer; Competent Authority (later view).

### User Journey
1. User uploads a photograph of the group of similar items placed together and individual sample photographs.
2. Where capture is on Android, photos inherit GIS tag and date-on-photo rules (F09-003 / F04-006).
3. CA can later open the group photo without opening every sample.

### Functional Capabilities
- Store group photograph of similar items together
- Store individual sample photographs
- Inherit GIS/date rules on Android capture
- Let CA open group photo without every sample

### Inputs
Group photo; sample photos.

### Outputs
Group and sample media on the movable group.

### Business Rules
- Android capture follows min size/GIS/date rules used for field photos
- Generative AI shall not invent photos

### Validations
- Group photo present to complete photo step where required
- Sample photos stored against the group

### Calculations
None.

### Workflow
Upload group → upload samples → CA can open group first.

### Search Requirements
Movable group, has-group-photo.

### Documents
Group photograph; sample photographs.

### Reports
Movable photo completeness.

### Notifications
None.

### Security
Need-to-know with the seizure/assignment.

### Integrations
GIS/date photo rules consume from field/Android pipeline (mapping and retry), not a second geocoding product.

### Dependencies
F06-001; F04-006; F09-003; F07-003 may pick tagged images after F05-009 if used.

### Assumptions
- Web upload of already-captured photos is allowed; Android capture uses GIS rules.

### Risks
Web uploads without GIS when the Authority expected field GIS.

### Non Functional Requirements
CA can retrieve group photo without loading all samples.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Group and sample photo pack | UI | Complex | 12 |
| Group/sample photo attach | API | Medium | 6 |
| Movable photo metadata | Database | Medium | 4 |
| GIS/date photo-rule consume | Integration | Medium | 16 |
| Movable photo tests | Testing | Complex | 8 |
| Movable photo guide | Documentation | Medium | 3 |
| **Total** | | | **49** |

### Estimation Assumptions
- Full GIS ingest pipeline hours remain in F04-006/F09-003; this feature consumes those rules (Integration Medium 16).
