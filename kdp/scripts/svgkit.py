# -*- coding: utf-8 -*-
"""Reusable flat-vector illustration kit for the picture book scenes."""

SKIN = "#E8B888"
SKIN2 = "#C68C53"
INK = "#3a2f2a"
BLUSH = "#F79A85"

# Color-psychology leads for the two hero characters (ages 3-5 respond more
# to bright, saturated hues than muted/pastel ones): Milu is warm coral-red —
# energy, warmth, "look at me" — since she's the one the child follows.
# Pico is bright sky blue — calm, trustworthy, a safe companion color that
# doesn't compete with Milu for attention.
MILU_CORAL = "#FF6F5E"
PICO_BLUE = "#4FC3E8"

_UID_COUNTER = [0]
def _uid():
    _UID_COUNTER[0] += 1
    return f"u{_UID_COUNTER[0]}"

def sky_ground(uid, sky_top, sky_bottom, ground_color, ground_y=250, w=700, h=355, sky_mid=None):
    gid = f"sky_{uid}"
    ggid = f"grnd_{uid}"
    vgid = f"vig_{uid}"
    gr2id = f"grnd2_{uid}"
    ground_glow = _shade(ground_color, 0.22)
    mid_stop = f'<stop offset="0.55" stop-color="{sky_mid}"/>' if sky_mid else ""
    return f"""
    <defs>
      <linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="{sky_top}"/>
        {mid_stop}
        <stop offset="1" stop-color="{sky_bottom}"/>
      </linearGradient>
      <linearGradient id="{ggid}" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.30"/>
        <stop offset="0.18" stop-color="#FFFFFF" stop-opacity="0"/>
        <stop offset="1" stop-color="#000000" stop-opacity="0.05"/>
      </linearGradient>
      <linearGradient id="{gr2id}" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="{ground_glow}"/>
        <stop offset="1" stop-color="{ground_color}"/>
      </linearGradient>
      <radialGradient id="{vgid}" cx="0.5" cy="0.42" r="0.75">
        <stop offset="0.6" stop-color="#000000" stop-opacity="0"/>
        <stop offset="1" stop-color="#3a2f2a" stop-opacity="0.10"/>
      </radialGradient>
    </defs>
    <rect x="0" y="0" width="{w}" height="{h}" fill="url(#{gid})"/>
    <rect x="0" y="{ground_y}" width="{w}" height="{h-ground_y}" fill="url(#{gr2id})"/>
    <rect x="0" y="{ground_y}" width="{w}" height="{h-ground_y}" fill="url(#{ggid})"/>
    """

def vignette(w=700, h=355, uid="v"):
    vgid = f"vigo_{uid}_{_uid()}"
    return f"""<defs><radialGradient id="{vgid}" cx="0.5" cy="0.45" r="0.72">
      <stop offset="0.62" stop-color="#000000" stop-opacity="0"/>
      <stop offset="1" stop-color="#2b2010" stop-opacity="0.16"/>
    </radialGradient></defs>
    <rect x="0" y="0" width="{w}" height="{h}" fill="url(#{vgid})"/>"""

def soft_shadow(cx, cy, rx, ry=None, opacity=0.30):
    ry = ry if ry is not None else rx * 0.34
    gid = f"shadow_{_uid()}"
    return f"""<defs><radialGradient id="{gid}">
      <stop offset="0" stop-color="#241a10" stop-opacity="{opacity}"/>
      <stop offset="0.7" stop-color="#241a10" stop-opacity="{opacity*0.5:.2f}"/>
      <stop offset="1" stop-color="#241a10" stop-opacity="0"/>
    </radialGradient></defs>
    <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="url(#{gid})"/>"""

def lin_grad(color_top, color_bottom, x1="0", y1="0", x2="0", y2="1"):
    """Returns (defs_svg, gradient_id) for a 2-stop linear gradient."""
    gid = f"lg_{_uid()}"
    defs = f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"><stop offset="0" stop-color="{color_top}"/><stop offset="1" stop-color="{color_bottom}"/></linearGradient>'
    return defs, gid

def _shade(hexcolor, factor):
    hexcolor = hexcolor.lstrip("#")
    if len(hexcolor) != 6:
        return hexcolor if hexcolor.startswith == "#" else f"#{hexcolor}"
    r, g, b = int(hexcolor[0:2], 16), int(hexcolor[2:4], 16), int(hexcolor[4:6], 16)
    if factor >= 0:
        r = r + (255 - r) * factor
        g = g + (255 - g) * factor
        b = b + (255 - b) * factor
    else:
        r = r * (1 + factor)
        g = g * (1 + factor)
        b = b * (1 + factor)
    r, g, b = [max(0, min(255, int(c))) for c in (r, g, b)]
    return f"#{r:02x}{g:02x}{b:02x}"

def outfit_fill(base_color):
    """Returns (defs, fill_url) — a soft top-light-to-base vertical gradient."""
    top = _shade(base_color, 0.35)
    defs, gid = lin_grad(top, base_color)
    return f"<defs>{defs}</defs>", f"url(#{gid})"

