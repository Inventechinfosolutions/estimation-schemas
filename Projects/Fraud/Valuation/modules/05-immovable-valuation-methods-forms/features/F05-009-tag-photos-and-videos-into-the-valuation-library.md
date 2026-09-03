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
1. Who creates: Approved Valuer
2. How they create: On the valuation working the Valuer tags Module 04 photographs and videos into the report library.
3. How they edit: CA report (F07-001) and auction-display picker (F07-003) use that tagged set.
4. How they send for approval: Untagged media remain on the inspection pack but do not appear in the CA photo-picker until tagged. Open working → tag media → library updated for CA.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Tag/untag field photos and videos into the valuation report library
- Keep untagged media on the inspection pack only
- Feed F07-001 and F07-003 from the tagged set

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My tag photos and videos into the valuation library list / queue | Medium |
| Valuation media tagging library | Complex |
| Tag photos and videos into the valuation library history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Tag/untag library membership | Medium |
| Update tag photos and videos into the valuation library | Medium |
| Search tag photos and videos into the valuation library | Medium |
| Read tag photos and videos into the valuation library history | Easy |

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
|---|---|---|---|
| My tag photos and videos into the valuation library list / queue | UI | Medium | 6 |
| Valuation media tagging library | UI | Complex | 12 |
| Tag photos and videos into the valuation library history | UI | Medium | 6 |
| Tag/untag library membership | API | Medium | 6 |
| Update tag photos and videos into the valuation library | API | Medium | 6 |
| Search tag photos and videos into the valuation library | API | Medium | 6 |
| Read tag photos and videos into the valuation library history | API | Easy | 4 |
| Tag photos and videos into the valuation library persistence | DB | Medium | 4 |
| Inspection media consume | Integration | Simple | 4 |
| Tag photos and videos into the valuation library feature tests | Testing | Medium | 6 |
| Tag photos and videos into the valuation library implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
