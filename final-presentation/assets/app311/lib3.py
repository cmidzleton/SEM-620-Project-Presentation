from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.dml import MSO_PATTERN
from pptx.oxml.ns import qn

# ---------- theme: industrial / futuristic console ----------
FONT = "Quattrocento Sans"
FONT_D = "Quattrocento Sans"
MONO = "Quattrocento Sans"

BG0 = "121417"; BG1 = "1C1F24"; BG2 = "24282F"; BG3 = "2E333B"
LINE = "2E333B"; LINE2 = "3D434D"
TXT = "F5F5F5"; MUT = "9AA0A8"; DIM = "555B63"
EDM = "0057B8"; EDM_L = "5AA9FF"; EDM_D = "003B7E"; EDM_LT = "E8F1FF"; ETS_BLUE = "1F4FBF"; ETS_GREY = "C9CDD2"
AMBER = "F2A900"; AMBER_D = "6B4A00"; CYAN = EDM_L; CYAN_D = EDM_D
GREEN = "3DBE7A"; GREEN_D = "15502F"; RED = "E5484D"; RED_D = "6E1F22"
ORANGE = "F2873C"; GOLD = "E3B92B"; VIOLET = "A78BFA"; WHITE = "FFFFFF"; BLACK = "000000"

LENS = {
    "lauren": ("LOGICAL LAUREN", "RATIONAL", CYAN, "lauren.png"),
    "nav": ("NEURO NAV", "PSYCHOLOGICAL", ORANGE, "nav.png"),
    "rick": ("RULING RICK", "POLITICAL", GOLD, "rick.png"),
}
ASSETS = "/mnt/project-files/final-presentation/assets/"
IMG = "/tmp/claude-0/sc/build/img/"
W, H = 13.333, 7.5

# ---------- content-zone transform: build2 coordinates (0.3..13.03 x 1.9..6.65) -> template zone (0.5..12.88 x 1.8..6.3) ----------
XF = False            # on while slide content is drawn; off for chrome
X0, X1 = 0.3, 13.03
Y0, Y1 = 1.9, 6.65
NX0, NX1 = 0.5, 12.88
NY0, NY1 = 1.76, 6.24
KX = (NX1 - NX0) / (X1 - X0); KY = (NY1 - NY0) / (Y1 - Y0); FSC = 1.1


def inzone(y):
    return XF and y >= 1.85


def T(x, y, w=None, h=None):
    if not inzone(y):
        return x, y, w, h
    return NX0 + (x - X0) * KX, NY0 + (y - Y0) * KY, (None if w is None else w * KX), (None if h is None else h * KY)


def fs(size, y):
    return size * FSC if (inzone(y) and size <= 13) else size


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
    x, y, w, h = T(x, y, w, h)
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
    rPr = run._r.get_or_add_rPr(); rPr.set("spc", str(int(spc * 0.2)))


def text(s, x, y, w, h, paras, anchor="top", margin=(0.02, 0.02, 0.02, 0.02), shape=None):
    y_orig = y
    x, y, w, h = T(x, y, w, h)
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
            f.size = Pt(fs(o.get("size", 11), y_orig)); f.bold = o.get("bold", False); f.italic = o.get("italic", False)
            f.name = o.get("font", FONT)
            f.color.rgb = rgb(o.get("color", TXT))
            if "spc" in o: _spc(r, o["spc"])
    return tb


def R(t, **o):
    return (t, o)


def M(t, **o):
    o.setdefault("font", MONO); return (t, o)


def line(s, x1, y1, x2, y2, color=LINE2, lw=1.0, dash=None):
    x1, y1, _, _ = T(x1, y1); x2, y2, _, _ = T(x2, y2)
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color); c.line.width = Pt(lw)
    if dash: c.line.dash_style = dash
    return c


def elbow(s, x1, y1, x2, y2, color=LINE2, lw=1.0, xm=None):
    """horizontal-vertical-horizontal connector"""
    xm = (x1 + x2) / 2 if xm is None else xm
    line(s, x1, y1, xm, y1, color, lw); line(s, xm, y1, xm, y2, color, lw); line(s, xm, y2, x2, y2, color, lw)


