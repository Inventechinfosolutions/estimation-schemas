# Annexure – 01

# Main Module: SPLOCA Geo Tagging & Valuation of Immovable Assets (eValueI)

**Functional Requirement Specification for Geo Tagging Immovable Asset Valuation**

**Source:** `Main module 1.pdf` (27 pages; scanned printout transcribed)

---

## Functional Requirement Specification

| Sl.no | Module Name | Features | Requirements |
|------:|-------------|----------|--------------|
| 1 | User – Admin | Provision to create an Assets data by the office user through Web Application | The system should allow office user to login with User name and password. The Application should allow the office user to enter basic details (Office user ID, User Name, Designation, Mobile Number, Allotted FE name, FE Code, CA name and CA Code, Asset Description, Asset Location, Latitude & Longitude, Date of Attachment, Date of Absolute, Court Order, IO Valuation, Section 7(1) Valuation, Guidance / Market Value) |
| 2 | Valuer Details | Provision to create Approved Valuer data through Web Application | **1.** The Application should allow the office user to enter basic details (Office user ID, User Name, Designation, Mobile Number, Approved Valuer name, Valuer Code, Category, Order Number, Rates of Valuation & Incidental Costs, Assignment Number, Assignment Date, Assigned Property Details)<br>**2.** The Application should allow the Valuer user to enter basic details (User ID, User Name, Designation, Mobile Number, Valuer Code, Assignment Number, Valuer Names Allotted, Mobile Numbers, Date of Visit, Stage of Valuation) |
| 3 | Asset Details | The System make provision to register of Assets and valuers’ details using web application from office user login. | The system should allow office user to create Assets basic details (ID, Asset Name, Type, Asset details, Address, Boundaries (As per Document – North, South, East, West), Asset Measure, Asset Registration Date, Parties and Value Stamp Duty Paid & Registration Fee, FE Code, CA Code, Court Order number, Court Order details (provision to upload), Sale deeds Details (provision to upload), Category of Asset (Land, Property, Building, Lease Holding, Other) |
| 3 / Data Capturing – I | Data Capturing – I (Mined Data) | The App makes provisions to VALUER to mine data from web application, down load data from secure sources, enter the asset valuation details with Photo with GIS tagging, and video upload on a real-time basis. While selecting the asset by the valuer, the basic details about the asset entered by office user must be displayed on the page; later, the remaining valued data will be entered by the assigned valuer in another API based on the Valuation Method adopted. Make provisions to capture the valuer real-time GIS data with system date and time. | The App should allow Asset valuer to select the Assets which is already created and assigned by the office user using drop down.<br><br>**Preliminary Site Inspection Report**<br>**a.** First, Selecting the Asset name from drop down.<br>**b.** Once selected, basic details like **Asset Name, Details, Address, Asset Measure, Asset Registration number** are displayed.<br>&nbsp;&nbsp;&nbsp;&nbsp;**i.** The Sale deeds and court order uploaded file has to see when valuer click view button.<br>**c.** Asset is identified along with CA Name, Designation, Mobile Number and Office Address and FE Name & Code.<br>**d.** Location of Asset (Asset no, Address, width of approach road, type of road, landmark, surrounding area, **Boundaries (North, South, East and West)**)<br>**e.** School/ College, Hospital, Malls, Temples/ Mosque /Church, Police station, and Transportation facilities (Bus stand, Railway station, Airport) near location distance needs to be fetched automatically in the application.<br>**f.** Google Map link & QR Code of the link<br>**g.** Enable mobile app to capture photos (minimum 4 each at least 5mb) with GIS tag (API Geocoding). *(Handwritten note: with date on the photo)*<br>**h.** Upload Photo / Video<br>**i.** Captured Date and Time<br>**j.** Any negative factors which affect the property<br>**k.** Overall Observation by Valuer (Remarks) |
| 4 | Data Capturing – II (Analytical Data) | APIs of Valuation Methods | **a.** Select and Open Application<br>**b.** Select Valuation Format<br>**c.** Select Valuation Method<br>**d.** Enter Code to populate basic data of asset in the application<br>**e.** Enter data<br>**f.** Upload Pictures / Videos into Library |
| 5 | MIS reports and Admin | The system shall make provision to generate the report based on the valuation details entered by valuer. Make provision to create, update or delete the valuer/asset/officer user login credentials in the web application. | **a.** Select and Open Application<br>**b.** Select Valuation Report Format<br>**c.** Enter Code to populate basic data of asset in the application<br>**d.** Enter report<br>**e.** Tag Videos & Photos |
| 6 | CA Report on Valuation Report & Valuer Assessment | The system shall make provision to evaluate the Valuer Report on key parameters – Time Taken, Asset Category, Method Adopted, Adjustment Factors used, Section 7(1) Valuation, Guidance Value | **a.** Select and Open Application<br>**b.** Select Valuation Report<br>**c.** Enter CA Code to populate basic data of asset in the application<br>**d.** Enter report<br>**e.** Select Photos for display in Auction<br>**f.** Accept / Reject / Order Revaluation / Issue SCN to Penalize Valuer |
| 7 | Valuer Billing | The System shall prepare bill and voucher | **a.** Select and Open Application<br>**b.** Enter Valuer Code to populate basic data of Valuer<br>**c.** Select Valuation Report<br>**d.** Open CA Report<br>**e.** Open Billing Window (If CA has accepted)<br>**f.** Enter details<br>**g.** Submit Bill online & upload signed hard copy |

---

## Software

Shall use **PHP** and a secure **Geocoding API** with:

1. **Geocoding** — Converts addresses into latitude and longitude coordinates or Place IDs that can be used to place markers on a map  
2. **Reverse geocoding** — Converts latitude/longitude coordinates or a Place ID into a human-readable address  

The return should be in **XML** or another compatible format in host PC / Android.

---

## Valuation Formats

### I. Cost of Construction Method

#### A. Accounts Method

1. Report of Materials Costs  
2. Report of Labour Costs  
3. Date of Construction Start & Completion  
4. Depreciation (Using Certified CLASSIFICATION OF STRUCTURES BASED ON SPECIFICATION WITH EXPECTED ECONOMIC LIFE AND RESIDUAL OR RESERVE VALUE OR SCRAP VALUE)  
5. Likely Market Value  
6. Certificate of all Accounts & Vouchers produced  

#### B. Comparable method – For built up properties

**(a) (Flats/Shops/Offices) In Apartments And Multi Storied Buildings:**

| Sr. No. | Description of property | Built up Area in Sqm. | Date of Sale / Transfer | Area of the Plot | FSI/FAR of the plot | Land appurtenant to Flat | Apparent consideration | Name of seller / purchaser | Register No. |
|--------:|-------------------------|-----------------------|-------------------------|------------------|---------------------|--------------------------|------------------------|----------------------------|--------------|
| | | | | | | | | | |

**(b) Sale Instances For Built Up Properties: Adjustment factors –**

1. Location  
2. Situation  
3. Area  
4. Floor Difference  
5. Specifications  
6. Facilities / Services  
7. Time-gap  
8. Status (Lease or Freehold)  
9. Area of the Building  
10. Floor disposition  

**(c) Floor Disposition**

### II. Fair Market Value of Residential flat / commercial premises

**Weightage for floor disposition:**

| Floor | Weightage |
|-------|-----------|
| **a) Basement** – Used for storage purpose | 0.50A |
| **a) Basement** – Used otherwise | 0.75A to 0.90A |
| **b) Ground floor / 1st & Mezzanine floors** | A |
| **c) 2nd to 5th floor** | 0.95A |
| **d) 6th to 9th floor** | 0.90A |
| **e) 9th floor and above** | 0.85A |

