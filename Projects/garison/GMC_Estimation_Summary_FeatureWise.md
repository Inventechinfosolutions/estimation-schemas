# GMC — Feature-wise Estimation Summary (Internal)

**Project:** Garrison Online Moulding Catalogue Platform  
**Project code:** GMC  
**As of:** 2026-10-05

## Grand totals

| Bucket | Hours |
|--------|------:|
| Recommended go-live | 4057 |
| Optional / conditional | 68 |
| All-in | 4125 |
| Features | 53 |
| Modules | 13 |

## Module-wise summary

| # | Module | Type | Features | UI | API | DB | Integ. | Test | Docs | Hours |
|---|--------|------|---------:|---:|---:|---:|---:|---:|---:|------:|
| 01 | Administrator Access & Role Management | Shared | 4 | 110 | 168 | 27 | 8 | 74 | 10 | 397 |
| 02 | Catalogue Taxonomy & Master Data | Business | 3 | 74 | 98 | 13 | 0 | 26 | 4 | 215 |
| 03 | Dynamic Attribute & Dimension Framework | Business | 4 | 120 | 136 | 26 | 0 | 58 | 10 | 350 |
| 04 | Product Profile Management | Business | 7 | 202 | 208 | 31 | 4 | 94 | 11 | 550 |
| 05 | Combinations & Product Relationships | Business | 3 | 76 | 102 | 14 | 0 | 32 | 4 | 228 |
| 06 | Content Governance & Publishing Workflow | Business | 5 | 160 | 190 | 23 | 20 | 80 | 10 | 483 |
| 07 | External Source, Provenance & Content Rights | Business | 3 | 76 | 90 | 11 | 0 | 32 | 6 | 215 |
| 08 | Public Catalogue Experience | Business | 5 | 228 | 70 | 9 | 0 | 74 | 8 | 389 |
| 09 | Search & Filtering | Business | 4 | 88 | 134 | 8 | 16 | 64 | 7 | 317 |
| 10 | Product Enquiry | Business | 3 | 40 | 60 | 5 | 12 | 30 | 3 | 150 |
| 11 | SEO, Analytics & Website Integration | Shared | 4 | 68 | 94 | 7 | 32 | 44 | 9 | 254 |
| 12 | Catalogue Data Import & Bulk Operations | Technical | 4 | 120 | 148 | 10 | 0 | 54 | 10 | 342 |
| 13 | Platform Security, Performance & Operations | Technical | 4 | 20 | 78 | 9 | 64 | 48 | 16 | 235 |
| | **Total** | | **53** | **1382** | **1576** | **193** | **156** | **710** | **108** | **4125** |

## Feature-wise detail

### 01 — Administrator Access & Role Management

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F01-001 | Administrator Authentication & Session Security | 6 | 7 | 26 | 44 | 7 | 4 | 20 | 3 | 104 | Go-live |
| F01-002 | Administrator User Management | 6 | 8 | 30 | 46 | 5 | 4 | 16 | 2 | 103 | Go-live |
| F01-003 | Role & Permission Configuration | 5 | 8 | 28 | 40 | 7 | 0 | 20 | 3 | 98 | Go-live |
| F01-004 | Administrative Audit Log | 4 | 6 | 26 | 38 | 8 | 0 | 18 | 2 | 92 | Go-live |

**Module total: 397 hours**

### 02 — Catalogue Taxonomy & Master Data

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F02-001 | Category & Sub-category Management | 5 | 8 | 32 | 46 | 6 | 0 | 12 | 2 | 98 | Go-live |
| F02-002 | Style & Collection Management | 5 | 6 | 20 | 26 | 3 | 0 | 8 | 1 | 58 | Go-live |
| F02-003 | Material, Species & Finish Masters | 5 | 6 | 22 | 26 | 4 | 0 | 6 | 1 | 59 | Go-live |

**Module total: 215 hours**

