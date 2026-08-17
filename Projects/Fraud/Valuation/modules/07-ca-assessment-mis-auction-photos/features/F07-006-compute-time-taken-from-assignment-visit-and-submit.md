# F07-006 — Compute Time Taken from assignment, visit and submit

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-006 |
| **Feature Name** | Compute Time Taken from assignment, visit and submit |
| **Module** | 07 — CA Assessment, MIS Reports & Auction-Display Photos |

### Description
The system computes elapsed time from Assignment Date (F04-001), Date of Visit (F04-008) and valuer submit timestamp (web or Android F09-005) to CA open/decision. The CA sees those intervals on the assessment form (F07-002) and may add a comment; the CA cannot silently overwrite the computed figures. Missing visit date is flagged.

### Business Objective
Show Time Taken as computed intervals from stored dates, not as the CA’s memory as the only source.

### Actors
Competent Authority (reads); system computes.

### User Journey
1. System computes elapsed time from Assignment Date, Date of Visit, and valuer submit timestamp (web or Android) to CA open/decision.
2. CA sees those intervals on F07-002 and may add a comment.
3. CA cannot silently overwrite the computed figures. Missing visit date is flagged.

### Functional Capabilities
- Compute intervals from assignment, visit, submit, CA open/decision
- Display on CA assessment; optional comment only
- Flag missing visit date
- Refuse silent overwrite of computed figures

### Inputs
Assignment Date; Date of Visit; submit timestamp; CA open/decision timestamps.

### Outputs
Computed intervals; missing-visit flag; optional CA comment.

### Business Rules
- Computed figures are authoritative
- CA comment does not replace them
- Missing visit date flagged

### Validations
- Assignment Date present
- Submit timestamp present when submitted

### Calculations
Elapsed time Assignment→Visit, Visit→Submit, Submit→CA open/decision (calendar rules as Authority confirms; default elapsed between stored timestamps).

### Workflow
On CA open → compute from stored timestamps → display → comment optional.

### Search Requirements
Asset, missing visit date, Time Taken band.

### Documents
None.

### Reports
Time Taken extract for CA MIS.

### Notifications
In-app missing visit date flag.

### Security
CA sees; valuers do not overwrite CA intervals.

### Integrations
Internal timestamps from F04-001, F04-008, F09-005.

### Dependencies
F04-001; F04-008; F09-005; F07-002.

### Assumptions
- Authority confirms whether elapsed is calendar days or working days; default calendar elapsed.

### Risks
Clock skew between Android submit and server.

### Non Functional Requirements
Store computed snapshot at CA open so later date edits are visible as recalculation with audit.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Time Taken interval panel | UI | Easy | 4 |
| Interval computation | API | Complex | 8 |
| Computed interval snapshot | Database | Easy | 2 |
| Assignment/visit/submit timestamp consume | Integration | Simple | 4 |
| Time Taken tests | Testing | Medium | 6 |
| Time Taken note | Documentation | Easy | 2 |
| **Total** | | | **26** |

### Estimation Assumptions
- Computation is this feature; display-on-CA-form also referenced from F07-002.