**A** is the average unit cost of a flat.

*Note: In metropolitan cities like Mumbai/ Bangalore, the position is quite reverse in case of flats and multistoried buildings as the rates of upper floors go on increasing as compared to rate of G.F. and F.F. rates. The floors above G. floor and Pent houses fetch the most. Hence above factor should be carefully decided keeping in view the local trends and situations.*

### A. Land and Building Method

Applicable where:

**(a)** Self-occupied property.  
**(b)** Partly self-occupied (i.e., more than 60%) and balance tenanted.  
**(c)** Not possible to obtain fair and maintainable rent.  
**(d)** No direct evidence of rent such as schools and hospitals etc.  
**(e)** Property is not fully developed, or the return from the property is not commercial.

#### i. Land Value: (Derived)

#### ii. Identification of Comparable Sales

**1. Order of preference:**

**(a)** Sale of the adjacent land.  
**(b)** Sale of the land in the same locality.  
**(c)** Sale of the land in the neighborhood or adjoining localities.  
**(d)** Guideline rates issued by Local Authorities for land & construction.

**2. Factors affecting the land value:**

i) Size, ii) Shape, iii) Frontage, iv) Locality and surroundings, v) Amenities and facilities, vi) FAR or FSI, vii) Connectivity, viii) Road width.

**3. Number of sale instances:** Min 3

#### iii. Factors of Adjustment / Influence

**(a) Location & Situation:**

1. Development and the situation of the property in commercial or residential zones – **+/- 5%**  
2. Nearness to roads / proximity to civic amenities & transport facilities: **+/- 5%**  
3. Corner plots: **+/- 5%**

**(b) Time-gap: NPV of Past Sale Instances**

If no such sale instances are available then the price rise should be considered **18 to 24% P.A.**

**(c) Shape:** Adjustment factor **+/- 5%** depending upon the irregularity in shape and frontage of the plot & Vaastu

**(d) Size:** For large size plots **+/- 0.5% per 100 Sqm.**

