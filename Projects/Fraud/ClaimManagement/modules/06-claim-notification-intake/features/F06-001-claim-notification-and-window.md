# F06-001 — Claim notification and window

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | Claim notification and window |
| **Module** | 06 — Claim Notification & Intake |

### Description
An authorised Officer or Administrator creates a notification, selects imported eligible FE and schemes, enters submission period, eligibility, required documents and instructions, and publishes it. The claim window becomes Active for that period. The same user can close the window; intake is then refused.

### Business Objective
Open and close claim windows against imported FE/schemes so intake cannot run outside a published period.

### Actors
Officer; Administrator.

### User Journey
1. Authorised Officer or Administrator creates a notification and selects imported eligible FE and schemes.
2. User enters submission period, eligibility, required documents and instructions, and publishes.
3. The claim window becomes Active for that period.
4. The same user can close the window; staff-mediated and OOK intake are then refused.

### Functional Capabilities
- Create notification against imported FE and schemes only.
- Enter period, eligibility, required documents and instructions.
- Publish to make the window Active; close to refuse intake.

### Inputs
Imported FE/schemes, submission period, eligibility, required documents, instructions.

### Outputs
Published notification; Active or Closed window used by F01-008, F06-002, F06-003.

### Business Rules
- Only imported FE and schemes are selectable.
- Intake is refused when the window is closed or the period has ended.
- In-KA vs OOK channel rules remain; the window does not create a mass in-KA portal.

### Validations
- Period end is on or after period start.
- At least one imported FE and scheme.

### Calculations
Window Active if published and now is within period and not manually closed.

### Workflow
Draft → publish (Active) → close (intake refused). Privileged publish/close audited.

### Search Requirements
FE, scheme, window status, period dates.

### Documents
Required-document list is instructions; actual packs are F06-002/003/004.

### Reports
Open/closed window register.

### Notifications
Window status is visible to staff and to OOK constrained path; not a public homepage PDF portal.

### Security
Only authorised Posts publish or close. Actions attributable to Person in Post.

### Integrations
None.

### Dependencies
F02-001, F02-003; F01-003.

### Assumptions
- sploca.org PDF portal is not rebuilt as the notification channel.

### Risks
- Leaving a window open after the period would allow late intake.

### Non Functional Requirements
Window state must be consistent for counter and OOK at the same moment.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Notification create and publish form | UI | Complex | 12 |
| Claim window status register | UI | Medium | 6 |
| Publish and close operations | API | Complex | 8 |
| Notification and window persistence | DB | Medium | 4 |
| Notification and window tests | Testing | Complex | 8 |
| Claim notification guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Intake wizards are estimated in F06-002 and F06-003.
