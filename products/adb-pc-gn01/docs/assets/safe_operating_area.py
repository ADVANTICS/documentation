import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Define Parameters (Updated based on operational constraints) ---
P_rated = 100000  # 100 kW
I_limit = 170     # A (Used for current limit region)
V_min_op = 650    # V (Minimum DC operating voltage)
V_max_op = 950    # V (Maximum DC operating voltage - used for nominal limit)
V_max_abs = 1000  # V (Absolute maximum system voltage, kept for context but not in SOA)

# V_min_power_limit is now fixed by V_min_op since I_limit is constant below it
I_max_at_V_min = P_rated / V_min_op # 100000 / 650 = 153.85 A. 
# Since I_limit is 170A, the power limit is active across the entire range (170A > 153.85A)

# --- 2. Generate Data for Plotting ---
# Voltage array for constant power curve (from V_min_op to V_max_op)
V_power_curve = np.linspace(V_min_op, V_max_op, 100)
I_power_curve_pos = P_rated / V_power_curve
I_power_curve_neg = -P_rated / V_power_curve

# --- 3. Plotting ---
plt.figure(figsize=(10, 8))
ax = plt.gca()

# Plot Constant Power Curve (This is the primary limit in this V range)
# The rated current of 170A is only hit below 588V, which is below V_min_op=650V.
# Therefore, the SOA is entirely defined by the 100kW constant power curve.
plt.plot(I_power_curve_pos, V_power_curve, 'b-', linewidth=2, label='Boundary')
plt.plot(I_power_curve_neg, V_power_curve, 'b-', linewidth=2)

# Plot Voltage Limits
plt.axhline(V_max_op, color='b', linestyle='-', linewidth=2)
plt.axhline(V_min_op, color='b', linestyle='-', linewidth=2)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8) # Zero current line

# Fill the Safe Operating Area (Between the curves and the voltage limits)
ax.fill_betweenx(V_power_curve, I_power_curve_neg, I_power_curve_pos, color='green', alpha=0.1, label='Safe Operating Area')

# --- 4. Annotations and Labels ---
plt.title('ADB-PC-AC01 Safe Operating Area (SOA)', fontsize=16)
plt.xlabel('DC Current (A)', fontsize=14)
plt.ylabel('DC Voltage (V)', fontsize=14)
plt.xlim(-200, 200)
# Set Y-axis view to the actual operating range plus margin
plt.ylim(600, 1000) 

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='lower left', fontsize=10)

# Annotation for Max Voltage Limit
plt.text(0, 970, f'Max DC Voltage ({V_max_op} VDC)', fontsize=10, horizontalalignment='center', color='darkblue')

# Annotation for Min Voltage Limit
plt.text(120, 630, f'Min DC Voltage ({V_min_op} VDC)', fontsize=10, horizontalalignment='center', color='darkblue')

# Annotation for Constant Power Limit
# Since I_max at 650V is 153.85A, the current is always power limited.
plt.text(0, 800, '100 kW Constant Power Limit (P = V * I)', fontsize=10, horizontalalignment='center', color='darkblue')
plt.annotate('', xy=(I_power_curve_pos[-1], V_max_op), xytext=(I_power_curve_pos[-1]-5, V_max_op),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8)) # Arrow near top right corner

# Recommended Derating Margins (Upper Left Corner)
# plt.text(-195, 990, 'Recommended Derating Margins:', fontsize=10, weight='bold', color='darkgreen')
# plt.text(-195, 965, f'- Current: 10% (±138 A max at 725V)', fontsize=9, color='darkgreen')
# plt.text(-195, 940, f'- Voltage: 5% ({950*0.95:.0f} VDC max)', fontsize=9, color='darkgreen')


plt.savefig('afe_soa_plot.webp', dpi=300, bbox_inches='tight')
print("Safe Operating Area plot saved as 'afe_soa_plot.png'")
