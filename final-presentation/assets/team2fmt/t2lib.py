"""Helpers that reproduce the Team 2 (Team2_Final_Presentation.pptx) format with python-pptx.
Base file: the uploaded Team 2 deck, emptied of slides, so its master, layouts and theme carry over."""
import copy, re
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

DARK = '13302A'; TXT = '1B2420'; RED = 'D43F1E'; GRN = '2A5A4E'; YEL = 'F2B33D'
GREY = '5B6B64'; LINE = 'C7D0CA'; PALE = 'E3EAE5'; BG = 'F4F5F1'; PALE2 = 'EBEFEC'
PINK = 'F7E3DD'; WHITE = 'FFFFFF'
HEAD = 'Bookman Old Style'; BODY = 'Cambria'; MONO = 'Courier New'
CHAPTERS = ['CALL', 'DECISION', 'ROUTINE', 'DATA', 'PLAN', 'ASK']


def rgb(h):
    return RGBColor.from_string(h)


def open_base(path):
    prs = Presentation(path)
    sldIdLst = prs.slides._sldIdLst
    for sldId in list(sldIdLst):
        rId = sldId.get(qn('r:id'))
        prs.part.drop_rel(rId)
        sldIdLst.remove(sldId)
    return prs


def layout(prs, name):
    for l in prs.slide_layouts:
        if l.name == name:
            return l
    raise KeyError(name)


def parse_marked(text):
    """'plain **hi** plain' -> [(plain,False),(hi,True),...]"""
    parts = re.split(r'(\*\*.+?\*\*)', text)
    out = []
    for p in parts:
        if not p:
            continue
        if p.startswith('**') and p.endswith('**'):
            out.append((p[2:-2], True))
        else:
            out.append((p, False))
    return out


def _style_run(r, size, color, font, bold=False, italic=False, spc=None):
    f = r.font
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    f.name = font
    f.color.rgb = rgb(color)
    if spc is not None:
        r._r.get_or_add_rPr().set('spc', str(spc))


def fill_tf(tf, paras, size=13, color=TXT, font=BODY, bold=False, hi=RED, align=None,
            italic=False, spc=None, line=None, space_after=0, hi_bold=None):
    """paras: str or list of str (each may contain **highlight**) or list of (str, dict) overrides."""
    if isinstance(paras, str):
        paras = [paras]
    tf.word_wrap = True
    first = True
    for item in paras:
        opts = {}
        if isinstance(item, tuple):
            item, opts = item
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        if align or opts.get('align'):
            p.alignment = opts.get('align', align)
        if line or opts.get('line'):
            p.line_spacing = opts.get('line', line)
        sa = opts.get('space_after', space_after)
        if sa:
            p.space_after = Pt(sa)
        if opts.get('space_before'):
            p.space_before = Pt(opts['space_before'])
        for txt, h in parse_marked(item):
            r = p.add_run()
            r.text = txt
            _style_run(r, opts.get('size', size), (opts.get('hi', hi) if h else opts.get('color', color)),
                       opts.get('font', font), opts.get('bold', bold) if not h else (hi_bold if hi_bold is not None else opts.get('bold', bold)),
                       opts.get('italic', italic), opts.get('spc', spc))
    return tf


def tb(s, x, y, w, h, paras, anchor='t', margin=0, **kw):
    box = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    for side in ('margin_left', 'margin_right', 'margin_top', 'margin_bottom'):
        setattr(tf, side, Inches(margin))
    tf.vertical_anchor = {'t': MSO_ANCHOR.TOP, 'm': MSO_ANCHOR.MIDDLE, 'b': MSO_ANCHOR.BOTTOM}[anchor]
    fill_tf(tf, paras, **kw)
    return box


def rect(s, x, y, w, h, fill=None, line=None, lw=0.75, shape=MSO_SHAPE.RECTANGLE, dash=None, rot=0, adj=None):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if adj is not None:
        sh.adjustments[0] = adj
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
    sh.shadow.inherit = False
    if rot:
        sh.rotation = rot
    if sh.has_text_frame:
        sh.text_frame.text = ''
    return sh


def line(s, x1, y1, x2, y2, color=LINE, w=0.75, dash=None, arrow=False):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(w)
    if dash:
        c.line.dash_style = dash
    if arrow:
        ln = c.line._get_or_add_ln()
        tail = etree.SubElement(ln, qn('a:tailEnd'))
        tail.set('type', 'triangle'); tail.set('w', 'med'); tail.set('len', 'med')
    return c


