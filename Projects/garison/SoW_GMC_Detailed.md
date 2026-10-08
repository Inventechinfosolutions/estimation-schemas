# SoW GMC — Detailed Statement of Work

## Garrison Online Moulding Catalogue Platform

**Client:** Garrison Industries  
**Project code:** GMC  
**Document type:** Detailed Statement of Work (RFP / estimation ready)  
**Version:** 1.0  
**Basis:** Garrison Online Moulding Catalogue — Technical Proposal v1.0

---

## 1. Introduction

Garrison Industries manufactures and supplies architectural wood mouldings. Its current website presents mouldings through a single page that does not let visitors browse, search or compare profiles in a structured way. The existing printed catalogue (approximately 38 pages) holds the technical detail: profile drawings, codes, dimensions, installation photographs and combinations. That detail is not available online in a searchable form.

This Statement of Work defines a **reusable Online Moulding Catalogue Platform** and the software support for an **initial populated catalogue**. Garrison will maintain the platform itself after go-live. The platform must let authorised Garrison users add, review, publish and maintain moulding profiles through administration only, with no software development change per product, category or attribute.

## 2. Project Overview

| Item | Description |
|------|-------------|
| Business problem | Moulding information is locked in a static page and a print catalogue; customers cannot find profiles by category, style, code or dimension |
| Target users | Public visitors (homeowners, contractors, architects, designers, dealers); Garrison catalogue staff |
| Delivery model | Public responsive web catalogue + secure administration portal + structured catalogue data layer |
| Primary outcome | Structured, searchable, SEO-ready catalogue integrated into the Garrison website and maintainable by Garrison |
| Secondary outcome | Initial catalogue populated from the Garrison catalogue and approved external reference sources, with provenance and content-rights control |
| Benchmark | Leading industry moulding catalogues (for example Brenlo) for structure and usability only |

The project has two related workstreams:

1. **Platform development** builds the catalogue framework, administration portal, public catalogue, search and filters, enquiry, SEO and website integration.
2. **Initial catalogue population** extracts, normalises and loads an agreed number of moulding profiles. Population labour is priced by product count. This SOW covers the software tooling that supports population (import, staging, bulk media). Data-entry labour is a separate commercial line.

## 3. Project Objectives

1. Replace the existing mouldings page with a modern online catalogue integrated into the Garrison website.
2. Represent every moulding as a structured product record whose technical detail is comparable to leading industry catalogues.
3. Support both **discovery browsing** ("I need a crown moulding") and **specification searching** ("about 3/4 inch thick and 5 inches wide").
4. Let Garrison add new categories, attributes and products **without database redesign or code changes**.
5. Provide tooling to load the initial catalogue drawn from the Garrison range and approved external profiles.
6. Track source, provenance and content-rights status for every externally referenced product, and block publication of unlicensed third-party media.
7. Deliver SEO-friendly product, category and combination pages.
8. Enforce a controlled Draft → In Review → Approved → Published workflow with history.

## 4. In Scope / Out of Scope

### In Scope

- Public responsive catalogue: home, category, style and collection listings; product detail and combination detail pages
- Global search by code, name, category, style, material, dimension and keyword; configurable faceted filters
- Configurable taxonomy covering categories, sub-categories, styles, collections, materials/species and finishes
- Dynamic attribute and dimension framework driven by category attribute templates, with units and fractional-inch handling
- Product profile management: core data, dimensions, materials, finishes, lengths, applications, media, drawings, technical documents, duplicate, archive and preview
- Typed product relationships and combinations built from linked component profiles
- Data completeness rules, duplicate validation, review and publishing workflow, approval history and workflow emails
- External source register, per-product provenance, and a content-rights publication gate
- Product enquiry form with spam protection, email routing to Garrison, and a basic enquiry register
- SEO foundation (URLs, metadata, canonical tags, redirects, XML sitemap, structured data, social metadata), website integration and usage analytics
- Bulk import templates, bulk media upload, import staging and commit for initial population
- Administrator access with configurable roles, and an administrative audit log
- Platform security hardening, media optimisation and delivery, backup, monitoring, environments and deployment