# ---------- chrome (template + 311 app feel) ----------
SECTIONS = ["01 Decision", "02 Algorithm", "03 Lenses", "04 Data & plan", "05 Appendix"]
NAV = []          # (shape, kind, payload): kind in section | back | home ; wired to slides by link_nav() once every slide exists
APPX = {}         # appendix page label -> slide
CUR = {"section": 0, "appendix": False}


def bus(s, x, y, w=0.95, facing_right=True, detail=False):
    """ETS-style city bus drawn from shapes, after the team's reference photo: blue upper body, white belt stripe,
    silver skirt, black glass, two doors, amber destination sign. (x, y) is top-left; total height about 0.26 * w."""
    h = w * 0.225; r = w * 0.036; glass = "10151F"; OV = MSO_SHAPE.OVAL
    body = rrect(s, x, y, w, h, ETS_BLUE, None, radius=0.14)
    rrect(s, x, y + h * 0.42, w, h * 0.58, ETS_GREY, None, radius=0.24)               # silver skirt, rounded at the bottom
    rect(s, x, y + h * 0.3, w, h * 0.27, ETS_BLUE)                                    # blue back over the skirt's top corners
    rect(s, x, y + h * 0.555, w, h * 0.05, WHITE)                                     # belt stripe
    top = y + h * 0.17; gh = h * 0.33
    for a, ww in [(0.075, 0.115), (0.205, 0.115), (0.50, 0.115), (0.63, 0.115), (0.765, 0.082)]:
        rect(s, x + w * a, top, w * ww, gh, glass)                                    # side windows
    for a, ww in [(0.352, 0.052), (0.41, 0.052), (0.868, 0.037), (0.909, 0.037)]:
        rect(s, x + w * a, top, w * ww, h * 0.72, glass)                              # middle and front doors
    if detail:
        text(s, x + w * 0.767, top + gh * 0.02, w * 0.078, gh * 0.4, [{"runs": [R("311", size=max(3, w * 1.9), bold=True, color=AMBER)], "align": "c"}], anchor="middle", margin=(0, 0, 0, 0))
        text(s, x + w * 0.40, y + h * 0.005, w * 0.36, h * 0.17, [{"runs": [R("Edmonton Transit Service", size=max(3, w * 1.75), bold=True, italic=True, color=WHITE)], "align": "r"}], anchor="middle", margin=(0, 0, 0, 0))
        ad = rect(s, x + w * 0.50, y + h * 0.645, w * 0.245, h * 0.27, WHITE)
        text(s, 0, 0, 1, 1, [{"runs": [R("Referral Check", size=max(3, w * 2.1), bold=True, color=EDM)], "align": "c", "line": 0.85}, {"runs": [R("a 20-second check", size=max(2.5, w * 1.35), color="333333")], "align": "c", "line": 0.85}], anchor="middle", shape=ad, margin=(0, 0, 0, 0))
    else:
        rect(s, x + w * 0.775, top + gh * 0.08, w * 0.062, gh * 0.3, AMBER)           # destination sign
    for a in (0.215, 0.80):
        cx = x + w * a; cy = y + h * 0.99
        rect(s, cx - r, cy - r, 2 * r, 2 * r, "0B0B0B", shape=OV)
        rect(s, cx - r * 0.45, cy - r * 0.45, r * 0.9, r * 0.9, ETS_GREY, shape=OV)
    return body


def tabbar(s, active, appendix=False):
    """App-style bottom tab bar that doubles as the template's section menu; the bus parks on the active stop.
    Every tab is a link to that section's divider slide."""
    y = 6.6
    rect(s, 0.12, y, W - 0.12, 0.012, LINE2)
    n = len(SECTIONS); x0 = 0.5; span = 12.3; slot = span / n
    for i, name in enumerate(SECTIONS):
        cx = x0 + i * slot
        on = (i == active)
        if on:
            icon = bus(s, cx, y + 0.085, w=0.8)
        else:
            icon = rect(s, cx + 0.35, y + 0.15, 0.1, 0.1, BG3, shape=MSO_SHAPE.OVAL)
        tb = text(s, cx + 0.9, y + 0.05, slot - 1.0, 0.3, [[R(name, size=9.5, bold=on, color=TXT if on else DIM)]], anchor="middle")
        NAV.append((icon, "section", i)); NAV.append((tb, "section", i))


