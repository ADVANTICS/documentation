import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. System Parameters ---
P_rated = 100000  # W
V_ll = 208        # V 
f = 60            # Hz
I_rated_rms = P_rated / (np.sqrt(3) * V_ll * 1) # ~277.5 A
I_nominal_peak = I_rated_rms * np.sqrt(2) # ~392.4 A
I_inrush_target = 450.0

# --- 2. Waveform Model Parameters ---
tau_ramp = 0.050   # 50 ms time constant for soft-start ramp-up
tau_over = 0.030   # 30 ms time constant for fast decay of overshoot
K_overshoot = (I_inrush_target / I_nominal_peak) - 1

# --- 3. Time Series Generation (Creates 't', 'I_peak_envelope', and 'I_ac_inrush') ---
t_stop = 0.200 # 200 ms
t = np.linspace(0, t_stop, 1000) 

I_peak_envelope = I_nominal_peak * (1 - np.exp(-t / tau_ramp)) * (1 + K_overshoot * np.exp(-t / tau_over))
I_ac_inrush = I_peak_envelope * np.sin(2 * np.pi * f * t)

# --- 4. DataFrame Creation (Fixes the NameError for 'df_inrush') ---
df_inrush = pd.DataFrame({
    'Time (ms)': t * 1000, # Convert to milliseconds
    'AC Inrush Current (A)': I_ac_inrush
})

# --- 5. Plotting ---
plt.figure(figsize=(10, 6))

plt.plot(df_inrush['Time (ms)'], df_inrush['AC Inrush Current (A)'], label='AC Inrush Current Waveform', color='blue')
plt.plot(df_inrush['Time (ms)'], I_peak_envelope, linestyle='--', color='red', alpha=0.6, label='Current Peak Envelope')
plt.plot(df_inrush['Time (ms)'], -I_peak_envelope, linestyle='--', color='red', alpha=0.6)

# Annotations
plt.axhline(I_nominal_peak, color='gray', linestyle=':', label=f'Nominal Peak ({I_nominal_peak:.0f} A)')
plt.axvline(150, color='green', linestyle=':', label='Settling Time (150 ms)')
plt.axhline(I_inrush_target, color='orange', linestyle='--', label=f'Peak Inrush ({I_inrush_target:.0f} A)')

# Labels and Title
plt.title('ADB-PC-AC01 Soft-Start Inrush Current Waveform', fontsize=16)
plt.xlabel('Time (ms)', fontsize=14)
plt.ylabel('AC Current (Amperes)', fontsize=14)
plt.xlim(0, 200)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right')

# Save the plot
plot_file_name = 'afe_inrush_current_waveform.webp'
plt.savefig(plot_file_name, dpi=300, bbox_inches='tight')
print(f"Plot saved successfully to {plot_file_name}")