### Out of Scope (this phase)

- E-commerce, online ordering, payment, pricing and inventory availability
- Customer accounts, favourites, project boards and quote requests
- Full enquiry lifecycle management (assignment, follow-up, CRM pipeline). Only capture, routing and a basic register are included
- CRM or ERP integration
- CAD file download centre and product comparison
- AI-assisted discovery or visual profile matching
- Multilingual content (English only)
- Labour for initial data extraction and entry beyond the software tooling (priced per product count, commercial lines B and C)
- Obtaining third-party content rights (Garrison responsibility)
- Hosting infrastructure, CDN, email service and analytics subscriptions (Garrison-provided or billed at cost)

## 5. Solution Expectations (Business-level Only)

- **Content-driven:** adding product 001, product 500 or product 2,000 uses the same administration flow with no developer effort.
- **Configurable structure:** categories, attributes, templates, filters and masters are maintained through administration.
- **Structured technical data:** dimensions are stored as typed numeric values with units, so specification search and range filters work reliably.
- **Governed publishing:** nothing reaches the public catalogue without passing completeness rules and the review workflow.
- **Rights-aware:** external content is published only when Garrison has confirmed the rights.
- **Brand-consistent:** the catalogue matches Garrison's website identity and navigation.
- **Technology-neutral:** the final technology stack is agreed after discovery of Garrison's website and hosting environment.

## 6. Consolidated Functional Modules

### 01. Administrator Access & Role Management

**Purpose:** Secure the administration portal so that only authorised Garrison staff can maintain catalogue content, with configurable role permissions and a full audit trail.

**Functional requirements:**
- Authenticate administrators with a strong password policy, account lockout, session timeout and self-service password reset.
- Maintain administrator users, including invite, activate, deactivate and role assignment.
- Provide four default roles (Super Administrator, Catalogue Administrator, Catalogue Reviewer, Content Administrator) with configurable permissions.
- Record every administrative create, update, delete, workflow and publish action with user, timestamp, before and after values.

**Acceptance criteria:**
- Only active, authenticated administrators can reach the portal; public visitors never need to log in.
- Each role sees and performs only the actions granted in the permission matrix.
- An auditor can trace any published product change to the user who made it.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Administrator Authentication & Session Security | Login, logout, password policy, lockout, reset and session timeout for portal users |
| F01-002 | Administrator User Management | Super Administrator invites, maintains, deactivates and assigns roles to portal users |
| F01-003 | Role & Permission Configuration | Configure the permission matrix for default and additional roles |
| F01-004 | Administrative Audit Log | Searchable, exportable log of all administrative and workflow actions with change detail |

---

### 02. Catalogue Taxonomy & Master Data

**Purpose:** Maintain the independent classification layers (category, sub-category, style, collection, material/species and finish) that drive navigation, filtering and product classification.

**Functional requirements:**
- Configure the category hierarchy, including sub-categories, display order, images, introductory SEO text and active/retired status. Seed it with the initial Garrison categories.
- Maintain styles and collections as a separate classification layer from category and material.
- Maintain material/species and finish masters, including swatch images and display order.
- Prevent deletion of in-use values; support retire/merge instead.

**Acceptance criteria:**
- Garrison can add, rename, reorder or retire a category without developer involvement.
- Category, style, collection, material and finish are filterable independently.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Category & Sub-category Management | Hierarchical categories with ordering, imagery, SEO intro and status |
| F02-002 | Style & Collection Management | Independent style and collection classification masters |
| F02-003 | Material, Species & Finish Masters | Material/species and finish masters with swatches and usage protection |

---

### 03. Dynamic Attribute & Dimension Framework

**Purpose:** Let each category define which technical dimensions and attributes apply, so the product form, detail page and filters adapt per category without code change.

**Functional requirements:**
- Maintain an attribute library covering data type (number, text, list, multi-select, yes/no), unit of measure, permitted values, display format and attribute group.
- Define category attribute templates that set applicable attributes, mandatory/conditional flags, display order, filterable and searchable flags.
- Assess and manage the impact on existing products when a template changes.
- Normalise dimension input in fractional inches, decimal inches and millimetres; store canonical numeric values; display in Garrison's preferred format.

