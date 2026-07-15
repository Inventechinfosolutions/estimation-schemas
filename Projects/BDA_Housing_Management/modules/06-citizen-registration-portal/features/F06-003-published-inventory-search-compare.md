# F06-003 — Published Inventory Search & Compare

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-003 |
| **Feature Name** | Published Inventory Search & Compare |
| **Module** | 06 — Citizen Registration Portal |

### Description
Expose only published, available housing projects and units for citizen discovery, filtering, detailed viewing, brochure retrieval, and side-by-side comparison.

### Business Objective
Help citizens make informed selections without revealing draft, withdrawn, booked, or restricted inventory.

### Actors
Visitor; Citizen; BDA Content Publisher; Auditor.

### User Journey
A visitor filters published inventory by location, project, BHK, area, price, and availability; opens unit details and media; selects eligible units for comparison; then proceeds to registration or application.

### Functional Capabilities
- Project and unit discovery lists with filter, sort, reset, and no-result states.
- Unit detail view for price components, amenities, photographs, floor plans, brochure, and availability.
- Comparison panel for a bounded set of selected units.

### Inputs
Published project/unit attributes, availability, price components, media, and citizen-selected filters.

### Outputs
Filtered result set, unit comparison, detail view, and brochure/download access.

### Business Rules
Only published projects with active citizen visibility are searchable; booked, cancelled, or withdrawn inventory is not presented as available; comparison uses the current published values.

### Validations
Supported filter ranges, valid project/unit references, comparison selection limit, and document download access.

### Calculations
Displayed total cost from the published unit price components; comparison highlights for price, area, BHK, facing, and availability.

### Workflow
Discover → filter → view detail/download → compare → select apply path.

### Search Requirements
Location, project, property type, BHK, tower/block, area range, price range, facing, amenities, and availability.

### Documents
Published brochures, floor plans, photographs, drawings, and approved supporting files.

### Reports
Citizen inventory-search usage and published-unit enquiry register.

### Notifications
No direct notification; optional saved-search alerts are outside baseline scope.

### Security
Unauthenticated access limited to public inventory; restricted project documents and unpublished values are excluded; downloads are audit logged where configured.

### Integrations
Published inventory/status consumption from Modules 03–05 (Medium).

### Dependencies
Modules 03 inventory, 04 status, and 05 housing-notification publication; F06-004 portal shell.

### Assumptions
Search indexes published BDA data; GIS/map browsing is excluded.

### Risks
Stale availability presentation may create booking expectations; the booking feature remains the authoritative exclusivity control.

### Non Functional Requirements
Fast filter response at peak notification traffic, mobile-responsive cards, and accessible comparison presentation.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Search/filter results and unit detail screens | UI | Very High | 16 |
| Unit comparison and brochure access screen | UI | Complex | 8 |
| Discovery, filter, and comparison processing | API | Complex | 8 |
| Search preference and comparison persistence | Database | Easy | 2 |
| Published inventory hub consumption | Integration | Medium | 16 |
| Discovery and visibility tests | Testing | Complex | 8 |
| Portal discovery guide | Documentation | Medium | 3 |
| **Total** | | | **61** |

### Estimation Assumptions
Inventory publication and unit media maintenance remain in Modules 03–05; this feature consumes approved citizen-visible data.
