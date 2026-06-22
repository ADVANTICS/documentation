import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Data Definition ---
data = {
    'Harmonic_Order': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],
    'Magnitude_Percent_of_Fundamental': [100.0, 1.5, 1.0, 0.7, 0.4, 0.3, 0.2, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05]
}
df_harmonics = pd.DataFrame(data)

# Calculate THDi from the synthetic data for verification and annotation
harmonic_magnitudes_relative = df_harmonics[df_harmonics['Harmonic_Order'] > 1]['Magnitude_Percent_of_Fundamental']
thdi_calculated = np.sqrt(np.sum(harmonic_magnitudes_relative**2)) / 100 * 100
print(f"Calculated THDi from this data: {thdi_calculated:.2f}%")

# --- Plotting ---
fig, ax = plt.subplots(figsize=(12, 6))

# Bar chart for all harmonics
bars = ax.bar(df_harmonics['Harmonic_Order'], df_harmonics['Magnitude_Percent_of_Fundamental'], color='skyblue', width=0.8)

# Highlight fundamental (1st harmonic)
bars[0].set_color('lightcoral')
bars[0].set_label('Fundamental (1st Harmonic)')

# Annotate values for better readability
for bar in bars:
    height = bar.get_height()
    if height > 0.01 and bar.get_x() + bar.get_width()/2 != 1: 
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.1,
                f"{height:.1f}%",
                ha='center', va='bottom', fontsize=8, color='dimgray')

# Annotate THDi
ax.text(0.98, 0.90, f'Overall THDi: {thdi_calculated:.2f}%', transform=ax.transAxes,
        fontsize=12, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.8, ec='gray'))

ax.set_title('AC Input Current Harmonic Spectrum at 100% Rated Power (ADB-PC-AC01)', fontsize=16)
ax.set_xlabel('Harmonic Order', fontsize=14)
ax.set_ylabel('Magnitude (% of Fundamental Current)', fontsize=14)
ax.set_xticks(df_harmonics['Harmonic_Order'])

# KEY FIX: Setting Y-axis limit to 110% to fully display the 100% fundamental
ax.set_ylim(0, 110) 
ax.set_yticks(np.arange(0, 101, 20)) # Set ticks for the 0-100 range

ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('afe_harmonic_spectrum.webp', dpi=300, bbox_inches='tight')

print("Harmonic spectrum plot saved as 'afe_harmonic_spectrum.webp' with full fundamental visibility.")