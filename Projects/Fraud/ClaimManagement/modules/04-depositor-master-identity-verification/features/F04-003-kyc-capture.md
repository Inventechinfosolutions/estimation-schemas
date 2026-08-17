# F04-003 — KYC capture

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | KYC capture |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
The Officer opens the depositor profile and enters personal information, Aadhaar, PAN, contacts, deposit and refund bank accounts, nominee and legal-heir details, then saves. These fields are the ones later used in claim intake and verification.

### Business Objective
Capture the KYC fields that intake (F06) and verification (F07) will rely on.

### Actors
Officer; assisting staff; auditor (read as authorised).

### User Journey
1. Officer opens the unique depositor profile.
2. Officer enters personal information, Aadhaar, PAN, contacts, deposit and refund bank accounts, nominee and legal-heir details.
3. Officer saves. Unverified Aadhaar capture remains visible as unverified only (F04-009).
4. Intake and verification later read these same fields.

### Functional Capabilities
- Capture personal information, Aadhaar, PAN and contacts.
- Capture deposit and refund bank accounts.
- Capture nominee and legal-heir details.
- Persist fields for intake and verification.

### Inputs
Personal data, Aadhaar, PAN, contacts, bank accounts, nominee/heir details.

### Outputs
Saved KYC on the unique depositor profile.

### Business Rules
- Unverified Aadhaar is not identity proof (F04-009).
- Refund account is the one later used for penny-drop (F04-007) and payment (Module 08).
- In-KA claimants do not self-key this as a mass portal; Officers capture from originals.

### Validations
- Mandatory KYC fields as Authority policy.
- Bank account format checks as applicable.

### Calculations
None.

### Workflow
Open profile → enter KYC → save. Verification of Aadhaar/PAN is F04-009.

### Search Requirements
Name, Aadhaar/PAN (authorised), contacts, profile ID.

### Documents
Supporting KYC papers via F04-010.

### Reports
None standalone.

### Notifications
None.

### Security
Depositor KYC is need-to-know. Aadhaar/PAN display follows official handling rules.

### Integrations
None for capture; verification services are F04-009.

### Dependencies
F04-002.

### Assumptions
- OOK claimants confirm these details on their own pack in F06-003 rather than becoming staff.

### Risks
- Capturing Aadhaar without the F04-009 unverified flag would be treated as proof incorrectly.

### Non Functional Requirements
Large KYC form remains usable (tabs/sections). Structured fields, not a PDF form dump.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| KYC capture form (personal, ID, banks, nominee) | UI | Complex | 12 |
| KYC save operations | API | Complex | 8 |
| KYC persistence | DB | Complex | 6 |
| KYC capture tests | Testing | Complex | 8 |
| KYC capture guide | Documentation | Medium | 3 |
| **Total** | | | **37** |

### Estimation Assumptions
- Uses Estimation Master values only.
- UI Complex 12 for the large KYC form (not 8).
- Aadhaar service call is F04-009.
