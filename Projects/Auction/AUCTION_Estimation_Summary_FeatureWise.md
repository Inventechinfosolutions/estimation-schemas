# Auction Management System — Feature-wise Estimation Summary

Internal feature-wise hours. Person-hours. Go-live is the full total. Optional hours are zero.

**All features:** 2171 hours

**Recommended go-live:** 2171 hours

**Optional / conditional:** 0 hours

## Module-wise summary

| # | Module | Type | Features | Hours | Share of go-live |
|---|--------|------|--------:|------:|-----------------:|
| 01 | Staff Access and Role Management | Shared | 4 | 165 | 7.6% |
| 02 | Category and Catalogue Management | Business | 5 | 246 | 11.3% |
| 03 | Bidder Registration and Profile | Business | 4 | 183 | 8.4% |
| 04 | Auction Creation | Business | 6 | 275 | 12.7% |
| 05 | Auction Review, Approval and Publication | Business | 2 | 104 | 4.8% |
| 06 | Corrigendum Management | Business | 2 | 95 | 4.4% |
| 07 | Auction Discovery and Participation | Business | 4 | 187 | 8.6% |
| 08 | Pre-Auction Query and Clarification | Business | 1 | 59 | 2.7% |
| 09 | Pre-Live Participation Evaluation | Business | 2 | 111 | 5.1% |
| 10 | Live Auction Bidding and Extension | Business | 3 | 175 | 8.1% |
| 11 | Live Auction Monitoring and Closure | Business | 3 | 107 | 4.9% |
| 12 | Results, Finalisation and Approval | Business | 3 | 164 | 7.6% |
| 13 | Award and Letter of Intent | Business | 3 | 129 | 5.9% |
| 14 | Notifications | Technical | 2 | 90 | 4.1% |
| 15 | Auction Status and History | Business | 2 | 81 | 3.7% |
|  | **Total** |  | **46** | **2171** | **100%** |

## Feature-wise tables

### 01. Staff Access and Role Management

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F01-001 | Staff User Accounts | 50 | Named staff accounts and active status for catalogue, auction, and award duties. |
| F01-002 | Role Assignment and Permissions | 57 | Assigns the seven staff roles and enforces them on later actions. |
| F01-003 | Department Master and Staff Department | 24 | Flat department list used on staff accounts, auctions, and bidder search. |
| F01-004 | Staff Login and Session | 34 | Staff sign-in, sign-out, and password reset. Separate from the bidder portal. |

**Module total:** 165 hours

### 02. Category and Catalogue Management

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F02-001 | Category and Sub-category Management | 57 | Category tree plus image, video, and location requirements. |
| F02-002 | Reusable Field Master | 34 | Reusable text, number, date, select, and boolean fields. |
| F02-003 | Field Options for Select Fields | 28 | Ordered, activatable options for select fields only. |
| F02-004 | Category–Field Mapping | 39 | Maps fields to a category with required flag and display order. |
| F02-005 | Catalogue Item Maintenance | 88 | Dynamic catalogue item with media, location, activation, and search. |

**Module total:** 246 hours

### 03. Bidder Registration and Profile

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F03-001 | Bidder Self-Registration | 43 | Bidder submits organisation and contact details and waits for verification. |
| F03-002 | Bidder Account Verification | 57 | Staff verifier activates or rejects a bidder before that bidder can participate. |
| F03-003 | Bidder Login and Session | 26 | Bidder portal sign-in, separate from staff sign-in. |
| F03-004 | Bidder Profile, Organisation and Documents | 57 | Bidder maintains organisation, contacts, and master documents. |

**Module total:** 183 hours

### 04. Auction Creation

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F04-001 | Auction Basic Information and Participation Rules | 53 | Draft header: direction, bid type, display flags, evaluation, and any closed bidder list. |
| F04-002 | Pricing, EMD and Bid Parameters | 41 | Item or lot structure, GST format, EMD type, bid-change price, and reserve amounts. |
| F04-003 | Catalogue Item Selection and Lot Organisation | 61 | Selects active catalogue items and arranges lots without editing the master. |
| F04-004 | Auction Supporting Documents | 30 | Uploads auction papers in the stated formats, up to 70 MB each. |
| F04-005 | Participation and Live Auction Schedule | 39 | Four schedule points, 15 or 30 minute delta, and next-day cutoff. |
| F04-006 | Draft Review and Submit for Approval | 51 | Creator reviews the full draft and submits it for approval. |

**Module total:** 275 hours

### 05. Auction Review, Approval and Publication

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F05-001 | Auction Review and Decision | 63 | Reviewer approves a submitted auction or sends it back with remarks. |
| F05-002 | Auction Notice and Publication | 41 | Assigns the auction notice number and publishes the approved auction. |

**Module total:** 104 hours

### 06. Corrigendum Management

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F06-001 | Corrigendum Draft and Approval | 61 | Drafts a numbered corrigendum and obtains approval before bidders see it. |
| F06-002 | Corrigendum Publication and Bidder Access | 34 | Publishes an approved corrigendum so eligible bidders can read it. |

**Module total:** 95 hours

### 07. Auction Discovery and Participation

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F07-001 | Published Auction Search and Detail | 53 | Bidder searches published auctions and reads the pack they are allowed to see. |
| F07-002 | Expression of Interest and Participation | 43 | Bidder participates in the window and confirms once EMD and documents are complete. |
| F07-003 | EMD Fulfilment | 47 | Records common, item-wise, or lot-wise EMD with reference and proof. No payment gateway. |
| F07-004 | Participation Document Upload | 44 | Bidder files the auction’s required participation documents for evaluation staff to read. |