**(e) FAR:** In case if sale instances of same or next above/below FAR are not available the adjustment in rates for FAR/ FSI should be made as under:

| FAR/FSI | Rate |
|---------|------|
| Additional 0.5 | 40% of basic rate |
| Next 0.5 | 35% |
| Next 0.5 | 30% |
| Next 0.5 | 25% |
| Next 0.1 | 45% |

**(f) Side Open:** Adjustment of **+5%** for each additional open side or vice-versa

**(g) Co-ownership Undivided Share, Rights & Interest:** Discount **5% to 12.5%** depending upon the Number of Co-owners and their relationship can be given.

**(h) Land Tenure:** Adjustment factor of **+/- 0.25%** for working out the land rate of free hold plot from the sale instance of lease hold plot and vice-versa.

**(i) Encumbrance / Civil Dispute / Lack of Approved Layout Plan / Encroachment:** Land value for the portion encumbered may be deferred for reasonable period to allow for depressing effect to the extent of **30%**.

**(j) Unearned increase:** If the property under valuation happens to be a lease hold plot then a certain percentage, as specified in the lease deed of unearned increase (current market rate less premium paid) is also to be deducted from the land value.

#### iv. Other Factors

Other factors effecting the price of property such as defect in title, mode of payment etc. (**Depressing Effect of 10%**)

#### v. Cost of Building

**FMV – Valuation Date – Cost of Reproduction minus the depreciation from the Date of Completion to Date of Valuation.**

#### vi. Depreciation

##### Calculation of Future life of a Building (Lf)

**i) Factors determining future life**

1. Date of commencement of construction  
2. Date of completion of construction  
3. Type and technique of construction  
4. Type and quality of construction materials  
5. Quality of workmanship  
6. Environment in which a building is situated  
7. Climatic conditions of the place  
8. Nature of past use and likely nature of future use  
9. Extent and quality of repair and maintenance  
10. Present physical condition, especially structural components and future repairability  
11. Obsolescence / Dilapidation  

**ii) Formula for Equivalent spent life (Le)**

The equivalent spent life (**Le**) of a building is the total life of the building (**L**) minus the assessed future life of the building (**Lf**).

**Le = L − Lf**

##### A. Straight Line Method

**Depreciation per annum = (Cost of reproduction − Salvage value) / Life of the building**

Assumption: Salvage value is typically taken as **10%** of the cost of reproduction.

**Depreciation per annum = 0.90 × Cost of reproduction / Life of the building**

##### Value of a property by the Land and Building Method

1. **Value of land** = A  
2. **Value of building:**  
   - 2.1 Reproduction cost of the building based on PWD-PAR = **B**  
   - 2.2 Amount of depreciation = (−) **C**  
   - 2.3 Builder’s efforts @ **3%** of B = **D**  
   - 2.4 Value of building **(B − C + D)** = **E**  
3. **Value of the property** = **A + E**

##### Quantum of Depreciation Formula

The Straight Line Method is often adopted for its simplicity in estimating depreciation.

**Q = (1 − p) × R × Le / I**

Where:

- **Q** = Quantum of depreciation  
- **R** = Reproduction cost of the building in Rupees  
- **p** = Percentage considered for estimating salvage value  
- **Le** = Equivalent spent life of the building in years  
- **I** = Life of the building in years  

With **p = 10%**: **Q = 0.9 × R × Le / I**

---

## Reporting Formats

### PROFORMA FOR RECORDING DETAILS OF SPECIFICATIONS OF THE PROPERTY

| Sl. No. | Details of Specification | Non Residential | Residential |
|--------:|--------------------------|-----------------|-------------|
| **1** | **FOUNDATION** | | |
| 1.1 | Type spread foundation/isolated/raft foundation / pile foundation (in case of pile foundation number of diameter and depth of pile be given). | | |
| 1.2 | Depth | | |
| **2** | **SUPERSTRUCTURE** | | |
| 2.1 | RCC framed construction / Load bearing | | |
| 2.2 | No. of Storeys | | |
| 2.3 | Internal & External Walls | | |
| 2.4 | Plinth height | | |
| 2.5 | Floor Height | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| | Door & Windows | | |
| **3** | **FITTINGS & FIXTURES** | | |
| 3.1 | Frames : Doors/Windows | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 3.2 | Shutters : Doors/Windows | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 3.3 | M.S. Grills Plain/Ornamental | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 3.4 | Fitting | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| **4** | **FLOORING** | | |
| 4.1 | Types of Flooring : | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 4.2 | Dado | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| **5** | **ROOFING** | | |
| **6** | **FINISHING** | | |
| 6.1 | Internal Walls | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 6.2 | External walls | | |
| **7** | **Sanitary & Water Supply installation (Details as per measurement recorded)** | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| **8** | **Electrical Installation (Details as per measurement recorded)** | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| **9** | **External Services** | | |
| 9.1 | Sewer connected to municipal sewer line/septic tank | | |
| 9.2 | Water Supply independent arrangement with tube well / mpl. Supply. | | |
| 9.3 | Overhead Tank | | |
| 9.4 | Underground sump well | | |
| 9.5 | No. of pumps | | |
| 9.6 | Storm water drain | | |
| 9.7 | Horticulture | | |
| 9.8 | Compound lighting | | |
| **10** | **FACILITIES** | | |
| 10.1 a) | Passenger lift …………….. No. for …………….. person | | |
| 10.1 b) | Service Lift …………….. No. for …………….. Kg. | | |
| 10.2 | Generator …………….. No. of ……….. KVA | | |
| 10.3 | Pavement / Road & Path | | |
| 10.4 | Compound wall & gate | | |
| **11** | **Special Items** | | |
| 11.1 | Dry/Wet Riser | | |
| 11.2 | Fire protection system | | |
| 11.3 | Central air conditioning | | |
| 11.4 | Sound System | | |
| 11.5 | T.V. Antenna/ Dish / DTH | | |
| 11.6 | Lightning Conductor | | |
| 11.7 | Telephone Connection | | |