def sun(cx, cy, r, color="#FFD98A", rays=True):
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="0.9"/>'
    if rays:
        import math
        segs = []
        for i in range(8):
            a = i * math.pi / 4
            x1, y1 = cx + math.cos(a) * (r + 6), cy + math.sin(a) * (r + 6)
            x2, y2 = cx + math.cos(a) * (r + 16), cy + math.sin(a) * (r + 16)
            segs.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="4" stroke-linecap="round" opacity="0.7"/>')
        out += "".join(segs)
    return out

def cloud(cx, cy, scale=1.0, color="#FFFDF8"):
    s = scale
    return f"""<g opacity="0.85">
      <ellipse cx="{cx}" cy="{cy}" rx="{28*s}" ry="{16*s}" fill="{color}"/>
      <ellipse cx="{cx-22*s}" cy="{cy+4*s}" rx="18*s" ry="12*s" fill="{color}"/>
      <ellipse cx="{cx+24*s}" cy="{cy+5*s}" rx="20*s" ry="13*s" fill="{color}"/>
    </g>""".replace("18*s", str(18*s)).replace("20*s", str(20*s)).replace("13*s", str(13*s))

def moon(cx, cy, r=26, color="#FFF3D6"):
    return f'<path d="M {cx-r*0.4} {cy-r} a {r} {r} 0 1 0 0 {2*r} a {r*0.75} {r*0.75} 0 1 1 0 {-2*r} z" fill="{color}"/>'

def stars(uid, positions, color="#FFF3D6"):
    out = []
    for (x, y, sz) in positions:
        out.append(f'<path d="M{x} {y-sz} L{x+sz*0.3} {y-sz*0.3} L{x+sz} {y} L{x+sz*0.3} {y+sz*0.3} L{x} {y+sz} L{x-sz*0.3} {y+sz*0.3} L{x-sz} {y} L{x-sz*0.3} {y-sz*0.3} Z" fill="{color}"/>')
    return "".join(out)

def coin(cx, cy, scale=1.0, uid="c", glow=True):
    s = scale
    gid = f"coinglow_{uid}_{_uid()}"
    bgid = f"coinbev_{uid}_{_uid()}"
    glow_html = ""
    if glow:
        glow_html = f"""
        <defs><radialGradient id="{gid}"><stop offset="0" stop-color="#FFF3C4" stop-opacity="0.95"/><stop offset="1" stop-color="#FFD98A" stop-opacity="0"/></radialGradient></defs>
        <circle cx="{cx}" cy="{cy}" r="{62*s}" fill="url(#{gid})"/>
        """
    return f"""<g>
      {glow_html}
      <defs><radialGradient id="{bgid}" cx="0.35" cy="0.3" r="0.8">
        <stop offset="0" stop-color="#FFF3B0"/>
        <stop offset="0.55" stop-color="#F7C948"/>
        <stop offset="1" stop-color="#DDA429"/>
      </radialGradient></defs>
      <ellipse cx="{cx}" cy="{cy+27*s}" rx="{22*s}" ry="{6*s}" fill="#241a10" opacity="0.12"/>
      <circle cx="{cx}" cy="{cy}" r="{26*s}" fill="url(#{bgid})" stroke="#C99A2E" stroke-width="{2.5*s}"/>
      <circle cx="{cx}" cy="{cy}" r="{17*s}" fill="none" stroke="#C99A2E" stroke-width="{1.5*s}" opacity="0.8"/>
      <path d="M {cx} {cy-11*s} a {6*s} {6*s} 0 0 1 0 {12*s}" stroke="#C99A2E" stroke-width="{1.5*s}" fill="none"/>
      <ellipse cx="{cx-9*s}" cy="{cy-10*s}" rx="{8*s}" ry="{4*s}" fill="#FFFFFF" opacity="0.35" transform="rotate(-28 {cx-9*s} {cy-10*s})"/>
    </g>"""

