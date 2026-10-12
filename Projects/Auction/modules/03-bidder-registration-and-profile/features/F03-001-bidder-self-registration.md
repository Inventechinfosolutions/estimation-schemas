# F03-001 — Bidder Self-Registration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Bidder Self-Registration |
| **Module** | 03 — Bidder Registration and Profile |

### Description
A prospective bidder opens the portal and submits a registration: organisation name, contact person, email, mobile, and the declaration that they want an account. The account is not active. Verification is F03-002. This screen does not collect EMD and does not attach the bidder to an auction.

### Business Objective
People who will bid have a single registration request that staff can verify before any participation.

### Actors
Maker: the prospective bidder. Approver: none on this feature. The verifier acts in F03-002.

### User Journey
1. Who creates: the prospective bidder creates the registration request. Staff do not type it for them.
2. How they create: Bidder portal → Register → organisation, contact name, email, mobile → Submit. They see an acknowledgement that the account awaits verification.
3. How they edit: until a verifier has opened the request, the bidder may correct organisation and contact details from the acknowledgement link. After a decision, changes go through the profile in F03-004 if the account was activated, or a new registration if it was rejected.
4. How they send for approval: Submit sends the request to the verifier queue in F03-002. The bidder does not choose the approver.
5. How the approver sees pending items: not on this feature. The verifier’s inbox is F03-002.
6. How the approver decides: not on this feature.
7. How the maker sees history: the bidder sees the request status: submitted, activated, or rejected.
8. How the auditor sees history: the verifier and the System / Catalogue Administrator see the submitted details and the later decision on F03-002. The bidder does not see internal verifier notes.

### Functional Capabilities
- Capture organisation and contact details for a new bidder
- Reject a second open request for the same email
- Leave the account inactive until verification
- Show the bidder a status of submitted, not yet active

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Organisation name
- Contact name
- Email
- Mobile

### Outputs
- A pending bidder registration
- A status the bidder can read

### Business Rules
- Submission does not allow participation or bidding.
- Email cannot already belong to an active bidder or to another pending request.
- Staff accounts and bidder accounts are separate even if the email string matches a staff user. The person still needs a bidder registration to bid.
- No auction is chosen during registration.

### Validations
- Organisation, contact, email, and mobile are mandatory.
- Email format is checked.
- Duplicate pending or active email is rejected.

### Calculations
None.

### Workflow
Submit moves the request to the verifier. There is no bidder-side approval.

### Search Requirements
The bidder finds their own request by signing in after activation, or by the status on the acknowledgement. They cannot search other bidders.

### Documents
None on this request. Master documents are added after activation in F03-004. The verifier may still reject a request that has no documents yet; document completeness is the verifier’s judgement in F03-002, and the organisation may require documents before activation.

### Reports
None.

### Notifications
Submission notifies the verifier through F14-001. The bidder is notified when F03-002 decides.

### Security
The public registration form reveals nothing about existing bidders beyond a duplicate-email failure on that person’s own address.

### Integrations
None. Notification dispatch is Module 14.

### Dependencies
F14-001 for the verifier alert.

### Assumptions
- The source says the bidder registers and completes applicable verification. It does not collect a government identity number. Those extra identifiers are not invented here.
- Mobile is a contact number, not an SMS one-time password. SMS is out of scope.

### Risks
A thin registration can be activated by mistake if the verifier does not look at documents. F03-002 is where that control sits.

### Non Functional Requirements
A double submit does not create two pending accounts for the same email.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Bidder registration form | UI | Complex | 12 |
| Registration acknowledgement | UI | Simple | 2 |
| Submit bidder registration | API | Complex | 8 |
| Check duplicate bidder email | API | Medium | 6 |
| Pending bidder registration records | DB | Medium | 4 |
| Bidder registration tests | Testing | Complex | 8 |
| Bidder registration notes | Documentation | Medium | 3 |

**Feature total: 43 hours**
