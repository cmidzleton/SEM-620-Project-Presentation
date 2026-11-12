from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.dml import MSO_PATTERN
from pptx.oxml.ns import qn

# ---------- theme: industrial / futuristic console ----------
FONT = "Inter"
FONT_D = "Inter Display"
MONO = "JetBrains Mono"

BG0 = "0B0E13"; BG1 = "121720"; BG2 = "1A2130"; BG3 = "222B3B"
LINE = "2B3444"; LINE2 = "3A465A"
TXT = "EEF2F7"; MUT = "9AA6B8"; DIM = "66728A"
AMBER = "FFB224"; AMBER_D = "8A5A00"; CYAN = "41D4F0"; CYAN_D = "0E5A6B"
GREEN = "3ED598"; GREEN_D = "0F5A3C"; RED = "FF5A5F"; RED_D = "7A1F22"
ORANGE = "F2873C"; GOLD = "E3B92B"; VIOLET = "A78BFA"; WHITE = "FFFFFF"; BLACK = "000000"

LENS = {
    "lauren": ("LOGICAL LAUREN", "RATIONAL", CYAN, "lauren.png"),
    "nav": ("NEURO NAV", "PSYCHOLOGICAL", ORANGE, "nav.png"),
    "rick": ("RULING RICK", "POLITICAL", GOLD, "rick.png"),
}
ASSETS = "/mnt/project-files/final-presentation/assets/"
IMG = "/tmp/claude-0/sc/build/img/"
W, H = 13.333, 7.5


def rgb(h):
    return RGBColor.from_string(h)


class Deck:
    def __init__(self, total_core):
        self.prs = Presentation()
        self.prs.slide_width = Emu(12192000)
        self.prs.slide_height = Emu(6858000)
        self.blank = self.prs.slide_layouts[6]
        self.page = 0
        self.total_core = total_core

    def save(self, path):
        self.prs.save(path)


def _noshadow(sh):
    try:
        sh.shadow.inherit = False
    except Exception:
        pass


def rect(s, x, y, w, h, fill=None, line=None, lw=0.75, shape=MSO_SHAPE.RECTANGLE, radius=None, dash=None):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    _noshadow(sh)
    if fill:
        sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    else:
        sh.fill.background()
    if line:
        sh.line.color.rgb = rgb(line); sh.line.width = Pt(lw)
        if dash:
            sh.line.dash_style = dash
    else:
        sh.line.fill.background()
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = radius
    sh.text_frame.text = ""
    return sh


def rrect(s, x, y, w, h, fill=BG1, line=LINE, lw=0.75, radius=0.05):
    return rect(s, x, y, w, h, fill, line, lw, MSO_SHAPE.ROUNDED_RECTANGLE, radius)


def hazard(s, x, y, w, h, fg=AMBER, bg=BG0):
    rect(s, x, y, w, h, bg)
    step = h * 2.2; cx = x
    while cx < x + w - step:
        sh = rect(s, cx, y, step * 0.5, h, fg, shape=MSO_SHAPE.PARALLELOGRAM)
        cx += step


def _spc(run, spc):
    rPr = run._r.get_or_add_rPr(); rPr.set("spc", str(int(spc)))


def text(s, x, y, w, h, paras, anchor="top", margin=(0.02, 0.02, 0.02, 0.02), shape=None):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)) if shape is None else shape
    tf = tb.text_frame; tf.word_wrap = True
    l, t, r, b = margin
    tf.margin_left, tf.margin_top, tf.margin_right, tf.margin_bottom = Inches(l), Inches(t), Inches(r), Inches(b)
    tf.vertical_anchor = {"top": MSO_ANCHOR.TOP, "middle": MSO_ANCHOR.MIDDLE, "bottom": MSO_ANCHOR.BOTTOM}[anchor]
    first = True
    for para in paras:
        if isinstance(para, str):
            para = {"runs": [(para, {})]}
        elif isinstance(para, list):
            para = {"runs": para}
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[para.get("align", "l")]
        if "after" in para: p.space_after = Pt(para["after"])
        if "before" in para: p.space_before = Pt(para["before"])
        if "line" in para: p.line_spacing = para["line"]
        for rt in para["runs"]:
            if isinstance(rt, str): rt = (rt, {})
            t, o = rt
            r = p.add_run(); r.text = t
            f = r.font
            f.size = Pt(o.get("size", 11)); f.bold = o.get("bold", False); f.italic = o.get("italic", False)
            f.name = o.get("font", FONT)
            f.color.rgb = rgb(o.get("color", TXT))
            if "spc" in o: _spc(r, o["spc"])
    return tb


