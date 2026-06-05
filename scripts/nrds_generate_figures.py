"""Generate figures and tables for NRDS Life-Course Review."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

FIG_DIR = "E:/medical-review/manuscript/figures"
os.makedirs(FIG_DIR, exist_ok=True)

# ============================================================
# Figure 1: Life-Course Framework
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('Figure 1. Life-Course Framework of NRDS Interventions', fontsize=14, fontweight='bold', pad=15)

ax.annotate('', xy=(9.5, 5.5), xytext=(0.5, 5.5), arrowprops=dict(arrowstyle='->', lw=3, color='gray'))
ax.text(5, 5.0, 'Life Course', ha='center', fontsize=11, color='gray', style='italic')

box1 = mpatches.FancyBboxPatch((0.5, 3.5), 2.5, 1.5, boxstyle="round,pad=0.1", facecolor='#FFB3BA', edgecolor='black', lw=1.5)
ax.add_patch(box1)
ax.text(1.75, 4.8, 'NICU Interventions', ha='center', fontsize=9, fontweight='bold')
ax.text(1.75, 4.3, 'ACS, PNS, Ventilation\nSurfactant, Oxygen', ha='center', fontsize=8)

box2 = mpatches.FancyBboxPatch((3.5, 3.5), 2.5, 1.5, boxstyle="round,pad=0.1", facecolor='#BAE1FF', edgecolor='black', lw=1.5)
ax.add_patch(box2)
ax.text(4.75, 4.8, 'Childhood (2-12y)', ha='center', fontsize=9, fontweight='bold')
ax.text(4.75, 4.3, 'Lung function, Asthma\nCognitive, School', ha='center', fontsize=8)

box3 = mpatches.FancyBboxPatch((6.5, 3.5), 2.5, 1.5, boxstyle="round,pad=0.1", facecolor='#BAFFC9', edgecolor='black', lw=1.5)
ax.add_patch(box3)
ax.text(7.75, 4.8, 'Adolescence (13-18y)', ha='center', fontsize=9, fontweight='bold')
ax.text(7.75, 4.3, 'FEV1 trajectory\nQoL, Education', ha='center', fontsize=8)

box4 = mpatches.FancyBboxPatch((0.5, 1.5), 2.5, 1.5, boxstyle="round,pad=0.1", facecolor='#FFFFBA', edgecolor='black', lw=1.5)
ax.add_patch(box4)
ax.text(1.75, 2.8, 'Adulthood (19-50y)', ha='center', fontsize=9, fontweight='bold')
ax.text(1.75, 2.3, 'COPD risk\nEmployment, Independence', ha='center', fontsize=8)

box5 = mpatches.FancyBboxPatch((3.5, 1.5), 5.5, 1.5, boxstyle="round,pad=0.1", facecolor='#E8E8E8', edgecolor='red', lw=2, linestyle='--')
ax.add_patch(box5)
ax.text(6.25, 2.8, 'BPD as Life-Course Mediator', ha='center', fontsize=10, fontweight='bold', color='red')
ax.text(6.25, 2.3, 'Evidence: SHORT-TERM strong | LONG-TERM absent (>2-5 years)', ha='center', fontsize=9, color='darkred')

ax.text(0.3, 1.0, 'Evidence certainty:', fontsize=8, fontweight='bold')
green_dot = plt.Circle((3.5, 0.9), 0.15, color='green')
ax.add_patch(green_dot)
ax.text(3.8, 0.8, 'HIGH (0-2 yr)', fontsize=7)
red_dot = plt.Circle((5.5, 0.9), 0.15, color='red')
ax.add_patch(red_dot)
ax.text(5.8, 0.8, 'ABSENT (>5 yr)', fontsize=7)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, 'Figure1_Framework.png'), dpi=200, bbox_inches='tight')
plt.close()
print('Figure 1 saved')

# ============================================================
# Figure 2: Evidence Gap bar chart
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 5.5))

interventions = ['Antenatal\nCorticosteroids', 'Postnatal\nCorticosteroids', 'Volume-Targeted\nVentilation',
                 'LISA\nSurfactant', 'Oxygen\nTargets', 'Quality\nof Life']

short_term = [95, 90, 85, 80, 85, 10]
long_term = [45, 30, 5, 0, 20, 5]

x = np.arange(len(interventions))
width = 0.35

bars1 = ax.bar(x - width/2, short_term, width, label='Short-term (0-2 yr)', color='#4CAF50', edgecolor='black')
bars2 = ax.bar(x + width/2, long_term, width, label='Long-term (>5 yr)', color='#F44336', edgecolor='black')

ax.set_ylabel('Evidence Certainty Score (0-100)', fontsize=11)
ax.set_title('Figure 2. Evidence Certainty: Short-Term vs Long-Term Outcomes', fontsize=13, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(interventions, fontsize=9)
ax.legend(fontsize=9, loc='upper right')
ax.set_ylim(0, 110)

for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', fontsize=8, fontweight='bold')
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', fontsize=8, fontweight='bold')

ax.axhline(y=80, color='gray', linestyle='--', alpha=0.5)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, 'Figure2_EvidenceGap.png'), dpi=200, bbox_inches='tight')
plt.close()
print('Figure 2 saved')

# ============================================================
# Table 1: Evidence Summary
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(11, 6))
ax.axis('off')

table_data = [
    ['Intervention', 'Short-term Evidence\n(Cochrane)', 'Key Long-term\nFinding', 'Long-term\nData Horizon', 'Evidence\nGap Severity'],
    ['Antenatal\nCorticosteroids', 'HIGH\n(RR 0.72 mortality)', 'No cognitive harm\nat 2-5 yr', '5 years\n(observational)', 'MODERATE'],
    ['Postnatal Steroids\n(Early Dexa)', 'HIGH\n(RR 0.72 BPD)', 'CP risk +42%\n(RR 1.42)', '18-24 months\n(Bayley)', 'HIGH'],
    ['Postnatal Steroids\n(Late Hydrocort)', 'HIGH\n(RR 0.80 BPD)', 'CP n.s. increase\n(RR 1.12)', '18-24 months\n(Bayley)', 'HIGH'],
    ['Volume-Targeted\nVentilation', 'HIGH\n(RR 0.73 death/BPD)', 'No follow-up\nbeyond discharge', 'Discharge only', 'CRITICAL'],
    ['LISA Surfactant', 'MODERATE\n(RR 0.77 death/BPD)', 'No follow-up\nat any age', '36 wk PMA only', 'CRITICAL'],
    ['Oxygen Targets\n(Low 85-89%)', 'HIGH\n(RR 0.72 ROP)', 'Mortality up at 5 yr\nneuro: n.s. diff', '5 years\n(RCT follow-up)', 'MODERATE'],
    ['Quality of Life\n(all interventions)', 'Not assessed', '8/528 papers\naddressed QoL', 'None', 'CRITICAL'],
]

table = ax.table(cellText=table_data, cellLoc='center', loc='center',
                 colWidths=[0.17, 0.17, 0.25, 0.18, 0.13])
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.6)

for i in range(5):
    table[0, i].set_facecolor('#2C3E50')
    table[0, i].set_text_props(color='white', fontweight='bold')

severity_colors = {'MODERATE': '#FFF9C4', 'HIGH': '#FFCC80', 'CRITICAL': '#FF8A80'}
for row in range(1, len(table_data)):
    sev = table_data[row][4]
    if sev in severity_colors:
        table[row, 4].set_facecolor(severity_colors[sev])

ax.set_title('Table 1. Summary of Evidence for NRDS Interventions: Short-Term and Long-Term Outcomes',
             fontsize=11, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, 'Table1_Summary.png'), dpi=200, bbox_inches='tight')
plt.close()
print('Table 1 saved')

print(f'\nAll files saved to {FIG_DIR}')
for f in sorted(os.listdir(FIG_DIR)):
    if f != '.gitkeep':
        size = os.path.getsize(os.path.join(FIG_DIR, f))
        print(f'  {f}: {size/1024:.0f} KB')
