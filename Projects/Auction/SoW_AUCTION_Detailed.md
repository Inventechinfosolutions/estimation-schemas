# Statement of Work

# Auction Management System

**Document Type:** Statement of Work — Business and Functional Requirements  
**Version:** 1.0  
**Status:** Draft for review  
**Project code:** AUCTION  
**Source:** Auction Management System — Functional Scope Statement of Work  
**Prepared for:** RFP discussion and delivery estimation

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Project Objectives](#3-project-objectives)
4. [In Scope / Out of Scope](#4-in-scope--out-of-scope)
5. [Solution Expectations](#5-solution-expectations)
6. [Consolidated Functional Modules](#6-consolidated-functional-modules)
7. [End-to-End Workflows](#7-end-to-end-workflows)
8. [Access Control](#8-access-control)
9. [Channels](#9-channels)
10. [Integrations](#10-integrations)
11. [Audit, Compliance and Security](#11-audit-compliance-and-security)
12. [Non-Functional Requirements](#12-non-functional-requirements)
13. [Data Migration](#13-data-migration)
14. [Phased Delivery](#14-phased-delivery)
15. [Deliverables](#15-deliverables)
16. [Acceptance Criteria](#16-acceptance-criteria)
17. [Expected Benefits](#17-expected-benefits)
18. [Assumptions and Dependencies](#18-assumptions-and-dependencies)
19. [Vendor Response Expectations](#19-vendor-response-expectations)
20. [Appendix A — Module and Feature Index](#20-appendix-a--module-and-feature-index)
21. [Appendix B — Role Responsibilities](#21-appendix-b--role-responsibilities)
22. [Appendix C — Auction Stage Record](#22-appendix-c--auction-stage-record)
23. [Appendix D — Document Types](#23-appendix-d--document-types)
24. [Appendix E — Consolidation Map](#24-appendix-e--consolidation-map)

---

## 1. Introduction

This Statement of Work defines the business and functional scope of the **Auction Management System**. It restates the source functional scope as the baseline for RFP discussion and delivery planning.

The system covers the auction lifecycle from reusable catalogue preparation through auction creation, review, publication, bidder participation, optional pre-live evaluation, live bidding, monitoring, closure, ranking, bidder finalisation, award, Letter of Intent, and completion.

The source corrects an earlier process error. **Evaluation is not a post-auction activity.** When Evaluation is set to Yes during auction creation, participation evaluation happens after participation, earnest money deposit (EMD) and document submission, and **before** the live auction. Only bidders accepted as eligible may enter live bidding. When Evaluation is set to No, that pre-live stage is skipped and eligible participants proceed to live bidding under the auction’s participation rules.

This document does not prescribe a technology stack, interface contracts, data structures, or screen layouts.

Document handling (catalogue media, auction papers, participation papers, corrigendum papers, and the Letter of Intent) and approval handling (auction approval, corrigendum approval, evaluation-list approval, finalisation approval, and award approval) are **embedded in the business processes** below. They are not separate document-management or workflow products.

---

## 2. Project Overview

The sponsoring organisation needs one system in which authorised staff prepare what may be auctioned, configure each auction, obtain approval, publish it, and run it through to award. Registered bidders discover published auctions, participate on the published terms, and — when eligible — bid while the live auction is open.

Two live-auction directions are required:

- **Forward auction** — ranking favours the highest valid bid (H1, H2, H3, and so on).
- **Reverse auction** — ranking favours the lowest valid bid (L1, L2, L3, and so on).

Two commercial structures are required:

- **Item-wise** — bidders bid separately on each selected catalogue item.
- **Group / lot-wise** — items are bundled into lots, and bidding is on the lot.

Participation may be **Direct** (open to eligible bidders), **Prequalified** (only prequalified bidders), or **Restricted** (limited participation). Procedure visibility may be **Open** (visible to eligible bidders) or **Restricted** (participation is limited).

A published auction may be corrected by a numbered **corrigendum**. Live auctions may extend automatically by a configured **delta time** (15 or 30 minutes) when a qualifying bid arrives near closure, subject to a **next-day continuation cutoff**. An authorised auctioning authority may **force close** an active auction with a recorded reason.

### 2.1 Business context

| Aspect | Description |
| ------ | ----------- |
| System | Auction Management System |
| Primary outcome | A controlled path from catalogue item to published auction, live result, approved successful bidder, and Letter of Intent |
| Staff users | Catalogue administration, auction creation, review and approval, evaluation, live monitoring, finalisation, and award |
| External users | Registered and verified bidders |
| Critical control | Evaluation = Yes gates live bidding; Evaluation = No does not |
| Commercial end state | Award, Letter of Intent, successful-bidder notification, and auction completion |

### 2.2 Guiding principles

1. The catalogue master is reusable. Selecting an item for an auction does not change the catalogue master.
2. An auction stays in draft until the creator submits it for approval.
3. Bidders see a published auction, its documents, and the latest applicable corrigendum according to eligibility and display rules.
4. Live bidding is limited to bidders who are eligible for that auction at the moment the live stage opens.
5. Bidder identity is masked from other bidders when the auction is configured that way.
6. After closure, no further bids are accepted. Final accepted bids are retained for ranking and award.
7. Award and Letter of Intent follow the approved finalisation. The auction is not complete until that path is finished and recorded.
8. Every material stage remains traceable on the auction history.

---

## 3. Project Objectives

1. Maintain categories, category-specific fields, and catalogue items that can be selected into later auctions.
2. Let an auction creator configure direction, bid type, procedure, pricing format, EMD structure, items or lots, documents, schedule, display rules, and the evaluation flag, then submit a complete draft for approval.
3. Let a reviewing authority approve or return the auction, then publish an approved auction under an auction notice number.
4. Issue, approve, and publish corrigenda so bidders always see the latest applicable correction.
5. Register and verify bidders and let them search, read, and participate in auctions they are allowed to see.
6. Collect participation, the configured EMD fulfilment, and required participation documents inside the participation window.
7. When Evaluation = Yes, evaluate participants and admit only the approved eligible list to the live auction.
8. Run forward and reverse live bidding, item-wise or lot-wise, with bid validation, configured visibility, delta-time extension, and next-day cutoff.
9. Let the auctioning authority monitor the live auction and force close it when permitted, with a reason.
10. Rank valid bids, support finalisation including tied top ranks, obtain finalisation approval, award, generate the Letter of Intent, notify the successful bidder, and complete the auction.
11. Notify the responsible people at the lifecycle events named in this SOW, and keep a full stage history.

---

## 4. In Scope / Out of Scope

### 4.1 In scope

- Staff access for the roles in Appendix B, with department as an organisational attribute.
- Category, sub-category, reusable field, field option, category–field mapping, and catalogue item maintenance, including images, video, documents, and geographical location where the category requires them.
- The six-step auction creation path: basic information, parameters, items, documents, schedule, and review, including draft save and submit for approval.
- Auction review, return for correction, approval, auction notice number, and publication.
- Corrigendum creation, numbering, approval where applicable, publication, and bidder viewing.
- Bidder registration, verification, login, profile, organisation and contact details, and bidder master documents.
- Bidder search and auction detail, expression of interest / participation, participation status, EMD fulfilment, and participation document upload.
- Pre-auction queries and departmental clarifications inside the configured query period.
- Pre-live participation evaluation and approval of the accepted bidder list when Evaluation = Yes, and the direct path to live bidding when Evaluation = No.
- Live bidding, bid validation, display of reserve price, last accepted bid, and bidder list according to configuration, masked identity where configured, delta time, and next-day cutoff.
- Live monitoring, force close, and scheduled closure.
- Ranking, successful-bidder finalisation, finalisation approval, award, Letter of Intent, successful-bidder notification, and completion.
- In-application notifications and email for the events listed in this SOW.
- Auction status and a lifecycle history that authorised users can trace.

### 4.2 Out of scope

- Online payment gateway collection, refund, or forfeiture accounting for EMD or for the awarded price. EMD in this SOW is fulfilment against the auction rule (amount, mode or instrument reference, and supporting proof), not a payment-gateway transaction.
- Contract management, purchase order, delivery, invoicing, or settlement after the Letter of Intent.
- A separate document-management product, a generic workflow-engine product, or a reporting-warehouse product.
- SMS, mobile applications, and a public unauthenticated bidding channel.
- Legacy data migration from a previous auction system.
- Multi-currency conversion and a GST computation engine. The pricing format records whether bids are inclusive or exclusive of GST; it does not calculate tax.
- Automatic rejection of a bid solely because it misses an undisclosed reserve. The source requires reserve price to be displayable, not to be an automatic commercial floor.
- Digital signature of the Letter of Intent, e-tender portal integration, and ERP or finance posting.
- Invented business scope beyond the source and the assumptions in Section 18.

---

## 5. Solution Expectations

At business level, the solution is expected to:

1. Offer a staff workspace and a bidder portal over the same auction record.
2. Drive catalogue item capture from the category’s mapped fields, required or optional, in the configured display order.
3. Keep auction creation as a guided draft until submission.
4. Enforce the schedule order: Participation Start, then Participation End, then Live Auction Start, then Live Auction End.
5. Branch the lifecycle on the evaluation flag exactly as Section 7 describes.
6. Accept a live bid only when direction, bid change, item or lot, timing, eligibility, and live status all pass.
7. Extend the live end by the configured delta when a qualifying bid arrives near closure, and stop extension at the next-day continuation cutoff.
8. Produce item-level or lot-level ranking consistent with forward or reverse direction.
9. Refuse award until required finalisation approval is complete.
10. Leave a history entry for each stage in Appendix C.

---

## 6. Consolidated Functional Modules

Modules are numbered in implementation order. Each capability below has a stable feature identifier.

### 01. Staff Access and Role Management

**Purpose:** Give named staff users the roles required to administer the catalogue, create and approve auctions, evaluate participants, monitor live bidding, finalise results, and award, with department as the organisational attribute used on auctions.

**Functional requirements:**

- Create, edit, search, activate, and deactivate staff user accounts.
- Assign one or more of the staff roles in Appendix B. Bidder access is not a staff role; it is Module 03.
- Maintain a department master. A staff user is associated with a department. System / Catalogue Administrator may work across departments. Other staff roles act on auctions of their department unless a later business rule on a specific screen says otherwise.
- Staff sign in with their own credentials and work in a session that ends on sign-out or expiry.
- Permission follows the role. A user without the relevant role cannot create, approve, evaluate, force close, finalise, or award.

**Acceptance criteria:**

- Every staff action in later modules is attributable to an active staff account and an allowed role.
- A deactivated account cannot sign in.
- Department is available as a selection on auction creation and as a filter on auction search.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Staff user accounts | Authorised administrator creates and maintains named staff accounts and their active status |
| F01-002 | Role assignment and permissions | Administrator assigns staff roles and the system enforces those roles on later actions |
| F01-003 | Department master and staff department | Administrator maintains departments and associates each staff user with a department |
| F01-004 | Staff login and session | Staff user signs in, works in a session, and signs out |

---

### 02. Category and Catalogue Management

**Purpose:** Maintain the reusable category structure, dynamic fields, and catalogue items that auction creation later selects. The catalogue is the master repository of items offered through auctions.

**Functional requirements:**

- Create and edit categories and sub-categories, including parent-child relationships.
- Activate and deactivate categories. Configure, per category, whether image, video, and geographical location are required.
- Define reusable fields of type text, number, date, select, and boolean. A field may be used by more than one category.
- For select fields, add, edit, reorder, and activate or deactivate options.
- Map fields to a category with required or optional, display order, and category-specific configuration.
- Create a catalogue item on a dynamic form driven by the selected category. Capture category-specific details, upload applicable images, video, and documents, and capture geographical location where the category requires it.
- Edit, activate, deactivate, search, and view catalogue items.
- Only active catalogue items may be selected during auction creation.
- Selecting an item onto an auction does not modify the catalogue master.

**Acceptance criteria:**

- A category with mapped fields produces an item form that shows those fields in order, with required fields enforced.
- Inactive categories, inactive options, and inactive items are not offered for new auction selection.
- An item stores its media and location only when the category configuration calls for them.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Category and sub-category management | Administrator maintains the category tree and image, video, and location requirements |
| F02-002 | Reusable field master | Administrator defines text, number, date, select, and boolean fields for reuse |
| F02-003 | Field options for select fields | Administrator maintains the ordered, activatable options of a select field |
| F02-004 | Category–field mapping | Administrator maps fields to a category with required flag and display order |
| F02-005 | Catalogue item maintenance | Administrator captures, edits, activates, and searches items on the dynamic category form |

---

### 03. Bidder Registration and Profile

**Purpose:** Onboard bidders so that a verified bidder account can discover and participate in auctions according to eligibility rules.

**Functional requirements:**

- A bidder registers on the portal and submits the information required to open an account.
- A designated staff verifier reviews the registration and activates or rejects it. Until the account is active, the bidder cannot participate.
- An active bidder signs in and signs out.
- The bidder maintains profile details, organisation and contact information, and the bidder’s own master documents.
- Participation in a specific auction uses Module 07. Master documents on the profile are not a substitute for documents the auction itself requires, unless the auction’s participation rules say a profile document satisfies a named requirement.

**Acceptance criteria:**

- An unverified or rejected bidder cannot submit participation or a live bid.
- Profile, organisation, and master documents are visible to the bidder and to staff roles that must review them during evaluation.
- Login is separate from staff login.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Bidder self-registration | Bidder submits a registration request for a portal account |
| F03-002 | Bidder account verification | Designated staff verifier activates or rejects the bidder account |
| F03-003 | Bidder login and session | Active bidder signs in and signs out of the bidder portal |
| F03-004 | Bidder profile, organisation, and documents | Bidder maintains organisation, contact details, and master documents |

---

### 04. Auction Creation

**Purpose:** Provide the guided six-step draft in which the auction creator defines the auction and submits it for approval. The auction remains draft until submission.

**Functional requirements:**

- **Basic information.** Auction title (required), department, description, and auction direction (forward or reverse). Bid type: Direct (open to all eligible bidders), Prequalified (only prequalified bidders), or Restricted (limited participation). Procedure type: Open (visible to eligible bidders) or Restricted (participation limited). Display configuration: display reserve price, display last accepted bid, display bidder list, lot-wise EMD, and evaluation, each Yes or No.
- **Evaluation rule.** If Evaluation = Yes, participation is evaluated before the live auction and only accepted bidders may bid live. If Evaluation = No, eligible participants proceed to the live auction under the participation rules. This flag is a workflow control set at creation, not a post-auction activity.
- **Prequalified and restricted participation.** For a prequalified auction, the creator identifies the prequalified bidders from active bidder accounts. For a restricted auction, the creator identifies the limited set of bidders who may participate. Direct auctions do not use a closed list.
- **Parameters.** Auction structure: item-wise or group/lot-wise. Pricing format: inclusive of GST or exclusive of GST. EMD type: common EMD for all items, or item-wise EMD. Where lot-wise EMD is Yes, EMD applies at lot level. These parameters are part of confirmed creation scope.
- **Bid change and reserve display value.** The creator records the applicable bid-change price used later to validate a live bid (minimum change in the auction’s direction). Where reserve price may be displayed, the creator records the reserve price amount at item or lot level. Display to bidders still follows the display flag. The reserve amount is not an automatic reject rule.
- **Items.** Search, filter, and list active catalogue items; select them; show the selected count; organise them item-wise or into lots according to the structure. The catalogue master is not edited from this step.
- **Documents.** Upload supporting auction documents in PDF, DOC, XLS, JPG, and PNG, with a maximum size of 70 MB per file as stated for the auction creation documents. Documents are later visible to authorised users and bidders according to stage and access.
- **Schedule.** Participation Start, Participation End, Live Auction Start, and Live Auction End, enforced in that order. Delta time of 15 or 30 minutes. Next-day continuation cutoff.
- **Review.** Before submission the creator reviews basic information, direction, bid type, procedure, parameters, pricing, EMD, selected items, documents, both schedules, delta time, next-day cutoff, display configuration, and the evaluation setting. The creator may save a draft, go back, save and continue, or submit for approval.

**Acceptance criteria:**

- A submitted auction contains the required title, direction, bid type, procedure, structure, pricing format, EMD treatment, at least one item or lot, a valid schedule sequence, and a delta time of 15 or 30 minutes.
- Draft auctions are not visible to bidders.
- Item selection cannot modify catalogue master data.
- Evaluation = Yes or No is stored on the auction and is the control used by Modules 09 and 10.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Auction basic information and participation rules | Creator sets title, department, direction, bid type, procedure, display flags, evaluation, and any prequalified or restricted bidder list |
| F04-002 | Pricing, EMD, and bid parameters | Creator sets item or lot structure, GST pricing format, EMD type, bid-change price, and reserve price amount |
| F04-003 | Catalogue item selection and lot organisation | Creator searches the active catalogue, selects items, and arranges lots without editing the master |
| F04-004 | Auction supporting documents | Creator uploads the auction’s supporting documents within the stated formats and size |
| F04-005 | Participation and live auction schedule | Creator sets the four schedule points, delta time, and next-day continuation cutoff |
| F04-006 | Draft review and submit for approval | Creator reviews the full draft, saves it, and submits it for approval |

---

### 05. Auction Review, Approval and Publication

**Purpose:** Let the reviewing authority verify a submitted auction, approve it or send it back, and publish an approved auction under an auction notice number.

**Functional requirements:**

- A submitted auction appears to the designated reviewing / approving authority.
- The authority can view the complete auction, selected items, parameters, supporting documents, and both schedules.
- The authority may approve, or send the auction back for correction. A returned auction goes back to the creator as a draft that can be corrected and submitted again.
- After approval, the system generates the auction notice number, publishes the auction, and makes it visible to eligible bidders with the configured details, applicable documents, schedule, and participation conditions.
- Publication follows: approved auction, then notice number, then publish, then available for participation.
- Bidders do not see the auction before publication. Staff with review rights can see it from submission onward.

**Acceptance criteria:**

- An auction cannot be published unless it has been approved.
- Send-back records that the auction was returned and allows correction and resubmission.
- A published auction has one auction notice number and shows the details and documents configured for bidders.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Auction review and decision | Reviewing authority verifies the submitted auction and either approves it or sends it back |
| F05-002 | Auction notice and publication | After approval, the system assigns the auction notice number and publishes the auction to eligible bidders |

---

### 06. Corrigendum Management

**Purpose:** Correct or modify a published auction through a numbered corrigendum that bidders can read with the auction.

**Functional requirements:**

- An authorised user creates a corrigendum against a published auction, with corrigendum details.
- Corrigendum numbers are sequential for that auction.
- The corrigendum is submitted for approval where applicable, approved, and then published.
- The latest applicable published corrigendum is available to bidders together with the auction information.
- Bidders can view the applicable corrigendum. Unpublished drafts are not shown to bidders.

**Acceptance criteria:**

- Each published corrigendum has the next sequential number for that auction.
- Bidders see published corrigenda and do not see unapproved drafts.
- The auction history records corrigendum publication.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Corrigendum draft and approval | Authorised user drafts a sequential corrigendum and obtains approval where applicable |
| F06-002 | Corrigendum publication and bidder access | Approved corrigendum is published and bidders can read it with the auction |

---

### 07. Auction Discovery and Participation

**Purpose:** Let an eligible bidder find a published auction, read it, and submit participation with the EMD and documents the auction requires, inside the participation window.

**Functional requirements:**

- Search and filter published auctions by department, title, status, and date.
- Open auction details: information, items or lots, description, documents, participation schedule, live schedule, applicable terms, and EMD requirements. Corrigenda are those published under Module 06.
- Within the participation period, the bidder expresses interest / participates, completes EMD, uploads required documents, and receives participation confirmation.
- The system keeps the bidder’s participation status.
- EMD follows the auction configuration: common EMD, item-wise EMD, or lot-wise EMD where lot-wise EMD was configured. The bidder must complete the applicable EMD requirement before becoming eligible for the next stage.
- EMD fulfilment records the amount required by the configuration, the mode or instrument reference, and the proof document. It does not collect money through a payment gateway.
- Participation documents: show the applicable requirements, allow upload, store the files against that bidder’s participation, and make them available to authorised evaluation users. Where Evaluation = Yes, these documents are part of the evaluation pack.
- A bidder who is outside the prequalified or restricted list cannot participate in that auction.
- Participation outside the participation window is rejected.

**Acceptance criteria:**

- A verified eligible bidder can search, open, and submit one participation for an auction during the participation window.
- Participation status shows whether EMD and required documents are complete.
- Evaluation users can open the participation documents of bidders who participated.
- Incomplete EMD blocks progression to the next stage defined for that auction.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | Published auction search and detail | Bidder searches published auctions and reads items, documents, schedule, terms, and EMD requirements |
| F07-002 | Expression of interest and participation | Bidder participates during the participation window and the system tracks participation status |
| F07-003 | EMD fulfilment | Bidder completes common, item-wise, or lot-wise EMD as configured, with reference and proof |
| F07-004 | Participation document upload | Bidder uploads the documents the auction requires and evaluation staff can read them |

---

### 08. Pre-Auction Query and Clarification

**Purpose:** Where the auction provides a query period, let bidders raise questions and let the department publish clarifications against that auction before the applicable deadline.

**Functional requirements:**

- A bidder submits a query before the query deadline, which falls inside the configured participation / query period.
- An authorised department user views the query and records a clarification.
- The bidder views the response.
- The query and the response stay associated with the auction.
- Queries are not accepted after the deadline.

**Acceptance criteria:**

- Each query is tied to one auction and one bidder.
- The bidder who asked, and authorised department users, can read the clarification once it is issued.
- A query submitted after the deadline is not accepted.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | Pre-auction query and clarification | Bidder raises a query in the query window and the department records a clarification on the auction |

---

### 09. Pre-Live Participation Evaluation

**Purpose:** When Evaluation = Yes, decide which participating bidders are eligible for the live auction. This module does not run when Evaluation = No.

**Functional requirements:**

- The path is: bidder participation, then EMD and document submission, then participation evaluation, then eligibility verification, then accepted/eligible or rejected/ineligible. Only accepted bidders proceed to the live auction.
- The evaluation authority sees the participating bidder list and can review bidder details, submitted documents, EMD status, eligibility conditions, prequalification requirements where the auction is prequalified, and restricted-participation conditions where the auction is restricted.
- The authority records a decision and remarks for each bidder.
- The evaluation is submitted for approval where required. The accepted list is final only after that approval.
- An accepted bidder may enter the live auction and submit bids while it is open.
- A rejected bidder is excluded from the eligible list and cannot submit live bids.
- When Evaluation = No, there is no pre-live evaluation. Participants who have completed participation, EMD, and required documents, and who meet the auction’s direct, prequalified, or restricted rule, proceed as eligible participants.

**Acceptance criteria:**

- For an Evaluation = Yes auction, a bidder who is not on the approved accepted list cannot open live bidding.
- For an Evaluation = No auction, the evaluation screens are not in the bidder’s or the authority’s mandatory path.
- Decisions and remarks are retained for history.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F09-001 | Participation evaluation and eligibility decision | Evaluation authority reviews each participant’s EMD, documents, and eligibility and records accepted or rejected |
| F09-002 | Accepted bidder list approval | The accepted list is submitted and approved before it controls entry to the live auction |

---

### 10. Live Auction Bidding and Extension

**Purpose:** Let only eligible bidders bid during the live window, under the auction’s direction and item or lot structure, and apply extension rules.

**Functional requirements:**

- Entry is limited to bidders eligible for the live auction (approved accepted list when Evaluation = Yes; otherwise eligible participants).
- The bidder sees item or lot details and submits a bid. The system validates and, if accepted, updates the current bid.
- Direction: forward or reverse, as configured. Structure: item-wise or lot-wise, as configured.
- Validation covers the applicable bid-change price, bid direction, the item or lot, auction timing, bidder eligibility, and live-auction status.
- Display options control whether reserve price, last accepted bid, and bidder list are visible. Where bidder identity is masked, a bidder does not see the identity of other participating bidders.
- When a qualifying bid is received near closure, the live end extends by the configured delta of 15 or 30 minutes. The updated remaining time is shown to authorised users and participating bidders.
- The next-day continuation cutoff limits how far the live auction may run into the following day. An extension that would pass the cutoff does not do so; the auction closes at the cutoff.
- After closure, this module accepts no further bids.

**Acceptance criteria:**

- An ineligible bidder, or a bid outside the live window, is rejected.
- A bid that fails direction or bid-change validation is rejected and does not become the current bid.
- A qualifying near-close bid extends the end by the configured delta unless the next-day cutoff stops it.
- Masked auctions do not reveal other bidders’ identities to a bidder.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F10-001 | Live bid submission | Eligible bidder enters the live auction and submits item-wise or lot-wise bids for a forward or reverse auction |
| F10-002 | Live bid validation and visibility | System validates bid change, direction, timing, and eligibility, and applies reserve, last-bid, and identity display rules |
| F10-003 | Delta time extension and next-day cutoff | A qualifying near-close bid extends the auction by 15 or 30 minutes, limited by the next-day cutoff |

---

### 11. Live Auction Monitoring and Closure

**Purpose:** Give the auctioning authority a live view of the auction and close it either at the scheduled end or by an authorised force close.

**Functional requirements:**

- The monitoring view shows live status, item or lot status, current bidding activity, participant activity, remaining time, extension information, and closure information.
- Bidder identity and activity on the monitoring view follow the masking rules. The auctioning authority’s operational view may show what is required to monitor the auction; bidders remain masked from each other as configured.
- Force close is available to the auctioning authority where permitted. The authority must enter a reason. The system closes the auction, records the closure, and shows the closed status on the history.
- The auction also closes automatically at the configured live auction end, after any valid extension that is still inside the next-day cutoff.
- On closure, further bidding stops, final accepted bids are retained, and item or lot results become available for post-auction processing. The auction moves to the next stage.

**Acceptance criteria:**

- The monitoring view updates for the life of the live auction, including extensions.
- Force close without a reason is rejected.
- After either form of closure, bid submission is rejected and the retained bids are the bids available for ranking.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F11-001 | Live auction monitoring console | Auctioning authority watches status, items or lots, activity, remaining time, and extensions |
| F11-002 | Authorised force close | Auctioning authority closes an active auction with a mandatory reason, recorded on the history |
| F11-003 | Scheduled closure and bid freeze | Auction closes at the effective live end and further bids are refused while accepted bids are retained |

---

### 12. Results, Finalisation and Approval

**Purpose:** After closure, rank valid bids and let the finalisation authority select the successful bidder, then obtain approval before award.

**Functional requirements:**

- Authorised users see auction results after live closure.
- Forward ranking is highest valid bid first: H1, H2, H3, and so on. Reverse ranking is lowest valid bid first: L1, L2, L3, and so on.
- Ranking is at the applicable item or lot level.
- The finalisation authority reviews results and ranking, reviews each item or lot, identifies H1 or L1 as applicable, and handles a tie where more than one bidder shares the top rank. The authority selects the successful bidder, records remarks, and submits the finalisation for approval.
- The system does not silently pick one bidder when the top rank is tied. The authority’s selection and remarks are required.
- The approving authority views the result, the ranking, the selected bidder, and the remarks, and may approve or send the finalisation back for correction.
- Only after the required approval does the auction move to awarding.

**Acceptance criteria:**

- Ranking order matches the auction direction and uses only final accepted bids.
- A tied top rank cannot be submitted without an explicit selection and remarks.
- Award is not available while finalisation is pending or has been sent back.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F12-001 | Item and lot bid ranking | System ranks final accepted bids H1/H2/H3 or L1/L2/L3 at item or lot level |
| F12-002 | Successful bidder finalisation | Finalisation authority reviews ranks, resolves a tied top rank, and submits the selected bidder |
| F12-003 | Finalisation approval | Approving authority approves the finalisation or sends it back before award can start |

---

### 13. Award and Letter of Intent

**Purpose:** Complete the auction by approving the award, generating the Letter of Intent, notifying the successful bidder, and marking the auction complete.

**Functional requirements:**

- The awarding authority reviews the final result and the selected bidder, approves the award, and records the award decision and remarks.
- After award approval, the system generates the Letter of Intent for the successful bidder.
- The Letter of Intent is associated with the auction, the auction notice number, the successful bidder, the applicable item or lot, the final accepted bid or result, and the award information.
- The Letter of Intent is available to the successful bidder under the access rules. Other bidders do not receive that Letter of Intent.
- The successful bidder is notified. The authority then completes the auction.
- The flow is: final result, review of the selected bidder, award approval, generate Letter of Intent, notify the successful bidder, complete the auction.

**Acceptance criteria:**

- A Letter of Intent cannot be generated before award approval, and award approval cannot precede finalisation approval.
- The Letter of Intent carries the notice number, bidder, item or lot, and final result.
- The auction reaches a completed state only after award, Letter of Intent, and successful-bidder notification have been recorded.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F13-001 | Award review and approval | Awarding authority reviews the approved finalisation and records the award decision |
| F13-002 | Letter of Intent generation | System generates the Letter of Intent for the successful bidder and makes it available to that bidder |
| F13-003 | Auction completion and successful-bidder advice | Authority completes the auction after the successful bidder has been advised |

---

### 14. Notifications

**Purpose:** Inform staff and bidders at the lifecycle points named in the source, inside the portal and by email.

**Functional requirements:**

- Raise notifications for: auction submitted for approval; auction approved; auction returned for correction; auction published; corrigendum published; participation submitted; participation evaluation completed; bidder accepted or eligible; bidder rejected or ineligible; live auction commencement; auction closure; bid finalisation; award approval; Letter of Intent generation; successful bidder notification; and auction completion.
- Each notification goes to the role or bidder the event concerns. For example, submit-for-approval notifies the reviewing authority; acceptance or rejection notifies that bidder; the Letter of Intent notifies the successful bidder.
- In-portal notification list shows the event and links it to the auction.
- Email carries the same event to the recipient’s recorded email address. Delivery outcome is visible to an administrator for operational follow-up.
- SMS is not part of this scope.

**Acceptance criteria:**

- Each listed event creates a notification for the relevant recipient when the event occurs.
- A bidder does not receive another bidder’s eligibility or Letter of Intent notification.
- Failed email delivery is visible for follow-up and does not roll back the business event that triggered it.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F14-001 | Lifecycle notification events and in-portal alerts | System records the named auction events and shows them to the relevant staff user or bidder |
| F14-002 | Email delivery of auction notifications | The same events are emailed to the recipient and delivery outcome is recorded |

---

### 15. Auction Status and History

**Purpose:** Show the current stage of an auction and keep a trace of the lifecycle for authorised users.

**Functional requirements:**

- Maintain functional status through the stages in Appendix C, including the evaluation branch and force close.
- History allows an authorised user to trace creation, draft, submission, review, approval or return, publication, corrigendum, bidder participation, participation evaluation where applicable, live bidding, closure, ranking, finalisation, approval, awarding, Letter of Intent, and completion.
- Bidders see only the history and status that their role and the auction’s display rules allow. They do not see internal return remarks intended only for the creator, except where a published corrigendum or a bidder-facing decision (such as their own eligibility) is addressed to them.
- Status changes are a consequence of the business actions in Modules 04 to 13, not a separate editable field for ordinary users.

**Acceptance criteria:**

- An authorised staff user can open one auction and read the sequence of stages that actually occurred.
- A force-closed auction shows the force-close reason on the history.
- Status shown to a bidder matches what that bidder is allowed to know at that stage.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F15-001 | Auction lifecycle status | Authorised users see the current stage, including the evaluation branch and closure type |
| F15-002 | Auction history for authorised users | Authorised users trace the recorded stages from creation through completion |

---

## 7. End-to-End Workflows

### 7.1 Catalogue preparation

1. The catalogue administrator creates categories and sub-categories and sets image, video, and location requirements.
2. The administrator defines reusable fields and, for select fields, their options.
3. The administrator maps fields to each category.
4. The administrator creates catalogue items on the dynamic form and activates the items that may be auctioned.

### 7.2 Auction creation and publication

1. The auction creator opens a draft and completes basic information, including direction, bid type, procedure, display flags, and Evaluation Yes or No.
2. The creator sets structure, pricing format, EMD type, bid-change price, and reserve price amount.
3. The creator selects active catalogue items and, when the structure is lot-wise, arranges lots.
4. The creator uploads supporting documents and sets participation and live schedules, delta time, and the next-day cutoff.
5. The creator reviews the draft and submits it.
6. The reviewing authority verifies items, parameters, documents, and schedules, then approves or sends the draft back.
7. On approval, the system assigns the auction notice number and publishes the auction to eligible bidders.

### 7.3 Corrigendum

1. An authorised user drafts a corrigendum on a published auction.
2. The corrigendum is approved where applicable and published with the next sequential number.
3. Bidders read the latest applicable corrigendum with the auction.

### 7.4 Bidder onboarding

1. The bidder registers.
2. The designated verifier activates or rejects the account.
3. An active bidder maintains profile, organisation, and master documents, and signs in to use the portal.

### 7.5 Participation when Evaluation = Yes

1. The bidder searches and opens the published auction.
2. Inside the participation window, the bidder participates, completes the configured EMD fulfilment, and uploads required documents.
3. The bidder may raise a query before the query deadline; the department records a clarification.
4. The evaluation authority reviews EMD, documents, and eligibility, and marks each participant accepted or rejected.
5. The accepted list is approved.
6. Only accepted bidders enter the live auction.

### 7.6 Participation when Evaluation = No

1. Steps 1 to 3 of Section 7.5 are the same.
2. There is no pre-live evaluation.
3. Participants who completed participation, EMD, and required documents, and who satisfy the direct, prequalified, or restricted rule, enter the live auction as eligible participants.

### 7.7 Live auction, ranking, and award

1. The eligible bidder views the item or lot and submits bids. Invalid bids are rejected. Accepted bids update the current bid.
2. A qualifying bid near closure extends the end by the delta time, unless the next-day cutoff stops the extension. Remaining time is shown to participants and to the monitoring authority.
3. The auctioning authority monitors status, activity, and time, and may force close with a reason.
4. At the effective end, or on force close, bidding stops and accepted bids are retained.
5. The system ranks H1/H2/H3 or L1/L2/L3 at item or lot level.
6. The finalisation authority selects the successful bidder, including an explicit choice when the top rank is tied, and submits for approval.
7. The approving authority approves or sends the finalisation back.
8. After approval, the awarding authority approves the award, the system generates the Letter of Intent, the successful bidder is notified, and the auction is completed.

---

## 8. Access Control

**Access model:** User → Role → Permissions, with **Department** as an organisational attribute on the staff user and on the auction. This is not a post or position hierarchy. The source lists roles and a department field; it does not define posts, reporting lines, or an organisation tree beyond department.

Bidder identity is a separate portal account (Module 03), not a staff role.

| Role | Typical access |
|------|----------------|
| System / Catalogue Administrator | Categories, fields, options, mappings, catalogue items; cross-department staff and department master |
| Auction Creator | Create and edit own department’s drafts, select items, set parameters, upload auction documents, set the schedule, submit for approval, correct a returned auction |
| Reviewing / Approving Authority | Review submitted auctions, approve or send back, approve corrigendum and the accepted-bidder list where those approvals apply, approve finalisation |
| Bidder | Register, sign in, search, view permitted auction details, participate, submit EMD proof and documents, query, bid when eligible, read own result notices and own Letter of Intent |
| Evaluation Authority | When Evaluation = Yes, review participants and record eligibility |
| Auctioning Authority | Monitor the live auction and force close where permitted |
| Finalisation Authority | Review ranking and select the successful bidder |
| Awarding Authority | Approve the award, issue the Letter of Intent, and complete the auction |

A person may hold more than one staff role. Actions remain attributable to the user. Department scoping limits auction creation and departmental processing to the user’s department, except for the System / Catalogue Administrator.

---

## 9. Channels

| Channel | Treatment |
|---------|-----------|
| Staff web application | In scope. Catalogue, creation, approval, evaluation, monitoring, finalisation, and award |
| Bidder web portal | In scope. Registration, search, participation, query, live bidding, and own Letter of Intent |
| In-portal notifications | In scope |
| Email | In scope, for the events in Module 14 |
| SMS | Out of scope |
| Native mobile applications | Out of scope |
| Unauthenticated public bidding | Out of scope. Bidders use a verified account |

---

## 10. Integrations

| Integration | Purpose | Treatment |
|-------------|---------|-----------|
| Email delivery service | Send the lifecycle notifications in Module 14 and record delivery outcome | In scope. The organisation provides the mail service |
| Payment gateway | Collect or refund EMD or award value | Out of scope |
| SMS provider | Text messages | Out of scope |
| ERP, finance, or e-tender portal | Posting of award or catalogue sync | Out of scope |
| Digital signature service | Signing the Letter of Intent | Out of scope |

No integration hub is required beyond email delivery. Catalogue files, auction documents, participation documents, and the Letter of Intent are stored with the business record they belong to.

---

## 11. Audit, Compliance and Security

- Staff and bidder passwords are stored so that they cannot be read back. Sessions expire and can be ended by the user.
- A bidder sees only auctions the bid type, procedure, and eligibility rules allow, and only the fields the display configuration allows during live bidding.
- One bidder does not see another bidder’s identity when masking applies, and does not see another bidder’s documents, EMD proof, eligibility remarks, or Letter of Intent.
- Internal send-back remarks are visible to the creator and the reviewing authority, not to the bidder community.
- The history in Module 15 records who performed each stage-changing action and when, including force-close reason, eligibility decision, finalisation choice, and award.
- Documents are available only to the roles named for that stage.
- The organisation remains responsible for the legal basis of the auction, the contents of the Letter of Intent, and retention periods. The system must be able to retain the auction record through completion.

---

## 12. Non-Functional Requirements

1. Live bid acceptance, rejection, current-bid update, and remaining-time display must stay consistent for all participants in the same auction, including when a delta extension occurs.
2. Two bids submitted at the same moment must result in one accepted current bid according to the validation rules, not two contradictory current bids.
3. Search and auction detail must remain usable for the organisation’s expected catalogue and published-auction volumes. Volumes are not stated in the source and will be confirmed before build sizing.
4. Monitoring must show the same remaining time and extension state that bidders see.
5. Uploads must enforce the 70 MB limit on auction supporting documents and the allowed formats named in this SOW.
6. A failed email must not undo publication, approval, closure, or award.
7. The service should be available during published participation windows and live auctions. Planned downtime must not be scheduled across a live auction that is already open.
8. The interface language of the source material is English. No second-language requirement is stated.

---

## 13. Data Migration

**Out of scope.** No legacy catalogue, bidder, or historical auction migration is included. Opening balances of categories, items, departments, and staff users are entered in the new system as ordinary master data, not as a migration project.

---

## 14. Phased Delivery

### Phase 1 — Go-live

All modules 01 to 15, including both Evaluation = Yes and Evaluation = No, forward and reverse auctions, item-wise and lot-wise structure, corrigendum, delta time, force close, ranking, award, and Letter of Intent.

### Not in this phase

Payment gateway, SMS, mobile applications, contract and settlement after the Letter of Intent, ERP posting, and legacy migration. These are outside this Statement of Work unless the organisation later commissions them.

---

## 15. Deliverables

1. Staff web application covering modules 01, 02, 04, 05, 06, 08, 09, 11, 12, 13, and the staff views of 07, 14, and 15.
2. Bidder web portal covering modules 03, 07, 08, 10, and the bidder views of 06, 13, 14, and 15.
3. Email notification for the events in Module 14.
4. Configurable category-driven catalogue and the six-step auction draft.
5. Live bidding with validation, masking, delta extension, monitoring, and closure.
6. Ranking, finalisation, award, and Letter of Intent.
7. Auction history for authorised users.
8. Administrator and user documentation sufficient to operate the processes in this SOW.
9. This Statement of Work as the functional baseline.

---

## 16. Acceptance Criteria

Program-level acceptance is met when all of the following are demonstrated on agreed sample data:

1. An administrator can define a category, fields, and an active catalogue item, and that item can be selected onto an auction without changing the master.
2. A creator can save a draft, submit it, receive a send-back, correct it, and obtain approval.
3. Publication produces an auction notice number and the auction becomes visible to an eligible bidder and not to an ineligible one.
4. A published corrigendum is numbered sequentially and is visible to the bidder.
5. A bidder can register, be verified, participate, file EMD proof, upload participation documents, and raise a query that receives a clarification.
6. With Evaluation = Yes, a rejected bidder cannot bid live and an accepted bidder can.
7. With Evaluation = No, a participant who completed the participation requirements can bid live without an evaluation step.
8. A forward auction ranks the highest valid bid as H1. A reverse auction ranks the lowest valid bid as L1.
9. A bid that breaks the bid-change rule, the direction, the window, or eligibility is rejected.
10. A qualifying bid near the end extends the auction by the configured 15 or 30 minutes and stops at the next-day cutoff.
11. Force close requires a reason, stops bidding, and appears on the history.
12. A tied top rank requires an explicit selection. Finalisation approval is required before award. The Letter of Intent is issued only to the successful bidder, and the auction can then be completed.
13. The named notification events reach the relevant recipient in the portal, and email delivery outcome is recorded.
14. An authorised user can read the auction history from draft through completion.

---

## 17. Expected Benefits

- One controlled record from catalogue item to Letter of Intent, instead of separate spreadsheets for items, approvals, and results.
- The evaluation flag makes the pre-live gate explicit, so ineligible bidders are not admitted to the live auction by process error.
- Configurable categories avoid a separate item form for every commodity.
- Publication, corrigendum, and notice numbers give bidders a single place to read the auction as issued and as corrected.
- Ranking rules are consistent with forward and reverse direction, and ties are resolved by a recorded decision rather than an unstated automatic choice.
- History supports later review of approval, eligibility, closure, and award.

---

## 18. Assumptions and Dependencies

1. The source does not name the sponsoring organisation. This SOW stays organisation-neutral. Department is a data attribute, not a specific external body.
2. **Access model** is User → Role, plus Department. No post or position hierarchy is included.
3. **Document management and approvals are embedded** in the modules above.
4. **Bidder verification** is performed by a designated staff user (Catalogue Administrator or another staff role the organisation names). The source requires “applicable verification” and does not name an external identity provider.
5. **Prequalified and restricted lists** are chosen from active bidder accounts during auction creation. There is no separate prequalification programme beyond that list and the checks during evaluation.
6. **EMD** is fulfilled by recording the configured amount, an instrument or reference, and a proof document. No payment gateway is in scope. EMD refund and forfeiture workflows are out of scope because the source does not describe them.
7. **Bid-change price** is captured at creation because live validation must apply “the applicable bid change price.” The source does not name the field; this SOW treats it as a required auction parameter.
8. **Reserve price amount** is captured so that it can be displayed when the display flag is Yes. Bids are not auto-rejected for missing the reserve, because the source does not state that rule.
9. **GST** is a pricing-format flag only. The system does not compute tax.
10. **Delta time** allows only the two values stated in the source: 15 minutes and 30 minutes.
11. **Next-day continuation cutoff** is a clock time, configured on the auction, past which the live auction may not be extended. The source does not fix the default clock time; the creator sets it per auction.
12. **Corrigendum approval** follows submit and approve before publication, because the source says approval “where applicable.” This SOW applies that approval for every corrigendum so publication is controlled. A later instruction may exempt a class of corrigendum; that would be a scope change.
13. **Evaluation-list approval** is required whenever Evaluation = Yes, because the source says the evaluation is submitted for approval where required and only the final accepted list may enter the live auction. The approver is the Reviewing / Approving Authority.
14. **Tied H1 or L1** is resolved by the finalisation authority’s explicit selection and remarks. The system does not auto-select.
15. **Notifications** use the in-portal list and email. SMS is out of scope. The organisation provides the email service and the mailbox addresses on staff and bidder profiles.
16. **Query period** is bounded by the participation window unless the organisation later defines a shorter deadline inside that window. The source says the query function operates within the configured participation / query period.
17. **70 MB** and the formats PDF, DOC, XLS, JPG, and PNG apply to auction supporting documents, as stated for auction creation. Catalogue media follow the category’s image, video, and document switches; a separate catalogue size cap is not stated and will be set as an operational limit without changing business scope.
18. **Single phase.** The source does not describe a phased release.
19. **No legacy migration.**
20. **Language** is English.
21. **Volumes** (bidders, concurrent live participants, catalogue size) are not in the source and are a dependency for capacity planning. They do not change the functional scope above.
22. Staff who approve auctions, corrigenda, evaluation lists, and finalisation are available in the role model. The source allows these to be the same reviewing authority; the organisation may later split duties by assigning roles to different people without a scope change.
23. Letter of Intent content is a structured notice assembled from the auction, notice number, bidder, item or lot, final result, and award. Legal wording of the template is supplied by the organisation.
24. This document is the functional baseline. The source functional scope remains the originating brief.

### Dependencies

- Organisation-supplied email service and template wording for the Letter of Intent.
- Named staff for each role, and a rule for which person verifies bidders.
- Confirmation of expected concurrent bidders in a single live auction before non-functional sizing is final.

---

## 19. Vendor Response Expectations

Respondents should confirm:

1. Coverage of every module and feature identifier in Appendix A, or an explicit exception.
2. That Evaluation = Yes is implemented before live bidding, and Evaluation = No skips that stage.
3. Forward and reverse ranking, item-wise and lot-wise bidding, and the 15/30 minute delta with next-day cutoff.
4. That EMD is fulfilment and proof, and that payment gateway, SMS, mobile apps, and post-LOI contract management are excluded unless added by change.
5. The access model in Section 8, including separate bidder accounts.
6. How concurrent bids and extension timing will be kept consistent, at business-outcome level, without turning this response into a technical design.
7. Dependencies they need from the organisation (email service, Letter of Intent wording, volumes, role holders).

---

## 20. Appendix A — Module and Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | Staff Access and Role Management | Shared | F01-001 … F01-004 (4) |
| 02 | Category and Catalogue Management | Business | F02-001 … F02-005 (5) |
| 03 | Bidder Registration and Profile | Business | F03-001 … F03-004 (4) |
| 04 | Auction Creation | Business | F04-001 … F04-006 (6) |
| 05 | Auction Review, Approval and Publication | Business | F05-001 … F05-002 (2) |
| 06 | Corrigendum Management | Business | F06-001 … F06-002 (2) |
| 07 | Auction Discovery and Participation | Business | F07-001 … F07-004 (4) |
| 08 | Pre-Auction Query and Clarification | Business | F08-001 (1) |
| 09 | Pre-Live Participation Evaluation | Business | F09-001 … F09-002 (2) |
| 10 | Live Auction Bidding and Extension | Business | F10-001 … F10-003 (3) |
| 11 | Live Auction Monitoring and Closure | Business | F11-001 … F11-003 (3) |
| 12 | Results, Finalisation and Approval | Business | F12-001 … F12-003 (3) |
| 13 | Award and Letter of Intent | Business | F13-001 … F13-003 (3) |
| 14 | Notifications | Technical | F14-001 … F14-002 (2) |
| 15 | Auction Status and History | Business | F15-001 … F15-002 (2) |

**Totals:** 15 modules, 46 features.

---

## 21. Appendix B — Role Responsibilities

| Role | Major responsibility |
|------|----------------------|
| System / Catalogue Administrator | Category, field, field option, category mapping, and catalogue item management; department and staff account administration |
| Auction Creator | Create the auction, select catalogue items, configure parameters, upload documents, schedule the auction, and submit for approval |
| Reviewing / Approving Authority | Review the auction, verify details, approve or send back; approve corrigendum, accepted-bidder list, and finalisation where those approvals apply |
| Bidder | Register, sign in, search auctions, view details, participate, submit EMD proof and documents, query, and bid when eligible |
| Evaluation Authority | When Evaluation = Yes, evaluate participants before the live auction and prepare the accepted list |
| Auctioning Authority | Monitor the live auction, including bids and timers, and force close where permitted |
| Finalisation Authority | Review results and ranking and select the successful bidder |
| Awarding Authority | Approve the award, generate and issue the Letter of Intent, and complete the auction |

---

## 22. Appendix C — Auction Stage Record

The history must be able to show which of the following occurred. Exact labels may be worded during implementation; the sequence and the branch may not.

| Order | Stage | Notes |
|------:|-------|-------|
| 1 | Draft | Editable by the creator. Not visible to bidders |
| 2 | Submitted for review | Waiting on the reviewing authority |
| 3 | Returned for correction | Back with the creator. Resubmission returns to submitted |
| 4 | Approved | Eligible for publication. Not yet public |
| 5 | Published | Notice number assigned. Visible to eligible bidders |
| 6 | Corrigendum published | One or more sequential corrigenda may occur while the auction is published |
| 7 | Participation open | Between participation start and participation end |
| 8 | Under evaluation | Only when Evaluation = Yes, after participation requirements and before the live auction |
| 9 | Eligible list final | Accepted list approved. Skipped as a gate when Evaluation = No |
| 10 | Live | Between live start and effective live end |
| 11 | Extended | Live end moved by delta time. Still a live auction |
| 12 | Closed | Scheduled end or force close. No further bids |
| 13 | Ranked | H1… or L1… available at item or lot level |
| 14 | Finalisation submitted | Successful bidder selected, including tie resolution |
| 15 | Finalisation returned | Sent back for correction |
| 16 | Finalisation approved | Award may start |
| 17 | Awarded | Award decision recorded |
| 18 | Letter of Intent issued | Available to the successful bidder |
| 19 | Completed | Successful bidder advised and auction closed out |

---

## 23. Appendix D — Document Types

| Document | Where it belongs | Who adds it | Who reads it |
|----------|------------------|-------------|--------------|
| Catalogue image, video, document | Catalogue item, if the category requires it | Catalogue administrator | Creator during selection; bidders as part of item detail when the auction shows the item |
| Geographical location | Catalogue item, if required | Catalogue administrator | Same as the item |
| Auction supporting document | Auction draft and published auction | Auction creator | Reviewer; eligible bidders after publication. PDF, DOC, XLS, JPG, PNG; 70 MB maximum |
| Corrigendum detail | Corrigendum on a published auction | Authorised staff user | Bidders after the corrigendum is published |
| Bidder master document | Bidder profile | Bidder | Bidder; verifier; evaluation authority when relevant |
| Participation document | That bidder’s participation on one auction | Bidder | Bidder; evaluation authority and other authorised evaluation users |
| EMD proof | That bidder’s EMD fulfilment | Bidder | Bidder; evaluation authority |
| Letter of Intent | Awarded auction | Generated after award approval | Successful bidder and awarding authority |

---

## 24. Appendix E — Consolidation Map

The source listed twenty-three functional areas. They are consolidated below so that each module can be estimated as one implementation unit. Nothing in the source was dropped; items that are not their own module are embedded as shown.

| Source area | Treatment in this SOW |
|-------------|------------------------|
| Category / Catalogue Management | Module 02 |
| Auction Creation, steps 1 to 6 | Module 04 |
| Auction Review and Approval | Module 05, with publication |
| Auction Publication | Module 05 |
| Corrigendum Management | Module 06 |
| Bidder Registration and Login | Module 03 |
| Auction Search, Details | Module 07 |
| Expression of Interest / Participation | Module 07 |
| EMD Management | Module 07. Not a payment module |
| Participation Documents | Module 07 |
| Pre-Auction Query / Clarification | Module 08 |
| Pre-Live Participation Evaluation | Module 09 |
| Evaluation = No direct path | Rule in Modules 09 and 10, not a separate module |
| Live Auction Bidding and bid validation | Module 10 |
| Delta Time and Auction Extension | Module 10 |
| Live Auction Monitoring | Module 11 |
| Force Close | Module 11 |
| Auction Closure | Module 11 |
| Auction Result and Bid Ranking | Module 12 |
| Bidder Finalisation | Module 12 |
| Finalisation Approval | Module 12 |
| Auction Awarding | Module 13 |
| Letter of Intent | Module 13 |
| Notifications | Module 14 |
| Auction Status and History | Module 15 |
| Role-wise responsibilities | Section 8 and Appendix B. Staff accounts are Module 01 because the source names the roles but does not specify how staff accounts are administered |
| Document upload and storage | Embedded in Modules 02, 03, 04, 06, 07, and 13 |
| Approval steps | Embedded in Modules 05, 06, 09, 12, and 13 |

---

*End of Statement of Work.*
