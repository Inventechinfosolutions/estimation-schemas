# F06-002 — Meter Reading Management

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F06-002 |
| **Feature Name** | Meter Reading Management |
| **Module** | 06 — Utilities & Statutory Payments |

### Description
Capture previous/current meter readings, compute units consumed, and validate current ≥ previous with override + reason where allowed (M5-AC1).

### Business Objective
Ensure reliable consumption data for utility billing and recovery.

### Actors
- Utility Officer, Data Entry Operator, Property Manager

### User Journey
1. Officer selects meter and billing/reading period.
2. Enters current reading (previous defaulted from last posted).
3. System validates; if current < previous, require override reason (if permitted) or block.
4. Posts reading; units consumed stored.

### Functional Capabilities
- Period-wise reading entry (single and batch-friendly grid)
- Auto previous reading default
- Units consumed = current − previous (after validation)
- Override with reason + audit when allowed
- Reading history timeline
- Photo of meter optional

### Inputs
- Meter, period, current reading, override reason, photo

### Outputs
- Posted reading; consumed units

### Business Rules
- Current ≥ previous unless override authorized (M5-AC1).
- Corrections via reversal/new reading with audit—not silent edit of posted history.
- Rollover meters (max dial) handled via configured max + rollover flag.

### Validations
- Numeric readings; period uniqueness per meter
- Override permission check

### Calculations
- units_consumed = f(current, previous, rollover)

### Workflow
N/A (direct post with optional approval on override — configurable).

### Search Requirements
By meter, property, period, status, outlier consumption.

### Documents
Meter photos (Module 08).

### Reports
Reading Register; missing readings list.

### Notifications
Alert on missing readings near cut-off (Module 09).

### Security
RBAC; audit overrides heavily.

### Integrations
None.

### Dependencies
F06-001; Module 01 permissions

### Assumptions
- No IoT/AMR integration in baseline.
- Complex UI for building-wise reading grids.

### Risks
- Manual override abuse — report overrides for audit.

### Non Functional Requirements
- Mobile-friendly field entry

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Reading entry list/grid | UI | Complex | 8 |
| Reading capture form + override reason | UI | Medium | 6 |
| Reading validate & post ops | API | Complex | 8 |
| Reading history entities | Database | Medium | 4 |
| Meter reading tests | Testing | Complex | 8 |
| Meter reading guide | Documentation | Medium | 3 |
| **Total** | | | **37** |

### Estimation Assumptions
- Rollover edge cases included in Complex API/testing.
