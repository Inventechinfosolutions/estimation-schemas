# F09-001 — Add contact and matter on Android

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-001 |
| **Feature Name** | Add contact and matter on Android |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
An Advocate or Legal Cell user opens the Android app, adds a contact or a matter (with required fields including FE/CA/court as on web), and saves. The record appears on web for authorised Posts.

### Business Objective
Let advocates and Legal Cell create contacts and matters on Android with the same required fields as web, syncing to web.

### Actors
Advocate; Legal Cell.

### User Journey
1. User opens the Legal Android app (session from F01-004).
2. Adds a contact or a matter with required fields including FE/CA/court as on web, and saves.
3. The record appears on web for authorised Posts.

### Functional Capabilities
- Android Add Contact screens
- Android Add Matter screens (FE/CA/court as on web)
- Save and sync to web
- Same identity; no second login directory
- iOS out of scope

### Inputs
Contact fields as Module 06; matter fields as F04-001 (classification, FE, CA, court, opponents, date).

### Outputs
Contact and/or matter on device cache and web.

### Business Rules
- Required fields including FE/CA/court as on web.
- IP of the app with SPLOCA.
- Not Claim settlement or eValueI field capture.

### Validations
Same required fields as web; shared session valid; sync conflict surfaced.

### Calculations
None.

### Workflow
Add on Android → save → sync to web → authorised Posts see it.

### Search Requirements
Device lists plus web search after sync.

### Documents
None at create.

### Reports
None.

### Notifications
Sync failure notice on device.

### Security
F01-004 session; no local password store.

### Integrations
Web contact/matter backend (Medium).

### Dependencies
F01-004; F04-001; F06-001/F06-002; F02-005.

### Assumptions
Offline draft may cache then sync; authoritative store is server.

### Risks
Partial save if network drops mid-matter create.

### Non Functional Requirements
Usable in court precincts with intermittent network; retry sync.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android Add Contact screens | UI | Complex | 12 |
| Android Add Matter screens (FE/CA/court as on web) | UI | Very High | 16 |
| Sync create operations | API | Complex | 8 |
| Device local cache | Database | Medium | 4 |
| Web contact and matter backend | Integration | Medium | 16 |
| Android create tests | Testing | Complex | 8 |
| Android add-contact and add-matter guide | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Web Create Matter hours remain F04-001; this is Android UI + sync.
- Play Store licensing is F09-008.
