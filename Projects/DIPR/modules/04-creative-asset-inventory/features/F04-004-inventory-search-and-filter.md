# F04-004 — Inventory search & filter

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-004 |
| Feature Name | Inventory search & filter |
| Module | 04 — Creative Asset Inventory |
| Description | Search and filter assets by campaign, channel, location, status, and metadata facets. |
| Business Objective | Let officers and verifiers quickly find the creative that should match a field PoD or approval record. |
| Actors | Campaign Officer; PoD Verifier; Asset Manager; Viewer roles |

### User Journey

- User opens Creative Inventory register → applies filters (campaign, channel, language, validity, geotagged, current version only) → sorts by date → opens asset preview (F04-005) → saves filter preset for recurring compliance reviews.

### Functional Capabilities

- Full-text search on title, tags, campaign name
- Faceted filters: channel, format, language, validity window, district/location, version status
- Saved filter presets per user
- Result columns configurable for compliance reviews
- Export asset ID list for bulk operations (not binary export)

### Inputs

- Search terms, filter selections, sort order

### Outputs

- Paginated asset result set

### Business Rules

- Results respect role-based asset access (F04-005)
- Expired assets shown with visual flag unless filter excludes

### Validations

- Export row cap enforced

### Calculations

- None

### Workflow

- Search → refine filters → open asset actions

### Search Requirements

- Sub-second feel for typical filters; indexed metadata fields

### Documents

- CSV of asset IDs and metadata summary

### Reports

- Inventory counts feed Module 07

### Notifications

- None

### Security

- Search results filtered by campaign/vendor scope for limited roles

### Integrations

- None

### Dependencies

- F04-001 metadata; F01 permissions

### Assumptions

- Elasticsearch or equivalent search index is implementation choice, effort captured as API complexity

### Risks

- Missing tags on legacy uploads weaken search until cleanup

### Non Functional Requirements

- Pagination for large digital campaign asset volumes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Creative asset inventory register with facets | Medium | 6 |
| UI | Advanced filter drawer (campaign, channel, date) | Medium | 6 |
| UI | Saved search preset chips | Easy | 4 |
| UI | Asset quick preview modal | Easy | 4 |
| UI | Export filtered inventory to CSV | Easy | 4 |
| UI | Full-text search box with hit highlights | Medium | 6 |
| API | Search assets with composite filters | Complex | 8 |
| API | Save and load user search preset | Easy | 4 |
| API | Export search result set | Medium | 6 |
| API | Facet counts for filter panels | Medium | 6 |
| Database | Search indexes on asset metadata | Medium | 4 |
| Database | Saved search preset storage | Simple | 1 |
| Testing | Filter combination correctness | Medium | 6 |
| Testing | Export row limit enforcement | Easy | 4 |
| Testing | RBAC hides unauthorized assets | Medium | 6 |
| Documentation | Asset inventory search user tips | Easy | 2 |

**Feature Total: 77 hours**

### Estimation Assumptions

- AI visual search is out of scope.
