# F03-005 — Result Locking & Versioned Re-import

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-005 |
| Feature Name | Result Locking & Versioned Re-import |
| Module | 03 — KPPP Result Intake & Site Package |
| Module Type | Business |
| Release | Go-live |

### Description
Integrity locking of imported results at the point of submission for verification and a controlled re-import path for corrected KPPP results, with reason, approval, version comparison and impact on downstream stages.

### Business Objective
Prevent silent changes to auction results while allowing documented corrections from KPPP.

### Actors
- Auction Admin
- Approving Authority

### User Journey
1. **Who creates:** The system locks results automatically; the Auction Admin initiates a re-import.
2. **How they create:** The Auction Admin selects a locked auction or site, chooses Re-import, attaches the KPPP correction reference, and the system fetches or accepts the new version and shows differences.
3. **How they edit:** The Auction Admin can cancel the re-import before submission.
4. **How they send for approval:** The Auction Admin submits the re-import for approval with reason.
5. **How the approver sees pending items:** The Approving Authority sees pending re-imports with old and new values and stages affected.
6. **How the approver decides:** The Approving Authority approves (new version active, downstream steps reset as configured) or rejects.
7. **How the applicant / maker sees history:** The Auction Admin sees the version history for each result.
8. **How the approver / auditor sees history:** Auditors see all versions with hashes and approvals.

### Functional Capabilities
- Lock on submission for verification with SHA-256 hash
- Re-import request with reason and KPPP reference
- Difference view between versions
- Impact analysis: which stages have started (approval, intimation, payment)
- Approval and activation of new version
- Downstream reset rules (e.g., re-verification, re-intimation) and blocking where payment is received

### UI Screens
- Re-import request form
- Version difference and impact view
- Re-import approval
- Result version history

### Logical API Operations
- Lock result with hash
- Create re-import request
- Compute differences and impact
- Approve / reject re-import
- Activate new version and reset stages
- Verify result hash

### Inputs
- Site or auction
- Reason
- KPPP reference
- New result data

### Outputs
- New active version
- Reset stages
- Version history

### Business Rules
- Locked results cannot be changed except through approved re-import
- Re-import after payment receipt needs Commissioner-level approval (configurable)
- Superseded versions are retained

### Validations
- Reason mandatory
- New version differs from current

### Calculations
- Hash comparison

### Workflow
Locked → Re-import requested → Approved (new version active) | Rejected

### Search Requirements
- Re-imports by auction, status

### Documents
- KPPP correction letter

### Reports
- Re-import log

### Notifications
- Approval request and outcome; notice to affected bidder where intimation already sent

### Security
- Approval mandatory

### Integrations
- Re-fetch through F03-001 connector

### Dependencies
- F03-001
- F03-002
- F04-003

### Assumptions
- Corrections after award are rare

### Risks
- Corrections after payment receipt create refund issues; flagged for manual handling

### Non Functional Requirements
- Impact analysis under 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Re-import request form | Medium | 6 |
| UI | Version difference and impact view | Complex | 12 |
| UI | Re-import approval | Easy | 4 |
| UI | Result version history | Easy | 4 |
| API | Lock result with hash | Easy | 4 |
| API | Create re-import request | Medium | 6 |
| API | Compute differences and impact | Complex | 8 |
| API | Approve / reject re-import | Medium | 6 |
| API | Activate new version and reset stages | Complex | 8 |
| API | Verify result hash | Easy | 4 |
| Database | Result version and lock store | Medium | 4 |
| Testing | Locking, re-import and stage reset tests | Complex | 8 |
| Documentation | Re-import procedure | Easy | 2 |

**Feature Total: 76 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 36 | 4 | 0 | 8 | 2 | **76** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Stage reset logic rated Complex
- No external integration channel in this feature; Integration row omitted.
