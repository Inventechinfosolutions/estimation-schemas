# F04-004 — Address and pin-code verification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-004 |
| **Feature Name** | Address and pin-code verification |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
The Officer enters address and pin code. The system tallies the pin code to actual areas and shows the verification result. On discrepancy the Officer records the outcome (including RPAD re-verification when that step is used) and saves.

### Business Objective
Tally pin code to actual areas and record discrepancy/RPAD outcomes on the depositor.

### Actors
Officer.

### User Journey
1. Who creates: Officer
2. How they create: Officer enters address and pin code on the depositor profile.
3. How they edit: The system tallies the pin code to actual areas and shows the verification result.
4. How they send for approval: On discrepancy, Officer records the outcome, including RPAD re-verification when that step is used, and saves. Enter address/pin → tally → record discrepancy/RPAD → save.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Pin-code to area tally.
- Show match/discrepancy result.
- Record RPAD re-verification outcome when used.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My address and pin-code verification list / queue | Medium |
| Address and pin-code tally screen | Medium |
| Address and pin-code verification history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Pin-code tally operations | Medium |
| Update address and pin-code verification | Medium |
| Search address and pin-code verification | Medium |
| Read address and pin-code verification history | Easy |

### Inputs
Address, pin code, RPAD outcome when applicable.

### Outputs
Verification result on the profile; recorded discrepancy handling.

### Business Rules
- Discrepancy does not silently pass.
- RPAD is recorded when that step is used; it is not assumed for every case.

### Validations
- Pin code format.
- Address mandatory when policy requires it for the claim.

### Calculations
Pin-to-area tally result.

### Workflow
Enter address/pin → tally → record discrepancy/RPAD → save.

### Search Requirements
Address, pin code, tally result (match / discrepancy).

### Documents
RPAD papers if used, via F04-010.

### Reports
Pin-discrepancy list for Officers.

### Notifications
None.

### Security
Address is KYC-class data (need-to-know).

### Integrations
Pin/area reference used for tally.

### Dependencies
F04-003.

### Assumptions
- Pin/area reference is an available official or contracted dataset.

### Risks
- Stale pin-area data would false-flag or miss discrepancies.

### Non Functional Requirements
Address / pin-code queries are part of programme search requirements.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My address and pin-code verification list / queue | UI | Medium | 6 |
| Address and pin-code tally screen | UI | Medium | 6 |
| Address and pin-code verification history | UI | Medium | 6 |
| Pin-code tally operations | API | Medium | 6 |
| Update address and pin-code verification | API | Medium | 6 |
| Search address and pin-code verification | API | Medium | 6 |
| Read address and pin-code verification history | API | Easy | 4 |
| Address verification persistence | DB | Easy | 2 |
| Pin/area reference tally | Integration | Easy | 8 |
| Address and pin-code verification feature tests | Testing | Medium | 6 |
| Address and pin-code verification implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **58** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