def console(d, s, story, appendix=False, label=None, active=0, count=True):
    """311-app header: status bar, back chevron (links to the previous slide), screen title, 311 badge (links to the agenda)."""
    rect(s, 0.12, 0, W - 0.12, 0.3, EDM_D)
    text(s, 0.45, 0.02, 2, 0.26, [[R("10:12", size=8, bold=True, color=WHITE)]], anchor="middle")
    text(s, 9.8, 0.02, 3.2, 0.26, [{"runs": [R("311  ·  LTE  ·  ▮▮▮", size=7.5, color=WHITE)], "align": "r"}], anchor="middle")
    rect(s, 0.12, 0.3, W - 0.12, 0.5, EDM)
    back = text(s, 0.45, 0.3, 0.4, 0.5, [[R("‹", size=20, bold=True, color=WHITE)]], anchor="middle")
    text(s, 0.85, 0.3, 9.5, 0.5, [[R(story, size=11.5, bold=True, color=WHITE)]], anchor="middle")
    b = rrect(s, 12.05, 0.37, 0.85, 0.36, WHITE, None, radius=0.12)
    text(s, 12.05, 0.37, 0.85, 0.36, [{"runs": [R("311", size=11, bold=True, color=EDM)], "align": "c"}], anchor="middle", shape=b, margin=(0, 0, 0, 0))
    NAV.append((back, "back", None)); NAV.append((b, "home", None))
    if appendix:
        text(s, 10.0, 0.3, 2.0, 0.5, [{"runs": [R(label or "APPENDIX", size=8.5, bold=True, color=WHITE)], "align": "r"}], anchor="middle")
    elif count:
        text(s, 10.3, 0.3, 1.7, 0.5, [{"runs": [R(f"{d.page:02d} / {d.total_core:02d}", size=9, color=WHITE)], "align": "r"}], anchor="middle")


def link_nav(d, dividers, home):
    """wire the app chrome: tabs -> section dividers, chevron -> previous slide, 311 badge -> agenda"""
    slides = list(d.prs.slides)
    index = {sl.slide_id: i for i, sl in enumerate(slides)}
    n = 0
    for shape, kind, payload in NAV:
        here = shape.part.slide
        target = None
        if kind == "section":
            target = dividers.get(payload)
        elif kind == "back":
            i = index[here.slide_id]
            target = slides[i - 1] if i > 0 else None
        elif kind == "home":
            target = home
        if target is not None and target.slide_id != here.slide_id:
            shape.click_action.target_slide = target; n += 1
    return n


def footer(s, page, foot="", label="ALBERTA SCHOOL OF BUSINESS  ·  University of Alberta  ·  Team 2"):
    text(s, 0.45, 7.06, 4.6, 0.26, [[R(label, size=7.5, bold=True, color=WHITE)]], anchor="middle")
    if foot:
        text(s, 5.0, 7.0, 7.0, 0.48, [[R(foot, size=6, color="747A84")]], anchor="top")
    text(s, 12.1, 7.06, 0.78, 0.26, [{"runs": [R(str(page), size=9, color=MUT)], "align": "r"}], anchor="middle")


def set_transition(s, kind="push", direction="l"):
    """PowerPoint slide transition (swipe feel). kind: push|wipe|cover."""
    from lxml import etree
    nsmap = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main", "p14": "http://schemas.microsoft.com/office/powerpoint/2010/main", "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006"}
    xml = (f'<mc:AlternateContent xmlns:mc="{nsmap["mc"]}" xmlns:p14="{nsmap["p14"]}" xmlns:p="{nsmap["p"]}">'
           f'<mc:Choice Requires="p14"><p:transition spd="med" p14:dur="500"><p:{kind} dir="{direction}"/></p:transition></mc:Choice>'
           f'<mc:Fallback><p:transition spd="med"><p:{kind} dir="{direction}"/></p:transition></mc:Fallback></mc:AlternateContent>')
    el = etree.fromstring(xml)
    sld = s._element
    # transition must follow clrMapOvr and precede timing/extLst
    anchor = sld.find("{%s}clrMapOvr" % nsmap["p"])
    if anchor is not None:
        anchor.addnext(el)
    else:
        sld.append(el)


