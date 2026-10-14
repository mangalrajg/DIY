#!/usr/bin/env python3
"""Build the DIY shoe rack guide PDF with fpdf2."""
from fpdf import FPDF

D = "/home/hatch/workspace/shoe-rack/"
IMG = {
    "design": D + "fig1-overview.jpg",
    "pieces": D + "fig2-parts.jpg",
    "frame": D + "fig14-frame.jpg",
    "shelves": D + "fig15-shelves.jpg",
    "strips": D + "fig17-strips.jpg",
    "drillspots": D + "media-generation-drill-spots-0-e9d673c9-da65-43de-bd61-7591c41c52b0.jpg",
    "xsect": D + "fig11-screw.jpg",
    "pins": D + "fig16-pin.jpg",
    "stripsclose": D + "shelf-iso-top.jpg",
    "marking": D + "fig13-marking.jpg",
    "bottomshelf": D + "fig7-bottom.jpg",
    "cleatjoint": D + "cleat-joint.jpg",
    "cleatbottom": D + "cleat-bottom-shelf.jpg",
    "divbottom": D + "divider-cleats.jpg",
    "divtop": D + "divider-top.jpg",
    "divmid": D + "divider-middle-shelf.jpg",
    "stripsfront": D + "strips-front.jpg",
    "stripsside": D + "strips-side.jpg",
    "backstrips": D + "backstop-strips.jpg",
    "pinecut": D + "pine12-cutting.jpg",
}

IMG = {k: v.replace(D, D + "pdf_img/").replace(".webp", ".jpg") for k, v in IMG.items()}

pdf = FPDF(orientation="P", unit="mm", format="Letter")
pdf.set_auto_page_break(True, margin=18)
pdf.set_margins(15, 15, 15)
W = 215.9 - 30  # usable width

def h1(t):
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(60, 40, 20)
    pdf.multi_cell(W, 10, t)
    pdf.ln(2)

def h2(t):
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(80, 55, 25)
    pdf.cell(W, 9, t, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)

def body(t):
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(W, 6, t)
    pdf.ln(1)

def bullets(items):
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(30, 30, 30)
    for it in items:
        pdf.set_x(15)
        pdf.cell(6, 6, "-")
        pdf.multi_cell(W - 6, 6, it)
    pdf.ln(2)

def note(t):
    pdf.set_fill_color(255, 248, 230)
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(90, 70, 40)
    pdf.multi_cell(W, 6, t, fill=True)
    pdf.ln(2)
    pdf.set_text_color(30, 30, 30)

def img(key, w):
    pdf.image(IMG[key], w=w)
    pdf.ln(3)

def caption(t, fig=None):
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(100, 100, 100)
    label = f"Fig. {fig} - " if fig else ""
    pdf.multi_cell(W, 5, label + t, align="C")
    pdf.ln(2)
    pdf.set_text_color(30, 30, 30)

# ---------------- COVER ----------------
pdf.add_page()
pdf.ln(8)
h1("DIY Shoe Rack - Complete Build Guide")
pdf.set_font("Helvetica", "", 12)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(W, 7, "5 ft wide  |  4 shelves  |  3/4 in plywood  |  removable middle shelves on shelf pins")
pdf.ln(4)
img("design", 150)
caption("Front and side views with overall dimensions. The center divider is one continuous piece; "
        "six shelf boards rest on pins (two per level, one per bay). The bottom shelf is raised 1.5 in on cleats.", fig=1)
h2("What you are building")
body("A 60 in wide x 48 in tall x 12 in deep open shoe rack. Two side panels, a bottom shelf resting on cleats, "
     "top board and center divider form a rigid frame - no screw goes through the side panels, so the outside "
     "faces stay clean. Six middle-shelf boards (two per level, "
     "one in each bay) rest on metal shelf pins, so you can lift them out or change their height any time. "
     "A 2 in backstop "
     "strip on each shelf keeps shoes off your wall; a front lip keeps them from sliding off.")

