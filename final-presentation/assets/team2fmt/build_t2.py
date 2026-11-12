"""Referral Check final deck in the Team 2 format. Run: python3 build_t2.py OUT.pptx"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t2lib import *
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from pptx.enum.dml import MSO_LINE_DASH_STYLE as DASH

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out.pptx')
prs = open_base(os.path.join(HERE, 'team2_base.pptx'))
OD = '311 Requests open data (data.edmonton.ca/d/q7ua-agfg), 2023 to Nov 6, 2026, phone referrals'

# ---------------------------------------------------------------- 1 CALL (dark)
s = new_slide(prs, dark=True, pill='LIVE · 311 INTAKE', pill_style='yellow', chap=0,
    context='Tue 10:12 · Caller 7, one call, twice',
    kicker='CALLER 7 · ONE CALL, ONE CODE, ONE DECISION',
    title='One code decides whether an officer drives out; **10,609 referrals** this year ended with nothing to act on',
    source=f'{OD}. Caller 7 and times illustrative; the code, counts and closure label are real (1,350 of 4,877 untidy-property phone referrals in 2026 closed "Does Not Meet Bylaw Offence Standards").',
    notes='0:00-1:00. Open on the decision, not the agenda. In October, Caller 4 showed you a bounce. Tonight Caller 7 shows the bigger cost. Same call, twice: today on the left, with Referral Check on the right. The agent picks the same code both times. What changes is one question before the officer drives out, and the caller can always insist on a referral. The algorithm never says no.')
rect(s, 0.6, 2.36, 9.2, 0.52, fill=GRN, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.5)
tb(s, 0.85, 2.36, 8.9, 0.52, [('CALLER 7   ', {}), ], anchor='m', size=10, color=YEL, font=MONO, bold=True)
tb(s, 2.05, 2.36, 7.6, 0.52, '“The yard next door is full of junk again.”', anchor='m', size=14, italic=True, color=WHITE, font=BODY)
tag(s, 9.95, 2.5, 'ILLUSTRATIVE', color=YEL)
rect(s, 0.6, 3.06, 5.92, 2.3, fill=GRN)
mono_label(s, 0.9, 3.26, 4.2, 'TODAY: AS IT RUNS', color=LINE)
tag(s, 5.25, 3.25, 'EMPTY VISIT', color=YEL)
line(s, 0.9, 3.64, 6.22, 3.64, color=GREY)
bullet_list(s, 0.9, 3.78, 5.4, ['Picks Complaint Registered - Untidy Property',
    'Thursday: officer finds **ordinary household items**', 'Closed: no bylaw offence. **28%** of these end so'],
    size=13.5, color=WHITE, sq=YEL, gap=0.5, hi=YEL)
s.shapes[-1]  # noqa
rect(s, 6.81, 3.06, 5.92, 2.3, fill=WHITE)
mono_label(s, 7.11, 3.26, 4.2, 'DECEMBER: WITH REFERRAL CHECK', color=DARK)
tag(s, 11.6, 3.25, 'CHECKED', color=DARK, fill=DARK)
line(s, 7.11, 3.64, 12.43, 3.64, color=LINE)
bullet_list(s, 7.11, 3.78, 5.4, ['Screen shows AMBER: **30% ended with nothing** last year',
    'Agent asks the area’s two questions (+20 s)', 'Caller can still insist; answers ride along'],
    size=13.5, color=TXT, sq=RED, gap=0.5)
mono_label(s, 0.6, 5.52, 9.5, 'PHONE REFERRALS, JAN 1 TO NOV 6, 2026', color=YEL)
chips = [('Referrals', '179,139', GRN), ('Empty field visits', '10,609', GRN), ('Codes flagged', '84', YEL), ('Capacity / yr', '$287K', GRN)]
for i, (a, b, f) in enumerate(chips):
    x = 0.6 + i * 3.07
    rect(s, x, 5.84, 2.92, 0.5, fill=f)
    c = DARK if f == YEL else WHITE
    tb(s, x + 0.15, 5.84, 1.8, 0.5, a, anchor='m', size=12, color=c, font=BODY)
    tb(s, x + 1.5, 5.84, 1.3, 0.5, b, anchor='m', size=17, bold=True, color=c, font=HEAD, align=PP_ALIGN.RIGHT)

# ---------------------------------------------------------------- 2 DECISION
s = new_slide(prs, pill='ON THE CALL', chap=1, context='Tue 10:13 · the decision, restated',
    kicker='THE CORE ANALYTIC DECISION · RESTATED AND REFINED',
    title='Same pick as October; the refinement is **whether the referral should go out at all**',
    source=f'{OD}. October figures: Team 2 Strategic Analytics Initiative deck (Oct 26, 2026). Grain-size rule and five-part test: SEM 620 Group Project brief.',
    notes='1:00-2:00. We kept the October decision: the code a 311 agent picks on a phone referral. The diagnosis moved. 98.9% of referrals land with the right area first time, so fixing bounces frees only $7K to $17K a year. The bigger loss is the referral that goes out and finds nothing: 12,583 in 2025. So the decision becomes: route on the code as picked, or check first. Grain size is one agent, one code, 20 seconds, 190,000 times a year.')
tb(s, 0.57, 2.3, 3.8, 0.85, '191,521', anchor='m', size=46, bold=True, color=DARK, font=HEAD)
tb(s, 0.6, 3.15, 3.5, 0.6, 'phone referrals in 2025, one agent pick each', size=14, color=TXT)
line(s, 0.6, 3.92, 4.1, 3.92)
tb(s, 0.57, 4.05, 3.5, 0.8, '12,583', anchor='m', size=42, bold=True, color=RED, font=HEAD)
tb(s, 0.6, 4.85, 3.5, 0.6, 'went out and ended with **nothing to act on**', size=14, color=TXT)
mono_label(s, 4.6, 2.3, 5.1, 'INSIDE EACH PICK')
rect(s, 4.6, 3.55, 1.45, 1.05, fill=DARK)
tb(s, 4.7, 3.55, 1.28, 1.05, 'Route now or check first', anchor='m', size=13.5, bold=True, color=WHITE, font=HEAD)
line(s, 6.05, 3.85, 6.7, 3.05, color=DARK, w=1.25)
line(s, 6.05, 4.3, 6.7, 5.25, color=RED, w=1.25)
card(s, 6.7, 2.6, 3.0, 0.95)
tb(s, 6.88, 2.66, 2.7, 0.42, 'Route as picked', size=14, bold=True, color=DARK, font=HEAD, anchor='m')
tb(s, 6.88, 3.1, 2.7, 0.36, 'Average code · 5.9% empty', size=9.5, color=GREY, font=MONO)
rect(s, 6.7, 4.8, 3.0, 0.95, fill=RED)
tb(s, 6.88, 4.86, 2.7, 0.42, 'Check first', size=14, bold=True, color=WHITE, font=HEAD, anchor='m')
tb(s, 6.88, 5.3, 2.7, 0.36, 'Untidy Property · 30% empty (2025)', size=9.5, color=WHITE, font=MONO)
tb(s, 4.6, 4.78, 1.6, 0.34, 'risk > 20%', size=12, bold=True, color=RED, font=MONO)
tag(s, 4.6, 5.14, 'CUT-OFF', color=RED)
rect(s, 10.0, 2.3, 2.73, 4.0, fill=DARK)
mono_label(s, 10.2, 2.45, 2.4, 'OCTOBER’S BOUNCE CASE', color=YEL, size=9.5)
tb(s, 10.2, 2.85, 2.4, 0.55, '1,062', size=26, bold=True, color=WHITE, font=HEAD, anchor='m')
tb(s, 10.2, 3.4, 2.4, 0.3, 'phone bounces, 2025', size=11, color=LINE)
tb(s, 10.2, 3.85, 2.4, 0.55, '98.9%', size=26, bold=True, color=WHITE, font=HEAD, anchor='m')
tb(s, 10.2, 4.4, 2.4, 0.5, 'of 2026 referrals did not bounce', size=11, color=LINE)
tb(s, 10.2, 4.95, 2.4, 0.55, '$7K–$17K', size=22, bold=True, color=YEL, font=HEAD, anchor='m')
tb(s, 10.2, 5.5, 2.4, 0.3, 'a year if bounces alone are fixed', size=11, color=LINE)
mono_label(s, 10.2, 5.95, 2.4, 'WHY THE DIAGNOSIS MOVED', color=LINE, size=8.5)

# ---------------------------------------------------------------- 3 PROBLEM TREE
s = new_slide(prs, pill='ON THE CALL', chap=1, context='Thu · the officer finds nothing · why?',
    kicker='PROBLEM TREE · SESSION 2: MECE BY STAGE OF ONE CALL',
    title='Empty referrals start in the code set, get **picked on the call**, and nobody learns after',
    source='Problem tree after Glaser, Analytic Trees pp. 5-10. Evidence: 311 open data (q7ua-agfg); Office of the City Auditor, City’s Response to 311 Requests (Nov 2023) pp. 3, 16, 19-20; CSD03148 (Sep 2, 2026) p. 2, Att. 2.',
    notes='2:00-3:00. The October tree, widened from bounces to every referral that ends with nothing. Branches are MECE by stage of one call: before, during, after. Each leaf carries its evidence grade. Say the assumption out loud: not every empty visit is an intake error. The design answers one leaf per branch: show the risk (before), ask the standard (during), send the reason back (after).')
rect(s, 0.6, 2.35, 2.55, 3.55, fill=DARK)
mono_label(s, 0.78, 2.5, 2.2, 'ROOT QUESTION', color=YEL, size=9)
tb(s, 0.78, 2.85, 2.25, 2.0, 'Why do 1 in 14 phone referrals end with nothing for the City to do, and why does no one learn?',
   size=14, bold=True, color=WHITE, font=HEAD)
tag(s, 0.78, 5.0, 'ASSUMED, STATED', color=YEL)
tb(s, 0.78, 5.27, 2.25, 0.6, 'Some empty visits are not intake errors.', size=10, color=LINE, italic=True)
cols = [('BEFORE THE CALL · THE CODE SET', [('Codes name an owner, not a standard', 'VERIFIED'),
            ('No published risk rate per code', 'VERIFIED'), ('Bylaw criteria sit in 900 scripts', 'VERIFIED')]),
        ('DURING THE CALL · THE PICK', [('The words don’t say if the standard is met', 'INFERRED'),
            ('Speed is measured: 120-s answer target', 'VERIFIED'), ('System 1 picks, System 2 defends it', 'HYPOTHESIS')]),
        ('AFTER THE CALL · NO LEARNING', [('98.7% “resolved on initial contact” hides it', 'ABSENCE'),
            ('No closure reason goes back to the agent', 'ABSENCE'), ('Closure labels differ by area', 'VERIFIED')])]
line(s, 3.15, 2.5, 3.4, 2.5, color=DARK, w=1.25)
line(s, 3.4, 2.5, 12.73, 2.5, color=DARK, w=1.25)
for ci, (head, leaves) in enumerate(cols):
    x = 3.4 + ci * 3.13
    w = 2.98
    line(s, x + 0.01, 2.5, x + 0.01, 2.72, color=DARK, w=1.25)
    mono_label(s, x, 2.68, w, head, color=RED, size=9)
    for li, (t, ev) in enumerate(leaves):
        y = 3.05 + li * 0.97
        card(s, x, y, w, 0.85)
        tb(s, x + 0.14, y + 0.08, w - 0.28, 0.5, t, size=12.5, bold=True, color=DARK, font=HEAD)
        tag(s, x + 0.14, y + 0.56, ev, color=(DARK if ev == 'VERIFIED' else RED), size=7)
tb(s, 3.4, 5.98, 9.3, 0.3, '**Design answer, one leaf per branch:** show the risk (before) · ask the standard (during) · send the reason back (after).',
   size=12, color=TXT)

# ---------------------------------------------------------------- 4 PROFIT TREE
s = new_slide(prs, pill='ON THE CALL', chap=1, context='Thu · what the empty visit cost',
    kicker='PROFIT TREE · SESSION 2: THE TREE RECONCILES',
    title='Checking the 84 riskiest codes frees about **$287K a year** of officer and desk time',
    source='Mean of 50,000 Monte Carlo draws on triangular ranges (seed 20261110): field visit $22/$84/$280 (team Oct 26 ranges; no City figure); desk 5/10/20 min at CSU 52 rates; avoided share 20/35/50% (assumed); check 20 s at $0.30-$1.02. Volumes: open data, 2026 annualised. Duplicates and File Already under Investigation excluded. Inputs: Appendix A3.',
    notes='3:00-4:00. The stake as a profit tree: each box is the sum or product of the boxes to its right, and it reconciles to $375K. Every input is a range; the one that matters most, 35% avoided, is ours and the pilot measures it. Say capacity, not cash, before anyone asks: officers freed for calls that need them, no budget line moves, no position cut. Duplicates are left out on purpose because the City is already working on them; left in, the figure would read $375K. We kept the same 20% line rather than move it to win the number back, because moving it invites the question of whether we take credit for the City’s own work. Bounces sit in the desk row, so October’s bounce stake is not counted twice.')
def tbox(x, y, w, h, label, val, sub=None, fill=WHITE, vc=DARK, lc=GREY, big=20):
    card(s, x, y, w, h, fill=fill, line_c=(LINE if fill == WHITE else fill))
    mono_label(s, x + 0.12, y + 0.07, w - 0.2, label, color=lc, size=8)
    tb(s, x + 0.12, y + 0.3, w - 0.2, 0.45, val, size=big, bold=True, color=vc, font=HEAD, anchor='m')
    if sub:
        tb(s, x + 0.12, y + h - 0.32, w - 0.2, 0.28, sub, size=9, color=lc, font=BODY)
tbox(0.6, 3.05, 2.35, 1.6, 'NET CAPACITY / YR', '$287K', 'P10-P90 $130K-$477K', fill=DARK, vc=YEL, lc=LINE, big=30)
tbox(3.35, 2.35, 2.35, 1.05, 'GROSS TIME FREED', '$304K', 'visits + desk work')
tbox(3.35, 4.45, 2.35, 1.05, 'COST OF THE CHECK', '–$17K', '22,459 calls × $0.78', vc=RED)
tbox(6.1, 2.3, 2.35, 1.0, 'FIELD VISITS AVOIDED', '$301K', '2,193 visits × $137')
tbox(6.1, 3.45, 2.35, 1.0, 'DESK WORK AVOIDED', '$3K', 'bounces, non-City')
# leaves
leaves = [('VISITS REACHED', '6,266', '50% of empty visits', None), ('× AVOIDED', '35%', 'range 20-50%', 'ASSUMPTION'),
          ('× COST PER VISIT', '$137', '$22-$280 + desk', 'TEAM RANGE')]
for i, (a, b, c, t) in enumerate(leaves):
    x = 8.85 + i * 1.3
    tbox(x, 2.3, 1.2, 1.0, a, b, None, big=17)
    tb(s, x + 0.12, 3.35, 1.1, 0.3, c, size=8.5, color=GREY)
    if t:
        tag(s, x + 0.08, 3.63, t, color=RED, size=6.5)
# connectors
def elbow(x1, y1, x2, y2, c=DARK):
    mx = (x1 + x2) / 2
    line(s, x1, y1, mx, y1, color=c, w=1); line(s, mx, y1, mx, y2, color=c, w=1); line(s, mx, y2, x2, y2, color=c, w=1)
elbow(2.95, 3.85, 3.35, 2.87); elbow(2.95, 3.85, 3.35, 4.97, RED)
elbow(5.7, 2.87, 6.1, 2.8); elbow(5.7, 2.87, 6.1, 3.95)
line(s, 8.45, 2.8, 8.85, 2.8, color=DARK, w=1)
rect(s, 6.1, 4.65, 6.63, 1.15, fill=PALE)
mono_label(s, 6.25, 4.72, 3, 'SENSITIVITY', color=RED, size=8.5)
tb(s, 6.25, 4.98, 3.15, 0.8, ['Break-even if the check avoids only **2.0%**', 'Halve the visit cost: **$145K**'], size=11, color=TXT)
mono_label(s, 9.5, 4.72, 3.1, 'DUPLICATES, LEFT OUT', color=RED, size=8.5)
tb(s, 9.5, 4.98, 3.15, 0.8, ['The City is already working on them', 'Left in, the figure would be **$375K**'], size=11, color=TXT)
rect(s, 0.6, 5.95, 12.13, 0.38, fill=DARK)
tb(s, 0.8, 5.95, 11.8, 0.38, '**Capacity, not cash:** officers freed for calls that need them. No budget line moves; no position is cut.',
   anchor='m', size=12, color=WHITE, hi=YEL)

# ---------------------------------------------------------------- 5 ALGORITHM
s = new_slide(prs, pill='ON THE CALL', chap=2, context='Tue 10:13 · the pick is scored',
    kicker='THE ALGORITHM · SESSION 1: A LEARNED RATIO PLUS AN EXPLICIT RULE',
    title='One number per code and a three-colour rule; **the agent does the rest**',
    source=f'{OD}. Score trained on 2025 closures, tested Jan-Nov 2026. Wasted = empty field visit or bounce / non-City closure; duplicates excluded. Tier shares of 2026 phone referrals: green 89.3%, amber 6.5%, red 4.2%. Threshold: ask cost $1.02 / (35% × $137) ≈ 2.2%. Glaser, Analytic Trees (decision tree threshold); The Psychological Perspective s. 3.2 (attention).',
    notes='4:00-5:00. Simple on purpose: one shrunk ratio per code, refreshed weekly, and a rule that turns it into three colours. The whole explanation an agent needs: this code ended with nothing 30% of the time last year (1,493 of 4,988 in 2025). Rare codes are pulled to the average so one closure cannot turn a code red; new codes sit amber for 90 days. The rational threshold is about 2%, but a prompt on every second call becomes wallpaper, so attention sets the cut-off at 20%: about one call in nine, catching half the empty visits. A richer logistic model did worse out of time (AUC 0.69 vs 0.82).')
rect(s, 0.6, 2.3, 5.4, 3.5, fill=DARK)
mono_label(s, 0.85, 2.45, 5, 'THE WHOLE MODEL', color=YEL, size=9.5)
tb(s, 0.85, 2.8, 5.0, 0.95, ['risk = (empty + 10 × 6.6%) / (n + 10)', '     + (desk + 10 × 0.8%) / (n + 10)'], size=15, bold=True, color=WHITE, font=MONO)
line(s, 0.85, 3.85, 5.75, 3.85, color=GREY)
bullet_list(s, 0.85, 3.98, 5.0, ['Last 12 months of closures, refreshed weekly', 'Rare codes pulled toward the average',
    'New codes sit amber for 90 days', 'One line: “30% of these ended with nothing last year”'],
    size=12, color=WHITE, sq=YEL, gap=0.43)
tiers = [('GREEN', 'under 20%', '89% of referrals', 'Nothing. Route as today.', GRN, WHITE),
         ('AMBER', '20% to 30%', '7% of referrals', 'Rate + the area’s questions; one click to confirm', YEL, DARK),
         ('RED', 'over 30%', '4% of referrals', 'Rate, two questions, alternatives; agent decides', RED, WHITE)]
mono_label(s, 6.3, 2.3, 2, 'RULE', size=8.5); mono_label(s, 8.55, 2.3, 4, 'AGENT SEES AND DOES', size=8.5)
for i, (n, r, sh, d, f, c) in enumerate(tiers):
    y = 2.62 + i * 1.07
    rect(s, 6.3, y, 2.1, 0.95, fill=f)
    tb(s, 6.42, y + 0.06, 1.9, 0.35, n, size=14, bold=True, color=c, font=MONO)
    tb(s, 6.42, y + 0.4, 1.9, 0.25, r, size=11, color=c, bold=True)
    tb(s, 6.42, y + 0.64, 1.9, 0.25, sh, size=9.5, color=c)
    card(s, 8.4, y, 4.33, 0.95)
    tb(s, 8.55, y, 4.05, 0.95, d, anchor='m', size=13, color=TXT)
rect(s, 0.6, 5.95, 12.13, 0.38, fill=PALE)
tb(s, 0.8, 5.95, 11.8, 0.38, '**Why 20% when the decision tree says 2%?** A prompt on every second call becomes wallpaper. Attention sets the cut-off: 11% of calls, half the empty visits.',
   anchor='m', size=11.5, color=TXT)

# ---------------------------------------------------------------- 6 ROUTINE FLOW
s = new_slide(prs, pill='CHECKED', pill_style='yellow', chap=2, context='Tue 10:13 · who does what, in order',
    kicker='THE ROUTINE · INPUTS, OUTPUTS, WHO ACTS, WHAT HAPPENS WHEN IT IS WRONG',
    title='The routine scores and asks; **the agent decides**; the area’s closure teaches it',
    source='Routine decomposed after Feldman and Pentland (2003): ostensive, performative, artifacts (Session 7). Ironstone Ready-Mix: co-design with senior agents before adding the card. OCA 2023 p. 19: agents are expected to ask clarifying questions.',
    notes='5:00-6:00. The brief’s four questions in one picture. In: the code picked, last year’s closures, the area’s two screening questions. Out: a tier, a rate, two questions. Who acts: the agent decides, the area closes with a reason, 311 and the area run the fix queue. When it is wrong, the closure reason comes back and the ratio moves. The ostensive routine (find the code, resolve or refer) does not change; the performative one gains one question; the artifacts are where the algorithm lives.')
steps = [('1', 'INPUT', 'Takes in', [('LIVE', 'Code the agent picked'), ('BATCH', '12 months of closures'), ('BY AREA', 'Two screening questions')], WHITE, DARK),
         ('2', 'AUTOMATED', 'Scores', [(None, 'Looks up the code’s risk'), (None, 'Assigns green, amber, red')], WHITE, DARK),
         ('3', 'AUTOMATED', 'Shows the card', [(None, 'Rate and two questions'), (None, 'Never a pre-selected answer')], WHITE, DARK),
         ('4', 'HUMAN', 'Agent decides', [(None, 'Refer with answers, inform, or switch code'), (None, 'Caller can always insist')], WHITE, RED),
         ('5', 'WHEN WRONG', 'Learns', [(None, 'Area closes with one of five reasons'), (None, 'Reason back to agent in a day'), (None, 'Weekly refresh; fix queue')], DARK, YEL)]
for i, (n, kind, head, items, f, acc) in enumerate(steps):
    x = 0.6 + i * 2.47
    w = 2.2
    card(s, x, 2.35, w, 3.05, fill=f, line_c=(acc if acc == RED else (DARK if f == DARK else LINE)), lw=(1.5 if acc == RED else 0.75))
    rect(s, x, 2.35, 0.36, 0.36, fill=(acc if f == WHITE else YEL))
    tb(s, x, 2.35, 0.36, 0.36, n, anchor='m', align=PP_ALIGN.CENTER, size=12, bold=True, color=(WHITE if f == WHITE else DARK), font=HEAD)
    mono_label(s, x + 0.45, 2.4, w - 0.5, kind, color=(RED if kind in ('HUMAN',) else (YEL if f == DARK else GREY)), size=7.5)
    tb(s, x + 0.12, 2.82, w - 0.2, 0.4, head, size=16, bold=True, color=(WHITE if f == DARK else DARK), font=HEAD)
    y = 3.35
    for t, txt in items:
        if t:
            tag(s, x + 0.12, y, t, color=RED, size=6.5)
            y += 0.24
        tb(s, x + 0.12, y, w - 0.22, 0.5, txt, size=11.5, color=(WHITE if f == DARK else TXT))
        y += 0.52 if not t else 0.42
    if i < 4:
        line(s, x + w + 0.02, 3.0, x + 2.45, 3.0, color=DARK, w=1.25, arrow=True)
line(s, 11.5, 5.4, 11.5, 5.72, color=RED, w=1.25, dash=DASH.DASH)
line(s, 11.5, 5.72, 1.7, 5.72, color=RED, w=1.25, dash=DASH.DASH)
line(s, 1.7, 5.72, 1.7, 5.42, color=RED, w=1.25, dash=DASH.DASH, arrow=True)
rect(s, 4.2, 5.58, 5.0, 0.3, fill=BG)
tb(s, 4.2, 5.58, 5.0, 0.3, 'Every closure reason becomes evidence for the next call', anchor='m', align=PP_ALIGN.CENTER, size=12, bold=True, color=RED)

# ---------------------------------------------------------------- 7 AUTOMATE VS PEOPLE
s = new_slide(prs, pill='CHECKED', pill_style='yellow', chap=2, context='Tue 10:14 · the agent overrides',
    kicker='AUTOMATE OR LEAVE TO PEOPLE · SESSIONS 1, 9 AND 10',
    title='Software counts and reminds; **people refer, close and decline**',
    source='Three elements of agency and the four agent questions (Session 1); Northfield Credit Union case. Robodebt and proxy drift (Session 9). What to refuse to automate (Session 10). Bucinca et al. (2021): answer-first designs cut over-reliance.',
    notes='6:00-7:00. Be explicit, as the brief asks. Automate the counting and the reminder; never the decision to refer, close or decline, because those stay with people who can be asked why. Then the five ways it can be wrong. The one to say before anyone asks is the last: Robodebt. A proxy became a reason to refuse service. Our rule: the algorithm never declines a referral, the caller can always insist, and referrals refused without consent are measured and must read zero.')
card(s, 0.6, 2.3, 5.9, 1.75)
mono_label(s, 0.85, 2.42, 4, 'AUTOMATE', color=DARK, size=9.5)
bullet_list(s, 0.85, 2.75, 5.5, ['Score and tier every pick, weekly', 'Show the card on amber and red', 'Log tier, answers and the agent’s choice'],
            size=12.5, sq=DARK, gap=0.4)
card(s, 6.83, 2.3, 5.9, 1.75, line_c=RED, lw=1.25)
mono_label(s, 7.08, 2.42, 4, 'LEAVE TO PEOPLE', color=RED, size=9.5)
bullet_list(s, 7.08, 2.75, 5.5, ['Refer, inform or switch: **the agent**', 'Close or declare no offence: **the area**', 'Retire or reword a code: **311 with the area**'],
            size=12.5, sq=RED, gap=0.4)
rect(s, 0.6, 4.2, 12.13, 0.5, fill=RED)
tb(s, 0.8, 4.2, 3.2, 0.5, 'REJECTED: AUTO-DECLINE', anchor='m', size=10.5, bold=True, color=WHITE, font=MONO)
tb(s, 4.0, 4.2, 8.6, 0.5, '“The algorithm never refuses a referral; the caller can always insist.”', anchor='m', size=14, bold=True, color=WHITE, font=HEAD)
mono_label(s, 0.6, 4.85, 9, 'WHEN IT IS WRONG · FIVE WAYS, FIVE ANSWERS', color=DARK, size=9.5)
wrong = [('False alarm', '20-40 s and one click. 80% overridden → code goes green'),
         ('Missed one', 'Same as today, but the reason now comes back'),
         ('Drift', 'An area changes recording: judge against control'),
         ('Rubber stamp', 'Acceptance over 95% → audit a sample'),
         ('Turned into a gate', 'Refused without consent must read zero')]
for i, (h, d) in enumerate(wrong):
    x = 0.6 + i * 2.45
    card(s, x, 5.15, 2.3, 1.15, line_c=(RED if i == 4 else LINE))
    tb(s, x + 0.12, 5.2, 2.1, 0.3, h, size=12, bold=True, color=(RED if i == 4 else DARK), font=HEAD)
    tb(s, x + 0.12, 5.52, 2.1, 0.75, d, size=10, color=TXT)

# ---------------------------------------------------------------- 8 EVIDENCE
s = new_slide(prs, pill='CHECKED', pill_style='yellow', chap=2, context='2025 predicts 2026 · would the flag have been right?',
    kicker='EVIDENCE · SESSION 3: TEST ON UNSEEN CASES · TRAINED 2025, TESTED 2026',
    title='Last year’s ratio finds this year’s waste: **11% of calls carry half** the empty visits',
    source=f'{OD}. Score trained on 2025 only, tested on 179,139 phone referrals Jan 1-Nov 6, 2026. AUC = prior-year empty-visit rate per code against each phone referral’s outcome, ticket level, ties counted half; 0.862 (2026), 0.888 (2025), 0.915 (2024); 2017-2026 in empty_visit_backtest_2017_2026.csv. Bounce-score AUC (0.82-0.93 since 2017) in Appendix A1. Code-rate stability: 402 codes with 30+ referrals.',
    notes='7:00-8:00. The test was specified before 2026 was scored: trained on 2025, scored on 2026, so the overfitting trap is handled. The chart is the design choice made visible: at a 20% cut-off we flag 11% of calls and reach half the empty visits; duplicates are excluded from the score. Code waste rates are stable year to year (r 0.91). Then say what the data cannot show, before the executive does. The 90-day data set is built to close those gaps.')
stats = [('0.86', 'AUC: 2025 rate ranks 2026 empty visits', '0.86 to 0.92 every year since 2017'), ('31%', 'of flagged referrals end in waste', 'vs 7% of all referrals'), ('r 0.91', 'code waste rate, 2024 vs 2025', '402 codes, 30+ referrals each year')]
for i, (a, b, c) in enumerate(stats):
    y = 2.3 + i * 1.17
    tb(s, 0.6, y, 2.6, 0.55, a, size=30, bold=True, color=(RED if i == 1 else DARK), font=HEAD, anchor='m')
    tb(s, 0.6, y + 0.55, 2.7, 0.3, b, size=11.5, color=TXT)
    tb(s, 0.6, y + 0.8, 2.7, 0.25, c, size=8.5, color=GREY, font=MONO)
mono_label(s, 3.5, 2.3, 5.5, 'CUT-OFF: SHARE OF 2026 CALLS FLAGGED VS EMPTY VISITS CAUGHT', size=8.5)
cd = CategoryChartData()
cd.categories = ['>10%', '>15%', '>20%', '>25%', '>30%', '>40%', '>50%']
cd.add_series('Calls flagged', (25.7, 17.1, 10.7, 8.8, 4.2, 2.5, 0.7))
cd.add_series('Empty visits caught', (76.4, 63.7, 50.2, 43.9, 28.1, 19.8, 7.3))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(3.4), Inches(2.6), Inches(5.9), Inches(3.3), cd)
ch = gf.chart
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.TOP; ch.legend.include_in_layout = False
ch.legend.font.size = Pt(9); ch.legend.font.name = BODY
plot = ch.plots[0]; plot.gap_width = 60; plot.overlap = -10
plot.has_data_labels = True
dl = plot.data_labels; dl.font.size = Pt(8); dl.font.name = MONO; dl.number_format = '0'; dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END
for ser, col in zip(plot.series, (LINE, RED)):
    ser.format.fill.solid(); ser.format.fill.fore_color.rgb = rgb(col)
pt = plot.series[1].points[2]
pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(DARK)
va = ch.value_axis; va.visible = False; va.has_major_gridlines = False; va.maximum_scale = 100
ca = ch.category_axis; ca.tick_labels.font.size = Pt(9); ca.tick_labels.font.name = MONO
ca.format.line.color.rgb = rgb(LINE)
tb(s, 3.5, 5.92, 5.8, 0.3, 'Chosen: >20%, 84 codes (dark bar). Duplicates excluded. Percent of 2026 phone referrals / empty visits.', size=9, color=GREY)
rect(s, 9.55, 2.3, 3.18, 4.0, fill=DARK)
mono_label(s, 9.75, 2.45, 2.9, 'WHAT THIS DATA CANNOT SHOW', color=YEL, size=9)
bullet_list(s, 9.75, 2.85, 2.85, ['Why the officer found nothing', 'Whether the first code differed from the final one', 'Which agent picked', 'Quiet misroutes fixed without a label'],
            size=11.5, color=WHITE, sq=YEL, gap=0.62, h=0.6)
tb(s, 9.75, 5.45, 2.85, 0.75, 'The 90-day data set is built to close these gaps.', size=11, color=YEL, bold=True)

exec(open(os.path.join(HERE, 'build_t2_part2.py')).read())
prs.save(OUT)
print('saved', OUT, len(prs.slides._sldIdLst), 'slides')
