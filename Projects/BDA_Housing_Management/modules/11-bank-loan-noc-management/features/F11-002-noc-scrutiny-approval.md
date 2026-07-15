# F11-002 — NOC Scrutiny & Approval

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F11-002 |
| **Feature Name** | NOC Scrutiny & Approval |
| **Module** | 11 — Bank / Loan NOC Management |

### Description
Enable NOC Desk scrutiny and configured multi-level approval of submitted NOC requests, including clarification, rejection, hold, delegation, and decision history.
### Business Objective
Ensure an NOC is issued only after property linkage, documents, and approval requirements have been satisfied.
### Actors
- NOC Desk officer, designated approvers, Housing/Estate officer, Citizen
### User Journey
1. NOC Desk opens a submitted case and verifies its linked record and documents.
2. The case is sent through configured approval levels, or returned for clarification.
3. The final decision is recorded; approved cases become ready for letter issuance.
### Functional Capabilities
- Scrutiny checklist; remarks; approval actions; configured-level routing; delegation/reassignment; clarification loop; decision timeline.
### Inputs
- NOC case, supporting documents, scrutiny result, approver remarks, configured approval assignment.
### Outputs
- Scrutiny outcome, approval status, full decision history, and issuance-ready case.
### Business Rules
- Only configured approvers may act at their assigned level.
- Rejected, withdrawn, or incomplete cases cannot proceed to issuance.
### Validations
- Required scrutiny findings, active approver assignment, valid action/status transition, and mandatory remarks for adverse actions.
### Calculations
- Approval-pendency counts only.
### Workflow
- Scrutiny Pending → Under Approval → Approved / Rejected / Sent Back / On Hold.
### Search Requirements
- Filter by status, assigned approver, bank, project, pending age, and decision date.
### Documents
- Submitted support, scrutiny evidence, and approval remarks.
### Reports
- NOC approval pendency and decision register.
### Notifications
- Assignment, clarification, approval, rejection, and overdue-pendency alerts through Module 12.
### Security
- Segregation of request, scrutiny, and approval actions; immutable action trail.
### Integrations
- Configured approval definitions from Module 02 and notifications from Module 12.
### Dependencies
- Modules 01–02 and 12; F11-001 and F11-003.
### Assumptions
- NOC approval levels are maintained through the shared workflow configuration.
### Risks
- Delayed approver mapping can leave submitted NOC cases unassigned.
### Non Functional Requirements
- Timely role-based work queues, complete audit history, and no loss of in-progress decisions.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Scrutiny and approval workbench | UI | Very High | 16 |
| NOC approval workflow operations | API | Very High | 16 |
| Scrutiny, action, and history state | Database | Complex | 6 |
| Approval workflow tests | Testing | Very High | 12 |
| NOC approval guide | Documentation | Complex | 4 |
| **Total** | | | **54** |

### Estimation Assumptions
- The shared approval configuration is consumed; this estimate covers NOC runtime scrutiny and decisions only.
