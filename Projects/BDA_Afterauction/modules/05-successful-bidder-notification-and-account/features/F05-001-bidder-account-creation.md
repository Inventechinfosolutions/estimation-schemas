# F05-001 — Bidder Account Creation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-001 |
| Feature Name | Bidder Account Creation |
| Module | 05 — Successful Bidder Notification & Account |
| Module Type | Business |
| Release | Go-live |

### Description
Automatic creation of the successful bidder's account in the Bidder Tracking Portal on final approval of a result, using KPPP bidder details, with de-duplication so that a bidder winning several sites (in this or earlier auctions) has one account, and correction of contact details by the Auction Admin with evidence.

### Business Objective
Give every successful bidder immediate, secure access to track their sites and pay instalments.

### Actors
- System
- Auction Admin
- Successful Bidder

### User Journey
1. **Who creates:** The system creates the account automatically when the result is approved.
2. **How they create:** On approval, the system checks for an existing account by PAN / mobile / KPPP bidder ID, creates or links the account and attaches the awarded site.
3. **How they edit:** The Auction Admin can correct mobile or e-mail with an uploaded request letter; the bidder can update details through OTP in F05-002.
4. **How they send for approval:** Contact corrections by the Auction Admin can require Approving Authority confirmation (configurable).
5. **How the approver sees pending items:** The confirming officer sees pending contact corrections.
6. **How the approver decides:** The confirming officer approves or rejects the correction.
7. **How the applicant / maker sees history:** The bidder sees all their sites after login.
8. **How the approver / auditor sees history:** Auditors see account creation, linking and every contact change.

### Functional Capabilities
- Automatic account creation on approval
- De-duplication by PAN, mobile and KPPP bidder ID with manual merge for conflicts
- Support for joint bidders / companies with authorised representative
- Contact correction with evidence and optional confirmation
- Account status: Active, Suspended, Closed

### UI Screens
- Bidder account list
- Bidder account detail with linked sites
- Contact correction with evidence
- Duplicate resolution / merge

### Logical API Operations
- Create or link bidder account on approval
- Detect duplicates
- Merge accounts
- Correct contact details
- Confirm correction
- Suspend / close account

### Inputs
- KPPP bidder details
- Correction details and evidence

### Outputs
- Active bidder account
- Linked sites

### Business Rules
- One account per PAN
- Mobile number is the login identity; change requires evidence
- Accounts with no open sites are closed after retention period

### Validations
- PAN format
- Mobile 10 digits
- E-mail format

### Calculations
- None

### Workflow
Created → Active → Suspended / Closed

### Search Requirements
- Bidders by name, PAN (masked), mobile, site

### Documents
- Contact correction request letter

### Reports
- Bidder accounts report

### Notifications
- Login details sent with intimation (F05-004)

### Security
- PAN masked in UI; encrypted at rest

### Integrations
- None

### Dependencies
- F04-003
- F05-002

### Assumptions
- KPPP provides PAN and mobile for each bidder

### Risks
- Missing or wrong mobile from KPPP; correction path mitigates

### Non Functional Requirements
- Account creation within 1 minute of approval

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Bidder account list | Easy | 4 |
| UI | Bidder account detail with linked sites | Medium | 6 |
| UI | Contact correction with evidence | Easy | 4 |
| UI | Duplicate resolution / merge | Medium | 6 |
| API | Create or link bidder account on approval | Complex | 8 |
| API | Detect duplicates | Medium | 6 |
| API | Merge accounts | Medium | 6 |
| API | Correct contact details | Easy | 4 |
| API | Confirm correction | Easy | 4 |
| API | Suspend / close account | Easy | 4 |
| Database | Bidder account and site linkage | Medium | 4 |
| Testing | Account creation and de-duplication tests | Medium | 6 |
| Testing | Correction and merge tests | Easy | 4 |
| Documentation | Bidder account administration guide | Easy | 2 |

**Feature Total: 68 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 32 | 4 | 0 | 10 | 2 | **68** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- De-duplication rated Complex
- No external integration channel in this feature; Integration row omitted.