def tag(s, x, y, text, color=RED, fill=None, w=None, h=0.22, size=7.5, tcolor=None):
    w = w or (0.13 + 0.074 * len(text))
    rect(s, x, y, w, h, fill=fill, line=color, lw=0.75)
    tb(s, x, y, w, h, text, anchor='m', size=size, color=tcolor or (color if not fill else WHITE),
       font=MONO, bold=True, align=PP_ALIGN.CENTER, spc=50)
    return w


def mono_label(s, x, y, w, text, color=GREY, size=10, h=0.26, align=None):
    return tb(s, x, y, w, h, text, size=size, color=color, font=MONO, bold=True, spc=50, align=align)


def bullet_list(s, x, y, w, items, size=13, color=TXT, sq=RED, gap=0.42, h=0.4, font=BODY, hi=None):
    for i, it in enumerate(items):
        yy = y + i * gap
        rect(s, x, yy + 0.12, 0.11, 0.11, fill=sq)
        tb(s, x + 0.24, yy, w - 0.24, h, it, size=size, color=color, font=font, hi=(hi or (YEL if color == WHITE else RED)))


def header(s, pill, context, chap, dark=False, pill_style='dark', total=6, appendix=False):
    """pill_style: 'dark' (tx2 pill, yellow dot, light text) or 'yellow' (yellow pill, dark text, dark dot)."""
    pw = 0.5 + 0.095 * len(pill)
    if pill_style == 'yellow':
        rect(s, 0.6, 0.3, pw, 0.3, fill=YEL, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.5)
        rect(s, 0.73, 0.405, 0.09, 0.09, fill=RED if not dark else DARK, shape=MSO_SHAPE.OVAL)
        tc = DARK
    elif pill_style == 'outline':
        rect(s, 0.6, 0.3, pw, 0.3, fill=None, line=DARK, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.5)
        rect(s, 0.73, 0.405, 0.09, 0.09, fill=RED, shape=MSO_SHAPE.OVAL)
        tc = DARK
    else:
        rect(s, 0.6, 0.3, pw, 0.3, fill=DARK if not dark else GRN, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.5)
        rect(s, 0.73, 0.405, 0.09, 0.09, fill=YEL, shape=MSO_SHAPE.OVAL)
        tc = BG
    tb(s, 0.88, 0.3, pw - 0.3, 0.3, pill, anchor='m', size=10, color=tc, font=MONO, bold=True, spc=100)
    tb(s, 0.6 + pw + 0.2, 0.3, 7.6 - (0.6 + pw + 0.2), 0.3, context, anchor='m', size=10,
       color=(LINE if dark else GREY), font=MONO)
    chap_lbl = f'{chap + 1:02d}/{total:02d} {CHAPTERS[chap]}'
    tb(s, 7.7, 0.3, 2.05, 0.3, chap_lbl, anchor='m', size=10, color=(YEL if dark else RED), font=MONO,
       bold=True, align=PP_ALIGN.RIGHT)
    # progress nav
    x0, x1, yy = 10.07, 12.66, 0.45
    step = (x1 - x0) / (total - 1)
    line(s, x0, yy, x1, yy, color=(GRN if dark else LINE), w=1.25)
    if chap > 0:
        line(s, x0, yy, x0 + step * chap, yy, color=(BG if dark else DARK), w=1.75)
    for i in range(total):
        cx = x0 + step * i
        if i == chap:
            rect(s, cx - 0.09, yy - 0.09, 0.18, 0.18, fill=(YEL if dark else RED), rot=45)
        elif i < chap:
            rect(s, cx - 0.055, yy - 0.055, 0.11, 0.11, fill=(BG if dark else DARK), line=(BG if dark else DARK))
        else:
            rect(s, cx - 0.055, yy - 0.055, 0.11, 0.11, fill=(DARK if dark else BG), line=(LINE if dark else DARK))


