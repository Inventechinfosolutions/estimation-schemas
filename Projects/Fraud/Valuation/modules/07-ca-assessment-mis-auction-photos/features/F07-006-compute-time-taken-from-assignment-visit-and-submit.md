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
1. Who creates: Competent Authority (reads)
2. How they create: System computes elapsed time from Assignment Date, Date of Visit, and valuer submit timestamp (web or Android) to CA open/decision.
3. How they edit: CA sees those intervals on F07-002 and may add a comment.
4. How they send for approval: CA cannot silently overwrite the computed figures. Missing visit date is flagged. On CA open → compute from stored timestamps → display → comment optional.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Competent Authority (reads) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Competent Authority (reads) opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Compute intervals from assignment, visit, submit, CA open/decision
- Display on CA assessment; optional comment only
- Flag missing visit date
- Refuse silent overwrite of computed figures

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My compute time taken from assignment, visit and submit list / queue | Medium |
| Time Taken interval panel | Easy |
| Compute time taken from assignment, visit and submit history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Interval computation | Complex |
| Update compute time taken from assignment, visit and submit | Medium |
| Search compute time taken from assignment, visit and submit | Medium |
| Read compute time taken from assignment, visit and submit history | Easy |

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
|---|---|---|---|
| My compute time taken from assignment, visit and submit list / queue | UI | Medium | 6 |
| Time Taken interval panel | UI | Easy | 4 |
| Compute time taken from assignment, visit and submit history | UI | Medium | 6 |
| Interval computation | API | Complex | 8 |
| Update compute time taken from assignment, visit and submit | API | Medium | 6 |
| Search compute time taken from assignment, visit and submit | API | Medium | 6 |
| Read compute time taken from assignment, visit and submit history | API | Easy | 4 |
| Compute time taken from assignment, visit and submit persistence | DB | Medium | 4 |
| Assignment/visit/submit timestamp consume | Integration | Simple | 4 |
| Compute Time Taken from assignment, visit and submit feature tests | Testing | Medium | 6 |
| Compute Time Taken from assignment, visit and submit implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **56** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
