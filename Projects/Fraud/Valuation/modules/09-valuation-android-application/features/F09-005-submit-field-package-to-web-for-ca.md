# F09-005 — Submit field package to web for CA

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-005 |
| **Feature Name** | Submit field package to web for CA |
| **Module** | 09 — Valuation Android Application (Approved Valuers) |

### Description
The Valuer submits the inspection and valuation working from Android. An Office user or CA then opens the same package on web (Modules 05–07). A failed submit leaves a clear retry state; partial drafts are attributable to the valuer Person.

### Business Objective
Deliver the field package to web so CA review uses the same data, with retry and attributable drafts.

### Actors
Approved Valuer; Office user; Competent Authority.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer submits inspection and valuation working from Android.
3. How they edit: Office user or CA opens the same package on web (Modules 05–07).
4. How they send for approval: Failed submit leaves a clear retry state; partial drafts are attributable to the valuer Person. Validate set → submit → web package available → on fail retry queue.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record. Submit timestamp feeds F07-006 Time Taken.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Submit field package from Android to web
- Retry state on failure
- Attributable partial drafts
- Stamp submit time for Time Taken

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My submit field package to web for ca list / queue | Medium |
| Android submit and retry | Medium |
| Submit field package to web for ca history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Field-package submit | Very High |
| Update submit field package to web for ca | Medium |
| Search submit field package to web for ca | Medium |
| Read submit field package to web for ca history | Easy |

### Inputs
Submit action; draft package.

### Outputs
Web-visible package; retry state; submit timestamp.

### Business Rules
- Refuse submit without F09-003 qualifying set
- Digital declaration for CA still F05-010 (may complete on web if not on device)
- No silent drop of drafts

### Validations
- Qualifying media set
- Assigned asset
- Connectivity or queued retry

### Calculations
None (timestamp recorded).

### Workflow
Validate set → submit → web package available → on fail retry queue.

### Search Requirements
Submit status on device and web.

### Documents
Field package (inspection + remaining working).

### Reports
None on device.

### Notifications
In-app retry/success.

### Security
Submit attributable; package need-to-know on web.

### Integrations
Device-to-web package sync (multi-step, retry) including large GIS media.

### Dependencies
F09-003; F09-004; F07-006; Modules 05–07.

### Assumptions
- Large photo sync may require retry; 5 MB × 4 minimum is in scope.

### Risks
Partial submit appearing complete on CA queue.

### Non Functional Requirements
Retry is explicit; drafts attributable; submit timestamp stored.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My submit field package to web for ca list / queue | UI | Medium | 6 |
| Android submit and retry | UI | Medium | 6 |
| Submit field package to web for ca history | UI | Medium | 6 |
| Field-package submit | API | Very High | 16 |
| Update submit field package to web for ca | API | Medium | 6 |
| Search submit field package to web for ca | API | Medium | 6 |
| Read submit field package to web for ca history | API | Easy | 4 |
| Submit field package to web for ca persistence | DB | Medium | 4 |
| Device-to-web package sync | Integration | Complex | 24 |
| Submit field package to web for CA feature tests | Testing | Very High | 12 |
| Submit field package to web for CA implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **93** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
