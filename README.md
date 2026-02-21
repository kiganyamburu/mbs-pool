# MBS Pool Analysis

Real Estate Capital Market Analysis tools for Spring 2026 coursework.

## Overview

This project contains Python scripts for analyzing Mortgage-Backed Securities (MBS) and solving real estate finance problems.

## Scripts

| Script                  | Purpose                                                            |
| ----------------------- | ------------------------------------------------------------------ |
| `analyze_mbs.py`        | Compares MBS pool balances vs collateral balances from Excel data  |
| `solve_midterm.py`      | Calculates mortgage balances, payments, and yields                 |
| `create_fred_chart.py`  | Generates charts from FRED economic data (Average Hourly Earnings) |
| `create_fred_excel.py`  | Exports FRED data to Excel                                         |
| `create_q3_chart.py`    | Creates Q3 cashflow/payment charts                                 |
| `create_q6_chart.py`    | Creates Q6 price charts                                            |
| `generate_chart.py`     | General chart generation utility                                   |
| `convert_md_to_docx.py` | Converts Markdown files to Word documents                          |
| `convert_to_word.py`    | Document conversion utility                                        |
| `create_final_doc.py`   | Generates final document outputs                                   |

## Data Files

- `Sample MBS actual paydown FN_BJ97911_MTGE PDI .xlsx` - MBS paydown history
- `Sample MBS Projected Cashflow.xlsx` - Projected cashflow data
- `FRED_AHE_Analysis.xlsx` - Average Hourly Earnings analysis
- `Exam1_2026S.xlsx` - Exam data

## Requirements

```
numpy
numpy-financial
openpyxl
matplotlib
python-docx
```

## Usage

```bash
# Analyze MBS pool data
python analyze_mbs.py

# Solve midterm problems
python solve_midterm.py

# Generate FRED chart
python create_fred_chart.py
```
