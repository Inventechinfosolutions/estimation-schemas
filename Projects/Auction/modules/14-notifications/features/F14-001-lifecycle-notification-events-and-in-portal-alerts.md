# F14-001 — Lifecycle Notification Events and In-portal Alerts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F14-001 |
| **Feature Name** | Lifecycle Notification Events and In-portal Alerts |
| **Module** | 14 — Notifications |

### Description
When a business event in the auction lifecycle occurs, the system writes an in-portal alert for the people that event concerns. The events are: auction submitted, approved, returned, published, corrigendum published, participation submitted, evaluation completed, bidder accepted, bidder rejected, live auction commencement, closure, finalisation submitted, award approval, letter issued, successful-bidder advice, and completion. A bidder never receives another bidder’s acceptance, rejection, or letter.

### Business Objective
Staff and bidders see the events that concern them on the portal, without a separate notification product to administer event by event in code each time.

### Actors
The business features raise the events. Recipients read them. The System / Catalogue Administrator can see that the event types exist. Approver: none.

### User Journey
1. Who creates: the business action creates the alert. A user does not compose it from a blank page.
2. How they create: submitting, approving, publishing, and the other listed actions call this feature, which stores an alert for each recipient the event allows.
3. How they edit: a recipient marks their own alert as read. They cannot edit the text. An administrator does not rewrite history.
4. How they send for approval: they do not. The business approval already happened in the originating feature.
5. How the approver sees pending items: there is no approval inbox for alerts. The recipient’s alert list is the inbox.
6. How the approver decides: there is no decision. Opening or marking read is not an auction decision.
7. How the maker sees history: the recipient sees their alerts with time and auction, newest first, including those they have read.
8. How the auditor sees history: the administrator can see which event was raised for an auction and which role was targeted, without reading another bidder’s private acceptance text in a shared dump. Bidder-specific text stays with that bidder.

### Functional Capabilities
- Raise an alert for each listed lifecycle event
- Target the role or the specific bidder the event concerns
- Show a recipient their own alert list, linked to the auction
- Mark an alert read
- Keep one bidder’s eligibility and letter alerts private

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Event type
- Auction
- Recipient

### Outputs
- In-portal alerts

### Business Rules
- The event list is the list in the Statement of Work. Staff cannot invent a new public event type from the screen.
- Submit-for-approval alerts the reviewing authority of the department.
- Return alerts the creator. Publish alerts eligible bidders. Acceptance or rejection alerts only that bidder, and only after the list is approved.
- Letter and successful-bidder advice alert only the successful bidder.
- A failed later email does not remove the in-portal alert.

### Validations
- Event type is one of the named events.
- The recipient is allowed to know that event.
- The auction reference is present.

### Calculations
None.

### Workflow
Business action → alert stored → recipient reads it. No extra approval.

### Search Requirements
The recipient filters by unread and by auction title.

### Documents
None. The alert links to the auction or the letter; it is not the document.

### Reports
None.

### Notifications
This feature is the in-portal channel. Email is F14-002.

### Security
A user can read only their alerts. Department staff alerts are limited to their department’s auctions.

### Integrations
None inside this feature.

### Dependencies
Events from Modules 04 through 13.

### Assumptions
- Wording of each alert is a short factual sentence naming the auction and the event. It is not a marketing template the administrator rewrites per auction.
- Live bid-by-bid events are not alerts. The source’s list does not include every bid.

### Risks
If a business feature forgets to raise an event, the user will not see it. Each originating feature in this package names the alert it raises.

### Non Functional Requirements
Writing the alert does not roll back the business action if the alert store fails; the failure is visible to the administrator. The business commit remains the source of truth and the alert can be retried.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Notification event list | UI | Medium | 6 |
| My notification inbox | UI | Medium | 6 |
| Raise lifecycle notification | API | Complex | 8 |
| List my notifications | API | Medium | 6 |
| Mark notification read | API | Easy | 4 |
| In-portal notification records | DB | Medium | 4 |
| In-portal notification tests | Testing | Complex | 8 |
| In-portal notification notes | Documentation | Medium | 3 |

**Feature total: 45 hours**
