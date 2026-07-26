# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from weasyprint import HTML
import svgkit as K

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_HTML = os.path.join(SCRIPT_DIR, "_build_kdp_interior.html")
OUT_PDF = os.path.join(SCRIPT_DIR, "..", "My-First-Money-Adventure-KDP-Interior-DRAFT.pdf")

AUTHOR = "Dr. Vijaya Dutta"
TITLE = "My First Money Adventure"
SERIES = "Little Money Explorers — Book 1"

# Sky triads (top, mid, bottom) — three stops instead of two for a richer,
# more dimensional gradient than a flat two-color fade.
DAY_SKY = ("#7EC8F2", "#AFE0F5", "#FFF0C2")
DUSK_SKY = ("#F2965E", "#F6B98E", "#F4C9DE")
NIGHT_SKY = ("#181A3D", "#2C2A6B", "#4B4373")
DAWN_SKY = ("#F9A66C", "#F9C88E", "#AEE0F2")
GLOW_SKY = ("#FFCB4D", "#FFDF8A", "#FFEFC2")

# ---- Coordinated character palette (muted, storybook-harmonious — replaces
# earlier ad hoc/saturated hexes so every helper reads as one cohesive cast) ----
# Color-psychology palette for ages 3-5: preschoolers engage more with
# bright, saturated hues than the muted/dusty tones adults tend to prefer
# (Boyatzis & Varghese, 1994; Zentner, 2001 — young children reliably choose
# high-saturation primary/secondary colors). Each hue below is picked for
# what it should make a small child feel about that character:
PALETTE = {
    "terracotta": "#D94E1F",   # warmth + energy — the storyteller's accent color
    "sage": "#5FAE62",         # green = growth, nature, "safe to trust" (Farmer Ravi)
    "sage_deep": "#3F9E6B",    # deeper green = nurture/care (Farmer Leela + animals)
    "dusty_blue": "#3AA6D6",   # blue = calm + dependability (Driver Joseph)
    "plum": "#9B5FC0",         # purple = imagination + wonder (Teacher Fatima)
    "ink_purple": "#6E3FA3",   # deeper violet accent, paired with plum
    "mustard": "#F2B134",      # yellow/gold = cheerfulness, optimism (Tailor Suresh)
    "cream_white": "#FBF7ED",  # white = cleanliness, gentleness (Doctor Ananya)
    "burnt_orange": "#F2843A", # orange = enthusiasm, hands-on energy (Builder Karim)
    "dusty_rose": "#F0688A",   # pink/red-pink = friendliness, warmth (Shopkeeper Meena)
}

HELPERS = {
    "farmer_ravi": dict(outfit=PALETTE["sage"], accessory="straw_hat", acc_color=None, skin=K.SKIN2),
    "farmer_leela": dict(outfit=PALETTE["sage_deep"], accessory="headscarf", acc_color=PALETTE["dusty_rose"], skin=K.SKIN2),
    "driver": dict(outfit=PALETTE["dusty_blue"], accessory="cap", acc_color="#1F7FAD", skin=K.SKIN2),
    "teacher": dict(outfit=PALETTE["plum"], accessory="headscarf", acc_color=PALETTE["ink_purple"], skin=K.SKIN2),
    "tailor": dict(outfit=PALETTE["mustard"], accessory="glasses", acc_color=None, skin=K.SKIN2),
    "doctor": dict(outfit=PALETTE["cream_white"], accessory=None, acc_color=None, prop="stethoscope", skin=K.SKIN2),
    "builder": dict(outfit=PALETTE["burnt_orange"], accessory="hardhat", acc_color=None, skin=K.SKIN2),
    "shopkeeper": dict(outfit=PALETTE["dusty_rose"], accessory="glasses", acc_color=None, skin=K.SKIN2),
}

def helper(cx, cy, scale, who):
    spec = HELPERS[who]
    return K.adult(
        cx, cy, scale,
        outfit=spec["outfit"], skin=spec["skin"],
        accessory=spec.get("accessory"), acc_color=spec.get("acc_color"), prop=spec.get("prop"),
    )

