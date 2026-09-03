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
1. Who creates: Advocate
2. How they create: User opens the Legal Android app (session from F01-004).
3. How they edit: Adds a contact or a matter with required fields including FE/CA/court as on web, and saves.
4. How they send for approval: The record appears on web for authorised Posts. Add on Android → save → sync to web → authorised Posts see it.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Android Add Contact screens
- Android Add Matter screens (FE/CA/court as on web)
- Save and sync to web
- Same identity; no second login directory
- iOS out of scope

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Android Add Contact screens | Complex |
| Android Add Matter screens (FE/CA/court as on web) | Very High |
| Add contact and matter on android history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Sync create operations | Complex |
| Update add contact and matter on android | Medium |
| Search add contact and matter on android | Medium |
| Read add contact and matter on android history | Easy |

### Inputs
Contact fields as Module 06; matter fields as F04-001 (classification, FE, CA, court, opponents, date).

### Outputs
Contact and/or matter on device cache and web.

### Business Rules
- Required fields including FE/CA/court as on web.
- IP of the app with SPLOCA.
- Not Claim settlement or eValueI field capture.

### Validations
- Same required fields as web; shared session valid; sync conflict surfaced.

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
- Offline draft may cache then sync; authoritative store is server.

### Risks
Partial save if network drops mid-matter create.

### Non Functional Requirements
Usable in court precincts with intermittent network; retry sync.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Android Add Contact screens | UI | Complex | 12 |
| Android Add Matter screens (FE/CA/court as on web) | UI | Very High | 16 |
| Add contact and matter on android history | UI | Medium | 6 |
| Sync create operations | API | Complex | 8 |
| Update add contact and matter on android | API | Medium | 6 |
| Search add contact and matter on android | API | Medium | 6 |
| Read add contact and matter on android history | API | Easy | 4 |
| Add contact and matter on android persistence | DB | Medium | 4 |
| Web contact and matter backend | Integration | Medium | 16 |
| Add contact and matter on Android feature tests | Testing | Complex | 8 |
| Add contact and matter on Android implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **89** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
