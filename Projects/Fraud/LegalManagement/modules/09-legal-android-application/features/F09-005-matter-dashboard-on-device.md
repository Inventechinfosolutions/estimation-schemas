# F09-005 — Matter dashboard on device

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-005 |
| **Feature Name** | Matter dashboard on device |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
The user opens a matter and sees tasks, communication, documents, court hearings, team members and client contact in one place, then drills into an item.

### Business Objective
Provide the Annexure-I matter dashboard on Android: tasks, communication, documents, hearings, team, client contact, with drill-in.

### Actors
Advocate; Legal Cell.

### User Journey
1. User opens a matter on the device.
2. Sees tasks, communication, documents, court hearings, team members and client contact in one place.
3. Drills into an item.

### Functional Capabilities
- Android Matter Dashboard
- Drill-in item screens
- Tiles aligned with web hub (F04-002) for the listed objects
- In-matter navigation

### Inputs
Matter id; drill-in target.

### Outputs
Aggregated device view; navigation to child screens.

### Business Rules
- Same matter data as web.
- Need-to-know on tiles.
- Not eValueI maps.

### Validations
Matter visible; session valid.

### Calculations
Counts as on web dashboard.

### Workflow
Open matter → dashboard → drill-in.

### Search Requirements
In-matter find as device allows.

### Documents
Document tile → F09-007.

### Reports
None.

### Notifications
Overdue/hearing badges if synced.

### Security
Limited tiles hidden.

### Integrations
Web matter hub (Medium).

### Dependencies
F04-002; F09-002; F09-003; F09-007; F01-004.

### Assumptions
Time and key dates appear if already on web hub; listed SOW items are the acceptance set.

### Risks
Stale dashboard cache in court.

### Non Functional Requirements
Pull-to-refresh; usable on phone form factor.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android Matter Dashboard | UI | Very High | 16 |
| Drill-in item screens | UI | Complex | 12 |
| Dashboard aggregate operations | API | Complex | 8 |
| Device hub cache | Database | Medium | 4 |
| Web matter hub | Integration | Medium | 16 |
| Android dashboard tests | Testing | Complex | 8 |
| Android matter dashboard guide | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Web hub hours remain F04-002.
