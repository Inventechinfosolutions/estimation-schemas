# F09-004 — Method-specific remaining entry on Android

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-004 |
| **Feature Name** | Method-specific remaining entry on Android |
| **Module** | 09 — Valuation Android Application (Approved Valuers) |

### Description
The Valuer selects the valuation method/format on the device and completes remaining fields (including eValueM tabulation where the assignment is movable). Approved secure sources may be queried as on web. Generative AI is not offered.

### Business Objective
Complete method-specific remaining particulars in the field on the same rules as Modules 05–06, without generative AI.

### Actors
Approved Valuer.

### User Journey
1. Valuer selects valuation method/format on the device and completes remaining fields, including eValueM tabulation when the assignment is movable.
2. May query approved secure sources as on web (F04-007).
3. Generative AI is not offered.

### Functional Capabilities
- Method/format remaining entry on Android
- eValueM tabulation on device when movable
- Approved-source query as on web
- No generative AI

### Inputs
Method/format; remaining field values; optional approved source.

### Outputs
Device draft of method remaining fields.

### Business Rules
- Same business rules as Modules 05–06 (subset remaining entry, not a second method engine rebuild of every V-1 control)
- No generative comparable or narrative invention

### Validations
- Assignment type matches method
- Approved source on Authority list

### Calculations
As in web method engines where those calculations are invoked; device may collect inputs and sync for engine run on submit if connectivity requires — still no AI.

### Workflow
Select method → enter remaining fields → optional source query → draft ready to submit.

### Search Requirements
On-device draft by asset.

### Documents
None beyond field pack.

### Reports
None.

### Notifications
In-app if mandatory remaining fields empty.

### Security
Assigned valuer; source queries audited.

### Integrations
Approved-source retrieve and web method-working sync (auth, mapping, retry).

### Dependencies
F05-001–F05-008; F06-001–F06-002; F04-007; F09-005.

### Assumptions
- Full Form V-1 working on a small screen may complete on web after submit of remaining fields; remaining field set is the FRS ‘method-specific remaining particulars’.

### Risks
Under-specifying remaining fields vs full V-1; Authority must confirm which fields are mandatory on device vs web.

### Non Functional Requirements
No generative AI; drafts attributable to Person.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android method remaining entry | UI | Very High | 16 |
| Device method remaining save | API | Complex | 8 |
| Device method draft | Database | Medium | 4 |
| Approved-source and web working sync | Integration | Medium | 16 |
| Android method-entry tests | Testing | Very High | 12 |
| Android method-entry guide | Documentation | Complex | 4 |
| **Total** | | | **60** |

### Estimation Assumptions
- UI Very High 16 for dynamic method UI on Android. Full statutory assemble remains Module 05/06 on web where needed.
