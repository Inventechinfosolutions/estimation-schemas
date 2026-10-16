# F04-002 — Single-Bidder & Abnormal Bid Flagging

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-002 |
| Feature Name | Single-Bidder & Abnormal Bid Flagging |
| Module | 04 — Result Verification & Approval |
| Module Type | Business |
| Release | Go-live |

### Description
Automatic flagging of results with a single bidder, bids below or close to the upset price, premium outside configured thresholds, bids far from the layout average, bidders with earlier defaults, and multiple sites won by the same bidder, with flag reasons shown to verifiers and approvers.

### Business Objective
Bring unusual results to the attention of decision makers as required by the RFP and support informed approval.

### Actors
- System
- Result Verifier
- Approving Authority

### User Journey
1. **Who creates:** Flags are created by the system on intake; no user creates them.
2. **How they create:** The flag engine evaluates thresholds from F02-003 and bidder history and attaches flags with reasons and values.
3. **How they edit:** Flags cannot be edited; the verifier can add a justification note against each flag.
4. **How they send for approval:** Flagged sites go for approval with flags and justifications attached.
5. **How the approver sees pending items:** Approvers see flag badges and reasons in their inbox and decision screen.
6. **How the approver decides:** Approvers decide considering the flags; certain flags can force a higher approval level (configured in F02-003).
7. **How the applicant / maker sees history:** Verifiers see flag history on the site.
8. **How the approver / auditor sees history:** Auditors see flag evaluations with threshold version used.

### Functional Capabilities
- Single-bidder flag
- Premium below / above thresholds; bid equals upset price
- Outlier against layout or auction average rate per sq. m
- Bidder previously defaulted or cancelled in BDA auctions
- Same bidder winning multiple sites in the auction (count and value)
- Flag justification notes
- Re-evaluation on re-import

### UI Screens
- Flags panel on workbench
- Flag justification dialog
- Flagged results report screen

### Logical API Operations
- Evaluate flags for result
- Compute layout averages
- Check bidder default history
- Save flag justification
- List flagged results
- Re-evaluate on re-import

### Inputs
- Result data
- Thresholds
- Bidder history

### Outputs
- Flags with reasons
- Justifications

### Business Rules
- Flag evaluation uses the threshold version active at intake
- Bidder matching uses PAN, mobile and KPPP bidder ID

### Validations
- Justification text mandatory where flag requires it

### Calculations
- Rate per sq. m = bid / site area
- Deviation from layout average %

### Workflow
Evaluated → Flag raised → Justified

### Search Requirements
- Flagged results by type and auction

### Documents
- None

### Reports
- Flagged results report

### Notifications
- None (shown in queues)

### Security
- Visible to verifiers, approvers and management

### Integrations
- None

### Dependencies
- F02-003
- F03-001
- F04-001

### Assumptions
- Default history available from Module data and migration

### Risks
- False positives if thresholds are not tuned

### Non Functional Requirements
- Flag evaluation under 1 second per site

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Flags panel on workbench | Easy | 4 |
| UI | Flag justification dialog | Simple | 2 |
| UI | Flagged results report screen | Medium | 6 |
| API | Evaluate flags for result | Complex | 8 |
| API | Compute layout averages | Medium | 6 |
| API | Check bidder default history | Medium | 6 |
| API | Save flag justification | Easy | 4 |
| API | List flagged results | Easy | 4 |
| API | Re-evaluate on re-import | Easy | 4 |
| Database | Flag register | Easy | 2 |
| Testing | Flag rule tests with boundary values | Medium | 6 |
| Testing | Bidder history matching tests | Medium | 6 |
| Documentation | Flag definitions reference | Easy | 2 |

**Feature Total: 60 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 32 | 2 | 0 | 12 | 2 | **60** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Rule engine reuses F02-003 evaluation
- No external integration channel in this feature; Integration row omitted.
