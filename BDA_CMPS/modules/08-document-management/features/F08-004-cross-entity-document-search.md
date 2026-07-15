# F08-004 — Cross-entity Document Search

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F08-004 |
| **Feature Name** | Cross-entity Document Search |
| **Module** | 08 — Document Management |

### Description
Search documents by property, tenant, lease, document type/category, tags, date, and other metadata, returning only ACL-visible results (M7-AC4).

### Business Objective
Enable officers to find artefacts quickly across the portfolio for operations, audit, and disputes.

### Actors
- Officers with document view permission, Auditor

### User Journey
1. User opens Document Search.
2. Enters criteria (property, tenant, lease, type, date range, tags, filename).
3. Reviews results; opens preview/download if allowed.

### Functional Capabilities
- Multi-criteria search and facets
- Results respect F08-003 ACL and Module 01 data scope
- Sort by date/name/category
- Export result metadata (not bulk zip of files unless permitted)

### Inputs
- Search criteria

### Outputs
- Ranked/filtered result list

### Business Rules
- Document search returns results by property, tenant, lease, and document type (M7-AC4).
- No results leakage across tenants/properties outside scope.

### Validations
- Date range limits for performance

### Calculations
None (relevance ranking optional simple).

### Workflow
N/A.

### Search Requirements
Primary capability of this feature.

### Documents
N/A.

### Reports
Search result export (metadata).

### Notifications
None.

### Security
Enforce ACL on each hit; no ID enumeration via timing if practical.

### Integrations
None (dedicated search service not a separate module).

### Dependencies
F08-001–003; Module 01 scope

### Assumptions
- DB indexes / optional full-text on metadata; OCR content search out of baseline.

### Risks
- OCR demands later — exclude from this estimate.

### Non Functional Requirements
- Search < 3s typical within date/scoped filters

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Advanced document search UI | UI | Complex | 8 |
| Search & facet query ops | API | Complex | 8 |
| Search indexes/support | Database | Medium | 4 |
| Document search tests | Testing | Complex | 8 |
| Document search guide | Documentation | Easy | 2 |
| **Total** | | | **30** |

### Estimation Assumptions
- Content OCR/full-text inside files not included.