def new_slide(d, story, foot="", appendix=False, page_label=None, label=None, section=0):
    global XF
    XF = False
    s = d.prs.slides.add_slide(d.blank)
    bg = s.background.fill; bg.solid(); bg.fore_color.rgb = rgb(BG0)
    d.page += 1
    rect(s, 0, 0, 0.12, H, EDM)                      # template's left accent bar
    console(d, s, story, appendix, label)
    tabbar(s, 4 if appendix else section, appendix)
    footer(s, page_label or d.page, foot)
    set_transition(s, "push", "l")
    CUR["section"] = 4 if appendix else section; CUR["appendix"] = appendix
    if appendix and page_label:
        APPX[page_label] = s
    XF = True
    return s


def raw_slide(d, count=True):
    """blank template slide with the left bar; no content transform"""
    global XF
    XF = False
    s = d.prs.slides.add_slide(d.blank)
    bg = s.background.fill; bg.solid(); bg.fore_color.rgb = rgb(BG0)
    if count: d.page += 1
    rect(s, 0, 0, 0.12, H, EDM)
    set_transition(s, "push", "l")
    return s


def divider(d, section, blurb, story):
    """template section divider: big number, name, blurb, bottom menu with the bus on the new stop"""
    s = raw_slide(d, count=False)
    console(d, s, story, False, None, count=False)
    text(s, 0.9, 1.25, 6, 2.6, [[R(f"{section + 1:02d}", size=150, bold=True, color=EDM_L)]], anchor="top")
    text(s, 1.0, 4.15, 11, 0.7, [[R(SECTIONS[section][3:], size=30, bold=True, color=TXT)]])
    text(s, 1.0, 4.9, 10.5, 0.9, [[R(blurb, size=12, color=MUT)]])
    # the bus pulls in to this stop
    bus(s, 7.7, 2.2, w=4.6, detail=True)
    rect(s, 6.9, 2.2 + 4.6 * 0.26 + 0.02, 5.9, 0.02, LINE2)
    for i in range(7):
        rect(s, 7.0 + i * 0.85, 2.2 + 4.6 * 0.26 + 0.2, 0.45, 0.025, BG3)
    text(s, 10.6, 5.75, 2.3, 0.3, [{"runs": [R("swipe  ›", size=9, color=MUT)], "align": "r"}])
    tabbar(s, section)
    footer(s, "")
    return s


def embed_fonts(path, font_dir="/tmp/claude-0/sc/tpl/x/ppt/fonts/"):
    """Embed the template's Quattrocento Sans (same EOT parts the template carries) so PowerPoint shows the template font."""
    import zipfile, shutil, os
    tmp = path + ".tmp"
    faces = [("regular", "QuattrocentoSans-regular.fntdata"), ("bold", "QuattrocentoSans-bold.fntdata"), ("italic", "QuattrocentoSans-italic.fntdata"), ("boldItalic", "QuattrocentoSans-boldItalic.fntdata")]
    zin = zipfile.ZipFile(path); zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "[Content_Types].xml":
            t = data.decode("utf8")
            if 'Extension="fntdata"' not in t:
                t = t.replace("<Default ", '<Default Extension="fntdata" ContentType="application/x-fontdata"/><Default ', 1)
            data = t.encode("utf8")
        elif item.filename == "ppt/_rels/presentation.xml.rels":
            t = data.decode("utf8")
            rels = "".join(f'<Relationship Id="rIdF{i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/font" Target="fonts/{fn}"/>' for i, (_, fn) in enumerate(faces))
            t = t.replace("</Relationships>", rels + "</Relationships>")
            data = t.encode("utf8")
        elif item.filename == "ppt/presentation.xml":
            t = data.decode("utf8")
            t = t.replace(' type="screen4x3"', "")
            lst = '<p:embeddedFontLst><p:embeddedFont><p:font typeface="Quattrocento Sans"/>' + "".join(f'<p:{k} r:id="rIdF{i + 1}"/>' for i, (k, _) in enumerate(faces)) + "</p:embeddedFont></p:embeddedFontLst>"
            import re
            t = re.sub(r"(<p:notesSz [^>]*/>)", r"\1" + lst, t, count=1)
            t = t.replace("<p:presentation ", '<p:presentation embedTrueTypeFonts="1" ', 1)
            data = t.encode("utf8")
        zout.writestr(item, data)
    for _, fn in faces:
        zout.write(font_dir + fn, "ppt/fonts/" + fn)
    zin.close(); zout.close(); shutil.move(tmp, path)


