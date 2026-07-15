# F02-010 — Notice Template Configuration

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-010 |
| **Feature Name** | Notice Template Configuration |
| **Module** | 02 — Master Data & System Configuration |

### Description
Configure notice templates for SMS, email, and PDF channels with merge fields from tenant/lease/dues data, used by notice generation and Notification Service.

### Business Objective
Standardize communication content for rent due/overdue, lease expiry, utility/tax due, legal/eviction templates, and related alerts without code changes.

### Actors
- Super Administrator
- Revenue / Estate officers (content owners as permitted)

### User Journey
1. Admin creates a template for a notice type and channel.
2. Inserts merge fields from controlled catalogue.
3. Previews with sample data.
4. Activates version for Module 09 / business notice batch jobs.

### Functional Capabilities
- Templates per notice type and channel (SMS/email/PDF)
- Merge-field catalogue (tenant, lease, property, dues, dates)
- Versioning / activate-deactivate
- Preview sample render
- Search and export template catalogue

### Inputs
- Notice type, channel, subject/body, merge fields, locale (English mandatory; Kannada optional later), status

### Outputs
- Versioned templates
- Preview content
- Catalogue export

### Business Rules
- Only active template version used for new dispatches.
- SMS length warnings for concatenated messages.
- PDF templates support header/footer basic branding fields.
- Legal notice templates are content containers; legal process remains offline.

### Validations
- Required merge fields validated against catalogue
- Channel-specific constraints (SMS length advisory)
- Unique active template per notice type + channel (or priority)

### Calculations
None (render preview only).

### Workflow
Optional content approval before activation.

### Search Requirements
By notice type, channel, status, language.

### Documents
PDF template samples stored via Module 08 optional.

### Reports
Template Catalogue.

### Notifications
N/A (templates consumed by Module 09).

### Security
Configure permission; audit versions; restrict who can activate legal templates.

### Integrations
None directly; consumed by Module 09 and business modules.

### Dependencies
Module 01; Module 09 for dispatch; Modules 04–06 for merge data producers.

### Assumptions
- Kannada content optional; English mandatory at go-live.
- Rich HTML email supported at Medium/Very High designer level; full drag-drop marketing builder out of scope.
- Batch selection logic remains in business modules.

### Risks
- Incorrect merge fields leak wrong tenant data — preview + test pack mandatory.
- Legal wording ownership must sit with BDA.

### Non Functional Requirements
- Preview accurate to dispatch rendering
- Version history retained

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Notice template list | UI | Medium | 6 |
| Template editor with merge fields | UI | Very High | 16 |
| Template CRUD + versioning | API | Complex | 8 |
| Template entities | Database | Medium | 4 |
| Template merge tests | Testing | Complex | 8 |
| Notice template guide | Documentation | Medium | 3 |
| **Total** | | | **45** |

### Estimation Assumptions
- Template editor = Very High dynamic UI.
- SMS/email gateway effort in Modules 09/10.
