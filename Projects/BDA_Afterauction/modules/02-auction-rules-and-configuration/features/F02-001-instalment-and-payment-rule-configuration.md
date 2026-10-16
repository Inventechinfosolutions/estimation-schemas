# F02-001 — Instalment & Payment Rule Configuration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-001 |
| Feature Name | Instalment & Payment Rule Configuration |
| Module | 02 — Auction Rules & Configuration |
| Module Type | Business |
| Release | Go-live |

### Description
Versioned, effective-dated configuration of the instalment structure and payment rules: number of instalments, percentage of each, due period and trigger event, EMD adjustment, grace period, interest on delayed payment, penalty, maximum extension, default threshold and forfeiture percentage, applicable by auction or layout.

### Business Objective
Allow BDA to change payment rules for new auctions without code changes, while cases already awarded continue under the rule version in force on their award date.

### Actors
- Auction Admin
- Approving Authority (rule approval)
- Finance Officer (view)

### User Journey
1. **Who creates:** The Auction Admin creates a payment rule set; default rule set (25% / 50% / 25%) is seeded.
2. **How they create:** The Auction Admin opens Payment Rules, clicks New Version, enters instalments, percentages, triggers and due periods, EMD adjustment, interest, penalty and default settings, and the effective-from date, then saves as draft.
3. **How they edit:** The Auction Admin edits the draft; a simulator shows the resulting schedule for a sample bid amount.
4. **How they send for approval:** The Auction Admin submits the draft for approval.
5. **How the approver sees pending items:** The Approving Authority sees pending rule versions in My Approvals with a comparison against the active version.
6. **How the approver decides:** The Approving Authority approves (version becomes active on the effective date) or returns with remarks.
7. **How the applicant / maker sees history:** The Auction Admin sees the version list with status and the auctions / sites each version applies to.
8. **How the approver / auditor sees history:** The Finance Officer and auditors see all versions, approvals and the rule applied to each case.

### Functional Capabilities
- Instalment definition: sequence, percentage of bid amount, trigger (intimation date, previous instalment, draft deed approval), due period in days
- EMD adjustment: deduct EMD from first instalment or from total (configurable)
- Grace period, simple / compound interest rate per annum for delayed payment
- Penalty amount or percentage after grace period
- Extension limits: maximum number and maximum days per instalment
- Default threshold (days overdue) and forfeiture percentage of amount paid
- Rounding rules (nearest rupee)
- Applicability by auction, layout or all; effective-from date
- Schedule simulator for a sample bid and EMD
- Version history, comparison and approval
- Rule version stamped on each case at award

### UI Screens
- Payment rule versions list
- Rule editor: instalments and triggers
- Rule editor: interest, penalty, extension and default
- Schedule simulator
- Version comparison
- Rule approval screen

### Logical API Operations
- Create / edit rule draft
- Validate rule consistency
- Simulate schedule
- Submit / approve / return rule version
- Resolve applicable rule for a case
- Compare versions
- List versions and applicability

### Inputs
- Instalment rows (percentage, trigger, due days)
- EMD adjustment mode
- Interest rate, grace days, penalty
- Extension and default limits
- Applicability and effective date

### Outputs
- Approved rule version
- Simulated schedule
- Rule stamped on each case

### Business Rules
- Instalment percentages must total 100%
- An active version cannot be edited; changes create a new version
- Cases keep the rule version stamped at award; later versions do not apply retrospectively
- Effective-from date cannot be in the past
- Only one active version per applicability scope on a date

### Validations
- Percentages 0–100 with two decimals
- Due days positive integers
- Interest and penalty within configured caps
- No overlapping effective periods

### Calculations
- Instalment amount = bid amount × percentage, EMD adjusted per mode, rounded to rupee
- Interest = overdue amount × rate × overdue days / 365

### Workflow
Draft → Submitted → Approved (Scheduled) → Active → Superseded; Returned → Draft

### Search Requirements
- Rule versions by status, scope, effective date

### Documents
- Government order / BDA resolution reference attached to version

### Reports
- Active rules by auction / layout
- Rule change history

### Notifications
- Approval request and decision alerts

### Security
- Only Auction Admin edits; only Approving Authority approves

### Integrations
- None

### Dependencies
- Used by F06-001, F06-006, F06-007, F06-008

### Assumptions
- BDA confirms default rule values in SRS

### Risks
- Rule changes mid-auction causing disputes; mitigated by version stamping

### Non Functional Requirements
- Schedule simulation under 1 second

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Payment rule versions list | Easy | 4 |
| UI | Rule editor: instalments and triggers | Complex | 12 |
| UI | Rule editor: interest, penalty, extension and default | Medium | 6 |
| UI | Schedule simulator | Medium | 6 |
| UI | Version comparison | Medium | 6 |
| UI | Rule approval screen | Easy | 4 |
| API | Create / edit rule draft | Medium | 6 |
| API | Validate rule consistency | Medium | 6 |
| API | Simulate schedule | Medium | 6 |
| API | Submit / approve / return rule version | Medium | 6 |
| API | Resolve applicable rule for a case | Complex | 8 |
| API | Compare versions | Easy | 4 |
| API | List versions and applicability | Easy | 4 |
| Database | Payment rule set and versions | Medium | 4 |
| Database | Rule applicability mapping | Easy | 2 |
| Testing | Rule validation and applicability tests | Medium | 6 |
| Testing | Simulator and schedule calculation tests | Complex | 8 |
| Testing | Versioning and approval tests | Easy | 4 |
| Documentation | Payment rule configuration guide | Medium | 3 |

**Feature Total: 105 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 38 | 40 | 6 | 0 | 18 | 3 | **105** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Rule resolution for a case is Complex because of scope and effective date precedence
- No external integration channel in this feature; Integration row omitted.