**Acceptance criteria:**
- A new category with its own dimension set can be configured and used to create products with no code change.
- Dimension values entered as `3/4"`, `0.75 in` or `19.05 mm` are stored consistently and filter correctly.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Attribute Library & Units of Measure | Central attribute definitions with type, unit, permitted values and group |
| F03-002 | Category Attribute Templates | Per-category attribute set with mandatory, conditional, order, filter and search flags |
| F03-003 | Template Change Impact Management | Impact analysis and controlled re-validation of products when templates change |
| F03-004 | Dimension Normalisation & Display Formatting | Fraction/decimal/metric parsing, canonical storage and display formatting rules |

---

### 04. Product Profile Management

**Purpose:** Maintain each moulding as a structured product profile covering core data, category-driven dimensions, materials, finishes, lengths, applications, media, drawings and documents.

**Functional requirements:**
- Provide a product register with filters, plus create and edit of core profile data (code, name, category, sub-category, style, collection, descriptions, featured flag).
- Render a dynamic dimension and attribute form from the selected category template.
- Capture materials/species, finish options, available lengths (standard and random), minimum quantity, special-order indicator and applications.
- Manage typed media (primary image, profile drawing, dimension drawing, installed image, gallery), alt text and ordering.
- Manage technical PDFs and supporting documents with versions.
- Duplicate a product as a template; archive and restore with impact warnings.
- Preview the public product page before submission or publication.

**Acceptance criteria:**
- An administrator can create a product, classify it, add dimensions, upload drawings and preview it in one guided flow.
- Product codes are unique and the form shows only fields applicable to the category.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Product Register & Core Profile | Product list, filters and core profile create/edit |
| F04-002 | Category-driven Dimension & Attribute Entry | Dynamic form rendered from the category attribute template |
| F04-003 | Materials, Finishes, Lengths & Applications | Material, finish, length, minimum quantity, special order and application details |
| F04-004 | Product Media & Drawing Management | Typed image and drawing upload, ordering, primary selection and alt text |
| F04-005 | Technical Document Management | Technical PDF and supporting document upload with versioning |
| F04-006 | Product Duplicate, Archive & Restore | Duplicate-as-template, archive and restore with relationship impact checks |
| F04-007 | Product Preview | Draft preview of the public product page in desktop and mobile views |

---

### 05. Combinations & Product Relationships

**Purpose:** Model coordinated trim through typed relationships between profiles, and through combinations managed as a separate catalogue entity assembled from component profiles.

**Functional requirements:**
- Define typed relationships between products (related, matching casing, matching crown, alternative, similar), with optional reciprocal creation.
- Maintain combination records with code, name, description, overall dimensions, assembly image and drawing, and status.
- Assemble combinations from component profiles with role/position and order; component pages link back to their combinations.

**Acceptance criteria:**
- A combination page lists each component with a link to its product page.
- A product page shows its related profiles and the combinations in which it is used.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Typed Product Relationships | Related, matching, alternative and similar relationships with reciprocity rules |
| F05-002 | Combination Record Management | Combination entity with code, media, dimensions and lifecycle |
| F05-003 | Combination Component Assembly | Link component profiles with role, position and order to a combination |

---

### 06. Content Governance & Publishing Workflow

**Purpose:** Ensure that only complete, reviewed and approved content reaches the public catalogue, with an auditable approval history.

**Functional requirements:**
- Enforce mandatory and template-driven conditional completeness rules; calculate a completeness score; detect probable duplicate profiles.
- Submit products and combinations for review; provide a reviewer queue.
- Let reviewers approve or request changes with comments; record approval history.
- Publish, unpublish and bulk publish approved content; archive retired content.
- Send email notifications on submission, change request, approval and publication.

