# Auction Management System — Module List

Source: SoW_AUCTION_Detailed.md (production Statement of Work). Original draft `STATEMENT OF WORK AUCTION.docx` was not modified. Module numbers and feature identifiers are taken from that Statement of Work and are not renumbered.

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Staff Access and Role Management | Shared | Named staff accounts, roles, and departments for every later staff action | Derived from the role table; required to implement the named roles |
| 02 | Category and Catalogue Management | Business | Reusable categories, dynamic fields, and catalogue items selected into auctions | Explicit — Category / Catalogue Management |
| 03 | Bidder Registration and Profile | Business | Bidder onboarding, verification, login, and master profile documents | Explicit — Bidder Registration & Login |
| 04 | Auction Creation | Business | Six-step draft covering rules, commercial parameters, items, documents, schedule, and submit | Explicit — Auction Creation |
| 05 | Auction Review, Approval and Publication | Business | Review, send-back or approval, notice number, and publication | Explicit — Auction Review & Approval; Auction Publication |
| 06 | Corrigendum Management | Business | Sequential correction of a published auction, approved and published for bidders | Explicit — Corrigendum Management |
| 07 | Auction Discovery and Participation | Business | Bidder search, participation, EMD fulfilment, and participation documents | Explicit — Search & Details; EOI; EMD; Participation Documents |
| 08 | Pre-Auction Query and Clarification | Business | Bidder questions and departmental clarifications inside the query window | Explicit — Pre-Auction Query / Clarification |
| 09 | Pre-Live Participation Evaluation | Business | Eligibility decisions and approved accepted list when Evaluation = Yes | Explicit — Pre-Live Participation Evaluation |
| 10 | Live Auction Bidding and Extension | Business | Eligible live bidding, validation, masking, and delta-time extension | Explicit — Live Auction Bidding; bid validation; Delta Time |
| 11 | Live Auction Monitoring and Closure | Business | Authority monitoring, force close, and scheduled closure | Explicit — Live Auction Monitoring; Force Close; Auction Closure |
| 12 | Results, Finalisation and Approval | Business | Direction-based ranking, successful-bidder selection, and finalisation approval | Explicit — Result & Ranking; Bidder Finalisation; Finalisation Approval |
| 13 | Award and Letter of Intent | Business | Award decision, Letter of Intent, successful-bidder advice, and completion | Explicit — Auction Awarding; Letter of Intent |
| 14 | Notifications | Technical | In-portal and email alerts for the named lifecycle events | Explicit — Notifications |
| 15 | Auction Status and History | Business | Current stage and trace of the auction from draft through completion | Explicit — Auction Status & History |

## Module Details

### 01. Staff Access and Role Management

- **Type:** Shared
- **Summary:** Administer staff who run the catalogue, auctions, evaluation, monitoring, finalisation, and award.
- **Source:** Derived from the role-wise responsibility table. The source names the roles and does not describe staff account administration. Bidder login is Module 03, not this module.
- **In Scope:** Staff user accounts; activation and deactivation; assignment of the staff roles in the Statement of Work; department master; association of a staff user to a department; staff sign-in and session end. Feature identifiers: F01-001, F01-002, F01-003, F01-004.
- **Out of Scope:** Bidder registration and bidder login. Post, position, or reporting-line hierarchy. External identity provider.
- **Key Actors:** System / Catalogue Administrator (maker for accounts, roles, and departments). Each staff role is a consumer of the resulting permission.
- **Dependencies:** None. All later staff modules depend on this module.
- **Notes:** Access model is User → Role → Permissions, with Department as an attribute. System / Catalogue Administrator is cross-department. Other staff roles work on auctions of their department.

### 02. Category and Catalogue Management

- **Type:** Business
- **Summary:** Maintain the reusable item master that auction creation selects from.
- **Source:** Explicit in the Statement of Work, Module 02, from source Category / Catalogue Management.
- **In Scope:** Category tree; image, video, and geo-location requirements; reusable text, number, date, select, and boolean fields; select-field options; category–field mapping with required flag and display order; dynamic catalogue item capture, media, location, activation, and search. Feature identifiers: F02-001 through F02-005.
- **Out of Scope:** Editing a catalogue item from inside an auction. Auction-specific documents. A separate document-management product.
- **Key Actors:** System / Catalogue Administrator.
- **Dependencies:** Module 01.
- **Notes:** Only active items can be selected in Module 04. Selection must not write back to the catalogue master. Inactive categories and options are not offered for new mapping or new items.

### 03. Bidder Registration and Profile

