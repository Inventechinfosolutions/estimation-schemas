# F07-002 — CA assessment on key parameters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | CA assessment on key parameters |
| **Module** | 07 — CA Assessment, MIS Reports & Auction-Display Photos |

### Description
The Competent Authority opens the valuer report, confirms asset basics via CA Code, and records assessment of Time Taken (shown as computed by F07-006, with optional CA comment), Asset Category, Method Adopted, Adjustment Factors used, Section 7(1) Valuation and Guidance Value. Saving stores the CA report against that valuation.

### Business Objective
Let the CA assess the valuer report on the six key parameters, with Time Taken computed rather than typed from memory as the only source.

### Actors
Competent Authority.

### User Journey
1. Who creates: Competent Authority
2. How they create: CA opens the valuer report and confirms asset basics via CA Code.
3. How they edit: CA records assessment of Time Taken (shown computed by F07-006, optional comment), Asset Category, Method Adopted, Adjustment Factors used, Section 7(1) Valuation and Guidance Value.
4. How they send for approval: Save stores the CA report against that valuation. Open by CA Code → review valuer report → record six parameters → save CA report.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Competent Authority works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Competent Authority opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Populate asset via CA Code
- Assess the six key parameters
- Show computed Time Taken with optional comment (cannot silently overwrite computed figures — F07-006)

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My ca assessment on key parameters list / queue | Medium |
| CA assessment form | Complex |
| Ca assessment on key parameters history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| CA assessment save | Complex |
| Update ca assessment on key parameters | Medium |
| Search ca assessment on key parameters | Medium |
| Read ca assessment on key parameters history | Easy |

### Inputs
CA Code; assessment of category, method, factors, 7(1), guidance; optional Time Taken comment.

### Outputs
Stored CA assessment report.

### Business Rules
- Time Taken on the form is computed (F07-006)
- CA cannot silently overwrite computed intervals
- Physical status shown from F03-005 current

### Validations
- Valuer report available
- Six parameters addressed
- CA Code matches the asset

### Calculations
None here (intervals in F07-006).

### Workflow
Open by CA Code → review valuer report → record six parameters → save CA report.

### Search Requirements
CA Code, asset, assessment saved yes/no.

### Documents
CA Report on Valuation Report & Valuer Assessment.

### Reports
CA assessment report.

### Notifications
None.

### Security
CA Post only to save assessment.

### Integrations
Internal consume of valuer report and F07-006 intervals.

### Dependencies
F07-001; F07-006; F05-007/F05-008/F06 forms; F03-005.

### Assumptions
- CA Code is the programme CA identity on the asset (F02-005).

### Risks
Assessing an unsigned form if the F05-010 gate fails.

### Non Functional Requirements
Assessment attributable to the CA Person.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My ca assessment on key parameters list / queue | UI | Medium | 6 |
| CA assessment form | UI | Complex | 12 |
| Ca assessment on key parameters history | UI | Medium | 6 |
| CA assessment save | API | Complex | 8 |
| Update ca assessment on key parameters | API | Medium | 6 |
| Search ca assessment on key parameters | API | Medium | 6 |
| Read ca assessment on key parameters history | API | Easy | 4 |
| Ca assessment on key parameters persistence | DB | Medium | 4 |
| Time Taken and report consume | Integration | Simple | 4 |
| CA assessment on key parameters feature tests | Testing | Complex | 8 |
| CA assessment on key parameters implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
