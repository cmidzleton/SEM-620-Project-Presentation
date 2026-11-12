"""Painterly textures for the painting-theme 311 deck: canvas grid, brush strokes, watercolour sticky notes, splatters."""
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
import os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__)) + "/tex"
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)

def hexrgb(h): return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def noise(h, w, scale, seed):
    r = np.random.default_rng(seed)
    small = r.random((max(2, h // scale), max(2, w // scale)))
    im = Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return np.asarray(im).astype(float) / 255

def fbm(h, w, seed, octaves=(64, 24, 8, 3), weights=(0.5, 0.25, 0.15, 0.1)):
    return sum(wt * noise(h, w, s, seed + i) for i, (s, wt) in enumerate(zip(octaves, weights)))

# 1. canvas + grid background (1920x1080)
W, H = 1920, 1080
base = np.array(hexrgb("FBFAF5"), float)
tex = fbm(H, W, 1)
weave = (np.sin(np.arange(W)[None, :] * 1.9) * np.sin(np.arange(H)[:, None] * 1.7)) * 0.5 + 0.5
img = base[None, None, :] * (0.975 + 0.03 * tex[..., None]) - 4 * weave[..., None] * 0.6
# warm vignette like old canvas
yy, xx = np.mgrid[0:H, 0:W]
d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
img -= np.clip(d - 0.75, 0, 1)[..., None] * np.array([10, 12, 20])
grid = np.array(hexrgb("E4EEF5"), float)
step = W / 26.67  # 0.5 in grid like the style deck
gl = np.zeros((H, W))
for k in np.arange(0, W, step):
    gl[:, int(k):int(k) + 2] = 1
for k in np.arange(0, H, step):
    gl[int(k):int(k) + 2, :] = 1
gl *= 0.55 + 0.45 * fbm(H, W, 9, (200, 50), (0.6, 0.4))
img = img * (1 - gl[..., None] * 0.85) + grid * gl[..., None] * 0.85
Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(f"{OUT}/canvas.png", optimize=True)

# 2. brush strokes (highlighter of paint) in several colours
def brush(color, w=1400, h=220, seed=0, name="brush"):
    r = np.random.default_rng(seed)
    x = np.linspace(0, 1, w)
    # stroke body: thickness varies, ends taper raggedly
    top = 0.16 + 0.10 * noise(1, w, 60, seed)[0] + 0.02 * np.sin(x * 7 + seed)
    bot = 0.86 - 0.10 * noise(1, w, 60, seed + 1)[0] - 0.02 * np.cos(x * 5 + seed)
    Y = np.linspace(0, 1, h)[:, None]
    body = ((Y > top[None, :]) & (Y < bot[None, :])).astype(float)
    # bristle streaks
    streak = noise(h, 1, 3, seed + 2)[:, :1] * np.ones((1, w))
    streak = 0.62 + 0.38 * np.asarray(Image.fromarray((streak * 255).astype(np.uint8)).resize((w, h))).astype(float) / 255
    dry = fbm(h, w, seed + 3, (40, 12, 4), (0.5, 0.3, 0.2))
    a = body * streak
    # dry brush at the right end, blob at the left start
    endfade = np.clip((1 - x) / 0.18, 0, 1) ** 0.7
    a *= np.where(dry < 0.12 + 0.6 * (1 - endfade[None, :]), 0.12, 1.0)
    startcut = np.clip(x / 0.03, 0, 1)
    a *= startcut[None, :]
    # paint pooling at the edges
    edge = Image.fromarray((body * 255).astype(np.uint8)).filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(3))
    edge = np.asarray(edge).astype(float) / 255
    a = np.clip(a * 0.85 + edge * 0.3 * body, 0, 1)
    c = np.array(hexrgb(color), float)
    shade = (0.92 + 0.12 * dry)[..., None]
    rgb = np.clip(c[None, None, :] * shade - edge[..., None] * 25, 0, 255)
    alpha = Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    out = np.dstack([rgb, np.asarray(alpha)]).astype(np.uint8)
    Image.fromarray(out, "RGBA").save(f"{OUT}/{name}.png", optimize=True)

for nm, col, sd in [("brush_yellow", "FFE45C", 1), ("brush_yellow2", "FFE45C", 5), ("brush_pink", "FFB3C6", 2),
                    ("brush_mint", "9EE6BC", 3), ("brush_blue", "A9C8F0", 4), ("brush_red", "E8616F", 6)]:
    brush(col, seed=sd, name=nm)

# 3. watercolour sticky notes
def wash(color, w=900, h=560, seed=0, name="wash"):
    c = np.array(hexrgb(color), float)
    yy, xx = np.mgrid[0:h, 0:w]
    m = fbm(h, w, seed, (120, 40, 10), (0.55, 0.3, 0.15))
    # irregular paper-cut edge with soft bleed
    inset = 10
    dx = np.minimum(xx, w - 1 - xx); dy = np.minimum(yy, h - 1 - yy)
    dist = np.minimum(dx, dy) - inset - 8 * (m - 0.5)
    alpha = np.clip(dist / 3, 0, 1)
    # watercolour edge darkening + blooms + granulation
    edge = np.exp(-np.clip(dist, 0, None) / 14)
    bloom = fbm(h, w, seed + 11, (180, 60), (0.7, 0.3))
    gran = np.random.default_rng(seed).random((h, w))
    dens = 0.62 + 0.45 * bloom + 0.4 * edge + 0.05 * (gran - 0.5)
    # mix toward paper white where density low
    paper = np.array([253, 252, 247], float)
    k = np.clip(dens, 0, 1.3)[..., None]
    rgb = paper + (c - paper) * k
    rgb = np.clip(rgb - edge[..., None] * 10, 0, 255)
    out = np.dstack([rgb, alpha * 255]).astype(np.uint8)
    Image.fromarray(out, "RGBA").save(f"{OUT}/{name}.png", optimize=True)

for nm, col, sd in [("wash_yellow", "FFEE8A", 21), ("wash_mint", "B5EDCB", 22), ("wash_pink", "FFC7D5", 23),
                    ("wash_blue", "C9DDF5", 24), ("wash_cream", "F6EEDC", 25), ("wash_red", "F7A9B2", 26)]:
    wash(col, seed=sd, name=nm)

# 4. splatters
def splat(color, size=500, seed=0, name="splat"):
    r = np.random.default_rng(seed)
    im = Image.new("L", (size, size), 0); d = ImageDraw.Draw(im)
    cx = cy = size / 2
    for _ in range(14):
        ang = r.random() * 6.28; rad = r.random() * size * 0.12
        x, y = cx + np.cos(ang) * rad, cy + np.sin(ang) * rad; s = size * (0.05 + r.random() * 0.1)
        d.ellipse([x - s, y - s, x + s, y + s], fill=255)
    for _ in range(60):
        ang = r.random() * 6.28; rad = size * (0.15 + r.random() ** 1.5 * 0.33)
        x, y = cx + np.cos(ang) * rad, cy + np.sin(ang) * rad; s = size * 0.004 + r.random() * size * 0.018
        d.ellipse([x - s, y - s, x + s, y + s], fill=255)
    im = im.filter(ImageFilter.GaussianBlur(1.2))
    c = np.array(hexrgb(color), float)
    a = np.asarray(im).astype(float) / 255
    v = fbm(size, size, seed + 3, (60, 15), (0.6, 0.4))
    rgb = np.clip(c[None, None, :] * (0.85 + 0.25 * v[..., None]), 0, 255)
    Image.fromarray(np.dstack([rgb, a * 235]).astype(np.uint8), "RGBA").save(f"{OUT}/{name}.png", optimize=True)

for nm, col, sd in [("splat_red", "D7263D", 31), ("splat_blue", "1F4E9C", 32), ("splat_yellow", "F2C230", 33), ("splat_mint", "2A9D5C", 34)]:
    splat(col, seed=sd, name=nm)

# 5. paint palette for the cover
def palette(size=900, name="palette"):
    W2, H2 = size, int(size * 0.72)
    im = Image.new("RGBA", (W2, H2), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([20, 20, W2 - 20, H2 - 20], fill=(222, 196, 150, 255))
    d.ellipse([W2 * 0.18, H2 * 0.55, W2 * 0.34, H2 * 0.8], fill=(0, 0, 0, 0))  # thumb hole
    arr = np.asarray(im).astype(float)
    v = fbm(H2, W2, 41, (90, 20, 5), (0.5, 0.3, 0.2))
    grain = (np.sin(np.arange(W2)[None, :] / 9 + v * 6) * 0.5 + 0.5)
    arr[..., :3] *= (0.86 + 0.1 * grain + 0.06 * v)[..., None]
    im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGBA")
    blobs = [("D7263D", .30, .25), ("FFE45C", .50, .18), ("2A9D5C", .70, .26), ("1F4E9C", .80, .48), ("FFB3C6", .62, .70), ("22252B", .45, .45)]
    r = np.random.default_rng(42)
    for col, fx, fy in blobs:
        s = int(size * 0.11)
        bl = Image.new("L", (s * 2, s * 2), 0); bd = ImageDraw.Draw(bl)
        for _ in range(9):
            ox, oy = r.normal(0, s * 0.18, 2); rr = s * (0.35 + r.random() * 0.25)
            bd.ellipse([s + ox - rr, s + oy - rr, s + ox + rr, s + oy + rr], fill=255)
        bl = bl.filter(ImageFilter.GaussianBlur(2))
        c = Image.new("RGBA", bl.size, hexrgb(col) + (255,)); c.putalpha(bl)
        im.alpha_composite(c, (int(W2 * fx - s), int(H2 * fy - s)))
    im.save(f"{OUT}/{name}.png", optimize=True)
palette()

# 6. ornate-ish painted frame ring for portraits
def frame(size=500, name="frame"):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([4, 4, size - 4, size - 4], fill=(176, 132, 52, 255))
    d.ellipse([28, 28, size - 28, size - 28], fill=(222, 182, 92, 255))
    d.ellipse([44, 44, size - 44, size - 44], fill=(150, 108, 40, 255))
    d.ellipse([52, 52, size - 52, size - 52], fill=(0, 0, 0, 0))
    arr = np.asarray(im).astype(float)
    v = fbm(size, size, 51, (40, 10, 3), (0.5, 0.3, 0.2))
    arr[..., :3] *= (0.85 + 0.3 * v)[..., None]
    Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGBA").save(f"{OUT}/{name}.png", optimize=True)
frame()
print("ok", OUT)