---

## SPLOCA VALUATION FORM V-1

**Report of Valuation of immovable property (other than agricultural lands, plantations, forests,) mines and quarries**

| Field | Value |
|-------|-------|
| Name of registered valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

### General

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner/owners  
4. If under joint ownership/co-ownership, share of each such owner. Divided / undivided?  
5. Brief description of the property  
6. Location, Street, Ward No.  
7. Survey/Plot No. of land  
8. Zone: Green Belt / Residential / Commercial / Mixed area / Industrial?  
9. Classification of locality: HIG / MIG / LIG  

10. **Proximity to civic amenities:**

| Amenity | Schools / Colleges | Hospitals | Offices | Markets | Cinemas / Malls |
|---------|--------------------|-----------|---------|---------|-----------------|
| Proximate (KM) | | | | | |

11. **Means and proximity to surface transport by which the locality is served:**

| Means of Transport | Public Transport | Auto / Taxi | Rail Station | Metro |
|--------------------|------------------|-------------|--------------|-------|
| Proximate (KM) | | | | |

### Land

12. **Area of land, shape, dimensions and physical features with documentary proof**

| Land Document | Shape | Side 1 (Mtr) | Side 2 (Mtr) | Side 3 (Mtr) | Side 4 (Mtr) | Area (Sq Mtr) | Surface |
|---------------|-------|--------------|--------------|--------------|--------------|---------------|---------|
| | | | | | | | |

13. **Roads, streets or lanes on which the land is abutting**

| Abutting Road | Major | Minor | Cross Road | Lane |
|---------------|-------|-------|------------|------|
| Name | | | | |
| Length | | | | |

14. Freehold or Leasehold?  

15. If leasehold, the name of lessor/lessee, nature of lease, dates of commencement and termination of lease and terms of renewal of lease:  
   - (i) Initial premium  
   - (ii) Ground rent payable per annum  
   - (iii) Unearned increase payable to the lessor in the event of sale or transfer  

16. Any restrictive covenant to use of land? If so, upload copy.  

17. Any agreements of easements? If so, upload Copies  

18. Approved Town Planning Scheme or any Development Plan of Government or any statutory body? If so, upload Particulars  

19. Any contribution towards development or is any demand for contribution outstanding?  

20. Whole or part of the land notified for acquisition by Government or any statutory body? Give date and number of the notification  

21. Upload a dimensioned site plan  

### Building Particulars

21. *(Duplicate numbering in source)* Any plans and elevations of structures standing or lay-out plan? Upload  

23. Technical details of the building: **[Use Annexure to this Form]**  

24. (i) Owner-occupied / tenanted / both?  
    (ii) Specify portion and extent under owner-occupation  

25. What is the Floor Space Index permissible and percentage actually utilized?

| FSI Permissible | FSI Utilized | Violation |
|-----------------|--------------|-----------|
| | | |

26. **Rents**

| Sl No | (i) Names of tenants/ lessees/ licensees | (ii) Portions in their occupation | (iii) Monthly or annual rent/ compensation / license fee / Maintenance | (iv) Payment for Furniture / Fittings | Relationship to Owner | Total Receipts from Property |
|------:|------------------------------------------|-----------------------------------|------------------------------------------------------------------------|---------------------------------------|-----------------------|------------------------------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

27. Occupants related to, or close business associates of, the owner:  

28. **Water and electricity charges borne by:**

| | Owner Share | Lessee Share |
|--|-------------|--------------|
| Water Charges Monthly | | |
| Electricity Charges Monthly | | |

29. **Cost of repairs and maintenance borne by:**

| | Owner Share | Lessee Share |
|--|-------------|--------------|
| Annual Repairs | | |
| Common Area Maintenance & Security (including Lift, Pump) | | |