**Acceptance criteria:**
- Products failing completeness rules cannot be submitted for review.
- The state flow Draft → In Review → Approved → Published (Changes Requested → Draft; Archived) is enforced for every product and combination.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Data Completeness & Duplicate Validation | Mandatory/conditional completeness rules, completeness score and duplicate detection |
| F06-002 | Submit for Review & Review Queue | Submission of products/combinations and reviewer work queue |
| F06-003 | Review Decision & Approval History | Approve or request changes with comments and full decision history |
| F06-004 | Publish, Unpublish & Bulk Publishing | Controlled publishing, unpublishing and bulk publish of approved content |
| F06-005 | Workflow Email Notifications | Email alerts for submission, changes requested, approval and publication |

---

### 07. External Source, Provenance & Content Rights

**Purpose:** Record where externally referenced profiles came from and what Garrison is permitted to reproduce, and prevent publication of third-party content without confirmed rights.

**Functional requirements:**
- Maintain an external source register (for example Brenlo) with URL, catalogue/series, contact and default rights position.
- Capture per-product provenance fields: source, URL, source catalogue, original code, source category, data usage status, content rights status, date verified and Garrison product status.
- Block publication with third-party media or text when rights are "To be confirmed" or usage is "Restricted"; provide a rights status dashboard and re-verification reminders.

**Acceptance criteria:**
- Every external product shows complete provenance before it can be submitted.
- An external product with unconfirmed rights cannot be published with third-party media.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | External Source Register | Master of approved external reference sources |
| F07-002 | Product Provenance Capture | Per-product provenance and rights fields linked to the source register |
| F07-003 | Content Rights Publication Gate & Rights Dashboard | Rights-based publish blocking, media flagging and rights status dashboard |

---

### 08. Public Catalogue Experience

**Purpose:** Provide visitors with a brand-consistent, responsive catalogue for discovery and technical evaluation of moulding profiles.

**Functional requirements:**
- Catalogue home with category entry points, featured products, collections and search.
- Category, sub-category, style and collection listing pages with product cards, sort, pagination and breadcrumbs.
- Product detail page showing profile drawing (zoom), dimensions table, materials, finishes, lengths, applications, documents, related profiles, combinations and a Request Information action.
- Combination detail page with assembly drawing, component list and links.
- Responsive design system aligned to Garrison branding, built with reference to WCAG 2.1 AA.

**Acceptance criteria:**
- A visitor can browse from catalogue home to a product detail page and download its technical PDF on desktop, tablet and mobile.
- Only Published content appears publicly.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | Catalogue Home Page | Landing page with category tiles, featured products, collections and search entry |
| F08-002 | Category, Style & Collection Listing Pages | Product grids by category, style and collection with sort and pagination |
| F08-003 | Product Detail Page | Full technical and inspirational product page with drawing viewer and enquiry action |
| F08-004 | Combination Detail Page | Combination assembly page with linked component profiles |
| F08-005 | Responsive Catalogue Design System & Accessibility | Brand-aligned responsive component library and accessibility baseline |

---

### 09. Search & Filtering

**Purpose:** Enable fast keyword, code and specification-oriented search with configurable faceted filters across a catalogue growing to 10,000+ products.

**Functional requirements:**
- Maintain a search index of published products and combinations, updated on publish, unpublish and master changes.
- Search by code, name, category, style, material, dimension and keyword, including dimension phrases (for example "5 inch crown") and synonyms.
- Faceted filters driven by template configuration (list facets with counts, numeric range facets for dimensions).
- Search suggestions, results page, sort, no-results guidance and search term capture.

**Acceptance criteria:**
- Searching `2051` returns the product with that code first; "5 inch crown" returns crown profiles about 5 inches in the relevant dimension.
- Marking an attribute as filterable in its template makes it a filter without development.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F09-001 | Search Index & Publication Synchronisation | Index build, incremental updates and full re-index of published content |
| F09-002 | Global Keyword, Code & Dimension Search | Ranked search with code priority, dimension parsing and synonyms |
| F09-003 | Configurable Faceted Filters | Template-driven list and range facets with counts and facet configuration |
| F09-004 | Search Suggestions & Results Experience | Type-ahead suggestions, results page, sort and no-results handling |

---

### 10. Product Enquiry

**Purpose:** Let visitors request information about a product or combination and route each enquiry reliably to Garrison.