STORY_TEXT = [
    "Milu loved mornings best. Sunlight danced on her windowsill, and her best friend Pico waited on her bed, wings fluttering, ready for whatever adventure today might bring.",
    "Pico was not quite a bird and not quite a toy — a fluffy little sky-blue friend who giggled, hummed, and always noticed things Milu almost missed.",
    "While hunting for a lost puzzle piece under the sofa, Milu's fingers touched something small, round, and warm. It wasn't a puzzle piece. It was a glowing golden coin.",
    "The coin trembled in her palm, humming a soft golden tune. Pico gasped. Light spilled from its edges, swirling into a shimmering doorway right there in the living room.",
    "“Where does bread even come from?” Pico wondered aloud, pointing at the warm loaf on the table. The coin flared bright gold and pulled them gently through the light.",
    "They landed in a field of golden wheat, swaying like the sea. Farmer Ravi waved his sun-browned hand. “I grow the wheat that becomes your bread,” he smiled.",
    "The wheat became flour, the flour became dough, and the dough became warm bread — sold with a smile by Shopkeeper Meena at her cheerful corner shop.",
    "Next, the coin glowed soft and white. They met Farmer Leela, gently milking her happy cows at sunrise, humming the very same tune as the coin.",
    "Beep beep! The coin led them to the bus stop, where Driver Uncle Joseph steered carefully through busy streets, waving to every rider who climbed aboard.",
    "At the cozy library, Teacher Ms. Fatima turned the pages of a story, her voice making dragons roar and stars twinkle for every listening child.",
    "Tap-tap-tap went the sewing machine. Tailor Uncle Suresh stitched bright thread into soft cotton, humming happily as Milu's favorite yellow shirt slowly took shape.",
    "In a bright white room, Doctor Ananya gently listened to a teddy bear's heartbeat with her stethoscope, just like she cares for real, wiggly children.",
    "“I built these very walls,” laughed Builder Uncle Karim, tapping a brick with his hammer. “Brick by brick, with my whole team, we made this hospital strong.”",
    "Back at Milu's own school, children sang and counted and giggled, while her teacher smiled, watering little minds like small important gardens.",
    "“This school too!” Builder Uncle Karim grinned, pointing at the sunny yellow walls. “Every brick was placed by hands that wanted you to learn and grow.”",
    "At the fruit market, Farmer Ravi's mangoes and Shopkeeper Meena's cheerful stall stood side by side — sweetness that took many hands to reach Milu's basket.",
    "Suddenly, every helper stood together — farmer, driver, teacher, tailor, doctor, builder, shopkeeper — smiling at Milu as the coin blazed brighter than the sun.",
    "“Money isn't for buying,” the coin whispered warmly. “It's a little thank-you, passed from hand to hand, for all the ways people help each other.”",
    "Milu hugged the glowing coin close to her heart. Bread, milk, buses, books, shirts, hospitals, schools, fruit — all of it was really, truly, people helping people.",
    "“Thank you!” Milu called to every helper, waving with both hands. Warm golden light bloomed around each one, like a hundred happy hugs.",
    "Home again, Milu tumbled into Mom and Dad's arms, words spilling out fast. “Everything we have,” she said, “is because someone cared enough to help.”",
    "That evening, Milu drew pictures — a wheat field, a big yellow bus, a sewing machine — one thank-you drawing for every helper she'd met.",
    "As stars filled the window, the coin's glow softened to a gentle whisper. Milu tucked it under her pillow, Pico curled beside her, both smiling sleepily.",
    "Just before sleep, the coin flickered once more. “Tomorrow,” it hummed softly, “let's discover where coins themselves come from...” Milu smiled. Another adventure was coming.",
]

def sc(uid, sky, ground, ground_y, extra):
    top, mid, bottom = sky
    bg = K.sky_ground(uid, top, bottom, ground, ground_y, sky_mid=mid)
    return bg + extra + K.vignette(700, 355, uid)

def scene_00(u):
    e = K.sun(600, 60, 34, "#FFD98A")
    e += K.window(560, 150, 110, 100, "#FFE9B8")
    e += K.bed(230, 300, 1.15, "#8ECDF0")
    e += K.milu(230, 240, 0.85)
    e += K.pico(330, 250, 0.7)
    return sc(u, DAY_SKY, "#FFF8EC", 300, e)

def scene_01(u):
    e = K.cloud(120, 60, 1.2) + K.cloud(560, 90, 0.9)
    e += K.milu(220, 300, 1.05)
    e += K.pico(400, 260, 1.5)
    return sc(u, DAY_SKY, "#FFF8EC", 300, e)

def scene_02(u):
    e = K.sofa(360, 300, 1.5, PALETTE["plum"])
    e += K.frame_portrait(600, 90, 1.0)
    e += K.coin(300, 305, 1.1, uid=u)
    e += K.milu(230, 300, 0.85)
    e += K.pico(160, 290, 0.6)
    return sc(u, DAY_SKY, "#FFF8EC", 300, e)

def scene_03(u):
    e = K.coin(420, 150, 2.1, uid=u)
    e += K.milu(300, 320, 1.05, hold_coin=False)
    e += K.pico(180, 300, 0.75)
    return sc(u, GLOW_SKY, "#FFF3D6", 300, e)

def scene_04(u):
    e = '<rect x="60" y="230" width="580" height="70" fill="#C9A46A"/>'
    e += K.bread_loaf(520, 225, 1.3)
    e += K.coin(230, 150, 1.3, uid=u)
    e += K.milu(230, 300, 0.85)
    e += K.pico(300, 270, 0.6)
    return sc(u, GLOW_SKY, "#FFF3D6", 300, e)

def scene_05(u):
    e = K.sun(600, 55, 30)
    e += K.wheat_row(20, 680, 300, 22)
    e += K.bird(150, 60, 1.1) + K.bird(200, 90, 0.9) + K.bird(500, 70, 1.0)
    e += helper(430, 300, 1.05, "farmer_ravi")
    e += K.milu(180, 310, 0.8)
    e += K.pico(120, 290, 0.6)
    return sc(u, DAWN_SKY, "#E8C468", 300, e)

