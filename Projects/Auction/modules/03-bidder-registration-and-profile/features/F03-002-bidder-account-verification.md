# F03-002 — Bidder Account Verification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Bidder Account Verification |
| **Module** | 03 — Bidder Registration and Profile |

### Description
A designated staff verifier opens pending bidder registrations, reads the organisation details, and activates or rejects the account. Only an activated bidder can sign in and participate. Rejection records remarks the bidder can see as the outcome, without exposing unrelated internal notes.

### Business Objective
No unverified person can participate in an auction or enter a live bid.

### Actors
Maker: the bidder, by having submitted F03-001. Decider: System / Catalogue Administrator, or another staff user the organisation has given this duty through a staff role. There is a decision, not a second unnamed committee, unless the organisation assigns the Catalogue Administrator role to the people who should verify.

### User Journey
1. Who creates: the bidder already created the request. The verifier creates the decision.
2. How they create: Verification inbox → open the request → read organisation and contact → Activate or Reject, with remarks → Save.
3. How they edit: a rejection is final for that request. A mistaken activation can be reversed by deactivating the bidder from this detail, which blocks participation immediately. The verifier does not rewrite the bidder’s organisation name; the bidder does that on the profile after activation.
4. How they send for approval: they do not send it onward. The verifier’s decision is the approval the source calls verification.
5. How the approver sees pending items: the verification inbox lists submitted requests that have no decision, filtered by date and organisation.
6. How the approver decides: Activate, which enables sign-in, or Reject, which keeps the account closed and stores the remark.
7. How the maker sees history: the bidder sees activated or rejected, and the remark addressed to them.
8. How the auditor sees history: the verifier sees the decision, the remark, who decided, and when. The System / Catalogue Administrator sees the same.

### Functional Capabilities
- List pending bidder registrations
- Read organisation and contact details
- Activate or reject with a remark
- Deactivate an already active bidder so they cannot participate further
- Show the bidder their own outcome

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Registration request
- Decision
- Remark

### Outputs
- Active or rejected bidder account
- Decision history
- Notification to the bidder

### Business Rules
- Only a pending request can be activated or rejected.
- Activation is what makes F03-003 succeed.
- A rejected request cannot participate. The person may submit a new registration.
- Deactivating an active bidder stops new participation and new bids. It does not delete participation already submitted.
- The verifier cannot activate their own bidder registration if they also hold a bidder account. Staff and bidder identities stay separate.

### Validations
- Decision and remark are mandatory.
- The request must still be pending.
- The acting user must hold the catalogue administrator duty.

### Calculations
None.

### Workflow
Inbox → decision → bidder notified. No further approver.

### Search Requirements
Organisation, email, status (pending, active, rejected), decision date.

### Documents
None added here. If the organisation expects master documents before activation, the verifier rejects until the bidder has a channel to supply them. Master document upload is available on the profile after activation; before activation the registration itself is the pack. This matches the source, which places documents on the bidder profile rather than on the registration form.

### Reports
None.

### Notifications
Activation and rejection notify that bidder through Module 14. Other bidders are not notified.

### Security
Verifier remarks meant for the bidder are visible to that bidder. The inbox is not visible to bidders or to auction creators who lack the administrator role.

### Integrations
None.

### Dependencies
F03-001. F01-002 for the verifier. Module 14 for the outcome message.

### Assumptions
- The source does not name a separate verifier role. The System / Catalogue Administrator performs verification unless the organisation assigns that role to the people who should do it.
- Rejection does not require a second approval.

### Risks
A single administrator activating bidders is an operational concentration. The role can be given to more than one person without a scope change.

### Non Functional Requirements
Activation is visible to sign-in immediately.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Bidder verification inbox | UI | Medium | 6 |
| Bidder verification detail | UI | Complex | 12 |
| Verification decision form | UI | Medium | 6 |
| Search pending bidder registrations | API | Medium | 6 |
| Record bidder verification decision | API | Complex | 8 |
| Read bidder verification history | API | Easy | 4 |
| Bidder verification records | DB | Medium | 4 |
| Bidder verification tests | Testing | Complex | 8 |
| Bidder verification notes | Documentation | Medium | 3 |

**Feature total: 57 hours**
