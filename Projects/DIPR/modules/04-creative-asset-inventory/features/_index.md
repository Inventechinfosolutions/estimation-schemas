# Feature Index — Ultra Detailed
## 04 — Creative Asset Inventory

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Line items | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|-----------:|-------|
| F04-001 | Asset upload & metadata | 28 | 28 | 8 | 0 | 16 | 2 | 82 | 18 |  |
| F04-002 | Asset versioning | 22 | 18 | 3 | 0 | 10 | 2 | 55 | 14 |  |
| F04-003 | Outdoor geotagging | 38 | 22 | 4 | 8 | 16 | 4 | 92 | 18 |  |
| F04-004 | Inventory search & filter | 30 | 24 | 5 | 0 | 16 | 2 | 77 | 16 |  |
| F04-005 | Asset access & preview | 22 | 22 | 3 | 0 | 14 | 2 | 63 | 15 |  |

**Module Total:** **369 hours** · **81 artefact line items**

### Module estimation line-item roll-up

| Area | Hours |
|------|------:|
| UI | 140 |
| API | 114 |
| Database | 23 |
| Integration | 8 |
| Testing | 72 |
| Documentation | 12 |

### Ultra-detailed artefact catalogue

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F04-001 | UI | Creative asset upload drop zone with progress | Medium | 6 |
| F04-001 | UI | Asset metadata form (campaign, channel, language) | Medium | 6 |
| F04-001 | UI | File type and size validation messages | Simple | 2 |
| F04-001 | UI | Bulk upload queue panel | Medium | 6 |
| F04-001 | UI | Upload failure retry list | Easy | 4 |
| F04-001 | UI | Asset thumbnail preview strip | Easy | 4 |
| F04-001 | API | Initiate multipart creative upload | Medium | 6 |
| F04-001 | API | Complete upload and persist metadata | Complex | 8 |
| F04-001 | API | List upload job status | Easy | 4 |
| F04-001 | API | Validate MIME type and size limits | Medium | 6 |
| F04-001 | API | Link uploaded asset to campaign | Easy | 4 |
| F04-001 | Database | Asset binary storage pointer | Easy | 2 |
| F04-001 | Database | Asset metadata entity | Medium | 4 |
| F04-001 | Database | Upload job queue record | Easy | 2 |
| F04-001 | Testing | Happy path for image/PDF/video types | Medium | 6 |
| F04-001 | Testing | Oversize and invalid MIME rejected | Medium | 6 |
| F04-001 | Testing | Bulk partial failure recovery | Easy | 4 |
| F04-001 | Documentation | Creative asset upload operator guide | Easy | 2 |
| F04-002 | UI | Asset version history stack panel | Easy | 4 |
| F04-002 | UI | Upload new creative version dialog | Medium | 6 |
| F04-002 | UI | Version compare preview (image/PDF) | Medium | 6 |
| F04-002 | UI | Mark version approved for PoD reference | Easy | 4 |
| F04-002 | UI | Superseded version banner on detail | Simple | 2 |
| F04-002 | API | List asset versions in lineage | Easy | 4 |
| F04-002 | API | Create new version in lineage | Medium | 6 |
| F04-002 | API | Set active approved version for PoD | Easy | 4 |
| F04-002 | API | Stream version binary for preview | Easy | 4 |
| F04-002 | Database | Version chain FK on asset | Easy | 2 |
| F04-002 | Database | Approved-for-PoD version flag | Simple | 1 |
| F04-002 | Testing | Only approved version used in PoD compare | Medium | 6 |
| F04-002 | Testing | Version rollback blocked after PoD link | Easy | 4 |
| F04-002 | Documentation | Creative version policy notes | Easy | 2 |
| F04-003 | UI | Outdoor geotag map picker (site pin drop) | Very High | 16 |
| F04-003 | UI | Manual latitude/longitude fallback form | Medium | 6 |
| F04-003 | UI | District boundary overlay toggle on map | Medium | 6 |
| F04-003 | UI | Geotag accuracy radius slider | Easy | 4 |
| F04-003 | UI | Geotag summary card on asset detail | Easy | 4 |
| F04-003 | UI | Immutable geotag lock indicator after PoD | Simple | 2 |
| F04-003 | API | Save geotag coordinates on outdoor asset | Medium | 6 |
| F04-003 | API | Validate coordinates against district master | Medium | 6 |
| F04-003 | API | Assist reverse geocode for pin placement | Easy | 4 |
| F04-003 | API | Enforce geotag immutability after PoD link | Medium | 6 |
| F04-003 | Integration | Base map tile / GIS provider hook | Easy | 8 |
| F04-003 | Database | Geotag columns on outdoor asset | Easy | 2 |
| F04-003 | Database | District FK validation constraint | Easy | 2 |
| F04-003 | Testing | District mismatch rejection | Medium | 6 |
| F04-003 | Testing | Immutability after PoD submission | Medium | 6 |
| F04-003 | Testing | Map picker pin drag accuracy | Easy | 4 |
| F04-003 | Documentation | Outdoor geotag capture guidelines | Easy | 2 |
| F04-003 | Documentation | UAT outdoor site pin placement script | Easy | 2 |
| F04-004 | UI | Creative asset inventory register with facets | Medium | 6 |
| F04-004 | UI | Advanced filter drawer (campaign, channel, date) | Medium | 6 |
| F04-004 | UI | Saved search preset chips | Easy | 4 |
| F04-004 | UI | Asset quick preview modal | Easy | 4 |
| F04-004 | UI | Export filtered inventory to CSV | Easy | 4 |
| F04-004 | UI | Full-text search box with hit highlights | Medium | 6 |
| F04-004 | API | Search assets with composite filters | Complex | 8 |
| F04-004 | API | Save and load user search preset | Easy | 4 |
| F04-004 | API | Export search result set | Medium | 6 |
| F04-004 | API | Facet counts for filter panels | Medium | 6 |
| F04-004 | Database | Search indexes on asset metadata | Medium | 4 |
| F04-004 | Database | Saved search preset storage | Simple | 1 |
| F04-004 | Testing | Filter combination correctness | Medium | 6 |
| F04-004 | Testing | Export row limit enforcement | Easy | 4 |
| F04-004 | Testing | RBAC hides unauthorized assets | Medium | 6 |
| F04-004 | Documentation | Asset inventory search user tips | Easy | 2 |
| F04-005 | UI | Asset detail preview page (image/PDF/video) | Medium | 6 |
| F04-005 | UI | Role-based download button visibility | Easy | 4 |
| F04-005 | UI | Watermarked preview for vendor users | Medium | 6 |
| F04-005 | UI | Internal share link expiry dialog | Easy | 4 |
| F04-005 | UI | Access denied explanation panel | Simple | 2 |
| F04-005 | API | Get asset with RBAC permission check | Medium | 6 |
| F04-005 | API | Stream preview rendition | Medium | 6 |
| F04-005 | API | Log asset view and download audit | Easy | 4 |
| F04-005 | API | Generate time-limited internal share token | Medium | 6 |
| F04-005 | Database | Asset access audit log | Easy | 2 |
| F04-005 | Database | Share token store | Simple | 1 |
| F04-005 | Testing | Vendor cannot download without entitlement | Medium | 6 |
| F04-005 | Testing | Watermark applied on vendor preview | Easy | 4 |
| F04-005 | Testing | Expired share link denied | Easy | 4 |
| F04-005 | Documentation | Asset access policy summary | Easy | 2 |