def scene_06(u):
    e = K.bookshelf(560, 300, 0.9)  # reused as shelf of goods
    e += K.market_stall(300, 300, 1.0, color="#FF9E80")
    e += K.bread_loaf(280, 265, 0.9)
    e += helper(230, 300, 0.95, "shopkeeper")
    e += K.milu(430, 310, 0.8)
    e += K.pico(490, 290, 0.6)
    return sc(u, DAY_SKY, "#FFF3D6", 300, e)

def scene_07(u):
    e = K.cow(320, 300, 1.1)
    e += helper(180, 305, 1.0, "farmer_leela")
    e += K.milu(520, 310, 0.8)
    e += K.pico(570, 290, 0.6)
    e += K.bird(460, 70, 1.0)
    return sc(u, DUSK_SKY, "#CDE7C7", 300, e)

def scene_08(u):
    e = K.road(300, 55)
    e += K.bus(360, 300, 1.05)
    e += K.milu(120, 320, 0.8)
    e += K.pico(70, 300, 0.6)
    return sc(u, DAY_SKY, "#FFF8EC", 300, e)

def scene_09(u):
    e = K.bookshelf(580, 260, 1.0)
    e += helper(300, 300, 1.0, "teacher")
    e += K.milu(180, 315, 0.72)
    e += K.pico(130, 300, 0.5)
    e += K.milu(400, 320, 0.62)
    return sc(u, DAY_SKY, "#FFF3D6", 300, e)

def scene_10(u):
    e = K.fabric_bolts(560, 300, 1.0)
    e += K.sewing_machine(340, 300, 1.1)
    e += helper(200, 300, 1.0, "tailor")
    e += K.milu(460, 320, 0.75)
    e += K.pico(500, 300, 0.55)
    return sc(u, DAY_SKY, "#FFF3D6", 300, e)

def scene_11(u):
    e = K.teddy_bear(500, 300, 1.3)
    e += helper(260, 300, 1.0, "doctor")
    e += K.milu(360, 320, 0.72)
    e += K.pico(410, 300, 0.5)
    return sc(u, ("#BEE8D3", "#EAF6EF", "#FFFFFF"), "#DFF2E6", 300, e)

def scene_12(u):
    e = K.brick_wall(250, 300, 300, 130, "#E0836B")
    e += helper(500, 300, 1.05, "builder")
    e += K.milu(560, 320, 0.7)
    e += K.pico(600, 300, 0.5)
    return sc(u, DAY_SKY, "#FFF8EC", 300, e)

def scene_13(u):
    e = helper(120, 300, 0.95, "teacher")
    kids_x = [280, 350, 420, 490]
    for i, kx in enumerate(kids_x):
        e += K.milu(kx, 320, 0.5) if i % 2 == 0 else K.pico(kx, 300, 0.45)
    return sc(u, DAY_SKY, "#FFF3D6", 300, e)

def scene_14(u):
    e = K.building(320, 300, 260, 140, PALETTE["mustard"], n_windows=3, roof=PALETTE["ink_purple"])
    e += helper(560, 300, 1.0, "builder")
    e += K.milu(100, 320, 0.75)
    e += K.pico(150, 300, 0.55)
    return sc(u, DAY_SKY, "#B7E4C7", 300, e)

def scene_15(u):
    e = K.market_stall(240, 300, 1.1, color=PALETTE["mustard"])
    e += K.fruit_basket(240, 265, 1.1)
    e += helper(430, 305, 0.95, "farmer_ravi")
    e += helper(510, 305, 0.95, "shopkeeper")
    e += K.milu(600, 320, 0.72)
    e += K.pico(340, 300, 0.5)
    return sc(u, DAY_SKY, "#FFF3D6", 300, e)

def scene_16(u):
    e = K.coin(350, 90, 1.7, uid=u)
    order = ["farmer_ravi", "farmer_leela", "driver", "teacher", "tailor", "doctor", "builder", "shopkeeper"]
    xs = [40, 100, 160, 220, 480, 540, 600, 660]
    for who, hx in zip(order, xs):
        e += helper(hx, 322, 0.4, who)
    e += K.milu(310, 325, 0.85)
    e += K.pico(400, 312, 0.55)
    return sc(u, GLOW_SKY, "#FFE9B8", 300, e)

def scene_17(u):
    e = K.coin(350, 110, 2.3, uid=u)
    e += K.milu(350, 320, 1.05)
    return sc(u, GLOW_SKY, "#FFE9B8", 300, e)