30. **Statutory Dues**

| | Owner Share | Lessee Share |
|--|-------------|--------------|
| Property Tax Annual | | |
| Insurance | | |

31. Any dispute between landlord and tenant pending in a court of law:  

### Sales

32. **Sales instances in the locality**

| Sl No | Name & Address of Property | Registration Number | Date of Sale | Area Sold | Sale Price |
|------:|----------------------------|---------------------|--------------|-----------|------------|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

33. Land rate adopted in this valuation:  

34. Basis of arriving at the land rate in absence of Sale Instances  

### Cost of Construction

35. **Construction Period**

| Commencement of construction | Completion of Construction |
|------------------------------|----------------------------|
| | |

36. Method of construction — by contract/by employing labour directly/both?  

37. Upload Contract, Agreements if available  

38. For items of work done by engaging labour directly, give basic rates of materials and labour supported by documentary proof  

### Part II – Valuation

Approach to valuation of the property and indicate how the value has been arrived at, supported by necessary calculations.

### Part III – Declaration

I hereby declare that —

**(a)** the information furnished in Part I is true and correct to the best of my knowledge and belief;  
**(b)** I have no direct or indirect interest in the property valued;  
**(c)** I have personally inspected the property on ________  

| | |
|--|--|
| Date: | Place: |
| Name & Digital Signature of Registered Valuer: | |
| Name & Digital Signature of Expert Valuer (if any): | |

---

### SUB-ANNEXURE TO FORM V-1

| Sl. No. | Technical details | Main building | Annexe | Servants' quarters | Garages | Pump house |
|--------:|-------------------|---------------|--------|--------------------|---------|------------|
| 1. | No. of floors and height of each floor | | | | | |
| 2. | Plinth area floor-wise (As per IS : 3861-1966) | | | | | |
| 3 | Year of construction | | | | | |
| 4 | Estimated future life | | | | | |
| 5 | Type of construction load bearing walls/RCC frame/steel frame | | | | | |
| 6 | Type of foundations | | | | | |
| 7 | **Walls** | | | | | |
| | (a) Basement and plinth | | | | | |
| | (b) Ground floor | | | | | |
| | (c) Superstructure above ground floor | | | | | |
| 8 | **Partitions** | | | | | |
| | Doors and windows (Floor-wise). | | | | | |
| | (a) Ground floor | | | | | |
| | (b) 1st floor | | | | | |
| | (c) 2nd floor, etc. | | | | | |
| 10 | **Flooring (Floor-wise).** *(Sl. No. 9 not present in source)* | | | | | |
| | (a) Ground floor | | | | | |
| | (b) 1st floor | | | | | |
| | (c) 2nd floor, etc | | | | | |
| 11 | **Finishing (Floor-wise).** | | | | | |
| | (a) Ground floor | | | | | |
| | (b) 1st floor | | | | | |
| | (c) 2nd floor, etc. | | | | | |
| 12 | Roofing and terracing | | | | | |
| 13 | Special architectural or decorative features, if any | | | | | |
| 14 | (i) Internal wiring surface or conduit | | | | | |
| | (ii) Class of fittings : Superior/ordinary/poor | | | | | |
| 15 | **Sanitary installations.** | | | | | |
| | (a) (i) No. of water closets | | | | | |
| | (ii) No. of lavatory basins | | | | | |
| | (iii) No. of urinals | | | | | |
| | (iv) No. of sinks | | | | | |
| | (v) No. of bath tubs | | | | | |
| | (vi) No. of bidets | | | | | |
| | (vii) No. of geysers | | | | | |
| | (b) Class of fittings : Superior Coloured /superior white/ ordinary | | | | | |
| 16 | **Compound wall.** | | | | | |
| | (i) Height and length | | | | | |
| | (ii) Type of construction | | | | | |
| 17 | No. of lifts and capacity | | | | | |
| 18 | Underground Pump – Capacity and type of construction | | | | | |
| 19 | **Overhead tank :** | | | | | |
| | (i) Where located | | | | | |
| | (ii) Capacity | | | | | |
| | (iii) Type of construction | | | | | |
| 20 | Pumps – No. and their horse power | | | | | |
| 21 | Roads and pavings within the compound, approximate area and type of paving | | | | | |
| 22 | Sewage disposal whether connected to public sewers. If septic tanks provided, No. and capacity | | | | | |

---

## SPLOCA VALUATION FORM V-2

**Report of valuation for agricultural lands other than forests & commercial plantations**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose for which valuation is made  
2. Date as on which valuation is made  
3. Name of the owner/owners of agricultural land  
4. If the agricultural land is under joint ownership/co-ownership, share of each owner: Are the share undivided?  
5. Particulars of agricultural land :