def new_slide(prs, *, kicker, title, source, pill, context, chap, dark=False, pill_style='dark', notes='',
              title_size=28):
    s = prs.slides.add_slide(layout(prs, 'AE_DARK' if dark else 'AE_LIGHT'))
    phs = {ph.placeholder_format.idx: ph for ph in s.placeholders}
    header(s, pill, context, chap, dark, pill_style)
    k = phs[101]
    k.text_frame.text = ''
    fill_tf(k.text_frame, kicker, size=12, bold=True, color=(YEL if dark else RED), font=MONO, spc=100)
    t = phs[102]
    t.text_frame.text = ''
    fill_tf(t.text_frame, title, size=title_size, bold=True, color=(WHITE if dark else DARK),
            hi=(YEL if dark else RED), font=HEAD, line=0.95, hi_bold=True)
    for ph in (k, t):
        bp = ph.text_frame._txBody.find(qn('a:bodyPr'))
        for a in ('lIns', 'tIns', 'rIns', 'bIns'):
            bp.set(a, '0')
    bp = t.text_frame._txBody.find(qn('a:bodyPr'))
    src = phs[103]
    src.text_frame.text = ''
    fill_tf(src.text_frame, source, size=9, color=(LINE if dark else GREY), font=BODY)
    bp = src.text_frame._txBody.find(qn('a:bodyPr'))
    bp.set('anchor', 'b')
    for a in ('lIns', 'tIns', 'rIns', 'bIns'):
        bp.set(a, '0')
    # slide number placeholder from layout (copy the layout's sldNum shape)
    for shp in s.slide_layout.placeholders:
        pass
    _add_slide_number(s, dark)
    if notes:
        s.notes_slide.notes_text_frame.text = notes
    return s


def _add_slide_number(s, dark):
    lay = s.slide_layout
    for el in lay.shapes._spTree.iterchildren():
        if el.tag == qn('p:sp') and 'sldNum' in etree.tostring(el).decode():
            s.shapes._spTree.append(copy.deepcopy(el))
            return


def card(s, x, y, w, h, fill=WHITE, line_c=LINE, lw=0.75, dash=None):
    return rect(s, x, y, w, h, fill=fill, line=line_c, lw=lw, dash=dash)


def table(s, x, y, col_w, rows, header_row=None, row_h=0.42, size=11, head_size=8.5, zebra=True,
          first_bold=True, first_font=HEAD, first_size=None, dark_head=False, hi=RED, line_c=LINE):
    """Drawn as shapes (renders the same everywhere). rows: list of lists of str."""
    yy = y
    W = sum(col_w)
    if header_row:
        cx = x
        for i, c in enumerate(header_row):
            tb(s, cx + 0.05, yy, col_w[i] - 0.1, 0.3, c, anchor='b', size=head_size, color=GREY, font=MONO,
               bold=True, spc=50)
            cx += col_w[i]
        yy += 0.34
        line(s, x, yy, x + W, yy, color=DARK, w=1.25)
    for r_i, r in enumerate(rows):
        rh = row_h[r_i] if isinstance(row_h, list) else row_h
        if zebra and r_i % 2 == 0:
            rect(s, x, yy, W, rh, fill=PALE)
        cx = x
        for i, c in enumerate(r):
            if i == 0 and first_bold:
                tb(s, cx + 0.08, yy, col_w[i] - 0.14, rh, c, anchor='m', size=first_size or size + 1,
                   color=DARK, font=first_font, bold=True, hi=hi)
            else:
                tb(s, cx + 0.08, yy, col_w[i] - 0.14, rh, c, anchor='m', size=size, color=TXT, font=BODY,
                   hi=hi, hi_bold=True)
            cx += col_w[i]
        yy += rh
        line(s, x, yy, x + W, yy, color=line_c, w=0.5)
    return yy


def persona(s, x, y, w, initials, name, lens, voiced, quote, fill=YEL):
    card(s, x, y, w, 0.72)
    rect(s, x + 0.1, y + 0.11, 0.5, 0.5, fill=DARK)
    tb(s, x + 0.1, y + 0.11, 0.5, 0.5, initials, anchor='m', align=PP_ALIGN.CENTER, size=14, bold=True,
       color=fill, font=HEAD)
    tb(s, x + 0.72, y + 0.08, 1.9, 0.26, name, size=11, bold=True, color=DARK, font=HEAD)
    tb(s, x + 0.72, y + 0.33, 1.9, 0.18, lens, size=7, bold=True, color=RED, font=MONO, spc=50)
    tb(s, x + 0.72, y + 0.5, 1.9, 0.18, voiced, size=7, color=GREY, font=BODY)
    line(s, x + 2.7, y + 0.12, x + 2.7, y + 0.6, color=LINE)
    tb(s, x + 2.85, y + 0.06, w - 3.0, 0.6, f'“{quote}”', anchor='m', size=10.5, italic=True,
       color=TXT, font=BODY)
