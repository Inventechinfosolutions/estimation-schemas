# F03-006 — Property Photos & Document Linkage

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F03-006 |
| **Feature Name** | Property Photos & Document Linkage |
| **Module** | 03 — Property & Asset Inventory |

### Description
Allow upload/view of property photographs and linkage of property-related documents (plans, NOCs, etc.) from the inventory record via Document Management.

### Business Objective
Give officers visual and documentary context for each asset without leaving the property workspace.

### Actors
- Estate Officer, Property Manager, Data Entry Operator

### User Journey
1. Open property/unit → Photos / Documents.
2. Upload photos or link existing DMS documents.
3. View gallery/preview; remove/replace with audit.

### Functional Capabilities
- Multi-photo upload with captions/order
- Link document categories relevant to property
- Preview thumbnails; open via Module 08 permissions
- Delete/replace governed by permission

### Inputs
- Image files, captions, document refs/categories

### Outputs
- Linked media set on property/unit

### Business Rules
- Storage/versioning owned by Module 08; this feature provides entity-context UX.
- File type/size limits applied.
- Litigation supporting docs can be linked when status is Under Litigation.

### Validations
- File type/size; virus scan hook if platform provides
- Permission to upload

### Calculations
None.

### Workflow
N/A.

### Search Requirements
Filter properties “with/without photos” optional.

### Documents
All property photos/docs (Module 08).

### Reports
None mandatory.

### Notifications
None.

### Security
Document category ACLs from Module 08 enforced on download.

### Integrations
Internal Document Management service (Simple).

### Dependencies
Module 08; F03-001/002.

### Assumptions
- Does not rebuild DMS; linkage + photo gallery only.
- Scanning legacy files is BDA operational effort.

### Risks
- Large unmanaged photo volumes — retention policy needed.

### Non Functional Requirements
- Mobile-friendly upload for field photos
- Reasonable thumbnail performance

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Photo gallery & upload UI on property | UI | Complex | 8 |
| Document link panel on property | UI | Medium | 6 |
| Media upload/link operations | API | Medium | 6 |
| Media metadata linkage | Database | Easy | 2 |
| DMS handoff (internal) | Integration | Simple | 4 |
| Media linkage tests | Testing | Medium | 6 |
| Property media guide | Documentation | Easy | 2 |
| **Total** | | | **34** |

### Estimation Assumptions
- DMS core estimated in Module 08; Simple internal integration here.