| Sl. No. | Survey No.(s) of land(s) | Village, tehsil and district in which situated | Area of the land (in hectares) | Classification of land(s) as given in the land revenue records etc. | Crops grown during the year | Annual land revenue, if any |
|--------:|--------------------------|------------------------------------------------|--------------------------------|-----------------------------------------------------------------|-----------------------------|-----------------------------|
| | | | | | | |

6. Does the land fall in an area included in any Town Planning Scheme or any Development Plan of Government or any statutory body? If so, upload order  

7. **Special features of the land**

| Soil Type | Quality and fertility | Mode of Irrigation (i.e., whether by wells, electric tube-wells or tube-wells or canal) | Distance from village/ town /markets | Approach roads | Means of transportation | Cultivated by self or tenants. Any other features |
|-----------|----------------------|------------------------------------------------------------------------------------------|--------------------------------------|----------------|-------------------------|---------------------------------------------------|
| | | | | | | |

8. **Comparable case of the sale relied upon :**  
   - **(a)** Type of Property  
   - **(b)** Distance of Locality of Sale  
   - **(c)** Date of Transaction  
   - **(d)** Sale Price and Unit value  

9. **Unit value adopted :** Valuer should discuss in details his approach to valuation of the land and indicate how the value has been arrived at  

10. Value of land(s)  

11. **Declaration:** I hereby declare that—  
    - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
    - **(b)** I have no direct or indirect interest in the land valued;  
    - **(c)** I have personally inspected the land(s) and I have examined the revenue records of village/tehsil  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer | |
| Name & Signature of Expert Valuer (if any) | |

---

## SPLOCA VALUATION FORM V-3

**Report of valuation of forests & plantations**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner(s) of the forest / plantation  
4. If the forest is under joint ownership/co-ownership, share of each owner: Are the share undivided?  
5. Location of the forest / plantation  
6. Area of forest/ plantation (in hectares)  
7. **Valuation of the forest** *(the valuation should be made indicating in detail the different factors which have been taken into account, such as the kind of timber the density of the forest mode of transportation of timber, etc.)*

| Land Location | Area in Hectares | Sale Instance Locality | Sale Instance Outside Locality | Sale Value | Market Value of Land |
|---------------|------------------|------------------------|--------------------------------|------------|----------------------|
| | | | | | |

| Tree Type | Number | Average Age | Value | Availability of Transportation Route | Commercial Value of Trees |
|-----------|--------|-------------|-------|--------------------------------------|---------------------------|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

8. **Declaration:** I hereby declare that—  
   - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
   - **(b)** I have no direct or indirect interest in the forest valued;  
   - **(c)** I have personally inspected the forest and I have examined the revenue records of village/tehsil/district  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer | |
| Name & Signature of Expert Valuer (if any) | |

---

## SPLOCA VALUATION FORM V-4

**Report of valuation of mines and quarries**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner/owner(s)/Lease holder of the mine(s)/quarry(ies)  
4. If joint ownership/co-ownership / joint lease, share of each: Are the share undivided?

| | Joint Owner / Lessee 1 | Joint Owner / Lessee 2 | ADD Joint Owner / Lessee 3 |
|--|------------------------|------------------------|----------------------------|
| Share | | | |
| Divided / Undivided | | | |

5. The name and location of the mine(s)/quarry(ies)  
6. Area of mine(s)/quarry(ies)  
7. **Valuation of the mine(s)/quarry(ies) excluding machinery, plant, buildings and furniture and fittings** *(the valuer should discuss in details the factors which have been taken into account including the average annual output during the past three years, the extractable reserves, the area available for extraction, the thickness of the seam, the stage of development, depillaring, Geological disturbances, etc.)*  

8. **Declaration:** I hereby declare that—  
   - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
   - **(b)** I have no direct or indirect interest in mine(s)/quarry(ies) valued;  
   - **(c)** I have personally inspected the mine(s)/quarry(ies) and I have examined the revenue records of village/ tehsil /district  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer | |
| Name & Signature of Expert Valuer (if any) | |

---

## Additional Module: QR Coding and Valuation of Movables (eValueM)

### Categorization and Tagging of Movables

#### 1. Coding