**Functional requirements:**
- Show an enquiry form on product and combination pages and as a general catalogue enquiry, with product context captured automatically and spam protection.
- Route enquiries by email to configured Garrison recipients (by category where configured); send an acknowledgement to the visitor.
- Provide a basic enquiry register with status (New / Handled), search and export.

**Acceptance criteria:**
- A submitted enquiry reaches the configured Garrison mailbox with product code and link, and appears in the enquiry register.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F10-001 | Product Enquiry Form | Contextual enquiry form with consent and spam protection |
| F10-002 | Enquiry Routing & Acknowledgement | Recipient rules, Garrison notification and visitor acknowledgement emails |
| F10-003 | Enquiry Register | Admin list of enquiries with status, search and export |

---

### 11. SEO, Analytics & Website Integration

**Purpose:** Make every catalogue page discoverable by search engines, integrate the catalogue into the existing Garrison website, and measure catalogue usage.

**Functional requirements:**
- Generate SEO-friendly URLs (for example `/mouldings/crown/CM-001`); support editable titles and meta descriptions, canonical URLs and automatic redirects when slugs change.
- Generate an XML sitemap, product structured data and social sharing metadata.
- Integrate with the Garrison website: navigation, header/footer, branding, replacement of the existing mouldings page with redirects. Use the integration method (sub-path, sub-domain or embedded) confirmed in discovery.
- Track catalogue usage events (search terms, filter use, product views, document downloads, enquiries) in the website analytics tool.

**Acceptance criteria:**
- Every published product, category and combination has a unique URL, title, meta description and sitemap entry.
- The catalogue is reachable from the Garrison website navigation, and the old mouldings page redirects to it.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F11-001 | SEO URLs, Metadata & Redirects | Slug rules, editable metadata, canonical URLs and redirect management |
| F11-002 | Sitemap, Structured Data & Social Metadata | XML sitemap, product structured data and social sharing tags |
| F11-003 | Garrison Website Integration | Navigation, header/footer, branding alignment and legacy page redirects |
| F11-004 | Catalogue Usage Analytics | Analytics event tagging and usage insight for catalogue interactions |

---

### 12. Catalogue Data Import & Bulk Operations

**Purpose:** Provide tooling to load the initial catalogue efficiently and accurately, and to support bulk maintenance afterwards.

**Functional requirements:**
- Generate category-specific import templates; import product records in bulk with row-level validation.
- Upload media in bulk and match files to products by naming convention.
- Stage imported records for review and correction before committing them as Draft products.
- Optionally export the catalogue and apply bulk attribute updates.

**Acceptance criteria:**
- A prepared template for a category imports into staging with a clear error report; corrected records commit as Draft products with media attached.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F12-001 | Import Templates & Bulk Product Import | Category template download and validated bulk upload into staging |
| F12-002 | Bulk Media Upload & Auto-matching | Archive upload of images/drawings matched to product codes |
| F12-003 | Import Staging Review & Commit | Review, correct and commit staged records as Draft products |
| F12-004 | Catalogue Export & Bulk Update | Export catalogue data and apply validated bulk attribute updates (optional) |

---

### 13. Platform Security, Performance & Operations

**Purpose:** Deliver a secure, fast and supportable production platform.

**Functional requirements:**
- Process uploaded media into optimised derivatives (thumbnails, responsive sizes, modern formats) and deliver them through caching/CDN.
- Apply OWASP Top 10 protections, upload validation and malware scanning, rate limiting, security headers and HTTPS.
- Configure backups with a tested restore procedure, uptime and error monitoring, and centralised logging.
- Provide development, staging and production environments with a controlled deployment pipeline and deployment documentation.

**Acceptance criteria:**
- Listing and product pages meet the agreed performance targets with representative data volume.
- A backup restore is demonstrated on staging before go-live.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F13-001 | Media Processing & Content Delivery | Image/drawing derivatives, modern formats, caching and CDN delivery |
| F13-002 | Security Hardening & Upload Protection | OWASP controls, upload scanning, rate limiting and security headers |
| F13-003 | Backup, Monitoring & Error Logging | Backup/restore, uptime and error monitoring, centralised logs |
| F13-004 | Environments & Deployment Pipeline | Dev/staging/production environments and controlled release pipeline |

