#!/usr/bin/env python3
"""Render entry.png v1 for news-image-20261125: a one-page newspaper
front page summing up Wednesday 25 November 2026 — lead + 8 stories +
6 briefs + markets strip. Every item first reported on 25 November 2026
(or a development of the day for a running story).
Output: 1024x1024 PNG. Run: python3 render.py (needs Pillow).
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024

NAVY = (16, 36, 62)
NAVY2 = (24, 52, 88)
PAPER = (246, 241, 231)
CARD = (255, 255, 255)
GRAY = (85, 85, 85)
RED = (192, 57, 43)
GOLD = (201, 162, 39)
LINE = (210, 204, 190)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def letterspaced(draw, xy, text, fnt, fill, spacing=4):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + spacing
    return x


# ---------------------------------------------------------------- stories
LEAD = {
    "kicker": "CHINA  ·  POLITICS",
    "headline": "Shanghai party chief Chen Jining under investigation",
    "summary": ("A Politburo member falls in Xi's purge: the fourth since 2025. "
                "Shanghai's leadership pledged loyalty to Beijing on Wednesday."),
}

STORIES = [
    {
        "kicker": "US INTELLIGENCE",
        "accent": (178, 44, 36),
        "headline": "CIA and spy chief's office hit by hack",
        "summary": "Unclassified systems hit; no classified data touched, officials say. Early signs point to China.",
    },
    {
        "kicker": "BUSINESS",
        "accent": (14, 124, 123),
        "headline": "Shein to pay $100m to settle FTC claims",
        "summary": "Shipping delays, hidden bad reviews, cotton claims. $100m to go to shoppers.",
    },
    {
        "kicker": "TURKIYE",
        "accent": (90, 60, 160),
        "headline": "Five killed as military helicopter crashes",
        "summary": "Training flight goes down in western Turkiye, the military says.",
    },
    {
        "kicker": "MIGRATION",
        "accent": (30, 132, 73),
        "headline": "About 175 migrants missing as boat vanishes",
        "summary": "Boat from Senegal bound for Europe lost at sea; a search is under way.",
    },
    {
        "kicker": "UKRAINE",
        "accent": (36, 86, 166),
        "headline": "Putin warns retaliation is inevitable",
        "summary": "As Kyiv keeps hitting Russian oil refineries, Moscow vows to answer.",
    },
    {
        "kicker": "SAUDI ARABIA",
        "accent": (70, 110, 40),
        "headline": "Houthis hit Riyadh's tallest tower; 11 hurt",
        "summary": "Second strike on the PIF tower in a week. Riyadh calls it a terrorist attack.",
    },
    {
        "kicker": "CONGO",
        "accent": (123, 45, 139),
        "headline": "Rebels call off advance on Bunia, pull back",
        "summary": "Fighting eases in Ituri after days of clashes around the city.",
    },
    {
        "kicker": "MARKETS",
        "accent": (185, 119, 14),
        "headline": "Wall Street cools after record rally",
        "summary": "Nasdaq -1.48% as AI shares give back gains; Dow climbs 0.85%.",
    },
]

BRIEFS = [
    "UN: five women killed every hour by a relative in 2025",
    "Senegal's 2025 AFCON title restored after CAS ruling",
    "European rights court lets states turn back migrants",
    "Iraq orders forces to seize Kurdish oilfields",
    "US soldier admits selling military secrets to China",
    "Nvidia's Huang says he is in therapy as rally fades",
]

TICKER = ("DOW 50,019  +0.85%   ·   S&P 500 7,201  -0.50%   ·   "
           "NASDAQ 23,734  -1.48%   ·   GOLD $3,553  -2.70%   ·   WTI $81.63  +1.82%")

# ---------------------------------------------------------------- canvas
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- masthead ------------------------------------------------------
d.rectangle([0, 0, W, 96], fill=NAVY)
letterspaced(d, (36, 10), "THE WORLD IN ONE IMAGE", font(SANS_B, 18), GOLD, spacing=6)
d.text((36, 30), "Wednesday 25 November 2026", font=font(SERIF_B, 44), fill=(255, 255, 255))
d.text((W - 36 - d.textlength("DAILY EDITION", font=font(SANS_B, 17)), 16),
       "DAILY EDITION", font=font(SANS_B, 17), fill=(170, 195, 225))
d.rectangle([36, 84, W - 36, 87], fill=GOLD)

# ---- markets ticker --------------------------------------------------
d.rectangle([0, 96, W, 122], fill=NAVY2)
tw = d.textlength(TICKER, font=font(SANS_B, 14))
d.text(((W - tw) / 2, 103), TICKER, font=font(SANS_B, 14), fill=(235, 220, 170))

# ---- lead card -------------------------------------------------------
lx, ly, lw, lh = 28, 132, W - 56, 232
d.rectangle([lx, ly, lx + lw, ly + lh], fill=CARD, outline=LINE, width=2)
d.rectangle([lx, ly, lx + 10, ly + lh], fill=RED)
tx = lx + 32
ty = ly + 14
d.text((tx, ty), LEAD["kicker"], font=font(SANS_B, 21), fill=RED)
ty += 30
hl = wrap(d, LEAD["headline"], font(SERIF_B, 32), 612)
ty = draw_lines(d, tx, ty, hl, font(SERIF_B, 32), NAVY, 38)
ty += 6
sl = wrap(d, LEAD["summary"], font(SANS, 19), 612)
draw_lines(d, tx, ty, sl, font(SANS, 19), GRAY, 23)

# lead illustration: classical hall of power — pediment, columns, steps
ix0, iy0, ix1, iy1 = 700, ly + 14, lx + lw - 14, ly + lh - 14
pw, ph = ix1 - ix0, iy1 - iy0
panel = Image.new("RGB", (pw, ph), (10, 22, 44))
p = ImageDraw.Draw(panel)
for (sx, sy, r) in [(22, 20, 2), (62, 60, 2), (110, 15, 3), (168, 50, 2),
                    (228, 25, 2), (32, 120, 2), (238, 140, 3), (140, 120, 2),
                    (84, 160, 2), (200, 180, 2), (238, 88, 2), (44, 190, 2)]:
    p.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(255, 255, 255))
p.text((12, 8), "SHANGHAI", font=font(SANS_B, 16), fill=(160, 190, 230))
# pediment
p.polygon([(48, 96), (140, 52), (232, 96)], fill=(201, 162, 39))
p.ellipse([128, 66, 152, 90], fill=(192, 57, 43))
# columns
for cx in (66, 106, 146, 186):
    p.rectangle([cx, 100, cx + 14, 168], fill=(220, 225, 235))
    p.rectangle([cx - 3, 96, cx + 17, 101], fill=(220, 225, 235))
    p.rectangle([cx - 3, 168, cx + 17, 173], fill=(220, 225, 235))
# steps
for i, y in enumerate((176, 184, 192)):
    p.rectangle([40 - i * 6, y, 240 + i * 6, y + 6], fill=(160, 170, 190))
# red seal stamp, tilted
seal = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
q = ImageDraw.Draw(seal)
q.ellipse([4, 4, 60, 60], outline=(220, 60, 50), width=4)
q.text((22, 16), "!", font=font(SANS_B, 30), fill=(220, 60, 50))
seal = seal.rotate(18, expand=False, resample=Image.BICUBIC)
panel.paste(seal, (196, 116), seal)
img.paste(panel, (ix0, iy0))

# ---- story grid: 8 cards, 2 x 4 --------------------------------------
gx, gy = 28, 372
cw, chh, gap = 472, 118, 8
for i, s in enumerate(STORIES):
    col, row = i % 2, i // 2
    x = gx + col * (cw + gap)
    y = gy + row * (chh + gap)
    d.rectangle([x, y, x + cw, y + chh], fill=CARD, outline=LINE, width=2)
    d.rectangle([x, y, x + cw, y + 6], fill=s["accent"])
    tx2 = x + 18
    ty2 = y + 11
    d.text((tx2, ty2), s["kicker"], font=font(SANS_B, 15), fill=s["accent"])
    ty2 += 20
    tw_card = 262 if s["kicker"] == "MARKETS" else cw - 36
    hl2 = wrap(d, s["headline"], font(SANS_B, 20), tw_card)
    ty2 = draw_lines(d, tx2, ty2, hl2[:2], font(SANS_B, 20), NAVY, 24)
    sl2 = wrap(d, s["summary"], font(SANS, 14), tw_card)
    draw_lines(d, tx2, ty2 + 3, sl2[:2], font(SANS, 14), GRAY, 17)
    if s["kicker"] == "MARKETS":
        # mini chart: S&P 500 Fri close 6,910 -> Mon close 7,237 (+4.7%) -> Tue close 7,201 (-0.5%)
        px0, py0, px1, py1 = x + 292, y + 12, x + cw - 12, y + chh - 10
        d.rectangle([px0, py0, px1, py1], fill=(248, 248, 244), outline=LINE, width=1)
        d.text((px0 + 8, py0 + 5), "S&P 500", font=font(SANS_B, 12), fill=NAVY)
        vals = [6910, 7237, 7201]
        lo, hi = 6850, 7300
        plot_y0, plot_y1 = py0 + 26, py1 - 15
        xs = [px0 + 24, (px0 + px1) // 2, px1 - 24]
        ys = [plot_y1 - (v - lo) / (hi - lo) * (plot_y1 - plot_y0) for v in vals]
        for j in range(2):
            d.line([xs[j], ys[j], xs[j + 1], ys[j + 1]], fill=(24, 52, 88), width=2)
        for j, (cx, cy) in enumerate(zip(xs, ys)):
            d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(192, 57, 43))
            lab = ["FRI", "MON", "TUE"][j]
            lw2 = d.textlength(lab, font=font(SANS, 9))
            d.text((cx - lw2 / 2, py1 - 13), lab, font=font(SANS, 9), fill=GRAY)
        d.text((xs[1] - 17, ys[1] - 16), "+4.7%", font=font(SANS_B, 11), fill=(30, 132, 73))
        d.text((xs[2] - 13, ys[2] + 6), "-0.5%", font=font(SANS_B, 11), fill=(192, 57, 43))

# ---- in brief band + footer -------------------------------------------
by0 = 876
d.rectangle([28, by0, W - 28, by0 + 132], fill=NAVY)
d.text((48, by0 + 10), "IN BRIEF", font=font(SANS_B, 16), fill=GOLD)
colw = (W - 56 - 40) // 2
for i, b in enumerate(BRIEFS):
    col, row = i % 2, i // 2
    x = 48 + col * colw
    y = by0 + 34 + row * 25
    d.ellipse([x, y + 5, x + 7, y + 12], fill=GOLD)
    bl = wrap(d, b, font(SANS, 15), colw - 22)
    d.text((x + 16, y), bl[0], font=font(SANS, 15), fill=(240, 240, 235))
d.line([48, by0 + 108, W - 48, by0 + 108], fill=(70, 100, 140), width=1)
foot = "Every story first reported on Wednesday 25 November 2026"
fw = d.textlength(foot, font=font(SANS, 14))
d.text(((W - fw) / 2, by0 + 114), foot, font=font(SANS, 13), fill=(170, 195, 225))

out_path = os.path.join(HERE, "entry.png")
img.save(out_path, "PNG", optimize=True)
print(out_path, os.path.getsize(out_path), "bytes,", img.size)
