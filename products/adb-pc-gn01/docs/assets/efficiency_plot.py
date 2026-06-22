import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Data Definition ---
data = {
    # We exclude 0% load from the plot data for better visualization, 
    # as efficiency is technically 0 at 0 power output.
    'Output Power (%)': [10, 25, 50, 75, 100],
    'Efficiency_208V (%)': [91.5, 95.0, 97.2, 98.0, 98.1],
    'Efficiency_380V (%)': [92.0, 95.5, 97.5, 98.2, 98.3],
    'Efficiency_480V (%)': [92.5, 96.0, 97.8, 98.4, 98.5]
}

df_plot = pd.DataFrame(data)

# --- Plot Generation (Publication Quality) ---

plt.figure(figsize=(10, 6))

# Plotting the three efficiency curves
plt.plot(df_plot['Output Power (%)'], df_plot['Efficiency_208V (%)'], marker='o', linestyle='-', label='Input Voltage: 208 V')
plt.plot(df_plot['Output Power (%)'], df_plot['Efficiency_380V (%)'], marker='s', linestyle='-', label='Input Voltage: 380 V')
plt.plot(df_plot['Output Power (%)'], df_plot['Efficiency_480V (%)'], marker='^', linestyle='-', label='Input Voltage: 480 V')

# Add grid and labels
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel('Output Power (% of 100 kW Rated Load)', fontsize=14)
plt.ylabel('Efficiency (%)', fontsize=14)
plt.title('ADB-PC-AC01 100 kW AC/DC Active Frontend Efficiency Map', fontsize=16)

# Set y-axis limits to clearly show the range of efficiency
plt.ylim(90, 100)
plt.xlim(0, 105)

# Add legend and customize ticks
plt.legend(fontsize=12, loc='lower right')
plt.xticks([10, 25, 50, 75, 100])
plt.yticks(np.arange(90, 100.5, 0.5))

# Annotate Peak Efficiency (for 480V) using LaTeX for formatting
plt.annotate(
    r'Peak $\eta: 98.5\%$',
    xy=(100, 98.5),
    xytext=(90, 99.3),
    arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, headwidth=5),
    fontsize=10
)

# Annotate Light Load Efficiency (for 208V)
plt.annotate(
    r'Light Load $\approx 91.5\%$',
    xy=(10, 91.5),
    xytext=(15, 90.5),
    arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, headwidth=5),
    fontsize=10
)

# Save the plot as a high-quality PNG
plt.savefig('afe_efficiency_plot.webp', dpi=300, bbox_inches='tight')
print("Plot saved successfully as 'afe_efficiency_plot.webp'")