| Sl | Item Category | Code & Sub Code | Object Code | Detail Code |
|----|---------------|-----------------|-------------|-------------|
| i. | **Air Conditioners:** | **AC** | | |
| | - Split | -SPL | | |
| | - Window | -WIN | | |
| ii. | **Computers & Peripherals:** | **PCP** | | |
| | - Desktop | -DT | | |
| | - Laptop | -LT | | |
| | - IPAD | -IPD | | |
| | -- Peripherals | | --P | |
| | --- Keyboard | | | ---KB |
| | --- Mouse | | | ---MUS |
| | - Printer | -PR | | |
| | -- Multifunction | | --MF | |
| | -- Large Format | | --LF | |
| | - Copier | -CP | | |
| | - Scanner | -SCN | | |
| | - Storage Drive | -STR | | |
| iii. | **Electrical & Electronic Goods:** | **EEG** | | |
| | - TV | -TV | | |
| | -- LCD | | --LCD | |
| | -- LED | | --LED | |
| | - CD/ DVD Player | -PLR | --CD/--DVD | |
| | - Mobile Phone | -MBL | | |
| | -- Android | | --AND | |
| | -- Apple | | --APL | |
| | - Domestic | -DOM | | |
| | -- Refrigerator | | --FRG | |
| | -- Microwave | | --MWV | |
| | -- Heater | | --HTR | |
| | -- Washing Machine | | --WSH | |
| | -- Vacuum Cleaner | | --VCM | |
| | -- UPS | | --UPS | |
| | -- Light Fittings | | --LGT | |
| | -- Fan Fittings | | --FAN | |
| | - Commercial | -COMM | | |
| | -- Calculator | | --CAL | |
| | -- POS Terminal | | --POS | |
| | -- Testing Equipment | | --TST | |
| iv. | **Furniture & Fixtures:** | **FF** | | |
| | - Sofa | -SF | | |
| | - Chair | -CHR | | |
| | - Table | -TBL | | |
| | - Storage | -STR | | |
| v. | **Machinery, Tools & Plant:** | **MTP** | | |
| | - Kitchen | -KCN | | |
| | -- Stove | | --STV | |
| | -- Utensils (Preparation) | | --UTPR | |
| | -- Utensils (Cooking) | | --UTCK | |
| | -- Utensils (Serving) | | --UTSRV | |
| | - Living | -LIV | | |
| | -- Gym | | --GYM | |
| | -- Other(Specify) | | --OTH | |
| | - Garden | -GDN | | |
| | -- Tools | | --TL | |
| | -- Machinery | | --MCN | |
| | - Factory | -FCT | | |
| | -- Tools | | --TL | |
| | -- Machinery | | --MCN | |
| | - Maintenance | -MNT | | |
| | -- Tools | | --TL | |
| | -- Machinery | | --MCN | |
| vi. | **Textiles including Sarees, Dress Materials, Men’s & Children’s Wear:** | **TXT** | | |
| | - Male | -ML | | |
| | -- Clothing | | --CLTH | |
| | -- Dress Materials | | --DRM | |
| | -- Undergarments | | --UGM | |
| | - Female | -FML | | |
| | -- Saree | | --SRI | |
| | -- Dress | | --DRS | |
| | -- Dress Materials | | --DRM | |
| | -- Undergarments | | --UGM | |
| | - Child | -CHD | | |
| | -- Dress | | --DRS | |
| | -- Dress Materials | | --DRM | |
| | - Drapery | -DRP | | |
| vii. | **Vehicles:** | **VEH** | | |
| | - Car | -CR | | |
| | -- Sedan | | --SDN | |
| | -- Hatchback | | --HTC | |
| | -- SUV | | --SUV | |
| | -- MUV | | --MUV | |
| | - Truck | -TRK | | |
| | - Bus | -BUS | | |
| | - Utility | -UTL | | |
| | -- Tractor | | --TRT | |
| | -- Harvester | | --HVR | |
| | -- Cultivator | | --CLT | |
| | -- Ambulance | | --AMB | |
| | -- Earth Mover | | --ERM | |
| | -- Fire Engine | | --FRE | |
| | - Two/ Three Wheeler | -BIK | | |
| | -- Bicycle | | --BCL | |
| | -- Scooter | | --SCT | |
| | -- Motorbike | | --MBK | |
| | -- Auto | | --AUT | |
| viii. | **Art Objects & Handicrafts:** | **ANC** | | |
| | - Art | -ART | | |
| | -- Modern | | --MOD | |
| | -- Antique | | --ANQ | |
| | --- Original | | | ---ORG |
| | --- Copy | | | ---CPY |
| | -- Rare | | --RARE | |
| | --- Original | | | ---ORG |
| | --- Copy | | | ---CPY |
| | - Handicraft | -CFT | | |
| | -- Handmade | | --HND | |
| | --- Traditional | | | ---TDN |
| | --- Antique | | | ---ANQ |
| | -- Machine Made | | --MCN | |

### Valuation & Recording

#### A. Tabulation

| Code of Category | Serial No of Group | Name of Item | Serial No of Item, Description including Material & Colour (in order) | Make / Brand if available | Rating if Available (Exclusive / High / Average / Low) | Condition (New / Unused / Working / Damaged (Details) / Scrap / Obsolete) | Appreciating / Depreciating |
|------------------|--------------------|--------------|-----------------------------------------------------------------------|---------------------------|--------------------------------------------------------|---------------------------------------------------------------------------|----------------------------|
| | | | | | | | |

#### B. Prepare Tagging Sticker / Label with Category, Name, Serial No, Condition

#### C. Upload Photo of Group of Similar Items Placed together & individual sample photos

---

## SPLOCA VALUATION FORM V-6

