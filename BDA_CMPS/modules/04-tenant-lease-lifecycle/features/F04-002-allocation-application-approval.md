# F04-002 — Allocation Application & Approval

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F04-002 |
| **Feature Name** | Allocation Application & Approval |
| **Module** | 04 — Tenant & Lease Lifecycle |

### Description
Manage allotment intake from property availability through application capture, verification, and approval prior to lease creation.

### Business Objective
Govern transparent allotment against vacant/ready units from Module 03 vacancy pipeline.

### Actors
- Estate Officer, Property Manager
- Verifiers / Approvers
- Applicant data entry (officer on behalf of applicant)

### User Journey
1. Officer checks unit availability (Vacant + ready-for-allocation).
2. Captures application against unit(s)/parking.
3. Verification checklist completed.
4. Approval per configured workflow.
5. On approval, lease creation (F04-003) can proceed.

### Functional Capabilities
- Availability check against Module 03 status/ready flag
- Application capture (applicant/tenant, units, proposed rent, remarks)
- Verification stage with findings
- Multi-level approval (F02-009)
- Reject/return with reasons; audit trail
- Soft-reserve unit on application submit (status Reserved) configurable

### Inputs
- Unit refs, tenant/applicant, proposed terms, verification notes, approval action

### Outputs
- Application record in workflow states
- Unit reserve effect
- Approval completion event for lease create

### Business Rules
- Cannot apply for Blocked / Under Litigation / Occupied units.
- Auction bidding portal out of scope; Auctioned status units may use post-auction application capture.
- Approved application required before lease activation (M3-AC1).

### Validations
- Unit available; tenant exists or applicant minimum fields
- Mandatory verification items before submit to approval

### Calculations
None significant.

### Workflow
Availability → Application → Verification → Approval → (Lease).

### Search Requirements
By application no., unit, tenant, stage, date.

### Documents
Application supporting docs via Module 08.

### Reports
Application Register; pending approval ageing.

### Notifications
Task alerts to verifiers/approvers (Module 09).

### Security
RBAC; SoD between data entry and approve where configured.

### Integrations
None (internal status update to Module 03).

### Dependencies
Module 03 vacancy/status; F02-009; F04-001; F04-003

### Assumptions
- Wizard UI = Very High; workflow API = Very High.
- Public citizen self-application portal not in baseline (officer-mediated).

### Risks
- Double-booking if reserve rules weak — enforce transactional reserve.

### Non Functional Requirements
- Work queue usable daily; mobile-friendly review screens preferred

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Availability & application list | UI | Complex | 8 |
| Application capture wizard | UI | Very High | 16 |
| Verification & approval work queue | UI | Complex | 8 |
| Application workflow operations | API | Very High | 16 |
| Application entities | Database | Medium | 4 |
| Allocation application tests | Testing | Very High | 12 |
| Allocation application guide | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- E-auction engine excluded.
