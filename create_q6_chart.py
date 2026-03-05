"""Create Question 6-1 Price vs Curve Shift Chart for MBS"""

import matplotlib.pyplot as plt
import numpy as np

# Actual Chart 6-2 data from exam: CUSIP 314M7GU9, Coupon 5%, WAC 5.83
# Price/Yield table at base price = 100 (par)
curve_shifts = np.array([-300, -200, -100, 0, 100, 200, 300])

# Actual MBS prices from Chart 6-2
mbs_prices = np.array([110.92, 108.48, 105.22, 100.00, 93.89, 87.64, 81.49])

# For comparison: a non-callable bond (positive convexity)
duration = 5.87  # OAD at base case from Chart 6-2
convexity = 0.5
bond_prices = 100 * (
    1
    - duration * (curve_shifts / 10000)
    + 0.5 * convexity * (curve_shifts / 10000) ** 2 * 100
)

plt.figure(figsize=(10, 7))
plt.plot(
    curve_shifts,
    mbs_prices,
    "b-o",
    linewidth=2.5,
    markersize=10,
    label="MBS Price (Negative Convexity)",
)
plt.plot(
    curve_shifts,
    bond_prices,
    "g--s",
    linewidth=2,
    markersize=8,
    alpha=0.7,
    label="Non-Callable Bond (Positive Convexity)",
)

# Add horizontal line at par
plt.axhline(y=100, color="gray", linestyle=":", alpha=0.5, label="Par (100)")
plt.axvline(x=0, color="gray", linestyle=":", alpha=0.5)

# Labels and formatting
plt.xlabel("Curve Shift (bps)", fontsize=14)
plt.ylabel("Price ($)", fontsize=14)
plt.title(
    "Question 6-1: MBS Price vs Curve Shift\nCUSIP 314M7GU9 (Chart 6-2 Data, Base Price = 100)",
    fontsize=14,
    fontweight="bold",
)
plt.legend(loc="upper right", fontsize=11)
plt.grid(True, alpha=0.3)

# Add annotations
plt.annotate(
    "Contraction Risk\n(Prepayments accelerate,\nprice upside limited)",
    xy=(-200, 108.48),
    xytext=(-220, 115),
    fontsize=10,
    ha="center",
    arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
)

plt.annotate(
    "Extension Risk\n(Prepayments slow,\nduration lengthens)",
    xy=(200, 87.64),
    xytext=(220, 78),
    fontsize=10,
    ha="center",
    arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
)

# Add data labels
for x, y in zip(curve_shifts, mbs_prices):
    plt.annotate(
        f"{y:.2f}",
        (x, y),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
        fontweight="bold",
    )

plt.xlim(-350, 350)
plt.ylim(75, 120)
plt.xticks([-300, -200, -100, 0, 100, 200, 300])
plt.tight_layout()
plt.savefig("Q6_1_Price_Chart.png", dpi=150, bbox_inches="tight")
plt.close()
print("Created Q6_1_Price_Chart.png")
