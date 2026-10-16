# F02-003 — Approval Hierarchy & Bid Threshold Configuration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-003 |
| Feature Name | Approval Hierarchy & Bid Threshold Configuration |
| Module | 02 — Auction Rules & Configuration |
| Module Type | Business |
| Release | Go-live |

### Description
Configuration of the multi-level result approval hierarchy (e.g., Verifier → Secretary → Commissioner → Government) based on case criteria such as bid value, premium percentage, single-bidder flag and site category, together with thresholds that define an abnormal bid.

### Business Objective
Implement BDA's delegation of financial powers without code changes and ensure high-value or unusual results go to the right authority.

### Actors
- Auction Admin
- Approving Authority (approval of configuration)

### User Journey
1. **Who creates:** The Auction Admin defines approval matrices and thresholds.
2. **How they create:** The Auction Admin opens Approval Hierarchy, adds a rule with conditions (bid value range, premium %, single bidder, category) and the ordered list of approval levels with role and signing requirement, and saves as draft.
3. **How they edit:** The Auction Admin edits the draft and uses the rule tester to see which chain a sample result would follow.
4. **How they send for approval:** The Auction Admin submits the configuration for approval.
5. **How the approver sees pending items:** The Approving Authority sees pending configuration changes in My Approvals.
6. **How the approver decides:** The Approving Authority approves or returns with remarks.
7. **How the applicant / maker sees history:** The Auction Admin sees active and past versions.
8. **How the approver / auditor sees history:** Auditors see which configuration version routed each result.

### Functional Capabilities
- Approval levels master (level name, role, DSC required, SLA days)
- Rule conditions: bid value range, premium over upset price %, single-bidder flag, site category, layout
- Ordered approval chain per rule, including referral to Government
- Abnormal bid thresholds: premium above / below %, bid below upset price, outlier versus layout average
- Rule priority and default rule
- Rule tester with sample inputs
- Versioning and approval

### UI Screens
- Approval levels master
- Approval rule editor with conditions
- Abnormal bid threshold settings
- Rule tester
- Version list and approval

### Logical API Operations
- Maintain approval levels
- Save approval rule draft
- Save thresholds
- Test rule against sample
- Approve / return configuration
- Resolve approval chain for a result
- Evaluate abnormal bid thresholds

### Inputs
- Levels
- Conditions
- Chain order
- Threshold values
- Priority

### Outputs
- Active configuration
- Resolved approval chain per result
- Threshold evaluation

### Business Rules
- Every result must match at least the default rule
- Higher priority rule wins when several match
- A chain must end at a level with final approval power
- Configuration in force when the result is submitted is stamped on the result

### Validations
- Ranges non-overlapping within the same priority
- At least one level per chain

### Calculations
- Premium % = (bid − upset price) / upset price × 100

### Workflow
Draft → Submitted → Active → Superseded

### Search Requirements
- Rules by condition and level

### Documents
- Delegation of powers order reference

### Reports
- Approval matrix export

### Notifications
- Approval request and outcome

### Security
- Only Auction Admin edits

### Integrations
- None

### Dependencies
- F04-002
- F04-003

### Assumptions
- BDA provides its delegation of financial powers

### Risks
- Incorrect thresholds route results to the wrong authority; mitigated by tester and approval

### Non Functional Requirements
- Chain resolution under 200 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Approval levels master | Easy | 4 |
| UI | Approval rule editor with conditions | Complex | 12 |
| UI | Abnormal bid threshold settings | Medium | 6 |
| UI | Rule tester | Medium | 6 |
| UI | Version list and approval | Easy | 4 |
| API | Maintain approval levels | Easy | 4 |
| API | Save approval rule draft | Medium | 6 |
| API | Save thresholds | Easy | 4 |
| API | Test rule against sample | Medium | 6 |
| API | Approve / return configuration | Easy | 4 |
| API | Resolve approval chain for a result | Complex | 8 |
| API | Evaluate abnormal bid thresholds | Medium | 6 |
| Database | Approval levels, rules and thresholds with versions | Medium | 4 |
| Testing | Chain resolution tests across conditions | Complex | 8 |
| Testing | Threshold evaluation tests | Medium | 6 |
| Documentation | Approval hierarchy configuration guide | Easy | 2 |

**Feature Total: 90 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 38 | 4 | 0 | 14 | 2 | **90** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Condition evaluation engine rated Complex
- No external integration channel in this feature; Integration row omitted.
