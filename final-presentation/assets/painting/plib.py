"""Painting / whiteboard-sketch slide helpers (python-pptx). Style after the T5 whiteboard template:
grid canvas, yellow highlight titles, rotated sticky notes, hand-drawn boxes, red circles, blue arrows,
rendered here with painted textures (brush strokes, watercolour washes)."""
import os, random
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.dml import MSO_LINE
from pptx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = os.path.join(HERE, "tex")
CAST_DIR = os.path.dirname(HERE)

HAND = "Segoe Print"      # handwriting face used by the template
BODY = "Segoe UI"
BODY_SB = "Segoe UI Semibold"

INK = "22252B"; BLUE = "1F4E9C"; RED = "D7263D"; GREEN = "2A9D5C"; SHADOW = "D9D4C3"
YEL = "FFE45C"; LYEL = "FFF3A3"; MINT = "C9F2D9"; PINK = "FFD6E0"; GREY = "5D6470"; PAPER = "FBFAF5"
WASH = {"yellow": "wash_yellow", "mint": "wash_mint", "pink": "wash_pink", "blue": "wash_blue",
        "cream": "wash_cream", "red": "wash_red"}
BRUSH = {"yellow": "brush_yellow", "yellow2": "brush_yellow2", "pink": "brush_pink", "mint": "brush_mint",
         "blue": "brush_blue", "red": "brush_red"}

random.seed(620)


def rgb(h):
    return RGBColor.from_string(h)


class Deck:
    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width = Emu(12192000)
        self.prs.slide_height = Emu(6858000)
        self.blank = self.prs.slide_layouts[6]
        self.page = 0

    def save(self, path):
        self.prs.save(path)


def _noshadow(sh):
    try:
        sh.shadow.inherit = False
    except Exception:
        pass


def pic(s, name, x, y, w=None, h=None, rot=0):
    path = name if os.path.isabs(name) else os.path.join(TEX, name + ".png")
    kw = {}
    if w is not None:
        kw["width"] = Inches(w)
    if h is not None:
        kw["height"] = Inches(h)
    p = s.shapes.add_picture(path, Inches(x), Inches(y), **kw)
    if rot:
        p.rotation = rot
    return p


def rect(s, x, y, w, h, fill=None, line=None, lw=1.0, shape=MSO_SHAPE.RECTANGLE, rot=0, dash=False):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    _noshadow(sh)
    if fill:
        sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    else:
        sh.fill.background()
    if line:
        sh.line.color.rgb = rgb(line); sh.line.width = Pt(lw)
        if dash:
            sh.line.dash_style = MSO_LINE.DASH
    else:
        sh.line.fill.background()
    if rot:
        sh.rotation = rot
    sh.text_frame.text = ""
    return sh


def R(t, size=12, bold=False, color=INK, font=BODY, italic=False):
    return (t, dict(size=size, bold=bold, color=color, font=font, italic=italic))


