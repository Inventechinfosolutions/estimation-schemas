# F05-003 — Citizen Active Notification Visibility

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-003 |
| **Feature Name** | Citizen Active Notification Visibility |
| **Module** | 05 — Housing Notification Management |

### Description
Present only active, approved housing notifications to citizens with the public booking information required for discovery.

### Business Objective
Ensure citizens see accurate, currently actionable housing opportunities.

### Actors
Citizen; Housing officers (publication verification); Auditor.

### User Journey
Citizen opens the housing notification area, sees active notifications, filters/selects one, reads project/unit summaries and terms, and proceeds to supported portal actions.

### Functional Capabilities
Active-only listing; notification detail; booking-window indicator; project/unit summary; terms/policy and document requirements display; expired/withdrawn suppression.

### Inputs
Published notification, current date/time, citizen filters.

### Outputs
Citizen-facing active notification list and detail display.

### Business Rules
Only active approved notifications in their booking window are visible; expired or withdrawn notifications are suppressed; application capture is Module 07.

### Validations
Active publication/status/window required; only approved linked project content displayed.

### Calculations
None.

### Workflow
Notification becomes published/active → citizen portal evaluates eligibility → list/detail displayed or suppressed.

### Search Requirements
Project, location, property type, booking window, price/availability indicators, active status.

### Documents
Published notification terms, policies, required-document information and referenced project material.

### Reports
None; management reporting is outside this feature.

### Notifications
No separate campaign notification; portal visibility updates immediately on publish/withdraw.

### Security
Public read-only access; no unpublished content; secure links to authorised materials.

### Integrations
Citizen portal content handoff (Simple).

### Dependencies
F05-001; F05-002; Module 06.

### Assumptions
Citizen registration and application processing are estimated in Modules 06–07.

### Risks
Caching or timing discrepancies could briefly show stale availability.

### Non Functional Requirements
Responsive web; agreed page response targets; consistent active-window evaluation.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Citizen active notification listing | UI | Complex | 8 |
| Citizen notification detail view | UI | Complex | 8 |
| Active notification retrieval operations | API | Complex | 8 |
| Visibility and publication persistence | Database | Medium | 4 |
| Citizen portal content handoff | Integration | Simple | 4 |
| Citizen visibility tests | Testing | Complex | 8 |
| Citizen notification guide | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
