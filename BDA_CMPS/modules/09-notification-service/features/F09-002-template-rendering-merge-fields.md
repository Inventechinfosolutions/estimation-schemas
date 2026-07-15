# F09-002 — Template Rendering & Merge Fields

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F09-002 |
| **Feature Name** | Template Rendering & Merge Fields |
| **Module** | 09 — Notification Service |

### Description
Render SMS/email (and in-app text) content from Module 02 notice templates using merge fields supplied by producers, with preview support for operators.

### Business Objective
Ensure consistent, correct messaging content without hard-coding strings in every module.

### Actors
- System, Super Administrator / content owners (preview)

### User Journey
1. Producer supplies template code + merge data bag.
2. Engine loads active template version (F02-010).
3. Renders subject/body; validates required fields; returns content for dispatch.

### Functional Capabilities
- Merge-field substitution
- Channel-specific length checks (SMS advisories)
- Missing-field handling (fail vs blank per config)
- Admin preview with sample payload
- Locale hook (English mandatory; Kannada later)

### Inputs
- Template code, channel, merge data, locale

### Outputs
- Rendered subject/body; validation errors

### Business Rules
- Template configuration owned by F02-010; this feature only renders/dispatches content.
- Active template version only.

### Validations
- Unknown template → fail
- Required merge fields present

### Calculations
None (string merge).

### Workflow
N/A.

### Search Requirements
N/A.

### Documents
N/A.

### Reports
N/A.

### Notifications
N/A.

### Security
Do not log full merge payloads containing Aadhaar/PAN.

### Integrations
Internal read of Module 02 templates.

### Dependencies
F02-010; F09-001

### Assumptions
- Complex API for safe merge + channel rules.
- Rich HTML email supported at baseline; marketing drag-drop builder out of scope.

### Risks
- Incorrect merge causing wrong tenant data — producer contract tests required.

### Non Functional Requirements
- Render latency low enough for OTP paths

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Render preview (admin) | UI | Medium | 6 |
| Template render operations | API | Complex | 8 |
| Render cache/support tables | Database | Easy | 2 |
| Template render tests | Testing | Complex | 8 |
| Template rendering guide | Documentation | Easy | 2 |
| **Total** | | | **26** |

### Estimation Assumptions
- Template CRUD already estimated in F02-010.
