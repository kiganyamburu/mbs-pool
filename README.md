# MBS Pool Analysis

Tools for analyzing Mortgage-Backed Securities (MBS) pool data, specifically Fannie Mae MBS pools.

## Overview

This project provides Python scripts to:

- Extract and analyze MBS pool paydown history from Excel files
- Compare pool balances with underlying collateral
- Generate charts and visualizations
- Create formatted Word documents with analysis results
- Fetch FRED (Federal Reserve Economic Data) for economic context

## Files

| Script                 | Description                                                                       |
| ---------------------- | --------------------------------------------------------------------------------- |
| `analyze_mbs.py`       | Compares MBS Pool balance (Tab #2) vs Collateral balance (Tab #3) from Excel data |
| `create_fred_chart.py` | Generates charts using FRED economic data                                         |
| `create_fred_excel.py` | Exports FRED data to Excel format                                                 |
| `generate_chart.py`    | Creates visualizations of MBS pool data                                           |
| `convert_to_word.py`   | Converts analysis output to Word document format                                  |
| `create_final_doc.py`  | Generates final formatted documentation                                           |

## Data Source

The scripts work with Fannie Mae MBS pool data, including:

- Pool paydown history
- Collateral history
- Pool factors and balances

Example data file: `Sample MBS actual paydown FN_BJ97911_MTGE PDI .xlsx`

## Requirements

- Python 3.x
- openpyxl (Excel file handling)
- Additional dependencies may be required for charting and document generation

## Usage

```bash
# Analyze MBS pool data
python analyze_mbs.py

# Generate charts
python generate_chart.py

# Create Word document
python create_final_doc.py
```

## Related Resources

- [Fannie Mae PoolTalk](https://www.pooltalk.fanniemae.com) - Look up MBS pool details by CUSIP
- [FRED](https://fred.stlouisfed.org) - Federal Reserve Economic Data
