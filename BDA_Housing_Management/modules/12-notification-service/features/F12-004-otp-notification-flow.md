# F12-004 — OTP Notification Flow

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F12-004 |
| **Feature Name** | OTP Notification Flow |
| **Module** | 12 — Notification Service |

### Description
Generate, dispatch, verify, expire, and resend mobile OTPs for citizen registration and other approved verification journeys.
### Business Objective
Confirm control of the mobile number before a protected citizen action completes.
### Actors
- Citizen; System
### User Journey
1. Citizen starts registration or verification. 2. BHMS sends an OTP to the registered mobile. 3. Citizen enters the code before expiry; outcome is recorded.
### Functional Capabilities
- OTP generation, configurable expiry/resend controls, verification, attempt limits, and outcome logging.
### Inputs
- Mobile number, verification purpose, OTP entry, and request context.
### Outputs
- Verified/not-verified result and next permitted action.
### Business Rules
- OTP is single-use, purpose-bound, expires after the configured window, and is rate limited.
### Validations
- Mobile format, active challenge, correct code, expiry, attempt limit, and resend interval.
### Calculations
- Requested → sent → verified / expired / locked.
### Workflow
- By masked mobile, purpose, request date, and verification outcome for authorized support.
### Search Requirements
- No standalone document.
### Documents
- OTP volume, success, expiry, and lockout trend.
### Reports
- OTP SMS through F12-002; portal status through F12-001 where applicable.
### Notifications
- F12-001/F12-002 and citizen-registration flows.
### Security
- BDA confirms OTP expiry, resend, and lockout policy.
### Integrations
- SMS-delivery failure or mobile-number change can prevent citizen registration.
### Dependencies
- Low-latency verification, abuse resistance, and no exposure of OTP values in logs.
### Assumptions
- [('OTP entry and resend experience', 'UI', 'Medium', 6), ('OTP generation, verification, and expiry operations', 'API', 'Complex', 8), ('OTP challenge state', 'Database', 'Easy', 2), ('OTP delivery coordination', 'Integration', 'Easy', 8), ('OTP flow tests', 'Testing', 'Complex', 8), ('OTP flow guide', 'Documentation', 'Easy', 2)]
### Risks
- 
### Non Functional Requirements
- 

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| OTP entry and resend experience | UI | Medium | 6 |
| OTP generation, verification, and expiry operations | API | Complex | 8 |
| OTP challenge state | Database | Easy | 2 |
| OTP delivery coordination | Integration | Easy | 8 |
| OTP flow tests | Testing | Complex | 8 |
| OTP flow guide | Documentation | Easy | 2 |
| **Total** | | | **34** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. [('OTP entry and resend experience', 'UI', 'Medium', 6), ('OTP generation, verification, and expiry operations', 'API', 'Complex', 8), ('OTP challenge state', 'Database', 'Easy', 2), ('OTP delivery coordination', 'Integration', 'Easy', 8), ('OTP flow tests', 'Testing', 'Complex', 8), ('OTP flow guide', 'Documentation', 'Easy', 2)]
