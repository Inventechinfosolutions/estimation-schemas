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
1. Valuer submits inspection and valuation working from Android.
2. Office user or CA opens the same package on web (Modules 05–07).
3. Failed submit leaves a clear retry state; partial drafts are attributable to the valuer Person.
4. Submit timestamp feeds F07-006 Time Taken.

### Functional Capabilities
- Submit field package from Android to web
- Retry state on failure
- Attributable partial drafts
- Stamp submit time for Time Taken

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
|---|---|---|---:|
| Android submit and retry | UI | Medium | 6 |
| Field-package submit | API | Very High | 16 |
| Submit/retry state | Database | Medium | 4 |
| Device-to-web package sync | Integration | Complex | 24 |
| Submit/retry tests | Testing | Very High | 12 |
| Android submit guide | Documentation | Medium | 3 |
| **Total** | | | **65** |

### Estimation Assumptions
- API Very High 16 for package submit workflow; Integration Complex 24 for device-web media sync.