- **Type:** Business
- **Summary:** Open and verify bidder accounts and hold organisation profile and master documents.
- **Source:** Explicit — Bidder Registration & Login.
- **In Scope:** Self-registration; staff verification (activate or reject); bidder sign-in; profile, organisation, contact, and master documents. Feature identifiers: F03-001 through F03-004.
- **Out of Scope:** Participation, EMD, and live bidding (Modules 07 and 10). Payment of any fee. External KYC bureau.
- **Key Actors:** Bidder (maker of registration and profile). System / Catalogue Administrator or the staff role the organisation designates (verifier).
- **Dependencies:** Module 01 for the verifier’s staff account.
- **Notes:** An inactive or rejected bidder cannot participate or bid. Profile documents do not replace auction-specific participation documents unless a participation rule explicitly accepts a named profile document.

### 04. Auction Creation

- **Type:** Business
- **Summary:** Guided draft through which the creator defines and submits an auction.
- **Source:** Explicit — Auction Creation, including parameter, item, document, schedule, and review steps.
- **In Scope:** Title, department, description, forward or reverse direction, direct / prequalified / restricted bid type, open or restricted procedure, display flags, evaluation flag, prequalified or restricted bidder list, item-wise or lot-wise structure, GST pricing format, common / item-wise / lot-wise EMD, bid-change price, reserve price amount, catalogue selection and lot arrangement, supporting documents (PDF, DOC, XLS, JPG, PNG, 70 MB), schedule sequence, delta of 15 or 30 minutes, next-day cutoff, draft save, and submit. Feature identifiers: F04-001 through F04-006.
- **Out of Scope:** Approval and publication (Module 05). Live bidding. GST tax calculation. Automatic reserve-price rejection. Payment gateway.
- **Key Actors:** Auction Creator.
- **Dependencies:** Modules 01, 02, and 03 (active bidders for a closed list).
- **Notes:** The auction remains draft until submit. Evaluation = Yes / No is stored here and consumed by Modules 09 and 10. Bid-change price and reserve amount are included because later validation and display require them; see Statement of Work assumptions.

### 05. Auction Review, Approval and Publication

- **Type:** Business
- **Summary:** Decide a submitted auction and publish the approved auction under a notice number.
- **Source:** Explicit — Auction Review & Approval and Auction Publication, consolidated because publication is the next mandatory step after approval and is not a separate business domain.
- **In Scope:** Review inbox; full verification of items, parameters, documents, and schedules; approve or send back; resubmission after return; auction notice number; publication to eligible bidders. Feature identifiers: F05-001, F05-002.
- **Out of Scope:** Corrigendum after publication (Module 06). Editing catalogue masters during review.
- **Key Actors:** Reviewing / Approving Authority. Auction Creator receives a return.
- **Dependencies:** Module 04.
- **Notes:** Bidders cannot see the auction before publication. Send-back returns the auction to the creator as a correctable draft.

### 06. Corrigendum Management

- **Type:** Business
- **Summary:** Issue a numbered, approved correction to a published auction.
- **Source:** Explicit — Corrigendum Management.
- **In Scope:** Draft corrigendum, sequential number, approval, publication, and bidder read. Feature identifiers: F06-001, F06-002.
- **Out of Scope:** Changing the original auction by silent edit after publication. Bidder participation itself.
- **Key Actors:** Authorised staff user (Auction Creator or Reviewing / Approving Authority, as the organisation assigns). Bidder (read published corrigendum only).
- **Dependencies:** Module 05 (auction must be published).
- **Notes:** Approval before publication is applied for every corrigendum, per the Statement of Work assumption. Unpublished drafts are hidden from bidders.

### 07. Auction Discovery and Participation

- **Type:** Business
- **Summary:** Bidder finds a published auction and completes participation, EMD fulfilment, and required documents.
- **Source:** Explicit — Auction Search, Details and Participation; Expression of Interest; EMD Management; Participation Documents. Consolidated because the source treats them as one participation path.
- **In Scope:** Search and filters; auction detail; participation inside the window; participation status; common, item-wise, or lot-wise EMD fulfilment with reference and proof; participation document checklist and upload. Feature identifiers: F07-001 through F07-004.
- **Out of Scope:** Payment gateway, EMD refund, and EMD forfeiture. Pre-live evaluation (Module 09). Queries (Module 08).
- **Key Actors:** Bidder. Evaluation Authority is a reader of participation documents and EMD status.
- **Dependencies:** Modules 03 and 05. Uses EMD and schedule configuration from Module 04.
- **Notes:** Closed lists from prequalified or restricted auctions are enforced here. Incomplete EMD blocks the next stage.

### 08. Pre-Auction Query and Clarification