---

## 7. End-to-End Workflows

### 7.1 Visitor discovery to enquiry

Garrison website → Mouldings → Catalogue home → browse category/style **or** search/filter → listing → product detail (drawing, dimensions, materials, finishes, lengths, documents) → related profiles / combinations → Request Information → enquiry routed to Garrison → acknowledgement to visitor.

### 7.2 Adding a new moulding

Catalogue Administrator selects category → template loads applicable fields → enters core data and dimensions → uploads drawings and images → selects materials and finishes → adds relationships and combinations → records provenance (external only) → previews → completeness check → submits for review → Reviewer approves or requests changes → Administrator publishes → search index, sitemap and listings update.

### 7.3 Initial catalogue population

Source catalogue → profile identification → data extraction into category import templates → bulk import into staging → validation and correction → bulk media upload and matching → commit as Draft → completeness check → Garrison review → bulk publish.

### 7.4 External content governance

External profile identified → source registered → provenance recorded → Garrison decides inclusion → rights confirmed? Yes: publish with source content. No: publish with Garrison-owned content or attributes only, or keep as reference only (not published).

## 8. Access Control / RBAC

Access model: **User → Role → Permissions** (configurable). Public visitors are anonymous; no customer login is in scope.

| Capability | Super Administrator | Catalogue Administrator | Catalogue Reviewer | Content Administrator |
|------------|:---:|:---:|:---:|:---:|
| Create / edit products and combinations | ✓ | ✓ | — | Content fields only |
| Manage categories, masters, attributes and templates | ✓ | ✓ | — | — |
| Manage images, documents and SEO content | ✓ | ✓ | — | ✓ |
| Review / approve / request changes | ✓ | — | ✓ | — |
| Publish / unpublish / archive | ✓ | ✓ | — | — |
| Manage sources and rights status | ✓ | ✓ | View | — |
| Import and bulk operations | ✓ | ✓ | — | — |
| Manage enquiry register | ✓ | ✓ | — | View |
| Manage users and roles | ✓ | — | — | — |
| View audit log | ✓ | View | View | — |

Maker-checker rule: a user cannot approve content they last edited, unless the Super Administrator enables a single-person approval override.

## 9. Channels

| Channel | Users | Notes |
|---------|-------|-------|
| Public responsive web catalogue | Visitors | Desktop, tablet, mobile; current Chrome, Edge, Safari, Firefox |
| Administration portal (web) | Garrison staff | Desktop-first, tablet-usable |
| Email | Garrison recipients, visitors, administrators | Enquiry routing, acknowledgements, workflow notifications |

No native mobile application is in scope.

## 10. Integrations

| Integration | Purpose | Notes |
|-------------|---------|-------|
| Garrison website | Navigation, header/footer, redirects | Method confirmed in discovery (sub-path, sub-domain or embedded) |
| Transactional email service / SMTP | Enquiry and workflow emails | Garrison-provided account |
| Web analytics (for example Google Analytics 4) | Usage tracking | Garrison-owned property |
| Spam protection service (for example reCAPTCHA) | Enquiry form protection | Garrison-registered keys |
| CDN / object storage | Media delivery | Aligned with Garrison hosting |
| Search engines | Sitemap submission | Through Garrison webmaster accounts |

No CRM, ERP, payment or inventory integration is in scope.

## 11. Audit, Compliance & Security

- HTTPS for all traffic; strong admin password policy; lockout and session timeout.
- Role-based access control for all administration functions, enforced server-side.
- Audit log of administrative changes, workflow decisions and publication events, with before/after values.
- Input validation and OWASP Top 10 protection; upload type, size, content and malware checks.
- Spam protection and rate limiting on the enquiry form; minimal personal data captured, with a consent statement.
- Content-rights gate on external content; provenance retained for every external product.
- Regular backups with a documented, tested restore procedure.

## 12. Non-Functional Requirements

