from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from pptx.oxml.ns import qn
import copy

FONT = "Segoe UI"
FONT_SB = "Segoe UI Semibold"
FONT_BK = "Segoe UI Black"

def rgb(h):
    return RGBColor.from_string(h)

NAVY = "23364A"; NAVY2 = "193A5A"; BLUE = "0072A8"; SLATE = "52657A"; RED = "CF464D"
ORANGE = "E1853E"; YELLOW = "F2C94C"; GOLD = "8A6D00"; BG = "D3E3EE"; WHITE = "FFFFFF"
GREEN = "2E7D4F"; LBLUE = "E3F1F9"; LORANGE = "FCEFE3"; LYELLOW = "FDF6D8"; LRED = "FBE4E4"
LGREEN = "E4F2EA"; LINE = "B7CADC"; MID = "35597F"; DGOLD = "E3B92B"

ASSETS = "/mnt/project-files/final-presentation/assets/"
CAST = {
    "lauren": ("LOGICAL LAUREN", "lauren.png", BLUE, LBLUE, BLUE),
    "nav": ("NEURO NAV", "nav.png", ORANGE, LORANGE, "B85D1C"),
    "rick": ("RULING RICK", "rick.png", DGOLD, LYELLOW, GOLD),
}

TOTAL = 900  # seconds, core talk

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

def rect(s, x, y, w, h, fill=None, line=None, lw=0.75, shape=MSO_SHAPE.RECTANGLE, radius=None):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    _noshadow(sh)
    if fill:
        sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    else:
        sh.fill.background()
    if line:
        sh.line.color.rgb = rgb(line); sh.line.width = Pt(lw)
    else:
        sh.line.fill.background()
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = radius
    sh.text_frame.text = ""
    return sh

def rrect(s, x, y, w, h, fill=WHITE, line=None, lw=0.75, radius=0.06):
    return rect(s, x, y, w, h, fill, line, lw, MSO_SHAPE.ROUNDED_RECTANGLE, radius)

def _spc(run, spc):
    rPr = run._r.get_or_add_rPr()
    rPr.set("spc", str(int(spc)))

def text(s, x, y, w, h, paras, anchor="top", margin=(0.02, 0.02, 0.02, 0.02), shape=None, autofit=False):
    """paras: list of paragraphs; each paragraph is dict(runs=[(text, opts)], align, after, before, line)
    or a list of runs, or a string. opts: size,bold,color,font,italic,spc"""
    if shape is None:
        tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    else:
        tb = shape
    tf = tb.text_frame
    tf.word_wrap = True
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
            if isinstance(rt, str):
                rt = (rt, {})
            t, o = rt
            r = p.add_run(); r.text = t
            f = r.font
            f.size = Pt(o.get("size", 12)); f.bold = o.get("bold", False); f.italic = o.get("italic", False)
            f.name = o.get("font", FONT)
            f.color.rgb = rgb(o.get("color", NAVY))
            if "spc" in o: _spc(r, o["spc"])
    return tb

def R(t, **o):
    return (t, o)

def kicker(s, x, y, w, t, color=BLUE, size=10.5):
    y = 0.6 if abs(y-0.65)<1e-6 else y
    return text(s, x, y, w, 0.28, [[R(t, size=size, bold=True, color=color, spc=200)]])

def title(s, runs, x=0.5, y=0.86, w=12.3, h=0.95, size=25):
    rs = []
    for t in runs:
        if isinstance(t, tuple):
            rs.append(R(t[0], size=size, bold=True, color=RED))
        else:
            rs.append(R(t, size=size, color=NAVY))
    return text(s, x, y, w, h, [{"runs": rs, "line": 0.95}])

def notes(s, t):
    s.notes_slide.notes_text_frame.text = t

def fmt_clock(sec):
    return f"{sec//60:02d}:{sec%60:02d}"

def callbar(s, story, elapsed=None, label="LIVE · 311 INTAKE", pill=RED, appendix=False):
    rect(s, 0, 0, 13.333, 0.48, NAVY)
    p = rrect(s, 0.33, 0.09, 1.95, 0.3, pill, radius=0.5)
    text(s, 0.33, 0.09, 1.95, 0.3, [{"runs": [R("● " + label, size=9, bold=True, color=WHITE, spc=150)], "align": "c"}], anchor="middle", shape=p)
    text(s, 2.45, 0.08, 7.3, 0.32, [[R(story, size=11.5, color=WHITE)]], anchor="middle")
    if appendix:
        text(s, 10.6, 0.08, 1.4, 0.32, [[R("APPENDIX", size=9, bold=True, color="C2D3E0", spc=150)]], anchor="middle")
        text(s, 12.0, 0.06, 1.1, 0.36, [{"runs": [R("--:--", size=17, bold=True, color=WHITE)], "align": "r"}], anchor="middle")
    else:
        codes = elapsed // 20
        text(s, 9.55, 0.08, 2.5, 0.32, [{"runs": [R(f"+{codes} ", size=10, bold=True, color=YELLOW), R("codes picked while you read", size=10, color="C2D3E0")], "align": "r"}], anchor="middle")
        text(s, 12.05, 0.06, 1.05, 0.36, [{"runs": [R(fmt_clock(elapsed), size=17, bold=True, color=WHITE)], "align": "r"}], anchor="middle")
        frac = min(1, elapsed / TOTAL)
        if frac > 0:
            rect(s, 0, 0.48, 13.333 * frac, 0.045, ORANGE)

