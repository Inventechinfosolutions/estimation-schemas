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
1. Who creates: Approved Valuer
2. How they create: Valuer opens an assigned asset on Android.
3. How they edit: Sees office-entered basics plus View of sale deeds and court orders already uploaded on web (F03-003 / F04-002 / F04-003).
4. How they send for approval: Does not re-type FE/CA/asset identity. Sync assigned list → open asset → show basics → View deeds/orders.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- List and open assigned assets on Android
- Display office basics
- View office-uploaded sale deeds and court orders
- No re-key of FE/CA/asset identity

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My retrieve assigned assets and office documents list / queue | Medium |
| Android assigned-work list | Complex |
| Retrieve assigned assets and office documents history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Assigned pack sync | Complex |
| Update retrieve assigned assets and office documents | Medium |
| Search retrieve assigned assets and office documents | Medium |
| Read retrieve assigned assets and office documents history | Easy |

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
|---|---|---|---|
| My retrieve assigned assets and office documents list / queue | UI | Medium | 6 |
| Android assigned-work list | UI | Complex | 12 |
| Retrieve assigned assets and office documents history | UI | Medium | 6 |
| Assigned pack sync | API | Complex | 8 |
| Update retrieve assigned assets and office documents | API | Medium | 6 |
| Search retrieve assigned assets and office documents | API | Medium | 6 |
| Read retrieve assigned assets and office documents history | API | Easy | 4 |
| Retrieve assigned assets and office documents persistence | DB | Medium | 4 |
| Web-to-device assigned-pack sync | Integration | Medium | 16 |
| Retrieve assigned assets and office documents feature tests | Testing | Complex | 8 |
| Retrieve assigned assets and office documents implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **79** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
