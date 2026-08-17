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
1. Officer enters address and pin code on the depositor profile.
2. The system tallies the pin code to actual areas and shows the verification result.
3. On discrepancy, Officer records the outcome, including RPAD re-verification when that step is used, and saves.

### Functional Capabilities
- Pin-code to area tally.
- Show match/discrepancy result.
- Record RPAD re-verification outcome when used.

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
| Address and pin-code tally screen | UI | Medium | 6 |
| Pin-code tally operations | API | Medium | 6 |
| Address verification persistence | DB | Easy | 2 |
| Pin/area reference tally | Integration | Easy | 8 |
| Address/pin verification tests | Testing | Medium | 6 |
| Pin-code verification note | Documentation | Easy | 2 |
| **Total** | | | **30** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Name/address tally across Aadhaar/PAN/EPIC is F04-005.
