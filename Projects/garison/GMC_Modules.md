# Garrison Online Moulding Catalogue Platform — Module List

Source: `SoW_GMC_Detailed.md` (derived from `Garrison_Technical_Proposal.md`)

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Administrator Access & Role Management | Shared | Admin sign-in and session security, user management, configurable role permissions, audit log | Explicit |
| 02 | Catalogue Taxonomy & Master Data | Business | Categories and sub-categories, styles, collections, materials/species, finishes | Explicit |
| 03 | Dynamic Attribute & Dimension Framework | Business | Attribute library, category attribute templates, template change impact, dimension normalisation | Explicit |
| 04 | Product Profile Management | Business | Product register, core profile, dynamic dimensions, materials/finishes/lengths, media, documents, lifecycle, preview | Explicit |
| 05 | Combinations & Product Relationships | Business | Typed product relationships; combinations as separate entity with component assembly | Explicit |
| 06 | Content Governance & Publishing Workflow | Business | Completeness and duplicate rules, submit/review/approve, publish/unpublish, workflow emails | Explicit |
| 07 | External Source, Provenance & Content Rights | Business | External source register, per-product provenance, rights-based publication gate and dashboard | Explicit |
| 08 | Public Catalogue Experience | Business | Catalogue home, listings, product detail, combination detail, responsive design system | Explicit |
| 09 | Search & Filtering | Business | Search index sync, ranked keyword/code/dimension search, configurable facets, suggestions | Explicit |
| 10 | Product Enquiry | Business | Contextual enquiry form, routing and acknowledgement emails, basic enquiry register | Explicit |
| 11 | SEO, Analytics & Website Integration | Shared | SEO URLs/metadata/redirects, sitemap and structured data, Garrison website integration, usage analytics | Explicit |
| 12 | Catalogue Data Import & Bulk Operations | Technical | Import templates and validation, bulk media matching, staging and commit, optional export/bulk update | Explicit |
| 13 | Platform Security, Performance & Operations | Technical | Media processing and CDN, security hardening, backup and monitoring, environments and deployment | Derived |

---

## Module Details

### 01. Administrator Access & Role Management

- **Type:** Shared
- **Summary:** Admin sign-in and session security, user management, configurable role permissions, audit log.
- **Source:** Explicit (Proposal §20, §22; FR-14, FR-20)
- **In Scope:** Admin authentication, password policy, lockout, reset; user invite and lifecycle; role-permission matrix; audit log with field-level diff
- **Out of Scope:** Public visitor accounts; SSO; MFA (future option)
- **Key Actors:** Super Administrator; Catalogue Administrator; Catalogue Reviewer; Content Administrator
- **Dependencies:** F06-005 (email connector); F13-002 (rate limiting)
- **Notes:** Access model User → Role → Permissions; four default roles seeded
- **Features:** F01-001 Administrator Authentication & Session Security, F01-002 Administrator User Management, F01-003 Role & Permission Configuration, F01-004 Administrative Audit Log

### 02. Catalogue Taxonomy & Master Data

- **Type:** Business
- **Summary:** Categories and sub-categories, styles, collections, materials/species, finishes.
- **Source:** Explicit (Proposal §8; FR-02, FR-07, FR-08)
- **In Scope:** Category hierarchy with ordering, imagery and SEO intro; styles; curated collections; material and finish masters with merge
- **Out of Scope:** Multi-language taxonomy
- **Key Actors:** Catalogue Administrator; Content Administrator
- **Dependencies:** Module 03 (templates); F11-001 (redirects); F09-001 (re-index)
- **Notes:** Classification layers kept independent for accurate filtering
- **Features:** F02-001 Category & Sub-category Management, F02-002 Style & Collection Management, F02-003 Material, Species & Finish Masters

### 03. Dynamic Attribute & Dimension Framework

- **Type:** Business
- **Summary:** Attribute library, category attribute templates, template change impact, dimension normalisation.
- **Source:** Explicit (Proposal §7; FR-04, FR-05)
- **In Scope:** Typed attributes with units and permitted values; per-category templates with mandatory/conditional/filterable flags; impact management; fraction/decimal/metric parsing
- **Out of Scope:** Formula-based calculated attributes
- **Key Actors:** Catalogue Administrator
- **Dependencies:** Module 02; consumed by Modules 04, 06, 09, 12
- **Notes:** Core enabler of 'no code change for new categories'
- **Features:** F03-001 Attribute Library & Units of Measure, F03-002 Category Attribute Templates, F03-003 Template Change Impact Management, F03-004 Dimension Normalisation & Display Formatting