def milu(cx, cy, scale=1.0, hold_coin=False):
    """cx,cy = ground point between feet. Geometry is strictly top-to-bottom:
    head (y=-92) -> tunic shoulders (y=-58) -> tunic hem (y=+8) -> feet (y=+14)."""
    s = scale
    def y(v): return cy + v * s
    def x(v): return cx + v * s
    coin_bit = coin(x(44), y(-150), 0.5, uid=f"m{int(cx)}{int(cy)}", glow=False) if hold_coin else ""
    tunic_defs, tunic_fill = outfit_fill(MILU_CORAL)
    head_defs, head_fill = outfit_fill(SKIN)
    shadow = soft_shadow(x(0), y(20), 30 * s, 9 * s, 0.24)
    return f"""<g>
      {tunic_defs}{head_defs}
      {shadow}
      <path d="M {x(-24)} {y(-58)} L {x(24)} {y(-58)} L {x(35)} {y(8)} Q {x(0)} {y(20)} {x(-35)} {y(8)} Z" fill="{tunic_fill}" stroke="{INK}" stroke-width="{1.2*s}" stroke-opacity="0.4"/>
      <ellipse cx="{x(-15)}" cy="{y(14)}" rx="{13*s}" ry="{8*s}" fill="#3a2f2a"/>
      <ellipse cx="{x(15)}" cy="{y(14)}" rx="{13*s}" ry="{8*s}" fill="#3a2f2a"/>
      <circle cx="{x(0)}" cy="{y(-92)}" r="{32*s}" fill="{head_fill}"/>
      <circle cx="{x(-30)}" cy="{y(-118)}" r="{12*s}" fill="#2b2320"/>
      <circle cx="{x(30)}" cy="{y(-118)}" r="{12*s}" fill="#2b2320"/>
      <path d="M {x(-30)} {y(-128)} l {-6*s} {-8*s}" stroke="#F2C94C" stroke-width="{3*s}" stroke-linecap="round"/>
      <path d="M {x(30)} {y(-128)} l {6*s} {-8*s}" stroke="#F2C94C" stroke-width="{3*s}" stroke-linecap="round"/>
      <ellipse cx="{x(-19)}" cy="{y(-84)}" rx="{6.5*s}" ry="{4.2*s}" fill="{BLUSH}" opacity="0.55"/>
      <ellipse cx="{x(19)}" cy="{y(-84)}" rx="{6.5*s}" ry="{4.2*s}" fill="{BLUSH}" opacity="0.55"/>
      <circle cx="{x(-12)}" cy="{y(-92)}" r="{3.4*s}" fill="{INK}"/>
      <circle cx="{x(12)}" cy="{y(-92)}" r="{3.4*s}" fill="{INK}"/>
      <circle cx="{x(-13.2)}" cy="{y(-93.2)}" r="{1*s}" fill="#FFFFFF" opacity="0.85"/>
      <circle cx="{x(10.8)}" cy="{y(-93.2)}" r="{1*s}" fill="#FFFFFF" opacity="0.85"/>
      <path d="M {x(-9)} {y(-80)} q {9*s} {8*s} {18*s} 0" stroke="{INK}" stroke-width="{2*s}" fill="none" stroke-linecap="round"/>
      <ellipse cx="{x(-10)}" cy="{y(-118)}" rx="{9*s}" ry="{5*s}" fill="#FFFFFF" opacity="0.16"/>
      {coin_bit}
    </g>"""

def pico(cx, cy, scale=1.0):
    s = scale
    def y(v): return cy + v * s
    def x(v): return cx + v * s
    body_defs, body_fill = outfit_fill(PICO_BLUE)
    wing_color = _shade(PICO_BLUE, -0.18)
    shadow = soft_shadow(x(0), y(30), 26 * s, 8 * s, 0.22)
    return f"""<g>
      {body_defs}
      {shadow}
      <ellipse cx="{x(-14)}" cy="{y(22)}" rx="{5*s}" ry="{7*s}" fill="#F2C94C"/>
      <ellipse cx="{x(14)}" cy="{y(22)}" rx="{5*s}" ry="{7*s}" fill="#F2C94C"/>
      <path d="M {x(-30)} {y(-14)} q {-14*s} {-4*s} -{20*s} {6*s} q {12*s} {6*s} {20*s} -{2*s}" fill="{wing_color}"/>
      <path d="M {x(30)} {y(-14)} q {14*s} {-4*s} {20*s} {6*s} q {-12*s} {6*s} -{20*s} -{2*s}" fill="{wing_color}"/>
      <ellipse cx="{x(0)}" cy="{y(-10)}" rx="{30*s}" ry="{26*s}" fill="{body_fill}"/>
      <ellipse cx="{x(-11)}" cy="{y(-22)}" rx="{10*s}" ry="{5*s}" fill="#FFFFFF" opacity="0.2"/>
      <ellipse cx="{x(-15)}" cy="{y(-2)}" rx="{6*s}" ry="{4*s}" fill="{BLUSH}" opacity="0.5"/>
      <ellipse cx="{x(15)}" cy="{y(-2)}" rx="{6*s}" ry="{4*s}" fill="{BLUSH}" opacity="0.5"/>
      <circle cx="{x(-11)}" cy="{y(-16)}" r="{3.6*s}" fill="{INK}"/>
      <circle cx="{x(11)}" cy="{y(-16)}" r="{3.6*s}" fill="{INK}"/>
      <circle cx="{x(-12)}" cy="{y(-17.2)}" r="{1*s}" fill="#FFFFFF" opacity="0.85"/>
      <circle cx="{x(9.8)}" cy="{y(-17.2)}" r="{1*s}" fill="#FFFFFF" opacity="0.85"/>
      <path d="M {x(-6)} {y(-4)} q {6*s} {5*s} {12*s} 0" stroke="{INK}" stroke-width="{1.6*s}" fill="none" stroke-linecap="round"/>
      <path d="M {x(-18)} {y(10)} q {18*s} {14*s} {36*s} 0" fill="{MILU_CORAL}"/>
    </g>"""

# accessory drawers keyed by name; each returns svg using head center (hx,hy) and scale s
def _acc_cap(hx, hy, s, color):
    return f'<path d="M {hx-22*s} {hy-6*s} a {22*s} {22*s} 0 0 1 {44*s} 0 z" fill="{color}"/><rect x="{hx-6*s}" y="{hy-8*s}" width="{30*s}" height="{7*s}" rx="{3*s}" fill="{color}"/>'