def R(t, **o):
    return (t, o)


def M(t, **o):
    o.setdefault("font", MONO); return (t, o)


def line(s, x1, y1, x2, y2, color=LINE2, lw=1.0, dash=None):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color); c.line.width = Pt(lw)
    if dash: c.line.dash_style = dash
    return c


def elbow(s, x1, y1, x2, y2, color=LINE2, lw=1.0, xm=None):
    """horizontal-vertical-horizontal connector"""
    xm = (x1 + x2) / 2 if xm is None else xm
    line(s, x1, y1, xm, y1, color, lw); line(s, xm, y1, xm, y2, color, lw); line(s, xm, y2, x2, y2, color, lw)


# ---------- chrome ----------
def console(d, s, story, appendix=False, label=None):
    rect(s, 0, 0, W, 0.5, BG1)
    rect(s, 0, 0.5, W, 0.012, LINE2)
    # 311 badge
    b = rrect(s, 0.3, 0.1, 0.72, 0.3, AMBER if not appendix else BG3, None, radius=0.15)
    text(s, 0.3, 0.1, 0.72, 0.3, [{"runs": [M("311", size=11, bold=True, color=BG0 if not appendix else MUT)], "align": "c"}], anchor="middle", shape=b, margin=(0, 0, 0, 0))
    text(s, 1.15, 0.08, 7.6, 0.34, [[M(story, size=9.5, color=MUT, spc=60)]], anchor="middle")
    # progress segments
    if not appendix:
        n = d.total_core; x0 = 9.0; seg_w = 2.9 / n
        for i in range(n):
            col = AMBER if i < d.page else (CYAN if i == d.page - 0 else BG3)
            col = AMBER if i + 1 <= d.page else BG3
            rect(s, x0 + i * seg_w, 0.21, seg_w - 0.03, 0.08, col)
        text(s, 11.95, 0.08, 1.1, 0.34, [{"runs": [M(f"{d.page:02d}", size=11, bold=True, color=TXT), M(f" / {n:02d}", size=9, color=DIM)], "align": "r"}], anchor="middle")
    else:
        text(s, 9.0, 0.08, 4.05, 0.34, [{"runs": [M(label or "APPENDIX", size=9, bold=True, color=DIM, spc=200)], "align": "r"}], anchor="middle")


def footer(s, page, foot="", label="TEAM 2 · REFERRAL CHECK · EDMONTON 311"):
    rect(s, 0.3, 7.02, W - 0.6, 0.008, LINE)
    text(s, 0.3, 7.06, 3.4, 0.3, [[M(label, size=6.5, color=DIM, spc=150)]], anchor="middle")
    if foot:
        text(s, 3.6, 7.05, 9.0, 0.42, [[R(foot, size=6.3, color=DIM)]], anchor="top")
    text(s, 12.6, 7.06, 0.45, 0.3, [{"runs": [M(str(page), size=8, bold=True, color=MUT)], "align": "r"}], anchor="middle")


def new_slide(d, story, foot="", appendix=False, page_label=None, label=None):
    s = d.prs.slides.add_slide(d.blank)
    bg = s.background.fill; bg.solid(); bg.fore_color.rgb = rgb(BG0)
    d.page += 1
    console(d, s, story, appendix, label)
    footer(s, page_label or d.page, foot)
    return s


