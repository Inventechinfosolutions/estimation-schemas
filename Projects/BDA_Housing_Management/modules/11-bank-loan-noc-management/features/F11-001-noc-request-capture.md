# F11-001 — NOC Request Capture

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F11-001 |
| **Feature Name** | NOC Request Capture |
| **Module** | 11 — Bank / Loan NOC Management |

### Description
Capture a citizen- or officer-initiated bank/loan NOC request against an eligible booking or allotment, with bank particulars and supporting documents.
### Business Objective
Create a complete, traceable NOC case for bank-loan processing without allowing requests against unrelated property records.
### Actors
- Citizen, NOC Desk officer, Housing/Estate officer
### User Journey
1. Citizen or officer selects the linked booking/allotment and starts an NOC request.
2. Required bank, loan-reference, applicant, property, and document details are provided.
3. BHMS validates eligibility, creates the NOC reference, and routes the case for scrutiny.
### Functional Capabilities
- Citizen and officer entry paths; booking/allotment linkage; bank and loan particulars; document attachment; acknowledgement; draft/submitted status.
### Inputs
- Booking/allotment reference, bank name, loan reference where applicable, applicant/property particulars, supporting documents.
### Outputs
- NOC request number, submitted case status, acknowledgement, and case history entry.
### Business Rules
- A request must relate to the requesting citizen’s eligible booking/allotment, or be created by an authorized officer.
- A duplicate active request for the same bank and property is prevented or flagged for review.
### Validations
- Required linkage, bank details, document types, citizen ownership, and permitted request state.
### Calculations
- None.
### Workflow
- Draft → Submitted → Scrutiny Pending.
### Search Requirements
- Search by NOC number, applicant, booking/allotment, bank, date, and status.
### Documents
- Loan-request support and other BDA-configured NOC documents.
### Reports
- NOC request register and pending-submission list.
### Notifications
- Submission acknowledgement and scrutiny-pending alert through Module 12.
### Security
- Citizens access only their own requests; officers require role-based NOC access; all changes are auditable.
### Integrations
- Internal booking/allotment and document capabilities.
### Dependencies
- Modules 01–02, 07–09, and 12; F11-002.
### Assumptions
- BDA defines mandatory supporting-document types by NOC request category.
### Risks
- Incomplete legacy booking linkage may require officer resolution before submission.
### Non Functional Requirements
- Responsive citizen and officer entry, attachment integrity, and retained case history.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Citizen/officer NOC request form and acknowledgement | UI | Complex | 8 |
| Request capture, eligibility, and search operations | API | Complex | 8 |
| NOC request and attachment-link state | Database | Medium | 4 |
| Request-capture tests | Testing | Complex | 8 |
| NOC request user guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- Estimation uses only Estimation Master values; approval execution is estimated in F11-002.