def _acc_hat_straw(hx, hy, s, color="#E8C468"):
    return f'<ellipse cx="{hx}" cy="{hy-4*s}" rx="{34*s}" ry="{9*s}" fill="{color}" stroke="#B98F2E" stroke-width="{1.5*s}"/><ellipse cx="{hx}" cy="{hy-14*s}" rx="{18*s}" ry="{13*s}" fill="{color}" stroke="#B98F2E" stroke-width="{1.5*s}"/>'

def _acc_headscarf(hx, hy, s, color):
    return f'<path d="M {hx-26*s} {hy} q {-4*s} {-40*s} {26*s} {-40*s} q {30*s} 0 {26*s} {40*s} q {-8*s} {-16*s} -{26*s} {-16*s} q {-18*s} 0 -{26*s} {16*s} z" fill="{color}"/>'

def _acc_hardhat(hx, hy, s, color="#F2A22B"):
    return f'<path d="M {hx-24*s} {hy-2*s} a {24*s} {20*s} 0 0 1 {48*s} 0 z" fill="{color}" stroke="#B9700F" stroke-width="{1.5*s}"/><rect x="{hx-26*s}" y="{hy-4*s}" width="{52*s}" height="{5*s}" rx="{2*s}" fill="{color}"/>'

def _acc_glasses(hx, hy, s):
    return f'<circle cx="{hx-10*s}" cy="{hy}" r="{7*s}" fill="none" stroke="{INK}" stroke-width="{1.6*s}"/><circle cx="{hx+10*s}" cy="{hy}" r="{7*s}" fill="none" stroke="{INK}" stroke-width="{1.6*s}"/><line x1="{hx-3*s}" y1="{hy}" x2="{hx+3*s}" y2="{hy}" stroke="{INK}" stroke-width="{1.6*s}"/>'

def _acc_stethoscope(cx, cy, s, color="#5FB0DE"):
    return f'<path d="M {cx-16*s} {cy-70*s} q 0 {24*s} {16*s} {24*s} q {16*s} 0 {16*s} -{24*s}" fill="none" stroke="{color}" stroke-width="{3*s}"/><circle cx="{cx}" cy="{cy-44*s}" r="{5*s}" fill="{color}"/>'

def adult(cx, cy, scale=1.0, outfit="#8ECDF0", skin=SKIN2, accessory=None, acc_color=None, prop=None):
    """Generic helper adult. cx,cy = ground point between feet."""
    s = scale
    def y(v): return cy + v * s
    def x(v): return cx + v * s
    hx, hy = x(0), y(-128)
    acc_svg = ""
    if accessory == "cap":
        acc_svg = _acc_cap(hx, hy, s, acc_color or "#3E6FA0")
    elif accessory == "straw_hat":
        acc_svg = _acc_hat_straw(hx, hy, s)
    elif accessory == "headscarf":
        acc_svg = _acc_headscarf(hx, hy, s, acc_color or "#8C6BB5")
    elif accessory == "hardhat":
        acc_svg = _acc_hardhat(hx, hy, s)
    glasses_svg = _acc_glasses(hx, hy, s) if accessory == "glasses" else ""
    stetho_svg = _acc_stethoscope(x(0), y(-30), s) if prop == "stethoscope" else ""
    outfit_defs, outfit_url = outfit_fill(outfit)
    skin_defs, skin_url = outfit_fill(skin)
    shadow = soft_shadow(x(0), y(26), 34 * s, 10 * s, 0.26)
    return f"""<g>
      {outfit_defs}{skin_defs}
      {shadow}
      <path d="M {x(-28)} {y(-92)} L {x(28)} {y(-92)} L {x(42)} {y(10)} Q {x(0)} {y(24)} {x(-42)} {y(10)} Z" fill="{outfit_url}" stroke="{INK}" stroke-width="{1.4*s}" stroke-opacity="0.5"/>
      <ellipse cx="{x(-18)}" cy="{y(16)}" rx="{16*s}" ry="{9*s}" fill="{INK}"/>
      <ellipse cx="{x(18)}" cy="{y(16)}" rx="{16*s}" ry="{9*s}" fill="{INK}"/>
      <circle cx="{hx}" cy="{hy}" r="{30*s}" fill="{skin_url}"/>
      <ellipse cx="{hx-9*s}" cy="{hy+9*s}" rx="{6*s}" ry="{4*s}" fill="{BLUSH}" opacity="0.45"/>
      <ellipse cx="{hx+9*s}" cy="{hy+9*s}" rx="{6*s}" ry="{4*s}" fill="{BLUSH}" opacity="0.45"/>
      <circle cx="{hx-11*s}" cy="{hy+2*s}" r="{3.2*s}" fill="{INK}"/>
      <circle cx="{hx+11*s}" cy="{hy+2*s}" r="{3.2*s}" fill="{INK}"/>
      <circle cx="{hx-12.2*s}" cy="{hy+0.8*s}" r="{0.9*s}" fill="#FFFFFF" opacity="0.85"/>
      <circle cx="{hx+9.8*s}" cy="{hy+0.8*s}" r="{0.9*s}" fill="#FFFFFF" opacity="0.85"/>
      <path d="M {hx-8*s} {hy+12*s} q {8*s} {7*s} {16*s} 0" stroke="{INK}" stroke-width="{2*s}" fill="none" stroke-linecap="round"/>
      {acc_svg}
      {glasses_svg}
      {stetho_svg}
    </g>"""

