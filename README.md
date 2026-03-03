# MBS Pool Analysis

Tools for analyzing Mortgage-Backed Securities (MBS) pool data, specifically Fannie Mae MBS pools.

## Overview

This project provides Python scripts to:

- Extract and analyze MBS pool paydown history from Excel files
- Compare pool balances with underlying collateral
- Generate charts and visualizations for projected cashflows across interest rate scenarios
- Create formatted Word documents with analysis results
- Fetch and visualize FRED (Federal Reserve Economic Data) for economic context

## Scripts

| Script                 | Description                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| `analyze_mbs.py`       | Compares MBS Pool balance (Tab #2) vs Collateral balance (Tab #3) from paydown history data |
| `generate_chart.py`    | Creates projected cashflow charts across rate scenarios (-300 to +300 MED) with WAL values  |
| `create_fred_chart.py` | Generates Average Hourly Earnings (AHE) trend charts using FRED data                        |
| `create_fred_excel.py` | Exports FRED AHE data to Excel format                                                       |
| `convert_to_word.py`   | Converts analysis output to Word document format                                            |
| `create_final_doc.py`  | Generates final formatted documentation                                                     |

## Data Files

| File                                                  | Description                                               |
| ----------------------------------------------------- | --------------------------------------------------------- |
| `Sample MBS actual paydown FN_BJ97911_MTGE PDI .xlsx` | Fannie Mae pool paydown and collateral history            |
| `Sample MBS Projected Cashflow.xlsx`                  | Projected cashflows under various interest rate scenarios |
| `FRED_AHE_Analysis.xlsx`                              | Exported FRED Average Hourly Earnings data                |
| `FRED_AHE_Chart.png`                                  | Generated AHE trend visualization                         |
| `Q3-3_Cashflow_Chart.png`                             | Projected cashflow chart output                           |

## Requirements

- Python 3.x
- openpyxl (Excel file handling)
- matplotlib (charting and visualization)
- python-docx (Word document generation)

## Usage

```bash
# Analyze MBS pool data
python analyze_mbs.py

# Generate projected cashflow chart
python generate_chart.py

# Generate FRED chart
python create_fred_chart.py

# Create Word document
python create_final_doc.py
```

## Related Resources

- [Fannie Mae PoolTalk](https://www.pooltalk.fanniemae.com) - Look up MBS pool details by CUSIP
- [FRED](https://fred.stlouisfed.org) - Federal Reserve Economic Data
  +1 and +2 years where did you get that data like estimate for sales, revenue link

+1 and +2 years where did you get that data like estimate for sales, revenue link
+1 and +2 years where did you get that data like estimate for sales, revenue link
+1 and +2 years where did you get that data like estimate for sales, revenue link
+1 and +2 years where did you get that data like estimate for sales, revenue link
+1 and +2 years where did you get that data like estimate for sales, revenue link
+1 and +2 years where did you get that data like estimate for sales, revenue link
+1 and +2 years where did you get that data like estimate for sales, revenue link
+1 and +2 years where did you get that data like estimate for sales, revenue link
