import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data from FRED
us_data = {
    "2007-01": 20.59,
    "2007-06": 20.95,
    "2007-12": 21.16,
    "2008-01": 21.19,
    "2008-06": 21.52,
    "2008-12": 21.95,
    "2009-01": 21.96,
    "2009-06": 22.14,
    "2009-12": 22.37,
    "2010-01": 22.40,
    "2010-06": 22.53,
    "2010-12": 22.76,
    "2011-01": 22.87,
    "2011-06": 23.00,
    "2011-12": 23.22,
    "2012-01": 23.26,
    "2012-06": 23.46,
    "2012-12": 23.72,
    "2013-01": 23.74,
    "2013-06": 23.96,
    "2013-12": 24.18,
    "2014-01": 24.22,
    "2014-06": 24.46,
    "2014-12": 24.63,
    "2015-01": 24.74,
    "2015-06": 24.97,
    "2015-12": 25.25,
    "2016-01": 25.37,
    "2016-06": 25.62,
    "2016-12": 25.93,
    "2017-01": 26.00,
    "2017-06": 26.26,
    "2017-12": 26.63,
    "2018-01": 26.72,
    "2018-06": 27.03,
    "2018-12": 27.56,
    "2019-01": 27.59,
    "2019-06": 27.97,
    "2019-12": 28.38,
    "2020-01": 28.43,
    "2020-06": 29.38,
    "2020-12": 29.91,
    "2021-01": 29.93,
    "2021-06": 30.54,
    "2021-12": 31.39,
    "2022-01": 31.60,
    "2022-06": 32.19,
    "2022-12": 32.94,
    "2023-01": 33.02,
    "2023-06": 33.69,
    "2023-12": 34.29,
    "2024-01": 34.47,
    "2024-06": 35.01,
    "2024-12": 35.69,
    "2025-01": 35.84,
    "2025-06": 36.36,
    "2025-12": 37.02,
}

ca_data = {
    "2007-01": 25.03,
    "2007-06": 24.66,
    "2007-12": 24.48,
    "2008-01": 24.23,
    "2008-06": 24.67,
    "2008-12": 25.57,
    "2009-01": 25.43,
    "2009-06": 25.30,
    "2009-12": 25.69,
    "2010-01": 26.41,
    "2010-06": 26.20,
    "2010-12": 26.69,
    "2011-01": 26.87,
    "2011-06": 26.67,
    "2011-12": 26.84,
    "2012-01": 27.26,
    "2012-06": 26.79,
    "2012-12": 27.16,
    "2013-01": 27.01,
    "2013-06": 27.12,
    "2013-12": 27.37,
    "2014-01": 27.34,
    "2014-06": 27.38,
    "2014-12": 27.90,
    "2015-01": 28.14,
    "2015-06": 27.95,
    "2015-12": 28.37,
    "2016-01": 28.61,
    "2016-06": 28.70,
    "2016-12": 29.51,
    "2017-01": 29.94,
    "2017-06": 29.71,
    "2017-12": 30.48,
    "2018-01": 30.63,
    "2018-06": 30.64,
    "2018-12": 31.99,
    "2019-01": 32.08,
    "2019-06": 32.43,
    "2019-12": 33.22,
    "2020-01": 33.20,
    "2020-06": 34.20,
    "2020-12": 35.50,
    "2021-01": 35.63,
    "2021-06": 35.69,
    "2021-12": 37.02,
    "2022-01": 37.51,
    "2022-06": 37.32,
    "2022-12": 37.66,
    "2023-01": 38.32,
    "2023-06": 37.68,
    "2023-12": 38.43,
    "2024-01": 38.58,
    "2024-06": 39.56,
    "2024-12": 40.78,
    "2025-01": 40.76,
    "2025-06": 41.17,
    "2025-12": 42.03,
}

oh_data = {
    "2007-01": 20.08,
    "2007-06": 19.99,
    "2007-12": 20.39,
    "2008-01": 19.95,
    "2008-06": 19.96,
    "2008-12": 20.52,
    "2009-01": 20.02,
    "2009-06": 19.76,
    "2009-12": 20.24,
    "2010-01": 20.11,
    "2010-06": 20.01,
    "2010-12": 20.63,
    "2011-01": 20.85,
    "2011-06": 20.78,
    "2011-12": 21.40,
    "2012-01": 21.97,
    "2012-06": 21.69,
    "2012-12": 22.46,
    "2013-01": 22.37,
    "2013-06": 22.12,
    "2013-12": 22.40,
    "2014-01": 22.37,
    "2014-06": 22.11,
    "2014-12": 22.44,
    "2015-01": 22.65,
    "2015-06": 22.44,
    "2015-12": 22.95,
    "2016-01": 23.14,
    "2016-06": 23.10,
    "2016-12": 23.92,
    "2017-01": 24.13,
    "2017-06": 23.77,
    "2017-12": 24.30,
    "2018-01": 24.64,
    "2018-06": 24.35,
    "2018-12": 25.44,
    "2019-01": 25.44,
    "2019-06": 25.07,
    "2019-12": 25.64,
    "2020-01": 25.69,
    "2020-06": 25.58,
    "2020-12": 26.65,
    "2021-01": 26.78,
    "2021-06": 27.25,
    "2021-12": 28.36,
    "2022-01": 28.96,
    "2022-06": 28.88,
    "2022-12": 30.21,
    "2023-01": 30.90,
    "2023-06": 30.24,
    "2023-12": 31.26,
    "2024-01": 31.36,
    "2024-06": 31.60,
    "2024-12": 32.91,
    "2025-01": 33.01,
    "2025-06": 33.07,
    "2025-12": 33.29,
}

