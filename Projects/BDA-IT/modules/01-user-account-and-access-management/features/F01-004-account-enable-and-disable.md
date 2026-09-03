# F01-004 — Account Enable and Disable

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-004 |
| **Feature Name** | Account Enable and Disable |
| **Module** | 01 — User Account and Access Management |

### Description
Admin activates or disables an account so access can be withdrawn without deleting the person from history. A disabled account cannot sign in. Past requests and tickets remain.

### Business Objective
Joiners and leavers (or suspended contract staff) can be granted or withdrawn access without destroying audit history.

### Actors
Maker: Admin. Approver: none.

### User Journey
1. Who creates: Admin initiates enable or disable on an existing account.
2. How they create: From the user account register, Admin chooses Disable (or Enable), confirms the action, and the account status changes.
3. How they edit: Admin may enable a disabled account again, or disable an enabled account. Status history records each change.
4. How they send for approval: Submit/approval does not apply.
5. How the approver sees pending items: There is no approver inbox.
6. How the approver decides: There is no approval decision on this feature.
7. How the maker sees history: Admin opens account status history (enabled/disabled, who, when).
8. How the approver / auditor sees history: Admin uses the same status history.

### Functional Capabilities
- Disable an enabled account
- Enable a disabled account
- Block login for disabled accounts
- Keep request/ticket history attached to the account after disable

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Disable confirmation | Simple |
| Enable confirmation | Simple |
| Account status history | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Disable account | Medium |
| Enable account | Medium |
| Enforce disabled login block | Easy |
| Read status history | Easy |

### Inputs
Account, action (enable / disable), confirmation.

### Outputs
Updated account status; status history; login refused when disabled.

### Business Rules
- Disable does not delete the account or its requests/tickets.
- Disabled accounts fail authentication.
- Admin cannot be left with zero enabled Admin accounts (at least one Admin remains enabled).

### Validations
- Confirmation required before disable.
- Last remaining enabled Admin cannot be disabled.

### Calculations
None.

### Workflow
No approval. Admin confirmation is final.

### Search Requirements
Register filter by enabled/disabled (owned with F01-001 register; this feature supplies status and history).

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
Admin only. User cannot enable or disable any account.

### Integrations
None.

### Dependencies
F01-001; login block enforced with F01-003.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- The user account register itself is billed under F01-001; this feature bills only enable/disable confirmations and status history.
- Soft-delete of accounts is out of scope.

### Risks
If the last Admin is disabled in error despite the guard, BDA would need a controlled operational recovery outside this estimate.

### Non Functional Requirements
Enable/disable attributable to the Admin who confirmed the action.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Disable confirmation | UI | Simple | 2 |
| Enable confirmation | UI | Simple | 2 |
| Account status history | UI | Easy | 4 |
| Disable account | API | Medium | 6 |
| Enable account | API | Medium | 6 |
| Enforce disabled login block | API | Easy | 4 |
| Read status history | API | Easy | 4 |
| Account status records | DB | Easy | 2 |
| Account enable and disable tests | Testing | Medium | 6 |
| Account enable and disable implementation documentation | Documentation | Easy | 2 |

**Feature total: 38 hours**