- **Type:** Business
- **Summary:** Questions and answers on a published auction during the query period.
- **Source:** Explicit — Pre-Auction Query / Clarification. Kept as its own module because the department response is a separate workflow from participation submission.
- **In Scope:** Bidder query, department clarification, association of both to the auction, deadline inside the participation / query period. Feature identifier: F08-001.
- **Out of Scope:** Queries after the deadline. Changing auction terms except through a corrigendum (Module 06).
- **Key Actors:** Bidder. Authorised department user (Auction Creator or Reviewing / Approving Authority).
- **Dependencies:** Module 05. Window comes from Module 04.
- **Notes:** A clarification is not itself a corrigendum. If the answer changes auction terms, the organisation issues a corrigendum.

### 09. Pre-Live Participation Evaluation

- **Type:** Business
- **Summary:** Decide the accepted bidder list before live bidding when Evaluation = Yes.
- **Source:** Explicit — Pre-Live Participation Evaluation, including the statement that this happens before the live auction. The Evaluation = No path is a rule of this module and Module 10, not a separate module.
- **In Scope:** Participant list; review of bidder, documents, EMD, eligibility, prequalification, and restricted-list conditions; accepted or rejected decision with remarks; submission and approval of the accepted list. Feature identifiers: F09-001, F09-002.
- **Out of Scope:** Running this stage when Evaluation = No. Post-auction ranking.
- **Key Actors:** Evaluation Authority (maker). Reviewing / Approving Authority (approver of the list). Bidder receives the outcome.
- **Dependencies:** Module 07. Flag from Module 04.
- **Notes:** Only an approved accepted bidder may enter Module 10 when the flag is Yes. Rejected bidders are excluded.

### 10. Live Auction Bidding and Extension

- **Type:** Business
- **Summary:** Take valid live bids and extend the end time under the delta and cutoff rules.
- **Source:** Explicit — Live Auction Bidding, Live Bid Validation, and Delta Time & Auction Extension.
- **In Scope:** Entry for eligible bidders only; forward and reverse; item-wise and lot-wise; bid-change, direction, timing, eligibility, and live-status validation; display of reserve, last accepted bid, and bidder list per flags; identity masking; 15 or 30 minute extension; next-day cutoff; remaining-time display. Feature identifiers: F10-001 through F10-003.
- **Out of Scope:** Monitoring console and force close (Module 11). Ranking (Module 12). Auto-reject for missing a reserve price.
- **Key Actors:** Eligible bidder. Auctioning Authority sees the same remaining time through Module 11.
- **Dependencies:** Modules 04, 07, and 09 (when Evaluation = Yes).
- **Notes:** A rejected validation does not update the current bid. Extension cannot pass the next-day cutoff.

### 11. Live Auction Monitoring and Closure

- **Type:** Business
- **Summary:** Operate the live auction from the authority side and close it.
- **Source:** Explicit — Live Auction Monitoring, Force Close, and Auction Closure.
- **In Scope:** Live status, item or lot status, bidding and participant activity, remaining time, extension and closure information, force close with mandatory reason, scheduled close, and bid freeze with retention of accepted bids. Feature identifiers: F11-001 through F11-003.
- **Out of Scope:** Placing bids. Choosing the successful bidder.
- **Key Actors:** Auctioning Authority.
- **Dependencies:** Module 10.
- **Notes:** Bidders remain masked from each other as configured. Closure, however caused, stops new bids and hands retained bids to Module 12.

### 12. Results, Finalisation and Approval

- **Type:** Business
- **Summary:** Rank closed bids and approve the successful bidder before any award.
- **Source:** Explicit — Auction Result & Bid Ranking, Bidder Finalisation, and Finalisation Approval.
- **In Scope:** H1/H2/H3 or L1/L2/L3 at item or lot level; result review; explicit selection when the top rank is tied; remarks; submit; approve or send back. Feature identifiers: F12-001 through F12-003.
- **Out of Scope:** Award and Letter of Intent (Module 13). Reopening the live auction from this module.
- **Key Actors:** Finalisation Authority (maker). Reviewing / Approving Authority (approver).
- **Dependencies:** Module 11.
- **Notes:** The system does not auto-pick a tied H1 or L1. Award stays blocked until finalisation is approved.

### 13. Award and Letter of Intent

- **Type:** Business
- **Summary:** Award the approved result, issue the Letter of Intent, and complete the auction.
- **Source:** Explicit — Auction Awarding and Letter of Intent. Consolidated because the source flow treats LOI generation as part of awarding.
- **In Scope:** Award review and decision; Letter of Intent tied to auction, notice number, successful bidder, item or lot, and final result; availability to that bidder only; advice to the successful bidder; completion. Feature identifiers: F13-001 through F13-003.
- **Out of Scope:** Contract, purchase order, delivery, and payment after the Letter of Intent. Digital signature service.
- **Key Actors:** Awarding Authority. Successful bidder (reader of the Letter of Intent and recipient of the advice).
- **Dependencies:** Module 12 approval. Module 14 carries the notification.
- **Notes:** Legal template wording is supplied by the organisation. Completion is refused until award, Letter of Intent, and advice are recorded.