def kicker(s, x, y, w, t, color=CYAN, size=8.5):
    return text(s, x, y, w, 0.25, [[M(t, size=size, bold=True, color=color, spc=220)]])


def title(s, runs, x=0.3, y=0.9, w=12.7, h=0.9, size=23):
    rs = []
    for t in runs:
        if isinstance(t, tuple):
            rs.append(R(t[0], size=size, bold=True, color=AMBER, font=FONT_D))
        else:
            rs.append(R(t, size=size, color=TXT, font=FONT_D, bold=True))
    return text(s, x, y, w, h, [{"runs": rs, "line": 0.98}])


def headline(s, kick, runs, y=0.68, size=22):
    kicker(s, 0.3, y, 12.7, kick)
    title(s, runs, y=y + 0.27, size=size, h=0.85)


def panel(s, x, y, w, h, head=None, head_color=CYAN, fill=BG1, line_c=LINE, top=None, body=None, body_size=10.5, pad=0.14):
    rrect(s, x, y, w, h, fill, line_c, radius=0.04)
    if top:
        rect(s, x + 0.01, y, w - 0.02, 0.05, top)
    cy = y + pad
    if head:
        text(s, x + pad, cy, w - 2 * pad, 0.24, [[M(head, size=7.5, bold=True, color=head_color, spc=200)]])
        cy += 0.28
    if body:
        text(s, x + pad, cy, w - 2 * pad, h - (cy - y) - pad * 0.5, body)
    return cy


def stat(s, x, y, w, h, num, label, sub=None, color=TXT, num_size=28, fill=BG1, line_c=LINE, top=None):
    rrect(s, x, y, w, h, fill, line_c, radius=0.04)
    if top: rect(s, x + 0.01, y, w - 0.02, 0.05, top)
    text(s, x + 0.14, y + 0.1, w - 0.28, 0.6, [[M(num, size=num_size, bold=True, color=color)]], anchor="top")
    text(s, x + 0.14, y + 0.12 + num_size / 72 * 1.25, w - 0.28, 0.5, [[R(label, size=9, color=TXT)]] + ([[R(sub, size=7.5, color=MUT)]] if sub else []))


def chip(s, x, y, t, color=MUT, w=None, size=6.5, fill=None, h=0.22):
    w = w or (0.16 + 0.062 * len(t))
    p = rrect(s, x, y, w, h, fill or BG0, color, lw=0.75, radius=0.5)
    text(s, x, y, w, h, [{"runs": [M(t, size=size, bold=True, color=color, spc=80)]}, ], anchor="middle", shape=p, margin=(0, 0, 0, 0))
    for para in p.text_frame.paragraphs: para.alignment = PP_ALIGN.CENTER
    return w


def chips(s, x, y, items, gap=0.08, size=6.5, h=0.22):
    """items: list of (text, color)"""
    cx = x
    for t, c in items:
        cx += chip(s, cx, y, t, c, size=size, h=h) + gap
    return cx


def concept_strip(s, items, y=6.72):
    text(s, 0.3, y, 1.25, 0.22, [[M("CONCEPTS USED", size=6.5, bold=True, color=DIM, spc=180)]], anchor="middle")
    chips(s, 1.55, y, items, size=6.3)


def tier(s, x, y, w, h, name, color, dark):
    p = rrect(s, x, y, w, h, dark, color, lw=1, radius=0.04)
    text(s, x, y, w, h, [{"runs": [M(name, size=8.5, bold=True, color=color, spc=200)], "align": "c"}], anchor="middle", shape=p, margin=(0, 0, 0, 0))
    return p