# Parse dates and values
dates = [datetime.strptime(d, "%Y-%m") for d in sorted(us_data.keys())]
us_vals = [us_data[d] for d in sorted(us_data.keys())]
ca_vals = [ca_data[d] for d in sorted(ca_data.keys())]
oh_vals = [oh_data[d] for d in sorted(oh_data.keys())]
gap_vals = [ca_data[d] - oh_data[d] for d in sorted(oh_data.keys())]

# Create figure with dual y-axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Primary axis - AHE levels
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Average Hourly Earnings ($/hour)", fontsize=12, color="black")
(line1,) = ax1.plot(
    dates, us_vals, "b-", linewidth=2, marker="o", markersize=4, label="US (National)"
)
(line2,) = ax1.plot(
    dates, ca_vals, "g-", linewidth=2, marker="s", markersize=4, label="California"
)
(line3,) = ax1.plot(
    dates, oh_vals, "r-", linewidth=2, marker="^", markersize=4, label="Ohio"
)
ax1.tick_params(axis="y")
ax1.set_ylim(15, 50)

# Secondary axis - Wage gap
ax2 = ax1.twinx()
ax2.set_ylabel("CA-OH Wage Gap ($/hour)", fontsize=12, color="purple")
(line4,) = ax2.plot(
    dates, gap_vals, "purple", linewidth=3, linestyle="--", label="CA-OH Gap"
)
ax2.tick_params(axis="y", labelcolor="purple")
ax2.set_ylim(0, 15)

# Format x-axis
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax1.xaxis.set_major_locator(mdates.YearLocator(2))
plt.xticks(rotation=45)

# Title
plt.title(
    "Average Hourly Earnings: US, California, Ohio, and CA-OH Wage Gap\n(FRED Data: January 2007 – December 2025)",
    fontsize=14,
    fontweight="bold",
)

# Legend
lines = [line1, line2, line3, line4]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper left", fontsize=10)

# Grid
ax1.grid(True, linestyle="--", alpha=0.7)

# Annotations
ax1.annotate(
    f"Dec 2025:\nUS: ${us_vals[-1]:.2f}\nCA: ${ca_vals[-1]:.2f}\nOH: ${oh_vals[-1]:.2f}",
    xy=(dates[-1], ca_vals[-1]),
    xytext=(dates[-8], 45),
    fontsize=9,
    ha="left",
    bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8),
    arrowprops=dict(arrowstyle="->", color="gray"),
)

ax2.annotate(
    f"Gap: ${gap_vals[-1]:.2f}/hr",
    xy=(dates[-1], gap_vals[-1]),
    xytext=(dates[-6], 12),
    fontsize=10,
    ha="center",
    color="purple",
    bbox=dict(boxstyle="round", facecolor="lavender", alpha=0.8),
    arrowprops=dict(arrowstyle="->", color="purple"),
)

plt.tight_layout()
plt.savefig("FRED_AHE_Chart.png", dpi=150, bbox_inches="tight")
print("Chart saved: FRED_AHE_Chart.png")

# Additional statistics for analysis
print("\n=== Detailed Analysis for Part D ===")
print("\n1. TRENDS OVER TIME:")
print(f"   - All three series show steady upward trends from 2007-2025")
print(f"   - COVID-19 pandemic (2020) caused temporary wage distortions")
print(f"   - Post-2020 recovery shows accelerated wage growth")

print("\n2. WAGE GAP EVOLUTION:")
print(
    f"   - Jan 2007 Gap: ${gap_vals[0]:.2f}/hr ({(ca_vals[0]/oh_vals[0]-1)*100:.1f}% premium)"
)
print(
    f"   - Dec 2025 Gap: ${gap_vals[-1]:.2f}/hr ({(ca_vals[-1]/oh_vals[-1]-1)*100:.1f}% premium)"
)
print(f"   - The gap WIDENED by ${gap_vals[-1] - gap_vals[0]:.2f}/hr over 18 years")

print("\n3. ECONOMIC IMPLICATIONS:")
print("   California's persistent wage premium reflects:")
print("   - Higher cost of living (housing, taxes)")
print("   - Tech sector concentration in Silicon Valley")
print("   - Higher minimum wage laws ($16/hr vs $10.45/hr)")
print("   - Different industry mix (more high-wage services)")
