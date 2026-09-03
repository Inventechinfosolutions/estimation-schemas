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
1. Who creates: Office user
2. How they create: User uploads a photograph of the group of similar items placed together and individual sample photographs.
3. How they edit: Where capture is on Android, photos inherit GIS tag and date-on-photo rules (F09-003 / F04-006).
4. How they send for approval: CA can later open the group photo without opening every sample. Upload group → upload samples → CA can open group first.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Store group photograph of similar items together
- Store individual sample photographs
- Inherit GIS/date rules on Android capture
- Let CA open group photo without every sample

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My group and sample photographs list / queue | Medium |
| Group and sample photo pack | Complex |
| Group and sample photographs history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Group/sample photo attach | Medium |
| Update group and sample photographs | Medium |
| Search group and sample photographs | Medium |
| Read group and sample photographs history | Easy |

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
|---|---|---|---|
| My group and sample photographs list / queue | UI | Medium | 6 |
| Group and sample photo pack | UI | Complex | 12 |
| Group and sample photographs history | UI | Medium | 6 |
| Group/sample photo attach | API | Medium | 6 |
| Update group and sample photographs | API | Medium | 6 |
| Search group and sample photographs | API | Medium | 6 |
| Read group and sample photographs history | API | Easy | 4 |
| Group and sample photographs persistence | DB | Medium | 4 |
| GIS/date photo-rule consume | Integration | Medium | 16 |
| Group and sample photographs feature tests | Testing | Complex | 8 |
| Group and sample photographs implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **77** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
