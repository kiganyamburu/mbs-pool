"""
Spring 2026 Real Estate Capital Market Analysis - Midterm Exam Solutions
"""
import numpy as np
import numpy_financial as npf

print('='*60)
print('QUESTION 1: Scheduled Balances at End of Year 5')
print('='*60)

# For a 30-year mortgage, the balance at month t equals PV of remaining payments

# Mortgage A: $100,000 at 8%
P_A = 100000
r_A = 0.08 / 12  # monthly rate
n_A = 360  # 30 years in months

# Monthly payment
PMT_A = P_A * (r_A * (1 + r_A)**n_A) / ((1 + r_A)**n_A - 1)
print(f'Mortgage A monthly payment: ${PMT_A:,.2f}')

# Balance at end of year 5 (month 60) = PV of remaining 300 payments
remaining_months_A = 300  # 25 years remaining
Balance_A = PMT_A * ((1 - (1 + r_A)**(-remaining_months_A)) / r_A)
print(f'Mortgage A balance at end of year 5: ${Balance_A:,.2f}')

# Mortgage B: $90,000 at 7%
P_B = 90000
r_B = 0.07 / 12
n_B = 360

PMT_B = P_B * (r_B * (1 + r_B)**n_B) / ((1 + r_B)**n_B - 1)
print(f'\nMortgage B monthly payment: ${PMT_B:,.2f}')

remaining_months_B = 300
Balance_B = PMT_B * ((1 - (1 + r_B)**(-remaining_months_B)) / r_B)
print(f'Mortgage B balance at end of year 5: ${Balance_B:,.2f}')

print()
print('='*60)
print('QUESTION 2: 15-Year Mortgage with Discount Points')
print('='*60)

# 2a. Monthly payment
P_2 = 200000
r_2 = 0.06 / 12
n_2 = 180  # 15 years

PMT_2 = P_2 * (r_2 * (1 + r_2)**n_2) / ((1 + r_2)**n_2 - 1)
print(f'2a. Monthly payment: ${PMT_2:,.2f}')

# 2b. APR - need to find rate that makes PV of payments = net proceeds
# Net proceeds = 200,000 - 2 points = 200,000 - 4,000 = 196,000
net_proceeds = 200000 * (1 - 0.02)
print(f'Net proceeds after 2 points: ${net_proceeds:,.2f}')

# Find APR using numpy financial
apr_monthly = npf.rate(n_2, -PMT_2, net_proceeds, 0)
apr_annual = apr_monthly * 12
print(f'2b. APR: {apr_annual*100:.4f}%')

# 2c. Effective cost if repaid at end of year 5 (month 60)
# Balance at month 60
remaining_2 = 120  # 10 years remaining
Balance_2_5yr = PMT_2 * ((1 - (1 + r_2)**(-remaining_2)) / r_2)
print(f'Balance at end of year 5: ${Balance_2_5yr:,.2f}')

# Cash flows: receive 196,000 at t=0, pay PMT for 60 months, pay balance at month 60
# Find IRR
cf = [-net_proceeds] + [PMT_2]*59 + [PMT_2 + Balance_2_5yr]
eff_rate_monthly = npf.irr(cf)
eff_rate_annual = eff_rate_monthly * 12
print(f'2c. Effective cost (APR) if repaid at year 5: {eff_rate_annual*100:.4f}%')

print()
print('='*60)
print('QUESTION 3: Mortgage Monthly Payment Calculations')
print('='*60)

# 3a. 30-year FRM, 6%, $200,000
P_3 = 200000
r_3 = 0.06 / 12
n_3 = 360

PMT_3a = P_3 * (r_3 * (1 + r_3)**n_3) / ((1 + r_3)**n_3 - 1)
print(f'3a. Monthly payment (30-yr fully amortized): ${PMT_3a:,.2f}')

# 3b. Interest-only for 5 years, then 25-year amortization
PMT_IO = P_3 * r_3  # Interest-only payment
print(f'\n3b. Interest-only payment (first 5 years): ${PMT_IO:,.2f}')

# After 5 years, balance is still $200,000, amortize over 25 years
n_3b = 300  # 25 years
PMT_3b_amort = P_3 * (r_3 * (1 + r_3)**n_3b) / ((1 + r_3)**n_3b - 1)
print(f'    Amortizing payment (remaining 25 years): ${PMT_3b_amort:,.2f}')

dollar_increase = PMT_3b_amort - PMT_IO
pct_increase = (dollar_increase / PMT_IO) * 100
print(f'    Payment increase: ${dollar_increase:,.2f} ({pct_increase:.2f}%)')

# 3c. Refinancing at 4% after 5 years
r_new = 0.04 / 12
n_new = 360  # 30-year term

# Scenario 3a: Balance after 5 years
remaining_3a = 300
Balance_3a_5yr = PMT_3a * ((1 - (1 + r_3)**(-remaining_3a)) / r_3)
print(f'\n3c. Balance at end of year 5 (scenario 3a): ${Balance_3a_5yr:,.2f}')

