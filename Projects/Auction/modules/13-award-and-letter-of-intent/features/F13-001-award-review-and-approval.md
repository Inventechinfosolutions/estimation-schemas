# F13-001 — Award Review and Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-001 |
| **Feature Name** | Award Review and Approval |
| **Module** | 13 — Award and Letter of Intent |

### Description
After finalisation is approved, the awarding authority reviews the result and the selected bidder for each item or lot, records the award decision and remarks, and approves the award. This is the commercial decision that allows a Letter of Intent. It does not create a contract, a purchase order, or a payment.

### Business Objective
The award is an explicit decision by the awarding authority, made only after the successful bidder has been approved.

### Actors
Maker and decider: Awarding Authority. The finalisation authority prepared the selection. Approver: this authority is the award approver. There is no further committee in the source.

### User Journey
1. Who creates: the Awarding Authority creates the award decision.
2. How they create: Award queue → open an auction whose finalisation is approved → read the result and the selected bidders → Approve award, with remarks.
3. How they edit: until they confirm, they can leave the queue. After confirmation the award remarks are not silently rewritten. A mistaken award is not cancelled inside this scope, because the source has no cancellation after award. Any such case would be a later change request.
4. How they send for approval: the finalisation was already approved. This confirm is the award approval itself.
5. How the approver sees pending items: the queue lists auctions with approved finalisation and no award yet.
6. How the approver decides: Approve award with remarks. There is no send-back on this screen; if the selection is wrong, that should have been sent back at finalisation. The authority who is not prepared to award does not confirm.
7. How the maker sees history: the authority sees the award time, user, and remarks.
8. How the auditor sees history: authorised staff see the award on the auction history. Bidders are not told until the Letter of Intent and the successful-bidder advice.

### Functional Capabilities
- List auctions ready for award
- Show the approved selection and ranking
- Record the award decision and remarks
- Refuse award when finalisation is not approved
- Leave contract and payment out of the action

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Approved finalisation
- Award remarks
- Confirm

### Outputs
- Awarded auction, ready for a Letter of Intent

### Business Rules
- Finalisation approval is a precondition.
- Remarks are mandatory.
- The award covers the selections already approved. The authority does not pick a new bidder here.
- No contract, delivery, or payment record is created.
- The user must hold Awarding Authority for the department.

### Validations
- Finalisation status is approved.
- Remarks are present.
- The auction is not already awarded.

### Calculations
None.

### Workflow
Finalisation approved → award approved → Letter of Intent can be generated.

### Search Requirements
Award queue by notice number and title.

### Documents
Read-only result pack.

### Reports
None.

### Notifications
Award approval notifies the awarding authority’s colleagues who issue the Letter of Intent, through Module 14. The successful bidder is not mailed until F13-003.

### Security
Awarding authority for the department. Bidders cannot open the queue.

### Integrations
None.

### Dependencies
F12-003. F13-002 follows. Module 14.

### Assumptions
- Award is one decision for the auction’s approved selections, not a new negotiation.
- There is no send-back at award because the source’s send-back sits on finalisation. The authority simply does not confirm if they will not award.

### Risks
An award confirmed in error has no reversal in this scope. Operations would need a later change to unwind it.

### Non Functional Requirements
A second confirm does not create a second award.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Award review dossier | UI | Complex | 12 |
| Award decision form | UI | Medium | 6 |
| Read award pack | API | Medium | 6 |
| Record award decision | API | Complex | 8 |
| Award records | DB | Medium | 4 |
| Award tests | Testing | Complex | 8 |
| Award notes | Documentation | Medium | 3 |

**Feature total: 47 hours**