**Report of valuation of equipment, furniture, machinery and plant**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner(s) of the machinery/plant, under valuation  
4. If the asset is under joint ownership/co-ownership, share of each owner:  
5. Description of the machinery/plant and the purpose for which it is utilised  
6. Valuation of the machinery/plant  

| Item | Code | Description, Colour, Material | Make / Manufacturer | Model Number / Year of Production | Original Price, Present Market Price | Depreciation on Year of Valuation | Market Value |
|------|------|-------------------------------|---------------------|-----------------------------------|--------------------------------------|-----------------------------------|--------------|
| | | | | | | | |

7. **Declaration:** I hereby declare that—  
   - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
   - **(b)** I have no direct or indirect interest in the machinery/plant valued;  
   - **(c)** I have personally inspected the machinery/plant.  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer: | |
| Name & Signature of Expert Valuer (if any): | |

---

## SPLOCA VALUATION FORM V-7

**Report of valuation of Gemstones, Precious Metals & Jewellery**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner(s) of the Gemstones, Precious Metals & Jewellery  
4. If the asset is under joint ownership/co-ownership, share of each owner:  
5. Description & Valuation of each item of Gemstones, Precious Metals & Jewellery  

| Precious Item | Description | Unit | Gross Weight | Net Weight | Value of Stone | Value of Precious Metal | Total Value of Item |
|---------------|-------------|------|--------------|------------|----------------|-------------------------|---------------------|
| | | | | | | | |
| | | | | | | | |

6. **Special Value Enhancement:** (The valuer should discuss the special features, if any, of the jewellery, such as its antique value, aesthetic value, etc.)  

13. **Explanation of Rates Adopted.** *(Numbering as in source — skips from 6 to 13)*  

14. **Purity Testing Methods Adopted.**

**Testing Methods:**

1. **Digital Weighing Scale** (Sartorius & Wensar brand) with high sensitivity. Weights are reported in Grams and for Gemstones in Carats.  
2. **Gold Purity:** XRF Testing Machine (Maxsell)/ traditional touchstone method with Nitric Acid (HNO₃).  
3. **Silver Purity:** XRF Testing Machine (Maxsell)/ traditional method – Nitric Acid (HNO₃) and Salt Solution (NaCl).  
4. **Diamond:** A 10x, 14x & 20x triplet loupe for visual characteristics and CVD Test both random and continuous testing by Solitaire Diamond Institute, Bangalore / IGI & GTL.  
5. **Precious Gemstones:** 10x loupe for visual characteristics.  

### Sub-Annexure I to Form V – 7

| SL NO | PCS (IO No) | Item | Gross WT (Container no) | Net Weight | Purity (TREASURY NO.) | StoneWT | Stone Qty | RATE | C/s | C/s qty | C/s rate | Pure Metal | VALUE |
|------:|-------------|------|-------------------------|------------|-----------------------|---------|-----------|------|-----|---------|----------|------------|-------|
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | 0 | TOTALS | 0.00 | 0.00 | | 0.00 | 0 | | 0.00 | 0 | | 0.00 | 0 |

### Sub-Annexure II to Form V – 7

| Precious Item | Description | Unit | Gross Weight | Net Weight | Value of Stone | Value of Precious Metal | Total Value of Item |
|---------------|-------------|------|--------------|------------|----------------|-------------------------|---------------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

15. **Declaration:** I hereby declare that—  
    - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
    - **(b)** I have no direct or indirect interest in the jewellery valued;  
    - **(c)** I have personally inspected the jewellery.  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer: | |
| Name & Signature of Expert Valuer (if any): | |

---

## SPLOCA VALUATION FORM V-8

**Report of valuation of works of Art & Handicrafts**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner(s) of the Handicraft / Art Object  
4. If the asset is under joint ownership/co-ownership, share of each owner:  
5. Description & Valuation of each item of Handicraft / Art Object  

| Handicraft / Art Object | Description | Material | Dimensions & Weight | Value | Value Added for Hand Crafted | Value added for Antiquity | Value added for Rarity | Total Value of Item |
|-------------------------|-------------|----------|---------------------|-------|------------------------------|---------------------------|------------------------|---------------------|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

7. **I hereby declare that—**  
   - **(a)** The information furnished above is true and correct to the best of my knowledge and belief;  
   - **(b)** I have no direct or indirect interest in the work(s) of Art & Handicrafts valued;  
   - **(c)** I have personally inspected the work(s) of Art & Handicrafts.  

| | |
|--|--|
| Date: | Place: |

---

**Note: Time period of Application development, alpha testing and beta live testing shall be not exceeding 3 months from date of contract.**

---

*Transcribed from scanned PDF `Main module 1.pdf` (27 pages). Spelling as in source retained where intentional (e.g. “Forth Floor”). Sl. No. 9 is absent in Sub-Annexure to Form V-1 in the source. Form V-5 is not present in this PDF.*