### 04. Product Profile Management

- **Type:** Business
- **Summary:** Product register, core profile, dynamic dimensions, materials/finishes/lengths, media, documents, lifecycle, preview.
- **Source:** Explicit (Proposal §6, §12.1–12.2; FR-03, FR-05, FR-06)
- **In Scope:** Product workspace; template-driven entry; typed media and drawings; technical PDFs; duplicate/archive/restore; draft preview
- **Out of Scope:** Pricing, stock, CAD downloads
- **Key Actors:** Catalogue Administrator; Content Administrator; Catalogue Reviewer (preview)
- **Dependencies:** Modules 02, 03, 06; F13-001
- **Notes:** Working-draft model keeps published pages live during edits
- **Features:** F04-001 Product Register & Core Profile, F04-002 Category-driven Dimension & Attribute Entry, F04-003 Materials, Finishes, Lengths & Applications, F04-004 Product Media & Drawing Management, F04-005 Technical Document Management, F04-006 Product Duplicate, Archive & Restore, F04-007 Product Preview

### 05. Combinations & Product Relationships

- **Type:** Business
- **Summary:** Typed product relationships; combinations as separate entity with component assembly.
- **Source:** Explicit (Proposal §11; FR-09, FR-10)
- **In Scope:** Related/matching/alternative/similar relationships with reciprocity; combination records; component roles and order; 'Used in combinations'
- **Out of Scope:** Automatic recommendations
- **Key Actors:** Catalogue Administrator
- **Dependencies:** Module 04; Module 06; Module 08
- **Notes:** Combinations follow the same workflow as products
- **Features:** F05-001 Typed Product Relationships, F05-002 Combination Record Management, F05-003 Combination Component Assembly

### 06. Content Governance & Publishing Workflow

- **Type:** Business
- **Summary:** Completeness and duplicate rules, submit/review/approve, publish/unpublish, workflow emails.
- **Source:** Explicit (Proposal §12.3–12.4; FR-15, FR-21)
- **In Scope:** Completeness score and gate; duplicate detection; review queue; maker-checker decisions; bulk publish; email connector and templates
- **Out of Scope:** Multi-level approval chains; scheduled publishing
- **Key Actors:** Catalogue Administrator; Content Administrator; Catalogue Reviewer; Super Administrator
- **Dependencies:** Modules 04, 05, 07; F09-001; F11-002
- **Notes:** Notification embedded here (F06-005); no separate notification module
- **Features:** F06-001 Data Completeness & Duplicate Validation, F06-002 Submit for Review & Review Queue, F06-003 Review Decision & Approval History, F06-004 Publish, Unpublish & Bulk Publishing, F06-005 Workflow Email Notifications

### 07. External Source, Provenance & Content Rights

- **Type:** Business
- **Summary:** External source register, per-product provenance, rights-based publication gate and dashboard.
- **Source:** Explicit (Proposal §14; FR-16)
- **In Scope:** Source master with agreements; provenance fields and status history; gate matrix; Garrison-owned-content-only mode; re-verification
- **Out of Scope:** Automated scraping of external catalogues; legal verification of rights
- **Key Actors:** Catalogue Administrator; Super Administrator; Catalogue Reviewer (view)
- **Dependencies:** Modules 04, 06
- **Notes:** Gate enforced server-side and cannot be bypassed
- **Features:** F07-001 External Source Register, F07-002 Product Provenance Capture, F07-003 Content Rights Publication Gate & Rights Dashboard

### 08. Public Catalogue Experience

- **Type:** Business
- **Summary:** Catalogue home, listings, product detail, combination detail, responsive design system.
- **Source:** Explicit (Proposal §5, §10, §15; FR-01, FR-13)
- **In Scope:** Home; category/style/collection listings; product page with drawing viewer; combination page; brand-aligned component library; accessibility baseline
- **Out of Scope:** Customer accounts, favourites, comparison
- **Key Actors:** Visitor; Content Administrator (home settings)
- **Dependencies:** Modules 02–05, 09, 10, 11
- **Notes:** Server-rendered/pre-rendered for SEO
- **Features:** F08-001 Catalogue Home Page, F08-002 Category, Style & Collection Listing Pages, F08-003 Product Detail Page, F08-004 Combination Detail Page, F08-005 Responsive Catalogue Design System & Accessibility

### 09. Search & Filtering

