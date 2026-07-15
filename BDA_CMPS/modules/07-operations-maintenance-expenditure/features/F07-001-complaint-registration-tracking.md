# F07-001 — Complaint Registration & Tracking

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F07-001 |
| **Feature Name** | Complaint Registration & Tracking |
| **Module** | 07 — Operations, Maintenance & Expenditure |

### Description
Allow officers and tenants (portal) to raise maintenance complaints across configurable categories (Electrical, Plumbing, Civil, Cleaning, Lift, Parking, Security, Others) and track status end-to-end (M6-AC1).

### Business Objective
Digitize complaint intake so issues are visible, assignable, and auditable across BDA commercial properties.

### Actors
- Tenant (Portal), Maintenance Officer, Property Manager, Data Entry Operator

### User Journey
1. Tenant/officer creates complaint with property/unit, category, description, photos.
2. System assigns ticket number and initial status.
3. User tracks progress through subsequent workflow stages (F07-002).

### Functional Capabilities
- Complaint create/list/detail for officers
- Tenant portal raise + track own complaints
- Categories configurable
- Photo/document attachments at registration
- Link to property/unit/lease where applicable
- Search/filter by status, category, property, date

### Inputs
- Category, property/unit, description, priority, attachments, complainant contact

### Outputs
- Complaint ticket; tracking timeline start

### Business Rules
- Tenant sees only own complaints; officers scoped by Module 01 data scope.
- SLA clock starts on registration (F07-002).
- Cannot delete after work order started—cancel with reason only.

### Validations
- Mandatory category/property/description
- Attachment type/size limits

### Calculations
None at intake (SLA due in F07-002).

### Workflow
Registered → (Assignment in F07-002).

### Search Requirements
By ticket no., property, category, status, complainant, date.

### Documents
Photos/docs via Module 08.

### Reports
Complaint Register (feeds Module 11).

### Notifications
Acknowledgement to tenant/officer (Module 09).

### Security
RBAC; tenant IDOR prevention; audit.

### Integrations
Internal DMS (Simple).

### Dependencies
Modules 01, 03, 08, 09; F01 portal auth; F07-002

### Assumptions
- Three Complex UIs: officer list/detail, create wizard, portal.
- Native mobile app out of scope; responsive web only.

### Risks
- Duplicate complaints for same issue — suggest open-ticket warnings.

### Non Functional Requirements
- Mobile-friendly portal create; < 3s list typical

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Complaint register & detail (officer) | UI | Complex | 8 |
| Complaint create wizard + attachments | UI | Complex | 8 |
| Tenant portal raise/track complaint | UI | Complex | 8 |
| Complaint lifecycle ops | API | Complex | 8 |
| Complaint entities | Database | Medium | 4 |
| DMS attachment handoff | Integration | Simple | 4 |
| Complaint registration tests | Testing | Complex | 8 |
| Complaint registration guide | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- End-to-end stage transitions estimated mainly in F07-002.