# ---- props -----------------------------------------------------------

def wheat_row(x0, x1, y, n=10, color="#E8C468"):
    import random
    rnd = random.Random(int(x0) + int(y))
    out = []
    for i in range(n):
        px = x0 + (x1 - x0) * i / (n - 1) + rnd.uniform(-6, 6)
        h = rnd.uniform(34, 48)
        out.append(f'<line x1="{px:.1f}" y1="{y}" x2="{px:.1f}" y2="{y-h:.1f}" stroke="{color}" stroke-width="3"/>')
        out.append(f'<ellipse cx="{px:.1f}" cy="{y-h:.1f}" rx="5" ry="9" fill="{color}"/>')
    return "".join(out)

def bird(cx, cy, scale=1.0, color="#8a7a6a"):
    s = scale
    return f'<path d="M {cx-10*s} {cy} q {10*s} {-10*s} {10*s} 0 q 0 {-10*s} {10*s} 0" fill="none" stroke="{color}" stroke-width="{2.2*s}" stroke-linecap="round"/>'

def cow(cx, cy, scale=1.0):
    s = scale
    return f"""<g>
      {soft_shadow(cx, cy+34*s, 50*s, 12*s, 0.20)}
      <ellipse cx="{cx}" cy="{cy}" rx="{46*s}" ry="{28*s}" fill="#FFFDF8" stroke="{INK}" stroke-width="2"/>
      <ellipse cx="{cx-24*s}" cy="{cy-8*s}" rx="{10*s}" ry="{8*s}" fill="#3a2f2a" opacity="0.85"/>
      <ellipse cx="{cx+14*s}" cy="{cy+8*s}" rx="{12*s}" ry="{9*s}" fill="#3a2f2a" opacity="0.85"/>
      <circle cx="{cx-44*s}" cy="{cy-14*s}" r="{16*s}" fill="#FFFDF8" stroke="{INK}" stroke-width="2"/>
      <ellipse cx="{cx-58*s}" cy="{cy-22*s}" rx="{5*s}" ry="{8*s}" fill="#FFFDF8" stroke="{INK}" stroke-width="1.5"/>
      <circle cx="{cx-50*s}" cy="{cy-16*s}" r="{1.8*s}" fill="{INK}"/>
      <rect x="{cx-40*s}" y="{cy+22*s}" width="{6*s}" height="{16*s}" fill="#FFFDF8" stroke="{INK}" stroke-width="1.5"/>
      <rect x="{cx+30*s}" y="{cy+22*s}" width="{6*s}" height="{16*s}" fill="#FFFDF8" stroke="{INK}" stroke-width="1.5"/>
    </g>"""

def bus(cx, cy, scale=1.0):
    s = scale
    w, h = 220 * s, 100 * s
    x0, y0 = cx - w / 2, cy - h
    outfit_defs, outfit_url = outfit_fill("#5FA8D3")
    return f"""<g>
      {outfit_defs}
      {soft_shadow(cx, y0+h+8*s, w*0.56, 10*s, 0.22)}
      <rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="{14*s}" fill="{outfit_url}" stroke="{INK}" stroke-width="2.5"/>
      <rect x="{x0+10*s}" y="{y0+12*s}" width="{w-20*s}" height="{34*s}" rx="{6*s}" fill="#D9F0FA"/>
      {"".join(f'<line x1="{x0+10*s+i*(w-20*s)/5}" y1="{y0+12*s}" x2="{x0+10*s+i*(w-20*s)/5}" y2="{y0+46*s}" stroke="#5FA8D3" stroke-width="2"/>' for i in range(1,5))}
      <rect x="{x0+10*s}" y="{y0+56*s}" width="{w-20*s}" height="{10*s}" fill="#F2A22B"/>
      <circle cx="{x0+30*s}" cy="{y0+h}" r="{16*s}" fill="#2b2320"/>
      <circle cx="{x0+w-30*s}" cy="{y0+h}" r="{16*s}" fill="#2b2320"/>
      <circle cx="{x0+30*s}" cy="{y0+h}" r="{6*s}" fill="#8a8a8a"/>
      <circle cx="{x0+w-30*s}" cy="{y0+h}" r="{6*s}" fill="#8a8a8a"/>
    </g>"""