- **Type:** Business
- **Summary:** Search index sync, ranked keyword/code/dimension search, configurable facets, suggestions.
- **Source:** Explicit (Proposal §9; FR-11, FR-12)
- **In Scope:** Dedicated search index; code-priority ranking; dimension phrase parsing; synonyms; template-driven list and range facets; type-ahead
- **Out of Scope:** AI/visual search
- **Key Actors:** Visitor; Catalogue Administrator (synonyms, facets)
- **Dependencies:** Modules 03, 06; F13-003
- **Notes:** Search engine choice confirmed at discovery
- **Features:** F09-001 Search Index & Publication Synchronisation, F09-002 Global Keyword, Code & Dimension Search, F09-003 Configurable Faceted Filters, F09-004 Search Suggestions & Results Experience

### 10. Product Enquiry

- **Type:** Business
- **Summary:** Contextual enquiry form, routing and acknowledgement emails, basic enquiry register.
- **Source:** Explicit (Proposal FR-17)
- **In Scope:** Enquiry form with spam protection; routing rules; acknowledgement; register with status, export and retention
- **Out of Scope:** Full enquiry/quote management; CRM integration
- **Key Actors:** Visitor; Catalogue Administrator; Garrison recipients
- **Dependencies:** Module 08; F06-005
- **Notes:** Full enquiry management is a future enhancement
- **Features:** F10-001 Product Enquiry Form, F10-002 Enquiry Routing & Acknowledgement, F10-003 Enquiry Register

### 11. SEO, Analytics & Website Integration

- **Type:** Shared
- **Summary:** SEO URLs/metadata/redirects, sitemap and structured data, Garrison website integration, usage analytics.
- **Source:** Explicit (Proposal §21; FR-18, FR-19)
- **In Scope:** URL scheme, metadata, canonical, redirects; sitemap, JSON-LD, social tags; header/footer/navigation integration; analytics events and insight dashboard
- **Out of Scope:** Ongoing SEO content marketing
- **Key Actors:** Content Administrator; Catalogue Administrator; Super Administrator; Garrison web administrator
- **Dependencies:** Module 08; Garrison website and hosting access
- **Notes:** Integration method (sub-path/sub-domain) confirmed at discovery
- **Features:** F11-001 SEO URLs, Metadata & Redirects, F11-002 Sitemap, Structured Data & Social Metadata, F11-003 Garrison Website Integration, F11-004 Catalogue Usage Analytics

### 12. Catalogue Data Import & Bulk Operations

- **Type:** Technical
- **Summary:** Import templates and validation, bulk media matching, staging and commit, optional export/bulk update.
- **Source:** Explicit (Proposal §13; FR-22); F12-004 Derived
- **In Scope:** Category import templates; validated bulk import; media auto-matching; staging grid and commit/rollback; export and bulk update (optional)
- **Out of Scope:** Manual data extraction and entry labour (priced per product)
- **Key Actors:** Catalogue Administrator; Data population team
- **Dependencies:** Modules 03, 04, 06; F13-001, F13-002
- **Notes:** Tooling for the population workstream; labour is a separate commercial line
- **Features:** F12-001 Import Templates & Bulk Product Import, F12-002 Bulk Media Upload & Auto-matching, F12-003 Import Staging Review & Commit, F12-004 Catalogue Export & Bulk Update

### 13. Platform Security, Performance & Operations

- **Type:** Technical
- **Summary:** Media processing and CDN, security hardening, backup and monitoring, environments and deployment.
- **Source:** Derived (Proposal §16, §19, §22, §26)
- **In Scope:** Derivatives and CDN; OWASP controls and upload scanning; backups, monitoring, logging; dev/staging/prod and pipeline
- **Out of Scope:** Hosting charges; independent VAPT; post-warranty operations (AMC)
- **Key Actors:** Super Administrator; Delivery/support team
- **Dependencies:** Garrison hosting environment
- **Notes:** Hosting stack finalised after discovery
- **Features:** F13-001 Media Processing & Content Delivery, F13-002 Security Hardening & Upload Protection, F13-003 Backup, Monitoring & Error Logging, F13-004 Environments & Deployment Pipeline

## Embedded capabilities (no separate module)

- **Notification:** workflow emails in F06-005 (shared email connector); enquiry emails in F10-002.
- **Document management:** technical documents in F04-005; source agreements in F07-001.
- **Workflow:** catalogue review and publishing workflow in Module 06.
- **Audit:** cross-cutting audit log in F01-004.
