# F03-004 — Dimension Normalisation & Display Formatting

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-004 |
| Feature Name | Dimension Normalisation & Display Formatting |
| Module | 03 — Dynamic Attribute & Dimension Framework |
| Module Type | Business |
| Release | Go-live |

### Description
Accept dimension input as fractional inches (3/4, 1-1/4, 1 1/4"), decimal inches (0.75 in) or millimetres (19.05 mm); store a canonical numeric value plus the original input; display dimensions in Garrison's preferred format (for example nearest 1/16 inch with optional millimetre equivalent).

### Business Objective
Make specification search and range filters reliable across inconsistent source data, and present dimensions the way Garrison customers expect.

### Actors
- Catalogue Administrator
- Content Administrator
- Data population team

### User Journey
1. **Who creates:** Dimension values are created by administrators during product entry (F04-002) or import (F12-001); this feature provides the parsing and formatting behaviour.
2. **How they create:** The dimension input control parses what the user types and shows a live preview of the normalised value and display format before saving.
3. **How they edit:** Editing a value re-parses and re-normalises; the Catalogue Administrator edits global display settings (fraction precision, metric display) in Dimension display settings.
4. **How they send for approval:** No approval applies to display settings; product dimension values follow the product review workflow.
5. **How the approver sees pending items:** There is no approver inbox on this feature.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Makers see the original input and normalised value on the product history.
8. **How the approver / auditor sees history:** Auditors see display setting changes in the audit log.

### Functional Capabilities
- Parser for fractions, mixed numbers, decimals, inch and millimetre suffixes, and common typos (for example 3/4in, 3/4 in., .75")
- Canonical storage in a single base unit with original input retained
- Display formatting: nearest fraction (1/8, 1/16, 1/32), decimal places, unit symbol, optional metric equivalent
- Global display settings with immediate effect on public pages (cache refresh)
- Conversion test utility for administrators
- Shared parser reused by search (F09-002) and import validation (F12-001)

### UI Screens
- Dimension display settings
- Dimension input control with live parse preview
- Conversion test utility

### Logical API Operations
- Parse dimension input to canonical value
- Format canonical value for display
- Get and save display settings
- Recalculate formatted values after settings change

### Inputs
- Raw dimension text
- Display settings: precision, metric toggle, unit symbol

### Outputs
- Canonical numeric value
- Formatted display string
- Validation message for unparseable input

### Business Rules
- Canonical base unit is inches with four decimal places
- Display rounds to the configured fraction precision; exact canonical value is used for filtering
- Unparseable input is rejected with an example of accepted formats

### Validations
- Value > 0
- Value within plausible range per attribute (configurable min/max, for example 0.125 to 24 inches)

### Calculations
- mm → in = mm ÷ 25.4
- Fraction rounding to nearest 1/16 (configurable)

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Display settings restricted to Catalogue Administrator

### Integrations
- None

### Dependencies
- F03-001
- F04-002
- F09-002
- F09-003
- F12-001

### Assumptions
- Inches are the primary unit; metric display is optional

### Risks
- Ambiguous source notations (for example 11/16 versus 1-1/16) need manual review during population

### Non Functional Requirements
- Parsing is deterministic and identical in UI, import and search

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Dimension display settings | Medium | 6 |
| UI | Dimension input control with live parse preview | Complex | 12 |
| UI | Conversion test utility | Easy | 4 |
| API | Parse dimension input to canonical value | Complex | 8 |
| API | Format canonical value for display | Medium | 6 |
| API | Get and save display settings | Easy | 4 |
| API | Recalculate formatted values after settings change | Complex | 8 |
| Database | Canonical numeric value and original input storage | Easy | 2 |
| Database | Display settings | Simple | 1 |
| Testing | Fraction, decimal and metric parsing cases | Complex | 8 |
| Testing | Rounding and display precision | Medium | 6 |
| Documentation | Dimension entry conventions | Easy | 2 |

**Feature Total: 67 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 26 | 3 | 0 | 14 | 2 | **67** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Parser edge-case coverage drives Complex testing
- Recalculation job refreshes cached display strings
- No external integration channel in this feature; Integration row omitted.