# ---------------- SHOPPING LIST ----------------
pdf.add_page()
h1("Shopping List - Home Depot")
h2("Wood")
bullets([
    '2 sheets of 4x8 ft, 3/4 in plywood (sanded pine or BCX - cheapest decent option)',
    '4 pieces of 1x2 x 8 ft pine board (8 front lips at 28.5 in = 228 in, plus 4 cleats at 12 in = 48 in, plus 2 divider cleats at 8 in = 16 in; 292 in total)',
])
h2("Hardware")
bullets([
    '#8 x 1-1/4 in wood screws - one box of 100 (about 70 needed)',
    '#8 x 2 in wood screws - one small box (2 needed: divider cleats to shelf)',
    '1/4 in shelf pins - 2 packs (you need 24)',
    'Wood glue - 1 bottle',
    'Wood filler (small tub)',
    '120-grit sandpaper (a few sheets)',
    'Finish of your choice: polyurethane or paint (optional)',
])
h2("Tools")
bullets([
    'Drill (you have one) + drill/driver bits',
    'Countersink bit, or a 7/64 in bit for pilot holes',
    '1/4 in drill bit (for the shelf-pin holes)',
    'Tape measure, pencil, carpenter square',
    '2 clamps (strongly recommended for assembly)',
    "Painter's tape (to mark drill depth)",
    'Safety glasses',
])

def parts_diagram(x, y):
    sc = 1.5
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(30, 30, 30)
    pdf.set_xy(x, y)
    pdf.cell(W, 6, "Fig. 2 - Parts inventory (all bars to the same scale - check off each piece)")
    y += 8
    items = [
        ("Side panel, 47-1/4 x 12 in", 2, 47.25, 12),
        ("Top board, 60 x 12 in", 1, 60, 12),
        ("Bottom shelf, 58.5 x 12 in", 1, 58.5, 12),
        ("Middle shelf, 28.75 x 12 in (one per bay)", 8, 28.75, 12),
        ("Center divider, 45 x 12 in", 1, 45, 12),
        ("Cleat (1x2), 12 in long", 4, 12, 1.5),
        ("Divider cleat (1x2), 8 in long", 2, 8, 1.5),
        ("Backstop strip, 28.5 x 2 in", 8, 28.5, 2),
        ("Front lip (1x2), 28.5 in long", 8, 28.5, 1.5),
    ]
    for label, qty, lin, win in items:
        bw, bh = lin * sc, max(win * sc, 5)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(30, 30, 30)
        pdf.set_xy(x, y)
        pdf.cell(72, 8, f"{qty} x  {label}")
        pdf.set_fill_color(255, 250, 240)
        pdf.set_draw_color(60, 60, 60)
        pdf.rect(x + 74, y + 1, bw, bh, style="DF")
        y += max(11, bh + 4)
    return y

# ---------------- CUT LIST ----------------
pdf.add_page()
h1("Cut List - Hand This Page to the Associate")
body("Home Depot will do the big cuts on their panel saw (first cuts are usually free). "
     "Ask them to rip each 4x8 sheet into four 12 in wide strips first, then crosscut the pieces below. "
     "Their tolerance is about 1/8 in - always measure your hole positions off the ACTUAL cut pieces.")
pdf.set_font("Helvetica", "B", 11)
pdf.set_fill_color(240, 235, 225)
colw = [52, 14, 40, W - 52 - 14 - 40]
for c, t in zip(colw, ["Piece", "Qty", "Size (inches)", "Notes"]):
    pdf.cell(c, 7, t, border=1, fill=True)
pdf.ln()
rows = [
    ("Side panel", "2", '47-1/4 x 12', ""),
    ("Bottom shelf", "1", "58.5 x 12", "rests on cleats (structural)"),
    ("Middle shelf (one per bay)", "8", "28.75 x 12", "6 rest on pins (removable) + 2 spare"),
    ("Top board", "1", "60 x 12", "screwed in"),
    ("Center divider", "1", "45 x 12", "cleats + screwed from top"),
    ("Cleat (1x2)", "4", "12 in long", "cut from the 1x2 board"),
    ("Divider cleat (1x2)", "2", "8 in long", "cut from the 1x2 board"),
    ("Backstop strip", "8", "28.5 x 2", "cut from offcuts"),
    ("Front lip (1x2)", "8", "28.5 long", 'cut from the 1x2 x 8 ft board'),
]
pdf.set_font("Helvetica", "", 10)
fill = False
for r in rows:
    for c, t in zip(colw, r):
        pdf.cell(c, 6.5, t, border=1, fill=fill)
    pdf.ln()
    fill = not fill
pdf.ln(3)
note("Backstop strips: rip the leftover offcut pieces into 2 in wide strips, then cut eight 28.5 in lengths. "
     "You will have plenty of offcut material.")
pdf.add_page()
h1("Parts Inventory - Check Off Each Piece")
parts_diagram(15, pdf.get_y())
pdf.ln(2)

