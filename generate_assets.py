# -*- coding: utf-8 -*-
"""Genera og-image.png (1200x630) y apple-touch-icon.png (180x180) para AGGO Associates."""
from PIL import Image, ImageDraw, ImageFont

NAVY = (7, 15, 36)
NAVY_LIGHT = (19, 41, 79)
GOLD = (201, 163, 92)
GOLD_LIGHT = (230, 197, 133)
SILVER = (244, 246, 250)
MUTED = (168, 176, 192)


def vertical_gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", size, top)
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / h
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, y), (w, y)], fill=c)
    return img


def load_font(names, size):
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


SERIF = ["georgiab.ttf", "georgia.ttf", "times.ttf"]
SANS = ["segoeui.ttf", "arial.ttf"]
SANS_BOLD = ["segoeuib.ttf", "arialbd.ttf"]


def draw_bars(d, cx, cy, scale, color_top, color_bottom):
    """Dibuja las 3 barras del logo con degradado simple."""
    bars = [(-1.4, 0.55), (-0.35, 1.0), (0.7, 0.75)]  # (offset_x, altura relativa)
    bw = 0.62 * scale
    max_h = 2.2 * scale
    for off, hrel in bars:
        x0 = cx + off * scale
        h = max_h * hrel
        y0 = cy + max_h / 2 - h
        y1 = cy + max_h / 2
        steps = int(h)
        for i in range(steps):
            t = i / max(steps - 1, 1)
            c = tuple(int(color_top[j] + (color_bottom[j] - color_top[j]) * t) for j in range(3))
            d.rectangle([x0, y0 + i, x0 + bw, y0 + i + 1], fill=c)


# ============ OG IMAGE 1200x630 ============
img = vertical_gradient((1200, 630), NAVY, (10, 24, 48))
d = ImageDraw.Draw(img)

# marco dorado sutil
d.rectangle([24, 24, 1175, 605], outline=GOLD, width=2)

# circulo + barras (logo) a la izquierda
cx, cy = 240, 260
d.ellipse([cx - 110, cy - 110, cx + 110, cy + 110], outline=GOLD, width=4)
draw_bars(d, cx, cy - 10, 60, SILVER, (140, 147, 163))
# arco dorado inferior (semicirculo grueso)
d.arc([cx - 122, cy - 122, cx + 122, cy + 122], start=110, end=210, fill=GOLD_LIGHT, width=8)

f_title = load_font(SERIF, 92)
f_sub = load_font(SERIF, 44)
f_small = load_font(SANS_BOLD, 30)
f_tiny = load_font(SANS, 26)

d.text((420, 150), "AGGO", font=f_title, fill=SILVER)
d.text((420, 260), "ASSOCIATES C.A.", font=f_sub, fill=GOLD)
d.line([(420, 340), (1100, 340)], fill=GOLD, width=2)
d.text((420, 365), "Contadores y Auditores", font=f_small, fill=SILVER)
d.text((420, 410), "Machala, El Oro — Ecuador", font=f_small, fill=MUTED)

d.text((420, 495), "Contabilidad · Impuestos · Consultoría Fiscal · Sector Minero", font=f_tiny, fill=GOLD_LIGHT)
d.text((420, 535), "wwwaggoacountt.com  ·  +593 99 107 1743", font=f_tiny, fill=MUTED)

img.save(r"C:\Users\ADMIN\Desktop\Tareas\PROGRAMAS\16. aggo-associates\og-image.png", optimize=True)

# ============ APPLE TOUCH ICON 180x180 ============
icon = vertical_gradient((180, 180), NAVY_LIGHT, NAVY)
d2 = ImageDraw.Draw(icon)
d2.ellipse([18, 18, 162, 162], outline=GOLD, width=5)
draw_bars(d2, 90, 82, 26, SILVER, (140, 147, 163))
d2.arc([12, 12, 168, 168], start=110, end=210, fill=GOLD_LIGHT, width=7)
icon.save(r"C:\Users\ADMIN\Desktop\Tareas\PROGRAMAS\16. aggo-associates\apple-touch-icon.png", optimize=True)

print("OK: og-image.png y apple-touch-icon.png generados")