def scene_18(u):
    e = K.coin(350, 130, 1.6, uid=u, glow=True)
    e += K.milu(350, 320, 1.0)
    e += K.pico(450, 305, 0.6)
    icons = ["bread", "milk", "bus", "book", "shirt", "hospital", "school", "fruit"]
    import math
    for i, kind in enumerate(icons):
        a = (2 * math.pi * i / len(icons)) - math.pi / 2
        ix = 350 + 260 * math.cos(a)
        iy = 130 + 90 * math.sin(a)
        iy = max(40, min(iy, 300))
        e += K.mini_icon(kind, ix, iy, 0.8)
    return sc(u, GLOW_SKY, "#FFF3D6", 320, e)

def scene_19(u):
    e = ""
    import math
    for i in range(7):
        a = 0.3 + i * 0.35
        gx = 80 + i * 85
        gy = 90 + (i % 3) * 20
        e += K.coin(gx, gy, 0.4, uid=f"{u}{i}", glow=True)
    e += K.milu(350, 320, 1.05)
    return sc(u, DAY_SKY, "#B7E4C7", 320, e)

def scene_20(u):
    e = K.sofa(560, 300, 1.1, PALETTE["plum"])
    e += K.frame_portrait(80, 90, 1.0)
    e += K.adult(230, 305, 1.0, outfit=PALETTE["dusty_rose"], skin=K.SKIN2)
    e += K.adult(420, 305, 1.0, outfit=PALETTE["dusty_blue"], skin=K.SKIN2)
    e += K.milu(325, 322, 0.75)
    e += K.pico(370, 300, 0.5)
    return sc(u, DAY_SKY, "#FFF8EC", 300, e)

def scene_21(u):
    e = K.table_simple(340, 300, 1.3)
    icons = ["bread", "bus", "shirt"]
    for i, kind in enumerate(icons):
        e += K.mini_icon(kind, 560, 90 + i * 60, 1.0)
    e += K.milu(280, 320, 0.85)
    e += K.pico(220, 300, 0.55)
    return sc(u, DUSK_SKY, "#FFF3D6", 300, e)

def scene_22(u):
    e = K.stars(u, [(60, 40, 6), (150, 70, 5), (610, 50, 6), (560, 100, 4), (250, 40, 4)])
    e += K.moon(600, 70, 26)
    e += K.bed(340, 320, 1.3, "#8ECDF0")
    e += K.milu(300, 260, 0.75)
    e += K.pico(400, 280, 0.6)
    e += K.coin(340, 255, 0.6, uid=u, glow=True)
    return sc(u, NIGHT_SKY, "#2C2A52", 300, e)

def scene_23(u):
    e = K.stars(u, [(80, 50, 5), (600, 60, 6), (520, 110, 4)])
    e += K.coin(420, 160, 2.6, uid=u)
    e += f'<circle cx="420" cy="160" r="10" fill="none" stroke="#8a5a1a" stroke-width="2"/>'
    e += K.milu(220, 320, 1.0)
    return sc(u, NIGHT_SKY, "#2C2A52", 300, e)

SCENE_FUNCS = [scene_00, scene_01, scene_02, scene_03, scene_04, scene_05, scene_06, scene_07,
               scene_08, scene_09, scene_10, scene_11, scene_12, scene_13, scene_14, scene_15,
               scene_16, scene_17, scene_18, scene_19, scene_20, scene_21, scene_22, scene_23]

def illo_scene(idx):
    uid = f"s{idx}"
    inner = SCENE_FUNCS[idx](uid)
    return f'<div class="illo-frame-outer"><div class="illo-frame">{K.scene_svg(uid, inner)}</div></div>'

# --------------------------------------------------------------- MAZE (SVG)
GRID = 5
CELL = 64
MARGIN = 24
path = []
for r in range(GRID):
    cols = range(GRID) if r % 2 == 0 else range(GRID - 1, -1, -1)
    for c in cols:
        path.append((r, c))
open_edges = set()
for i in range(len(path) - 1):
    a, b = path[i], path[i + 1]
    open_edges.add(frozenset([a, b]))

def cell_xy(r, c):
    return MARGIN + c * CELL, MARGIN + r * CELL

svg_lines = []
size = MARGIN * 2 + GRID * CELL
svg_lines.append(f'<rect x="{MARGIN}" y="{MARGIN}" width="{GRID*CELL}" height="{GRID*CELL}" fill="none" stroke="#3a2f2a" stroke-width="4"/>')
for r in range(GRID):
    for c in range(GRID):
        x, y = cell_xy(r, c)
        if c < GRID - 1 and frozenset([(r, c), (r, c + 1)]) not in open_edges:
            svg_lines.append(f'<line x1="{x+CELL}" y1="{y}" x2="{x+CELL}" y2="{y+CELL}" stroke="#3a2f2a" stroke-width="4" stroke-linecap="round"/>')
        if r < GRID - 1 and frozenset([(r, c), (r + 1, c)]) not in open_edges:
            svg_lines.append(f'<line x1="{x}" y1="{y+CELL}" x2="{x+CELL}" y2="{y+CELL}" stroke="#3a2f2a" stroke-width="4" stroke-linecap="round"/>')