| Area | Requirement |
|------|-------------|
| Performance | Listing and product pages render quickly on broadband and 4G; search responses are near-instant at the target volume; images lazy-loaded and optimised |
| Scalability | Growth from about 100 to 10,000+ products without redesign of the product model |
| Availability | Production deployment suited to Garrison hosting; backups; uptime and error monitoring |
| Usability | Responsive across desktop, tablet and mobile; consistent with Garrison branding |
| Accessibility | Built with reference to WCAG 2.1 AA (alt text, contrast, keyboard navigation, focus states) |
| Maintainability | Content-driven; no developer effort to add products, categories, attributes or filters |
| Browser support | Current versions of Chrome, Edge, Safari and Firefox |
| SEO | Server-rendered or pre-rendered public pages readable by search engines |

## 13. Data Migration and Initial Population

There is no legacy database migration; the current mouldings page holds no structured data. Initial content is loaded through the import tooling (Module 12):

- Phase 1: convert the existing Garrison catalogue into structured records.
- Phase 2: identify additional profiles from approved sources (subject to Module 07).
- Phase 3: normalise codes, categories, dimensions, units, materials, styles and terminology.
- Phase 4: Garrison reviews and approves the dataset in the platform's review workflow.
- Phase 5: bulk publish approved records.

The number of products in the initial population is agreed during discovery and priced separately.

## 14. Phased Delivery

### Phase 1 — Go-live (this SOW)

All modules 01–13. F12-004 (Catalogue Export & Bulk Update) is optional and recommended.

### Phase 2 — Future considerations (not estimated herein)

Full enquiry management and quote requests; customer accounts, favourites and project boards; CAD downloads and download centre; product comparison; CRM/ERP integration; e-commerce and inventory; AI-assisted discovery and visual profile matching.

## 15. Deliverables

- Responsive public catalogue integrated with the Garrison website
- Administration portal with workflow, provenance and import tooling
- Catalogue data model and dynamic attribute framework, configured with initial categories, attributes and templates
- Search index and configurable filters
- SEO foundation, analytics tagging and website integration
- Development, staging and production environments with deployment pipeline
- Technical architecture document, catalogue data model document, administrator guide, deployment and maintenance documentation
- UAT scenarios and test reports

## 16. Acceptance Criteria (Program Level)

| Perspective | Criterion |
|-------------|-----------|
| Customer | A visitor can browse, search, filter, view a product and its technical details, explore related profiles and combinations, and submit an enquiry |
| Administrator | An authorised user can create a product, classify it, add dimensions, upload drawings, preview, submit, approve and publish it |
| Business | Garrison can add a new category with its own dimensions, and new products, without developer involvement |
| Data | The agreed initial product set is imported, meets completeness rules and is published |
| Technical | NFRs are met in performance, security and browser tests; backup restore is demonstrated |

## 17. Expected Benefits

- Customers find the right profile faster through category, style, code or dimension.
- Garrison controls its catalogue content and growth without dependence on developers.
- Technical drawings and specifications become discoverable through search engines.
- Enquiries arrive with product context, reducing back-and-forth.
- External content is used within confirmed rights, reducing legal exposure.

## 18. Assumptions & Dependencies

1. The platform is a digital product catalogue, not a transactional e-commerce system.
2. Access model is User → Role → Permissions with four default roles; no public login.
3. Garrison provides website and hosting access, brand assets and catalogue source files at the dates required by the plan.
4. Garrison approves taxonomy, external inclusions and the initial dataset, and confirms third-party content rights.
5. Initial product count is confirmed at discovery; population labour is priced separately per product.
6. Content is English only; dimensions primarily in inches, with millimetre display optional.
7. Garrison provides the email service, analytics property, spam protection keys and hosting/CDN accounts.
8. Technology stack is confirmed after discovery; estimates assume a standard web stack with a dedicated search capability.
9. Garrison nominates a single point of contact and turns reviews around within agreed timelines.

## 19. Vendor Response Expectations

- Confirm the technology stack and hosting approach after discovery of the current website.
- Provide the effort split between platform development (fixed) and population tooling.
- State the per-product population rate assumption separately from platform effort.
- Identify any dependency on Garrison-provided services and accounts.
- Provide the testing approach covering functional, data validation, responsive, performance, security and SEO tests.