**Module total:** 187 hours

### 08. Pre-Auction Query and Clarification

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F08-001 | Pre-auction Query and Clarification | 59 | Bidder asks, and the department posts a clarification on the auction before the deadline. |

**Module total:** 59 hours

### 09. Pre-Live Participation Evaluation

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F09-001 | Participation Evaluation and Eligibility Decision | 74 | Evaluator marks each confirmed participant accepted or rejected before the live auction. |
| F09-002 | Accepted Bidder List Approval | 37 | Approves the accepted-bidder list that gates the live auction. |

**Module total:** 111 hours

### 10. Live Auction Bidding and Extension

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F10-001 | Live Bid Submission | 84 | Eligible bidder submits item or lot bids in a forward or reverse live auction. |
| F10-002 | Live Bid Validation and Visibility | 56 | Accepts or rejects a live bid against direction, change, time, and eligibility, and applies display masks. |
| F10-003 | Delta Time Extension and Next-day Cutoff | 35 | Extends the live end by 15 or 30 minutes on a late accepted bid, and stops at the next-day cutoff. |

**Module total:** 175 hours

### 11. Live Auction Monitoring and Closure

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F11-001 | Live Auction Monitoring Console | 52 | Authority view of live status, items, activity, remaining time, and extensions. |
| F11-002 | Authorised Force Close | 24 | Authority closes a live auction early, with a mandatory reason. |
| F11-003 | Scheduled Closure and Bid Freeze | 31 | Closes the auction at the effective end and freezes accepted bids for ranking. |

**Module total:** 107 hours

### 12. Results, Finalisation and Approval

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F12-001 | Item and Lot Bid Ranking | 60 | Ranks closed bids H1/H2/H3 or L1/L2/L3 per item or lot, and leaves ties unbroken. |
| F12-002 | Successful Bidder Finalisation | 59 | Selects the successful bidder per item or lot, including an explicit choice when the top rank is tied. |
| F12-003 | Finalisation Approval | 45 | Approves the successful-bidder selection or sends it back before award. |

**Module total:** 164 hours

### 13. Award and Letter of Intent

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F13-001 | Award Review and Approval | 47 | Records the award once finalisation is approved. No contract or payment. |
| F13-002 | Letter of Intent Generation | 54 | Generates the Letter of Intent from the awarded result for the successful bidder only. |
| F13-003 | Auction Completion and Successful-bidder Advice | 28 | Advises the successful bidder and marks the auction complete after the letter is issued. |

**Module total:** 129 hours

### 14. Notifications

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F14-001 | Lifecycle Notification Events and In-portal Alerts | 45 | In-portal alerts for the auction lifecycle events, targeted to the right person. |
| F14-002 | Email Delivery of Auction Notifications | 45 | Emails the lifecycle alerts and records whether delivery succeeded. |

**Module total:** 90 hours

### 15. Auction Status and History

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F15-001 | Auction Lifecycle Status | 36 | Shows the current auction stage, including the evaluation branch and force close. |
| F15-002 | Auction History for Authorised Users | 45 | Staff trace the auction from draft to completion. Bidders see only their own allowed events. |

**Module total:** 81 hours

## Optional commercial line items

None. Payment gateway, SMS, mobile applications, and post-award contract management are out of scope rather than optional priced lines.

## Effort profile

Largest features:

- F02-005 Catalogue Item Maintenance (Category and Catalogue Management): 88 hours
- F10-001 Live Bid Submission (Live Auction Bidding and Extension): 84 hours
- F09-001 Participation Evaluation and Eligibility Decision (Pre-Live Participation Evaluation): 74 hours
- F05-001 Auction Review and Decision (Auction Review, Approval and Publication): 63 hours
- F06-001 Corrigendum Draft and Approval (Corrigendum Management): 61 hours
- F04-003 Catalogue Item Selection and Lot Organisation (Auction Creation): 61 hours
- F12-001 Item and Lot Bid Ranking (Results, Finalisation and Approval): 60 hours
- F12-002 Successful Bidder Finalisation (Results, Finalisation and Approval): 59 hours
- F08-001 Pre-auction Query and Clarification (Pre-Auction Query and Clarification): 59 hours
- F03-004 Bidder Profile, Organisation and Documents (Bidder Registration and Profile): 57 hours

Hours by type:

- Shared: 165 hours (7.6%)
- Business: 1916 hours (88.3%)
- Technical: 90 hours (4.1%)

## Indicative phasing

Single phase, matching the Statement of Work. Modules 01 through 15 are the go-live scope, including both evaluation paths, forward and reverse auctions, item and lot structure, corrigendum, delta time, force close, ranking, award, and Letter of Intent.

Build order follows the module numbers: access and catalogue, bidder onboarding, auction draft and publication, participation, evaluation, live bidding, closure, finalisation, award, notifications, and history.

## Exclusions

- Payment gateway, EMD refund, and EMD forfeiture
- Contract, purchase order, delivery, invoicing, and settlement after the Letter of Intent
- SMS, native mobile applications, and a public unauthenticated bidding channel
- Legacy data migration
- GST computation, multi-currency, digital signature, and ERP posting
- Automatic rejection of bids that miss the reserve price
- Hosting, infrastructure, training delivery beyond operating documentation, and annual maintenance