hx, hy = cell_xy(0, 0)
ex, ey = cell_xy(GRID - 1, GRID - 1)
hcx, hcy = hx + CELL / 2, hy + CELL / 2
ecx, ecy = ex + CELL / 2, ey + CELL / 2
svg_lines.append(f'<circle cx="{hcx}" cy="{hcy}" r="20" fill="#FFD98A" stroke="#C99A2E" stroke-width="3"/>')
svg_lines.append(f'<rect x="{hcx-9}" y="{hcy-2}" width="18" height="13" fill="none" stroke="#8a5a1a" stroke-width="2.2"/>')
svg_lines.append(f'<path d="M {hcx-12} {hcy-2} L {hcx} {hcy-13} L {hcx+12} {hcy-2} Z" fill="none" stroke="#8a5a1a" stroke-width="2.2" stroke-linejoin="round"/>')
svg_lines.append(f'<circle cx="{ecx}" cy="{ecy}" r="20" fill="#FF9E80" stroke="#C2410C" stroke-width="3"/>')
svg_lines.append(f'<path d="M {ecx-11} {ecy+6} q -1 -15 11 -15 q 12 0 11 15 q -1 6 -11 6 q -10 0 -11 -6 Z" fill="none" stroke="#8a2a12" stroke-width="2.2" stroke-linejoin="round"/>')
svg_lines.append(f'<path d="M {ecx-5} {ecy-6} L {ecx-3} {ecy+2} M {ecx} {ecy-8} L {ecx+1} {ecy+3} M {ecx+5} {ecy-6} L {ecx+6} {ecy+2}" stroke="#8a2a12" stroke-width="1.6"/>')
svg_lines.append(f'<text x="{hcx}" y="{hy-8}" font-size="11" text-anchor="middle" fill="#8a5a1a" stroke="none">HOME</text>')
svg_lines.append(f'<text x="{ecx}" y="{ey+CELL+18}" font-size="11" text-anchor="middle" fill="#8a2a12" stroke="none">BAKERY</text>')
MAZE_SVG = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">' + "".join(svg_lines) + "</svg>"

# ------------------------------------------------------------ COLORING PAGE
COLORING_SVG = """
<svg width="480" height="500" viewBox="0 0 480 500" xmlns="http://www.w3.org/2000/svg" stroke="#2a2a2a" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path d="M30 460 q210 30 420 0" stroke-width="3.5"/>
  <circle cx="240" cy="90" r="50"/>
  <circle cx="240" cy="90" r="32" stroke-width="3"/>
  <path d="M240 66 a24 24 0 0 1 0 48" stroke-width="3"/>
  <path d="M195 68 q45 -30 90 0" stroke-width="2.5"/>
  <path d="M195 112 q45 30 90 0" stroke-width="2.5"/>
  <path d="M240 145 L240 175" stroke-width="3"/>
  <ellipse cx="135" cy="330" rx="62" ry="54"/>
  <circle cx="112" cy="310" r="7" fill="#2a2a2a"/>
  <circle cx="158" cy="310" r="7" fill="#2a2a2a"/>
  <path d="M124 332 q11 10 22 0" stroke-width="3"/>
  <path d="M74 330 q-22 -6 -30 10 q19 9 32 -2" />
  <path d="M196 330 q22 -6 30 10 q-19 9 -32 -2" />
  <ellipse cx="112" cy="378" rx="11" ry="15"/>
  <ellipse cx="158" cy="378" rx="11" ry="15"/>
  <path d="M108 366 q27 20 54 0" stroke-width="3"/>
  <path d="M112 300 l-10 -16 M158 300 l10 -16" stroke-width="2.5"/>
  <circle cx="330" cy="300" r="66"/>
  <circle cx="286" cy="250" r="22"/>
  <circle cx="374" cy="250" r="22"/>
  <path d="M280 233 l-15 -20" stroke-width="4"/>
  <path d="M380 233 l15 -20" stroke-width="4"/>
  <circle cx="308" cy="293" r="6.5" fill="#2a2a2a"/>
  <circle cx="352" cy="293" r="6.5" fill="#2a2a2a"/>
  <path d="M308 320 q22 18 44 0" stroke-width="3"/>
  <path d="M264 362 q66 64 132 0 l-10 96 q-56 22 -112 0 z"/>
  <ellipse cx="292" cy="466" rx="17" ry="10"/>
  <ellipse cx="368" cy="466" rx="17" ry="10"/>
</svg>
"""

# ------------------------------------------------------------------- BUILD
sections = []

def section(cls, kicker, title, inner):
    sections.append(f"""
    <section class="section {cls}">
      {f'<div class="kicker">{kicker}</div>' if kicker else ''}
      {f'<h1>{title}</h1>' if title else ''}
      {inner}
    </section>""")