def text(s, x, y, w, h, paras, anchor="top", rot=0, margin=0.03, shape=None, wrap=True):
    """paras: str | list of runs | dict(runs=[...], align='l'|'c'|'r', after=pt, line=float)."""
    tb = shape if shape is not None else s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = wrap
    for side in ("left", "right", "top", "bottom"):
        setattr(tf, f"margin_{side}", Inches(margin))
    tf.vertical_anchor = {"top": MSO_ANCHOR.TOP, "middle": MSO_ANCHOR.MIDDLE, "bottom": MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(paras, (str, tuple)):
        paras = [paras]
    first = True
    for p in paras:
        if isinstance(p, str):
            p = {"runs": [R(p)]}
        elif isinstance(p, tuple):
            p = {"runs": [p]}
        elif isinstance(p, list):
            p = {"runs": p}
        para = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        para.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[p.get("align", "l")]
        if "after" in p:
            para.space_after = Pt(p["after"])
        if "before" in p:
            para.space_before = Pt(p["before"])
        if "line" in p:
            para.line_spacing = p["line"]
        for t, o in p["runs"]:
            r = para.add_run(); r.text = t
            f = r.font; f.size = Pt(o["size"]); f.bold = o["bold"]; f.italic = o["italic"]
            f.color.rgb = rgb(o["color"]); f.name = o["font"]
    if rot:
        tb.rotation = rot
    return tb


def bullets(items, size=12, color=INK, gap=4, mark="•", mcolor=None, font=BODY):
    out = []
    for it in items:
        runs = it if isinstance(it, list) else [R(it, size, color=color, font=font)]
        out.append({"runs": [R(mark + "  ", size, True, mcolor or color, font=font)] + runs, "after": gap})
    return out


def notes(s, t):
    s.notes_slide.notes_text_frame.text = t


def wobble_box(s, x, y, w, h, color=INK, lw=1.75, jitter=0.03, seed=None, fill=None):
    """Hand-drawn rectangle: a closed freeform whose corners and edges wobble slightly."""
    rnd = random.Random(seed)
    E = 914400
    pts = []
    def j():
        return rnd.uniform(-jitter, jitter)
    corners = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    for i in range(4):
        (ax, ay), (bx, by) = corners[i], corners[(i + 1) % 4]
        for t in (0.0, 0.33, 0.66):
            pts.append((ax + (bx - ax) * t + j(), ay + (by - ay) * t + j()))
    b = s.shapes.build_freeform(int(pts[0][0] * E), int(pts[0][1] * E), scale=1.0)
    b.add_line_segments([(int(px * E), int(py * E)) for px, py in pts[1:]] + [(int((x + j()) * E), int((y + j()) * E))], close=True)
    sh = b.convert_to_shape()
    _noshadow(sh)
    if fill:
        sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    else:
        sh.fill.background()
    sh.line.color.rgb = rgb(color); sh.line.width = Pt(lw)
    return sh


def hand_line(s, x1, y1, x2, y2, color=INK, lw=1.5, dash=False, arrow=False):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color); c.line.width = Pt(lw)
    if dash:
        c.line.dash_style = MSO_LINE.DASH
    if arrow:
        ln = c.line._get_or_add_ln()
        tail = ln.makeelement(qn("a:tailEnd"), {"type": "triangle", "w": "med", "len": "med"})
        ln.append(tail)
    return c


def blue_arrow(s, x, y, w=0.45, h=0.26, rot=0):
    return rect(s, x, y, w, h, BLUE, None, shape=MSO_SHAPE.RIGHT_ARROW, rot=rot)


def red_circle(s, x, y, w, h, lw=2.0, color=RED):
    return rect(s, x, y, w, h, None, color, lw, shape=MSO_SHAPE.OVAL)


def sticky(s, x, y, w, h, color="yellow", rot=0.0, paras=None, anchor="top", pad=0.16, shadow=True):
    """Watercolour sticky note with the template's offset shadow."""
    if shadow:
        rect(s, x + 0.06, y + 0.08, w, h, SHADOW, None, rot=rot)
    pic(s, WASH[color], x, y, w, h, rot=rot)
    if paras is not None:
        text(s, x + pad, y + pad * 0.8, w - 2 * pad, h - 1.6 * pad, paras, anchor=anchor, rot=rot)


def brush_label(s, x, y, label, size=24, color="yellow", w=None, ink=INK, rot=-0.6):
    """Short heading on a painted highlighter stroke (the template's yellow title bar)."""
    if w is None:
        w = 0.6 + len(label) * size * 0.0098
    pic(s, BRUSH[color], x - 0.12, y - 0.02, w + 0.3, size / 72 * 1.55, rot=rot)
    text(s, x, y - 0.06, w + 0.6, size / 72 * 1.6, [[R(label, size, True, ink, HAND)]], anchor="middle")


def page_badge(s, n):
    rect(s, 12.25, 6.77, 0.6, 0.5, None, INK, 1.5, shape=MSO_SHAPE.OVAL)
    text(s, 12.25, 6.77, 0.6, 0.5, [{"runs": [R(str(n), 12, True, INK, BODY_SB)], "align": "c"}], anchor="middle")


