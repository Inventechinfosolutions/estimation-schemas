# F09-006 — Attendance and expense on Android

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-006 |
| **Feature Name** | Attendance and expense on Android |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
The user submits court attendance or an expense line with voucher photo/upload from the device, linked to the matter, as on web.

### Business Objective
Capture court attendance and expense lines on Android with voucher photo, always linked to the matter as on web.

### Actors
Advocate; Legal Cell.

### User Journey
1. User submits court attendance or an expense line with voucher photo/upload from the device.
2. Linked to the matter, as on web (F07).
3. Cause list photo may accompany attendance.

### Functional Capabilities
- Android Attendance form + cause list photo
- Android Expense + voucher camera/upload
- Mandatory matter link as F07-005
- Parity with web submit
- Not EVAL valuer billing

### Inputs
Attendance fields as F07-001; expense categories as F07-002; photos.

### Outputs
Attendance/expense rows on web matter.

### Business Rules
- Linked to the matter as on web.
- Unlinked personal notes refused.
- Bill compile/review may remain web (F07-004).

### Validations
Same as web; photo size limits; matter required.

### Calculations
Duration if times entered.

### Workflow
Capture on device → sync → web matter dashboard.

### Search Requirements
After sync, F07-003 on web; device list of own drafts.

### Documents
Cause list and voucher images.

### Reports
None on device.

### Notifications
Sync failure.

### Security
Photos not stored in an unprotected gallery export; attributed Person.

### Integrations
Web attendance/expense (Medium).

### Dependencies
F07-001; F07-002; F07-005; F01-004.

### Assumptions
Camera permissions; offline draft then sync.

### Risks
Unreadable voucher photo.

### Non Functional Requirements
Court-precinct capture; retry upload.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android Attendance form + cause list photo | UI | Complex | 12 |
| Android Expense + voucher camera/upload | UI | Complex | 12 |
| Attendance/expense submit operations | API | Complex | 8 |
| Device draft cache | Database | Medium | 4 |
| Web attendance and expense backend | Integration | Medium | 16 |
| Android attendance/expense tests | Testing | Complex | 8 |
| Android attendance and expense guide | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Web bill review remains F07-004.
