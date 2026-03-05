"""Create Question 3 Payment Comparison Charts"""

import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Chart 1: Payment Comparison (3a vs 3b)
ax1 = axes[0]
scenarios = [
    "3a: Fully\nAmortized",
    "3b: IO Period\n(Years 1-5)",
    "3b: Amortizing\n(Years 6-30)",
]
payments = [1199.10, 1000.00, 1288.60]
colors = ["#2E86AB", "#A23B72", "#F18F01"]

bars1 = ax1.bar(scenarios, payments, color=colors, edgecolor="black", linewidth=1.2)
ax1.set_ylabel("Monthly Payment ($)", fontsize=12)
ax1.set_title(
    "Question 3: Monthly Payment Comparison\n(Fully Amortized vs Interest-Only)",
    fontsize=13,
    fontweight="bold",
)
ax1.set_ylim(0, 1500)
ax1.grid(axis="y", alpha=0.3)

# Add value labels on bars
for bar, val in zip(bars1, payments):
    ax1.annotate(
        f"${val:,.2f}",
        xy=(bar.get_x() + bar.get_width() / 2, val),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
        fontsize=11,
        fontweight="bold",
    )

# Add payment increase annotation
ax1.annotate(
    "",
    xy=(2, 1288.60),
    xytext=(1, 1000),
    arrowprops=dict(arrowstyle="->", color="red", lw=2),
)
ax1.annotate(
    "+$288.60\n(+28.86%)",
    xy=(1.5, 1150),
    fontsize=10,
    ha="center",
    color="red",
    fontweight="bold",
)

# Chart 2: Refinancing Savings (3c)
ax2 = axes[1]

# Data for refinancing comparison
labels = ["Scenario 3a\n(Fully Amortized)", "Scenario 3b\n(Interest-Only)"]
old_payments = [1199.10, 1288.60]  # Payment before refi
new_payments = [888.51, 954.83]  # Payment after refi
savings = [310.59, 333.77]

x = np.arange(len(labels))
width = 0.35

bars_old = ax2.bar(
    x - width / 2,
    old_payments,
    width,
    label="Before Refinancing",
    color="#E74C3C",
    edgecolor="black",
)
bars_new = ax2.bar(
    x + width / 2,
    new_payments,
    width,
    label="After Refinancing (4%)",
    color="#27AE60",
    edgecolor="black",
)

ax2.set_ylabel("Monthly Payment ($)", fontsize=12)
ax2.set_title(
    "Question 3c: Refinancing Savings at Year 5\n(New Rate: 4%, 30-Year Term)",
    fontsize=13,
    fontweight="bold",
)
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.legend(loc="upper right")
ax2.set_ylim(0, 1500)
ax2.grid(axis="y", alpha=0.3)

# Add value labels
for bar in bars_old:
    ax2.annotate(
        f"${bar.get_height():,.2f}",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
        fontsize=10,
        fontweight="bold",
    )
for bar in bars_new:
    ax2.annotate(
        f"${bar.get_height():,.2f}",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
        fontsize=10,
        fontweight="bold",
    )

# Add savings annotations
for i, (label, save) in enumerate(zip(labels, savings)):
    ax2.annotate(
        f"Savings:\n${save:,.2f}/mo",
        xy=(i, (old_payments[i] + new_payments[i]) / 2),
        fontsize=10,
        ha="center",
        color="#2C3E50",
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
    )

plt.tight_layout()
plt.savefig("Q3_Payment_Chart.png", dpi=150, bbox_inches="tight")
plt.close()

print("Created Q3_Payment_Chart.png")
