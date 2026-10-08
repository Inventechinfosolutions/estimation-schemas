# Garrison Catalogue Product Migration to Existing Website (Option B) — Module List

Source: `SoW_GPM_Detailed.md`

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Catalogue Data Extraction & Preparation | Technical | Throttled extraction, image optimisation, normalisation and Garrison review workbook | Explicit |
| 02 | Product Data Store on Existing Website | Technical | Product storage, idempotent loader with rollback, media hosting | Derived |
| 03 | Catalogue Pages on Existing Website | Business | Landing page, category listings with filters, product detail, search, enquiry handoff | Explicit |
| 04 | Website Integration, SEO & Go-live | Shared | Code onboarding, environments, navigation/theme, SEO, reconciliation and go-live | Derived |

---

## Module Details

### 01. Catalogue Data Extraction & Preparation

- **Type:** Technical
- **Summary:** Throttled extraction, image optimisation, normalisation and Garrison review workbook.
- **Source:** Explicit (client request); F01-005 Optional
- **In Scope:** Moulding products and images from the source catalogue; normalisation; review workbook
- **Out of Scope:** New content creation; doors and sheet goods unless F01-005 is taken
- **Key Actors:** Delivery developer; Garrison catalogue owner (review)
- **Dependencies:** Brenlo permission; F04-001
- **Notes:** Supplier data file can replace extraction if Brenlo provides one
- **Features:** F01-001 Source Catalogue Extraction Utility, F01-002 Product Image Acquisition & Optimisation, F01-003 Data Normalisation & Validation, F01-004 Garrison Review Workbook & Sign-off, F01-005 Interior Doors & In-Stock Product Extension

### 02. Product Data Store on Existing Website

- **Type:** Technical
- **Summary:** Product storage, idempotent loader with rollback, media hosting.
- **Source:** Derived
- **In Scope:** Data store in existing stack; loader; media sync
- **Out of Scope:** Admin portal
- **Key Actors:** Delivery developer
- **Dependencies:** F04-001
- **Notes:** Developer-maintained; no admin portal
- **Features:** F02-001 Product Data Store & Loader, F02-002 Media Hosting & Delivery Setup

### 03. Catalogue Pages on Existing Website

- **Type:** Business
- **Summary:** Landing page, category listings with filters, product detail, search, enquiry handoff.
- **Source:** Explicit (client request); F03-006 Optional
- **In Scope:** Public catalogue templates in existing theme
- **Out of Scope:** Customer accounts, quotes, e-commerce
- **Key Actors:** Visitor
- **Dependencies:** Module 02; F04-002
- **Notes:** Fixed fields and filters
- **Features:** F03-001 Mouldings Landing Page, F03-002 Category Listing Page with Filters, F03-003 Product Detail Page, F03-004 Catalogue Search, F03-005 Product Enquiry Handoff, F03-006 Combinations Pages

### 04. Website Integration, SEO & Go-live

- **Type:** Shared
- **Summary:** Code onboarding, environments, navigation/theme, SEO, reconciliation and go-live.
- **Source:** Derived
- **In Scope:** Staging, backup, theme integration, SEO, UAT, deployment
- **Out of Scope:** Hosting migration, SSL remediation, redesign
- **Key Actors:** Delivery developer; Garrison hosting contact
- **Dependencies:** Garrison source code and access
- **Notes:** Changes only via staging with rollback
- **Features:** F04-001 Source Code Onboarding & Environment Setup, F04-002 Navigation & Theme Integration, F04-003 SEO, Sitemap & Redirects, F04-004 Migration Reconciliation & Go-live
