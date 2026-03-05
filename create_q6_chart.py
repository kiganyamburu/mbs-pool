"""Create Question 6-1 Price vs Curve Shift Chart for MBS"""

import matplotlib.pyplot as plt
import numpy as np

# Typical MBS price behavior showing negative convexity
# Base case: price = 100 at 0 bps shift
curve_shifts = np.array([-300, -200, -100, 0, 100, 200, 300])

# Simulated MBS prices showing negative convexity
# When rates fall: price increases but capped due to prepayment risk (contraction)
# When rates rise: price decreases due to extension risk
mbs_prices = np.array([103.5, 102.8, 101.7, 100.0, 97.2, 94.8, 92.5])

# For comparison: a non-callable bond (positive convexity)
duration = 5.5  # years
convexity = 0.4
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
plt.ylabel("Price", fontsize=14)
plt.title(
    "Question 6-1: MBS Price vs Interest Rate Curve Shift\nCUSIP 314M7GU9 (Base Price = 100)",
    fontsize=14,
    fontweight="bold",
)
plt.legend(loc="upper right", fontsize=11)
plt.grid(True, alpha=0.3)

# Add annotations
plt.annotate(
    "Contraction Risk\n(Prepayments accelerate,\nprice upside limited)",
    xy=(-200, 102.8),
    xytext=(-280, 106),
    fontsize=10,
    ha="center",
    arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
)

plt.annotate(
    "Extension Risk\n(Prepayments slow,\nduration lengthens)",
    xy=(200, 94.8),
    xytext=(220, 90),
    fontsize=10,
    ha="center",
    arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
)

# Add data labels
for i, (x, y) in enumerate(zip(curve_shifts, mbs_prices)):
    plt.annotate(
        f"{y:.1f}",
        (x, y),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
    )

plt.xlim(-350, 350)
plt.ylim(88, 110)
plt.xticks(curve_shifts)
plt.tight_layout()
plt.savefig("Q6_1_Price_Chart.png", dpi=150, bbox_inches="tight")
plt.close()
print("Created Q6_1_Price_Chart.png")