# New payment after refinancing
PMT_3a_refi = Balance_3a_5yr * (r_new * (1 + r_new)**n_new) / ((1 + r_new)**n_new - 1)
print(f'    New payment after refi (3a): ${PMT_3a_refi:,.2f}')
savings_3a = PMT_3a - PMT_3a_refi
print(f'    Monthly savings from refinancing (3a): ${savings_3a:,.2f}')

# Scenario 3b: Balance after 5 years is still $200,000
Balance_3b_5yr = 200000
print(f'\n    Balance at end of year 5 (scenario 3b): ${Balance_3b_5yr:,.2f}')

PMT_3b_refi = Balance_3b_5yr * (r_new * (1 + r_new)**n_new) / ((1 + r_new)**n_new - 1)
print(f'    New payment after refi (3b): ${PMT_3b_refi:,.2f}')
savings_3b = PMT_3b_amort - PMT_3b_refi
print(f'    Monthly savings from refinancing (3b): ${savings_3b:,.2f}')

print()
print('='*60)
print('QUESTION 4: Interest Rate Risk of Mortgage Loan')
print('='*60)

# Original: 30-year FRM, $100,000, 8%, purchased at par
P_4 = 100000
r_4 = 0.08 / 12
n_4 = 360

PMT_4 = P_4 * (r_4 * (1 + r_4)**n_4) / ((1 + r_4)**n_4 - 1)
print(f'Original monthly payment: ${PMT_4:,.2f}')

# 4-1a: Rate goes to 8.5%, held to full term
# New market value = PV of remaining payments at new rate
r_up = 0.085 / 12
MV_up_full = PMT_4 * ((1 - (1 + r_up)**(-360)) / r_up)
loss_4_1a = P_4 - MV_up_full
print(f'\n4-1a. Market value at 8.5% (full term): ${MV_up_full:,.2f}')
print(f'      Estimated loss: ${loss_4_1a:,.2f}')

# 4-1b: Rate goes to 8.5%, payoff at end of year 3
# Market value = PV of 36 monthly payments + PV of payoff balance at month 36
remaining_after_36 = 324  # months remaining
Balance_at_36 = PMT_4 * ((1 - (1 + r_4)**(-remaining_after_36)) / r_4)
print(f'\n      Balance at end of year 3: ${Balance_at_36:,.2f}')

# PV at new rate 8.5%
PV_payments_36 = PMT_4 * ((1 - (1 + r_up)**(-36)) / r_up)
PV_balance_36 = Balance_at_36 / (1 + r_up)**36
MV_up_3yr = PV_payments_36 + PV_balance_36
loss_4_1b = P_4 - MV_up_3yr
print(f'4-1b. Market value at 8.5% (3-year payoff): ${MV_up_3yr:,.2f}')
print(f'      Estimated loss: ${loss_4_1b:,.2f}')

# 4-1c: Which scenario has higher loss?
print(f'\n4-1c. Higher loss in: {"Full term" if loss_4_1a > loss_4_1b else "3-year payoff"}')
print('      Learning: Longer duration mortgages have higher interest rate risk.')
print('      When rates rise, holding the mortgage longer exposes the investor')
print('      to more discounting periods at the higher rate, resulting in greater loss.')

# 4-2a: Rate goes to 7.5%, held to full term
r_down = 0.075 / 12
MV_down_full = PMT_4 * ((1 - (1 + r_down)**(-360)) / r_down)
gain_4_2a = MV_down_full - P_4
print(f'\n4-2a. Market value at 7.5% (full term): ${MV_down_full:,.2f}')
print(f'      Estimated gain: ${gain_4_2a:,.2f}')

# 4-2b: Effective Duration
# Duration = - (1/P) * (dP/dy) ≈ (P_down - P_up) / (2 * P_0 * delta_y)
delta_y = 0.005  # 50 bps each way = 100 bps total spread
P_0 = 100000
eff_duration = (MV_down_full - MV_up_full) / (2 * P_0 * delta_y)
print(f'\n4-2b. Effective Duration: {eff_duration:.2f} years')

print()
print('='*60)
print('QUESTION 5: WAL (Weighted Average Life)')
print('='*60)

# Loan 1: $200,000, 6.50%, 30-year, held to maturity
P_L1 = 200000
r_L1 = 0.065 / 12
n_L1 = 360

PMT_L1 = P_L1 * (r_L1 * (1 + r_L1)**n_L1) / ((1 + r_L1)**n_L1 - 1)
print(f'Loan 1 monthly payment: ${PMT_L1:,.2f}')

# Calculate Average Life for Loan 1
# AL = sum(t * Principal_t) / Total Principal
# For each month, principal payment = PMT - interest
al_L1_numerator = 0
balance_L1 = P_L1
for t in range(1, 361):
    interest = balance_L1 * r_L1
    principal = PMT_L1 - interest
    al_L1_numerator += (t/12) * principal  # Convert months to years
    balance_L1 -= principal

AL_L1 = al_L1_numerator / P_L1
print(f'Loan 1 Average Life: {AL_L1:.2f} years')