## 20. Appendices

### Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | Administrator Access & Role Management | Shared | F01-001 … F01-004 (4) |
| 02 | Catalogue Taxonomy & Master Data | Business | F02-001 … F02-003 (3) |
| 03 | Dynamic Attribute & Dimension Framework | Business | F03-001 … F03-004 (4) |
| 04 | Product Profile Management | Business | F04-001 … F04-007 (7) |
| 05 | Combinations & Product Relationships | Business | F05-001 … F05-003 (3) |
| 06 | Content Governance & Publishing Workflow | Business | F06-001 … F06-005 (5) |
| 07 | External Source, Provenance & Content Rights | Business | F07-001 … F07-003 (3) |
| 08 | Public Catalogue Experience | Business | F08-001 … F08-005 (5) |
| 09 | Search & Filtering | Business | F09-001 … F09-004 (4) |
| 10 | Product Enquiry | Business | F10-001 … F10-003 (3) |
| 11 | SEO, Analytics & Website Integration | Shared | F11-001 … F11-004 (4) |
| 12 | Catalogue Data Import & Bulk Operations | Technical | F12-001 … F12-004 (4) |
| 13 | Platform Security, Performance & Operations | Technical | F13-001 … F13-004 (4) |

### Appendix B — Module consolidation map (proposal → consolidated)

| Proposal area | Consolidated module |
|---------------|---------------------|
| §20 User Roles, §22 Security (admin auth), FR-14, FR-20 | 01 Administrator Access & Role Management |
| §8 Categories, Styles & Collections, FR-02, FR-07, FR-08 | 02 Catalogue Taxonomy & Master Data |
| §7 Dynamic Attribute & Dimension Framework, FR-04, FR-05 | 03 Dynamic Attribute & Dimension Framework |
| §6 Product Information Framework, §12.1–12.2, FR-03, FR-06 | 04 Product Profile Management |
| §11 Combinations & Relationships, FR-09, FR-10 | 05 Combinations & Product Relationships |
| §12.3–12.4 Publishing & Data Quality, FR-15, FR-21 | 06 Content Governance & Publishing Workflow |
| §14 External Sources & Content Rights, FR-16 | 07 External Source, Provenance & Content Rights |
| §5 Catalogue Experience, §10 Product Detail, §15 UX, FR-01, FR-13 | 08 Public Catalogue Experience |
| §9 Search & Filtering, FR-11, FR-12 | 09 Search & Filtering |
| FR-17 Enquiry | 10 Product Enquiry |
| §21 SEO & Website Integration, FR-18, FR-19 | 11 SEO, Analytics & Website Integration |
| §13 Initial Catalogue Population, FR-22 | 12 Catalogue Data Import & Bulk Operations |
| §16 Architecture, §19 NFR, §22 Security, §26 Deployment | 13 Platform Security, Performance & Operations |

Notification and document handling are embedded: workflow emails in F06-005, enquiry emails in F10-002, technical documents in F04-005. No separate notification or document management module is required.

### Appendix C — Key business entities (logical)

Category, SubCategory, Style, Collection, Material, Finish, Attribute, AttributeTemplate, Product, ProductAttributeValue, Media, Document, ProductRelationship, Combination, CombinationComponent, Source, ProductProvenance, WorkflowHistory, Enquiry, ImportBatch, User, Role, Permission, AuditLog.

### Appendix D — Risks and considerations

| Risk | Mitigation |
|------|-----------|
| External profile volume larger than expected | Product count fixed at discovery; per-product rate beyond agreed quantity |
| Third-party content rights not granted | Rights gate (F07-003); Garrison-owned alternatives |
| Inconsistent source dimensions and units | Normalisation rules (F03-004); staging validation (F12-003) |
| Late taxonomy changes | Configurable taxonomy and templates; impact management (F03-003) |
| Duplicate profiles across sources | Duplicate validation (F06-001) |
| Large drawings slow pages | Media processing and CDN (F13-001) |
| Website integration method unknown | Confirmed at discovery; F11-003 sized for sub-path/sub-domain integration |
