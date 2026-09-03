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
1. Who creates: Approved Valuer
2. How they create: Valuer selects valuation method/format on the device and completes remaining fields, including eValueM tabulation when the assignment is movable.
3. How they edit: May query approved secure sources as on web (F04-007).
4. How they send for approval: Generative AI is not offered. Select method → enter remaining fields → optional source query → draft ready to submit.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Method/format remaining entry on Android
- eValueM tabulation on device when movable
- Approved-source query as on web
- No generative AI

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My method-specific remaining entry on android list / queue | Medium |
| Android method remaining entry | Very High |
| Method-specific remaining entry on android history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Device method remaining save | Complex |
| Update method-specific remaining entry on android | Medium |
| Search method-specific remaining entry on android | Medium |
| Read method-specific remaining entry on android history | Easy |

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
|---|---|---|---|
| My method-specific remaining entry on android list / queue | UI | Medium | 6 |
| Android method remaining entry | UI | Very High | 16 |
| Method-specific remaining entry on android history | UI | Medium | 6 |
| Device method remaining save | API | Complex | 8 |
| Update method-specific remaining entry on android | API | Medium | 6 |
| Search method-specific remaining entry on android | API | Medium | 6 |
| Read method-specific remaining entry on android history | API | Easy | 4 |
| Method-specific remaining entry on android persistence | DB | Medium | 4 |
| Approved-source and web working sync | Integration | Medium | 16 |
| Method-specific remaining entry on Android feature tests | Testing | Very High | 12 |
| Method-specific remaining entry on Android implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **88** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
