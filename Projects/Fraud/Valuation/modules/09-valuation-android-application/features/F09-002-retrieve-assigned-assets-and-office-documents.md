# F09-002 — Retrieve assigned assets and office documents

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Retrieve assigned assets and office documents |
| **Module** | 09 — Valuation Android Application (Approved Valuers) |

### Description
The Valuer opens an assigned asset on Android and sees office-entered basics plus View of sale deeds and court orders already uploaded on web. The valuer does not re-type FE/CA/asset identity.

### Business Objective
Give the field valuer the office pack on device without re-keying identity.

### Actors
Approved Valuer.

### User Journey
1. Valuer opens an assigned asset on Android.
2. Sees office-entered basics plus View of sale deeds and court orders already uploaded on web (F03-003 / F04-002 / F04-003).
3. Does not re-type FE/CA/asset identity.

### Functional Capabilities
- List and open assigned assets on Android
- Display office basics
- View office-uploaded sale deeds and court orders
- No re-key of FE/CA/asset identity

### Inputs
Assigned-asset selection on device.

### Outputs
Device view of basics and office documents.

### Business Rules
- Only assigned assets
- Office fields not blanked
- Need-to-know F01-003

### Validations
- Assignment to this Person
- Document ACL

### Calculations
None.

### Workflow
Sync assigned list → open asset → show basics → View deeds/orders.

### Search Requirements
Assigned assets on device (dropdown/list).

### Documents
Sale deeds; court order (view on device).

### Reports
None.

### Notifications
In-app if document missing (same gap rule as F04-003).

### Security
Assignment-scoped download/view; documents not a public gallery.

### Integrations
Web-to-device sync of assigned pack (auth, mapping, retry).

### Dependencies
F04-001; F04-002; F04-003; F03-003; F01-003.

### Assumptions
- Field connectivity sufficient to retrieve; offline cache of already-downloaded packs is in scope as attributable drafts.

### Risks
Stale deeds if office replaces files after last sync.

### Non Functional Requirements
No re-type of identity; refresh from web when connected.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android assigned-work list | UI | Complex | 12 |
| Assigned pack sync | API | Complex | 8 |
| Device assigned-pack cache | Database | Medium | 4 |
| Web-to-device assigned-pack sync | Integration | Medium | 16 |
| Android retrieve tests | Testing | Complex | 8 |
| Android retrieve guide | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- GIS capture is F09-003; method remaining entry F09-004.