### 03 — Dynamic Attribute & Dimension Framework

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F03-001 | Attribute Library & Units of Measure | 5 | 7 | 32 | 40 | 9 | 0 | 12 | 3 | 96 | Go-live |
| F03-002 | Category Attribute Templates | 5 | 6 | 42 | 40 | 10 | 0 | 20 | 3 | 115 | Go-live |
| F03-003 | Template Change Impact Management | 3 | 4 | 24 | 30 | 4 | 0 | 12 | 2 | 72 | Go-live |
| F03-004 | Dimension Normalisation & Display Formatting | 3 | 4 | 22 | 26 | 3 | 0 | 14 | 2 | 67 | Go-live |

**Module total: 350 hours**

### 04 — Product Profile Management

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F04-001 | Product Register & Core Profile | 6 | 8 | 56 | 50 | 8 | 0 | 24 | 3 | 141 | Go-live |
| F04-002 | Category-driven Dimension & Attribute Entry | 3 | 4 | 32 | 28 | 8 | 0 | 14 | 2 | 84 | Go-live |
| F04-003 | Materials, Finishes, Lengths & Applications | 4 | 5 | 20 | 20 | 6 | 0 | 10 | 1 | 57 | Go-live |
| F04-004 | Product Media & Drawing Management | 5 | 6 | 44 | 28 | 4 | 4 | 16 | 2 | 98 | Go-live |
| F04-005 | Technical Document Management | 3 | 6 | 12 | 30 | 2 | 0 | 8 | 1 | 53 | Go-live |
| F04-006 | Product Duplicate, Archive & Restore | 4 | 5 | 18 | 34 | 2 | 0 | 12 | 1 | 67 | Go-live |
| F04-007 | Product Preview | 3 | 3 | 20 | 18 | 1 | 0 | 10 | 1 | 50 | Go-live |

**Module total: 550 hours**

### 05 — Combinations & Product Relationships

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F05-001 | Typed Product Relationships | 4 | 6 | 24 | 34 | 5 | 0 | 10 | 1 | 74 | Go-live |
| F05-002 | Combination Record Management | 4 | 6 | 30 | 40 | 6 | 0 | 12 | 2 | 90 | Go-live |
| F05-003 | Combination Component Assembly | 3 | 5 | 22 | 28 | 3 | 0 | 10 | 1 | 64 | Go-live |

**Module total: 228 hours**

### 06 — Content Governance & Publishing Workflow

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F06-001 | Data Completeness & Duplicate Validation | 4 | 6 | 46 | 36 | 4 | 0 | 18 | 3 | 107 | Go-live |
| F06-002 | Submit for Review & Review Queue | 4 | 6 | 30 | 38 | 5 | 0 | 18 | 2 | 93 | Go-live |
| F06-003 | Review Decision & Approval History | 5 | 6 | 34 | 42 | 6 | 0 | 16 | 2 | 100 | Go-live |
| F06-004 | Publish, Unpublish & Bulk Publishing | 4 | 4 | 28 | 46 | 4 | 4 | 18 | 2 | 102 | Go-live |
| F06-005 | Workflow Email Notifications | 4 | 5 | 22 | 28 | 4 | 16 | 10 | 1 | 81 | Go-live |

**Module total: 483 hours**

### 07 — External Source, Provenance & Content Rights

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F07-001 | External Source Register | 3 | 5 | 16 | 22 | 2 | 0 | 4 | 1 | 45 | Go-live |
| F07-002 | Product Provenance Capture | 4 | 5 | 28 | 32 | 6 | 0 | 14 | 2 | 82 | Go-live |
| F07-003 | Content Rights Publication Gate & Rights Dashboard | 4 | 6 | 32 | 36 | 3 | 0 | 14 | 3 | 88 | Go-live |

**Module total: 215 hours**

