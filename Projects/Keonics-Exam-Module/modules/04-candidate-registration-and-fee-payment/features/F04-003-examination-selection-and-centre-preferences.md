# F04-003 — Examination Selection and Centre Preferences

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | Examination Selection and Centre Preferences |
| **Module** | 04 — Candidate Registration and Fee Payment |

### Description
After identity capture (F04-001 or F04-002), the candidate selects an examination that is currently open for registration and records **two preferred centres** from active authorised centres. Preferences are stored on the registration draft for later centre allocation (F05-002).

### Business Objective
Capture examination choice and ordered centre preferences so scheduling and allocation can honour candidate preference and centre capacity rules.

### Actors
Maker: Candidate. Approver: none. Auditor: Examination Administrator (preference history on registration).

### User Journey
1. Who creates: The authenticated candidate with a Type 1 or Type 2 identity draft in progress.
2. How they create: Open examinations list → select one open examination → review examination summary → select preferred centre 1 and preferred centre 2 from active authorised centres → confirm preferences → save to registration draft.
3. How they edit: Before fee payment success / registration completion lock, candidate may change examination (if still open and rules allow) and/or change the two centre preferences; after lock, changes require admin policy (out of this feature’s normal path).
4. How they send for approval: Does not apply — preference capture is not an approval workflow.
5. How the approver sees pending items: No approver inbox for preferences.
6. How the approver decides: No decision step.
7. How the applicant / maker sees history: Candidate sees saved examination and preference pair on draft summary and later on registration status (F04-005).
8. How the approver / auditor sees history: Administrator views preference values and change history on the registration during verification and allocation preparation.

### Functional Capabilities
- List examinations currently open for registration only.
- Prevent selection of closed, inactive or not-yet-open examinations.
- Show examination summary needed for informed choice (name, window, high-level parameters as configured).
- Require exactly two preferred centres.
- Enforce that preference 1 and preference 2 are distinct centres.
- Restrict selectable centres to active authorised centres from Module 03.
- Persist preferences on the registration draft linked to the selected examination.
- Validate eligibility to select the examination for the candidate type where configured.
- Allow preference change before completion lock.
- Surface clear messages when no open examination or insufficient active centres exist.
- Provide preference confirmation before continuing to fee path.
- Audit examination selection and preference changes.

### UI Screens
| Screen | Purpose |
|---|---|
| Open examinations list screen | Browse examinations open for registration |
| Examination selection detail screen | Confirm chosen examination particulars |
| Two centre preferences selection screen | Choose preference 1 and preference 2 |
| Preference confirmation screen | Confirm examination and centres before save |
| Centre preference change history screen | View preference/exam change trail |

### Logical API operations
| Operation | Purpose |
|---|---|
| List open examinations for registration | Return selectable examinations |
| Get examination selection detail | Return summary for chosen examination |
| Save examination and centre preferences | Persist exam + two centres on draft |
| Validate preference eligibility | Enforce distinct centres, active centres, open exam |
| Get centre preference history | Return change history for the draft |

### Inputs
Selected examination identifier; preferred centre 1; preferred centre 2; registration draft reference; candidate session.

### Outputs
Updated registration draft with examination and two centre preferences; validation errors; preference history events.

### Business Rules
- Only open-for-registration examinations are selectable.
- Exactly two preferences; centres must differ.
- Only active authorised centres appear.
- Preferences are inputs to later allocation (F05-002); selection here is not final allotment.
- Identity draft (F04-001/F04-002) must exist before preferences can be saved.

### Validations
- Examination open status.
- Centre active/authorised status.
- Preference 1 ≠ preference 2.
- Draft ownership by logged-in candidate.

### Calculations
None (capacity enforcement is at allocation, not preference capture).

### Workflow
Identity draft ready → select open examination → select two centres → confirm → draft ready for fee (F04-004). No approval.

### Search Requirements
Admin may filter registrations by selected examination and preferred centres for operational preparation.

### Documents
None.

### Reports
Preference distribution feeds Module 09; not a separate report artefact here.

### Notifications
None specific beyond in-portal validation messages.

### Security
Candidate edits only own draft; admin read for operations; audited changes.

### Integrations
None.

### Dependencies
F04-001 or F04-002; Module 03 examination and centre masters; consumed by F04-004, F05-002.

### Assumptions
- Centre list and open flags come from Module 03 masters.
- Allocation algorithm is F05-002, not this feature.
- Hours vary from sibling features; each screen/API estimated independently.

### Risks
Thin active-centre lists force repeated preference changes; candidates may confuse preference with final allotment.

### Non Functional Requirements
Clear preference UX; consistent centre labels/addresses; auditable preference changes.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Open examinations list screen | UI | Medium | 6 |
| Examination selection detail screen | UI | Easy | 4 |
| Two centre preferences selection screen | UI | Complex | 12 |
| Preference confirmation screen | UI | Easy | 4 |
| Centre preference change history screen | UI | Easy | 4 |
| List open examinations for registration | API | Medium | 6 |
| Get examination selection detail | API | Easy | 4 |
| Save examination and centre preferences | API | Complex | 8 |
| Validate preference eligibility | API | Medium | 6 |
| Get centre preference history | API | Easy | 4 |
| Examination selection and preference persistence | Database | Medium | 4 |
| Examination selection and preferences tests | Testing | Medium | 6 |
| Examination selection and preferences documentation | Documentation | Easy | 2 |

**Feature total: 70 hours**

### Estimation Assumptions
- No integration channel on this feature.
- Final centre allotment hours remain on F05-002.
