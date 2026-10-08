# SoW GPM — Detailed Statement of Work

## Garrison Catalogue Product Migration to Existing Website (Option B)

**Client:** Garrison Industries  
**Project code:** GPM  
**Document type:** Detailed Statement of Work (estimation ready)  
**Version:** 1.0  
**Relationship to other proposals:** Alternative to the full Online Moulding Catalogue Platform (Option A, project code GMC). Option B moves catalogue products onto the existing Garrison website without an administration portal.

---

## 1. Introduction

Garrison Industries wants the moulding products shown in the Brenlo online catalogue (https://brenlo.com/catalogue/) to appear on its existing website, www.garrisonindustries.ky. This option is a **product migration**: extract the products from the source catalogue, prepare them, and publish them as catalogue pages inside the existing website using its current technology and theme.

Option B does not provide an administration portal, publishing workflow or configurable product framework. After go-live, product changes are made by a developer updating the prepared dataset and re-running the loader.

## 2. Project Overview

| Item | Description |
|------|-------------|
| Source | Brenlo public online catalogue: Moulding section (by category and style) |
| Target | Existing Garrison website (www.garrisonindustries.ky), modified in its source code |
| Business problem | Garrison's current mouldings page does not list individual profiles |
| Outcome | Browsable, searchable moulding catalogue pages on the Garrison website with an enquiry action |
| Maintenance model | Developer-maintained dataset and loader (no admin portal) |

### 2.1 Source catalogue observations (from review of the public catalogue)

| Observation | Implication |
|-------------|-------------|
| Moulding catalogue organised by 37 moulding types (Apron … Window Stool), styles (Classic, Modern, Transitional, Inspire Series) and Combinations | Category and style taxonomy can be mirrored or mapped to Garrison names |
| 201 products confirmed across 21 single-word categories (for example Casing 41, Baseboard 45, Backband 21, D4S 21, Crown 18, Doorstop 10); 16 further categories could not be counted remotely | Planning quantity set at **350 moulding products**; actual count confirmed at the start |
| Each product exposes: category, product code, thickness × width (fractional inches), style, species options and one isometric profile image | Data per product is compact; migration effort per product is low |
| No technical drawings, PDFs or long descriptions are exposed per product | Product pages show image, dimensions, style and species only unless Garrison supplies more content |
| Interior Doors and In-Stock sheet goods (MDF, Plywood, Frogboard) are separate catalogue sections | Treated as optional extensions |

## 3. Project Objectives

1. Publish the agreed Brenlo moulding products on the existing Garrison website with category, style, dimensions, species and image.
2. Replace the current mouldings page with a catalogue landing page, category listings with filters, product detail pages and search.
3. Let visitors send an enquiry about a specific product through the existing contact mechanism.
4. Keep the existing website's look, navigation and hosting.
5. Provide a repeatable, documented process to refresh products from the prepared dataset.

## 4. In Scope / Out of Scope

### In Scope

- Onboarding of the existing website source code; local and staging environments; technical assessment
- Automated, rate-limited extraction of Brenlo moulding products (or ingestion of a data file supplied by Brenlo, if available)
- Image download, renaming and web optimisation
- Data normalisation (dimensions, categories, styles, species), duplicate checks and validation
- Garrison review workbook and incorporation of include/exclude/rename decisions
- Product data store and idempotent loader inside the existing website stack
- Catalogue landing page, category listings with filters, product detail pages, search and enquiry handoff
- Navigation and theme integration, SEO-friendly URLs, metadata, sitemap and redirect of the old mouldings page
- Reconciliation report, testing, UAT support, production deployment and handover

### Out of Scope

- Administration portal, user roles, review/publishing workflow (available in Option A)
- Configurable attribute templates and dynamic categories (Option A)
- Content creation (new descriptions, technical drawings, PDFs, installation photos)
- Interior Doors, In-Stock sheet goods and Combinations (optional extensions)
- Website redesign, hosting migration, SSL certificate remediation, e-commerce, pricing or quoting
- Obtaining permission from Brenlo to reproduce its product data and images (Garrison responsibility)

## 5. Solution Expectations (Business-level Only)

- Catalogue pages look and behave as part of the current Garrison website.
- Product data is held in one prepared dataset, which is the single source for website pages.
- Re-running the loader refreshes products without duplicates and can be rolled back.
- Extraction respects the source website: throttled requests, no login, no circumvention of access controls.

## 6. Consolidated Functional Modules

### 01. Catalogue Data Extraction & Preparation

**Purpose:** Turn the source catalogue into a clean, Garrison-approved product dataset with optimised images.

**Functional requirements:**
- Extract product records and image references from the source catalogue by category and style, or ingest a supplier data file.
- Download and optimise product images.
- Normalise dimensions, map categories, styles and species, detect duplicates and validate.
- Produce a review workbook for Garrison and apply its decisions.

**Acceptance criteria:**
- The master dataset reconciles with the source counts per category, with every exception explained.
- Garrison signs off the reviewed dataset before loading.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Source Catalogue Extraction Utility | Throttled extraction of product records and image references from the source catalogue |
| F01-002 | Product Image Acquisition & Optimisation | Image download, renaming and web derivative generation |
| F01-003 | Data Normalisation & Validation | Dimension parsing, taxonomy mapping, duplicate checks and master dataset build |
| F01-004 | Garrison Review Workbook & Sign-off | Review workbook export and import of Garrison decisions |
| F01-005 | Interior Doors & In-Stock Product Extension | Optional extraction and pages for doors and sheet goods |

---

### 02. Product Data Store on Existing Website

**Purpose:** Hold the approved products inside the existing website stack and load them repeatably.

**Functional requirements:**
- Create product storage (database tables or structured data files, per the existing stack).
- Provide an idempotent loader with rollback and a data access layer for catalogue pages.
- Place optimised images on the web server or storage path with caching.

**Acceptance criteria:**
- Re-running the loader with the same dataset produces no changes; a changed dataset updates only affected products.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Product Data Store & Loader | Product storage, idempotent loader, rollback and data access layer |
| F02-002 | Media Hosting & Delivery Setup | Image placement, caching and lazy loading on existing hosting |

---

### 03. Catalogue Pages on Existing Website

**Purpose:** Present the migrated products to visitors within the current website.

**Functional requirements:**
- Mouldings landing page with category tiles and search.
- Category listing pages with filters (style, thickness, width, species), sort and pagination.
- Product detail page with image, code, category, style, dimensions, species, similar products and Request Information.
- Search by code, category, style and dimension keywords.
- Enquiry handoff to the existing contact form or email with product context.

**Acceptance criteria:**
- A visitor can go from the mouldings page to a product and send an enquiry that names the product.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Mouldings Landing Page | Replacement mouldings page with category tiles and search entry |
| F03-002 | Category Listing Page with Filters | Product grid by category with style and dimension filters |
| F03-003 | Product Detail Page | Product page with image, dimensions, species, similar products and enquiry action |
| F03-004 | Catalogue Search | Search by code, category, style and dimensions |
| F03-005 | Product Enquiry Handoff | Product-aware link into the existing contact form or email |
| F03-006 | Combinations Pages | Optional listing and detail pages for moulding combinations |

---

### 04. Website Integration, SEO & Go-live

**Purpose:** Safely change the existing website, keep it consistent, and launch the catalogue.

**Functional requirements:**
- Onboard source code; set up local and staging environments; back up the live site.
- Integrate navigation and theme.
- SEO-friendly URLs, metadata, sitemap, structured data and redirect of the old mouldings page.
- Reconciliation report, UAT support, production deployment with rollback, handover.

**Acceptance criteria:**
- Staging is signed off by Garrison; production deployment completes with a rollback path and no regression on existing pages.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Source Code Onboarding & Environment Setup | Code access, stack assessment, local/staging environments, live backup |
| F04-002 | Navigation & Theme Integration | Mouldings menu and catalogue styling within the existing theme |
| F04-003 | SEO, Sitemap & Redirects | URLs, metadata, sitemap, structured data and legacy redirect |
| F04-004 | Migration Reconciliation & Go-live | Reconciliation report, UAT support, deployment and handover |

---

## 7. End-to-End Workflow

Source code onboarding → extraction run → image download and optimisation → normalisation and validation → Garrison review workbook → decisions applied → master dataset frozen → loader run on staging → catalogue pages verified → reconciliation report → UAT sign-off → production deployment → handover.

Product refresh after go-live: developer updates the dataset (or re-runs extraction) → validation → loader on staging → verification → production.

## 8. Access Control

No administration portal or user roles. Catalogue pages are public. Dataset and loader are used only by developers with server access.

## 9. Channels

Existing Garrison website (desktop, tablet, mobile). No mobile app.

## 10. Integrations

| Integration | Purpose | Notes |
|-------------|---------|-------|
| Brenlo public catalogue | Read-only source of product data and images | Throttled extraction, or supplier data file if Brenlo provides one |
| Existing Garrison website | Target pages, theme, routing, contact form | Requires source code and server access |
| Existing contact form / email | Enquiry handoff | Reuses Garrison's current mechanism |

## 11. Compliance & Security

- **Content rights:** Brenlo's product images, codes and data are Brenlo's content. Garrison must obtain Brenlo's written permission (for example under a dealer or distribution arrangement) before publication. Pages can carry "Brenlo" attribution if required.
- Extraction uses public pages only: no login, no bypassing of blocks, rate-limited.
- Changes to the existing website are deployed via staging with a full backup and rollback.
- Input handling on new pages (search, filters, enquiry parameters) is validated and escaped.

## 12. Non-Functional Requirements

| Area | Requirement |
|------|-------------|
| Performance | Listing and product pages load quickly; images optimised and lazy-loaded |
| Compatibility | Current Chrome, Edge, Safari and Firefox; responsive layouts |
| Maintainability | Documented dataset format and loader procedure |
| SEO | Crawlable product and category pages with unique titles and sitemap entries |

## 13. Data Migration

| Item | Planning basis |
|------|----------------|
| Moulding products | 350 (201 confirmed + estimate for categories not countable remotely) |
| Images | One isometric image per product (about 350) |
| Per-product verification | Spot check of image, code, dimensions, style, species and category mapping after automated extraction |
| Variance | Products beyond the planning quantity are charged at the per-product rate |

## 14. Phased Delivery

1. Onboarding and assessment.
2. Data extraction and preparation, with Garrison review.
3. Website build: data store, pages, integration and SEO.
4. Testing, reconciliation, go-live.

Optional extensions: Combinations pages (F03-006); Interior Doors and In-Stock products (F01-005).

## 15. Deliverables

- Catalogue pages on the existing Garrison website
- Master product dataset (CSV/JSON) and optimised image set
- Extraction utility, normalisation scripts and loader with procedure document
- Data dictionary and taxonomy mapping sheet
- Reconciliation report and UAT results
- Technical assessment note and go-live/handover document

## 16. Acceptance Criteria (Program Level)

| Perspective | Criterion |
|-------------|-----------|
| Visitor | Can browse, filter, search, view a product and send a product enquiry |
| Garrison | Approved product set is live with correct images and dimensions |
| Data | Reconciliation report shows the agreed product count published with zero unexplained gaps |
| Technical | No regression on existing website pages; rollback tested |

## 17. Expected Benefits

- Fast, low-cost path to a populated moulding catalogue on the current website.
- No platform change or retraining of Garrison staff.
- Can later be upgraded to the full platform (Option A), since the dataset is reusable for import.

## 18. Assumptions & Dependencies

1. **Source code (go/no-go):** Garrison owns and provides the complete, current source code of www.garrisonindustries.ky (templates, themes, plugins, build files and database), with the right to modify it, plus server/hosting access (SSH/FTP), database access and any build tooling. No admin logins are currently available, so all changes are made in code. If the source code cannot be provided or does not match the live site, this estimate does not apply and will be revised (page rebuild or Option A).
2. The existing website is a custom or common web stack (for example PHP/WordPress/Node) that can host new templates and a data store.
3. Garrison obtains Brenlo's permission to reproduce product data and images before go-live.
4. Planning quantity: 350 moulding products; the actual count is confirmed after the first extraction run.
5. The source catalogue remains reachable for automated extraction. If it is blocked, a manual capture rate applies.
6. No new content is written; product pages use source data only.
7. Enquiries reuse the existing contact form or email address.
8. Hosting, domain and SSL certificate issues are Garrison's responsibility.

## 19. Vendor Response Expectations

- Confirm the website stack after code onboarding and adjust the data store approach if needed.
- State software effort separately from per-product verification effort.
- Provide the manual capture rate as a contingency.

## 20. Appendices

### Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | Catalogue Data Extraction & Preparation | Technical | F01-001 … F01-005 (5) |
| 02 | Product Data Store on Existing Website | Technical | F02-001 … F02-002 (2) |
| 03 | Catalogue Pages on Existing Website | Business | F03-001 … F03-006 (6) |
| 04 | Website Integration, SEO & Go-live | Shared | F04-001 … F04-004 (4) |

### Appendix B — Comparison with Option A

| Aspect | Option A — Full Catalogue Platform (GMC) | Option B — Product Migration (GPM) |
|--------|------------------------------------------|------------------------------------|
| Admin portal and roles | Yes | No |
| Garrison self-service product maintenance | Yes | No (developer re-runs loader) |
| Dynamic attributes and templates | Yes | No (fixed fields) |
| Review and publishing workflow | Yes | No (one-time Garrison review workbook) |
| Provenance and rights gate | Yes | No (rights confirmed once, before go-live) |
| Search and filters | Advanced, configurable | Basic, fixed filters |
| Website | Integrated new catalogue application | Pages added to existing website code |

### Appendix C — Risks

| Risk | Mitigation |
|------|-----------|
| Brenlo does not permit reproduction | Confirm before build; use Garrison's own data and images instead |
| Source site blocks automated extraction | Throttled extraction; supplier data file; manual capture rate as contingency |
| Existing website code is unavailable or unmaintainable | Code onboarding first; re-estimate or move to Option A |
| Actual product count higher than planned | Per-product rate for additional products |
| Source data changes after extraction | Freeze date for dataset; refresh via loader |