# Loan 2: $100,000, 6.00%, 30-year amortization, payoff at end of year 5
P_L2 = 100000
r_L2 = 0.06 / 12
n_L2 = 360

PMT_L2 = P_L2 * (r_L2 * (1 + r_L2)**n_L2) / ((1 + r_L2)**n_L2 - 1)
print(f'\nLoan 2 monthly payment: ${PMT_L2:,.2f}')

# Calculate Average Life for Loan 2
al_L2_numerator = 0
balance_L2 = P_L2
for t in range(1, 61):  # Only 60 months
    interest = balance_L2 * r_L2
    principal = PMT_L2 - interest
    al_L2_numerator += (t/12) * principal
    balance_L2 -= principal

# At month 60, remaining balance is paid off
remaining_L2_60 = 300
Balance_L2_60 = PMT_L2 * ((1 - (1 + r_L2)**(-remaining_L2_60)) / r_L2)
al_L2_numerator += 5 * Balance_L2_60  # Year 5 payoff

AL_L2 = al_L2_numerator / P_L2
print(f'Loan 2 Balance at payoff (year 5): ${Balance_L2_60:,.2f}')
print(f'Loan 2 Average Life: {AL_L2:.2f} years')

# WAL of combined portfolio
# WAL = (AL_L1 * P_L1 + AL_L2 * P_L2) / (P_L1 + P_L2)
total_balance = P_L1 + P_L2
WAL = (AL_L1 * P_L1 + AL_L2 * P_L2) / total_balance
print(f'\nQuestion 5-2: Weighted Average Life (WAL) of combined loans: {WAL:.2f} years')

print()
print('='*60)
print('QUESTION 6: MBS Risk and Return Measures')
print('='*60)
print('''
Note: Questions 6-1 through 6-4 require reference to Charts 6-1, 6-2, and 6-3 
from the exam document, which contain Price/Yield tables for CUSIP 314M7GU9.

ANSWERS:

6-1: Draw Price vs Curve Shift chart
-------------------------------------
Using data from Chart 6-2 (price at par = 100), plot:
- X-axis: Curve Shift Scenarios (-300, -200, -100, 0, +100, +200, +300 bps)
- Y-axis: Price
The curve should show:
- Higher prices when rates decrease (negative shifts)
- Lower prices when rates increase (positive shifts)
- Negative convexity (curve bends downward on both ends relative to a straight line)

6-2: Contraction and Extension Risk through OAD, OAC, WAL, Life CPR
-------------------------------------------------------------------
- OAD (Option-Adjusted Duration): 
  * Decreases when rates fall (contraction) as prepayments accelerate
  * Increases when rates rise (extension) as prepayments slow
  * Contraction risk: Duration shortens when you want longer exposure (rates falling)
  * Extension risk: Duration lengthens when you want shorter exposure (rates rising)

- OAC (Option-Adjusted Convexity):
  * Typically negative for MBS due to prepayment option
  * Contraction risk: More negative convexity when rates fall
  * Extension risk: Less negative (or positive) convexity when rates rise

- WAL (Weighted Average Life):
  * Decreases when rates fall (faster prepayments)
  * Increases when rates rise (slower prepayments)
  * Shows actual expected timing of principal returns

- Life CPR (Conditional Prepayment Rate):
  * Higher when rates fall (more refinancing)
  * Lower when rates rise (less refinancing)
  * Directly measures expected prepayment speed

6-3: Why Yield remains constant across curve shifts
---------------------------------------------------
The Yield shown (5.0524%) is the YIELD TO MATURITY calculated at the BASE PRICE 
of 100 (par). This yield is a property of the bond itself when purchased at par - 
it represents the coupon rate/pass-through rate of the MBS.

When we shift the curve, we are simulating market rate changes to measure risk 
metrics (like duration and convexity). The yield shown is not the "market yield" 
at different rate scenarios - it's the original yield at purchase.

In other words, the table shows what happens to PRICE and RISK METRICS when rates 
change, but the "Yield" column is simply showing the original purchase yield for 
reference, not recalculating it for each scenario.

6-4: Price at 105 (premium) scenarios
-------------------------------------
a) WAL and Life CPR same as Chart 6-2:
   WAL and Life CPR depend on the RATE environment and prepayment expectations, 
   not on the price paid. The prepayment model uses current market rates to project 
   prepayments. Since the rate scenarios are identical, the prepayment projections 
   are identical, resulting in same WAL and Life CPR.

b) Why Yield increases when curve shifts up and decreases when curve shifts down:
   When you buy at 105 (premium), the yield-to-maturity relationship works inversely:
   - Curve shifts UP (rates rise): Prepayments slow down, so the investor holds the 
     premium bond longer, BUT in Chart 6-3, the yield shown reflects the expected 
     return given the price paid. At a premium price, slower prepayments (extension) 
     actually improve yield because the higher coupon is received longer.
   - Curve shifts DOWN (rates fall): Prepayments speed up (contraction), and the 
     premium paid is amortized faster, reducing yield.
   
   This is the classic "negative convexity" behavior of premium MBS - loses in both 
   directions but more severely when rates fall.
''')
