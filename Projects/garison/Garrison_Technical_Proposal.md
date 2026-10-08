# Technical Proposal

## Online Moulding Catalogue Platform

**Prepared for:** Garrison Industries  
**Prepared by:** InvenTech Info Solutions  
**Document type:** Technical & Commercial Proposal  
**Version:** 1.0 (Draft for review)  
**Date:** [DD Month YYYY]  
**Proposal reference:** [INV-GAR-YYYY-NNN]  
**Classification:** Confidential — for Garrison Industries evaluation only

---

> **EDITOR'S NOTE — REMOVE BEFORE ISSUE**
> This document contains **figure placeholders** marked `[FIGURE n PLACEHOLDER]`. Each placeholder states the figure's purpose, what it must show, a ready-to-use image-generation prompt, and output format.
> **Global visual style for all figures:** clean, flat, professional B2B consulting style; white or very light warm-grey background (#F7F5F2); primary navy #1B3A5F; accent warm oak #B07A45; secondary slate #5B6B7A; success green #3C8D5A for "Published/Approved" states; rounded rectangles, thin 1.5 px connectors, generous whitespace; sans-serif labels (Calibri / Inter); no 3D, no stock-photo people, no gradients beyond subtle tints.
> **Practical tip:** AI image generators often misspell labels. For label-heavy diagrams (architecture, data model, workflows, timeline) build the final figure in draw.io, Figma, Visio or PowerPoint using the **Must show** list as the specification, and use the prompt for visual style. Use AI generation directly for illustrative figures (UI mock-ups, cover, roadmap).
> Replace every placeholder with the final image, keep the caption line, and delete this note and all `Image generation` details before sending to Garrison.

---

## Table of Contents

1. Executive Summary
2. Understanding of the Requirement
3. Project Objectives
4. Proposed Solution Overview
5. Catalogue Experience
6. Product Information Framework
7. Dynamic Attribute & Dimension Framework
8. Categories, Styles & Collections
9. Search & Filtering
10. Product Detail Experience
11. Combinations & Product Relationships
12. Catalogue Administration & Publishing
13. Initial Catalogue Population
14. External Catalogue Sources & Content Rights
15. UX/UI Approach
16. Technical Architecture
17. Logical Data Model
18. Functional Requirements Matrix
19. Non-Functional Requirements
20. User Roles & Permissions
21. SEO & Website Integration
22. Security
23. Testing & Quality Assurance
24. Implementation Methodology
25. Project Timeline
26. Deliverables
27. Roles & Responsibilities
28. Assumptions
29. Dependencies
30. Risks & Mitigation
31. Commercial Proposal
32. Future Enhancements
33. Acceptance Criteria
34. Conclusion

---

## 1. Executive Summary

Garrison Industries intends to modernise its website by replacing the current mouldings page with a comprehensive, structured and user-friendly online moulding catalogue.

InvenTech Info Solutions proposes to design and develop a **reusable, scalable Online Moulding Catalogue Framework** for Garrison Industries, together with an **initial populated catalogue** ready for immediate use.

The solution is not a collection of static product pages. Every moulding profile will be maintained as a **structured product record** capturing category, style, product code, technical profile drawings, dimensions, materials, finishes, available lengths, descriptions, images, related products and moulding combinations. The level of detail will be comparable to leading industry catalogues such as Brenlo, which Garrison has identified as a benchmark.

The framework will be populated initially with Garrison's existing moulding range and with approved additional profiles identified from publicly available industry sources. A secure administration interface will allow authorised Garrison users to add, modify, review, publish and maintain future moulding profiles using the same standardised product structure — **without software development changes**.

**Key outcomes for Garrison:**

| Outcome | Benefit |
|---------|---------|
| Structured, searchable catalogue | Customers find profiles by category, style, code or dimension |
| Configurable product framework | New categories and products added without redesign or code changes |
| Initial populated dataset | Catalogue is useful from launch day |
| Self-service administration | Garrison controls content, publishing and growth |
| Content provenance and rights control | External references are tracked and published only with confirmed rights |
| SEO-ready product pages | Every profile is discoverable through search engines |

> **[FIGURE 1 PLACEHOLDER] Solution at a Glance — Framework + Populated Catalogue**
> **Purpose:** Communicate in one view that the project delivers two things: a reusable catalogue engine and a high-quality initial dataset.
> **Diagram type:** Conceptual overview illustration (two connected blocks feeding a website).
> **Must show:** Left block "Catalogue Framework" (icons: categories, product profiles, dimensions, media, search & filters, administration, publishing); right block "Initial Catalogue Population" (icons: existing Garrison catalogue, approved industry references, data normalisation, Garrison approval); both arrows converge into "Garrison Online Moulding Catalogue" shown as a laptop and phone displaying a moulding profile drawing; small caption "Garrison adds future products through the same framework".
> **Image generation prompt:** "Flat professional infographic, white background, two rounded navy (#1B3A5F) panels side by side labelled 'Catalogue Framework' and 'Initial Catalogue Population', each containing simple line icons (folder tree, ruler, image, magnifying glass, gear, checkmark document), arrows from both panels flowing into a central laptop and smartphone showing a wooden architectural moulding cross-section drawing, warm oak accent colour (#B07A45), minimal clean B2B consulting style, no people, no 3D, 16:9."
> **Format:** 16:9, 1600 × 900 px, PNG · file `fig01-solution-at-a-glance.png`

*Figure 1 — Solution at a glance*

---

## 2. Understanding of the Requirement

We understand the requirement as **two related deliverables**.

### 2.1 Reusable Catalogue Framework

A flexible platform through which Garrison can continuously maintain its moulding catalogue, covering categories, product profiles, technical attributes, dimensions, images and drawings, materials, finishes, combinations, related products, search and filters, and publishing.

### 2.2 Initial Populated Catalogue

The framework will initially be populated with:

1. Existing Garrison moulding profiles.
2. Relevant profile information from approved public sources.
3. Additional moulding profiles identified during the catalogue discovery exercise.
4. Structured product information prepared according to the new catalogue template.

The project is therefore not only to build a catalogue website; it is to **build the catalogue engine and populate it with a high-quality initial dataset**.

### 2.3 Source Material

The existing Garrison catalogue (approximately 38 pages) is a primary source for the initial population. It includes technical profile information, codes, dimensions, architectural installation photographs and combinations across the following categories:

Casings · Back Bands · Plinth and Corner Blocks · Baseboards · Crown Moulds · Chair Rails · Door Stops · Panel Moulds · Quarter / Half Rounds · Brick Moulds · Window Stool · Tongue & Groove Paneling · Combinations

### 2.4 Scope Interpretation

Garrison's requirement refers to the "full range of publicly available moulding profiles". Because this is an open-ended and continually changing set, we propose to define the scope as:

> **"A comprehensive range of moulding profiles drawn from Garrison's existing portfolio and approved publicly available industry sources, with Garrison determining the final products and content to be published."**

This keeps the platform scope fixed and makes the catalogue population effort measurable against an agreed product count.

---

## 3. Project Objectives

1. Replace the existing mouldings page with a modern, structured online catalogue integrated with the Garrison website.
2. Represent every moulding as a structured product record with technical detail comparable to leading industry catalogues.
3. Support both discovery-oriented browsing and specification-oriented searching.
4. Allow Garrison to add new categories, attributes and products without database redesign or code changes.
5. Deliver an initial catalogue populated with Garrison's range and approved additional profiles.
6. Maintain source and content-rights information for externally referenced products.
7. Provide SEO-friendly product and category pages that improve organic discovery.
8. Provide a controlled review and publishing workflow for catalogue content.

---

## 4. Proposed Solution Overview

The solution comprises a public-facing catalogue, an administration portal, and a structured catalogue data layer.

| Layer | Purpose |
|-------|---------|
| Online Catalogue (public) | Browse, search, filter, view product and combination pages, submit enquiries |
| Administration Portal | Manage products, taxonomy, attributes, media, relationships, sources and publishing |
| Catalogue Services | Product, search, media and enquiry services exposed through a catalogue API |
| Catalogue Data | Products, categories, attribute templates, dimensions, media, combinations, sources |

> **[FIGURE 2 PLACEHOLDER] Catalogue Framework Capability Map**
> **Purpose:** Show the full set of framework capabilities grouped logically.
> **Diagram type:** Capability map (grouped tiles).
> **Must show:** Four groups — **Customer Experience** (Catalogue Home, Search, Filters, Product Details, Combinations, Enquiry); **Catalogue Content** (Categories, Styles & Collections, Products, Attributes & Dimensions, Materials, Finishes, Media & Documents, Relationships); **Governance** (Draft–Review–Publish, Data Quality Rules, Source & Provenance, Audit Trail, User Roles); **Platform** (SEO, Website Integration, Analytics, Security, Responsive UI).
> **Image generation prompt:** "Clean capability map diagram, four rounded group containers in a 2x2 grid on light warm-grey background, each with a navy header bar and 5–8 small white tiles with thin line icons, accent oak brown highlights, flat B2B consulting style, crisp sans-serif labels, no people, 16:9."
> **Format:** 16:9, 1600 × 900 px, PNG · file `fig02-capability-map.png`

*Figure 2 — Catalogue framework capability map*

---

## 5. Catalogue Experience

### 5.1 Customer Journey

Garrison Website → Mouldings → Online Catalogue → Browse / Search / Filter → Category / Style → Product Profile → Technical Details → Related / Matching Profiles → Product Enquiry

> **[FIGURE 3 PLACEHOLDER] Customer Journey**
> **Purpose:** Illustrate how a visitor moves from the Garrison website to an enquiry.
> **Diagram type:** Horizontal journey map with stage icons.
> **Must show:** Eight stages in order — Garrison Website, Online Catalogue, Browse / Search / Filter, Category & Style, Product Profile, Technical Details, Related & Matching Profiles, Request Information. Below the line, two persona call-outs: "Discovery: *I need a crown moulding*" and "Specification: *about 3/4 in thick and 5 in wide*".
> **Image generation prompt:** "Horizontal customer journey map infographic, eight circular navy stage icons connected by a thin oak-brown line, icons for website, catalogue book, magnifying glass with filter funnel, category tags, moulding profile drawing, ruler with dimensions, linked chain, envelope enquiry; two speech-bubble callouts underneath; flat minimal consulting style, white background, 16:9."
> **Format:** 16:9, 1600 × 700 px, PNG · file `fig03-customer-journey.png`

*Figure 3 — Customer journey*

### 5.2 Two Ways to Find a Profile

| Mode | Example need | How the catalogue supports it |
|------|--------------|-------------------------------|
| Discovery-oriented browsing | "I need a crown moulding." | Category and style navigation, curated collections, imagery |
| Specification-oriented searching | "I need a moulding about 3/4 inch thick and 5 inches wide." | Structured dimension attributes, numeric filters, code search |

Structured product attributes make specification-oriented search possible; this is a core reason for the structured product model described in Section 6.

### 5.3 Responsive Experience

| Device | Experience focus |
|--------|------------------|
| Desktop | Rich filtering, side-by-side detail, technical drawings at full size |
| Tablet | Optimised browsing and readable technical information |
| Mobile | Search-first and filter-first discovery; tap-to-enquire |

The catalogue will match the visual identity of the existing Garrison website while providing a modern product-discovery experience.

---

## 6. Product Information Framework

Every moulding is represented as a structured **Product Profile**.

### 6.1 Core Product Information

| Field | Description |
|-------|-------------|
| Product ID | Internal unique identifier |
| Product Code | Garrison or source profile number |
| Product Name | Display name |
| Category | Casing, Crown, Baseboard, etc. |
| Sub-category | Optional classification |
| Collection / Style | Classic, Modern, Transitional, etc. |
| Status | Draft / In Review / Approved / Published / Archived |
| Short Description | Catalogue summary |
| Detailed Description | Full description |
| Featured Product | Yes / No |

### 6.2 Technical Profile Information

The existing Garrison catalogue presents products primarily through **technical profile drawings and dimensions**, not product photographs alone. Each product therefore supports:

- Profile drawing and profile image
- Cross-sectional illustration
- Dimension drawing
- Technical document (PDF)
- High-resolution image
- Additional product images

### 6.3 Media Structure

| Media type | Use |
|------------|-----|
| Primary image | Listing and hero display |
| Profile drawing | Technical cross-section |
| Dimension drawing | Annotated measurements |
| Installed / application image | Design inspiration |
| Gallery images | Additional views |
| Technical PDF | Downloadable specification |
| Additional documents | Supporting material |

This allows the catalogue to provide both **technical information** and **design inspiration**, as the existing Garrison catalogue does by combining installation photographs with profile drawings.

> **[FIGURE 4 PLACEHOLDER] Product Profile Anatomy**
> **Purpose:** Show what makes up one product record.
> **Diagram type:** Hub-and-spoke diagram.
> **Must show:** Centre node "Product Profile (Code · Name · Category · Style · Status)"; spokes to Technical Dimensions, Profile & Dimension Drawings, Images & Gallery, Materials / Species, Finishes, Available Lengths, Documents, Related Products, Combinations, Source & Provenance, SEO Metadata.
> **Image generation prompt:** "Hub and spoke infographic, central rounded navy card showing a wooden moulding cross-section icon labelled 'Product Profile', eleven surrounding white rounded cards with thin oak-brown connectors, each card with a simple line icon (ruler, drawing, photo, wood grain, paint swatch, length arrow, PDF, link, stacked profiles, source tag, globe), flat clean B2B style, light background, 1:1."
> **Format:** 1:1, 1200 × 1200 px, PNG · file `fig04-product-profile-anatomy.png`

*Figure 4 — Product profile anatomy*

---

## 7. Dynamic Attribute & Dimension Framework

### 7.1 Why Dimensions Must Be Configurable

Different moulding categories are measured differently. A single hard-coded dimension model would force irrelevant fields onto products and block future categories.

| Category | Typical dimensions |
|----------|--------------------|
| Casing | Width, Height / Thickness, Projection |
| Crown | Projection, Height, Thickness |
| Panel Mould | Width, Thickness, Projection |
| Half Round | Diameter, Length |

### 7.2 How It Works

**Category → Category Attribute Template → Product → Applicable Dimensions & Attributes**

Each category carries an attribute template defining which attributes apply, which are mandatory, their units and permitted values. When an administrator creates a product, the system presents only the fields relevant to the selected category.

This allows Garrison to introduce a new product category in future **without database redesign or application code changes**.

> **[FIGURE 5 PLACEHOLDER] Dynamic Attribute & Dimension Framework**
> **Purpose:** Explain the configurable template mechanism to non-technical readers.
> **Diagram type:** Left-to-right flow with example.
> **Must show:** Four stages — "Category" → "Attribute Template" → "Product" → "Displayed Fields". Two worked examples as parallel lanes: *Crown* (Projection, Height, Thickness) and *Half Round* (Diameter, Length). A side note: "New category = new template, no code change".
> **Image generation prompt:** "Flat process diagram with two horizontal swim lanes, each lane flows through four rounded boxes: category, template checklist, product card, form with dimension fields; top lane shows a crown moulding icon, bottom lane a half-round moulding icon; navy boxes, oak-brown arrows, light grey lane backgrounds, clean consulting style, 16:9."
> **Format:** 16:9, 1600 × 800 px, PNG · file `fig05-dynamic-attributes.png`

*Figure 5 — Dynamic attribute and dimension framework*

### 7.3 Attribute Groups

| Group | Attributes |
|-------|-----------|
| Classification | Category, Sub-category, Style, Collection |
| Technical | Width, Height, Thickness, Projection, Diameter, Length, other category-specific dimensions |
| Material | Species, Wood type, Engineered material, MDF, Other |
| Finish | Natural, Primed, Painted, Custom, Other approved finishes |
| Commercial / Availability | Available length, Standard / random length, Minimum quantity, Special-order indicator |

Not every attribute applies to every product; the catalogue displays attributes according to category configuration.

---

## 8. Categories, Styles & Collections

### 8.1 Categories

Initial categories will be based on the existing Garrison catalogue: Casings, Back Bands, Plinth Blocks, Corner Blocks, Baseboards, Crown Moulds, Chair Rails, Door Stops, Panel Moulds, Quarter Rounds, Half Rounds, Brick Moulds, Window Stool, Tongue & Groove Paneling and Combinations.

Categories are configurable; Garrison can add, rename, reorder or retire categories through administration.

### 8.2 Styles and Collections

Style and collection form a **separate classification layer** from category and material, e.g. Classic, Modern, Transitional and other Garrison-defined styles.

| Dimension of classification | Example value |
|-----------------------------|---------------|
| Category | Crown |
| Style | Traditional |
| Collection | Heritage |
| Material | Oak |

Keeping these independent means "Classic", "Crown" and "Oak" are never treated as the same kind of data, which keeps filtering accurate and the taxonomy maintainable.

---

## 9. Search & Filtering

### 9.1 Global Search

Visitors can search by product code, product name, category, style, material, dimensions and keywords — for example `2051` or `5 inch crown`. Exact search behaviour (ranking, partial matches, unit handling) will be refined during UX design.

### 9.2 Advanced Filtering

Filters are driven by catalogue configuration, so new attributes can become filters without development.

| Filter | Example options |
|--------|-----------------|
| Category | Crown, Casing, Baseboard, Chair Rail |
| Style | Classic, Modern, Transitional |
| Material | Oak, Maple, Pine, MDF |
| Thickness | 1/2", 3/4", 7/8" |
| Width | 3", 4", 5", 6" |

> **[FIGURE 6 PLACEHOLDER] Catalogue Listing Page — Search & Filter (UI concept)**
> **Purpose:** Give Garrison a visual impression of the browsing experience. Indicative only; final design follows UX phase.
> **Diagram type:** Desktop UI mock-up (wireframe-plus, light styling).
> **Must show:** Top bar with Garrison logo placeholder and search box; breadcrumb "Mouldings › Crown"; left filter panel (Category, Style, Material, Thickness, Width with checkboxes); main grid of 9 product cards each showing a black-line moulding profile drawing, product code (e.g., CM-101), name and "W × T" dimensions; result count and sort control; label "Indicative concept".
> **Image generation prompt:** "Clean desktop web UI mockup of an architectural wood moulding catalogue, white background, top navigation with logo placeholder and search bar, left sidebar with checkbox filters for category, style, material, thickness and width, main 3x3 grid of product cards each showing a black line-drawing cross-section of a wood moulding profile with product code and dimensions below, navy and warm oak accent colours, modern minimal e-catalogue design, 16:10."
> **Format:** 16:10, 1600 × 1000 px, PNG · file `fig06-listing-page-concept.png`

*Figure 6 — Catalogue listing page concept (indicative)*

---

## 10. Product Detail Experience

Each published product has a dedicated detail page. Indicative content order:

1. Product name, product code, category and style
2. Profile / technical drawing
3. Dimensions (width, height, thickness, projection — as applicable)
4. Description
5. Material / species
6. Finish options
7. Available lengths
8. Applications
9. Related products
10. Combinations in which the profile is used
11. **Request Information** action

> **[FIGURE 7 PLACEHOLDER] Product Detail Page (UI concept)**
> **Purpose:** Show how technical and inspirational content combine on one page.
> **Diagram type:** Desktop UI mock-up.
> **Must show:** Left large profile drawing with dimension call-outs; right column with product name, code, category/style tags, dimension table, material and finish chips, available lengths; below: description, application photo strip, "Related Products" carousel, "Used in Combinations" block; prominent "Request Information" button; label "Indicative concept".
> **Image generation prompt:** "Modern desktop product detail page mockup for an architectural wood moulding, large black technical cross-section drawing with dimension arrows on the left, right column with product title, code, style tags, clean dimension table, wood species and finish swatches, available lengths, a navy 'Request Information' button, lower section with interior room photo strip showing installed crown moulding and a related products carousel of line-drawing cards, white background, navy and oak accents, minimal premium design, 16:10."
> **Format:** 16:10, 1600 × 1000 px, PNG · file `fig07-product-detail-concept.png`

*Figure 7 — Product detail page concept (indicative)*

---

## 11. Combinations & Product Relationships

### 11.1 Product Relationships

The catalogue supports typed relationships between profiles:

| Relationship type | Example use |
|-------------------|-------------|
| Related product | General cross-sell |
| Matching casing / matching crown | Coordinated room trim |
| Alternative profile | Substitute when unavailable |
| Similar product | Visually comparable profile |
| Component of combination | Profile used inside a combination |

### 11.2 Combination Catalogue

The existing Garrison catalogue includes dedicated combination sections where several profiles are assembled together. Combinations will be managed as a **separate catalogue entity**, not as free-text descriptions.

A combination page shows: combination image / drawing, name, code, component profiles with links, overall dimensions and description.

> **[FIGURE 8 PLACEHOLDER] Combination Structure**
> **Purpose:** Show how a combination is built from linked component profiles.
> **Diagram type:** Exploded assembly illustration with links.
> **Must show:** One assembled combination cross-section (crown + back band + casing + baseboard) on the left; on the right, each component as a separate profile card with its product code, connected by thin lines to its position in the assembly; caption "Each component links to its own product page".
> **Image generation prompt:** "Technical exploded-view illustration of an architectural wood moulding combination, assembled cross-section on the left made of crown, back band, casing and baseboard profiles in black line art, on the right four separated profile cards with codes, thin navy leader lines connecting each card to its position, warm oak highlight on the assembly, clean white background, engineering catalogue style, 16:9."
> **Format:** 16:9, 1600 × 900 px, PNG · file `fig08-combination-structure.png`

*Figure 8 — Combination structure*

---

## 12. Catalogue Administration & Publishing

### 12.1 Administration Functions

| Area | Functions |
|------|-----------|
| Products | Add, edit, duplicate, archive, preview, publish / unpublish |
| Taxonomy | Manage categories, sub-categories, styles, collections |
| Masters | Manage materials, finishes, attributes and attribute templates |
| Relationships | Manage related products and combinations |
| Media | Manage images, drawings and technical documents |
| Sources | Record external source and content-rights status |
| Governance | Review queue, approval history, audit log |

### 12.2 Adding a New Moulding

1. Select category
2. System loads the category template
3. Enter product information
4. Enter applicable dimensions
5. Upload profile drawing
6. Add images
7. Select material(s)
8. Select finish(es)
9. Add related products / combinations
10. Add source information (for external references)
11. Preview
12. Submit for review → publish

Garrison can add product 001 today, product 500 next year and product 2,000 later using the same framework.

> **[FIGURE 9 PLACEHOLDER] Add New Moulding — Administrator Workflow**
> **Purpose:** Demonstrate that adding products is a guided, repeatable process.
> **Diagram type:** Numbered step flow (two rows of six steps).
> **Must show:** The twelve steps listed in Section 12.2 with small icons; a highlight on step 2 "Template loads category-specific fields".
> **Image generation prompt:** "Numbered step-by-step process infographic, twelve rounded step cards in two rows of six connected by arrows, each with a small line icon (category folder, template, form, ruler, drawing upload, photo, wood grain, paint swatch, link, source tag, eye preview, publish rocket/check), step 2 highlighted in oak brown, others navy outline, white background, clean flat style, 16:9."
> **Format:** 16:9, 1600 × 800 px, PNG · file `fig09-add-product-workflow.png`

*Figure 9 — Add new moulding workflow*

### 12.3 Review & Publishing Workflow

**Draft → In Review → Approved → Published** (with **Changes Requested** returning to Draft, and **Archived** for retired products)

This is particularly valuable while catalogue data is prepared by several contributors.

> **[FIGURE 10 PLACEHOLDER] Content Publishing Lifecycle**
> **Purpose:** Show content states and who moves content between them.
> **Diagram type:** State diagram.
> **Must show:** States Draft, In Review, Approved, Published, Archived; transitions — Submit (Administrator), Request Changes (Reviewer, back to Draft), Approve (Reviewer), Publish (Administrator), Unpublish / Archive; Published state in green.
> **Image generation prompt:** "Simple state lifecycle diagram, five rounded state pills in a left-to-right flow labelled Draft, In Review, Approved, Published, Archived, curved return arrow from In Review back to Draft, Published pill in green, others navy outline, small role labels on arrows, flat minimal style, white background, 16:9."
> **Format:** 16:9, 1400 × 600 px, PNG · file `fig10-publishing-lifecycle.png`

*Figure 10 — Content publishing lifecycle*

### 12.4 Product Data Quality Rules

**Mandatory baseline**

| Information | Requirement |
|-------------|-------------|
| Product Code | Mandatory |
| Product Name | Mandatory |
| Category | Mandatory |
| Profile Image / Drawing | Mandatory where available |
| Description | Mandatory |
| Applicable Dimensions | Mandatory (per category template) |
| Source | Mandatory for external products |
| Source Reference | Mandatory for external products |

**Conditional** — material, finish, length, applications, related products and technical documents become mandatory where the category template requires them.

Products failing completeness rules cannot be submitted for review.

---

## 13. Initial Catalogue Population

Initial catalogue population is delivered as a **dedicated workstream**, running in parallel with platform development.

### 13.1 Sources

| Source | Content |
|--------|---------|
| Existing Garrison catalogue | Profile codes, categories, technical drawings, dimensions, combinations, general information |
| Approved external catalogues | Additional profiles identified for inclusion (e.g., Brenlo), subject to Section 14 |

### 13.2 Data Preparation Process

Source Catalogue → Profile Identification → Data Extraction → Data Normalisation → Category Mapping → Attribute Mapping → Image / Drawing Preparation → Quality Review → Garrison Approval → Catalogue Import

> **[FIGURE 11 PLACEHOLDER] Catalogue Data Population Pipeline**
> **Purpose:** Show the controlled, quality-assured path from source material to published records.
> **Diagram type:** Pipeline / funnel flow.
> **Must show:** Two inputs on the left ("Garrison Catalogue (38 pp)", "Approved Industry Sources"); ten pipeline stages from Section 13.2; a gate icon at "Garrison Approval"; output "Structured Catalogue Records"; a side callout "Provenance captured for external sources".
> **Image generation prompt:** "Horizontal data pipeline infographic, two input document stacks on the left (catalogue booklet and web pages) feeding a series of ten connected rounded stage boxes, a gate/checkpoint icon before the final stage, output on the right as a neat database of product cards, navy stages, oak-brown connectors, small shield callout for provenance, flat clean consulting style, white background, 16:9."
> **Format:** 16:9, 1800 × 800 px, PNG · file `fig11-data-population-pipeline.png`

*Figure 11 — Catalogue data population pipeline*

### 13.3 Population Phases

| Phase | Activity |
|-------|----------|
| 1 — Existing Garrison data | Convert the current catalogue into structured records |
| 2 — Catalogue expansion | Identify additional relevant profiles from approved sources |
| 3 — Data standardisation | Normalise categories, codes, dimensions, units, materials, styles and terminology |
| 4 — Quality review | Garrison reviews and approves the initial dataset |
| 5 — Publishing | Approved records are published |

The number of products in the initial population will be agreed during discovery and forms the basis of the population commercial line (Section 31).

---

## 14. External Catalogue Sources & Content Rights

### 14.1 Third-Party Catalogue and External Content Clarification

Garrison Industries has indicated that the new catalogue should include relevant moulding profiles and information available through publicly accessible external catalogues, including Brenlo.

Such external catalogues will be treated as **reference sources** for product discovery, industry classification, catalogue structure, technical attributes and user-experience benchmarking. The solution will maintain source and provenance information for every externally referenced product.

Public accessibility of a website or catalogue does not, by itself, establish rights to reproduce or redistribute its proprietary product descriptions, photographs, technical drawings, profile artwork, catalogue graphics or other protected content. Accordingly, reproduction of third-party content within the Garrison catalogue will be subject to Garrison confirming the appropriate rights, permissions or licences. Where such rights are not available, the source may be used for research and classification purposes only, or alternative Garrison-owned content may be created or provided.

Final inclusion of third-party products and associated content is subject to Garrison's approval and confirmation of applicable usage rights.

### 14.2 Reference Use versus Content Reproduction

| Reference / research (in scope) | Content reproduction (requires confirmed rights) |
|---------------------------------|--------------------------------------------------|
| Identify moulding categories and common profile types | Product descriptions |
| Understand industry classification | Product photographs |
| Identify technical attributes | Technical drawings and profile images |
| Benchmark catalogue UX | Catalogue graphics and artwork |
| Determine useful filters and search criteria | Proprietary product data |

Where rights are not available, the team can use the source as reference only, capture generic product attributes where legally permissible, create Garrison-owned representations, link to the original source where appropriate, or exclude restricted content until authorisation is obtained.

### 14.3 Provenance Captured per External Product

| Field | Purpose |
|-------|---------|
| Source Name | e.g., Brenlo |
| Source URL | Original public source |
| Source Catalogue | Catalogue / series name |
| Original Product Code | Source identifier |
| Source Category | Original classification |
| Data Usage Status | Approved / Pending / Restricted |
| Content Rights Status | Confirmed / To be confirmed |
| Date Verified | Last verification date |
| Garrison Product Status | Reference / Garrison / Other |

Products with a rights status of "To be confirmed" or a usage status of "Restricted" cannot be published with third-party media.

> **[FIGURE 12 PLACEHOLDER] External Content Governance Decision Flow**
> **Purpose:** Show how each external profile is assessed before publication.
> **Diagram type:** Decision flowchart.
> **Must show:** Start "External profile identified" → "Record source & provenance" → decision "Garrison wants to include?" (No → Exclude) → decision "Rights confirmed for media/text?" — Yes → "Publish with source content"; No → decision "Generic attributes permissible?" — Yes → "Publish with Garrison-owned content / attributes only"; No → "Reference only (not published)".
> **Image generation prompt:** "Clean decision flowchart, rounded start box, rectangular process steps and diamond decision shapes, three end outcomes coloured green (publish with source content), oak brown (publish with Garrison-owned content), grey (reference only / exclude), navy outlines, thin connectors with Yes/No labels, flat consulting style, white background, 4:3."
> **Format:** 4:3, 1400 × 1050 px, PNG · file `fig12-content-governance-flow.png`

*Figure 12 — External content governance decision flow*

---

## 15. UX/UI Approach

1. **Discovery & benchmarking** — review the current Garrison site, existing catalogue and benchmark catalogues (including Brenlo) for navigation, filtering and profile presentation patterns.
2. **Information architecture** — confirm taxonomy, navigation, filter set and page templates with Garrison.
3. **Wireframes** — catalogue home, category listing, search results, product detail, combination detail, enquiry and key admin screens.
4. **Visual design** — apply Garrison branding; high-fidelity designs for desktop and mobile.
5. **Design approval** — Garrison sign-off before build of the public catalogue.

Benchmark catalogues inform structure and usability principles only; data, design, terminology and branding remain Garrison's own.

---

## 16. Technical Architecture

The architecture is technology-neutral at proposal stage. The final technology stack will be aligned with Garrison's existing website and hosting environment after technical discovery.

| Component | Responsibility |
|-----------|----------------|
| Online Catalogue UI | Public browsing, search, filters, product and combination pages |
| Admin Portal | Catalogue management, workflow, sources, media |
| Catalogue API | Single access layer for UI and admin |
| Product Service | Products, taxonomy, attributes, relationships, combinations |
| Search Service & Index | Fast keyword, code and attribute search with faceted filters |
| Media Store / CDN | Optimised images, drawings and documents |
| Product Database | Structured catalogue data and audit history |
| Enquiry handling | Capture and route product enquiries to Garrison |

**Architecture principles:** content-driven (no developer effort per product), configurable taxonomy and attributes, search-optimised, media-optimised, secure administration, and integration with the existing Garrison website.

> **[FIGURE 13 PLACEHOLDER] Solution Architecture**
> **Purpose:** Present a clear, technology-neutral logical architecture.
> **Diagram type:** Layered architecture diagram.
> **Must show:** Top layer — "Garrison Website" and "Visitors (desktop / tablet / mobile)"; Presentation — "Online Catalogue UI" and "Admin Portal (authorised users)"; Services — "Catalogue API" fronting "Product Service", "Search Service", "Media Service", "Enquiry Service"; Data — "Product Database", "Search Index", "Media Store / CDN"; side band — "Security & Access Control", "Audit Logging", "Monitoring & Backup"; note "Technology stack confirmed after discovery".
> **Image generation prompt:** "Layered software architecture diagram, four horizontal bands (users/website, presentation, services, data) with rounded component boxes, vertical side band for security, audit and monitoring, navy boxes with white labels, oak-brown accent for the Catalogue API, thin connectors, database cylinder icons in the data layer, flat clean enterprise style, white background, 16:9."
> **Format:** 16:9, 1600 × 1000 px, PNG · file `fig13-solution-architecture.png`

*Figure 13 — Solution architecture (logical)*

---

## 17. Logical Data Model

The logical model centres on Category, Product and Attribute Template.

| Entity group | Entities |
|--------------|----------|
| Taxonomy | Category, SubCategory, Collection, Style |
| Product | Product, Attribute Template, Attribute, AttributeValue, ProductAttribute |
| Masters | Material, Finish |
| Content | Media, Document |
| Relationships | ProductRelationship, Combination, CombinationComponent |
| Provenance | Source, CatalogueReference |
| Engagement | Enquiry |
| Administration | User, Role, AuditLog |

> **[FIGURE 14 PLACEHOLDER] Logical Data Model**
> **Purpose:** Show key entities and relationships at a business level (not a physical database design).
> **Diagram type:** Simplified entity-relationship diagram.
> **Must show:** Category 1–* Product; Category 1–1 Attribute Template; Attribute Template *–* Attribute; Product *–* AttributeValue (via ProductAttribute); Product *–* Material; Product *–* Finish; Product 1–* Media; Product 1–* Document; Product *–* Product (ProductRelationship); Combination 1–* CombinationComponent *–1 Product; Product *–1 Source (optional); Product 1–* Enquiry; User *–1 Role; AuditLog linked to User.
> **Image generation prompt:** "Simplified entity relationship diagram, rounded entity boxes with entity names only, Product box larger in the centre highlighted oak brown, surrounding navy-outlined boxes for Category, Attribute Template, Attribute, Material, Finish, Media, Document, Combination, Source, Enquiry, thin crow's-foot connectors, flat clean style, white background, 16:9."
> **Format:** 16:9, 1600 × 1000 px, PNG · file `fig14-logical-data-model.png`

*Figure 14 — Logical data model*

---

## 18. Functional Requirements Matrix

| Ref | Module | Requirement |
|-----|--------|-------------|
| FR-01 | Catalogue Home | Catalogue landing page with category entry points and featured products |
| FR-02 | Category Management | Configure categories and sub-categories with ordering and status |
| FR-03 | Product Management | Create, edit, duplicate, archive and preview product profiles |
| FR-04 | Attribute Management | Configure attributes and category attribute templates |
| FR-05 | Dimension Management | Capture category-specific technical dimensions with units |
| FR-06 | Media Management | Upload, optimise and order images, drawings and documents |
| FR-07 | Material Management | Maintain material / species master |
| FR-08 | Finish Management | Maintain finish master |
| FR-09 | Combination Management | Create combinations with linked component profiles |
| FR-10 | Relationship Management | Define typed product relationships |
| FR-11 | Search | Search by code, name, category, style, material, dimensions and keywords |
| FR-12 | Filters | Configurable attribute-based faceted filters |
| FR-13 | Product Details | Detailed product and combination pages |
| FR-14 | Admin Portal | Secure role-based catalogue administration |
| FR-15 | Publishing | Draft → Review → Approve → Publish workflow with history |
| FR-16 | External Source Management | Capture source, provenance and content-rights status |
| FR-17 | Enquiry | Product enquiry form routed to Garrison |
| FR-18 | SEO | SEO-friendly URLs, metadata, sitemap, structured data |
| FR-19 | Analytics | Catalogue usage tracking via website analytics |
| FR-20 | Audit | Track administrative changes with user and timestamp |
| FR-21 | Data Quality | Enforce mandatory and conditional completeness rules |
| FR-22 | Data Import | Import prepared initial catalogue records |

---

## 19. Non-Functional Requirements

| Area | Requirement |
|------|-------------|
| Performance | Fast catalogue loading; optimised images; pagination / lazy loading; search optimised for large volumes |
| Scalability | Growth from ~100 to 1,000 to 10,000+ products without redesigning the product model |
| Availability | Production deployment suited to Garrison's hosting environment; backup strategy; monitoring and error logging |
| Usability | Responsive across desktop, tablet and mobile; consistent with Garrison branding |
| Accessibility | Designed with reference to WCAG 2.1 AA good practice (alt text, contrast, keyboard navigation) |
| Maintainability | Content-driven; no developer effort to add products, categories or attributes |
| Browser support | Current versions of Chrome, Edge, Safari and Firefox |

---

## 20. User Roles & Permissions

| Capability | Super Administrator | Catalogue Administrator | Catalogue Reviewer | Content Administrator |
|------------|:---:|:---:|:---:|:---:|
| Create / edit products | ✓ | ✓ | — | Content fields |
| Manage categories & attributes | ✓ | ✓ | — | — |
| Manage images, documents, SEO content | ✓ | ✓ | — | ✓ |
| Review / approve / request changes | ✓ | — | ✓ | — |
| Publish / unpublish | ✓ | ✓ | — | — |
| Manage sources & rights status | ✓ | ✓ | View | — |
| Manage users & roles | ✓ | — | — | — |
| View audit log | ✓ | View | View | — |

Role permissions are configurable and will be confirmed during discovery.

---

## 21. SEO & Website Integration

### 21.1 SEO Foundation

- SEO-friendly URLs, e.g. `/mouldings/crown/CM-001`, `/mouldings/casing/C-123`
- Editable page titles and meta descriptions
- Product structured data where appropriate
- Category page SEO content
- Search-engine-readable product information
- XML sitemap integration and canonical URLs
- Image alt text
- Social sharing metadata

### 21.2 Website Integration

The catalogue will be integrated into the existing Garrison website navigation (replacing the current mouldings page), using consistent header, footer and branding. The integration method (sub-path, sub-domain or embedded module) will be confirmed after technical discovery of the current website platform.

---

## 22. Security

- Secure administrator authentication with strong password policy
- Role-based access control for all administration functions
- HTTPS for all public and admin traffic
- Input validation and protection against common web vulnerabilities (OWASP Top 10)
- File-upload validation (type, size, content checks)
- Audit logging of administrative changes
- Spam protection on the enquiry form
- Regular backups and controlled restore procedure

---

## 23. Testing & Quality Assurance

| Test type | Scope |
|-----------|-------|
| Functional testing | All functional requirements in Section 18 |
| Data validation | Completeness rules, unit normalisation, duplicate detection on imported records |
| Responsive & browser testing | Desktop, tablet, mobile across supported browsers |
| Performance testing | Listing, search and product page response with representative data volume |
| Security testing | Authentication, authorisation, input and upload validation |
| SEO checks | URLs, metadata, sitemap, canonical tags |
| User Acceptance Testing | Garrison-led UAT with agreed scenarios and sign-off |

Defects are logged, prioritised and resolved before go-live; UAT sign-off is the release gate.

---

## 24. Implementation Methodology

The project follows a phased, iterative approach with Garrison review points at each stage.

| Stage | Key activities | Garrison checkpoint |
|-------|----------------|---------------------|
| Discovery | Requirements confirmation, catalogue analysis, taxonomy draft, product count, hosting review | Discovery sign-off |
| Design | Information architecture, wireframes, visual design | Design approval |
| Build | Framework, admin, catalogue UI, search & filters in iterative sprints | Sprint demos |
| Populate | Data extraction, normalisation and review in parallel with build | Dataset approval |
| Integrate | Website integration and SEO | Staging review |
| Test | QA and UAT | UAT sign-off |
| Launch | Production deployment and handover | Go-live approval |

> **[FIGURE 15 PLACEHOLDER] Delivery Approach — Two Parallel Workstreams**
> **Purpose:** Show that platform development and catalogue population run in parallel and converge at UAT.
> **Diagram type:** Two-track process flow.
> **Must show:** Track A "Platform Development" (Discovery → Design → Build → Integrate); Track B "Catalogue Population" (Source Analysis → Extraction → Normalisation → Garrison Review); both converge into "Test & UAT" → "Go-Live"; Garrison checkpoint icons at each stage.
> **Image generation prompt:** "Two parallel horizontal process tracks merging into one, upper navy track and lower oak-brown track each with four rounded stage boxes, both converging into a combined testing stage and final go-live flag, small checkpoint badge icons above stages, flat clean consulting infographic, white background, 16:9."
> **Format:** 16:9, 1600 × 700 px, PNG · file `fig15-delivery-approach.png`

*Figure 15 — Delivery approach*

---

## 25. Project Timeline

Indicative duration: **10–12 weeks**, subject to the confirmed initial product count and external data volume.

| Phase | Indicative duration | Indicative weeks |
|-------|---------------------|------------------|
| Discovery & catalogue analysis | 1 week | Week 1 |
| UX/UI design | 1–2 weeks | Weeks 2–3 |
| Catalogue framework & data model | 1 week | Week 3–4 |
| Admin & catalogue development | 3 weeks | Weeks 4–6 |
| Search & filtering | 1 week | Week 7 |
| Product & combination experience | 1 week | Week 8 |
| Initial data population (parallel) | 2–4 weeks | Weeks 4–9 |
| Website integration & SEO | 1 week | Week 9 |
| Testing & UAT | 1–2 weeks | Weeks 10–11 |
| Production deployment | 2–3 days | Week 12 |

Software development and catalogue population are scheduled as separate, parallel workstreams so content preparation does not delay platform build.

> **[FIGURE 16 PLACEHOLDER] Project Timeline (Gantt)**
> **Purpose:** Visualise phases, overlaps and milestones over 12 weeks.
> **Diagram type:** Gantt chart.
> **Must show:** X-axis Weeks 1–12; bars per the table above; data population bar in oak brown spanning Weeks 4–9; milestone diamonds at Discovery sign-off (end W1), Design approval (end W3), Dataset approval (end W9), UAT sign-off (end W11), Go-live (W12).
> **Image generation prompt:** "Clean Gantt chart, 12 weekly columns, ten horizontal task bars in navy with one long oak-brown parallel bar for data population, five diamond milestone markers in green along the top, light grid lines, flat minimal project-plan style, white background, 16:9."
> **Format:** 16:9, 1600 × 800 px, PNG · file `fig16-project-timeline.png` (recommended to build in Excel / PowerPoint / MS Project for accuracy)

*Figure 16 — Indicative project timeline*

---

## 26. Deliverables

**Platform**
- Responsive online catalogue integrated with the Garrison website
- Catalogue database and dynamic attribute framework
- Product, category, material, finish and attribute management
- Search and configurable filtering
- Product detail and combination pages
- Related-product management
- Media management
- Administration portal with review and publishing workflow
- External source and provenance management
- Product enquiry capability
- SEO foundation

**Data**
- Existing Garrison catalogue converted into structured records
- Approved additional profiles populated (up to the agreed quantity)
- Categories, attributes and templates configured
- Product relationships and combinations configured
- Source / provenance information captured

**Documentation**
- Technical architecture document
- Catalogue data model document
- Administrator / user guide
- Deployment documentation
- Basic maintenance documentation

---

## 27. Roles & Responsibilities

| Activity | InvenTech | Garrison |
|----------|:---:|:---:|
| Confirm final catalogue scope and product count | Support | **Owner** |
| Provide / approve Garrison product information | Support | **Owner** |
| Confirm naming, taxonomy and classification | Propose | **Approve** |
| Approve external products for inclusion | Propose | **Approve** |
| Confirm third-party content rights / permissions | — | **Owner** |
| Build catalogue framework, admin and data model | **Owner** | Review |
| Configure categories and attributes | **Owner** | Approve |
| Perform agreed initial data population and normalisation | **Owner** | Review |
| Develop search, filters, product pages and responsive UI | **Owner** | Review |
| Provide brand assets | — | **Owner** |
| Provide website and hosting access | — | **Owner** |
| Website integration and deployment | **Owner** | Support |
| Testing | **Owner** | UAT |
| Review and approve populated catalogue | Support | **Owner** |

---

## 28. Assumptions

1. The initial objective is a digital product catalogue, not a transactional e-commerce platform.
2. Garrison will provide access to its existing website and hosting environment.
3. Garrison will approve the final product and category taxonomy.
4. Garrison will approve which external profiles are included.
5. Garrison will confirm rights / permissions for third-party content where required.
6. Product information supplied by Garrison or approved sources will be available in a usable form.
7. The number of initial catalogue products will be finalised during discovery.
8. Initial data population effort will be based on the confirmed product count.
9. Hosting and infrastructure requirements will be finalised after technical discovery.
10. Payment, inventory and ERP functionality are outside the current scope.
11. Content will be prepared in a single language (English) unless otherwise agreed.
12. Garrison will nominate a single point of contact and provide timely reviews and approvals.

---

## 29. Dependencies

| Dependency | Needed by |
|------------|-----------|
| Access to existing website platform and hosting | Discovery (Week 1) |
| Existing catalogue in highest available quality (PDF / source files) | Population start (Week 4) |
| Brand guidelines and assets | Design (Week 2) |
| Confirmed initial product count and external source list | End of Discovery |
| Content-rights confirmation for external material | Before publication of external content |
| Timely Garrison reviews at each checkpoint | Throughout |
| Enquiry routing details (recipients / email) | Build phase |

Delays in dependencies may affect the timeline; any impact will be raised promptly and agreed with Garrison.

---

## 30. Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Large number of external profiles | Population effort and timeline grow | Confirm product count before commercial commitment; per-product rate beyond agreed quantity |
| Third-party content rights | Content cannot be published | Garrison confirms permissions; provenance tracking; Garrison-owned alternatives |
| Inconsistent source data | Poor catalogue quality | Data normalisation rules and unit standards |
| Different dimension models | Rigid, confusing product data | Dynamic attribute framework |
| Future catalogue growth | Performance or redesign needs | Scalable product architecture and search index |
| Poor product data quality | Incomplete product pages | Mandatory / conditional completeness rules |
| Duplicate profiles | Confusing catalogue | Product matching and duplicate validation |
| Unclear categorisation | Inconsistent navigation | Garrison-approved taxonomy at discovery |
| Large images and drawings | Slow pages | Media optimisation and CDN / storage strategy |
| Ongoing maintenance burden | Dependence on developers | Admin-driven catalogue management |

---

## 31. Commercial Proposal

### 31.1 Commercial Structure

To keep the commercial commitment clear and defensible, pricing is separated into fixed platform costs and volume-based content costs.

| # | Component | Basis | Amount |
|---|-----------|-------|--------|
| A | Catalogue Platform Development (UX/UI, frontend, backend, database, admin, search, filters, product & combination management, website integration, testing, deployment) | Fixed price | [Currency] [Amount] |
| B | Initial Catalogue Population — up to **[N]** products | One-time fixed price | [Currency] [Amount] |
| C | Additional product population beyond the agreed quantity | Per product | [Currency] [Amount] / product |
| D | Optional support & maintenance (AMC) | Annual | [Currency] [Amount] / year |

Prices exclude applicable taxes, hosting charges and third-party licence fees unless stated otherwise.

> **[FIGURE 17 PLACEHOLDER] Commercial Model**
> **Purpose:** Explain the four-part commercial structure at a glance.
> **Diagram type:** Stacked building-block illustration.
> **Must show:** Base block "A — Platform Development (fixed)"; next block "B — Initial Population (up to N products)"; smaller expandable block "C — Additional Products (per product)"; optional dashed block "D — Support / AMC (optional)".
> **Image generation prompt:** "Stacked building blocks infographic, solid navy foundation block, oak-brown second block, smaller expandable block with plus icon, top dashed-outline optional block, clean flat style with short labels, white background, 4:3."
> **Format:** 4:3, 1200 × 900 px, PNG · file `fig17-commercial-model.png`

*Figure 17 — Commercial model*

### 31.2 Payment Milestones (proposed)

| Milestone | % of A + B |
|-----------|-----------|
| Project kick-off / signing | [ ]% |
| Design approval | [ ]% |
| UAT readiness | [ ]% |
| Go-live | [ ]% |

### 31.3 Validity

This proposal is valid for **[30 / 60 / 90] days** from the date of issue.

---

## 32. Future Enhancements

The framework is designed to support future capabilities without changing the core architecture. These are **not included** in the current scope unless Garrison requests them:

| Theme | Possible enhancements |
|-------|----------------------|
| Engagement | Enquiry management, quote requests, customer accounts, favourites, project boards |
| Content | Download centre, CAD file downloads, product comparison |
| Commerce | E-commerce, online ordering, inventory availability |
| Integration | CRM integration, ERP integration |
| Intelligence | AI-assisted product discovery and visual profile matching |

> **[FIGURE 18 PLACEHOLDER] Future Roadmap**
> **Purpose:** Show the growth path beyond the initial release.
> **Diagram type:** Roadmap / staircase illustration.
> **Must show:** Step 1 "Launch — Online Moulding Catalogue"; Step 2 "Engage — enquiries, quotes, accounts, favourites"; Step 3 "Enable — CAD downloads, comparison, download centre"; Step 4 "Integrate — CRM, ERP, inventory"; Step 5 "Transact & Intelligent — e-commerce, AI discovery". Label "Current scope = Step 1".
> **Image generation prompt:** "Ascending staircase roadmap infographic with five steps, first step highlighted in oak brown labelled current scope, subsequent steps navy outline with simple icons (catalogue, chat bubble, download/CAD, connected systems, shopping cart with sparkle), flat minimal consulting style, white background, 16:9."
> **Format:** 16:9, 1600 × 800 px, PNG · file `fig18-future-roadmap.png`

*Figure 18 — Future roadmap*

---

## 33. Acceptance Criteria

The project will be accepted when the following are demonstrated in UAT and production:

| Perspective | Criterion |
|-------------|-----------|
| Customer | A visitor can browse, search, filter, view, understand, explore related profiles and submit an enquiry |
| Administrator | An authorised user can create a product, classify it, add technical details, upload drawings, preview and publish |
| Business | Garrison can add new moulding profiles without developers creating pages or modifying the database structure |
| Data | The agreed initial product set is published and meets the data quality rules |
| Technical | The catalogue meets the non-functional requirements and can grow substantially without fundamental redesign |

---

## 34. Conclusion

InvenTech Info Solutions will deliver both a **populated online moulding catalogue for immediate use** and a **reusable catalogue management platform** that enables Garrison Industries to expand and maintain its moulding portfolio independently.

By combining a configurable product framework, structured technical data, controlled publishing, content-rights governance and an SEO-ready customer experience, the solution positions Garrison's catalogue alongside leading industry catalogues while keeping full ownership of its data, design and brand.

We welcome the opportunity to discuss this proposal and to begin discovery at Garrison's convenience.

**Contact**

| | |
|---|---|
| Name | [Name] |
| Designation | [Designation] |
| Email | [email@inventech.example] |
| Phone | [+00 00000 00000] |

---

*InvenTech Info Solutions — Confidential*
