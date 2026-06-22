import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Data Definition (10% to 100% load for plotting) ---
data = {
    'Output Power (%)': [10, 25, 50, 75, 100],
    'Power Factor (PF)': [0.90, 0.98, 0.992, 0.995, 0.997],
    'THDi (%)': [15.0, 4.5, 3.0, 2.5, 2.0]
}
df_plot = pd.DataFrame(data)

# --- Plot Generation ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('ADB-PC-AC01 Power Factor and THDi vs. Load', fontsize=16)

# --- Subplot 1: Power Factor ---
axes[0].plot(df_plot['Output Power (%)'], df_plot['Power Factor (PF)'], marker='o', color='C0')
# FINAL FIX: Using Unicode characters (≥) instead of MathText (\ge)
axes[0].axhline(y=0.99, color='red', linestyle='--', label='Constraint: PF ≥ 0.99')
axes[0].set_xlabel('Output Power (%)', fontsize=12)
axes[0].set_ylabel('Power Factor (PF)', fontsize=12)
axes[0].set_title('Power Factor vs. Load', fontsize=14)
axes[0].set_ylim(0.85, 1.0)
axes[0].set_xlim(0, 105)
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend(loc='lower right')
axes[0].set_xticks([10, 25, 50, 75, 100])

# --- Subplot 2: THDi ---
axes[1].plot(df_plot['Output Power (%)'], df_plot['THDi (%)'], marker='s', color='C1')
# FINAL FIX: Using Unicode characters (≤) instead of MathText (\le)
axes[1].axhline(y=5.0, color='red', linestyle='--', label='Constraint: THDi ≤ 5%')
axes[1].set_xlabel('Output Power (%)', fontsize=12)
axes[1].set_ylabel('THDi (%)', fontsize=12)
axes[1].set_title('Total Harmonic Distortion (THDi) vs. Load', fontsize=14)
axes[1].set_ylim(0, 20)
axes[1].set_xlim(0, 105)
axes[1].grid(True, linestyle='--', alpha=0.6)
axes[1].legend(loc='upper right')
axes[1].set_xticks([10, 25, 50, 75, 100])

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('afe_pf_thdi_plots.webp', dpi=300, bbox_inches='tight')
print("Combined plot saved successfully as 'afe_pf_thdi_plots.webp'")