def kicker(s, x, y, w, t, color=EDM_L, size=10):
    return text(s, x, y, w, 0.3, [[R(t, size=size, bold=True, color=color)]])


def title(s, runs, x=0.3, y=0.9, w=12.7, h=0.9, size=23):
    rs = []
    for t in runs:
        if isinstance(t, tuple):
            rs.append(R(t[0], size=size, bold=True, color=EDM_L, font=FONT_D))
        else:
            rs.append(R(t, size=size, color=TXT, font=FONT_D, bold=True))
    return text(s, x, y, w, h, [{"runs": rs, "line": 0.98}])


def headline(s, kick, runs, y=0.84, size=20):
    sec = SECTIONS[CUR["section"]]
    tag = sec[:2] + " " + sec[3:].upper()
    if kick.startswith("APPENDIX "):
        kick = kick[len("APPENDIX "):]
    kicker(s, 0.5, y, 12.3, tag + "  ·  " + kick, size=10)
    title(s, runs, x=0.5, y=y + 0.2, w=12.3, size=size, h=0.68)


def pic(s, name, x, y, width):
    """picture by width; in the content zone both dimensions scale by KY so the bottom edge stays where the box was"""
    from PIL import Image
    path = name if name.startswith("/") else IMG + name
    iw, ih = Image.open(path).size
    height = width * ih / iw
    if inzone(y):
        x, y, _, _ = T(x, y); width *= KY; height *= KY
    return s.shapes.add_picture(path, Inches(x), Inches(y), Inches(width), Inches(height))


def panel(s, x, y, w, h, head=None, head_color=CYAN, fill=BG1, line_c=LINE, top=None, body=None, body_size=10.5, pad=0.14):
    rrect(s, x, y, w, h, fill, line_c, radius=0.04)
    if top:
        rect(s, x + 0.01, y, w - 0.02, 0.05, top)
    cy = y + pad
    if head:
        text(s, x + pad, cy, w - 2 * pad, 0.24, [[M(head, size=8, bold=True, color=head_color, spc=200)]])
        cy += 0.28
    if body:
        text(s, x + pad, cy, w - 2 * pad, h - (cy - y) - pad * 0.5, body)
    return cy


def stat(s, x, y, w, h, num, label, sub=None, color=TXT, num_size=28, fill=BG1, line_c=LINE, top=None):
    rrect(s, x, y, w, h, fill, line_c, radius=0.04)
    if top: rect(s, x + 0.01, y, w - 0.02, 0.05, top)
    text(s, x + 0.14, y + 0.1, w - 0.28, 0.6, [[M(num, size=num_size, bold=True, color=color)]], anchor="top")
    text(s, x + 0.14, y + 0.12 + num_size / 72 * 1.25, w - 0.28, 0.5, [[R(label, size=9, color=TXT)]] + ([[R(sub, size=7.5, color=MUT)]] if sub else []))


_FONT_CACHE = {}


def tw(t, size, bold=True):
    """text width in inches in the template font (measured from the installed TTF; falls back to a per-character estimate)"""
    try:
        from PIL import ImageFont
        key = (bold, 200)
        if key not in _FONT_CACHE:
            _FONT_CACHE[key] = ImageFont.truetype("/root/.fonts/qs/QuattrocentoSans-%s.ttf" % ("Bold" if bold else "Regular"), 200)
        return _FONT_CACHE[key].getlength(t) / 200 * size / 72
    except Exception:
        return 0.0085 * size * len(t)


def chip_w(t, size, y):
    if inzone(y):
        return (0.2 + tw(t, size * FSC) * 1.04) / KX
    return 0.22 + tw(t, size) * 1.04


def chip(s, x, y, t, color=MUT, w=None, size=6.5, fill=None, h=0.22, cw=0.062):
    if w is None:
        w = chip_w(t, size, y)
    p = rrect(s, x, y, w, h, fill or BG0, color, lw=0.75, radius=0.5)
    text(s, x, y, w, h, [{"runs": [M(t, size=size, bold=True, color=color, spc=80)]}, ], anchor="middle", shape=p, margin=(0, 0, 0, 0))
    for para in p.text_frame.paragraphs: para.alignment = PP_ALIGN.CENTER
    return w