# ---------------- CUTTING DIAGRAMS ----------------
pdf.add_page()
h1("Cutting Diagrams - How Each Sheet Is Cut")
body("Each 4x8 sheet is first ripped into four 12 in wide strips (96 in long). Gray areas are offcuts - keep them for the backstop strips.")

def draw_sheet(x, y, title, strips, scale=1.75, fig=None):
    sheet_w = 96 * scale
    strip_h = 12 * scale
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(30, 30, 30)
    pdf.set_xy(x, y)
    pdf.cell(sheet_w, 6, (f"Fig. {fig} - " if fig else "") + title)
    y0 = y + 7
    for i, strip in enumerate(strips):
        sy = y0 + i * strip_h
        cx = x
        for label, length, off in strip:
            w = length * scale
            if off:
                pdf.set_fill_color(225, 225, 225)
            else:
                pdf.set_fill_color(255, 246, 235)
            pdf.set_draw_color(60, 60, 60)
            pdf.rect(cx, sy, w, strip_h, style="DF")
            pdf.set_font("Helvetica", "", 7)
            pdf.set_xy(cx, sy + strip_h / 2 - 2.5)
            pdf.cell(w, 5, label, align="C")
            cx += w
    return y0 + 4 * strip_h

s1 = [
    [("Top board 60\"", 60, False), ("offcut", 36, True)],
    [("Shelf 28.75\"", 28.75, False), ("Shelf 28.75\"", 28.75, False), ("Shelf 28.75\"", 28.75, False), ("offcut", 9.75, True)],
    [("Shelf 28.75\"", 28.75, False), ("Shelf 28.75\"", 28.75, False), ("Shelf 28.75\"", 28.75, False), ("offcut", 9.75, True)],
    [("Extra shelf 28.75\"", 28.75, False), ("Extra shelf 28.75\"", 28.75, False), ("spare", 38.5, True)],
]
s2 = [
    [("Side 47-1/4\"", 47.25, False), ("Side 47-1/4\"", 47.25, False)],
    [("Bottom shelf 58.5\"", 58.5, False), ("offcut", 37.5, True)],
    [("Divider 45\"", 45, False), ("offcut", 51, True)],
    [("SPARE STRIP", 96, False)],
]
x0 = 15 + (W - 96 * 1.75) / 2
y = pdf.get_y()
y = draw_sheet(x0, y, "Sheet 1 of 2", s1, fig=3) + 8
y = draw_sheet(x0, y, "Sheet 2 of 2", s2, fig=4) + 8
pdf.set_y(y)
note("Cut 2 EXTRA shelves from sheet 1's spare strip - backups in case you ever need them (no strips attached). The SPARE strip on sheet 2 is your safety net for mistakes - and a source of extra backstop strips.")
img("backstrips", 150)
caption("Backstop strips (cut at home with hand saw): rip the 36 in offcut (Sheet 1) into 2 in strips for 5 backstops, plus 3 more from the 37.5 in offcut (Sheet 2). Eight 28.5 in lengths total.", fig=5)
pdf.set_x(15)
img("pinecut", 140)
caption("1x2 cutting: Home Depot crosscuts the 28.5 in lips and 12 in cleats (all over 12 in). Cut the two 8 in divider cleats at home with your hand saw.", fig=6)

# ---------------- DRILLING GUIDE ----------------
pdf.add_page()
h1("Where to Drill - Every Plank")
body("Drill ALL holes before assembling. Two kinds of holes:")
pdf.set_font("Helvetica", "", 11)
pdf.set_fill_color(70, 130, 200)
x = pdf.get_x(); y = pdf.get_y()
pdf.circle(x + 2, y + 3, 1.6, style="F")
pdf.set_xy(x + 7, y)
pdf.cell(W - 7, 6, 'Blue circle = 1/4 in shelf-pin hole. Drill only 3/8 in deep - NEVER through the panel.',
         new_x="LMARGIN", new_y="NEXT")
pdf.set_fill_color(200, 60, 60)
x = pdf.get_x(); y = pdf.get_y()
pdf.rect(x + 0.8, y + 1.8, 2.4, 2.4, style="F")
pdf.set_xy(x + 7, y)
pdf.cell(W - 7, 6, "Red square = screw hole. Drill a pilot hole all the way through + a countersink on the outside face.",
         new_x="LMARGIN", new_y="NEXT")
