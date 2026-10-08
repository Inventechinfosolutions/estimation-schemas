# SoW GWM — Detailed Statement of Work

## Garrison Website Design & Product Catalogue Migration (Option 1)

**Client:** Garrison Industries  
**Project code:** GWM  
**Document type:** Detailed Statement of Work (estimation ready)  
**Version:** 1.0  
**Relationship to other proposals:** One of three options. Option 1 — website design and product migration (GWM). Option 2 — Option 1 plus AI product images (GWA). Option 3 — Premium online catalogue platform with admin portal (GMC).

---

## 1. Introduction

Garrison Industries wants a redesigned website at www.garrisonindustries.ky that includes the moulding products shown in the Brenlo online catalogue (https://brenlo.com/catalogue/). Garrison has advised that its products rarely change, so catalogue set-up (categories, styles, products and reference data) is a **one-time activity** and **no administration portal is required**.

Because the current website's source code and admin logins are not available, the website is **rebuilt** from its public content in a new design. Products are extracted from the source catalogue, reviewed and approved by Garrison in a workbook, and published as catalogue pages. Later changes are made by a developer.

## 2. Project Overview

| Item | Description |
|------|-------------|
| Source | Brenlo public online catalogue: Moulding section (by category and style) |
| Target | New Garrison website on garrisonindustries.ky (rebuilt; current source code not required) |
| Business problem | Current website does not show individual moulding profiles and needs a modern design |
| Outcome | Redesigned website with a browsable, searchable moulding catalogue and enquiry form |
| Maintenance model | Developer-maintained content files and product dataset (no admin portal) |
| Product images | Source catalogue images, optimised (permission required) |

### 2.1 Source catalogue observations

| Observation | Implication |
|-------------|-------------|
| 37 moulding types, styles Classic / Modern / Transitional / Inspire, and Combinations | Taxonomy mirrored or renamed by Garrison |
| 201 products confirmed in 21 categories; 16 multi-word categories could not be counted remotely | Planning quantity **350 products** |
| Each product: category, code, thickness × width (fractions), style, species options, one isometric image (about 541×402 px) | Compact data; low per-product effort |
| No drawings, PDFs or descriptions | Product pages show facts and image only unless Garrison supplies text |

### 2.2 Current website observations

| Observation | Implication |
|-------------|-------------|
| Self-hosted on a cloud virtual server; SSL certificate did not validate during review | New hosting with valid SSL |
| Automated requests were refused by the server | Content captured page by page in a browser where needed |
| Company email on Google Workspace | DNS cutover must keep MX and email authentication records |
| No source code or admin logins available | Website rebuilt from public content; only domain/DNS access needed |

## 3. Project Objectives

1. Deliver a modern, responsive Garrison website in an approved new design.
2. Migrate the useful content of the current website, with redirects from current URLs.
3. Publish the agreed moulding products with category, style, dimensions, species and image.
4. Let visitors browse, filter, search and send product enquiries to Garrison's mailbox.
5. Set up the catalogue once, without an admin portal, with a documented refresh procedure.

## 4. In Scope / Out of Scope

### In Scope

- Discovery & Website Design: Content capture, sitemap, wireframes, style guide, component library, page designs, prototype
- Website Build: Layout, navigation, components, home, about, services, gallery, content pages, enquiry form, migrated content
- Product Catalogue Pages: Public catalogue pages generated from the one-time dataset
- One-time Product Data Migration: Brenlo moulding products; one-time set-up of categories, styles and products; refresh procedure
- Hosting, SEO & Launch: Hosting set-up, DNS cutover preserving email, SEO, analytics, testing, launch, handover

### Out of Scope

- Administration portal, user roles, publishing workflow and configurable product framework (available in Option 3)
- New logo or brand identity, copywriting, photography
- New product descriptions, technical drawings or PDFs
- E-commerce, pricing, quotes, customer accounts
- Hosting, domain and third-party service fees
- Obtaining permission from Brenlo and legal advice (Garrison responsibility)
- Combinations pages and Interior Doors / In-Stock products unless the optional features are taken

## 5. Solution Expectations (Business-level Only)

- Fast, secure, statically generated website with no admin login surface.
- Content and product data held in version-controlled files; one prepared dataset drives all catalogue pages.
- Garrison approves the product list once through a review workbook instead of an admin portal.
- Later changes: developer edits the dataset or content, rebuilds on staging, verifies and releases.

## 6. Consolidated Functional Modules

### 01. Discovery & Website Design

**Purpose:** Understand what the current website contains and design the new website before it is built.

**Functional requirements:**
- Capture all useful content and URLs from the current public website.
- Agree a sitemap and page wireframes.
- Produce an approved visual design for every page template on desktop and mobile.

**Acceptance criteria:**
- Garrison approves the page list, wireframes and visual designs in writing.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Existing Website Discovery & Content Capture | Review of the current Garrison website from its public pages, because neither source code nor admin logins are available |
| F01-002 | Information Architecture & Wireframes | New sitemap and navigation model covering the company pages and the product catalogue |
| F01-003 | Visual Design System & Page Designs | Brand-aligned visual design for the new website: style guide (colour, typography, spacing, iconography, imagery treatment), a UI component library … |

---

### 02. Website Build

**Purpose:** Build the new Garrison website from the approved designs.

**Functional requirements:**
- Responsive site with header, navigation, footer and reusable components.
- Home page, company and service pages populated with migrated content.
- Enquiry form delivering to Garrison's existing mailbox with spam protection.

**Acceptance criteria:**
- All confirmed pages are live on staging, match the approved designs and pass testing.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Site Foundation, Layout & Navigation | Technical foundation of the new website: a modern statically generated site (for example Astro or Next.js static export) with content held in … |
| F02-002 | Home Page | New home page: hero banner, product range highlights linking into the catalogue, company introduction and value proposition, featured moulding … |
| F02-003 | Company & Service Content Pages | Templates for Garrison's company pages: About, Products & Services overview (covering lines beyond mouldings), Projects/Gallery with lightbox, … |
| F02-004 | Contact & Enquiry Form | Contact page with enquiry form (name, email, phone, company, subject, message, optional product reference), validation, spam protection, email … |
| F02-005 | Existing Content Migration | Move the content Garrison keeps from the current site into the new templates: clean up text, optimise and rename images, place content into content … |

---

### 03. Product Catalogue Pages

**Purpose:** Present the migrated products so visitors can browse, filter, search and enquire.

**Functional requirements:**
- Landing page with category tiles and style shortcuts.
- Category listing with style, thickness, width and species filters.
- Product page with image, code, dimensions, species, similar products and Request Information.
- Search by code, category, style and size.

**Acceptance criteria:**
- A visitor can go from the home page to a product and send an enquiry that names the product.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Mouldings Landing Page | Catalogue entry page: introduction, category tiles (image and product count), style shortcuts (Classic, Modern, Transitional, Inspire) and a … |
| F03-002 | Category Listing Page with Filters | Product grid per category showing image, code and thickness × width, with filters for style, thickness, width and species, sort (code, thickness, … |
| F03-003 | Product Detail Page | Product page with image and lightbox, code, category, style, thickness and width (fraction display), available species, similar products (same … |
| F03-004 | Catalogue Search | Search box with suggestions and a results page, matching product code (exact and prefix), category, style and dimension phrases (for example '5 1/2 … |
| F03-005 | Product Enquiry | Request Information action on product pages that opens the enquiry form (F02-004) with the product code, category, dimensions and page link … |
| F03-006 | Combinations Pages | Optional listing and detail pages for moulding combinations from the source catalogue, showing the combination image and component profiles linked to … (Optional) |

---

### 04. One-time Product Data Migration

**Purpose:** Set up the catalogue once from the source, with Garrison approving the product list, instead of building an admin portal.

**Functional requirements:**
- Extract moulding products from the source catalogue (or a supplier data file).
- Normalise dimensions, categories, styles and species.
- Garrison reviews and signs off the product list in a workbook.
- Generate the website's catalogue data from the signed-off dataset.

**Acceptance criteria:**
- Every approved product is published; the reconciliation report shows no unexplained gaps.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Source Catalogue Extraction Utility | Command-line utility that walks the source catalogue's moulding categories and styles, reads each listing and product view, and captures product … |
| F04-002 | Product Image Acquisition & Optimisation | Download every product image referenced in the raw dataset, verify it, rename it to a Garrison convention (category-code), and generate web … |
| F04-003 | Data Normalisation & Validation | Transform raw records into the master dataset: parse fractional dimensions (for example 5 1/2, 3 11/16) into numbers while keeping display text, map … |
| F04-004 | Garrison Review Workbook & Sign-off | Export the master dataset to an Excel review workbook (thumbnail link, code, category, style, dimensions, species, include/exclude and rename … |
| F04-005 | Catalogue Data Build & Publishing | Turn the frozen dataset into the website's catalogue data files (per category, per product and search index), link product images, generate page … |
| F04-006 | Interior Doors & In-Stock Product Extension | Optional extension applying the same extraction, preparation and page approach to the Interior Doors (Stock, Classic, Modern, Transitional, French) … (Optional) |

---

### 05. Hosting, SEO & Launch

**Purpose:** Launch the new website on Garrison's domain securely, discoverably and without email disruption.

**Functional requirements:**
- SEO-ready URLs, metadata, sitemap and 301 redirects from current URLs.
- Hosting, SSL and DNS cutover with email preserved.
- Analytics with consent; full testing; user acceptance testing and handover.

**Acceptance criteria:**
- Site live on garrisonindustries.ky with valid SSL, working email and no broken redirects.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | SEO Foundation & Redirects | SEO-friendly URLs (for example /mouldings/crown/507), template-driven titles and meta descriptions, XML sitemap and robots file, product and … |
| F05-002 | Hosting, Domain, SSL & DNS Cutover | Provision staging and production hosting for the new static site and form handler, set up automated build and deployment, install SSL with automatic … |
| F05-003 | Analytics & Cookie Consent | Web analytics with key events (product view, filter use, search, enquiry submitted) and a cookie consent banner that loads analytics only after … |
| F05-004 | Quality Assurance, Accessibility & Performance | Functional test cycle across all pages and catalogue features, cross-browser and device testing, accessibility checks against WCAG 2.1 AA basics, and … |
| F05-005 | UAT, Launch & Handover | Migration reconciliation report (approved products per category versus published pages, missing images, broken links), user acceptance testing … |

---

## 7. End-to-End Workflow

Discovery and content capture → wireframes and design approval → website build → product extraction → normalisation → image optimisation → Garrison review workbook sign-off → catalogue data build → testing → user acceptance testing → DNS cutover → handover.

Product refresh after go-live: developer updates the dataset → build on staging → verification → production release.

## 8. Access Control

No administration portal or user roles. All website pages are public. Content, dataset and deployment are used only by the delivery team and later maintenance developers.

## 9. Channels

Responsive website (desktop, tablet, mobile). No mobile app.

## 10. Integrations

| Integration | Purpose | Notes |
|-------------|---------|-------|
| Brenlo public catalogue | One-time source of product data and images | Throttled extraction, or a supplier data file |
| Transactional email service | Enquiry and acknowledgement emails | Authenticated alongside Google Workspace |
| Spam protection service | Enquiry form protection | For example Turnstile or reCAPTCHA |
| Web analytics | Visitor and enquiry insights | Loaded after cookie consent |
| Hosting and DNS | Website hosting, SSL, domain | Email records preserved |

## 11. Compliance, Security & Content Rights

- **Brenlo content (go/no-go):** Brenlo's product data, product codes and photographs are Brenlo's content. Garrison should hold written permission from Brenlo (for example as an authorised dealer or distributor) before publishing them. If Garrison is not a Brenlo dealer, it should not present Brenlo product codes as its own range.
- Extraction reads public pages only, with throttled requests and no circumvention of access controls.
- Enquiry form: spam protection, input validation, no enquiry data stored on the website.
- HTTPS with automatic certificate renewal; no admin login surface.

## 12. Non-Functional Requirements

| Area | Requirement |
|------|-------------|
| Performance | Key templates meet Core Web Vitals 'good'; images optimised and lazy-loaded |
| Compatibility | Current Chrome, Edge, Safari, Firefox; iOS and Android phones |
| Accessibility | WCAG 2.1 AA basics (contrast, alt text, keyboard navigation, headings) |
| SEO | Unique titles, sitemap, structured data, 301 redirects from current URLs |
| Maintainability | Documented content update and product refresh procedures |

## 13. Data Migration & Volume Basis

| Item | Quantity | Rate (hours) | Hours |
|------|---------:|-------------:|------:|
| Per-product data verification | 350 | 0.25 | 88 |
| Existing page content migration | 15 | 1.5 | 23 |

Products beyond 350 and pages beyond 15 are charged at the same rates.

## 14. Phased Delivery

1. Discovery and design: content capture, wireframes, visual design approval.
2. Build: website foundation, pages, content migration and catalogue templates.
3. Product migration: extraction, normalisation, images, Garrison review and sign-off.
4. Launch: testing, user acceptance testing, DNS cutover, handover.

Optional: Combinations pages (F03-006); Interior Doors and In-Stock products (F04-006).

## 15. Deliverables

- Redesigned website live on garrisonindustries.ky
- Approved design files and style guide
- Master product dataset (CSV/JSON)
- Extraction, normalisation and catalogue build scripts with refresh procedure
- Reconciliation report, test report and handover document
- Hosting and DNS runbook

## 16. Acceptance Criteria (Program Level)

| Perspective | Criterion |
|-------------|-----------|
| Visitor | Can browse, filter, search, view a product and send a product enquiry on any device |
| Garrison | Approved designs implemented; approved product set live with correct data |
| Data | Reconciliation shows the agreed product count published with zero unexplained gaps |
| Technical | Valid SSL, working email after cutover, no broken redirects |

## 17. Assumptions & Dependencies

1. Garrison holds written permission from Brenlo to use its product data and images before go-live (go/no-go).
2. Current website source code and admin logins are not needed; Garrison provides domain/DNS (registrar) access.
3. Planning quantity: 350 moulding products and about 15 existing pages; actuals confirmed early.
4. Products change rarely; later changes are made by a developer (no admin portal).
5. Garrison supplies brand assets and approves content; no new copywriting or photography.
6. Two review rounds each for wireframes, designs, the product workbook and user acceptance testing.
7. Hosting and third-party fees are paid by Garrison.

## 18. Appendices

### Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | Discovery & Website Design | Business | F01-001 … F01-003 (3) |
| 02 | Website Build | Business | F02-001 … F02-005 (5) |
| 03 | Product Catalogue Pages | Business | F03-001 … F03-006 (6) |
| 04 | One-time Product Data Migration | Technical | F04-001 … F04-006 (6) |
| 05 | Hosting, SEO & Launch | Shared | F05-001 … F05-005 (5) |

### Appendix B — Comparison of the Three Options

| Aspect | Option 1 — Design + Migration | Option 2 — Option 1 + AI Images | Option 3 — Premium Platform |
|---|---|---|---|
| New website design | Yes | Yes | Catalogue application integrated with website |
| Product data from source catalogue | Yes, one time | Yes, one time | Yes, via governed import |
| Product images | Source images (permission needed) | Original AI-assisted images | Source or Garrison images, with rights tracking |
| Admin portal and roles | No | No | Yes |
| Self-service product changes | No (developer) | No (developer) | Yes |
| Publishing workflow and rights gate | No | No | Yes |

### Appendix C — Risks

| Risk | Mitigation |
|------|-----------|
| Brenlo does not permit use of its data or images | Confirm before build; use Garrison's own data |
| Source site blocks extraction | Supplier data file or manual capture at a higher per-product rate |
| Registrar/DNS access unavailable | Garrison recovers access before cutover |
| Product count higher than planned | Per-product rate for extra products |
