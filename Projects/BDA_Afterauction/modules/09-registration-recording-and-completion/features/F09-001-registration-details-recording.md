# F09-001 — Registration Details Recording

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-001 |
| Feature Name | Registration Details Recording |
| Module | 09 — Registration Recording & Completion |
| Module Type | Business |
| Release | Go-live |

### Description
Recording of sale deed registration done outside the Module: registration number, book and volume, date, Sub-Registrar office, stamp duty and fees paid, and upload of the registered deed copy, entered by the case worker or submitted by the bidder for verification.

### Business Objective
Capture registration evidence to close the case and update records.

### Actors
- Case Worker
- Deputy Secretary
- Successful Bidder

### User Journey
1. **Who creates:** The bidder or case worker records registration details.
2. **How they create:** They enter registration details and upload the registered deed copy.
3. **How they edit:** Entries can be edited until verification.
4. **How they send for approval:** The entry goes to the DS for verification.
5. **How the approver sees pending items:** The DS sees pending registration verifications.
6. **How the approver decides:** The DS verifies or returns.
7. **How the applicant / maker sees history:** The bidder sees verification status.
8. **How the approver / auditor sees history:** Auditors see entry and verification.

### Functional Capabilities
- Registration detail capture
- Registered deed upload
- Verification by DS
- Precondition: 100% payment

### UI Screens
- Registration entry (staff)
- Registration submission (bidder)
- Registration verification

### Logical API Operations
- Record registration
- Upload registered deed
- Verify registration
- Get registration details

### Inputs
- Registration number, date, office, fees
- Deed copy

### Outputs
- Verified registration

### Business Rules
- Allowed only after 100% payment
- Registration number unique per office

### Validations
- Date not in future
- PDF ≤ 20 MB

### Calculations
- None

### Workflow
Entered → Verified | Returned

### Search Requirements
- By registration number

### Documents
- Registered deed copy

### Reports
- Registration status report

### Notifications
- Verification outcome

### Security
- DS isolation

### Integrations
- None

### Dependencies
- F06-005
- F02-006

### Assumptions
- None

### Risks
- None significant

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Registration entry (staff) | Easy | 4 |
| UI | Registration submission (bidder) | Easy | 4 |
| UI | Registration verification | Easy | 4 |
| API | Record registration | Easy | 4 |
| API | Upload registered deed | Easy | 4 |
| API | Verify registration | Easy | 4 |
| API | Get registration details | Simple | 2 |
| Database | Registration record | Easy | 2 |
| Testing | Recording and verification tests | Easy | 4 |
| Documentation | Registration recording guide | Simple | 1 |

**Feature Total: 33 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 14 | 2 | 0 | 4 | 1 | **33** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small
- No external integration channel in this feature; Integration row omitted.
