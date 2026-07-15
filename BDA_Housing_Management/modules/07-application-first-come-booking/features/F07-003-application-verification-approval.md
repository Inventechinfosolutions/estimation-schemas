# F07-003 — Application Verification & Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | Application Verification & Approval |
| **Module** | 07 — Application First Come Booking |

### Description
Enable officers to scrutinise submitted applications, record deficiencies, request clarification, and route completed applications through BDA’s configured approval process.

### Business Objective
Ensure only complete and valid applications become eligible for booking confirmation.

### Actors
Housing/Estate Officer; Configured Approvers; Citizen; Auditor.

### User Journey
An officer opens a pending application, checks the required details/documents, records verification findings, sends a clarification request where needed, or recommends it for approval; each configured approver acts with remarks until the application is approved or rejected.

### Functional Capabilities
- Verification queue, checklist, document review, and deficiency/clarification actions.
- Configured approval worklist with approve, reject, send back, hold, reassign, delegate, and clarification actions.
- Status history and approved-application handoff to booking.

### Inputs
Submitted application, verification checklist, document findings, officer remarks, approver action, and clarification response.

### Outputs
Verified/approved/rejected application, deficiency record, approval history, and booking-eligible status.

### Business Rules
Only submitted complete applications are scrutinised; configured approval sequence governs decision rights; an application is booking-eligible only after successful verification and all required approvals; maker-checker constraints apply.

### Validations
Required checklist disposition, approver authority, mandatory remarks for reject/send-back/hold, valid reassignment/delegation, and current application state.

### Calculations
Verification ageing, clarification turnaround, approval pendency, and checklist completion.

### Workflow
Submitted → verification → clarification requested/resubmitted or recommended → multi-level approval → approved/rejected → booking eligible.

### Search Requirements
Application number, project, unit, citizen, verifier, approval stage, status, submission date, and ageing.

### Documents
Submitted documents, scrutiny checklist, deficiency communication, clarification responses, and approval notes.

### Reports
Application verification register, approval pendency, deficiency ageing, and rejection reason report.

### Notifications
Clarification requests, approval tasks, approval/rejection outcomes through Module 12.

### Security
Role-based queues, maker-checker separation, immutable decision history, and citizen access limited to external-facing status/requests.

### Integrations
Configured workflow consumption from Module 02 (Medium) and notifications via Module 12 (Easy).

### Dependencies
F07-001, F07-002, F07-004; Modules 01, 02, and 12.

### Assumptions
Workflow definitions and permission mappings are maintained outside this feature.

### Risks
Unclear document criteria or stalled approvals can delay booking conversion.

### Non Functional Requirements
Auditable action timestamps, responsive worklists, and reliable state transition integrity.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Verification queue, checklist, and deficiency UI | UI | Very High | 16 |
| Approval worklist and decision timeline | UI | Very High | 16 |
| Verification, clarification, and approval processing | API | Very High | 16 |
| Verification and approval-history persistence | Database | Complex | 6 |
| Workflow and notification consumption | Integration | Medium | 16 |
| Verification and approval tests | Testing | Very High | 12 |
| Verification procedure guide | Documentation | Complex | 4 |
| **Total** | | | **86** |

### Estimation Assumptions
Workflow configuration is Module 02; this estimate covers runtime application verification and approval usage.