def chips(s, x, y, items, gap=0.08, size=6.5, h=0.22, cw=0.062):
    """items: list of (text, color)"""
    cx = x
    for t, c in items:
        cx += chip(s, cx, y, t, c, size=size, h=h, cw=cw) + gap
    return cx


def concept_strip(s, items, y=6.31):
    global XF
    keep = XF; XF = False
    text(s, 0.5, y, 1.0, 0.22, [[R("CONCEPTS", size=7, bold=True, color=MUT)]], anchor="middle")
    chips(s, 1.45, y, items, size=7.2, cw=0.056, gap=0.1)
    XF = keep


def tier(s, x, y, w, h, name, color, dark):
    p = rrect(s, x, y, w, h, dark, color, lw=1, radius=0.04)
    text(s, x, y, w, h, [{"runs": [M(name, size=8.5, bold=True, color=color, spc=200)], "align": "c"}], anchor="middle", shape=p, margin=(0, 0, 0, 0))
    return p


def person(s, who, x, y, w, h, quote, tag=None, qsize=10, fill=BG1):
    name, lens, col, img = LENS[who]
    rrect(s, x, y, w, h, fill, col, lw=1.0, radius=0.06)
    sz = min(0.6, h - 0.2)
    px, py, pw, ph = T(x + 0.1, y + 0.1, sz, sz)
    s.shapes.add_picture(ASSETS + img, Inches(px), Inches(py), Inches(min(pw, ph)), Inches(min(pw, ph)))
    head = [M(name, size=7.5, bold=True, color=col, spc=120), M("  ·  " + (tag or lens), size=7, color=MUT, spc=100)]
    text(s, x + sz + 0.2, y + 0.08, w - sz - 0.3, 0.24, [head])
    text(s, x + sz + 0.2, y + 0.31, w - sz - 0.3, h - 0.36, [[R(quote, size=qsize, color=TXT)]])


def _cell_border(cell, color=BG0, w=1.0):
    from lxml import etree
    tcPr = cell._tc.get_or_add_tcPr()
    for tag in ("lnB", "lnT", "lnR", "lnL"):          # inserted at 0 in reverse so the final order is L, R, T, B before the fill
        ln = etree.Element(qn("a:" + tag)); tcPr.insert(0, ln)
        ln.set("w", str(int(w * 12700))); ln.set("cap", "flat"); ln.set("cmpd", "sng"); ln.set("algn", "ctr")
        sf = etree.SubElement(ln, qn("a:solidFill")); c = etree.SubElement(sf, qn("a:srgbClr")); c.set("val", color)
        etree.SubElement(ln, qn("a:prstDash")).set("val", "solid")


def table(s, x, y, w, h, rows, colw=None, sizes=None, fills=None, head_fill=BG3, bold_first_col=False, row_h=None, head_color=CYAN, zebra=True):
    nr, nc = len(rows), len(rows[0])
    if inzone(y):
        colw = [c * KX for c in colw] if colw else None
        row_h = row_h * KY if row_h else None
        sizes = [v * FSC for v in sizes] if sizes else None
    x, y, w, h = T(x, y, w, h)
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
            _cell_border(cell)
            size = (sizes[ci] if sizes else 8.5)
            tf = cell.text_frame; tf.word_wrap = True
            runs = val if isinstance(val, list) else [R(str(val))]
            p = tf.paragraphs[0]
            for rt in runs:
                if isinstance(rt, str): rt = (rt, {})
                t, o = rt
                r = p.add_run(); r.text = t
                if ri == 0:
                    r.font.name = MONO; r.font.size = Pt(o.get("size", 7) * (FSC if XF else 1)); r.font.bold = True; r.font.color.rgb = rgb(head_color)
                    _spc(r, 120)
                else:
                    r.font.name = o.get("font", FONT)
                    r.font.size = Pt(o.get("size", size) * (FSC if (XF and "size" in o) else 1)); r.font.bold = o.get("bold", bold_first_col and ci == 0)
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
        chip(s, x + w - 0.1 - chip_w(tag, 6.2, y + h - 0.27), y + h - 0.27, tag, tag_color or MUT, size=6.2, h=0.2)


def big_ghost(s, t, x, y, w, h, size=160, color=BG2):
    text(s, x, y, w, h, [{"runs": [M(t, size=size, bold=True, color=color)], "align": "r"}], anchor="middle")