def footer(s, src=None):
    text(s, 0.45, 7.0, 6.0, 0.25, [[R("ALBERTA SCHOOL OF BUSINESS", 8, True, BLUE, BODY_SB), R("  ·  University of Alberta  ·  SEM 620 Team 2", 8, False, BLUE)]])
    if src:
        text(s, 0.45, 6.62, 11.5, 0.36, [[R(src, 7.5, False, GREY)]], anchor="bottom")


def base(d, kicker=None, title=None, src=None, kcolor="yellow", tsize=21, number=True):
    s = d.prs.slides.add_slide(d.blank)
    d.page += 1
    pic(s, "canvas", 0, 0, 13.333, 7.5)
    if kicker:
        brush_label(s, 0.55, 0.32, kicker, 22, kcolor)
    if title:
        tl = title if isinstance(title, list) else [title]
        runs = []
        for part in tl:
            if isinstance(part, tuple):
                runs.append(R(part[0], tsize, True, BLUE if len(part) < 2 else part[1], BODY_SB))
            else:
                runs.append(R(part, tsize, True, INK, BODY_SB))
        text(s, 0.55, 0.98, 12.2, 0.9, [{"runs": runs, "line": 0.95}])
    footer(s, src)
    if number:
        page_badge(s, d.page)
    return s


def portrait(s, who, x, y, size=1.3):
    """Team character in a painted gold frame."""
    pic(s, os.path.join(CAST_DIR, who + ".png"), x + size * 0.1, y + size * 0.1, size * 0.8, size * 0.8)
    pic(s, "frame", x, y, size, size)


def tag(s, x, y, label, color=BLUE, size=8.5, w=None):
    """Small handwritten concept tag, e.g. 'S2 · Profit tree'."""
    w = w or (0.22 + len(label) * size * 0.0072)
    rect(s, x, y, w, 0.27, None, color, 1.0, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, x, y, w, 0.27, [{"runs": [R(label, size, True, color, BODY_SB)], "align": "c"}], anchor="middle", margin=0.01)
    return w


def table(s, x, y, colw, rows, rowh, size=9.5, header_color="yellow", hsize=None, line=INK, zebra=None, bold_first=True):
    """Sketch table: header on a paint wash, hand-drawn rules, text boxes per cell.
    rows[0] is the header. rowh: float or list (header height first)."""
    hs = hsize or size
    if not isinstance(rowh, (list, tuple)):
        rowh = [rowh] * len(rows)
    W = sum(colw)
    pic(s, WASH[header_color], x - 0.04, y - 0.02, W + 0.08, rowh[0] + 0.04)
    yy = y
    for ri, row in enumerate(rows):
        h = rowh[ri]
        if zebra and ri > 0 and ri % 2 == 0:
            rect(s, x, yy, W, h, zebra)
        xx = x
        for ci, cell in enumerate(row):
            if ri == 0:
                paras = [[R(cell, hs, True, INK, BODY_SB)]]
            elif isinstance(cell, (list, dict)):
                paras = cell if isinstance(cell, list) and cell and isinstance(cell[0], (dict, list)) else [cell]
            else:
                paras = [[R(str(cell), size, bold_first and ci == 0, INK, BODY_SB if (bold_first and ci == 0) else BODY)]]
            text(s, xx + 0.05, yy + 0.03, colw[ci] - 0.1, h - 0.06, paras, anchor="middle" if ri == 0 else "top")
            xx += colw[ci]
        yy += h
        hand_line(s, x, yy, x + W, yy, line if ri == 0 else "B9B3A3", 1.25 if ri == 0 else 0.6)
    return yy


def concepts(s, labels, y=6.28, x=0.55):
    """Row of course-concept tags at the bottom of a slide."""
    text(s, x, y, 1.2, 0.27, [[R("COURSE CONCEPTS", 7.5, True, GREY, BODY_SB)]], anchor="middle")
    xx = x + 1.2
    for lb in labels:
        w = tag(s, xx, y, lb, BLUE, 7.5)
        xx += w + 0.08
