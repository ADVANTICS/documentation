# Platforms

## Hardware

<div class="noheader-table compact-table">
<span>iMX7 systems (ADM-CS-SECC, ADM-CS-EVCC)</span>

| * | *
|---|---
| **Compute module** | Toradex Colibri iMX7 Dual 1GB
| **Processor** | NXP i.MX 7
| **Cores** | 2 * ARM Cortex-A7 + 1 * ARM Cortex-M4F
| **Clock** | 1 GHz (A7) + 200 MHz (M4)
| **Instruction sets** | armv7l + half thumb fastmult vfp edsp thumbee neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm
| **RAM** | 1 GB DDR3
| **Flash** | 4 GB eMMC

</div>
<br/>
<div class="noheader-table compact-table">
<span>iMX6 systems (ADM-CO-CU1)</span>

| * | *
|---|---
| **Compute module** | Toradex Colibri iMX6 DualLite 512MB IT
| **Processor** | NXP i.MX 6
| **Cores** | 2 * ARM Cortex-A9
| **Clock** | 800 MHz
| **Instruction sets** | armv7l + half thumb fastmult vfp edsp thumbee neon vfpv3 tls vfpd32
| **RAM** | 512 MB DDR3
| **Flash** | 4 GB eMMC

</div>

## Software


<div class="noheader-table compact-table">

| * | *
|---|---
| **Kernel** | Linux LTS branch (5.4 currently), iMX6: Vanilla + ADC patch, iMX7: Toradex + RS485 patch
| **System** | Advantics 3.x branch, based on Buildroot 2020.11.1
| **Container** | Docker CE 19.03
| **Python** | 3.9 (system), 3.9 (container)

</div>
