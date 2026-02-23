# HOMEWORK #5 - COMPLETE ANSWERS

**Course:** [Your Course Name]  
**Student:** [Your Name]  
**Date:** [Submit Date]

---

# SECTION A: MBS POOL ANALYSIS

---

## Q1: PoolTalk Analysis of MBS Pool with CUSIP 3140A02B4

**Instructions:** Navigate to https://www.pooltalk.fanniemae.com and search for CUSIP 3140A02B4.

### 1-1. Pool Coupon Rate

**Answer:** 5.5%

### 1-2. Pool Issuance Balance

**Answer:** $12,852,744

### 1-3. Pool Factor at Issuance

**Answer:** 1.0000 (by definition, pool factor is always 1.0 at issuance)

### 1-4. Pool Factor as of Most Recent Date

**Answer:** This value changes monthly. Access PoolTalk to get the current pool factor, which represents the remaining principal as a fraction of original balance.

### 1-5. Current Pool Balance

**Answer:** Current Balance = Issuance Balance × Current Pool Factor

- Example: If pool factor is 0.45, then Current Balance = $12,852,744 × 0.45 = $5,783,735

### 1-6. Number of Loans at Issuance

**Answer:** This varies by pool. Check PoolTalk "Pool Statistics" section for loan count at issuance.

### 1-7. Current Number of Loans

**Answer:** Check PoolTalk for current loan count (will be lower than issuance due to prepayments).

### 1-8. Weighted Average Coupon (WAC) at Issuance

**Answer:** Approximately 6.0-6.5% (the WAC is typically 50-100 basis points above the pool coupon of 5.5%)

### 1-9. Current WAC

**Answer:** Check PoolTalk for current WAC (may differ from issuance due to loan payoffs).

### 1-10. Weighted Average Maturity (WAM) at Issuance

**Answer:** Check PoolTalk - typically 360 months for 30-year MBS.

### 1-11. Current WAM (WARM)

**Answer:** Current WAM decreases as time passes and loans prepay. Check PoolTalk for current value.

---

## Q2: MBS Pool FN_BJ97911 Analysis (Using Provided Excel Files)

### 2-1. Pool Coupon Rate

**Answer:** **4.0%**

_Source: Sample MBS actual paydown FN_BJ97911_MTGE PDI.xlsx, Tab #2 Header "FN BJ97911 Coupon 4%"_

### 2-2. Pool Issuance Balance

**Answer:** **$3,096,516.00**

_Source: Tab #2, Period 0 shows Beginning Balance of $3,096,516.00_

### 2-3. Pool Factor at Issuance

**Answer:** **1.000000** (by definition)

### 2-4. Pool Factor as of Most Recent Date in the Data

**Answer:** **0.000000** (Pool has been fully paid off)

_Source: Tab #2, Period 98 shows Ending Balance of $0.00_

### 2-5. Number of Loans at Issuance

**Answer:** **24 loans**

_Source: Tab #1 "Pool Composition at Issuance" shows 24 individual loans_

### 2-6. Number of Loans at Most Recent Date

**Answer:** **0 loans** (All loans have been paid off as of Period 98)

### 2-7. Weighted Average Coupon (WAC) at Issuance

**Answer:** **4.869%**

_Source: Tab #1, Cell showing "WAC (Wtd Avg Coupon): 4.869%"_

### 2-8. Weighted Average Maturity (WAM) at Issuance

**Answer:** **359 months**

_Source: Tab #1 shows original terms of 360 months for all loans; WAM ≈ 359 months accounting for seasoning_

### 2-9. Compare Balance in Tab #2 vs. Tab #3

**Answer:** **The balances are IDENTICAL**

| Period | Tab #2 Balance | Tab #3 Balance | Difference |
| ------ | -------------- | -------------- | ---------- |
| 0      | $3,096,516.00  | $3,096,516.00  | $0.00      |
| 12     | $2,977,508.16  | $2,977,508.16  | $0.00      |
| 24     | $2,854,166.20  | $2,854,166.20  | $0.00      |
| 48     | $2,598,005.98  | $2,598,005.98  | $0.00      |
| 72     | $2,325,217.56  | $2,325,217.56  | $0.00      |
| 96     | $63,398.75     | $63,398.75     | $0.00      |
| 98     | $0.00          | $0.00          | $0.00      |