def footer(s, page, foot="", label="EDMONTON 311 · ROUTE CHECK", lc=NAVY):
    rect(s, 0.33, 7.05, 12.67, 0.008, LINE)
    c = rect(s, 0.33, 7.1, 0.34, 0.34, NAVY, shape=MSO_SHAPE.OVAL)
    text(s, 0.33, 7.1, 0.34, 0.34, [{"runs": [R(str(page), size=10, bold=True, color=WHITE)], "align": "c"}], anchor="middle", shape=c, margin=(0, 0, 0, 0))
    text(s, 0.78, 7.13, 2.6, 0.28, [[R(label, size=7.5, bold=True, color=lc, spc=150)]], anchor="middle")
    if foot:
        text(s, 3.3, 7.08, 9.75, 0.4, [[R(foot, size=6.5, color=lc if lc != NAVY else SLATE)]], anchor="top")

def new_slide(d, story, elapsed=None, foot="", appendix=False, page_label=None):
    s = d.prs.slides.add_slide(d.blank)
    bg = s.background.fill; bg.solid(); bg.fore_color.rgb = rgb(BG)
    d.page += 1
    if appendix:
        callbar(s, story, label="ON HOLD", pill=SLATE, appendix=True)
    else:
        callbar(s, story, elapsed)
    footer(s, page_label or d.page, foot)
    return s

def card(s, x, y, w, h, head=None, head_color=BLUE, fill=WHITE, line=None, top=None, body=None, body_size=11.5, pad=0.15):
    rrect(s, x, y, w, h, fill, line, radius=0.05)
    if top:
        rect(s, x, y, w, 0.06, top)
    cy = y + pad
    if head:
        text(s, x + pad, cy, w - 2 * pad, 0.27, [[R(head, size=9.5, bold=True, color=head_color, spc=150)]])
        cy += 0.3
    if body:
        text(s, x + pad, cy, w - 2 * pad, h - (cy - y) - pad * 0.6, body)

def person(s, who, x, y, w, h, quote, tag=None, qsize=11):
    name, img, border, fill, dark = CAST[who]
    rrect(s, x, y, w, h, fill, border, lw=1.25, radius=0.08)
    sz = min(0.62, h - 0.2)
    s.shapes.add_picture(ASSETS + img, Inches(x + 0.1), Inches(y + 0.1), Inches(sz), Inches(sz))
    head = [R(name, size=8.5, bold=True, color=dark, spc=120)]
    if tag:
        head += [R("  ·  " + tag, size=8.5, bold=True, color=dark, spc=120)]
    text(s, x + sz + 0.2, y + 0.07, w - sz - 0.3, 0.25, [head])
    text(s, x + sz + 0.2, y + 0.3, w - sz - 0.3, h - 0.35, [[R(quote, size=qsize, color=NAVY)]])

def label_chip(s, x, y, t, color, w=None):
    w = w or (0.12 + 0.075 * len(t))
    p = rrect(s, x, y, w, 0.22, WHITE, color, lw=1, radius=0.5)
    text(s, x, y, w, 0.22, [{"runs": [R(t, size=7, bold=True, color=color, spc=100)], "align": "c"}], anchor="middle", shape=p, margin=(0, 0, 0, 0))

def arrow(s, x, y, w, h, color=SLATE, shape=MSO_SHAPE.RIGHT_ARROW):
    return rect(s, x, y, w, h, color, shape=shape)

def table(s, x, y, w, h, rows, colw=None, header_fill=NAVY, sizes=None, fills=None, bold_first_col=False, row_h=None):
    nr, nc = len(rows), len(rows[0])
    gt = s.shapes.add_table(nr, nc, Inches(x), Inches(y), Inches(w), Inches(h))
    tbl = gt.table
    # strip style banding
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "0"); tblPr.set("bandRow", "0")
    if colw:
        for i, cw in enumerate(colw):
            tbl.columns[i].width = Inches(cw)
    for ri, row in enumerate(rows):
        if row_h:
            tbl.rows[ri].height = Inches(row_h if ri else max(row_h, 0.3))
        for ci, val in enumerate(row):
            cell = tbl.cell(ri, ci)
            cell.margin_left = cell.margin_right = Inches(0.07)
            cell.margin_top = cell.margin_bottom = Inches(0.035)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            if ri == 0:
                f = header_fill
            elif fills and fills.get((ri, ci)):
                f = fills[(ri, ci)]
            elif fills and fills.get((ri, None)):
                f = fills[(ri, None)]
            else:
                f = WHITE if ri % 2 else "F3F7FA"
            cell.fill.solid(); cell.fill.fore_color.rgb = rgb(f)
            size = (sizes[ci] if sizes else 9.5)
            tf = cell.text_frame; tf.word_wrap = True
            runs = val if isinstance(val, list) else [R(str(val))]
            p = tf.paragraphs[0]
            for rt in runs:
                if isinstance(rt, str): rt = (rt, {})
                t, o = rt
                r = p.add_run(); r.text = t
                r.font.name = FONT
                if ri == 0:
                    r.font.size = Pt(o.get("size", 8.5)); r.font.bold = True; r.font.color.rgb = rgb(WHITE)
                else:
                    r.font.size = Pt(o.get("size", size)); r.font.bold = o.get("bold", bold_first_col and ci == 0)
                    r.font.color.rgb = rgb(o.get("color", NAVY))
    return tbl
