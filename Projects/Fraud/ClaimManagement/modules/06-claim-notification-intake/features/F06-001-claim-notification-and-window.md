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
1. Who creates: Officer
2. How they create: Authorised Officer or Administrator creates a notification and selects imported eligible FE and schemes.
3. How they edit: User enters submission period, eligibility, required documents and instructions, and publishes.
4. How they send for approval: The claim window becomes Active for that period. Draft → publish (Active) → close (intake refused). Privileged publish/close audited.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. The same user can close the window; staff-mediated and OOK intake are then refused.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Create notification against imported FE and schemes only.
- Enter period, eligibility, required documents and instructions.
- Publish to make the window Active; close to refuse intake.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Notification create and publish form | Complex |
| Claim window status register | Medium |
| Claim notification and window history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Publish and close operations | Complex |
| Update claim notification and window | Medium |
| Search claim notification and window | Medium |
| Read claim notification and window history | Easy |

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
| Claim notification and window history | UI | Medium | 6 |
| Publish and close operations | API | Complex | 8 |
| Update claim notification and window | API | Medium | 6 |
| Search claim notification and window | API | Medium | 6 |
| Read claim notification and window history | API | Easy | 4 |
| Notification and window persistence | DB | Medium | 4 |
| Claim notification and window feature tests | Testing | Complex | 8 |
| Claim notification and window implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