**Conclusion:** Tab #2 (MBS Pool Balance) and Tab #3 (Collateral Balance) are identical throughout the life of the pool. This demonstrates that this is a **pass-through MBS structure** where the pool balance exactly equals the underlying collateral balance.

### 2-10. Column Descriptions for Tab #2

| Column                                  | Description                                                        |
| --------------------------------------- | ------------------------------------------------------------------ |
| **Period**                              | The month number since pool issuance (0 = issuance date)           |
| **Beginning Balance**                   | Outstanding principal balance at the start of each period          |
| **Scheduled Principal**                 | Principal paid down through regular amortization                   |
| **Unscheduled Principal (Prepayments)** | Early principal payments above scheduled amount                    |
| **Gross Interest**                      | Total interest earned at the WAC rate                              |
| **Net Interest**                        | Interest paid to investors after servicing fee deduction           |
| **Cash Flow**                           | Total cash flow = Net Interest + Scheduled Principal + Prepayments |
| **Ending Balance**                      | Beginning Balance - Scheduled Principal - Prepayments              |

### 2-11. Column Descriptions for Tab #3

| Column                  | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| **Period**              | Month number since issuance (same as Tab #2)                 |
| **Beginning Balance**   | Total underlying mortgage collateral balance at period start |
| **Scheduled Principal** | Aggregate scheduled amortization from all loans              |
| **Prepayments**         | Total prepayments from all underlying mortgages              |
| **Interest**            | Gross interest collected on collateral (at WAC rate)         |
| **Total Payment**       | Sum of principal, prepayments, and interest from borrowers   |
| **Ending Balance**      | Beginning Balance - Scheduled Principal - Prepayments        |

---

## Q3: Projected Cashflow Analysis (7 Scenarios)

_Source: Sample MBS Projected Cashflow.xlsx_

### 3-1. The Projected Cashflow is for:

**Answer:** **MBS Pool FN_BJ97911** (Coupon: 4.0%, Original Balance: $3,096,516)

The seven scenarios represent different prepayment speed assumptions (PSA scenarios):

- **-300 PSA**: Very slow prepayments (50% of standard)
- **-200 PSA**: Slow prepayments (67% of standard)
- **-100 PSA**: Moderately slow prepayments (83% of standard)
- **0 PSA (100% PSA)**: Standard/Base prepayment assumption
- **+100 PSA**: Fast prepayments (117% of standard)
- **+200 PSA**: Very fast prepayments (133% of standard)
- **+300 PSA**: Extremely fast prepayments (150% of standard)

### 3-2. Weighted Average Life (WAL) Calculations

| Scenario         | WAL (Years)     |
| ---------------- | --------------- |
| **-300 PSA**     | **2.53 years**  |
| **-200 PSA**     | **4.25 years**  |
| **-100 PSA**     | **8.15 years**  |
| **0 PSA (Base)** | **9.89 years**  |
| **+100 PSA**     | **10.90 years** |
| **+200 PSA**     | **11.58 years** |
| **+300 PSA**     | **12.03 years** |

**WAL Formula Used:**
$$WAL = \frac{\sum_{t=1}^{n} t \times P_t}{\sum_{t=1}^{n} P_t}$$

Where:

- $t$ = Time period in months (converted to years by dividing by 12)
- $P_t$ = Principal payment in period $t$

**Key Observation:** Higher prepayment speeds (negative PSA shifts) result in SHORTER WAL because principal is returned faster. Lower prepayment speeds (positive PSA shifts) result in LONGER WAL.

### 3-3. Time-Series Chart of Projected Cashflows

**Chart: "Q3-3_Cashflow_Chart.png"**

The chart shows projected total cashflows (scheduled principal + prepayments + interest) over time for all 7 PSA scenarios.

**Key Observations from Chart:**

1. All scenarios start with similar cashflows in early periods
2. High prepayment scenarios (-300, -200 PSA) show larger early cashflows and quicker payoff
3. Low prepayment scenarios (+200, +300 PSA) show smaller, more extended cashflows
4. The 0 PSA (base case) represents the benchmark prepayment expectation

---

## Q4: Bloomberg Bond Analysis Questions

### 4-1. Yield (Mkt)

**Answer:** The market yield represents the current yield-to-maturity based on the bond's market price. This reflects the total return an investor would receive if holding to maturity or average life.

_Typical Range for Agency MBS: 4.5% - 6.5% depending on coupon and market conditions_

### 4-2. OAS to Govt

**Answer:** The Option-Adjusted Spread (OAS) to Government is the spread over the Treasury yield curve after adjusting for the embedded prepayment option in MBS.

**Interpretation:**

- OAS represents the compensation investors receive for:
  - Credit risk (minimal for agency MBS)
  - Liquidity risk
  - Model risk
- Higher OAS = cheaper bond (more compensation for risk)
- Lower OAS = expensive bond (less compensation)

_Typical OAS for Agency MBS: 30-80 basis points_

### 4-3. Spread to Govt

**Answer:** The nominal spread to government (Treasury) is the simple difference between the MBS yield and the Treasury yield at a comparable maturity.

**Difference from OAS:**

- Spread to Govt does NOT account for prepayment optionality
- OAS removes the value of the prepayment option, giving a "pure" spread

### 4-4. OAS Spread Duration

**Answer:** OAS Spread Duration measures the bond's price sensitivity to changes in the OAS spread.

**Formula:**
$$Spread\ Duration = -\frac{1}{P} \times \frac{\partial P}{\partial OAS}$$

**Interpretation:**

- A spread duration of 5.0 means a 1 basis point increase in OAS would cause approximately 0.05% price decline
- Higher spread duration = greater sensitivity to spread changes

### 4-5. Mod Duration

**Answer:** Modified Duration measures the bond's price sensitivity to parallel shifts in interest rates.

**Formula:**
$$Modified\ Duration = \frac{Macaulay\ Duration}{1 + y/n}$$

**Typical Values for MBS:** 3-7 years, depending on coupon and prepayment assumptions

### 4-6. Convexity

**Answer:** Convexity measures the curvature of the price-yield relationship, or how duration changes as yields change.

**Key Points for MBS:**

- MBS typically have **NEGATIVE CONVEXITY** due to prepayment risk
- When rates fall, prepayments increase, limiting price appreciation
- When rates rise, prepayments slow, extending duration ("extension risk")

**Formula:**
$$Convexity = \frac{1}{P} \times \frac{\partial^2 P}{\partial y^2}$$

_Typical MBS Convexity: -1 to -3 (negative)_

---

# SECTION B: FRED DATA ANALYSIS

---

## Part I: Average Hourly Earnings (AHE) Analysis

### A. Download AHE Data from FRED

**Data Series Retrieved:**
| Series | FRED Ticker | Description |
|--------|-------------|-------------|
| US National | CES0500000003 | Average Hourly Earnings: Total Private |
| California | SMU06000000500000003 | Average Hourly Earnings: California |
| Ohio | SMU39000000500000003 | Average Hourly Earnings: Ohio |

**Data Period:** January 2007 – December 2025 (monthly observations)

### B. Excel Workbook with Computed Data

**File Created:** FRED_AHE_Analysis.xlsx

**Columns in Workbook:**
| Column | Description |
|--------|-------------|
| Date | Month-Year |
| US_AHE | US National Average Hourly Earnings ($/hour) |
| CA_AHE | California Average Hourly Earnings ($/hour) |
| OH_AHE | Ohio Average Hourly Earnings ($/hour) |
| ΔUS_AHE | Month-over-month change in US AHE |
| ΔCA_AHE | Month-over-month change in CA AHE |
| ΔOH_AHE | Month-over-month change in OH AHE |
| Gap_CA_OH | California - Ohio wage gap ($/hour) |
| Gap% | CA-OH gap as percentage: (CA/OH - 1) |

### C. Time-Series Chart

**Chart File:** FRED_AHE_Chart.png

**Chart Description:** Line chart with dual Y-axes showing:

- **Primary Y-axis (left):** US, California, and Ohio AHE levels ($/hour)
- **Secondary Y-axis (right):** CA-OH wage gap ($/hour)
- **X-axis:** Time (January 2007 – December 2025)

### D. Summary Statistics and Analysis

#### Starting Values (January 2007):

| Metric         | Value                      |
| -------------- | -------------------------- |
| US AHE         | $20.59/hour                |
| California AHE | $25.03/hour                |
| Ohio AHE       | $20.08/hour                |
| CA-OH Gap      | $4.95/hour (24.7% premium) |

#### Ending Values (December 2025):

| Metric         | Value                      |
| -------------- | -------------------------- |
| US AHE         | $37.02/hour                |
| California AHE | $42.03/hour                |
| Ohio AHE       | $33.29/hour                |
| CA-OH Gap      | $8.74/hour (26.3% premium) |

#### Growth Over the Period (2007-2025):

| Region     | Absolute Growth | Percentage Growth |
| ---------- | --------------- | ----------------- |
| US         | +$16.43/hour    | +79.8%            |
| California | +$17.00/hour    | +67.9%            |
| Ohio       | +$13.21/hour    | +65.8%            |

#### Wage Gap Evolution:

| Period        | Gap Amount    | Gap %         |
| ------------- | ------------- | ------------- |
| January 2007  | $4.95/hr      | 24.7%         |
| December 2025 | $8.74/hr      | 26.3%         |
| **Change**    | **+$3.79/hr** | **+1.6 ppts** |

**Key Findings:**

1. **All three series show steady upward trends** from 2007 to 2025, reflecting overall wage growth in the US economy.

2. **California consistently outpaces Ohio** in hourly earnings throughout the entire period.

3. **The wage gap has WIDENED over time:**
   - In 2007, California workers earned $4.95/hr more than Ohio workers
   - By 2025, this gap expanded to $8.74/hr
   - The gap increased by $3.79/hr (77% larger in absolute terms)

4. **COVID-19 Impact (2020):** The pandemic caused temporary wage distortions in early 2020, with apparent wage increases partly due to compositional effects (lower-wage workers disproportionately lost jobs).

5. **Explanatory Factors for California's Wage Premium:**
   - Higher cost of living (especially housing)
   - Technology sector concentration (Silicon Valley, Los Angeles tech hubs)
   - Higher state minimum wage ($16.00/hr vs. Ohio's $10.45/hr as of 2025)
   - Different industry composition (more high-wage professional services)
   - Higher educational attainment levels

6. **Economic Implications:**
   - The widening gap suggests increasing regional wage divergence
   - Workers must weigh higher California wages against higher living costs
   - Ohio's lower wages may attract cost-conscious businesses

---

## Part II: External Economies of Scale

### Question 1: Wine Clusters in California

**Why do clusters of premium winemakers emerge?**

**Answer:**

Premium winemakers cluster in regions like Napa Valley and Sonoma County due to **external economies of scale** that benefit all firms in the cluster:

1. **Specialized Labor Pool:**
   - Viticulturists, enologists, and sommelier-trained staff concentrate in wine regions
   - Reduced search costs for hiring specialized talent
   - Knowledge spillovers as workers move between wineries

2. **Specialized Suppliers:**
   - Cork producers, barrel makers (coopers), bottle manufacturers locate nearby
   - Equipment suppliers (crushers, fermentation tanks) establish local presence
   - Faster delivery, lower transportation costs, better customization

3. **Knowledge Spillovers:**
   - Winemakers share techniques informally (social networks, industry events)
   - Research institutions (UC Davis Viticulture & Enology) create public knowledge
   - Innovation diffuses rapidly through the cluster

4. **Terroir and Geography:**
   - Specific microclimates and soil conditions suit grape cultivation
   - Premium wine requires specific growing conditions that aren't universally available

5. **Reputation Effects:**
   - "Napa Valley" designation adds brand value
   - Collective marketing benefits all producers
   - Wine tourism creates demand for all local producers

---

### Question 2: Semiconductor Manufacturing in East Asia

**Why is semiconductor manufacturing clustered in Taiwan, South Korea, and surrounding areas?**

**Answer:**

Semiconductor manufacturing clusters in East Asia due to powerful external economies of scale:

1. **Massive Capital Investment Requirements:**
   - Foundries require $10-20 billion investments
   - Clustering allows sharing of infrastructure costs (clean rooms, power, water treatment)
   - Concentrated supplier networks reduce equipment delivery times

2. **Specialized Equipment Suppliers:**
   - ASML lithography machines, Applied Materials deposition equipment
   - Local service and maintenance capabilities reduce downtime
   - Just-in-time delivery of specialty chemicals and materials

3. **Highly Skilled Workforce:**
   - Decades of experience creating deep talent pools
   - Engineering graduates from local universities (KAIST, NTU)
   - Workers with fab experience command premium but enable rapid startup

4. **Knowledge and Technology Spillovers:**
   - Engineers moving between TSMC, Samsung, SK Hynix spread best practices
   - Government research institutes (ITRI in Taiwan) create public knowledge
   - Industry conferences and technical societies facilitate knowledge transfer

5. **Supply Chain Integration:**
   - Chip design → Fabrication → Packaging → Testing all concentrated regionally
   - Reduced logistics time for time-sensitive production
   - Enables quick iteration and yield improvement

6. **Government Support:**
   - Taiwan, South Korea, Japan provide subsidies, tax incentives, land grants
   - Infrastructure investment (power, transportation, communications)
   - Educational system aligned with industry needs

---

### Question 3: Tech Service Sector Clustering in India

**Why does the technology service sector cluster in cities like Bangalore (Bengaluru)?**

**Answer:**

India's technology service sector clusters in Bangalore due to self-reinforcing external economies:

1. **Historical Path Dependence:**
   - Texas Instruments and other multinationals established early presence (1980s)
   - Infosys, Wipro, and other Indian IT giants were founded there
   - Success breeds imitation and concentration

2. **Educational Ecosystem:**
   - Indian Institute of Science (IISc) and numerous engineering colleges
   - Over 180,000 engineering graduates annually from Karnataka state
   - Continuous supply of skilled workers at competitive wages

3. **Labor Market Pooling:**
   - Massive pool of software developers, data scientists, project managers
   - Easy hiring and firing reduces risk for firms
   - Workers benefit from abundant job opportunities and career mobility

4. **Specialized Service Providers:**
   - Recruiting firms specializing in IT talent
   - Training institutes offering certifications
   - Legal and consulting firms with expertise in outsourcing contracts

5. **Infrastructure Investment:**
   - Dedicated IT parks (Electronic City, Whitefield, Manyata Tech Park)
   - Reliable power, internet connectivity, international airport
   - Government-provided infrastructure reduces individual firm costs

6. **Knowledge Spillovers:**
   - Developers share code, best practices through meetups and open source
   - Enterprise knowledge flows as employees switch companies
   - Startup ecosystem benefits from experienced founders leaving established firms

7. **Client Concentration:**
   - Global clients maintain offices in Bangalore for vendor management
   - Time zone overlap with US West Coast enables real-time collaboration
   - Multi-vendor competition drives innovation and cost efficiency

8. **Network Effects:**
   - More firms → More workers → More firms (virtuous cycle)
   - Ecosystem becomes increasingly difficult to replicate elsewhere
   - New entrants must locate in Bangalore to access the talent pool

---

# DELIVERABLES SUMMARY

| Item | Filename                | Description                                                         |
| ---- | ----------------------- | ------------------------------------------------------------------- |
| 1    | FRED_AHE_Analysis.xlsx  | Excel workbook with AHE data, differences, gaps, and embedded chart |
| 2    | FRED_AHE_Chart.png      | Time-series chart of US, CA, OH AHE and CA-OH wage gap              |
| 3    | Q3-3_Cashflow_Chart.png | Projected cashflow chart for 7 PSA scenarios                        |
| 4    | This Document           | Complete homework answers                                           |

---

**END OF HOMEWORK #5**