# 1. TITLE PAGE — illustrated hero
hero = K.sky_ground("hero", "#FFCB4D", "#FFE9B8", "#FFD98A", 300, 700, 420, sky_mid="#FFDD8C")
hero += K.sun(620, 70, 36)
hero += K.coin(350, 100, 2.1, uid="hero")
hero += K.milu(250, 350, 1.15)
hero += K.pico(480, 335, 0.85)
hero += K.vignette(700, 420, "hero")
title_hero = f'<div class="hero-frame">{K.scene_svg("hero", hero, 700, 420)}</div>'
section("title first-section", "", "", f"""
  <div class="title-wrap">
    {title_hero}
    <div class="title-series">{SERIES}</div>
    <h1 class="title-main">{TITLE}</h1>
    <div class="title-rule"></div>
    <div class="title-byline">Written by {AUTHOR}</div>
    <div class="title-byline">Illustrated by <span class="todo">[Illustrator name — to be added]</span></div>
  </div>
""")

# 2. COPYRIGHT PAGE
section("copyright", "", "", f"""
  <div class="copyright-wrap">
    <p>{TITLE}<br/>{SERIES}</p>
    <p>Text copyright &copy; 2026 {AUTHOR}<br/>
    Illustrations copyright &copy; 2026 <span class="todo">[Illustrator name]</span></p>
    <p>All rights reserved. No part of this book may be reproduced, stored, or
    transmitted in any form without written permission from the copyright
    holder, except for brief quotations used in reviews.</p>
    <p>This is a work of fiction. Any resemblance to real persons is coincidental.</p>
    <p>Recommended for ages 3&ndash;5.<br/>First Edition, 2026.</p>
    <p>Also in this series: <em>My First Coin Adventure</em> (Book 2)</p>
  </div>
""")

# 3. DEDICATION
ded_art = K.sky_ground("ded", "#FFCB4D", "#FFF3D6", "#FFD98A", 130, 700, 170, sky_mid="#FFE0A0")
ded_art += K.coin(350, 85, 1.4, uid="ded")
section("dedication", "", "", f"""
  <div class="dedication-wrap">
    <div class="dedication-art">{K.scene_svg("ded", ded_art, 700, 170)}</div>
    <p>For every child learning that the world runs on kindness &mdash;<br/>
    and every grown-up who shows them how.</p>
  </div>
""")

# 4-27: STORY PAGES
divider_svg = K.scene_svg("div", K.coin(30, 30, 0.55, uid="div", glow=False), 60, 60)
for i, text in enumerate(STORY_TEXT):
    lead, _, rest = text.partition(" ")
    styled_text = f'<span class="lead-word">{lead}</span> {rest}'
    section("story", "", "", f"""
      {illo_scene(i)}
      <div class="divider">
        <span class="divider-line"></span>
        <span class="divider-coin">{divider_svg}</span>
        <span class="divider-line"></span>
        <span class="page-tag">PAGE {i+4}</span>
      </div>
      <div class="text-card"><p class="story-text">{styled_text}</p></div>
    """)

# 28: HELPING CHART — visual infographic
HELPER_ICON_SPEC = [
    ("bread", "Farmer &amp; Shopkeeper", "farmer_ravi"),
    ("milk", "Farmer", "farmer_leela"),
    ("bus", "Driver", "driver"),
    ("book", "Teacher", "teacher"),
    ("shirt", "Tailor", "tailor"),
    ("hospital", "Doctor &amp; Builder", "doctor"),
    ("school", "Teacher &amp; Builder", "teacher"),
    ("fruit", "Farmer &amp; Shopkeeper", "shopkeeper"),
]
cards = []
for kind, who, who_key in HELPER_ICON_SPEC:
    mini = K.scene_svg(f"chart{kind}", K.mini_icon(kind, 30, 30, 1.0), 60, 60)
    avatar = K.scene_svg(f"av{kind}", helper(30, 62, 0.42, who_key), 60, 68)
    cards.append(f"""
    <div class="chart-card">
      <div class="chart-icons"><span class="mini">{mini}</span><span class="plus">+</span><span class="mini">{avatar}</span></div>
      <div class="chart-label">{who}</div>
      <div class="chart-box">&#9744;</div>
    </div>""")
section("activity", "PAGE 28", "The Helping Chart", f"""
  <p class="activity-intro">Can you remember who helped make each thing? Check the box once you spot each helper!</p>
  <div class="chart-grid">{''.join(cards)}</div>
""")

# 29: THANK YOU CARD + DRAW YOUR HELPER
tyou_art = K.scene_svg("tyou", K.coin(350, 60, 1.0, uid="tyou") + K.milu(280, 110, 0.55) + K.pico(400, 100, 0.4), 700, 130)
section("activity", "PAGE 29", "Say Thank You", f"""
  <div class="small-art">{tyou_art}</div>
  <p class="activity-intro">Think of someone who helps you and your family every day. Write (or ask a grown-up to help you write) a thank-you note, then draw them below.</p>
  <div class="card-box">
    <p>Dear ______________________,</p>
    <p>Thank you for ______________________.</p>
    <p>Love, ______________________ &#9825;</p>
  </div>
  <div class="draw-box"><span class="draw-label">Draw your helper here</span></div>
""")

