"""Generate publication-quality PNG figures using Python PIL."""

from config_loader import load_config, find_project_root
config = load_config()
ROOT = find_project_root()


import json, os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = str(ROOT / config["paths"]["figures_dir"])
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Try to find a usable font
def get_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

def draw_box(draw, x, y, w, h, text, color, text_color="white", font_size=14):
    """Draw a rounded rectangle with centered text."""
    draw.rectangle([x, y, x+w, y+h], fill=color, outline="black", width=2)
    font = get_font(font_size)
    # Word wrap for long text
    lines = []
    words = text.split()
    line = ""
    for word in words:
        test = line + " " + word if line else word
        bbox = draw.textbbox((0,0), test, font=font)
        if bbox[2] - bbox[0] < w - 20:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)

    total_h = len(lines) * (font_size + 4)
    start_y = y + (h - total_h) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0,0), line, font=font)
        tw = bbox[2] - bbox[0]
        draw.text((x + (w - tw)//2, start_y + i*(font_size+4)), line, fill=text_color, font=font)

def draw_arrow(draw, x1, y1, x2, y2, color="black"):
    """Draw an arrow."""
    draw.line([(x1, y1), (x2, y2)], fill=color, width=3)
    # Arrowhead
    import math
    angle = math.atan2(y2-y1, x2-x1)
    arrow_len = 12
    draw.line([
        (x2, y2),
        (x2 - arrow_len*math.cos(angle-0.5), y2 - arrow_len*math.sin(angle-0.5))
    ], fill=color, width=3)
    draw.line([
        (x2, y2),
        (x2 - arrow_len*math.cos(angle+0.5), y2 - arrow_len*math.sin(angle+0.5))
    ], fill=color, width=3)


# ============================================================
# FIGURE 1: PRISMA Flow Diagram
# ============================================================
def fig1_prisma():
    img = Image.new('RGB', (1000, 1300), 'white')
    draw = ImageDraw.Draw(img)
    title_font = get_font(20, bold=True)
    body_font = get_font(13)

    # Title
    draw.text((250, 20), "PRISMA 2020 Flow Diagram", fill="black", font=title_font)

    x_center = 500
    box_w = 700
    x = x_center - box_w//2

    # IDENTIFICATION
    y = 60
    draw_box(draw, x, y, box_w, 100,
             "IDENTIFICATION\nRecords from Europe PMC (n = 4,106)\n7 queries (2025-2026) + Year-stratified (2020-2024)",
             "#2C7BB6", "white", 13)
    draw_arrow(draw, x_center, y+100, x_center, y+135)

    # SCREENING
    y = 135
    draw_box(draw, x, y, box_w, 140,
             "SCREENING\nDeduplicated records (n = 4,106)\nExcluded: corrections, case reports, editorials (n = 267)\nTitle/abstract screened (n = 432, keyword: squamous + resistance)\nExcluded: non-lung SCC, non-squamous, no mechanism (n = 370)",
             "#D7191C", "white", 13)
    draw_arrow(draw, x_center, y+140, x_center, y+175)

    # FULL-TEXT
    y = 275
    draw_box(draw, x, y, box_w, 140,
             "FULL-TEXT ASSESSMENT\nFull-text assessed (n = 62)\nPMC Open Access: 60 (96.8%), Preprints: 2\nExcluded: laryngeal SCC (1), non-squamous NSCLC (2),\nlimited mechanism (13), redundant models (9) = 25 excluded",
             "#FDAE61", "black", 13)
    draw_arrow(draw, x_center, y+140, x_center, y+175)

    # INCLUDED
    y = 415
    draw_box(draw, x, y, box_w, 80,
             "INCLUDED\nn = 37 studies (Reviews: 8, Original: 26, SysRev/MA: 3)\nCoverage: 2020-2026",
             "#1A9641", "white", 13)

    # Side notes
    y2 = 520
    draw.text((30, y2), "Year distribution:", fill="black", font=get_font(12, bold=True))
    years_data = "2020: 5 | 2021: 12 | 2022: 13 | 2023: 4 | 2024: 8 | 2025: 11 | 2026: 9"
    draw.text((30, y2+20), years_data, fill="#555555", font=get_font(11))

    # Exclusion reasons summary
    y3 = y2 + 50
    draw.text((30, y3), "Primary exclusion reasons:", fill="black", font=get_font(12, bold=True))
    reasons = [
        "• Non-lung squamous cancers (oral/esophageal/HNSCC/cutaneous): ~180",
        "• Non-squamous NSCLC focus (adenocarcinoma): ~60",
        "• No resistance mechanism discussion: ~50",
        "• Case reports / errata / protocols: ~40",
        "• Pure prognostic models, imaging, economics: ~40",
    ]
    for i, r in enumerate(reasons):
        draw.text((30, y3+20+i*18), r, fill="#555555", font=get_font(11))

    out = os.path.join(OUTPUT_DIR, "Figure1_PRISMA.png")
    img.save(out, dpi=(300,300))
    print(f"Saved: {out}")

# ============================================================
# FIGURE 2: Three-Dimensional Resistance Framework
# ============================================================
def fig2_framework():
    img = Image.new('RGB', (1200, 900), 'white')
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((300, 15), "Three-Dimensional Framework of ICI Resistance in LUSC",
              fill="black", font=get_font(20, bold=True))

    box_w = 330
    box_h = 500
    gap = 35
    start_x = 50
    box_y = 60

    colors = ["#2C7BB6", "#D7191C", "#FDAE61"]
    titles = ["TUMOR-INTRINSIC\nRESISTANCE", "TME-MEDIATED\nRESISTANCE", "ACQUIRED\nRESISTANCE"]
    contents = [
        ["PI3K/AKT/mTOR Pathway", "KEAP1/NRF2 Activation", "p38 MAPK (TGM2-NR3C1)",
         "FGFR1/EGFR Bypass", "EMT (LAMC2-CD44 Axis)", "DNA Methylation Silencing",
         "lncRNA / circHMGB2", "Anoikis / Ferroptosis", "Neoantigen Loss / HLA↓"],
        ["T Cell Exhaustion (TOX/TCF1)", "9 Co-expressed ICPs", "M2 TAMs (ALDOA-Lactate)",
         "POSTN+ CAFs / ECM Barrier", "MDSCs (Arg-1/ROS)", "Tregs (FOXP3/CTLA-4)",
         "TGF-β / IL-6 / IL-10 Axis", "Lactic Acidosis (pH 6.0-6.5)", "Hypoxia → STING↓ / AhR↑"],
        ["Clonal Evolution (JAK1/2, B2M)", "Adenosquamous Transformation",
         "Phenotypic Plasticity", "SCLC Transformation",
         "Immunoediting", "Lineage Switch", "", "", ""]
    ]

    for col, (color, title, content) in enumerate(zip(colors, titles, contents)):
        x = start_x + col * (box_w + gap)
        # Box header
        draw.rectangle([x, box_y, x+box_w, box_y+60], fill=color, outline="black", width=2)
        # Center title text
        title_lines = title.split('\n')
        title_font = get_font(15, bold=True)
        for ti, tl in enumerate(title_lines):
            bbox = draw.textbbox((0,0), tl, font=title_font)
            tw = bbox[2] - bbox[0]
            draw.text((x+(box_w-tw)//2, box_y+8+ti*22), tl, fill="white", font=title_font)

        # Content
        draw.rectangle([x, box_y+60, x+box_w, box_y+box_h], fill="#F7F7F7", outline="black", width=2)
        item_font = get_font(12)
        for i, item in enumerate(content):
            if item:
                draw.text((x+15, box_y+75+i*42), f"• {item}", fill="black", font=item_font)

        # Bottom arrow
        arrow_y = box_y + box_h + 15
        draw_arrow(draw, x+box_w//2, arrow_y, x+box_w//2, arrow_y+35, color)

    # Convergence box
    conv_y = box_y + box_h + 55
    conv_x = 250
    conv_w = 700
    draw.rectangle([conv_x, conv_y, conv_x+conv_w, conv_y+70], fill="#333333", outline="black", width=3)
    conv_text = "CONVERGENCE & REDUNDANCY\nMultiple mechanisms coexist → Single-agent ICI insufficient → Rational combinations required"
    conv_lines = conv_text.split('\n')
    for ti, tl in enumerate(conv_lines):
        cf = get_font(14, bold=True) if ti == 0 else get_font(13)
        bbox = draw.textbbox((0,0), tl, font=cf)
        tw = bbox[2] - bbox[0]
        draw.text((conv_x+(conv_w-tw)//2, conv_y+8+ti*28), tl, fill="white", font=cf)

    # Bottom clinical implication
    clin_y = conv_y + 100
    draw.rectangle([conv_x-50, clin_y, conv_x+conv_w+50, clin_y+50], fill="#1A9641", outline="black", width=2)
    clin_text = "CLINICAL IMPLICATION: Mechanism-informed precision combination strategies based on TIME subtype"
    bbox = draw.textbbox((0,0), clin_text, font=get_font(13, bold=True))
    tw = bbox[2] - bbox[0]
    draw.text((conv_x+conv_w//2-tw//2-50, clin_y+15), clin_text, fill="white", font=get_font(13, bold=True))

    out = os.path.join(OUTPUT_DIR, "Figure2_Framework.png")
    img.save(out, dpi=(300,300))
    print(f"Saved: {out}")


# ============================================================
# FIGURE 3: EIC Diagram
# ============================================================
def fig3_eic():
    img = Image.new('RGB', (1100, 800), 'white')
    draw = ImageDraw.Draw(img)

    draw.text((280, 15), "The Exhausted Immune Class (EIC) in LUSC (28-36%)",
              fill="black", font=get_font(20, bold=True))

    # Four quadrant boxes
    quads = [
        ("T CELL EXHAUSTION", ["TOX↑, EOMES↑", "TCF1↓ (Tpex loss)", "Terminal exhaustion",
                                "Epigenetic imprinting", "PD-1 refractory"]),
        ("9 IMMUNE CHECKPOINTS", ["CTLA-4, PDCD1", "LAG-3, BTLA", "TIGIT, HAVCR2 (TIM3)",
                                   "IDO1, SIGLEC7", "VISTA"]),
        ("IMMUNOSUPPRESSIVE CELLS", ["M2 TAMs ↑", "CD4+FOXP3+ Tregs ↑",
                                      "TGF-β↑, CCL18↑", "IL-10↑", "MDSC recruitment"]),
        ("CLINICAL FEATURES", ["High TIL density", "Poor prognosis",
                                "Anti-PD-1 resistance", "PD-L1 expression ≠ response",
                                "~1/3 of patients"])
    ]

    colors = ["#D7191C", "#2C7BB6", "#FDAE61", "#1A9641"]
    qw = 480
    qh = 280
    positions = [(40, 55), (570, 55), (40, 370), (570, 370)]

    for (qx, qy), color, (title, items) in zip(positions, colors, quads):
        # Box
        draw.rectangle([qx, qy, qx+qw, qy+qh], fill="#F8F8F8", outline=color, width=3)
        # Title bar
        draw.rectangle([qx, qy, qx+qw, qy+40], fill=color, outline=color, width=2)
        tf = get_font(14, bold=True)
        bbox = draw.textbbox((0,0), title, font=tf)
        tw = bbox[2] - bbox[0]
        draw.text((qx+(qw-tw)//2, qy+10), title, fill="white", font=tf)
        # Items
        item_font = get_font(12)
        for i, item in enumerate(items):
            draw.text((qx+20, qy+55+i*35), f"• {item}", fill="black", font=item_font)

    # Center paradox text
    center_x = 550
    center_y = 335
    draw.ellipse([center_x-120, center_y-20, center_x+120, center_y+80],
                 fill="#333333", outline="black", width=2)
    ptext = "PARADOX:\nInflamed but functionally\nsuppressed immunity"
    for ti, tl in enumerate(ptext.split('\n')):
        pf = get_font(13, bold=True) if ti == 0 else get_font(12)
        bbox = draw.textbbox((0,0), tl, font=pf)
        tw = bbox[2] - bbox[0]
        draw.text((center_x-tw//2, center_y+5+ti*22), tl, fill="white", font=pf)

    # Bottom implication
    impl_y = 680
    impl_text = "→ Single-agent PD-1/PD-L1 blockade is mechanistically insufficient → Multi-checkpoint blockade required"
    draw.rectangle([50, impl_y, 1050, impl_y+50], fill="#D7191C", outline="black", width=2)
    bbox = draw.textbbox((0,0), impl_text, font=get_font(13, bold=True))
    tw = bbox[2] - bbox[0]
    draw.text((550-tw//2, impl_y+15), impl_text, fill="white", font=get_font(13, bold=True))

    out = os.path.join(OUTPUT_DIR, "Figure3_EIC.png")
    img.save(out, dpi=(300,300))
    print(f"Saved: {out}")


# ============================================================
# FIGURE 4: TIME-based Decision Framework
# ============================================================
def fig4_decision():
    img = Image.new('RGB', (1200, 750), 'white')
    draw = ImageDraw.Draw(img)

    draw.text((280, 15), "LUSC TIME-Based Therapeutic Decision Framework",
              fill="black", font=get_font(20, bold=True))

    columns = [
        ("IMMUNE-INFLAMED\n(with EIC ~30%)", "#D7191C",
         ["TILs: HIGH", "ICPs: 9 co-upregulated", "TAMs: M2 dominant",
          "Cytokines: TGF-β↑", ""],
         ["→ Multi-ICP blockade", "→ Anti-TIGIT / Anti-LAG3",
          "→ TAM reprogramming", "→ Tpex preservation"]),
        ("IMMUNE-EXCLUDED\n(stromal barrier)", "#FDAE61",
         ["TILs: Stromal only", "CAFs: POSTN+/FAP+", "ECM: Dense",
          "TAM-CAF axis active", ""],
         ["→ CAF targeting (FAPi)", "→ TGF-β blockade", "→ ECM normalization",
          "→ Chemo to deplete MDSCs"]),
        ("IMMUNE-DESERT\n(no T cells)", "#2C7BB6",
         ["TILs: ABSENT", "STING/cGAS: Suppressed", "DCs: Impaired priming",
          "MHC: Low expression", ""],
         ["→ STING agonists", "→ Oncolytic viruses", "→ Epigenetic priming",
          "→ DC vaccination"]),
    ]

    col_w = 340
    col_gap = 40
    start_x = 50
    header_h = 70
    feature_h = 200
    strategy_h = 200

    for ci, (title, color, features, strategies) in enumerate(columns):
        cx = start_x + ci * (col_w + col_gap)

        # Column header
        draw.rectangle([cx, 55, cx+col_w, 55+header_h], fill=color, outline="black", width=2)
        for ti, tl in enumerate(title.split('\n')):
            tf = get_font(14, bold=True)
            bbox = draw.textbbox((0,0), tl, font=tf)
            tw = bbox[2] - bbox[0]
            draw.text((cx+(col_w-tw)//2, 60+ti*25), tl, fill="white", font=tf)

        # Features
        fy = 55 + header_h
        draw.rectangle([cx, fy, cx+col_w, fy+feature_h], fill="#FFF5F0", outline=color, width=2)
        draw.text((cx+15, fy+10), "CHARACTERISTICS", fill=color, font=get_font(12, bold=True))
        for fi, feat in enumerate(features):
            if feat:
                draw.text((cx+20, fy+40+fi*30), f"• {feat}", fill="black", font=get_font(11))

        # Strategies
        sy = fy + feature_h
        draw.rectangle([cx, sy, cx+col_w, sy+strategy_h], fill="#F0FFF0", outline=color, width=2)
        draw.text((cx+15, sy+10), "THERAPEUTIC STRATEGY", fill=color, font=get_font(12, bold=True))
        for si, strat in enumerate(strategies):
            draw.text((cx+20, sy+40+si*30), f"{strat}", fill="#1A9641", font=get_font(11))

    # Bottom note
    note_y = 470
    draw.text((50, note_y), "NOTE: EIC = subset of immune-inflamed with terminal exhaustion | Classifications from scRNA-seq + spatial transcriptomics",
              fill="#666666", font=get_font(11))

    # Arrow showing progression
    arrow_y = 510
    draw.text((50, arrow_y), "Therapeutic Strategy Selection Flow:", fill="black", font=get_font(12, bold=True))
    draw.text((50, arrow_y+25),
              "Biopsy → Multi-omics Profiling → TIME Classification → Mechanism-Matched Combination → Dynamic ctDNA Monitoring",
              fill="#333333", font=get_font(12))

    out = os.path.join(OUTPUT_DIR, "Figure4_Decision.png")
    img.save(out, dpi=(300,300))
    print(f"Saved: {out}")


# ============================================================
# Run all
# ============================================================
if __name__ == "__main__":
    print("WARNING: generate_figures.py contains domain-specific example figures. Edit figure content before using it for a new review.")
    print("Generating figures...\n")
    fig1_prisma()
    fig2_framework()
    fig3_eic()
    fig4_decision()
    print(f"\nAll 4 figures saved to: {OUTPUT_DIR}")