def bookshelf(cx, cy, scale=1.0):
    s = scale
    w, h = 150 * s, 130 * s
    x0, y0 = cx - w / 2, cy - h
    colors = ["#FF9E80", "#8ECDF0", "#B7E4C7", "#CDB4DB", "#F2C94C"]
    rows = []
    for r in range(2):
        ry = y0 + 8 * s + r * 62 * s
        bx = x0 + 8 * s
        for i in range(6):
            bw = 12 * s
            rows.append(f'<rect x="{bx:.1f}" y="{ry:.1f}" width="{bw:.1f}" height="{50*s:.1f}" fill="{colors[i%len(colors)]}"/>')
            bx += bw + 2 * s
    return f"""<g>
      <rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#C9A46A" stroke="{INK}" stroke-width="2.5"/>
      <line x1="{x0}" y1="{y0+64*s}" x2="{x0+w}" y2="{y0+64*s}" stroke="{INK}" stroke-width="2"/>
      {"".join(rows)}
    </g>"""

def sewing_machine(cx, cy, scale=1.0):
    s = scale
    return f"""<g>
      <rect x="{cx-50*s}" y="{cy-14*s}" width="{100*s}" height="{16*s}" rx="{4*s}" fill="#4a4a52"/>
      <path d="M {cx-30*s} {cy-14*s} q {0} {-40*s} {40*s} {-40*s} l {6*s} 0 l 0 {14*s} l -6*s 0 q {-24*s} 0 -{24*s} {26*s} z" fill="#4a4a52"/>
      <rect x="{cx+10*s}" y="{cy-52*s}" width="{10*s}" height="{10*s}" fill="#F2C94C"/>
      <circle cx="{cx-30*s}" cy="{cy-16*s}" r="{6*s}" fill="#F2C94C"/>
    </g>""".replace("-6*s", str(-6*s))

def fabric_bolts(cx, cy, scale=1.0):
    s = scale
    colors = ["#FF9E80", "#8ECDF0", "#B7E4C7"]
    out = []
    for i, c in enumerate(colors):
        out.append(f'<rect x="{cx-40*s+i*30*s}" y="{cy-30*s-i*4*s}" width="{26*s}" height="{60*s+i*4*s}" rx="{6*s}" fill="{c}" stroke="{INK}" stroke-width="1.5"/>')
    return "".join(out)

def teddy_bear(cx, cy, scale=1.0):
    s = scale
    return f"""<g>
      <circle cx="{cx}" cy="{cy-8*s}" r="{22*s}" fill="#C9A46A" stroke="{INK}" stroke-width="2"/>
      <circle cx="{cx-16*s}" cy="{cy-26*s}" r="{9*s}" fill="#C9A46A" stroke="{INK}" stroke-width="1.5"/>
      <circle cx="{cx+16*s}" cy="{cy-26*s}" r="{9*s}" fill="#C9A46A" stroke="{INK}" stroke-width="1.5"/>
      <ellipse cx="{cx}" cy="{cy+26*s}" rx="{26*s}" ry="{22*s}" fill="#C9A46A" stroke="{INK}" stroke-width="2"/>
      <circle cx="{cx-8*s}" cy="{cy-10*s}" r="{2.4*s}" fill="{INK}"/>
      <circle cx="{cx+8*s}" cy="{cy-10*s}" r="{2.4*s}" fill="{INK}"/>
      <ellipse cx="{cx}" cy="{cy-2*s}" rx="{4*s}" ry="{3*s}" fill="{INK}"/>
    </g>"""

def brick_wall(cx, cy, w, h, color="#E0836B"):
    s = 1
    rows = int(h / 18)
    out = [f'<rect x="{cx-w/2}" y="{cy-h}" width="{w}" height="{h}" fill="{color}" stroke="{INK}" stroke-width="2"/>']
    for r in range(rows):
        ry = cy - h + r * 18
        off = 0 if r % 2 == 0 else 20
        x = cx - w / 2 + off - 20
        while x < cx + w / 2:
            out.append(f'<line x1="{x:.0f}" y1="{ry:.0f}" x2="{x+40:.0f}" y2="{ry:.0f}" stroke="{INK}" stroke-width="0.8" opacity="0.35"/>')
            x += 40
        out.append(f'<line x1="{cx-w/2}" y1="{ry:.0f}" x2="{cx+w/2}" y2="{ry:.0f}" stroke="{INK}" stroke-width="0.8" opacity="0.35"/>')
    return "".join(out)