### 14. Notifications

- **Type:** Technical
- **Summary:** Deliver the lifecycle events named in the Statement of Work in the portal and by email.
- **Source:** Explicit — Notifications. Implemented as its own module because many business modules raise the same class of alert and email needs a single delivery path.
- **In Scope:** The event list in the Statement of Work (submitted, approved, returned, published, corrigendum published, participation submitted, evaluation completed, accepted, rejected, live commencement, closure, finalisation, award, Letter of Intent, successful-bidder notification, completion); recipient targeting; in-portal list; email send and delivery outcome. Feature identifiers: F14-001, F14-002.
- **Out of Scope:** SMS. Using email failure to reverse a business action.
- **Key Actors:** System on behalf of the business event. Staff and bidders as recipients. Administrator reads delivery outcome.
- **Dependencies:** Business events from Modules 03 through 13. Email service supplied by the organisation.
- **Notes:** A bidder must not receive another bidder’s eligibility decision or Letter of Intent.

### 15. Auction Status and History

- **Type:** Business
- **Summary:** Show the current stage and the trace of what happened.
- **Source:** Explicit — Auction Status & History. Kept as a module because the source requires a complete lifecycle record, not only a technical log.
- **In Scope:** Stage display for the sequence in the Statement of Work appendix, including the evaluation branch and force close; history readable by authorised users; bidder-limited view. Feature identifiers: F15-001, F15-002.
- **Out of Scope:** A free-form status edit. A general audit product covering non-auction masters beyond what each master already records. A reporting warehouse.
- **Key Actors:** Authorised staff. Bidder, for the subset they are allowed to see.
- **Dependencies:** Stage changes produced by Modules 04 through 13.
- **Notes:** History is written by those business actions. This module presents and retains that record.

## Excluded / Embedded Capabilities

| Capability | Treatment |
|------------|-----------|
| Generic workflow engine | Not a module. Approvals sit inside Modules 05, 06, 09, 12, and 13 |
| Document management product | Not a module. Files sit on the catalogue item, bidder profile, auction, participation, corrigendum, and Letter of Intent |
| Payment gateway, EMD refund, EMD forfeiture | Out of scope. EMD fulfilment is inside F07-003 |
| GST calculation | Out of scope. Pricing format is a flag on F04-002 |
| Reserve price as an automatic bid floor | Out of scope. Amount and display flag only |
| Evaluation = No as its own module | Embedded rule. Module 09 does not run; Module 10 admits eligible participants |
| Bid validation as its own module | Feature F10-002 inside live bidding |
| Delta time as its own module | Feature F10-003 |
| Force close as its own module | Feature F11-002 |
| Letter of Intent as its own module | Features F13-002 and F13-003 inside award |
| Search engine product | Not a module. Auction search is F07-001; catalogue search is inside Module 02 and F04-003 |
| Reporting / MIS warehouse | Not a module. Operational views are the monitoring console, ranking, and history |
| API integration hub | Not a module. The only external channel is email on F14-002 |
| Audit log product | Not a module. Auction history is Module 15; account and decision history sit on the owning feature |
| Mobile app, SMS, legacy migration, post-LOI contract | Out of scope in the Statement of Work |
| Staff identity | Module 01, because the source named roles without an administration feature |

## Assumptions

1. Statement of Work assumptions apply, including User → Role plus Department, embedded documents and approvals, EMD as proof rather than a payment, email but not SMS, and both evaluation paths in the go-live scope.
2. Module boundaries follow the Statement of Work. Source areas were consolidated only where the Statement of Work already consolidated them.
3. Corrigendum, evaluation-list, and finalisation approvals use the Reviewing / Approving Authority.
4. No module was added for file storage, job scheduling, or a search service.

## Risks

1. If the organisation later requires a payment gateway or EMD forfeiture, Module 07 and the integration boundary change.
2. If reserve price must reject bids, F04-002 and F10-002 gain a commercial rule that this list does not include.
3. If corrigendum or evaluation approval is waived for some auctions, F06-001 and F09-002 become conditional and the stage sequence changes.
4. Concurrent live bidding and extension timing are a delivery risk inside Module 10; they do not justify a separate module.
5. Unstated bidder and concurrency volumes may affect non-functional sizing without moving module boundaries.
6. Splitting one person across creator, approver, and awarder is a role-assignment choice, not a new module, but weak separation of duties is an operational risk.

## Review checklist

- Every source area maps to a module or to the embedded table.
- Identifiers match the Statement of Work.
- Business, shared, and technical types are separated.
- No hours are assigned in this list.
