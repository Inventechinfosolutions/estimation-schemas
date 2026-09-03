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
1. Who creates: Officer
2. How they create: Officer opens the unique depositor profile.
3. How they edit: Officer enters personal information, Aadhaar, PAN, contacts, deposit and refund bank accounts, nominee and legal-heir details.
4. How they send for approval: Officer saves. Unverified Aadhaar capture remains visible as unverified only (F04-009). Open profile → enter KYC → save. Verification of Aadhaar/PAN is F04-009.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Intake and verification later read these same fields.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Capture personal information, Aadhaar, PAN and contacts.
- Capture deposit and refund bank accounts.
- Capture nominee and legal-heir details.
- Persist fields for intake and verification.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My kyc capture list / queue | Medium |
| KYC capture form (personal, ID, banks, nominee) | Complex |
| Kyc capture history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| KYC save operations | Complex |
| Update kyc capture | Medium |
| Search kyc capture | Medium |
| Read kyc capture history | Easy |

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
| My kyc capture list / queue | UI | Medium | 6 |
| KYC capture form (personal, ID, banks, nominee) | UI | Complex | 12 |
| Kyc capture history | UI | Medium | 6 |
| KYC save operations | API | Complex | 8 |
| Update kyc capture | API | Medium | 6 |
| Search kyc capture | API | Medium | 6 |
| Read kyc capture history | API | Easy | 4 |
| KYC persistence | DB | Complex | 6 |
| KYC capture feature tests | Testing | Complex | 8 |
| KYC capture implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **65** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