# 30: COLORING PAGE
section("activity coloring", "PAGE 30", "Color It In!", f"""
  <div class="coloring-frame">{COLORING_SVG}</div>
""")

# 31: MAZE
section("activity", "PAGE 31", "Help Milu Reach the Bakery!", f"""
  <div class="maze-frame">{MAZE_SVG}</div>
""")

# 32: MATCHING GAME — with icons
MATCH_SPEC = [
    ("Farmer", "farmer_ravi", "bread", "Bread / Fruit"),
    ("Driver", "driver", "bus", "Bus Ride"),
    ("Teacher", "teacher", "book", "Book"),
    ("Tailor", "tailor", "shirt", "Shirt"),
    ("Doctor", "doctor", "hospital", "Hospital Care"),
    ("Builder", "builder", "school", "School / Hospital"),
]
rows = []
for name, who_key, kind, made in MATCH_SPEC:
    av = K.scene_svg(f"m{name}", helper(30, 62, 0.42, who_key), 60, 68)
    ic = K.scene_svg(f"i{name}", K.mini_icon(kind, 30, 30, 1.0), 60, 60)
    rows.append(f'<tr><td><span class="row-icon">{av}</span> {name}</td><td class="dots">&#8226;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;</td><td>{made} <span class="row-icon">{ic}</span></td></tr>')
section("activity", "PAGE 32", "Match the Helper to What They Made", f"""
  <table>
    <tr><th>Helper</th><th></th><th>What They Made</th></tr>
    {''.join(rows)}
  </table>
  <p class="activity-intro">Draw a line connecting each helper to what they made.</p>
""")

