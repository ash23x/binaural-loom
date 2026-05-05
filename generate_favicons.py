"""Generate raster favicons (PNG + multi-size ICO) from the SVG design.
Renders at 4x then downsamples for clean anti-aliased edges.
"""
from PIL import Image, ImageDraw

def make_favicon(size):
    scale = 4
    s = size * scale
    sf = s / 32.0  # scale factor relative to 32px design coords

    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Dark rounded background
    radius = int(5 * sf)
    draw.rounded_rectangle((0, 0, s-1, s-1), radius=radius, fill=(13, 13, 26, 255))

    # Two intersecting carrier rings (orange + purple)
    cy = int(16 * sf)
    cx_l = int(12 * sf)
    cx_r = int(20 * sf)
    r = int(8 * sf)
    stroke_w = max(2, int(1.4 * sf))
    draw.ellipse((cx_l - r, cy - r, cx_l + r, cy + r),
                 outline=(255, 136, 0, 191), width=stroke_w)
    draw.ellipse((cx_r - r, cy - r, cx_r + r, cy + r),
                 outline=(178, 102, 255, 191), width=stroke_w)

    # Glowing gold core (radial gradient via concentric circles)
    cx_c = int(16 * sf)
    cy_c = int(16 * sf)
    max_r = int(7 * sf)
    for i in range(max_r, 0, -1):
        t = i / max_r
        if t < 0.55:
            b = t / 0.55
            col = (255, int(232 - 28 * b), int(153 - 85 * b), 255)
        else:
            b = (t - 0.55) / 0.45
            col = (255, int(204 - 68 * b), int(68 - 68 * b), int(217 * (1 - b)))
        draw.ellipse((cx_c - i, cy_c - i, cx_c + i, cy_c + i), fill=col)

    # Downsample with Lanczos for clean AA
    return img.resize((size, size), Image.LANCZOS)

if __name__ == '__main__':
    out_dir = r'D:\binaural-loom'
    # Standard PNG sizes
    for sz in [16, 32, 48, 192]:
        make_favicon(sz).save(f'{out_dir}\\favicon-{sz}.png')
    # Multi-resolution ICO for the bookmark/shortcut bar
    src = make_favicon(256)
    src.save(f'{out_dir}\\favicon.ico', format='ICO',
             sizes=[(16, 16), (32, 32), (48, 48)])
    print("Generated: favicon-{16,32,48,192}.png + favicon.ico")
