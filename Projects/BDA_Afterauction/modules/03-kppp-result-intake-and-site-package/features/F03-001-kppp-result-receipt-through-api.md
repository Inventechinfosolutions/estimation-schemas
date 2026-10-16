# F03-001 — KPPP Result Receipt through API

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-001 |
| Feature Name | KPPP Result Receipt through API |
| Module | 03 — KPPP Result Intake & Site Package |
| Module Type | Business |
| Release | Go-live |

### Description
Automated receipt of auction results from the KPPP e-Auction module through API (push or scheduled pull), creating one awarded site record per auctioned site with auction ID, site number, layout, upset price, highest bid, highest bidder, bidder count, bid history summary and closure time, with idempotency and acknowledgement.

### Business Objective
Eliminate manual re-entry of results and start the post-auction process within one hour of auction closure.

### Actors
- System (integration)
- Auction Admin (monitoring)

### User Journey
1. **Who creates:** The system creates awarded site records automatically from KPPP; no user creates them manually on this route.
2. **How they create:** On auction closure KPPP pushes results (or the scheduler pulls them); the connector validates the payload and creates the records in Received status.
3. **How they edit:** Records cannot be edited; corrections come only through versioned re-import (F03-005).
4. **How they send for approval:** Received records are passed automatically to matching (F03-003) and then to the verification queue (F04-001).
5. **How the approver sees pending items:** The Auction Admin sees each import batch with counts (received, created, duplicate, failed) on the Intake Dashboard.
6. **How the approver decides:** The Auction Admin does not approve imports; failed or exception records are resolved in F03-003 or retried from the error queue.
7. **How the applicant / maker sees history:** The Auction Admin sees the history of batches and payload references for each auction.
8. **How the approver / auditor sees history:** Auditors see each payload hash, receipt time, acknowledgement and record creation in the audit trail.

### Functional Capabilities
- Inbound API endpoint for KPPP push with signed request validation
- Scheduled pull by auction ID or date range where push is not available
- Payload schema validation and mapping to awarded site records
- Idempotency by KPPP auction ID + site ID + result version
- Acknowledgement to KPPP with created / rejected counts
- Storage of raw payload with SHA-256 hash for evidence
- Batch summary and alerts on failures
- Bidder details captured: name, KPPP bidder ID, mobile, e-mail, address, PAN (masked), EMD paid
- Bid summary: upset price, highest bid, number of bidders, number of bids, closure time

### UI Screens
- Intake dashboard with batch list
- Batch detail with record-level status
- Raw payload and hash view
- Manual pull by auction ID

### Logical API Operations
- Receive KPPP result push
- Scheduled pull from KPPP
- Validate and map result payload
- Create awarded site records idempotently
- Send acknowledgement to KPPP
- Store raw payload with hash
- List batches and records
- Retry failed batch

### Inputs
- KPPP result payload (auction, sites, bids, bidders)
- Auction ID for manual pull

### Outputs
- Awarded site records
- Batch summary
- Acknowledgement to KPPP
- Stored payload with hash

### Business Rules
- A site result is created once per result version; duplicates are ignored and reported
- Results arriving for an auction already locked go to re-import control (F03-005)
- Only closed auctions are accepted
- Raw payloads are retained for the record retention period

### Validations
- Schema conformance
- Mandatory fields present (auction ID, site ID, highest bid, bidder ID)
- Highest bid ≥ upset price unless flagged
- Signature / token valid

### Calculations
- Premium = highest bid − upset price; premium % = premium / upset price × 100

### Workflow
Received → Validated → Created (to matching) | Failed (error queue)

### Search Requirements
- Batches by auction ID, date, status

### Documents
- Raw payload JSON / XML retained as evidence

### Reports
- Import batch summary report

### Notifications
- Alert to Auction Admin on batch failure or partial import
- Notice of new results to Result Verifiers

### Security
- Mutual authentication / signed tokens with KPPP
- IP allow-listing
- Payload hash stored for integrity

### Integrations
- KPPP e-Auction module

### Dependencies
- F13-001
- F13-002
- F03-003
- F14-001

### Assumptions
- KPPP provides a result API with documented schema; if not, F03-002 is used

### Risks
- KPPP API availability and schema changes outside BDA control

### Non Functional Requirements
- Import within 1 hour of auction closure
- Handles 1,000 sites per batch

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Intake dashboard with batch list | Medium | 6 |
| UI | Batch detail with record-level status | Medium | 6 |
| UI | Raw payload and hash view | Easy | 4 |
| UI | Manual pull by auction ID | Easy | 4 |
| API | Receive KPPP result push | Complex | 8 |
| API | Scheduled pull from KPPP | Complex | 8 |
| API | Validate and map result payload | Complex | 8 |
| API | Create awarded site records idempotently | Complex | 8 |
| API | Send acknowledgement to KPPP | Medium | 6 |
| API | Store raw payload with hash | Easy | 4 |
| API | List batches and records | Easy | 4 |
| API | Retry failed batch | Medium | 6 |
| Database | Awarded site record (core case entity) | Complex | 6 |
| Database | Import batch and raw payload store | Medium | 4 |
| Database | Bidder snapshot from KPPP | Medium | 4 |
| Integration | KPPP e-Auction result API connector (push and pull) | Complex | 24 |
| Testing | API contract tests with KPPP sample payloads | Complex | 8 |
| Testing | Idempotency, retry and failure tests | Medium | 6 |
| Testing | Load test for large auctions (500+ sites) | Medium | 6 |
| Documentation | KPPP interface specification | Medium | 3 |
| Documentation | Intake operations guide | Easy | 2 |

**Feature Total: 135 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 52 | 14 | 24 | 20 | 5 | **135** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- One Complex integration row for the KPPP connector built on the F13-001 framework