def person(s, who, x, y, w, h, quote, tag=None, qsize=10, fill=BG1):
    name, lens, col, img = LENS[who]
    rrect(s, x, y, w, h, fill, col, lw=1.0, radius=0.06)
    sz = min(0.6, h - 0.2)
    s.shapes.add_picture(ASSETS + img, Inches(x + 0.1), Inches(y + 0.1), Inches(sz), Inches(sz))
    head = [M(name, size=7.5, bold=True, color=col, spc=120), M("  ·  " + (tag or lens), size=7, color=MUT, spc=100)]
    text(s, x + sz + 0.2, y + 0.08, w - sz - 0.3, 0.24, [head])
    text(s, x + sz + 0.2, y + 0.31, w - sz - 0.3, h - 0.36, [[R(quote, size=qsize, color=TXT)]])


def table(s, x, y, w, h, rows, colw=None, sizes=None, fills=None, head_fill=BG3, bold_first_col=False, row_h=None, head_color=CYAN, zebra=True):
    nr, nc = len(rows), len(rows[0])
    gt = s.shapes.add_table(nr, nc, Inches(x), Inches(y), Inches(w), Inches(h))
    tbl = gt.table
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "0"); tblPr.set("bandRow", "0")
    # remove style id so no default theme borders
    if colw:
        for i, cw in enumerate(colw): tbl.columns[i].width = Inches(cw)
    for ri, row in enumerate(rows):
        if row_h: tbl.rows[ri].height = Inches(row_h if ri else max(row_h, 0.28))
        for ci, val in enumerate(row):
            cell = tbl.cell(ri, ci)
            cell.margin_left = cell.margin_right = Inches(0.07)
            cell.margin_top = cell.margin_bottom = Inches(0.03)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            if ri == 0: f = head_fill
            elif fills and fills.get((ri, ci)): f = fills[(ri, ci)]
            elif fills and fills.get((ri, None)): f = fills[(ri, None)]
            else: f = BG1 if (ri % 2 or not zebra) else BG2
            cell.fill.solid(); cell.fill.fore_color.rgb = rgb(f)
            size = (sizes[ci] if sizes else 8.5)
            tf = cell.text_frame; tf.word_wrap = True
            runs = val if isinstance(val, list) else [R(str(val))]
            p = tf.paragraphs[0]
            for rt in runs:
                if isinstance(rt, str): rt = (rt, {})
                t, o = rt
                r = p.add_run(); r.text = t
                if ri == 0:
                    r.font.name = MONO; r.font.size = Pt(o.get("size", 7)); r.font.bold = True; r.font.color.rgb = rgb(head_color)
                    _spc(r, 120)
                else:
                    r.font.name = o.get("font", FONT)
                    r.font.size = Pt(o.get("size", size)); r.font.bold = o.get("bold", bold_first_col and ci == 0)
                    r.font.color.rgb = rgb(o.get("color", TXT))
    return tbl


def notes(s, t):
    s.notes_slide.notes_text_frame.text = t


def arrow(s, x, y, w, h, color=LINE2, shape=MSO_SHAPE.RIGHT_ARROW):
    return rect(s, x, y, w, h, color, shape=shape)


def node(s, x, y, w, h, head, body=None, color=CYAN, fill=BG1, head_size=7.5, body_size=9, tag=None, tag_color=None, align="l"):
    rrect(s, x, y, w, h, fill, LINE, radius=0.04)
    rect(s, x, y + 0.02, 0.05, h - 0.04, color)
    paras = [[M(head, size=head_size, bold=True, color=color, spc=100)]]
    if body:
        paras.append({"runs": [R(body, size=body_size, color=TXT)], "before": 2})
    text(s, x + 0.14, y + 0.07, w - 0.2, h - 0.12, paras)
    if tag:
        chip(s, x + w - 0.1 - (0.16 + 0.062 * len(tag)), y + h - 0.27, tag, tag_color or MUT, size=5.8, h=0.19)


def big_ghost(s, t, x, y, w, h, size=160, color=BG2):
    text(s, x, y, w, h, [{"runs": [M(t, size=size, bold=True, color=color)], "align": "r"}], anchor="middle")