css = """
/* @page margin (not body padding) is what's used for the page-content
   inset: body is one long fragmented box across all 32 pages, and per the
   CSS Fragmentation spec, a fragmented box's padding only paints on its
   FIRST and LAST fragments -- so body padding here would silently vanish
   on pages 2-31, breaking every "bleed to page edge" negative margin on
   every page but the first. @page margin/background apply per-page. */
@page { size: 8.5in 8.5in; margin: 0.55in 0.6in 0.6in 0.6in; background: #FBF3E3; }
* { box-sizing: border-box; }
body {
  font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
  color: #2a2320; font-size: 12pt; line-height: 1.5;
}
.section { page-break-before: always; position: relative; }
.section.first-section { page-break-before: avoid; }
.kicker {
  position: absolute; top: 0.28in; right: 0.6in;
  font-size: 7.5pt; letter-spacing: 1.2px; color: #B8894A;
  background: #FFFDF8; border: 1pt solid #E8D8B8; border-radius: 10pt;
  padding: 2pt 9pt;
}
h1 {
  font-family: 'DejaVu Serif', serif; font-weight: bold;
  font-size: 16pt; color: #A8481A; margin: 0 0 0.2in 0;
  padding-bottom: 0.09in; border-bottom: 2pt solid #EAD9B4;
}
/* back-matter/activity pages get a teal identity, distinct from the
   story's terracotta, so the reader feels the section change */
.activity h1 { color: #2E7D68; border-bottom-color: #BEDDD3; }
.activity .kicker { color: #2E7D68; border-color: #BEDDD3; }
.activity .divider-line, .story .divider-line { background: #DEC9A0; }

.title-wrap { text-align: center; }
.hero-frame {
  margin: -0.55in -0.6in 0.2in -0.6in;
  border-radius: 0 0 32px 32px; overflow: hidden;
  box-shadow: 0 6pt 16pt rgba(58,47,42,0.22);
}
.hero-frame svg { display: block; width: 100%; height: auto; }
.title-series {
  font-size: 10.5pt; letter-spacing: 2px; text-transform: uppercase;
  color: #8C6BB5; margin: 0.1in 0 0.08in 0; font-weight: bold;
}
.title-main {
  font-family: 'DejaVu Serif', serif; font-weight: bold;
  font-size: 30pt; color: #C2410C; margin: 0 0 0.05in 0;
  border-bottom: none; padding-bottom: 0;
}
.title-rule { width: 1.6in; height: 2pt; background: #EAD9B4; margin: 0 auto 0.3in auto; }
.title-byline { font-size: 11pt; color: #4a3d33; margin: 0.06in 0; }

.copyright-wrap, .dedication-wrap { font-size: 10pt; color: #4a3d33; }
.copyright-wrap { padding-top: 0.7in; }
.copyright-wrap p { margin: 0.14in 0; }
.dedication-wrap { text-align: center; padding-top: 0.2in; }
.dedication-art { margin-bottom: 0.35in; border-radius: 18px; overflow: hidden; box-shadow: 0 4pt 12pt rgba(58,47,42,0.14); }
.dedication-art svg { display: block; width: 100%; height: auto; }
.dedication-wrap p {
  font-family: 'DejaVu Serif', serif; font-style: italic;
  font-size: 14pt; color: #5a3d24; line-height: 1.6;
}
.todo { color: #b23b3b; font-style: italic; }

/* Story illustrations bleed to the full page width (not just the text
   margins) so the picture dominates the page — young children engage with
   the art, not the surrounding whitespace. A rainbow gradient "frame" ring
   (instead of a flat gold line) makes it feel like a bright picture-book
   plate rather than a document figure. */
.illo-frame-outer {
  margin: -0.55in -0.6in 0.22in -0.6in;
  padding: 7pt;
  border-radius: 0 0 20px 20px;
  background: linear-gradient(135deg, #FFCB4D 0%, #F0688A 35%, #9B5FC0 68%, #3AA6D6 100%);
  box-shadow: 0 10pt 22pt rgba(58,47,42,0.24);
  overflow: hidden;
}
.illo-frame { border-radius: 0 0 14px 14px; overflow: hidden; box-shadow: 0 0 0 4pt #FFFDF8 inset; }
.illo-frame svg { display: block; width: 100%; height: auto; }

.divider { display: flex; align-items: center; justify-content: center; margin: 0 0 0.14in 0; position: relative; }
.divider-line { flex: 1; max-width: 0.9in; height: 1pt; background: #DEC9A0; }
.divider-coin { width: 38px; height: 38px; margin: 0 0.14in; flex-shrink: 0; }
.divider-coin svg { display: block; width: 100%; height: 100%; }
.page-tag {
  position: absolute; right: 0; top: 50%; transform: translateY(-50%);
  font-size: 7.5pt; letter-spacing: 1.2px; color: #B8894A;
  background: #FFFDF8; border: 1pt solid #E8D8B8; border-radius: 10pt;
  padding: 2pt 9pt;
}

.text-card {
  background: linear-gradient(180deg, #FFFFFF 0%, #FFFCF3 100%);
  border-radius: 16px; padding: 0.18in 0.32in;
  box-shadow: 0 3pt 10pt rgba(58,47,42,0.08);
}
.story-text {
  font-family: 'DejaVu Serif', serif;
  font-size: 16.5pt; line-height: 1.5; color: #3a2f2a; margin: 0;
}
.story-text .lead-word { color: #D94E1F; font-weight: bold; }

.activity-intro { font-size: 11pt; color: #4a3d33; margin-bottom: 0.15in; }
.small-art { border-radius: 14px; overflow: hidden; margin-bottom: 0.15in; box-shadow: 0 3pt 10pt rgba(58,47,42,0.12); }
.small-art svg { display: block; width: 100%; height: auto; }

table { width: 100%; border-collapse: collapse; margin: 0.12in 0; font-size: 10.5pt; box-shadow: 0 2pt 8pt rgba(58,47,42,0.06); }
th { background: #F3E6CE; text-align: left; padding: 0.08in 0.1in; border: 1pt solid #e8d8b8; font-family: 'DejaVu Serif', serif; }
td { padding: 0.09in 0.1in; border: 1pt solid #eee1c9; vertical-align: middle; background: #FFFDF8; }
.dots { text-align: center; color: #cbb89a; }
.row-icon svg { width: 26px; height: 26px; vertical-align: middle; }

.card-box { border: 2px solid #E07856; border-radius: 14px; padding: 0.16in 0.25in; margin-bottom: 0.15in; font-size: 12pt; background: #FFFDF8; box-shadow: 0 2pt 8pt rgba(58,47,42,0.07); }
.card-box p { margin: 0.12in 0; border-bottom: 1pt dotted #cbb89a; }
.draw-box { border: 2px dashed #cdbfa8; border-radius: 14px; height: 1.9in; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 0.12in; background: #FFFDF8; }
.draw-label { color: #b3a58c; font-size: 9pt; }
.coloring-frame, .maze-frame {
  display: flex; justify-content: center; align-items: center; margin-top: 0.15in;
  background: #FFFDF8; border-radius: 18px; padding: 0.2in; box-shadow: 0 2pt 8pt rgba(58,47,42,0.06);
}

.chart-grid { display: flex; flex-wrap: wrap; gap: 0.14in; justify-content: space-between; }
.chart-card { width: 47%; border: 2px solid #E8D8B8; border-radius: 14px; padding: 0.12in; display: flex; align-items: center; gap: 0.1in; background: #FFFDF8; box-shadow: 0 2pt 6pt rgba(58,47,42,0.06); }
.chart-icons { display: flex; align-items: center; gap: 0.04in; }
.chart-icons .mini svg { width: 34px; height: 34px; display: block; }
.chart-icons .plus { color: #cbb89a; font-size: 10pt; }
.chart-label { flex: 1; font-size: 9.5pt; color: #4a3d33; }
.chart-box { font-size: 14pt; color: #2E7D68; }
"""

html_doc = f"""<!doctype html>
<html><head><meta charset="utf-8">
<title>{TITLE}</title>
<meta name="author" content="{AUTHOR}">
<style>{css}</style></head>
<body>{''.join(sections)}</body></html>"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_doc)

HTML(filename=OUT_HTML).write_pdf(OUT_PDF)
print("Wrote", OUT_PDF)
