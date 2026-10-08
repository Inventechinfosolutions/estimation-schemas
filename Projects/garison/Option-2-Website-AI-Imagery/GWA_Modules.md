# Garrison Website Design, Product Catalogue Migration & AI Product Imagery (Option 2) — Module List

Source: `SoW_GWA_Detailed.md`

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Discovery & Website Design | Business | Discovery of the current site from its public pages, information architecture, wireframes and visual design | Explicit |
| 02 | Website Build | Business | Static website foundation, home page, company pages, contact form and existing content migration | Explicit |
| 03 | Product Catalogue Pages | Business | Mouldings landing page, category listings with filters, product detail, search and product enquiry | Explicit |
| 04 | One-time Product Data Migration | Technical | Extraction, image handling, normalisation, Garrison review workbook and catalogue data build | Explicit |
| 05 | Hosting, SEO & Launch | Shared | SEO and redirects, hosting, SSL and DNS cutover, analytics, quality assurance, testing and launch | Derived |
| 06 | AI Product Imagery | Technical | Original AI-assisted product images built from profile silhouettes, plus lifestyle scenes, review and provenance records | Explicit |

---

## Module Details

### 01. Discovery & Website Design

- **Type:** Business
- **Summary:** Discovery of the current site from its public pages, information architecture, wireframes and visual design.
- **Source:** Explicit (client request: website design)
- **In Scope:** Content capture, sitemap, wireframes, style guide, component library, page designs, prototype
- **Out of Scope:** New logo or brand identity; copywriting; photography
- **Key Actors:** Delivery business analyst and designer; Garrison business owner
- **Dependencies:** Garrison business owner availability
- **Notes:** Source code and admin logins are not needed; the site is rebuilt
- **Features:** F01-001 Existing Website Discovery & Content Capture, F01-002 Information Architecture & Wireframes, F01-003 Visual Design System & Page Designs

### 02. Website Build

- **Type:** Business
- **Summary:** Static website foundation, home page, company pages, contact form and existing content migration.
- **Source:** Explicit (client request: website design)
- **In Scope:** Layout, navigation, components, home, about, services, gallery, content pages, enquiry form, migrated content
- **Out of Scope:** Admin portal or content management system; e-commerce; customer accounts
- **Key Actors:** Visitor; Delivery developer
- **Dependencies:** Module 01
- **Notes:** No admin portal: content held in version-controlled files and changed by a developer
- **Features:** F02-001 Site Foundation, Layout & Navigation, F02-002 Home Page, F02-003 Company & Service Content Pages, F02-004 Contact & Enquiry Form, F02-005 Existing Content Migration

### 03. Product Catalogue Pages

- **Type:** Business
- **Summary:** Mouldings landing page, category listings with filters, product detail, search and product enquiry.
- **Source:** Explicit (client request); F03-006 Optional
- **In Scope:** Public catalogue pages generated from the one-time dataset
- **Out of Scope:** Quotes, pricing, cart, customer accounts
- **Key Actors:** Visitor
- **Dependencies:** Modules 02 and 04
- **Notes:** Fixed fields and filters
- **Features:** F03-001 Mouldings Landing Page, F03-002 Category Listing Page with Filters, F03-003 Product Detail Page, F03-004 Catalogue Search, F03-005 Product Enquiry, F03-006 Combinations Pages

### 04. One-time Product Data Migration

- **Type:** Technical
- **Summary:** Extraction, image handling, normalisation, Garrison review workbook and catalogue data build.
- **Source:** Explicit (client request); F04-006 Optional
- **In Scope:** Brenlo moulding products; one-time set-up of categories, styles and products; refresh procedure
- **Out of Scope:** Admin portal; new product descriptions or drawings; doors and sheet goods unless F04-006 is taken
- **Key Actors:** Delivery developer; Garrison catalogue owner (review)
- **Dependencies:** Brenlo permission (go/no-go)
- **Notes:** Replaces admin activities: catalogue, categories and products are set up once from the reviewed dataset
- **Features:** F04-001 Source Catalogue Extraction Utility, F04-002 Reference Image Capture (Internal Use Only), F04-003 Data Normalisation & Validation, F04-004 Garrison Review Workbook & Sign-off, F04-005 Catalogue Data Build & Publishing, F04-006 Interior Doors & In-Stock Product Extension

### 05. Hosting, SEO & Launch

- **Type:** Shared
- **Summary:** SEO and redirects, hosting, SSL and DNS cutover, analytics, quality assurance, testing and launch.
- **Source:** Derived
- **In Scope:** Hosting set-up, DNS cutover preserving email, SEO, analytics, testing, launch, handover
- **Out of Scope:** Hosting fees; ongoing support after warranty; paid advertising
- **Key Actors:** Delivery developer and QA; Garrison domain contact
- **Dependencies:** Domain/DNS access
- **Notes:** Google Workspace email records preserved
- **Features:** F05-001 SEO Foundation & Redirects, F05-002 Hosting, Domain, SSL & DNS Cutover, F05-003 Analytics & Cookie Consent, F05-004 Quality Assurance, Accessibility & Performance, F05-005 UAT, Launch & Handover

### 06. AI Product Imagery

- **Type:** Technical
- **Summary:** Original AI-assisted product images built from profile silhouettes, plus lifestyle scenes, review and provenance records.
- **Source:** Explicit (client request: AI image generation); F06-007 Optional
- **In Scope:** Style guide and pilot, silhouettes, base renders, AI generation, review, scenes, disclosure and provenance
- **Out of Scope:** Photography; legal opinion; AI service fees (shown separately as pass-through cost)
- **Key Actors:** Delivery imagery specialist and developer; Garrison business owner
- **Dependencies:** Module 04; Garrison legal review
- **Notes:** Brenlo photographs are not published and not sent to the AI service
- **Features:** F06-001 AI Imagery Style Guide, Model Setup & Pilot, F06-002 Profile Silhouette Preparation, F06-003 Base Render & AI Image Generation, F06-004 Image Review, Selection & Touch-up, F06-005 Lifestyle & Category Hero Images, F06-006 AI Image Disclosure & Provenance Record, F06-007 Finish / Species Variant Images
