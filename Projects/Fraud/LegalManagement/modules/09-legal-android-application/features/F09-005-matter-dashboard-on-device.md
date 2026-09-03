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
1. Who creates: Advocate
2. How they create: User opens a matter on the device.
3. How they edit: Sees tasks, communication, documents, court hearings, team members and client contact in one place.
4. How they send for approval: Drills into an item. Open matter → dashboard → drill-in.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Android Matter Dashboard
- Drill-in item screens
- Tiles aligned with web hub (F04-002) for the listed objects
- In-matter navigation

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Android Matter Dashboard | Very High |
| Drill-in item screens | Complex |
| Matter dashboard on device history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Dashboard aggregate operations | Complex |
| Update matter dashboard on device | Medium |
| Search matter dashboard on device | Medium |
| Read matter dashboard on device history | Easy |

### Inputs
Matter id; drill-in target.

### Outputs
Aggregated device view; navigation to child screens.

### Business Rules
- Same matter data as web.
- Need-to-know on tiles.
- Not eValueI maps.

### Validations
- Matter visible; session valid.

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
- Time and key dates appear if already on web hub; listed SOW items are the acceptance set.

### Risks
Stale dashboard cache in court.

### Non Functional Requirements
Pull-to-refresh; usable on phone form factor.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Android Matter Dashboard | UI | Very High | 16 |
| Drill-in item screens | UI | Complex | 12 |
| Matter dashboard on device history | UI | Medium | 6 |
| Dashboard aggregate operations | API | Complex | 8 |
| Update matter dashboard on device | API | Medium | 6 |
| Search matter dashboard on device | API | Medium | 6 |
| Read matter dashboard on device history | API | Easy | 4 |
| Matter dashboard on device persistence | DB | Medium | 4 |
| Web matter hub | Integration | Medium | 16 |
| Matter dashboard on device feature tests | Testing | Complex | 8 |
| Matter dashboard on device implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **89** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
