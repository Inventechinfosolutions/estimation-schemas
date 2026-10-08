# F03-003 — Fee Rules and Attempt History Basis

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Fee Rules and Attempt History Basis |
| **Module** | 03 — Examination, Centre and Fee Masters |

### Description
Examination Administrators configure examination fee rules by candidate category and attempt basis, and the system uses attempt history to distinguish first versus subsequent government registrations. Business rules: first government attempt is free; subsequent government attempts are payable as configured; other-organisation registrations always attract the configured mandatory fee. During registration (Module 04), fee calculation consumes these rules and the candidate’s attempt history for the examination (or Department-defined attempt scope). Payment collection itself is Module 04; this feature owns rule configuration, attempt-history basis resolution and fee determination preview/calculator for Administrators.

### Business Objective
Ensure fee amounts charged at registration correctly reflect category and attempt history so first-time government candidates are not charged incorrectly and other-organisation / subsequent government attempts follow configured payable amounts.

### Actors
Examination Administrator (configures fee rules; previews calculation); Candidate (experiences calculated fee in Module 04); Auditor (read-only rule and attempt-basis history).

### User Journey
1. Who creates: Examination Administrator with fee-master privilege creates fee rules for an examination (or global rule set if Department defines defaults overridden per examination).
2. How they create: Open Fee rules register → New rule → select examination → define government first-attempt = Free → government subsequent amount → other-organisation amount → effective dates → save Active rule.
3. How they edit: Open rule → revise amounts or effective dates → save; superseded rules retained for history and past registrations.
4. How they send for approval: Submit/approval does not apply by default; fee rule activation is administrative with audit. No candidate approval of fees.
5. How the approver sees pending items: There is no approver inbox; Draft vs Active fee rules are filtered on the register. Attempt-history exceptions, if any, are investigative via attempt history view—not an approval queue.
6. How the approver decides: There is no approval decision on fee rules; payment success/failure decisions belong to Module 04 payment feature.
7. How the applicant / maker sees history: Administrator opens fee rule change history and can run fee calculation preview for a sample category/attempt count.
8. How the approver / auditor sees history: Auditor opens rule history and attempt-history basis records used for past fee determinations (as stored for audit).

### Functional Capabilities
- Maintain fee rule register per examination (and optional default template) with create, edit, activate and supersede.
- Configure first government attempt as Free (zero payable).
- Configure subsequent government attempt payable amount.
- Configure mandatory other-organisation fee amount.
- Define attempt history basis (count prior registrations/attempts for same examination / same candidate identity as Department directs).
- Resolve attempt count for a candidate identity when previewing or when called by registration fee calculation.
- Provide Administrator fee calculation preview (category + attempt count → payable amount).
- Effective-date control so rule changes do not silently rewrite historical fee determinations.
- Prevent Active overlapping rules for the same examination/category/attempt band unless Department allows priority rules.
- Audit rule changes with before/after amounts.
- Support search of rules by examination, category, status and effective dates.
- Expose calculated fee result structure for Module 04 payment gate (amount, currency/INR, fee basis reason text).

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Fee rules register and search | Complex |
| Fee rule create / edit by category and attempt | Complex |
| Attempt history basis configuration | Medium |
| Fee calculation preview / simulator | Complex |
| Attempt history lookup for candidate sample | Medium |
| Fee rule change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save fee rule configuration | Complex |
| Activate or supersede fee rule | Medium |
| Resolve attempt history for candidate | Complex |
| Calculate applicable fee | Complex |
| Search fee rules | Medium |
| Fee calculation preview | Medium |
| Read fee rule change history | Easy |

### Inputs
Examination reference; category (Government / Other organisation); attempt band (first / subsequent); amounts; effective from/to; attempt-basis definition; sample candidate identity for preview; Administrator remarks.

### Outputs
Active fee rules; resolved attempt count; calculated payable amount and basis reason; preview results; rule change history; fee determination payload for registration.

### Business Rules
- First government attempt is free.
- Subsequent government attempts are payable as configured.
- Other-organisation fee is mandatory (non-zero unless Department explicitly configures zero—default is payable amount required).
- Fee calculation must use category and attempt history correctly.
- Historical registrations retain the fee basis determined at registration time; changing rules does not rewrite past payments.
- Attempt history for fee logic begins from registrations in this system unless historical attempt data is formally provided (SOW migration assumption).

### Validations
- Amounts ≥ 0; subsequent government and other-organisation amounts mandatory when those bands are enabled.
- Effective date ranges valid; no unintended Active overlap for same band.
- Examination reference must exist (F03-001).
- Preview requires category and enough identity/attempt inputs to resolve basis.
- Cannot activate rule without all mandatory bands defined for the examination.

### Calculations
Payable fee = rule amount for (category, attempt band); attempt band = first if attempt_count == 0 (or Department definition of first), else subsequent for government; other-organisation always uses other-org amount. Currency INR as Department standard.

### Workflow
Configure rules → Activate → registration calls calculate fee → payment in Module 04. No maker–checker for rule save by default. Supersede creates new Active version and closes prior.

### Search Requirements
Examination, category, attempt band, status, effective dates, updated by.

### Documents
None.

### Reports
Fee rule listing export; optional fee-basis summary counts for open examinations (operational).

### Notifications
None required on rule save; payment notifications belong to Module 04 / 09.

### Security
Only fee-master privileged Administrators mutate rules; attempt history lookup limited to need-to-know; calculated fee basis stored for audit with registration; no candidate edit of fee rules.

### Integrations
None in this feature (payment gateway is Module 04). Attempt history is internal to Examination Module data.

### Dependencies
F03-001 Examination Catalogue; consumed by Module 04 Fee Calculation and Payment. Candidate identity and prior registrations from Module 04 supply attempt history.

### Assumptions
- Legacy attempt migration is out of scope unless Department supplies extracts; otherwise first attempt is first in this system.
- Hours use Estimation Master; Calculate applicable fee is Complex (business rules + transactional determination), not a payment gateway Integration.
- Each named screen and logical API billed independently.

### Risks
- Incorrect attempt counting could charge first-time government candidates or waive fees incorrectly.
- Overlapping Active rules could produce ambiguous amounts.
- Treating other-organisation as free would violate mandatory fee acceptance criteria.

### Non Functional Requirements
Fee calculation must be deterministic and auditable; preview and registration-time calculation must return the same result for the same inputs; rule changes must be attributable; performance suitable for registration peak fee determinations.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Fee rules register and search | UI | Complex | 12 |
| Fee rule create / edit by category and attempt | UI | Complex | 12 |
| Attempt history basis configuration | UI | Medium | 6 |
| Fee calculation preview / simulator | UI | Complex | 12 |
| Attempt history lookup for candidate sample | UI | Medium | 6 |
| Fee rule change history | UI | Medium | 6 |
| Save fee rule configuration | API | Complex | 8 |
| Activate or supersede fee rule | API | Medium | 6 |
| Resolve attempt history for candidate | API | Complex | 8 |
| Calculate applicable fee | API | Complex | 8 |
| Search fee rules | API | Medium | 6 |
| Fee calculation preview | API | Medium | 6 |
| Read fee rule change history | API | Easy | 4 |
| Fee rules and attempt basis persistence | DB | Complex | 6 |
| Fee rules feature tests | Testing | Very High | 12 |
| Fee rules implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **121** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- No Integration row — payment gateway is estimated under Module 04 payment feature, not here.
- Testing is Very High for category × attempt-band matrix and supersede/effective-date cases.
- Each named UI screen and logical API estimated separately.
