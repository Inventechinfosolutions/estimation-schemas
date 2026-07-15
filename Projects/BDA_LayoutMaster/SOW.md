Scope of Work
Layout Master & Site Management System
Bangalore Development Authority (BDA)
1. Project Overview
The Layout Master & Site Management System is a centralized web-based application designed to digitally manage all BDA layouts, sites, and related land information. The system will serve as the master repository for all layouts and individual sites owned and managed by Bangalore Development Authority.
The application will enable BDA officials to create, maintain, classify, approve, monitor, and manage layouts and sites while ensuring that every property record is available through a single authenticated platform.
The application will also act as the master source for other BDA applications such as Auction Management, Allotment Management, CA Site Management, GIS Systems, and other departmental applications.
2. Objectives
The objectives of the application are to:
Digitize all BDA layout and site records.
Maintain a centralized master repository of layouts and sites.
Eliminate manual registers and duplicate records.
Provide standardized approval workflows for property classification.
Integrate layout and site information with GIS systems.
Provide reliable property information to downstream BDA applications.
Improve transparency, data accuracy, and operational efficiency.
3. Functional Scope
3.1 Layout Management
The application shall provide complete lifecycle management of BDA layouts.
The system shall allow authorized officials to:
Create new layouts.
Update layout information.
View layout details.
Maintain layout boundaries and survey details.
Capture layout location details including State, District, Taluk, Village, Hobli, and BDA Zone.
Capture latitude and longitude coordinates.
Maintain total layout area.
Maintain Block, Sector, Phase, Stage, and Section information.
Upload approved layout plans and supporting documents.
Upload layout photographs.
Maintain layout status.
Archive layouts where applicable.
Each layout shall become the parent entity for all sites created within that layout.
3.2 Site Management
The application shall provide complete management of all individual sites belonging to a layout.
The system shall support:
Creation of sites.
Modification of site information.
Site cancellation where applicable.
Viewing complete site details.
Site numbering.
Site dimensions.
Site area calculations.
Corner and intermediate site identification.
Road facing details.
Khata information.
Survey numbers.
Reservation information.
Legal status.
Litigation information.
Site ownership status.
Supporting documents.
Site photographs.
Every site shall always belong to a registered layout.
3.3 Site Classification Management
The application shall serve as the master classification system for all BDA sites.
Each site may be classified into one or more categories based on departmental requirements.
Examples include:
Residential Site
Commercial Site
Civic Amenity (CA) Site
Auction Site
Land Loser Site
Corner Site
Intermediate Site
Park
Civic Infrastructure
Utility Site
Public Purpose Site
Government Reserved Site
Future Development Site
Other categories defined by BDA.
Classification shall determine the business process applicable to the site and the downstream applications that can access the property.
3.4 Site Classification Approval Workflow
Site classification shall not become effective immediately after creation.
Whenever a site is marked under a special category such as:
Auction Site
Land Loser Site
CA Site
Commercial Property
Public Utility Site
Reserved Site
Any department-specific category
the classification shall undergo an approval workflow.
The workflow shall:
Route the request to the concerned BDA department.
Allow department officials to verify the site details.
Approve or reject the proposed classification.
Record remarks during each approval stage.
Maintain complete approval history.
Record date, time, and approving authority.
Only after successful approval shall the site become available for use by the respective business process.
3.5 Department-wise Workflow
The application shall support configurable approval workflows for different site classifications.
Each site category may have its own approval hierarchy as defined by BDA.
Examples include:
Engineering Section
Land Acquisition Section
Auction Section
Revenue Section
Legal Section
CA Site Section
Town Planning Section
Commissioner Office
Workflow levels, approvers, and approval conditions shall be configurable based on departmental requirements.
3.6 Auction Integration
The Layout Master application shall act as the master source for the Auction Management System.
The auction process itself is outside the scope of this application.
The application shall:
Allow officials to identify sites proposed for auction.
Route the proposal through the required approval workflow.
Mark the site as "Approved for Auction" after successful approval.
Publish only approved auction sites for downstream integration.
The Auction Management System shall consume only those sites that have been officially approved for auction.
Sites not approved through the Layout Master application shall not be available for auction.
Any changes to auction-approved sites shall automatically be reflected in downstream applications.
3.7 Land Loser Management
The application shall support identification of Land Loser sites.
The workflow shall include:
Marking a site as Land Loser.
Department verification.
Approval workflow.
Recording supporting documents.
Maintaining Land Loser reference information.
Publishing approved Land Loser sites for downstream applications.
3.8 CA Site Integration
The application shall maintain Civic Amenity (CA) sites as part of the master property repository.
Only sites approved as CA Sites shall be available for the CA Site Management application.
The application shall maintain synchronization between Layout Master and the CA Site Management System.
3.9 GIS Integration
The application shall integrate with the BDA GIS platform for spatial information management.
The integration shall support:
Retrieval of layout boundaries from the GIS server.
Retrieval of site polygons from the GIS server.
Retrieval of spatial attributes.
Display of GIS information within the application.
Synchronization of GIS updates.
Whenever a layout or site is created or modified within the GIS platform, the corresponding records shall be synchronized with the Layout Master application.
Similarly, whenever layouts or sites are created or updated within the Layout Master application, the GIS platform shall also be updated to ensure consistency across both systems.
The synchronization mechanism shall ensure that spatial and non-spatial information remains consistent between both systems.
3.10 GeoServer Integration
The application shall integrate with the BDA GeoServer for maintaining geospatial data.
The integration shall include:
Fetching layout geometry from GeoServer.
Fetching site geometry from GeoServer.
Updating newly created layouts to GeoServer.
Updating newly created sites to GeoServer.
Updating geometry modifications.
Synchronizing attribute changes.
Handling synchronization failures through retry or exception mechanisms.
Maintaining synchronization logs for audit purposes.
The Layout Master application and GeoServer shall remain synchronized to ensure accurate geospatial representation.
3.11 Master Data Management
The application shall provide centralized master data management for:
Countries
States
Districts
Taluks
Villages
Hoblis
BDA Zones
Sections
Site Categories
Reservation Categories
Road Facing
Property Status
Layout Status
Workflow Masters
Department Masters
These masters shall be configurable by authorized administrators.
3.12 Document Management
The application shall provide centralized document management for layouts and sites.
Supported documents include:
Approved Layout Plans
Survey Sketches
Government Orders
Acquisition Documents
Court Orders
Khata Documents
Site Sketches
Classification Approval Documents
GIS Reference Documents
Supporting Certificates
All uploaded documents shall be securely stored and linked to the corresponding layout or site.
3.13 Dashboard & Reporting
The application shall provide dashboards for monitoring layouts and sites across the organization.
The dashboards shall include:
Total Layouts
Total Sites
Layout-wise Site Count
Zone-wise Layout Distribution
Category-wise Site Distribution
Auction Site Summary
CA Site Summary
Land Loser Site Summary
Commercial Site Summary
Residential Site Summary
Reserved Site Summary
Department-wise Pending Approvals
Approval Status Summary
GIS Synchronization Status
Recently Updated Layouts
Recently Updated Sites
The application shall also generate operational and management reports for decision-making.
3.14 Search & Data Retrieval
The application shall provide comprehensive search capabilities for locating layouts and sites using multiple search parameters, including:
Layout Name
Layout Code
Site Number
Survey Number
Zone
District
Taluk
Village
Block
Sector
Phase
Stage
Site Category
Auction Status
CA Site Status
Land Loser Status
Approval Status
GIS Availability
Property Status
3.15 Integration with Other BDA Applications
The Layout Master application shall function as the authoritative master repository for property information and provide validated layout and site data to other BDA applications through secure integration mechanisms.
The application shall support integration with systems such as:
Auction Management System
CA Site Management System
GIS / GeoServer
Any future BDA departmental applications
Only approved and validated layout and site records shall be made available for consumption by downstream applications, ensuring data consistency and eliminating duplicate property records across the BDA ecosystem.
 