pdf.set_fill_color(40, 140, 70)
x = pdf.get_x(); y = pdf.get_y()
pdf.circle(x + 2, y + 3, 1.6, style="F")
pdf.set_xy(x + 7, y)
pdf.cell(W - 7, 6, "Green circle = front-lip screw position. Driven horizontally through the lip into the shelf edge (see Fig. 12).",
         new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
note("CRITICAL: pin holes must be at the exact same height on every panel or shelves will wobble. "
     "Make a template: drill the pattern once into a scrap strip, clamp it to each panel, and drill through it as a guide. "
     "The divider sits 3/4 in higher (on top of the bottom shelf), so let the template's bottom edge hang 3/4 in BELOW "
     "the divider's bottom edge - the diagram already accounts for this.")

def panel_map(x, y, height_in, title, screw_pts, subtitle="", y_offset=0, fig=None):
    sc = 2.0
    pw, ph = 12 * sc, height_in * sc
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.set_xy(x, y)
    pdf.cell(pw, 5, (f"Fig. {fig} - " if fig else "") + title, align="C")
    if subtitle:
        pdf.set_font("Helvetica", "I", 8)
        pdf.set_xy(x, y + 5)
        pdf.cell(pw, 4, subtitle, align="C")
        y += 4
    y0 = y + 10
    pdf.set_draw_color(60, 60, 60)
    pdf.set_fill_color(255, 252, 246)
    pdf.rect(x, y0, pw, ph, style="DF")
    # pin holes: columns at 2 and 10 in, rows 6..42 step 2
    pdf.set_fill_color(70, 130, 200)
    for r in range(6, 43, 2):
        rel = r - y_offset
        if rel < 2 or rel > height_in - 2:
            continue
        for c in (2, 10):
            pdf.circle(x + c * sc, y0 + ph - rel * sc, 1.3, style="F")
    # screw holes
    pdf.set_fill_color(200, 60, 60)
    for (cx, cy) in screw_pts:
        pdf.rect(x + cx * sc - 1.2, y0 + ph - cy * sc - 1.2, 2.4, 2.4, style="F")
    # dimension label
    pdf.set_font("Helvetica", "", 8)
    pdf.set_xy(x, y0 + ph + 1)
    pdf.cell(pw, 4, '12" wide', align="C")
    return y0 + ph + 8

y = pdf.get_y()
x0 = 30
y1 = panel_map(x0, y, 47.25, "SIDE PANEL (x2)", [],
               "drill on INSIDE face", fig=7)
y2 = panel_map(x0 + 70, y, 45, "DIVIDER (x1)", [], "drill on BOTH faces", y_offset=2.25, fig=8)
pdf.set_y(max(y1, y2))
body("Side panel: pin holes only - no screw holes. The panels join the frame through the cleats (bottom shelf) "
     "and the top-board screws. "
     "Divider: pin holes on both faces, 5/16 in deep per side (so they don't meet in the middle); no screw holes on the divider itself - it is cleated to the "
     "bottom shelf and screwed from the top board.")

def topview_map(x, y, length_in, title, holes, foot, fig=None):
    sc = 2.0
    bw, bh = length_in * sc, 12 * sc
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.set_xy(x, y)
    pdf.cell(bw, 5, (f"Fig. {fig} - " if fig else "") + title, align="C")
    y0 = y + 6
    pdf.set_draw_color(60, 60, 60)
    pdf.set_fill_color(255, 252, 246)
    pdf.rect(x, y0, bw, bh, style="DF")
    for (hx, hy, kind) in holes:
        if kind == "pin":
            pdf.set_fill_color(70, 130, 200)
            pdf.circle(x + hx * sc, y0 + bh - hy * sc, 1.3, style="F")
        elif kind == "lip":
            pdf.set_fill_color(40, 140, 70)
            pdf.circle(x + hx * sc, y0 + bh, 1.6, style="F")
        else:
            pdf.set_fill_color(200, 60, 60)
            pdf.rect(x + hx * sc - 1.2, y0 + bh - hy * sc - 1.2, 2.4, 2.4, style="F")
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_xy(x, y0 + bh + 1)
    pdf.multi_cell(bw, 4, foot, align="C")
    return y0 + bh + 20

pdf.add_page()
h2("Horizontal boards (top view)")
y = pdf.get_y()
x0 = 15 + (W - 60 * 2.0) / 2
img("bottomshelf", 130)
caption("Bottom shelf top view: mark the divider center (29.25 in from each end) and the 2 cleat positions before assembly.", fig=9)
y = pdf.get_y()
y = topview_map(x0, y, 60, "TOP BOARD (x1)",
                [(1.125, 2, "screw"), (1.125, 10, "screw"), (58.875, 2, "screw"),
                 (58.875, 10, "screw"), (30, 3, "screw"), (30, 9, "screw")],
                "Drill from the TOP face: 4 screws down into the top cleats, "
                "2 down into the divider's top end (spaced front-to-back)",
                fig=10)
y = topview_map(x0, y, 28.75, "MIDDLE SHELF (x6) - one per bay",
                [(7.2, 11.625, "screw"), (14.4, 11.625, "screw"), (21.55, 11.625, "screw"),
                 (7.2, 0, "lip"), (14.4, 0, "lip"), (21.55, 0, "lip")],
                "Red squares: 3 screws UP into the backstop strip. "
                "Green circles: 3 screws horizontally through the front lip (glue it first). "
                "Two boards per level (one per bay).",
                fig=11)
pdf.set_y(y)
h2("How each joint works")
img("xsect", 130)
caption("Screw joint cross-section, drawn to scale. The screw lands in the exact middle of the 3/4 in shelf edge.", fig=12)
img("drillspots", 120)
caption("Side panel drilling drawing, drawn to scale - use the dimensions, do not scale the drawing. "
        "Drill on the INSIDE face.", fig=13)

def size_comparison(x, y):
    sc = 2.0
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(30, 30, 30)
    pdf.set_xy(x, y)
    pdf.cell(140, 6, "Fig. 14 - Side panel vs divider, drawn to the same scale")
    y0 = y + 8
    pdf.set_fill_color(255, 250, 240)
    pdf.set_draw_color(60, 60, 60)
    pdf.rect(x, y0, 12 * sc, 47.25 * sc, style="DF")
    pdf.rect(x + 40, y0 + 2.25 * sc, 12 * sc, 45 * sc, style="DF")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(30, 30, 30)
    pdf.set_xy(x, y0 + 47.25 * sc + 2)
    pdf.cell(24, 5, 'Side: 47-1/4"', align="C")
    pdf.set_xy(x + 40, y0 + 47.25 * sc + 2)
    pdf.cell(24, 5, 'Divider: 45"', align="C")
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.set_xy(x, y0 + 47.25 * sc + 8)
    pdf.multi_cell(140, 5, "The divider is 2-1/4 in shorter: the bottom shelf sits 2-1/4 in up (1.5 in cleat + 3/4 in shelf).")
    pdf.set_text_color(30, 30, 30)
    return y0 + 47.25 * sc + 22
    return y0 + 48 * sc + 22

# ---------------- ASSEMBLY ----------------
pdf.add_page()
h1("Assembly - Step by Step")

h2("Step 1 - Sand and drill everything")
size_comparison(15, pdf.get_y())
pdf.ln(2)
bullets([
    "Sand all cut edges with 120-grit sandpaper.",
    "Drill every hole using Figs. 5-9 on the previous pages. Use painter's tape on the 1/4 in bit as a depth stop: 3/8 in for the side panels, 5/16 in for the divider (it gets holes on BOTH faces, so 5/16 + 5/16 leaves a 1/8 in web).",
    "Drill pin holes BEFORE assembling - you cannot reach the inside faces afterwards.",
])
img("marking", 100)
caption("Marking the shelf heights on a side panel - measure 12, 24, and 36 in up from the bottom edge. "
        "Pin holes go every 2 in from 6 to 42 in; the full pattern is in Fig. 7.", fig=15)

h2("Step 2 - Assemble the rigid frame")
img("frame", 130)
caption("After this step: sides + cleats + bottom shelf + divider + top board are joined. Middle shelves NOT yet installed.", fig=16)
bullets([
    "Lay one side panel flat, inside face up. Run wood glue on the inside face along the bottom 1.5 in.",
    "Press a cleat (1x2 x 12 in, on edge) against the glue with its bottom flush with the panel's bottom edge. Drive 3 screws through the cleat into the panel face.",
    "Glue and screw a second cleat near the top of the panel with its top flush with the panel's top edge. Repeat both cleats on the second panel.",
    "Stand both panels upright, inside faces toward each other.",
    "Lower the bottom shelf onto the two bottom cleats. It should sit flat and level.",
    "Mark the divider center (29.25 in from either end of the shelf). Stand the divider on the mark.",
    "Glue a divider cleat (1x2 x 8 in, on edge) to each face of the divider. Drive 2 horizontal screws through each cleat into the divider face, then 1 vertical screw (2 in) down through each cleat into the shelf. The divider is now tied to the shelf - it cannot come off.",
    "Set the top board on the top cleats and divider: 4 screws down into the cleats + 2 down into the divider.",
    "Check square: measure both diagonals corner-to-corner. They must match - tap the frame until they do.",
])
img("cleatjoint", 110)
caption("A cleat joint: every screw goes into a flat face - nothing blind, nothing to miss.", fig=17)
img("cleatbottom", 110)
caption("Bottom shelf on cleats: the shelf rests on the cleats, which sit on the floor. Lift the rack and the shelf lifts with it.", fig=18)
img("divbottom", 100)
caption("Divider bottom joint: a cleat on each face - 2 horizontal screws tie each cleat to the divider, 1 vertical screw (2 in) ties each cleat to the shelf. The divider cannot come off.", fig=19)
img("divtop", 100)
caption("Divider top joint: 2 screws down through the top board into the divider, 3 in and 9 in from the front.", fig=20)

pdf.add_page()
h2("Step 3 - Drop in the middle shelves")
img("shelves", 150)
caption("After this step: all six shelf boards resting on pins (two per level). They lift straight out.", fig=21)
bullets([
    "Push 4 shelf pins into the holes at your chosen height for each board (2 on the side panel, 2 on the divider - same height on both sides).",
    "Lower each of the 6 boards onto its 4 pins - two boards per level, one in each bay, with a small gap at the divider. Done - no screws.",
    "To remove a board later, just lift it off. To change heights, move the pins to a different row of holes.",
])
img("pins", 105)
caption("Shelf pin cross-section, drawn to scale. The 1/4 in hole is 3/8 in deep and never goes through; "
        "the shelf simply rests on the pins.", fig=22)
img("divmid", 110)
caption("Middle shelves on the divider: pins go 5/16 in deep per side, leaving a 1/8 in web. Yes, 3/4 in is thick enough.", fig=23)

h2("Step 4 - Backstop strips and front lips")
img("strips", 150)
caption("After this step: every shelf has a backstop strip (shoes can't touch the wall) and a front lip (shoes can't slide off).", fig=24)
bullets([
    "Backstop strips: stand a 28.5 x 2 in strip upright (2 in tall) at the BACK edge of each shelf (8 total, one per bay). Middle boards: flip each board over first and drive 3 screws UP from underneath into the strip. Bottom shelf: drive 3 screws DOWN through the strip into the shelf - you can't reach underneath it.",
    "Front lips: run glue along the front edge of each shelf, press a 1x2 strip on, and drive 3 screws horizontally through the lip into the shelf edge.",
    "The strips also stiffen the whole rack against side-to-side wobble.",
])
img("stripsclose", 120)
caption("One shelf: screw positions (top view, red dots) and directions (isometric, red arrows). "
        "Backstop: 3 screws UP from underneath. Front lip: 3 screws horizontally into the shelf edge. "
        "Positions at 1/4, 1/2, 3/4 of the 28-1/2 in strip.", fig=25)
img("stripsfront", 130)
caption("One shelf, front view: backstop stands 2 in tall at the back edge; front lip (1x2) sticks 3/4 in above the shelf.", fig=26)
img("stripsside", 110)
caption("One shelf, side cross-section: backstop screwed UP from underneath, lip screwed horizontally into the shelf edge.", fig=27)

h2("Step 5 - Finish and place")
bullets([
    "Fill all screw holes with wood filler. Let dry, then sand smooth.",
    "Wipe off dust and apply 2 coats of polyurethane or paint.",
    "Place the rack about 1 in off the wall. If it feels tippy, screw a small L-bracket from the top board into a wall stud.",
    "Total build time after cutting: about 2 hours.",
])
h2("Troubleshooting")
bullets([
    "Shelf wobbles on pins: your pin holes are not at equal heights. Re-drill using the template trick, or shim with a washer under one pin.",
    "Plywood splits when screwing: you skipped the pilot hole. Always pilot + countersink first.",
    "Frame not square: loosen is not an option with glue - measure diagonals BEFORE the glue dries and tap into square.",
    "Shelf sags in the middle: that is what the center divider prevents. Do not skip it on a 5 ft span.",
])

pdf.output(D + "shoe-rack-build-guide.pdf")
print("PDF written:", D + "shoe-rack-build-guide.pdf")