### 08 — Public Catalogue Experience

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F08-001 | Catalogue Home Page | 4 | 3 | 30 | 14 | 1 | 0 | 10 | 1 | 56 | Go-live |
| F08-002 | Category, Style & Collection Listing Pages | 6 | 4 | 56 | 22 | 2 | 0 | 18 | 1 | 99 | Go-live |
| F08-003 | Product Detail Page | 10 | 4 | 66 | 18 | 4 | 0 | 20 | 2 | 110 | Go-live |
| F08-004 | Combination Detail Page | 3 | 2 | 30 | 12 | 2 | 0 | 10 | 1 | 55 | Go-live |
| F08-005 | Responsive Catalogue Design System & Accessibility | 6 | 1 | 46 | 4 | 0 | 0 | 16 | 3 | 69 | Go-live |

**Module total: 389 hours**

### 09 — Search & Filtering

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F09-001 | Search Index & Publication Synchronisation | 2 | 5 | 8 | 44 | 2 | 16 | 14 | 2 | 86 | Go-live |
| F09-002 | Global Keyword, Code & Dimension Search | 3 | 4 | 22 | 32 | 3 | 0 | 20 | 2 | 79 | Go-live |
| F09-003 | Configurable Faceted Filters | 3 | 5 | 32 | 40 | 2 | 0 | 20 | 2 | 96 | Go-live |
| F09-004 | Search Suggestions & Results Experience | 4 | 3 | 26 | 18 | 1 | 0 | 10 | 1 | 56 | Go-live |

**Module total: 317 hours**

### 10 — Product Enquiry

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F10-001 | Product Enquiry Form | 3 | 2 | 16 | 12 | 2 | 8 | 12 | 1 | 51 | Go-live |
| F10-002 | Enquiry Routing & Acknowledgement | 2 | 4 | 10 | 20 | 1 | 4 | 10 | 1 | 46 | Go-live |
| F10-003 | Enquiry Register | 4 | 5 | 14 | 28 | 2 | 0 | 8 | 1 | 53 | Go-live |

**Module total: 150 hours**

### 11 — SEO, Analytics & Website Integration

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F11-001 | SEO URLs, Metadata & Redirects | 3 | 6 | 24 | 38 | 4 | 0 | 12 | 2 | 80 | Go-live |
| F11-002 | Sitemap, Structured Data & Social Metadata | 1 | 5 | 2 | 28 | 1 | 0 | 10 | 2 | 43 | Go-live |
| F11-003 | Garrison Website Integration | 3 | 2 | 22 | 8 | 0 | 24 | 12 | 3 | 69 | Go-live |
| F11-004 | Catalogue Usage Analytics | 2 | 3 | 20 | 20 | 2 | 8 | 10 | 2 | 62 | Go-live |

**Module total: 254 hours**

### 12 — Catalogue Data Import & Bulk Operations

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F12-001 | Import Templates & Bulk Product Import | 4 | 5 | 40 | 50 | 4 | 0 | 18 | 3 | 115 | Go-live |
| F12-002 | Bulk Media Upload & Auto-matching | 2 | 4 | 24 | 28 | 2 | 0 | 12 | 2 | 68 | Go-live |
| F12-003 | Import Staging Review & Commit | 3 | 4 | 34 | 38 | 2 | 0 | 14 | 3 | 91 | Go-live |
| F12-004 | Catalogue Export & Bulk Update | 2 | 3 | 22 | 32 | 2 | 0 | 10 | 2 | 68 | Optional |

**Module total: 342 hours**

### 13 — Platform Security, Performance & Operations

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F13-001 | Media Processing & Content Delivery | 2 | 4 | 10 | 30 | 2 | 16 | 12 | 2 | 72 | Go-live |
| F13-002 | Security Hardening & Upload Protection | 1 | 4 | 4 | 26 | 1 | 8 | 18 | 3 | 60 | Go-live |
| F13-003 | Backup, Monitoring & Error Logging | 1 | 4 | 6 | 22 | 2 | 8 | 10 | 4 | 52 | Go-live |
| F13-004 | Environments & Deployment Pipeline | 0 | 0 | 0 | 0 | 4 | 32 | 8 | 7 | 51 | Go-live |

**Module total: 235 hours**
