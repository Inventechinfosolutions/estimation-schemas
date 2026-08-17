# F05-009 — Tag photos and videos into the valuation library

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-009 |
| **Feature Name** | Tag photos and videos into the valuation library |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
On the valuation working, the Valuer tags field photographs and videos (Module 04) into the report library so the CA report and auction-display selection (Module 07) use the same media set. Untagged media remain on the inspection pack but do not appear in the CA photo-picker until tagged.

### Business Objective
Build a report media library from field capture so CA MIS and auction-display pick from tagged items only.

### Actors
Approved Valuer; Competent Authority (consumes tagged set).

### User Journey
1. On the valuation working the Valuer tags Module 04 photographs and videos into the report library.
2. CA report (F07-001) and auction-display picker (F07-003) use that tagged set.
3. Untagged media remain on the inspection pack but do not appear in the CA photo-picker until tagged.

### Functional Capabilities
- Tag/untag field photos and videos into the valuation report library
- Keep untagged media on the inspection pack only
- Feed F07-001 and F07-003 from the tagged set

### Inputs
Inspection media; tag/untag.

### Outputs
Tagged library membership.

### Business Rules
- CA photo-picker shows tagged only
- Does not replace the four-photo GIS rule (F04-006)

### Validations
- Media belongs to this asset’s inspection pack

### Calculations
Count of tagged items.

### Workflow
Open working → tag media → library updated for CA.

### Search Requirements
Asset, tagged vs untagged.

### Documents
Photographs; videos (library membership).

### Reports
Valuation media library list.

### Notifications
None.

### Security
Assigned valuer tags; CA sees tagged after report available.

### Integrations
Internal media consume from F04-006.

### Dependencies
F04-006; F07-001; F07-003.

### Assumptions
- Tagging does not alter GIS/date metadata.

### Risks
CA picking untagged media if the filter fails.

### Non Functional Requirements
Same media binary; tag is membership only.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Valuation media tagging library | UI | Complex | 12 |
| Tag/untag library membership | API | Medium | 6 |
| Library tag store | Database | Easy | 2 |
| Inspection media consume | Integration | Simple | 4 |
| Library tagging tests | Testing | Medium | 6 |
| Media library note | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- GIS ingest hours remain in F04-006 / F09-003.