def building(cx, cy, w, h, color, n_windows=3, roof=None):
    x0, y0 = cx - w / 2, cy - h
    out = [f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="{color}" stroke="{INK}" stroke-width="2.5"/>']
    ww = w / (n_windows * 2.2)
    for i in range(n_windows):
        wx = x0 + w * (i + 0.75) / n_windows - ww / 2
        out.append(f'<rect x="{wx:.1f}" y="{y0+h*0.28:.1f}" width="{ww:.1f}" height="{ww:.1f}" rx="3" fill="#FFF8EC" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<rect x="{cx-w*0.09}" y="{cy-h*0.32}" width="{w*0.18}" height="{h*0.32}" fill="#FFF8EC" stroke="{INK}" stroke-width="1.5"/>')
    if roof:
        out.append(f'<path d="M {x0-6} {y0} L {cx} {y0-h*0.28} L {x0+w+6} {y0} Z" fill="{roof}" stroke="{INK}" stroke-width="2.5"/>')
    return "".join(out)

def fruit_basket(cx, cy, scale=1.0):
    s = scale
    fruit_colors = ["#F2994A", "#EB5757", "#F2C94C", "#6FCF97"]
    out = [f'<path d="M {cx-38*s} {cy} q {-4*s} {30*s} {8*s} {32*s} l {60*s} 0 q {12*s} {-2*s} {8*s} -{32*s} z" fill="#C9A46A" stroke="{INK}" stroke-width="2"/>']
    for i in range(4):
        fx = cx - 26 * s + i * 18 * s
        out.append(f'<circle cx="{fx}" cy="{cy-8*s}" r="{13*s}" fill="{fruit_colors[i%4]}" stroke="{INK}" stroke-width="1.5"/>')
    return "".join(out)

def market_stall(cx, cy, scale=1.0, color="#FF9E80"):
    s = scale
    w = 200 * s
    x0 = cx - w / 2
    stripes = "".join(f'<rect x="{x0+i*w/6:.1f}" y="{cy-90*s:.1f}" width="{w/6:.1f}" height="{18*s:.1f}" fill="{color if i%2==0 else "#FFF8EC"}"/>' for i in range(6))
    return f"""<g>
      <rect x="{x0}" y="{cy-70*s}" width="{w}" height="{60*s}" fill="#FFF8EC" stroke="{INK}" stroke-width="2"/>
      <path d="M {x0-8*s} {cy-70*s} L {x0-8*s} {cy-90*s} L {x0+w+8*s} {cy-90*s} L {x0+w+8*s} {cy-70*s} Z" fill="{color}" stroke="{INK}" stroke-width="2"/>
      {stripes}
      <line x1="{x0}" y1="{cy-10*s}" x2="{x0}" y2="{cy}" stroke="{INK}" stroke-width="3"/>
      <line x1="{x0+w}" y1="{cy-10*s}" x2="{x0+w}" y2="{cy}" stroke="{INK}" stroke-width="3"/>
    </g>"""

def sofa(cx, cy, scale=1.0, color="#CDB4DB"):
    s = scale
    w, h = 180 * s, 70 * s
    x0, y0 = cx - w / 2, cy - h
    return f"""<g>
      <rect x="{x0}" y="{y0+20*s}" width="{w}" height="{h-20*s}" rx="{14*s}" fill="{color}" stroke="{INK}" stroke-width="2.5"/>
      <rect x="{x0-10*s}" y="{y0}" width="{34*s}" height="{h}" rx="{14*s}" fill="{color}" stroke="{INK}" stroke-width="2.5"/>
      <rect x="{x0+w-24*s}" y="{y0}" width="{34*s}" height="{h}" rx="{14*s}" fill="{color}" stroke="{INK}" stroke-width="2.5"/>
      <rect x="{x0+30*s}" y="{y0+8*s}" width="{50*s}" height="{34*s}" rx="{10*s}" fill="#FFF8EC" opacity="0.6"/>
    </g>"""

def bed(cx, cy, scale=1.0, blanket="#8ECDF0"):
    s = scale
    w, h = 220 * s, 70 * s
    x0, y0 = cx - w / 2, cy - h
    return f"""<g>
      <rect x="{x0}" y="{y0+20*s}" width="{w}" height="{h-20*s}" rx="{10*s}" fill="{blanket}" stroke="{INK}" stroke-width="2.5"/>
      <rect x="{x0}" y="{y0}" width="{60*s}" height="{34*s}" rx="{10*s}" fill="#FFFDF8" stroke="{INK}" stroke-width="2"/>
      <rect x="{x0-6*s}" y="{y0-4*s}" width="{12*s}" height="{h+8*s}" fill="#C9A46A"/>
    </g>"""

def window(cx, cy, w, h, sky="#FFD98A"):
    x0, y0 = cx - w / 2, cy - h
    return f"""<g>
      <rect x="{x0-8}" y="{y0-8}" width="{w+16}" height="{h+16}" fill="#C9A46A" stroke="{INK}" stroke-width="2"/>
      <rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="{sky}"/>
      <line x1="{cx}" y1="{y0}" x2="{cx}" y2="{y0+h}" stroke="{INK}" stroke-width="2"/>
      <line x1="{x0}" y1="{cy}" x2="{x0+w}" y2="{cy}" stroke="{INK}" stroke-width="2"/>
    </g>"""

def table_simple(cx, cy, scale=1.0):
    s = scale
    return f"""<g>
      <rect x="{cx-70*s}" y="{cy-10*s}" width="{140*s}" height="{12*s}" fill="#C9A46A" stroke="{INK}" stroke-width="2"/>
      <rect x="{cx-60*s}" y="{cy+2*s}" width="{8*s}" height="{34*s}" fill="#C9A46A"/>
      <rect x="{cx+52*s}" y="{cy+2*s}" width="{8*s}" height="{34*s}" fill="#C9A46A"/>
    </g>"""

def road(y, h, w=700):
    return f'<rect x="0" y="{y}" width="{w}" height="{h}" fill="#B9B0A2"/><line x1="0" y1="{y+h/2}" x2="{w}" y2="{y+h/2}" stroke="#FFF8EC" stroke-width="4" stroke-dasharray="26,18"/>'

def bread_loaf(cx, cy, scale=1.0):
    s = scale
    return f"""<g>
      <path d="M {cx-32*s} {cy} q {-4*s} -{30*s} {32*s} -{30*s} q {36*s} 0 {32*s} {30*s} z" fill="#D9A05B" stroke="{INK}" stroke-width="2"/>
      <path d="M {cx-16*s} {cy-18*s} l {6*s} {10*s} M {cx} {cy-22*s} l {6*s} {12*s} M {cx+16*s} {cy-18*s} l {6*s} {10*s}" stroke="{INK}" stroke-width="1.5"/>
    </g>"""

def frame_portrait(cx, cy, scale=1.0):
    s = scale
    return f"""<g>
      <rect x="{cx-30*s}" y="{cy-40*s}" width="{60*s}" height="{50*s}" fill="#F2C94C" stroke="{INK}" stroke-width="2.5"/>
      <rect x="{cx-22*s}" y="{cy-32*s}" width="{44*s}" height="{34*s}" fill="#FFF8EC"/>
      <circle cx="{cx-8*s}" cy="{cy-16*s}" r="{8*s}" fill="{SKIN}"/>
      <circle cx="{cx+10*s}" cy="{cy-16*s}" r="{8*s}" fill="{SKIN2}"/>
    </g>"""

MINI_ICON_COLORS = {
    "bread": "#D9A05B", "milk": "#FFFDF8", "bus": "#5FA8D3", "book": "#8ECDF0",
    "shirt": "#F2C94C", "hospital": "#EB5757", "school": "#F2A22B", "fruit": "#6FCF97",
}

def mini_icon(kind, cx, cy, scale=1.0):
    s = 26 * scale
    if kind == "bread":
        return f'<path d="M {cx-s} {cy+s*0.5} q -3 -{s} {s} -{s} q {s+3} 0 {s} {s} z" fill="#D9A05B" stroke="{INK}" stroke-width="1.5"/>'
    if kind == "milk":
        return f'<path d="M {cx-s*0.5} {cy-s} l {s} 0 l {s*0.35} {s*1.7} l -{s*1.7} 0 z" fill="#FFFDF8" stroke="{INK}" stroke-width="1.5"/><rect x="{cx-s*0.5}" y="{cy-s}" width="{s}" height="{s*0.4}" fill="#8ECDF0"/>'
    if kind == "bus":
        return f'<rect x="{cx-s}" y="{cy-s*0.6}" width="{2*s}" height="{s*1.1}" rx="6" fill="#5FA8D3" stroke="{INK}" stroke-width="1.5"/><circle cx="{cx-s*0.6}" cy="{cy+s*0.5}" r="{s*0.25}" fill="{INK}"/><circle cx="{cx+s*0.6}" cy="{cy+s*0.5}" r="{s*0.25}" fill="{INK}"/>'
    if kind == "book":
        return f'<rect x="{cx-s}" y="{cy-s*0.8}" width="{2*s}" height="{s*1.5}" rx="3" fill="#8ECDF0" stroke="{INK}" stroke-width="1.5"/><line x1="{cx}" y1="{cy-s*0.8}" x2="{cx}" y2="{cy+s*0.7}" stroke="{INK}" stroke-width="1.2"/>'
    if kind == "shirt":
        return f'<path d="M {cx-s} {cy-s*0.6} l {s*0.5} -{s*0.4} l {s*0.5} {s*0.3} l {s*0.5} -{s*0.3} l {s*0.5} {s*0.4} l -{s*0.3} {s*0.4} l 0 {s*1.1} l -{s*1.4} 0 l 0 -{s*1.1} z" fill="#F2C94C" stroke="{INK}" stroke-width="1.3"/>'
    if kind == "hospital":
        return f'<rect x="{cx-s}" y="{cy-s}" width="{2*s}" height="{2*s}" rx="4" fill="#FFF8EC" stroke="{INK}" stroke-width="1.5"/><rect x="{cx-s*0.18}" y="{cy-s*0.6}" width="{s*0.36}" height="{s*1.2}" fill="#EB5757"/><rect x="{cx-s*0.6}" y="{cy-s*0.18}" width="{s*1.2}" height="{s*0.36}" fill="#EB5757"/>'
    if kind == "school":
        return f'<path d="M {cx-s} {cy+s} l 0 -{s*0.9} l {s} -{s*0.6} l {s} {s*0.6} l 0 {s*0.9} z" fill="#F2A22B" stroke="{INK}" stroke-width="1.5"/><rect x="{cx-s*0.3}" y="{cy+s*0.2}" width="{s*0.6}" height="{s*0.8}" fill="#FFF8EC"/>'
    if kind == "fruit":
        return f'<circle cx="{cx}" cy="{cy}" r="{s*0.9}" fill="#EB5757" stroke="{INK}" stroke-width="1.5"/><path d="M{cx} {cy-s*0.9} q 4 -6 8 -4" stroke="#6FCF97" stroke-width="2" fill="none"/>'
    return ""

def scene_svg(uid, inner, w=700, h=355):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" width="100%">{inner}</svg>'
