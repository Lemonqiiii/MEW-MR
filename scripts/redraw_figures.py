"""Redraw publication-quality figures using matplotlib/seaborn."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUT_DIR = "E:/medical-review/manuscript/figures"
os.makedirs(OUT_DIR, exist_ok=True)

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 14,
    'axes.labelsize': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.2,
})

def fig1_framework():
    """Figure 1: Three-Dimensional Framework of ICI Resistance in LUSC.
    Uses a clean, grid-based layout with regular rectangles."""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    c_tumor = '#2B83BA'; c_tme = '#D7191C'; c_acq = '#FDAE61'
    c_conv = '#333333'; c_clin = '#1A9641'

    ax.text(8, 9.7, 'Figure 1. Three-Dimensional Framework of ICI Resistance in LUSC',
            ha='center', fontsize=15, fontweight='bold')

    # Column layout
    cols = [
        {'x': 0.5, 'w': 4.5, 'color': c_tumor, 'title': 'TUMOR-INTRINSIC RESISTANCE',
         'items': [
             'PI3K/AKT/mTOR: PD-L1 up, M2 polarization',
             'KEAP1/NRF2: ROS scavenging, IFN down',
             'p38 MAPK (NR3C1-TGM2): immune evasion',
             'FGFR1/EGFR bypass: ligand-independent',
             'EMT (LAMC2-CD44): T cell exclusion',
             'DNA Methylation/HDAC: MHC silencing',
             'lncRNA/circHMGB2: anti-PD-1 resistance',
             'Anoikis/Ferroptosis: cell death defects',
             'Neoantigen loss / HLA down: immunoediting',
         ]},
        {'x': 5.7, 'w': 4.5, 'color': c_tme, 'title': 'TME-MEDIATED RESISTANCE',
         'items': [
             'T Cell Exhaustion: TOX up, TCF-1 down',
             '9 Co-expressed ICPs: CTLA-4,LAG-3,TIGIT,TIM-3',
             'M2 TAMs: ALDOA-lactate circuit',
             'CAFs (POSTN+/FAP+): ECM barrier',
             'MDSCs: Arg-1, ROS, amino acid depletion',
             'Tregs (FOXP3+): CTLA-4 transendocytosis',
             'TGF-beta/IL-6/IL-10: cytolytic suppression',
             'Lactic Acidosis (pH 6.0-6.5): T cell inhibition',
             'Hypoxia: STING down, AhR up',
         ]},
        {'x': 10.9, 'w': 4.5, 'color': c_acq, 'title': 'ACQUIRED RESISTANCE',
         'items': [
             'Clonal Evolution: JAK1/2, B2M mutations',
             'Adenosquamous Transf.: SOX2,TP63,ZEB1',
             'Phenotypic Plasticity: cytoskeletal',
             'SCLC Transformation: RB1/TP53 loss',
             'Immunoediting: neoantigen loss',
             'Lineage Plasticity: neuroendocrine switch',
             '', '', '',
         ]},
    ]

    header_h = 0.6
    item_h = 0.55
    start_y = 8.5

    for col in cols:
        x, w, color, title, items = col['x'], col['w'], col['color'], col['title'], col['items']

        # Header bar
        rect = mpatches.Rectangle((x, start_y), w, header_h, facecolor=color,
                                   edgecolor='black', linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x + w/2, start_y + header_h/2, title, ha='center', va='center',
               fontsize=9.5, fontweight='bold', color='white', zorder=3)

        # Body
        body_top = start_y - len(items) * item_h
        rect = mpatches.Rectangle((x, body_top), w, len(items)*item_h,
                                   facecolor='#FAFAFA', edgecolor=color, linewidth=1.5, zorder=1)
        ax.add_patch(rect)

        # Items
        for i, item in enumerate(items):
            if item:
                item_y = start_y - header_h - (i+1)*item_h + item_h/2
                ax.text(x + w/2, item_y, item, ha='center', va='center',
                       fontsize=7.2, color='#333333')

    # Arrows
    ax.annotate('', xy=(8, 2.8), xytext=(2.75, 3.5),
               arrowprops=dict(arrowstyle='->', color=c_tumor, lw=2.5))
    ax.annotate('', xy=(8, 2.8), xytext=(8, 3.5),
               arrowprops=dict(arrowstyle='->', color=c_tme, lw=2.5))
    ax.annotate('', xy=(8, 2.8), xytext=(13.15, 3.5),
               arrowprops=dict(arrowstyle='->', color=c_acq, lw=2.5))

    # Convergence
    rect = mpatches.Rectangle((3, 2.2), 10, 0.6, facecolor=c_conv,
                               edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(8, 2.5, 'CONVERGENCE & MECHANISTIC REDUNDANCY',
           ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    # Clinical
    rect = mpatches.Rectangle((2, 1.2), 12, 0.55, facecolor=c_clin,
                               edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(8, 1.48, 'Mechanism-informed precision combination strategies based on TIME subtype',
           ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    # Abbrev
    ax.text(8, 0.4, 'ICP: immune checkpoint; CAF: cancer-associated fibroblast; ECM: extracellular matrix; STING: stimulator of interferon genes',
           ha='center', fontsize=7, color='gray')

    path = os.path.join(OUT_DIR, "Figure2_Framework.png")
    fig.savefig(path, dpi=300, facecolor='white', edgecolor='none', bbox_inches='tight')
    plt.close(fig)
    print(f"Saved: {path}")


def table1_tumor_intrinsic():
    """Table 1: Tumor-Intrinsic Mechanisms of ICI Resistance in LUSC."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 5.5))
    ax.axis('off')

    # Title
    ax.text(0.5, 1.02, 'Table 1. Tumor-Intrinsic Mechanisms of ICI Resistance in LUSC',
           transform=ax.transAxes, ha='center', va='bottom',
           fontsize=13, fontweight='bold', color='#2B83BA')

    # Table data
    col_labels = ['Mechanism', 'Key Genes/Pathways', 'Frequency\nin LUSC', 'Effect on Immunity', 'Therapeutic Approach', 'Ref PMID']
    data = [
        ['PI3K/AKT/mTOR', 'PIK3CA ampl/mut', '30–40%', 'PD-L1 (up), M2 polarization, IL-10 (up)', 'PI3K/mTORi + ICI', '36198685'],
        ['KEAP1/NRF2', 'KEAP1 mutation', '~12%', 'ROS (down), IFN (down), ICD (down)', 'NRF2i, STING agonist', '36198685'],
        ['p38 MAPK (TGM2)', 'NR3C1 -> TGM2 -> p38', 'TBD', 'Th1 (down), immune suppression', 'TGM2 inhibitor', '41050683'],
        ['EMT (LAMC2–CD44)', 'LAMC2, CD44', 'CS3 subtype', 'T cell exclusion, ECM barrier', 'LAMC2/CD44 targeting', '38803944'],
        ['DNA Methylation', 'DNMT, CpG islands', 'Common', 'MHC class I/II silencing, ISG (down)', 'DNMTi + ICI', '35116387'],
        ['circHMGB2', 'circHMGB2 / miRNA', 'TBD', 'Anti-PD-1 resistance', 'circRNA targeting', '35525959'],
        ['Anoikis Resistance', 'S100A7/A8, SPP1', 'TBD', 'Treg/M2 enrichment', 'Anoikis sensitization', '41902322'],
        ['EGFR-TKI Resistance', 'EGFR/RAS bypass', 'EGFR overexp.', 'Intrinsic TKI resistance', 'Pan-pathway blockade', '33133263'],
    ]

    # Column widths
    col_widths = [0.15, 0.15, 0.08, 0.25, 0.17, 0.08]
    n_rows = len(data)
    n_cols = len(col_labels)

    # Header row
    header_color = '#2B83BA'
    for j, (label, w) in enumerate(zip(col_labels, col_widths)):
        x = sum(col_widths[:j]) + 0.04
        y = 0.92
        rect = mpatches.FancyBboxPatch(
            (x, y), w - 0.01, 0.06, boxstyle="round,pad=0.02",
            facecolor=header_color, edgecolor='white', linewidth=0.5)
        ax.add_patch(rect)
        ax.text(x + (w-0.01)/2, y + 0.03, label, ha='center', va='center',
               fontsize=7, fontweight='bold', color='white')

    # Data rows
    for i, row in enumerate(data):
        bg = '#F0F5FA' if i % 2 == 0 else 'white'
        for j, (cell, w) in enumerate(zip(row, col_widths)):
            x = sum(col_widths[:j]) + 0.04
            y = 0.85 - (i+1) * 0.095
            rect = mpatches.FancyBboxPatch(
                (x, y), w - 0.01, 0.085, boxstyle="round,pad=0.02",
                facecolor=bg, edgecolor='#DDDDDD', linewidth=0.3)
            ax.add_patch(rect)
            ax.text(x + (w-0.01)/2, y + 0.042, cell, ha='center', va='center',
                   fontsize=6.5, color='#333333')

    path = os.path.join(OUT_DIR, "Table2_Tumor_Intrinsic.png")
    fig.savefig(path, dpi=300, facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Saved: {path}")


def table2_tme():
    """Table 2: TME-Mediated Resistance Mechanisms and Interventions."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 6))
    ax.axis('off')

    ax.text(0.5, 1.02, 'Table 2. TME-Mediated Resistance Mechanisms and Therapeutic Interventions',
           transform=ax.transAxes, ha='center', va='bottom',
           fontsize=13, fontweight='bold', color='#D7191C')

    col_labels = ['TME Component', 'Mechanism of Resistance', 'Biomarker', 'Intervention Strategy', 'Ref PMID']
    data = [
        ['Exhausted CD8+ T cells', 'TOX up, TCF-1 down, co-expression of 9 ICPs', 'EIC signature\n(28-36% of LUSC)', 'Multi-ICP blockade\nTpex preservation', '35799269'],
        ['M2 TAMs', 'ALDOA -> lactate -> M2 polarization\nCAF–TAM co-dependency', 'CD163, CD206,\nAPOE', 'CSF1Ri, CD47 blockade\nMetabolic inhibition', '41239433'],
        ['POSTN+/FAP+ CAFs', 'ECM deposition (collagen, fibronectin)\nT cell physical exclusion', 'POSTN, FAP,\nαSMA', 'FAPi, TGF-β trap\nHedgehog antagonist', '41133013'],
        ['MDSCs', 'Arginase-1 -> arginine depletion\nROS -> TCR nitrosylation', 'CD14+HLA-DR-', 'PDE5i, CXCR2i\nChemotherapy depletion', '41133013'],
        ['Tregs (FOXP3+)', 'CTLA-4 transendocytosis\nIL-10, TGF-β, IL-35 secretion', 'FOXP3, CD25ʰi', 'Anti-CTLA-4, CCR4i\nLow-dose cyclophosphamide', '35799269'],
        ['Hypoxia', 'HIF-1α -> PD-L1 (up), VEGF (up)\nSTING pathway suppression', 'HIF-1α IHC', 'STING agonists\nHypoxia relief', '40138855'],
        ['Lactic Acidosis', 'pH 6.0–6.5 -> T cell inhibition\nM2 polarization, Treg stability', 'LDH, MCT4', 'MCT1/MCT4 inhibitors\nMetabolic reprogramming', '41239433'],
        ['IDO1 / Tryptophan', 'Kynurenine -> AhR -> Treg (up)\nGCN2 -> mTOR inhibition', 'IDO1 expression', 'IDO1 inhibitors\nTryptophan supplementation', '35799269'],
        ['Intratumoral Microbiome', 'Lactobacillus -> immunosuppression\nLactate–microbiome crosstalk', 'Microbiota\ncomposition', 'Probiotics, antibiotics\nMetabolite modulation', '40568577'],
    ]

    col_widths = [0.15, 0.28, 0.14, 0.25, 0.07]
    header_color = '#D7191C'

    for j, (label, w) in enumerate(zip(col_labels, col_widths)):
        x = sum(col_widths[:j]) + 0.04
        y = 0.92
        rect = mpatches.FancyBboxPatch(
            (x, y), w - 0.01, 0.06, boxstyle="round,pad=0.02",
            facecolor=header_color, edgecolor='white', linewidth=0.5)
        ax.add_patch(rect)
        ax.text(x + (w-0.01)/2, y + 0.03, label, ha='center', va='center',
               fontsize=7.5, fontweight='bold', color='white')

    for i, row in enumerate(data):
        bg = '#FFF5F0' if i % 2 == 0 else 'white'
        for j, (cell, w) in enumerate(zip(row, col_widths)):
            x = sum(col_widths[:j]) + 0.04
            y = 0.85 - (i+1) * 0.085
            rect = mpatches.FancyBboxPatch(
                (x, y), w - 0.01, 0.08, boxstyle="round,pad=0.02",
                facecolor=bg, edgecolor='#DDDDDD', linewidth=0.3)
            ax.add_patch(rect)
            ax.text(x + (w-0.01)/2, y + 0.04, cell, ha='center', va='center',
                   fontsize=6.5, color='#333333')

    path = os.path.join(OUT_DIR, "Table3_TME_Mechanisms.png")
    fig.savefig(path, dpi=300, facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Saved: {path}")


if __name__ == '__main__':
    print("Redrawing publication-quality figures...\n")
    fig1_framework()
    table1_tumor_intrinsic()
    table2_tme()
    print(f"\nAll 3 figures saved to: {OUT_DIR}")
