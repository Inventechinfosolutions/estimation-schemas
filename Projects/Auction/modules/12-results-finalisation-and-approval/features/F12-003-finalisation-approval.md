# F12-003 — Finalisation Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-003 |
| **Feature Name** | Finalisation Approval |
| **Module** | 12 — Results, Finalisation and Approval |

### Description
The reviewing authority reads the ranking, the selected bidder for each item or lot, and the remarks, then approves the finalisation or sends it back. Award cannot start until this approval is recorded.

### Business Objective
The successful-bidder choice is checked by the approving authority before any award or Letter of Intent.

### Actors
Maker: Finalisation Authority, who submitted. Decider: Reviewing / Approving Authority.

### User Journey
1. Who creates: the reviewing authority creates the approval decision.
2. How they create: Finalisation inbox → open the dossier (ranking, selections, tie notes, remarks) → Approve or Send back.
3. How they edit: they do not change the selected bidder on this screen. Send-back returns that edit to the finalisation authority.
4. How they send for approval: the submission already happened. This is the decision.
5. How the approver sees pending items: the inbox lists submitted finalisations for the department with auction title, notice number, and item or lot count.
6. How the approver decides: Approve, which unlocks award, or Send back with mandatory remarks.
7. How the maker sees history: the finalisation authority sees approved or returned, and the remarks.
8. How the auditor sees history: both roles see the decision, user, and time. Bidders are not notified of this internal approval. They are notified at award.

### Functional Capabilities
- List submitted finalisations
- Read ranking, selection, and remarks
- Approve and unlock award
- Send back with remarks
- Block award while approval is missing or returned

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Submitted finalisation
- Decision
- Remarks when sending back

### Outputs
- Approved finalisation, or a returned selection

### Business Rules
- Only a submitted finalisation can be decided.
- Award and Letter of Intent check this approval.
- Send-back remarks are mandatory.
- The approver does not pick a different bidder here.
- Bidders do not see this inbox.

### Validations
- Status is submitted.
- Send-back has remarks.
- User holds Reviewing / Approving Authority for the department.

### Calculations
None.

### Workflow
Submitted → approved, or submitted → returned → edited → submitted again.

### Search Requirements
Inbox by notice number, title, and status.

### Documents
Read-only auction pack and ranking.

### Reports
None.

### Notifications
Return notifies the finalisation authority. Approval notifies the awarding authority that award can start. Bidders are not mailed at this step.

### Security
Department reviewing role only.

### Integrations
None.

### Dependencies
F12-002. Module 13 waits on approval. Module 14.

### Assumptions
- The approver is the Reviewing / Approving Authority, consistent with the other approval gates in this baseline.

### Risks
An approver who also finalised the result can approve their own selection if both roles are assigned. The source allows that assignment. The decision is still recorded.

### Non Functional Requirements
Award remains unavailable until the approval record exists. A screen refresh cannot skip it.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Finalisation approval inbox | UI | Medium | 6 |
| Finalisation decision dossier | UI | Complex | 12 |
| List pending finalisations | API | Medium | 6 |
| Decide finalisation | API | Complex | 8 |
| Finalisation approval records | DB | Easy | 2 |
| Finalisation approval tests | Testing | Complex | 8 |
| Finalisation approval notes | Documentation | Medium | 3 |

**Feature total: 45 hours**
