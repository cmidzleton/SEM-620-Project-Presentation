import sys
sys.path.insert(0, "/tmp/claude-0/sc/build")
from lib3 import *
import lib3
lib3.IMG = "/tmp/claude-0/sc/build/img3/"
from figs import cached, K

# Every figure on the slides comes from figs.figures(): 2025 scores tested on 2026, duplicate requests left out, 20% amber line, 30% red line.
F = cached(0.20, 0.30); MC_ = F["mc"]; F15 = cached(0.15, 0.25)
NET, MED, P10, P90 = K(MC_["net"]), K(MC_["p50"]), K(MC_["p10"]), K(MC_["p90"]); RNG = f"{P10}-{P90}"
GROSS, COST, FIELD_, DESK_ = K(MC_["gross"]), K(MC_["cost"]), K(MC_["field"]), K(MC_["desk"])
NC = F["codes"]                                                    # flagged codes
FLG = f"{F['flag']:.0f}%"; CGT = f"{F['caught']:.0f}%"             # share of calls flagged, share of empty visits caught
BASE = f"{F['p1']:.1f}%"; G1, G2, G3 = (f"{x:.1f}%" for x in F["gate"][1:])
FLY = f"{round(F['FL'], -1):,.0f}"; FLY_R = f"{round(F['FL'], -2):,.0f}"; FVY = f"{round(F['FV'], -1):,.0f}"; WVY = f"{round(F['wv_year'], -1):,.0f}"
VAV = f"{MC_['visits_avoided']:,.0f}"; DAV = f"{MC_['desk_avoided']:,.0f}"; UV = f"${MC_['unit_visit']:.2f}"; UD = f"${MC_['unit_desk']:.2f}"
BE = f"{100 * MC_['be']:.1f}%"; BEX = int(0.35 / MC_["be"])        # break-even avoided share, and how many times over the 35% can be wrong
PM = f"{round(F['per_month'], -1):,.0f}"; ONEIN = F["one_in_flag"]; ANY = f"{F['any_rate26']:.1f}%"; ANY1 = F["any_one_in"]
DS_LOG = f"{round(F['ds_logged'], -2):,.0f}"; DS_CLO = f"{round(F['ds_closed'], -2):,.0f}"; DS_EMP = f"{round(F['ds_empty'], -1):,.0f}"; DS_ALL = f"{round(F['ds_logged'] * F['p1'] / 100, -2):,.0f}"
HIST = F["hist"]; HMIN = min(h["auc_deck_score_visits"] for h in HIST); HMAX = max(h["auc_deck_score_visits"] for h in HIST); H26 = HIST[-1]["auc_deck_score_visits"]
H3 = [h["caught"] for h in HIST if h["year"] in (2023, 2024, 2025)]
NODUP = "Duplicate requests are left out of every figure: the City is already working on them"

CORE = 17
d = Deck(CORE)
OD = "311 Requests open data (q7ua-agfg), 2023 to Nov 6, 2026, re-run on the team's six-part export"
ILL = "Caller 7 is illustrative; every code, count and closure label is real"

# concept chip colours by session
S1 = VIOLET; S2 = CYAN; S3 = ORANGE; S4 = GOLD; S5 = GREEN; S6 = "7DD3FC"; S7 = AMBER; S9 = RED; S10 = "F472B6"; BR = MUT

# =====================================================================
# 1 COVER (template style, app header, bus on the route)
# =====================================================================
s = raw_slide(d)
console(d, s, "311 · Referral Check · SEM 620 final presentation", False, None)
text(s, 0.9, 1.3, 11.5, 0.35, [[R("CITY OF EDMONTON  ·  311 AND CUSTOMER ACCESS  ·  ONE SMALL DECISION, ONE SIMPLE ALGORITHM", size=10, bold=True, color=EDM_L)]])
text(s, 0.85, 1.7, 11.5, 1.3, [[R("Referral Check", size=60, bold=True, color=TXT)]])
text(s, 0.9, 3.0, 11.0, 1.1, [[R("Before a 311 referral goes out, a 20-second check on ", size=18, color=MUT), R("the codes that most often end with nothing", size=18, bold=True, color=AMBER), R(" for the City to do", size=18, color=MUT)]])
rrect(s, 0.9, 4.35, 6.3, 1.3, BG1, LINE, radius=0.04); rect(s, 0.9, 4.35, 0.06, 1.3, EDM_L)
text(s, 1.12, 4.42, 5.9, 0.3, [[R("SEM 620  ·  FINAL PRESENTATION  ·  25% OF THE GROUP PROJECT", size=7.5, bold=True, color=MUT)]])
text(s, 1.12, 4.68, 6.0, 0.95, [[R("Team 2 · Lauren Lonsberry · Nav Sekhon · Rick Auger · Curtis Middleton", size=9.5, color=TXT)],
                               {"runs": [R("Session 11 · Monday, December 7, 2026 · 15 minutes + Q&A", size=9.5, color=MUT)], "before": 3},
                               {"runs": [R(f"{NET} A YEAR OF FIELD AND DESK CAPACITY  ·  P10-P90 {RNG}  ·  CAPACITY, NOT CASH", size=7.5, bold=True, color=AMBER)], "before": 6}])
text(s, 7.5, 4.4, 5.3, 1.25, [[R("Dollar figures are the mean of 50,000 Monte Carlo draws on the team's own cost ranges, trained on 2025 tickets and tested on 2026. The share of empty visits the check avoids (35%) is our assumption; the pilot measures it. Duplicate requests are left out: the City is already working on them.", size=9, color=MUT)]])
# the route: five stops, the bus at the first
ry = 6.05
line(s, 1.2, ry + 0.42, 12.2, ry + 0.42, LINE2, 1.5)
for i, name in enumerate(SECTIONS):
    sx = 1.2 + i * 2.75
    rect(s, sx - 0.06, ry + 0.36, 0.12, 0.12, EDM if i == 0 else BG3, shape=MSO_SHAPE.OVAL)
    text(s, sx - 0.1, ry + 0.52, 2.5, 0.28, [[R(name, size=8, bold=(i == 0), color=TXT if i == 0 else DIM)]])
bus(s, 0.75, ry - 0.02, w=1.5, detail=True)
text(s, 10.3, ry - 0.1, 2.5, 0.3, [{"runs": [R("swipe to begin  ›", size=9, color=MUT)], "align": "r"}])
footer(s, 1)
notes(s, "Cover. Open on the decision, not the agenda: one 311 agent, one code, 20 seconds, and whether a City officer drives across town. Referral Check is the algorithm that sits between the pick and the referral. Say up front: capacity, not cash; the 35% is ours to test; duplicate requests are left out of every figure because the City is already working on them. The deck moves like the 311 app: swipe left; the bus at the bottom shows which stop we are at.")


# =====================================================================
# AGENDA (template page 2; un-numbered) · the app's home screen
# =====================================================================
DIV = {}
s = raw_slide(d, count=False)
HOME = s
console(d, s, "311 · Referral Check · Home", False, None, count=False)
text(s, 0.9, 1.1, 6, 0.6, [[R("Agenda", size=26, bold=True, color=TXT)]])
ag = [("01", "Decision", "Caller 7, the pick restated and refined, the problem tree, the profit tree", "slides 2 to 5"),
      ("02", "Algorithm", "One ratio per code, the routine, who decides and what happens when it is wrong, the backtest", "slides 6 to 9"),
      ("03", "Lenses", "Rational, psychological and political lenses; the ten biases, including ours", "slides 10 to 11"),
      ("04", "Data & plan", "Data inventory, the 90-day data set, the gate, the measures, the ask, AI process reflection", "slides 12 to 17"),
      ("05", "Appendix", "Score method, the codes, ten-year check, Monte Carlo, pilot length, the political game, concept map, sources", "A1 to A8")]
AG_ROWS = []
for i, (n_, name, blurb, where) in enumerate(ag):
    y = 1.95 + i * 0.86; live = i < 4
    a_ = text(s, 0.9, y, 1.3, 0.78, [[R(n_, size=34, bold=True, color=EDM_L if live else DIM)]], anchor="middle")
    b_ = text(s, 2.3, y, 2.9, 0.78, [[R(name, size=18, bold=True, color=TXT if live else MUT)]], anchor="middle")
    text(s, 5.2, y, 6.0, 0.78, [[R(blurb, size=11, color=MUT if live else DIM)]], anchor="middle")
    text(s, 11.3, y, 1.55, 0.78, [{"runs": [R(where + "  ›", size=9, color=EDM_L if live else DIM)], "align": "r"}], anchor="middle")
    if i < 4:
        rect(s, 0.9, y + 0.82, 11.95, 0.01, LINE)
    AG_ROWS.append((a_, b_, i))
tabbar(s, -1)
footer(s, "")
notes(s, "Agenda, laid out like the app's home screen. Each row and each stop on the bottom bar is a link to that section. Five stops; the bus shows where we are. Timing: 17 core slides will not fit in 15 minutes if every slide is read. A spoken path of about nine slides at 90 seconds each: 2 (Caller 7), 5 (profit tree), 6 (the algorithm), 9 (evidence), 10 (lenses), 12 (the 90-day data set), 13 (plan and gate), 15 (the ask), 16 (AI reflection). On 3, 4, 7, 8, 11 and 14, say the headline and move on; they are there for the rubric and for questions.")

# =====================================================================
# 2 THE HOOK · CALLER 7
# =====================================================================
DIV[0] = divider(d, 0, "One pick on one call, 190,000 times a year. What it costs when the referral should not have gone out, and the tree behind it.", "01 · THE DECISION")
s = new_slide(d, "TUE 10:12 · CALLER 7 ON THE LINE · THE SAME CALL, TWICE", foot=f"{OD}. {ILL}. 2025: 191,521 phone referrals; 12,583 closed with a field outcome of nothing to act on, called an empty visit in this deck (Does Not Meet Bylaw Offence Standards, Assessed - No Action Required, Unable to Locate Animal, Location Not Found, Unable to Contact Complainant; the last two, {F['noproof25']:,} tickets, do not prove an officer attended). 2026 to Nov 6: 179,139 and 10,609. {NODUP}.", section=0)
headline(s, "THE DECISION, AS IT HAPPENS", ["One pick on one call decides whether an officer is sent. ", ("12,583 times in 2025", ), " the referral ended with nothing for the City to act on."])

# left: today
panel(s, 0.3, 1.9, 6.15, 3.72, head="TODAY · THE CALL AS IT RUNS", head_color=RED, top=RED)
steps = [("10:12", "Caller 7: \"The yard next door is full of junk again.\""),
         ("10:13", "Agent searches \"untidy\", picks Complaint Registered - Untidy Property, refers to Municipal Enforcement. Clock: 120-second answer target."),
         ("Thu", "A peace officer drives out. Ordinary household items, nothing that meets the bylaw standard."),
         ("Thu", "Closed: Does Not Meet Bylaw Offence Standards. 1,350 of 4,877 such phone referrals ended this way in 2026 (28%)."),
         ("Later", "Nothing goes back to the agent. The scorecard counts the ticket as resolved on first contact.")]
yy = 2.3
for t, body in steps:
    text(s, 0.45, yy, 0.7, 0.5, [[M(t, size=8.5, bold=True, color=RED)]])
    text(s, 1.15, yy, 5.15, 0.64, [[R(body, size=9.5, color=TXT)]])
    yy += 0.65
# right: with referral check
panel(s, 6.6, 1.9, 6.43, 3.72, head="WITH REFERRAL CHECK · 20 SECONDS ADDED", head_color=GREEN, top=GREEN)
steps2 = [("10:12", "Same call, same words."),
          ("10:13", f"Agent picks the same code. The screen shows {F['untidy_tier']}: {F['untidy25_rate']:.1f}% of these referrals ended with nothing to act on last year ({F['untidy25_wv']:,} of {F['untidy25_n']:,}), and two screening questions written by Municipal Enforcement."),
          ("10:13", "\"Is it visible from the street or a neighbour's yard? More than ordinary household items?\" Caller: \"Just bins and a bike.\" Agent gives the bylaw information; caller can still insist on a referral."),
          ("Thu", "No officer dispatched. If the referral had gone out, the officer's closure reason would return to the agent within a day."),
          ("Weekly", "The code's risk table updates. Codes that stay flagged go to a fix queue 311 reviews with the area.")]
yy = 2.3
for t, body in steps2:
    text(s, 6.75, yy, 0.75, 0.5, [[M(t, size=8.5, bold=True, color=GREEN)]])
    text(s, 7.5, yy, 5.4, 0.64, [[R(body, size=9.5, color=TXT)]])
    yy += 0.65
# stats row
stat(s, 0.3, 5.72, 3.05, 0.93, f"1 in {F['wv_one_in']}", f"phone referrals ends with nothing to act on in the field ({F['wv_rate26']:.1f}%, 2026)", color=AMBER, num_size=18)
stat(s, 3.45, 5.72, 3.0, 0.93, f"1 in {ANY1}", f"ends in any wasted outcome, desk or field ({ANY}; duplicates left out)", color=AMBER, num_size=18)
stat(s, 6.6, 5.72, 3.1, 0.93, f"{NC} codes", f"carry {CGT} of the empty visits ({FLG} of calls)", color=CYAN, num_size=18)
stat(s, 9.85, 5.72, 3.18, 0.93, f"{NET} / yr", f"field and desk capacity freed, mean; P10-P90 {RNG}", color=GREEN, num_size=18)
concept_strip(s, [("BRIEF · ONE CONCRETE SITUATION", BR), ("S7 · ROUTINE AS PERFORMED", S7), ("S3 · FEEDBACK LINKS ACTION TO RESULT", S3)])
notes(s, "The hook. Caller 4 told you about bounces in October; Caller 7 is the bigger cost. Illustrative dialogue; real code (Complaint Registered - Untidy Property), real counts. The screening questions are examples of what the area would write; the area owns them. Key line: the caller can always insist on a referral. The algorithm never says no. The card is amber, not red: the code's 2025 rate is 29.9%, a hair under the 30% red line, which is a fair example of why the cut-offs are a value choice. Two of the five closure labels (Unable to Contact Complainant, Location Not Found) do not prove an officer attended; 'empty visit' is the deck's short name for all five.")

# =====================================================================
# 3 THE DECISION, RESTATED AND REFINED
# =====================================================================
s = new_slide(d, "TUE 10:13 · THE PICK · WHAT DECISION ARE WE IMPROVING?", foot=f"{OD}. October figures from the team's Oct 26 Strategic Analytics Initiative deck. Five-part test and grain-size rule from the SEM 620 Group Project brief; McGarry (ready-mix dispatcher) is the brief's benchmark for a decision an algorithm can take. 1,917 codes as counted in the team's October deck; 1,930 when a code is service area + category + description (Appendix A1).", section=0)
headline(s, "THE CORE ANALYTIC DECISION · RESTATED, REFINED", ["Same 20-second pick as October. The refinement: the code chooses ", ("whether the work goes out", ), ", not only where."])
# left october vs now
panel(s, 0.3, 1.9, 4.1, 2.25, head="OCTOBER · DIAGNOSIS", head_color=MUT)
text(s, 0.44, 2.22, 3.85, 1.9, [[R("Which service code does a new 311 phone ticket get?", size=12, color=TXT, bold=True)],
                                {"runs": [R("Agent picks 1 of 1,917 codes. A wrong code bounces between areas: 1,062 phone-referral bounces in 2025, about $100K a year, 98.9% of referrals land first time.", size=9.5, color=MUT)], "before": 6}])
panel(s, 0.3, 4.3, 4.1, 2.3, head="DECEMBER · THE DECISION WE DESIGN FOR", head_color=AMBER, top=AMBER)
text(s, 0.44, 4.62, 3.85, 1.95, [[R("On each phone referral: route on the code as picked, or check first whether the referral should go out at all?", size=12, color=TXT, bold=True)],
                                 {"runs": [R("The code sets resolve-or-refer on 99.4% of tickets. 1,062 bounced; 12,583 went out and ended with nothing to act on. Same pick, same screen, a bigger loss.", size=9.5, color=MUT)], "before": 6}])
# middle: five-part test
rows = [["FIVE-PART TEST", "FINDING", "SOURCE"],
        ["Who makes it, how often", "A 311 agent, live, once per phone referral: 191,521 in 2025, about one every 100 seconds the line is open", "open data"],
        ["Inputs used now", "Caller's words and address, a code search, 900 area scripts, experience. Nothing on screen says how a code usually ends", "OCA 2023; CSD03148"],
        ["Options", "Resolve on the call, refer under one of 1,917 codes, or ask one more question first", "team deck, Oct 26"],
        ["Bad instance x frequency", "Empty visit $22 / $84 / $280 (team ranges) x 12,583 a year; bounce $36 x 1,062; days residents wait in the wrong queue", "stake model"],
        ["Could an algorithm make it?", "Not the pick: only the agent hears the caller. But a lookup can say, before the referral, how often this code ends with nothing", "this proposal"]]
table(s, 4.55, 1.9, 5.5, 4.7, rows, colw=[1.45, 3.25, 0.8], sizes=[8, 8, 7], bold_first_col=True, row_h=0.72)
# right: why it moved
panel(s, 10.2, 1.9, 2.83, 4.7, head="WHY THE DIAGNOSIS MOVED", head_color=CYAN)
text(s, 10.34, 2.22, 2.58, 4.3, [[R("1  The pick is right for routing", size=9.5, bold=True, color=TXT)], [R("98.9% of 2026 phone referrals did not bounce. Fixing bounces alone frees $7K to $17K a year.", size=8.5, color=MUT)],
                                 {"runs": [R("2  The bigger loss is the referral that should not have gone", size=9.5, bold=True, color=TXT)], "before": 6}, [R(f"5.9% of phone referrals end with nothing to act on in the field; {ANY} in some wasted outcome, duplicates left out. Each visit costs far more than a bounce.", size=8.5, color=MUT)],
                                 {"runs": [R("3  Grain size", size=9.5, bold=True, color=TXT)], "before": 6}, [R("One agent, one code, 20 seconds, 190,000 times a year. One level narrower than \"intake\", as the brief asks. McGarry's board was replaced; this agent is not.", size=8.5, color=MUT)]])
concept_strip(s, [("BRIEF · FIVE-PART TEST", BR), ("BRIEF · GRAIN SIZE", BR), ("S7 · McGARRY BENCHMARK", S7), ("S2 · IS THIS THE DECISION WE FACE?", S2)])
notes(s, "Restate, then refine. The October decision stands; the diagnosis moved because the open data showed the pick is almost always right for routing, while one referral in 14 ends with nothing for the City to do. Name the change openly: October's alternatives slide ranked complaint-intake screening sixth; the data moved it up.")

# =====================================================================
# 4 PROBLEM TREE
# =====================================================================
s = new_slide(d, "THU · THE OFFICER FINDS NOTHING · WHY DOES IT KEEP HAPPENING?", foot=f"Problem tree after Glaser, Analytic Trees pp. 5-10: a root sentence with a result and a puzzle, branches by stage of one call (MECE by time), evidence marked on every leaf. {OD}; OCA 2023 pp. 3, 16, 19, 20; CSD03148 (Sep 2, 2026) p. 2, Att. 2.", section=0)
headline(s, "PROBLEM TREE · WHY, IN ONE CALL", ["Empty referrals start before the call, are picked during it, and after it ", ("no one is told", ), ", so no one learns."])
# root
node(s, 0.3, 2.05, 2.75, 1.55, "ROOT QUESTION", f"Why does one phone referral in {ANY1} end with nothing for the City to do, and why does no one learn from it?", color=AMBER, body_size=10)
text(s, 0.3, 3.7, 2.75, 1.4, [[M("ASSUMED, STATED", size=7, bold=True, color=RED, spc=150)], [R("An empty visit is treated as avoidable at intake. Some are not: the condition changed, or the caller was right and the officer could not see it.", size=8, color=MUT)]])
text(s, 0.3, 5.0, 2.75, 1.6, [[M("THREE REAL EVENTS, ONE BRANCH EACH", size=7, bold=True, color=CYAN, spc=150)], [R("Garbage-can bounce (4 codes, 4 owners): BEFORE. Untidy yard, no offence: DURING. 2026 bounce rise, 39% from new recording: AFTER.", size=8, color=MUT)]])
# branches
bx = 3.35; bw = 3.1; gap = 0.13
branches = [
    ("BEFORE THE CALL · THE CODE SET", CYAN, [
        ("Codes name an owner, not a standard", "The bylaw criteria live in 900 scripts the areas sign off; the code itself carries none of them.", "VERIFIED", GREEN),
        ("Ownership follows the asset", "One garbage can, four codes, four owners. The caller's words rarely name the owner.", "VERIFIED", GREEN),
        ("Risk is invisible", "No published rate per code. Untidy Property: 28% empty; the average referral: 5.9%.", "VERIFIED", GREEN)]),
    ("DURING THE CALL · THE PICK", AMBER, [
        ("The words do not say whether the standard is met", "\"Junk in the yard\" fits the code; whether an officer can act is a second question nobody asks.", "INFERRED", AMBER),
        ("Speed is what is measured", "120-second answer target; script AI framed around shorter calls. The first code that fits saves time.", "VERIFIED", GREEN),
        ("System 1 picks, System 2 defends", "A familiar phrase calls up a familiar code; the search then confirms it. No feedback ever arrives to retrain the intuition.", "HYPOTHESIS", ORANGE)]),
    ("AFTER THE CALL · NO LEARNING", RED, [
        ("No count on the scorecard", "\"Resolved on Initial Contact\" 98.7% counts an empty visit nobody chased as resolved.", "ABSENCE", RED),
        ("No word back", "No process we found returns the closure reason to the agent who picked the code.", "ABSENCE", RED),
        ("Labels are built differently by area", "Eight areas began recording bounces only in 2026; closure reasons vary by area. The measure moves when recording moves.", "VERIFIED", GREEN)]),
]
for i, (head, col, leaves) in enumerate(branches):
    x = bx + i * (bw + gap)
    p = rrect(s, x, 2.05, bw, 0.4, BG2, col, lw=1, radius=0.04)
    text(s, x, 2.05, bw, 0.4, [{"runs": [M(head, size=7.5, bold=True, color=col, spc=150)], "align": "c"}], anchor="middle", shape=p, margin=(0, 0, 0, 0))
    line(s, 3.05, 2.82, bx, 2.82, LINE2) if i == 0 else None
    ly = 2.6
    for (lh, lb, tag, tc) in leaves:
        node(s, x, ly, bw, 1.27, lh, lb, color=col, body_size=8.5, head_size=8, tag=tag, tag_color=tc)
        ly += 1.35
# connector from root to branch heads
line(s, 3.05, 2.25, 3.2, 2.25, LINE2); line(s, 3.2, 2.25, 3.2, 2.25, LINE2)
for i in range(3):
    x = bx + i * (bw + gap)
    line(s, 3.2, 2.25, x, 2.25, LINE2) if i == 0 else None
concept_strip(s, [("S2 · PROBLEM TREE", S2), ("S2 · MECE BY STAGE", S2), ("S2 · EXPLANATION AS HYPOTHESIS", S2), ("S3 · SYSTEM 1 / SYSTEM 2", S3), ("S6 · METRIC BUILT SLIGHTLY WRONG", S6), ("S5 · WHAT THE DATA CANNOT SHOW", S5)])
notes(s, "The October problem tree, widened from bounces to every referral that ends with nothing to do. Root is a sentence with a result and a puzzle. Branches are MECE by stage of one call. Each leaf carries its evidence grade. The assumption is on the slide: not every empty visit is an intake error. Three real events each land in exactly one branch, the test the reading prescribes. The design on slide 6 answers one leaf per branch: show the risk (before), ask the standard (during), send the reason back (after).")

# =====================================================================
# 5 PROFIT TREE · THE STAKE
# =====================================================================
s = new_slide(d, "THU · WHAT THE EMPTY VISIT COST · THE STAKE AS A TREE", foot="Profit tree after Glaser, Analytic Trees Fig 2.1: each box is the sum or product of the boxes to its right and the tree reconciles. Triangular inputs (min / likely / max): field visit $22 / $84 / $280 and desk time 5 / 10 / 20 min at $36.93-$52.09 an hour (team's Oct 26 ranges, CSU 52 rates); avoided share 20 / 35 / 50% (assumed); check 20 s at $0.30-$1.02 (agent time only to average cost per contact, $16.29 per contact from the $14.66M budget). 50,000 draws, seed 20261110. Volumes: 2026 to Nov 6, annualised x 12/10.2. Duplicate requests left out.", section=0)
headline(s, "PROFIT TREE · CAPACITY AT STAKE", [f"Checking the {NC} riskiest codes frees about ", (f"{NET} a year", ), " of officer and desk time. Capacity, not cash: no budget line moves."])
# tree nodes left-to-right
def pnode(x, y, w, h, head, num, body, color=TXT, sub=None):
    rrect(s, x, y, w, h, BG1, LINE, radius=0.04)
    text(s, x + 0.12, y + 0.08, w - 0.24, 0.22, [[M(head, size=7, bold=True, color=CYAN, spc=120)]])
    text(s, x + 0.12, y + 0.3, w - 0.24, 0.42, [[M(num, size=17, bold=True, color=color)]])
    text(s, x + 0.12, y + 0.72, w - 0.24, h - 0.78, [[R(body, size=8, color=MUT)]] + ([[M(sub, size=7.5, bold=True, color=TXT)]] if sub else []))
pnode(0.3, 3.1, 2.3, 1.55, "NET CAPACITY FREED, A YEAR", NET, f"mean of 50,000 draws; median {MED}; every draw above zero", color=GREEN, sub=f"P10-P90 {RNG}")
pnode(2.95, 2.0, 2.3, 1.3, "GROSS TIME FREED", GROSS, "field visits avoided + desk work avoided", color=TXT)
pnode(2.95, 4.5, 2.3, 1.3, "COST OF THE CHECK", "-" + COST, f"{FLY} flagged calls x about $0.78 of agent time (20 s)", color=RED)
pnode(5.6, 1.9, 2.3, 1.2, "FIELD VISITS AVOIDED", FIELD_, f"{VAV} visits x {UV} (visit + desk)", color=TXT)
pnode(5.6, 3.25, 2.3, 1.1, "DESK WORK AVOIDED", DESK_, f"{DAV} desk closures x {UD}", color=TXT)
pnode(8.25, 1.9, 1.55, 1.2, "VISITS REACHED", FVY, f"{CGT} of {WVY} a year, in the {NC} flagged codes", color=AMBER)
pnode(9.9, 1.9, 1.5, 1.2, "x AVOIDED", "35%", "assumed 20 / 35 / 50%; pilot measures it", color=AMBER)
pnode(11.5, 1.9, 1.53, 1.2, "x COST PER VISIT", "$137", "$22 / $84 / $280 + desk", color=AMBER)
# connectors
elbow(s, 2.6, 3.87, 2.95, 2.65, xm=2.78); elbow(s, 2.6, 3.87, 2.95, 5.15, xm=2.78)
elbow(s, 5.25, 2.65, 5.6, 2.5, xm=5.42); elbow(s, 5.25, 2.65, 5.6, 3.8, xm=5.42)
line(s, 7.9, 2.5, 8.25, 2.5, LINE2)
text(s, 9.78, 2.2, 0.15, 0.3, [[M("x", size=12, color=DIM)]]); text(s, 11.38, 2.2, 0.15, 0.3, [[M("x", size=12, color=DIM)]])
# MC chart
pic(s, "mc.png", 8.25, 3.25, 4.78)
# bottom: what it says
panel(s, 0.3, 4.85, 2.3, 1.75, head="MIX EFFECT", head_color=AMBER)
text(s, 0.42, 5.15, 2.08, 1.4, [[R("The City-wide rate (5.9%) hides codes at 28%, 43%, 62%. Judge the pilot inside flagged codes, never on the average, or a change in call mix will read as a result.", size=8, color=TXT)]])
panel(s, 5.6, 4.5, 2.3, 2.1, head="SENSITIVITY", head_color=CYAN)
text(s, 5.72, 4.8, 2.08, 1.8, [[R(f"Break-even if the check avoids only {BE} of flagged empty visits: the 35% can be wrong {BEX} times over. Halve the visit cost: {K(F['sens_halve'])}. Price every check at the full $1.02: {K(F['sens_ask102'])}. Leave desk closures out: {K(F['sens_nodesk'])}.", size=8, color=TXT)]])
text(s, 8.25, 5.95, 4.78, 0.7, [[R(f"What the dollars leave out: residents' days in the wrong queue (16,987 in 2025 on bounces alone), hazard tickets delayed, and the calls the officer could have served instead. Bounces are counted once, in the desk row. Duplicate requests ({F['dup25']:,} in 2025) are left out: the City is already working on them.", size=7.5, color=MUT)]])
concept_strip(s, [("S2 · PROFIT TREE RECONCILES", S2), ("S2 · EXPECTED VALUE IS NOT A FORECAST", S2), ("S2 · MIX EFFECT", S2), ("S2 · SENSITIVITY", S2), ("S5 · DISAGGREGATE", S5), ("DECK STD · UNITS, SOURCE, ASSUMPTIONS", BR)])
notes(s, f"The stake as a profit tree: children multiply to the parent, the tree reconciles to {NET}. Every input is a range with a source or a stated assumption; the one that matters most, the 35% avoided, is ours, and the pilot measures it. Say it out loud: break-even is {BE}, so the 35% can be wrong {BEX} times over and the check still pays. Duplicate requests are left out because the City is already working on them; with them counted the figure was $375K. Say 'capacity, not cash' before anyone asks: officers freed for calls that need them; no budget line moves and no position is cut. The Monte Carlo spread is wide because visit cost is wide ($22 to $280).")

# =====================================================================
# 6 THE ALGORITHM
# =====================================================================
DIV[1] = divider(d, 1, "One ratio per code, three colours, and a routine where the agent still decides. Tested on a year it had never seen.", "02 · THE ALGORITHM")
s = new_slide(d, "TUE 10:13 · THE PICK IS SCORED · ONE RATIO PER CODE", foot=f"Risk score: last 12 months' empty outcomes per referral for the code, shrunk toward the City average with a prior of about 10 tickets (empirical Bayes), refreshed weekly from CRM closures. Trained on 2025, tested on Jan-Nov 2026. Shares of 2026 phone referrals: green {F['green_share']:.1f}%, amber {F['amber_share']:.1f}%, red {F['red_share']:.1f}%. Threshold maths: ask cost $1.02 / (35% x $137) = 2.1% (0.6% at agent-time pricing). {OD}. Duplicate requests left out.", section=1)
headline(s, "THE ALGORITHM · SIMPLE ON PURPOSE", ["The algorithm is one number per code: how often it ended with nothing last year. ", ("A rule turns it into three colours", ), "; the agent does the rest."])
# formula panel
panel(s, 0.3, 1.9, 6.3, 1.75, head="THE WHOLE MODEL · EXPLAINABLE IN ONE SENTENCE", head_color=CYAN, top=CYAN)
text(s, 0.45, 2.2, 6.0, 0.34, [[M("risk(code) = ", size=12.5, color=TXT), M(f"(empty visits + 10 x {F['prior_wv']:.1f}%)", size=12.5, color=AMBER), M(" / ", size=12.5, color=TXT), M("(referrals + 10)", size=12.5, color=CYAN)]])
text(s, 0.45, 2.56, 6.0, 0.26, [[M(f"+ the same ratio for desk outcomes (prior {F['prior_wd']:.1f}%). The priors are last year's City-wide rates.", size=9, color=TXT)]])
text(s, 0.45, 2.86, 6.0, 0.78, [[R(f"Counted over the last 12 months of closed phone referrals, refreshed weekly. \"This code ended with nothing to act on {F['untidy25_wv']:,} of {F['untidy25_n']:,} times last year\" is the whole explanation an agent needs. Rare codes are pulled toward the average so a code used five times cannot go red on one closure. New codes sit amber for 90 days.", size=8.8, color=MUT)]])
# three kinds of system
panel(s, 0.3, 3.8, 6.3, 2.8, head="WHAT KIND OF SYSTEM, AND THE QUESTION EACH KIND RAISES", head_color=VIOLET)
rows = [["KIND (SESSION 1)", "IN REFERRAL CHECK", "THE QUESTION TO ASK, AND OUR ANSWER"],
        ["Learns a predictive pattern", "The ratio per code, from past closures", "How were the examples labelled? By the receiving area's closure reason, so the label is the area's verdict. Build a required reason field; audit a sample."],
        ["Applies an explicit rule", "20% and 30% cut-offs; amber for new codes", "Who set the conditions and exceptions? 311 with the three pilot areas and CSU 52; reviewed at the gate."],
        ["Generates content", "Nothing. No text is written or read by a model in phase one", "Is it faithful to the source? Not triggered until phase two, when the Generative AI Standard's human-review rule applies."]]
table(s, 0.42, 4.12, 6.06, 2.38, rows, colw=[1.45, 1.75, 2.86], sizes=[8, 8, 7.5], bold_first_col=True, row_h=0.6)
# tiers
panel(s, 6.75, 1.9, 6.28, 2.95, head="WHAT THE RULE PUTS OUT · THREE TIERS", head_color=AMBER)
ty = 2.47
for (name, col, dark, share, rule, sees, does) in [
        ("GREEN", GREEN, GREEN_D, f"{F['green_share']:.0f}% of referrals, {F['green_wv']:.0f}% of empty visits", "risk under 20%", "Nothing. Route as today.", "Route"),
        ("AMBER", AMBER, AMBER_D, f"{F['amber_share']:.1f}% of referrals, {F['amber_wv']:.0f}% of empty visits", "risk 20% to 30%", "The code's rate and the area's screening questions, one click to confirm.", "Confirm or switch"),
        ("RED", RED, RED_D, f"{F['red_share']:.1f}% of referrals, {F['red_wv']:.0f}% of empty visits", "risk over 30%", "Rate, two screening questions to ask, and the alternatives (information, self-serve, report again if it persists).", "Ask, then decide")]:
    tier(s, 6.9, ty, 0.95, 0.68, name, col, dark)
    text(s, 7.95, ty - 0.02, 1.5, 0.76, [[M(rule, size=7.5, bold=True, color=col)], [R(share, size=8, color=MUT)]])
    text(s, 9.5, ty - 0.02, 2.3, 0.76, [[R(sees, size=8, color=TXT)]])
    text(s, 11.85, ty - 0.02, 1.1, 0.76, [[M(does.upper(), size=6.8, bold=True, color=col, spc=80)]])
    ty += 0.78
text(s, 6.9, 2.24, 0.95, 0.2, [[M("TIER", size=6.5, bold=True, color=MUT)]]); text(s, 7.95, 2.24, 1.5, 0.2, [[M("RULE", size=6.5, bold=True, color=MUT)]]); text(s, 9.5, 2.24, 2.3, 0.2, [[M("AGENT SEES", size=6.5, bold=True, color=MUT)]]); text(s, 11.85, 2.24, 1.1, 0.2, [[M("AGENT DOES", size=6.5, bold=True, color=MUT)]])
# why 20 not 2
panel(s, 6.75, 5.0, 6.28, 1.6, head="WHY 20%, WHEN THE DECISION TREE SAYS 2%", head_color=CYAN)
text(s, 6.9, 5.32, 6.0, 1.25, [[R(f"Rolled back right to left, a 20-second check pays whenever a code's risk is above about 2%: $1.02 against 35% of a $137 visit. That is more than half of all referrals. Attention does not scale like expected value: a prompt on every second call becomes wallpaper. So the cut-off is set by the agent's attention, not the arithmetic: flag about one call in {ONEIN} and still reach {CGT} of the empty visits. The 2% line is the floor; the gate tests the 20% line. A 15% line would flag one call in {F15['one_in_flag']} and reach {F15['caught']:.0f}%: a choice to revisit at the gate.", size=8.5, color=TXT)]])
concept_strip(s, [("S1 · THREE KINDS OF SYSTEM", S1), ("S1 · HOW WERE EXAMPLES LABELLED", S1), ("S2 · DECISION TREE THRESHOLD", S2), ("S2 · SENSITIVITY", S2), ("S3 · ATTENTION NEEDS ONE QUESTION", S3), ("S1 · PREDICTION MACHINE", S1)])
notes(s, "The algorithm is deliberately the simplest thing that works: a shrunk ratio per code, a rule, three colours. Session 1's three kinds of system each raise a question; answer all three on the slide. The rational threshold (2%) and the psychological constraint (attention) disagree; the design sides with attention and says so. A logistic model with more features did worse out of time (AUC 0.69 vs 0.82 on bounces).")

# =====================================================================
# 7 THE ROUTINE · SWIM LANE
# =====================================================================
s = new_slide(d, "TUE 10:13 · THE CHECK · WHO DOES WHAT, IN ORDER", foot="Routine decomposed after Feldman and Pentland (2003): ostensive (the steps as understood), performative (as carried out), artifacts (screens, lists, fields). Ironstone Ready-Mix (Session 7): the scheduling system removed the afternoon readiness calls nobody had written down. OCA 2023 p. 19: agents are expected to ask clarifying questions.", section=1)
headline(s, "THE ROUTINE · INPUTS, OUTPUTS, WHO ACTS", ["Four actors, one new artifact. The algorithm scores; the agent asks; the area closes with a reason; ", ("the reason comes back", ), "."])
lanes = [("RESIDENT", MUT), ("311 AGENT", CYAN), ("REFERRAL CHECK", AMBER), ("RECEIVING AREA", GREEN)]
cols = ["DURING THE CALL", "THE PICK (20 s)", "THE CHECK (+20 s)", "ROUTE", "AFTER (DAYS)", "LEARN (WEEKLY)"]
x0, y0, lw_, cw, rh = 1.55, 2.15, 1.2, 1.9, 0.84
for j, c in enumerate(cols):
    text(s, x0 + j * cw, 1.9, cw, 0.22, [{"runs": [M(c, size=6.5, bold=True, color=DIM, spc=120)], "align": "c"}])
for i, (ln, col) in enumerate(lanes):
    y = y0 + i * rh
    rect(s, 0.3, y, 12.73, rh - 0.06, BG1 if i % 2 == 0 else BG0, LINE)
    rect(s, 0.3, y, 0.05, rh - 0.06, col)
    text(s, 0.42, y, 1.1, rh - 0.06, [[M(ln, size=7, bold=True, color=col, spc=100)]], anchor="middle")
def cell(i, j, t, col=TXT, fill=BG2, bold=False, span=1):
    x = x0 + j * cw + 0.06; y = y0 + i * rh + 0.07
    p = rrect(s, x, y, cw * span - 0.12, rh - 0.2, fill, LINE, radius=0.03)
    text(s, x, y, cw * span - 0.12, rh - 0.2, [{"runs": [R(t, size=7.6, color=col, bold=bold)], "align": "c"}], anchor="middle", shape=p, margin=(0.05, 0.02, 0.05, 0.02))
cell(0, 0, "\"The yard next door is full of junk.\" Gives the address.")
cell(0, 2, "Answers two questions. Can always insist on a referral.", col=TXT)
cell(0, 4, "Hears the outcome once, with the reason, by text or email (phase 2).")
cell(1, 0, "Listens; searches the code list under a 120-s answer target.")
cell(1, 1, "Picks Complaint Registered - Untidy Property.", bold=True)
cell(1, 2, "Reads the tier, asks the two questions, then refers with the answers or gives information.", col=TXT, fill=AMBER_D)
cell(1, 3, "Final call on the referral stays here.", bold=True)
cell(1, 4, "Sees the closure reason in a daily digest to the team lead. Coaching only.")
cell(2, 1, "Looks up the code's risk and tier. Takes in: code, risk table, screening set.", col=BG0, fill=AMBER, bold=True)
cell(2, 2, "Puts out: tier, rate, questions, alternatives. Logs tier, answers and the agent's choice.", col=BG0, fill=AMBER)
cell(2, 5, "Recomputes every code's ratio; drift alerts; codes that stay flagged go to the fix queue.", fill=AMBER_D)
cell(3, 3, "Receives the ticket with the two answers attached.")
cell(3, 4, "Officer attends; closes with a required reason (one of five).", bold=True)
cell(3, 5, "Owns the screening questions and the fix queue with 311: retire, merge, reword, re-script.")
# arrows across
for (xa, ya, xb, yb) in [(x0 + 1 * cw + 0.05, y0 + 1.5 * rh, x0 + 1 * cw + 0.9, y0 + 2 * rh + 0.1)]:
    pass
# ostensive / performative / artifact strip
oy = 5.58
panel(s, 0.3, oy, 4.15, 1.07, head="OSTENSIVE · THE STEPS AS UNDERSTOOD", head_color=CYAN)
text(s, 0.42, oy + 0.3, 3.95, 0.77, [[R("Find the right code; resolve or refer. Unchanged. We add one step inside it: on risky codes, ask the standard before referring.", size=8, color=TXT)]])
panel(s, 4.6, oy, 4.15, 1.07, head="PERFORMATIVE · AS CARRIED OUT", head_color=AMBER)
text(s, 4.72, oy + 0.3, 3.95, 0.77, [[R("Search a phrase, pick the first fit, refer, next call. Where judgment moves: the \"can an officer act?\" question moves from the curb on Thursday to the line on Tuesday. The pick itself does not move.", size=8, color=TXT)]])
panel(s, 8.9, oy, 4.13, 1.07, head="ARTIFACTS · OLD AND NEW", head_color=GREEN)
text(s, 9.02, oy + 0.3, 3.9, 0.77, [[R("Old: 1,917-code list, 900 scripts, CRM status field. New: the tier on the pick screen, the screening card, a required closure reason, the weekly fix queue. Ironstone's lesson: before we add the card, ask senior agents what they already ask.", size=8, color=TXT)]])
concept_strip(s, [("S7 · OSTENSIVE / PERFORMATIVE / ARTIFACT", S7), ("S7 · IRONSTONE · TACIT WORK", S7), ("S7 · WHERE JUDGMENT MOVES", S7), ("BRIEF · IN, OUT, WHO ACTS", BR), ("S1 · AGENCY IN THE ASSEMBLAGE", S1)])
notes(s, "The brief's four questions in one picture: what goes in (the code, the risk table, the area's screening set), what comes out (tier, rate, questions, alternatives, a log), who acts (agent decides, area closes with a reason, 311 and the area run the fix queue), and the loop back. Session 7 decomposition at the bottom: the ostensive routine barely changes; the performative one gains one question; the artifacts are where the algorithm lives. Ironstone: co-design with senior agents so we do not pave over what they already ask.")

# =====================================================================
# 8 AUTOMATE VS PERSON · WHEN WRONG
# =====================================================================
s = new_slide(d, "TUE 10:14 · THE AGENT OVERRIDES · WHO DECIDES WHAT, AND WHAT IF IT IS WRONG", foot="Three elements of agency and the four agent questions: Session 1 (Reassembly of Agency); Northfield Credit Union case (score, 1-in-20 override, throughput metric). Robodebt and proxy drift: Session 9, Lindebaum et al. (2022). Refusals: Session 10 brief. Green (2022): oversight people cannot perform is not oversight; Bucinca et al. (2021): answer-first designs cut over-reliance.", section=1)
headline(s, "AUTOMATE VS LEAVE TO A PERSON · AND WHEN IT IS WRONG", ["Automate the counting and the reminder. ", ("Never the decision to refer, close or decline", ), ": those stay with people who can be asked why."])
rows = [["STEP", "AUTOMATED", "A PERSON", "WHY"],
        ["Score and tier every pick", "Yes: one ratio, one rule, weekly", "Sets the thresholds; reviews at the gate", "Counting is what machines do well; the cut-off is a value choice"],
        ["Show the screening questions", "Yes: the card appears on amber and red", "The area writes them; the agent asks them", "Only the agent hears the caller (Northfield: the interface shapes the outcome)"],
        ["Decide to refer, inform or switch code", "No", "The agent, every time; one-click override, logged", "Decision authority stays where the information is; overrides are a signal, not a fault"],
        ["Close a ticket or declare no offence", "No, ever", "The receiving area", "Accountability sits with the area that must explain the result"],
        ["Retire, merge or reword a code", "No: the queue is automatic, the decision is not", "311 knowledge team with the owning area", "Political, not statistical: areas sign off scripts today"],
        ["Coach an agent", "No: the digest is coaching material only", "Team lead", "Feedback works from a person the agent trusts; agreed in writing with CSU 52"]]
table(s, 0.3, 1.9, 7.6, 3.55, rows, colw=[1.75, 1.7, 1.85, 2.3], sizes=[8, 7.8, 7.8, 7.5], bold_first_col=True, row_h=0.47)
# four agent questions
panel(s, 0.3, 5.55, 7.6, 1.08, head="FOUR QUESTIONS FOR ANY AGENT · ACCESS · CHANGE · STOP · CORRECT", head_color=VIOLET)
text(s, 0.42, 5.85, 7.4, 0.8, [[R("Access: code, closure and referral tables in the CRM; no caller notes, no names. Change: nothing; it displays and logs. Stop: tiers fall back to green if override rate passes 80%, recording drops in a pilot area, or the service is down; agents route as today. Correct: the weekly fix queue, owned jointly; an agent can flag a wrong tier from the card.", size=8, color=TXT)]])
# when wrong cards
wx = 8.05
panel(s, wx, 1.9, 4.98, 4.73, head="WHEN IT IS WRONG · FIVE WAYS, FIVE ANSWERS", head_color=RED, top=RED)
wrongs = [("FALSE ALARM", "A flag on a real offence costs 20 to 40 seconds and one click. The override feeds the table; a code that is overridden 80% of the time is noise and goes green."),
          ("MISSED ONE", "A green code sends an officer to nothing: the same as today. The closure reason now returns within a day and the code's ratio moves."),
          ("DRIFT", "An area changes how it closes tickets (eight began recording bounces in 2026). Track recording rate by area; judge the pilot only against its control group."),
          ("RUBBER STAMP", "Agents accept every prompt: audit a sample when acceptance passes 95%. Answer-first design: the questions, never a pre-selected outcome."),
          ("TURNED INTO A GATE", "The Robodebt failure: a proxy becomes a reason to refuse service and the burden shifts to the resident. Rule: the algorithm never declines a referral; the caller can always insist; \"referrals declined without consent\" is measured and must read zero.")]
wy = 2.25
for h_, b_ in wrongs:
    text(s, wx + 0.14, wy, 1.25, 0.8, [[M(h_, size=7, bold=True, color=RED, spc=100)]])
    text(s, wx + 1.4, wy, 3.5, 0.86, [[R(b_, size=7.8, color=TXT)]])
    wy += 0.86
concept_strip(s, [("S1 · THREE ELEMENTS OF AGENCY", S1), ("S1 · FOUR AGENT QUESTIONS", S1), ("S1 · NORTHFIELD", S1), ("S10 · WHAT TO REFUSE TO AUTOMATE", S10), ("S9 · ROBODEBT · BURDEN OF PROOF", S9)])
notes(s, "Be explicit, as the brief asks. Influence: the card changes what gets asked. Decision authority: agent recommends and executes the referral; area approves the outcome; 311 and the area revise codes. Accountability: whoever must explain the result keeps the decision. Zuboff's worry (people who depend on the machine and lose the knowledge) is answered by keeping the ask with the agent and returning the outcome to them; Davenport's promise (strip bias, automate the structured part) is kept to the counting. Robodebt is the Q&A trap: say the refusal rule before anyone asks.")

# =====================================================================
# 9 EVIDENCE · BACKTEST
# =====================================================================
s = new_slide(d, "WOULD THE FLAG HAVE BEEN RIGHT? · 2025 PREDICTS 2026", foot=f"{OD}. Score trained on 2025 closures only and tested on 179,139 phone referrals from Jan 1 to Nov 6, 2026 (10,609 empty visits). Ten-year check: the same score, each year scored with the year before, on the City's yearly 311 datasets 2016-2022 and the current dataset 2023-2026 (empty_visit_backtest_2017_2026.csv). On bounces alone the lookup scored AUC 0.82 in 2026 against 0.69 for a richer logistic model. Peer results: team research, Nov 1 report (city self-reports; vendor claims excluded).", section=1)
headline(s, "EVIDENCE · OUT-OF-TIME BACKTEST", ["Last year's ratio picks this year's empty visits: ", (f"{FLG} of calls, {CGT} of the empty visits", ), ". It has ranked the next year's empty visits in each of ten years."])
pic(s, "coverage.png", 0.3, 1.9, 6.0)
pic(s, "auc.png", 6.5, 1.9, 6.53)
# stats under auc
stat(s, 6.5, 5.2, 1.55, 1.45, f"{H26:.2f}", "AUC on 2026 empty visits", sub=f"{HMIN:.2f} to {HMAX:.2f} since 2017", color=CYAN, num_size=20)
stat(s, 8.15, 5.2, 1.55, 1.45, f"{F['prec']:.0f}%", "of flagged referrals end with nothing to act on", sub=f"vs {F['any_rate26']:.0f}% of all", color=AMBER, num_size=20)
stat(s, 9.8, 5.2, 1.55, 1.45, f"r {F['r']:.2f}", "code rate, 2024 vs 2025", sub=f"{F['r_codes']} codes, 30+ each", color=GREEN, num_size=20)
stat(s, 11.45, 5.2, 1.58, 1.45, f"{F['new_wv_share']:.0f}%", "of 2026 empty visits on codes new that year", sub="new codes start amber", color=RED, num_size=20)
panel(s, 0.3, 5.2, 6.0, 1.45, head="WHAT THIS DATA CANNOT SHOW · SAID BEFORE ANYONE ASKS", head_color=MUT)
text(s, 0.42, 5.5, 5.8, 1.12, [[R("Why the officer found nothing (the resident was wrong, or the condition changed) or, for two of the five labels, whether an officer attended at all. Whether the first code differed from the final one: no re-route link exists. Which agent picked. Quiet misroutes an area fixes without a label. Peers measure what we cannot: Winnipeg publishes returns due to agent error (1.62%, 2024); Madrid's receiving units validated 79% of 38,221 AI routings. The 90-day data set (slide 12) is built to close these gaps.", size=8, color=TXT)]])
concept_strip(s, [("S3 · OVERFITTING TRAP · TEST ON UNSEEN CASES", S3), ("S5 · DISAGGREGATE BEFORE YOU CONCLUDE", S5), ("S4 · DATA LIMITS · WHAT NO PHOTO SHOWS", S4), ("S4 · ADVISERS WHO KNOW YOUR ANSWER", S4)])
notes(s, f"Evidence slide. The test was specified before the 2026 data was scored: trained on 2025, scored on 2026, so the overfitting trap is addressed. The coverage curve is the design choice made visible: pick any point; we picked {FLG} of calls for {CGT} of empty visits. Ten years of the same score on the same outcome show the ratio is not fitted to one odd year: AUC {HMIN:.2f} to {HMAX:.2f}. Say the uncomfortable part too: 2026 is the weakest of the ten years, and at the same 20% line the rule would have caught {min(H3):.0f}% to {max(H3):.0f}% of empty visits in 2023 to 2025. Then say what the data cannot show, before the executive does.")

# =====================================================================
# 10 THREE LENSES
# =====================================================================
DIV[2] = divider(d, 2, "Rational, psychological, political: each lens changes one design choice. Then the ten biases, including our own.", "03 · THE LENSES")
s = new_slide(d, "THE SHIFT DEBRIEF · THREE LENSES ON THE SAME DESIGN", foot="Rational: Glaser, Analytic Trees (threshold p. 20; option value of waiting; loss beside the average p. 21). Psychological: Glaser, The Psychological Perspective (3.2 attention, 3.3 feedback, 3.6 reference point); Kahneman and Klein (2009). Political: Session 4 (the political game; Allison: where you stand depends on where you sit; mirror imaging; sedimented assumptions; strategic foresight). CSD03148 p. 2: areas assume full ownership after routing; OCA 2023 p. 20: areas sign off scripts.", section=2)
headline(s, "THE LENS · RATIONAL, PSYCHOLOGICAL, POLITICAL", ["Each lens changes one design choice: the rational lens sets the floor, the psychological lens sets the cut-off, ", ("the political lens sets the order of asking", ), "."])
cols3 = [
    ("lauren", "The arithmetic says check almost everything. I set the floor, not the ceiling.", [
        ("EXPECTED VALUE", f"A 20-second check pays above about 2% risk; rolled back, {NET} a year of capacity across the {NC} flagged codes. An average, not a forecast."),
        ("LOSS BESIDE THE AVERAGE", f"P10 is {P10}; no draw is negative. The loss case is not money, it is 20 seconds on {FLY_R} calls and a prompt agents stop reading."),
        ("OPTION VALUE OF WAITING", f"Waiting for the 2030 CRM costs three years of freed capacity (about ${3 * MC_['net'] / 1e6:.2f}M) and arrives with no labelled data. Waiting has a price; we state it."),
        ("DOING NOTHING, STAGED OPTIONS", "The base case is on slide 14. The pilot is the small, staged option; phase two and three are bought only if the gate passes.")]),
    ("nav", "Agents do not need to be more careful. They need one concrete question and to hear how it turned out.", [
        ("ATTENTION", f"\"Be more thoughtful\" does nothing on a 120-second clock. The card gives one manageable question on one call in {ONEIN}, and the clock pauses for flagged calls."),
        ("FEEDBACK FOR INTUITION", "Kahneman and Klein: intuition needs feedback that links action to result. Today a closure reason never reaches the agent; the digest returns it within a day."),
        ("ANCHORING", "A suggested outcome would anchor. The card shows the rate and the questions, never a pre-selected answer; the agent writes the answer."),
        ("GAIN, LOSS, REFERENCE POINT", "Reference point is speed. Frame what agents gain (officers not sent to nothing, a fair measure) and name the loss (20 seconds). Calling concern \"resistance\" answers nothing.")]),
    ("rick", "The ratio is harmless. Publishing it is political: it makes the areas' closures visible for the first time.", [
        ("THE PLAYERS", "311 owns the pick; areas own the outcome labels and sign off scripts; CSU 52 represents the agents; Council asked for closure and duplicate numbers, not misroutes; the Auditor closed all five recommendations."),
        ("WHERE YOU STAND", "An area may read a published empty-visit rate as an audit of its officers. Mirror imaging: do not assume they want it counted. So the area writes the questions and co-owns the queue."),
        ("SEDIMENTED ASSUMPTION", "\"98.7% resolved on initial contact\" and \"efficiently routed\" have been repeated to Council since 2023. Nobody in the room is lying; nobody is counting."),
        ("STRATEGIC FORESIGHT", "Future to now: the 2030 CRM replacement will inherit whatever labels exist. Now to future: every pilot field is written as a requirement for it.")]),
]
cx = 0.3; cwid = 4.15
for who, quote, items in cols3:
    name, lens, col, img = LENS[who]
    person(s, who, cx, 1.9, cwid, 0.95, quote, qsize=8.6)
    iy = 2.95
    for h_, b_ in items:
        text(s, cx + 0.05, iy, cwid - 0.1, 0.92, [[M(h_, size=6.8, bold=True, color=col, spc=120)], [R(b_, size=7.9, color=TXT)]])
        iy += 0.93
    cx += cwid + 0.14
concept_strip(s, [("S2 · EV · OPTION VALUE · LOSS", S2), ("S3 · ATTENTION · FEEDBACK · ANCHORING · FRAMING", S3), ("S4 · PLAYERS · WHERE YOU SIT · MIRROR IMAGING · FORESIGHT", S4), ("S3 · ETHICS TEST", S3)])
notes(s, "The three characters from October assess the proposal. Rational: EV, loss beside the average, option value of waiting, staged options. Psychological: attention needs a concrete question (3.2), feedback for intuition (3.3, Kahneman and Klein), anchoring, gain/loss framing (3.6), and the ethics test: we use what we know about agents to help them see the 20 seconds, never to hide it. Political: the game's five questions (full table in Appendix A6), where you stand, mirror imaging, sedimentation, foresight both directions. Each lens changes a design choice; say which.")

# =====================================================================
# 11 BIASES
# =====================================================================
s = new_slide(d, "WED · THE TEAM CHAT · \"WHY DIDN'T WE CATCH IT?\" · THE BIASES, AND OURS", foot="Biases as taught in Session 3 (Glaser, The Psychological Perspective; Tversky and Kahneman 1974, 1981; Nickerson 1998; Moore and Healy 2008; Kahneman and Tversky 1979; Arkes and Blumer 1985; Fazio et al. 2015; MacGarvie and McElheran 2018). Method rule: say what happened, then the tendency, then what is neglected; a heuristic is a shortcut, a bias is a systematic distortion under particular conditions.", section=2)
headline(s, "BIASES · SAY WHAT HAPPENED BEFORE NAMING ONE", ["Ten biases from the course, each with the situation first, and ", ("the design choice that answers it", ), ". Two of them are ours."])
rows = [["BIAS", "WHAT HAPPENS (THE SITUATION)", "WHAT IS NEGLECTED", "WHAT THE DESIGN DOES"],
        ["Availability", "A memorable empty visit (or a memorable real offence) stands in for how often each happens", "The ordinary, unmemorable cases: 4,877 untidy-property referrals a year", "The ratio counts every case; the card shows the rate, not an anecdote"],
        ["Confirmation", "System 2 searches the code list to confirm the code System 1 offered", "Evidence the standard is not met", "The screening questions ask the other way round: what would make this not an offence?"],
        ["Anchoring", "A ranked suggestion on screen becomes the answer", "The caller's actual words", "No pre-selected outcome; the agent records the answers and decides"],
        ["Overconfidence", "\"99% of referrals land correctly\" reads as \"the pick is fine\"", "Overprecision: the 99% is routing, not usefulness", "Report precision per code (28%, 43%, 62%), never a city-wide average"],
        ["Framing", f"\"98.7% resolved on initial contact\" vs \"1 in {ANY1} referrals ends with nothing to do\"", "The same facts, said the other way", "The scorecard carries both lines"],
        ["Loss aversion", "Agents' reference point is the 120-second clock; areas' is control of their closures", "What each side experiences as lost", "Pause the clock on flagged calls; areas write the questions and co-own the queue"],
        ["Sunk cost", "\"Wait for the 2030 CRM\" or \"we already built the script search\"", "What can still change now at low cost", "A lookup table and a card; every field doubles as a CRM requirement"],
        ["Jumping to conclusions", "\"Agents are careless\" is a coherent story", "The code set and the labels are built by the system, not the agent", "The problem tree names nine causes; the agent is one leaf"],
        ["Illusory truth", "\"Efficiently routed to the appropriate department\" repeated in reports since 2023", "Where the claim originated: no routing measure exists", "Put a measured rate beside the repeated phrase"],
        ["Overfitting", "A model that explains 2025 perfectly", "Whether it predicts cases not yet seen", f"Trained on one year, tested on the next, ten years running (AUC {HMIN:.2f} to {HMAX:.2f}); one ratio, not a feature-rich model"]]
fills = {}
table(s, 0.3, 1.9, 9.1, 4.75, rows, colw=[1.2, 2.9, 2.3, 2.7], sizes=[8, 7.3, 7.3, 7.3], bold_first_col=True, row_h=0.42)
panel(s, 9.55, 1.9, 3.48, 4.75, head="OUR OWN · DECLARED BEFORE Q&A", head_color=ORANGE, top=ORANGE)
text(s, 9.68, 2.22, 3.22, 4.3, [[M("CONFIRMATION", size=7, bold=True, color=ORANGE, spc=120)], [R(f"We went looking for a bigger dollar case after the bounce case came in at $7K to $17K, and found one. Our first figure ($375K) counted duplicate requests the City is already fixing; a team member caught it. Re-run without them: {NET}. The out-of-time test held.", size=8, color=TXT)],
                                 {"runs": [M("OVERCONFIDENCE", size=7, bold=True, color=ORANGE, spc=120)], "before": 8}, [R(f"The 35% avoided share has no source; it is a team judgment with a 20% to 50% range. The case holds down to {BE}. The pilot replaces the assumption with a measurement.", size=8, color=TXT)],
                                 {"runs": [M("PROMPT FRAMING", size=7, bold=True, color=ORANGE, spc=120)], "before": 8}, [R("Asking an AI for \"the most savings\" produces savings. We asked the loss side separately: who pays for the 20 seconds, and who could be refused service.", size=8, color=TXT)],
                                 {"runs": [M("HEURISTIC OR BIAS?", size=7, bold=True, color=ORANGE, spc=120)], "before": 8}, [R("\"Untidy yard means the untidy-property code\" is a useful shortcut. It becomes a bias only under one condition: no feedback. The design changes the condition, not the person.", size=8, color=TXT)]])
concept_strip(s, [("S3 · TEN BIASES", S3), ("S3 · SITUATION, TENDENCY, NEGLECTED", S3), ("S3 · HEURISTIC VS BIAS", S3), ("S3 · PROMPT FRAMING MOVES THE ANSWER", S3), ("S2 · SIX QUESTIONS FOR AN ANALYSIS", S2)])
notes(s, "Each row follows the method rule: the situation, then the tendency, then what is neglected, then the design answer. Keep the agents out of the dock: the biases live in the system (no feedback, a speed clock, a label built by the area). Own ours in the room before the examiner finds them: confirmation (we wanted a dollar case), overconfidence (35%), framing of our own prompts.")

# =====================================================================
# 12 DATA
# =====================================================================
DIV[3] = divider(d, 3, "The data the City has, the 90-day data set it does not, the gate, the measures, and the three decisions for this room.", "04 · DATA AND PLAN")
s = new_slide(d, "THU · THE AREA CLOSES THE TICKET · WHAT RECORD DOES THAT LEAVE?", foot=f"Inventory columns after the Session 6 exercise (Scandinavian Building Services, Ivey W35309): have it, structured or not, real-time or batch, decision it serves, gap. SBS lesson: the 10-1-24 figure measured the reply, not the fix. Session 1: how the examples were labelled. Volumes: about {PM} flagged phone referrals a month at the 20% cut-off (2026 pace).", section=3)
headline(s, "DATA · CONSTRUCTED, THEN LEVERAGED", ["The ratio needs five fields the City already has. ", ("Learning needs a data set that does not exist yet", ), ": we build it in the first 90 days."])
rows = [["DATA", "HAVE IT?", "FORM", "USED FOR", "WHO MUST CHANGE BEHAVIOUR"],
        ["Code, area, channel, referral type, closure label, dates", "Yes, public", "Structured, batch", "The ratio, the tiers, the backtest", "No one"],
        ["Ticket address, agent ID, handle time", "Yes, in the CRM (inferred; not public)", "Structured, real-time", "Digest routing, handle-time guardrail, phase-two owner lookup", "CRM owner: a data agreement with 311"],
        ["Closure reason, consistent across areas", "Partly: eight areas began recording in 2026", "Structured, batch", "The label every ratio learns from", "Receiving areas: a required reason on every closure"],
        ["Screening answers on flagged calls", "No", "Structured, real-time (two fields)", "The 90-day data set; answer-level risk in phase two", "Agents: record two answers; CSU 52 agreement"],
        ["Agent's choice after the card (refer / inform / caller insisted)", "No", "Structured, real-time", "Override rate, consent guardrail, training label", "Comes free with the card"],
        ["Link from a referred ticket to its final code (re-route)", "No; cannot be rebuilt from open data", "Structured, batch", "Whether the picked code was the right code", "Area dispatch clerks: one field on reassignment"],
        ["Accuracy of codes on calls resolved on the phone (473,564)", "No", "Sampled QA", "Replaces the stake's biggest unknown", "311 QA: about 200 calls a month"]]
table(s, 0.3, 1.9, 8.2, 4.1, rows, colw=[2.2, 1.6, 1.3, 1.75, 1.35], sizes=[7.6, 7.3, 7.3, 7.3, 7.3], bold_first_col=True, row_h=0.5)
text(s, 0.3, 6.05, 8.2, 0.6, [[R("Data is built. The label we learn from is the receiving area's verdict, written under its own incentives. A measure constructed slightly wrong rewards the wrong thing: an empty-visit rate on its own rewards areas for closing \"no action\" less often, whatever happened at the curb. So every rate is paired with resident re-contact within 30 days, and the labels are audited by sample.", size=8, color=MUT)]])
# 90-day data set
panel(s, 8.65, 1.9, 4.38, 4.75, head="THE 90-DAY DATA SET · BUILT SO THE ALGORITHM CAN LEARN", head_color=AMBER, top=AMBER)
text(s, 8.78, 2.24, 4.1, 4.4, [[R("One row per flagged phone referral, from day 31:", size=8.5, bold=True, color=TXT)],
                               [R("code picked · tier and rate shown · the two answers · agent's choice · caller insisted (y/n) · days to closure · closure reason · reassigned to (final code) · re-contact within 30 days", size=8, color=MUT)],
                               {"runs": [M("SIZE BY DAY 90", size=7, bold=True, color=AMBER, spc=120)], "before": 8},
                               [R(f"About {DS_LOG} flagged referrals logged (30 days of shadow, 30 of pilot); about {DS_CLO} closed with a reason by day 90; about {DS_EMP} empty visits labelled by then, about {DS_ALL} once all have closed. Enough to re-estimate the ratio of every code with 30 or more closures.", size=8, color=TXT)],
                               {"runs": [M("WHAT IT LETS THE ALGORITHM LEARN", size=7, bold=True, color=AMBER, spc=120)], "before": 8},
                               [R("1  Whether the two answers predict an empty visit better than the code alone (answer-level risk, phase two).", size=8, color=TXT)],
                               [R("2  Whether the picked code and the final code differ: the first ground truth for \"coded correctly\" the City will ever have.", size=8, color=TXT)],
                               [R("3  Which codes are confusing versus which standards are unclear: two different fixes.", size=8, color=TXT)],
                               {"runs": [M("RULES FOR THE SET", size=7, bold=True, color=AMBER, spc=120)], "before": 8},
                               [R("No caller names or notes. Agent ID held by 311 QA only, never in the digest. Held out by time before any model is trained on it. Every field written as a requirement for the 2030 CRM.", size=8, color=TXT)]])
concept_strip(s, [("S6 · DATA IS BUILT", S6), ("S6 · INVENTORY COLUMNS", S6), ("S6 · SBS · REPLY IS NOT FIX", S6), ("S1 · HOW EXAMPLES WERE LABELLED", S1), ("S1 · DATA STRUCTURE IS A CHOICE", S1), ("S5 · WHAT IT CANNOT SHOW", S5)])
notes(s, "This is the 30% criterion. Left: the inventory in the Session 6 columns, with the behaviour change each gap needs. Right: the data set the City does not have and the pilot creates: one row per flagged call with the answers, the agent's choice, the outcome and the re-route. By day 90 it is large enough to re-estimate pilot codes from their own closures and to test whether answers beat codes. Labels are the area's verdict: audit them, pair them with re-contact.")

# =====================================================================
# 13 INTEGRATION · 90 DAYS
# =====================================================================
s = new_slide(d, "THE PLAN · FIRST 90 DAYS, THE GATE, THEN PHASES TWO AND THREE", foot=f"Split after the course's consulting-deck standard (USPS 2010): what 311 can do within its own authority vs what needs others. Pilot by team-week randomisation, half the teams; at about {PM} flagged calls a month a 20% relative drop needs about {round(F['pw20']['n'], -1):,.0f} flagged referrals in each arm, about one month of pilot calls, and reads out near week seven once those visits close (80% power, 5% two-sided; team-week clustering makes this a minimum). Strategic foresight: Session 4. Generative AI Standard (Jul 2024, s. 3.2 Jul 2025) and the Privacy Impact Assessment standard (May 2026) apply from phase two.", section=3)
headline(s, "INTEGRATION · PHASED, GATED", ["Ninety days inside 311's own authority, three areas, half the teams. ", ("Phase two is bought only if the gate passes", ), "."])
phases = [("DAYS 1-30 · BUILD, NO SCREEN CHANGE", CYAN, [
              ("311", "Re-run the backtest on internal closures; pick the three pilot areas (Municipal Enforcement, Peace Officers, Parking: 3 of every 4 flagged empty visits)."),
              ("311 + AGENTS + CSU 52", "Co-design the card with senior agents: what do they already ask? Agree in writing: digest is coaching only, no individual ranking."),
              ("NEEDS OTHERS", "Data agreement with the CRM owner; required closure reason and a reassignment field in the three areas; each area writes its two screening questions.")]),
          ("DAYS 31-60 · SHADOW MODE", AMBER, [
              ("311", f"Score every pick, show nothing. Confirm about {FLG} would be flagged and the mix matches the backtest."),
              ("DATA SET STARTS", "Log tier, outcome, reason and re-route for every flagged referral. Daily digest and weekly fix queue begin."),
              ("NEEDS OTHERS", "Areas close with a reason on 80% or more of flagged referrals, or the pilot waits.")]),
          ("DAYS 61-90 · PILOT", GREEN, [
              ("311", "Card on for half the teams, chosen by team-week at random; the other half is the control. Clock paused on flagged calls."),
              ("DATA SET FILLS", "Two answers and the agent's choice logged on every flagged call; QA samples 200 resolved calls a month."),
              ("NEEDS OTHERS", "Weekly fix queue with the three areas: retire, merge, reword, re-script. Union walkthrough at day 75.")])]
px = 0.3; pw = 3.0
for head, col, items in phases:
    panel(s, px, 1.9, pw, 3.25, head=head, head_color=col, top=col)
    iy = 2.25
    for h_, b_ in items:
        text(s, px + 0.12, iy, pw - 0.24, 0.95, [[M(h_, size=6.5, bold=True, color=col, spc=100)], [R(b_, size=7.8, color=TXT)]])
        iy += 0.95
    px += pw + 0.1
# gate
panel(s, 9.6, 1.9, 3.43, 3.25, head="THE GATE · DAY 120 · ALL MUST BE TRUE", head_color=RED, top=RED)
gate = ["Empty-visit rate on flagged codes, pilot teams vs control: down 20% or more",
        "Referrals a caller wanted and did not get: zero",
        "Handle time on flagged calls: up 15 seconds or less; 120-s answer target still met",
        "Override rate between 20% and 80%",
        "Closure reason present on 80%+ of flagged referrals in all three areas",
        "Data set: 3,500+ flagged calls with a closure reason",
        "Three areas and CSU 52 sign the phase-two scope"]
gy = 2.22
for g_ in gate:
    text(s, 9.72, gy, 0.2, 0.3, [[M("□", size=9, color=RED)]]); text(s, 9.92, gy, 3.0, 0.42, [[R(g_, size=7.7, color=TXT)]]); gy += 0.4
# phases 2 and 3
panel(s, 0.3, 5.25, 6.2, 1.4, head="PHASE TWO · MONTHS 5-12 · IF THE GATE PASSES", head_color=VIOLET)
text(s, 0.42, 5.55, 5.95, 1.1, [[R("All teams and all areas. Retrain the ratio on the 90-day set; test answer-level risk in shadow first. Then the text suggestion on the agent's typed notes (top three codes, never pre-selected), reusing the City's app AI of July 2026: Generative AI Standard human review, a privacy impact assessment, 85% top-three accuracy offline before it is shown. Resident sees the closure reason by text or email.", size=8, color=TXT)]])
panel(s, 6.6, 5.25, 6.43, 1.4, head="PHASE THREE · 2027 ON · OPTIONS WITH A START CONDITION", head_color=MUT)
text(s, 6.72, 5.55, 6.2, 1.1, [[R("Every pilot field becomes a requirement for the 2030 CRM replacement (future to now). The shared app and web intake platform the team debated starts only if the phone pilot passes and app bounce rates move after the City's own AI suggestion (no visible fall in three months so far). Full automatic routing is not on the roadmap: no accuracy test, no stop rule, and the Standard requires review.", size=8, color=TXT)]])
concept_strip(s, [("DECK STD · WITHIN CONTROL VS NEEDS OTHERS", BR), ("S4 · STRATEGIC FORESIGHT", S4), ("S2 · STAGED OPTIONS", S2), ("S7 · DASHBOARD SIM · WHAT THE SYSTEM MAKES INVISIBLE", S7), ("S10 · GOVERNANCE", S10)])
notes(s, "Ninety days in three columns, each split into what 311 controls and what needs others. The gate is numeric and complete: every line must be true. Phase two is where the AI assistant from the team's plan enters, gated and in shadow first. Phase three carries the CRM requirements and the platform option with its start condition. Pilot length: about a month of pilot calls reads out a 20% drop; the day-120 gate leaves room for those visits to close and for team-week clustering.")

# =====================================================================
# 14 HOW WE KNOW IT WORKS
# =====================================================================
s = new_slide(d, "THE DEBRIEF · HOW WILL 311 KNOW IT WORKED?", foot=f"Measures chosen before launch (Session 9: proxies drift from what they stand for; values wither when nothing measures them). Base case: {BASE} of flagged referrals ended in an empty visit in 2026. Weekly City-wide phone-referral bounce rates ran 0.79% to 2.05% between April and October 2026, so the City-wide average cannot be the test. Robodebt: the burden of proof must stay with the City.", section=3)
headline(s, "HOW THE CITY WOULD KNOW · MEASURES CHOSEN BEFORE LAUNCH", ["One primary measure, paired with the thing it could corrupt. ", ("Containment and handle time are guardrails, never targets", ), "."])
rows = [["MEASURE", "BASELINE", "GATE / TARGET", "TYPE", "WHAT IT COULD REWARD BY MISTAKE, AND THE PAIR"],
        ["Empty-visit rate on flagged codes, pilot vs control", f"{BASE} (2026)", "down 20%+ at the gate; 35% expected", "Primary", "Areas closing \"no action\" less often on paper: paired with the re-contact line below"],
        ["Resident re-contact within 30 days on flagged calls", "to be measured in shadow", "no rise", "Resident-facing", "Catches a check that talks residents out of real problems"],
        ["Referrals a caller wanted and did not get", "none today", "zero", "Guardrail (Robodebt)", "The algorithm becoming a gate; burden shifting to the resident"],
        ["Median days in the wrong queue per bounce", "2.0 days (2026 phone)", "down", "Resident-facing", "Kept from October; bounces still matter for hazards"],
        ["Closure reason back to the agent within 24 h", "none today", "90%", "Learning loop", "A digest nobody opens: track opens, not sends"],
        ["Codes cleared from the fix queue per quarter", "none today", "rising, then falling", "Learning loop", "Clearing codes by deleting them: pair with re-contact"],
        ["Average handle time on flagged calls", "from 311", "+15 s or less", "Guardrail", "Never a target: a target here recreates the speed incentive"],
        ["Override rate", "none today", "20% to 80%", "Guardrail", "Below 20%: rubber stamp. Above 80%: the tier is noise"],
        ["Recording rate by area", "varies", "stable", "Data health", "Judge the model only where recording is stable"]]
table(s, 0.3, 1.9, 8.4, 4.75, rows, colw=[2.3, 1.15, 1.25, 1.05, 2.65], sizes=[7.6, 7.2, 7.2, 7, 7.2], bold_first_col=True, row_h=0.45)
pic(s, "gate.png", 8.85, 1.9, 4.18)
panel(s, 8.85, 4.15, 4.18, 2.5, head="WHAT WOULD CHANGE OUR MINDS", head_color=AMBER)
text(s, 8.97, 4.45, 3.95, 2.15, [[R(f"Shadow mode flags 20%+ of calls rather than {FLG}: raise the cut-off before any agent sees it.", size=8, color=TXT)],
                                 {"runs": [R("Re-contact rises on flagged calls: the check is talking residents out of real problems; stop and redesign the questions.", size=8, color=TXT)], "before": 4},
                                 {"runs": [R("Empty-visit rate falls in the control group too: a recording change, not us; extend the pilot.", size=8, color=TXT)], "before": 4},
                                 {"runs": [R("Handle time rises more than 15 s: the card is too long; cut to one question.", size=8, color=TXT)], "before": 4},
                                 {"runs": [R("Values we refuse to trade: no resident is refused a referral; no agent is ranked by the digest.", size=8, color=AMBER)], "before": 4}])
concept_strip(s, [("S9 · PROXY DRIFT · VALUES WITHER", S9), ("S9 · MEASURES BEFORE LAUNCH", S9), ("S6 · EVERY MEASURE REWARDS SOMETHING", S6), ("S2 · WHAT FLIPS THE RECOMMENDATION", S2), ("DECK STD · BASE CASE FIRST", BR)])
notes(s, "Session 9 applied to ourselves. The primary measure (empty-visit rate on flagged codes) could be gamed by areas closing differently, so it is paired with resident re-contact. The Robodebt guardrail is explicit: referrals a caller wanted and did not get must be zero. Handle time and containment stay guardrails, not targets, or the routine recreates the speed incentive the problem tree found. 'What would change our minds' pre-empts the Q&A.")

# =====================================================================
# 15 THE ASK · PREMORTEM
# =====================================================================
s = new_slide(d, "THE ASK · THREE DECISIONS FOR THIS ROOM", foot="Premortem after Klein (2007). Peer evidence: team research Nov 1 and Nov 11 reports (Amsterdam Signalen, Dutch algorithm register gm0363; Winnipeg 311 budget presentation Dec 9, 2025 p. 6; Madrid SyRCI-IA, Interoperable Europe listing; Denver Council record 26-1373 and Auditor report Aug 2025; Toronto 'Simplifying the 311 Intake Experience' Apr 30, 2026). One-time cost is a team estimate with no City quote: a lookup table, one card and two CRM fields, not a platform.", section=3)
headline(s, "RECOMMENDATION", ["Approve a 90-day pilot in three areas and ", ("decide again at day 120", ), " with the numbers on the previous slide."])
asks = [("1", "APPROVE THE PILOT", f"Referral Check on the {NC} codes above 20% risk, three areas, half the teams by team-week. One-time configuration estimated at $10K to $150K (assumed; no City quote); running cost about {COST} a year of agent time, inside the {NET} of capacity it frees. Capacity, not cash."),
        ("2", "SIGN THE DATA AGREEMENT", "Two CRM fields (closure reason, reassignment) in Municipal Enforcement, Peace Officers and Parking Enforcement, and 311's access to internal closures. This is the step that needs people outside 311."),
        ("3", "SET THE TERMS WITH CSU 52", "Coaching only, no individual ranking, the clock paused on flagged calls, and a walkthrough at day 75. Agreed before any agent sees a card.")]
ax_ = 0.3
for n_, h_, b_ in asks:
    rrect(s, ax_, 1.9, 4.1, 1.75, BG1, LINE, radius=0.04)
    text(s, ax_ + 0.15, 1.95, 0.6, 0.6, [[M(n_, size=26, bold=True, color=AMBER)]])
    text(s, ax_ + 0.75, 2.05, 3.25, 0.3, [[M(h_, size=8, bold=True, color=TXT, spc=150)]])
    text(s, ax_ + 0.75, 2.35, 3.25, 1.3, [[R(b_, size=8.2, color=MUT)]])
    ax_ += 4.2 + 0.1
# premortem
panel(s, 0.3, 3.8, 6.2, 2.85, head="PREMORTEM · IT IS DECEMBER 2027 AND IT FAILED. WHY?", head_color=RED, top=RED)
pm = [("THE RATE FELL ON PAPER", "Areas closed fewer tickets as \"no action\" and more as \"resolved\". Residents re-contacted more. Answer: the paired re-contact measure, label audits by sample."),
      ("AGENTS CLICKED THROUGH", "The card became wallpaper; override rate sat at 5%. Answer: the 20% to 80% guardrail, one question not two, coaching from a team lead who sees the digest."),
      ("THE SIGNAL DROWNED", "Two more areas changed recording mid-pilot and the control group moved too. Answer: judge pilot against control, by area, never on the City-wide rate."),
      ("A REASON NOT ON THE TREE", "The CRM vendor could not add two fields before 2028. Answer: the shadow phase and the data set run on exports; the card waits.")]
py = 4.12
for h_, b_ in pm:
    text(s, 0.42, py, 1.45, 0.62, [[M(h_, size=6.5, bold=True, color=RED, spc=80)]])
    text(s, 1.9, py, 4.5, 0.66, [[R(b_, size=7.8, color=TXT)]]); py += 0.63
# upside / downside and peers
panel(s, 6.6, 3.8, 3.15, 2.85, head="UPSIDE AND DOWNSIDE", head_color=CYAN)
text(s, 6.72, 4.12, 2.9, 2.5, [[M("UPSIDE", size=6.5, bold=True, color=GREEN, spc=120)], [R(f"P90 {P90}; answer-level risk in phase two reaches the {F['green_wv']:.0f}% of empty visits that sit in green codes; residents hear the reason.", size=7.8, color=TXT)],
                               {"runs": [M("DOWNSIDE", size=6.5, bold=True, color=RED, spc=120)], "before": 6}, [R(f"P10 {P10}; 20 seconds on {FLY_R} calls a year; a published rate the areas resent. Nothing in the pilot is hard to undo: turn the card off and the fields remain useful.", size=7.8, color=TXT)]])
panel(s, 9.85, 3.8, 3.18, 2.85, head="WHAT OTHER CITIES TEACH", head_color=GOLD)
text(s, 9.97, 4.12, 2.95, 2.5, [[R("Winnipeg already publishes returns due to agent error (1.62% in 2024): measuring misroutes is normal.", size=7.8, color=TXT)],
                                {"runs": [R("Madrid: rules first, then AI; the receiving unit validated 79% of 38,221 routings and rejections retrain the model.", size=7.8, color=TXT)], "before": 5},
                                {"runs": [R("Amsterdam (Signalen, live since 2022): a model suggests the category, anything under 40% confidence goes to a human desk, staff corrections retrain it. The closest precedent for a human-in-the-loop check.", size=7.8, color=TXT)], "before": 5},
                                {"runs": [R("Denver: a chatbot paired with cuts; Council voted 9 to 3 against a US$3.9M extension. A tool plus job cuts invites a fight. Ours cuts no position.", size=7.8, color=TXT)], "before": 5}])
concept_strip(s, [("S2 · PREMORTEM", S2), ("S2 · DOING NOTHING · STAGED OPTIONS", S2), ("DECK STD · RISKS BESIDE THE FORECAST", BR), ("S4 · THE POLITICAL GAME · WHO SAYS YES, IN ORDER", S4), ("BRIEF · NOT ALREADY DOING IT", BR)])
notes(s, "Close on the decision the room can take today. Three asks, in the order the political game requires: 311 approves, the CRM owner and three areas sign, the union agrees the terms. Premortem (Klein): four failure stories, each with the answer already in the design; the fourth is the reason not on the tree. Upside and downside beside the forecast, as the consulting standard asks. Peers: measuring misroutes is ordinary (Winnipeg); humans validate AI routing (Madrid); tools paired with cuts fail politically (Denver).")

# =====================================================================
# 16 AI PROCESS REFLECTION
# =====================================================================
s = new_slide(d, "AI PROCESS REFLECTION · HOW WE WORKED, WHERE THE AI WAS WRONG", foot="Sloan and Glaser (2026), Stop Prompting AI, Start Directing It; Glaser, Sloan and Knight (2025): assistant, analyst, coach; Mollick (2024) four rules; AI Literacy Exercise brief: tools, crux moves, validation, errors. All analysis and final writing are the team's own; AI drafts were rewritten and every figure re-derived from the open data by a team member.", section=3)
headline(s, "REQUIRED SLIDE", ["AI Process Reflection ", ("· how we worked, and where the AI was wrong",)])
quads = [("TOOLS, AND THE KIND OF TASK EACH DID", CYAN, [
            "Analyst: Claude with Python and DuckDB over 3.5 million open-data rows (the backtest, the ten-year check, the Monte Carlo). Source-grounded, re-runnable scripts in the project folder.",
            "Assistant: first drafts of slide text, the swim lane and this deck's build script; the team rewrote every slide in its own words.",
            "Coach: AI played the skeptical 311 director (\"why fix something 99% right?\", \"is this cash?\") and the CSU 52 representative before each team meeting.",
            "Fact-checkers: separate AI agents checked the Nov 1 research report against its sources: 610 rows, 369 verified, 208 corrected, 25 unverified, 8 wrong."]),
         ("TWO CRUX MOVES", AMBER, [
            "The AI argued against our own AI idea. Asked to validate an AI code suggester trained on past tickets, it showed the training labels are agents' own picks (errors included) and that LLM-written test tickets would be circular. We kept the suggester, but as a gated phase two behind a human-built data set.",
            "\"Give me the most savings\" moved the decision. The first routine (bounces only) came back at $7K to $17K a year. Directed to find the larger loss, the analysis found 12,583 referrals that ended with nothing to act on. Re-running it showed the flagged codes are bylaw complaints, so the question on the card changed from \"who owns it?\" to \"does it meet the standard?\"."]),
         ("HOW WE VALIDATED", GREEN, [
            "Two independent pulls: the City's API and the team's own six-part CSV export; counts matched (191,521 phone referrals 2025; 179,139 in 2026).",
            "Every model was trained on one year and tested on the next; a richer model that scored better in-sample scored worse out of time and was dropped.",
            "Every figure on a slide has a source or is labelled assumed; where a citation could not be opened, it was dropped.",
            "Framing test: the same question asked gain-first and loss-first; the loss-first run produced the refusal rule and the re-contact pairing."]),
         ("WHERE THE AI WAS WRONG, AND WHAT WE DID", RED, [
            f"Its first savings figure ($375K) counted duplicate requests, which the City is already fixing. A team member caught it. Re-run without them: {NET}, and {NC} codes instead of 150.",
            "It wrote that red codes hold 65% of empty visits; that was amber and red together (red alone: 28%). It also offered ten years of bounce results as evidence about empty visits. A second AI review caught both, and we re-ran the right test.",
            "It proposed the 35% avoided share with confidence and no source. We kept it only as a labelled assumption with a range, and built the pilot to replace it.",
            "It drafted fluent slide prose that read as our own. The syllabus says the final writing must be ours; we rewrote, and kept a log of what changed."])]
qx, qy = 0.3, 1.85
for i, (h_, col, items) in enumerate(quads):
    x = qx + (i % 2) * 6.4; y = qy + (i // 2) * 2.42
    panel(s, x, y, 6.33, 2.32, head=h_, head_color=col, top=col)
    text(s, x + 0.14, y + 0.33, 6.05, 1.95, [{"runs": [R("• " + t, size=7.9, color=TXT)], "after": 3} for t in items])
concept_strip(s, [("S8 · DIRECT, DON'T PROMPT", S1), ("S1 · ASSISTANT / ANALYST / COACH", S1), ("S1 · MOLLICK · HUMAN IN THE LOOP", S1), ("S3 · PROMPT FRAMING", S3), ("BRIEF · TOOLS · CRUX · VALIDATION · ERRORS", BR)])
notes(s, "Draft only: the team must write this slide in its own voice and with its own log. The four quadrants follow the brief: tools by kind of task, one or two crux moves, how outputs were validated, and what happened when the AI was wrong. 'A reflection that reports only successes has not been written honestly.' The figures in the fact-check line come from the Nov 1 team report: have it on hand, or drop the line. The duplicates catch is the strongest example on the slide because a person, not the AI, found it.")


# =====================================================================
# 17 CLOSING · QUESTIONS · THE MAYOR WATCHES THE BARS FALL
# =====================================================================
s = new_slide(d, "END OF THE FEED · QUESTIONS", section=3, foot="")
headline(s, "QUESTIONS", ["Every empty visit avoided is an officer ", ("on a call that needed one",), ". Decide again at day 120."])
# the improvement, drawn as four bars
panel(s, 0.3, 1.9, 7.3, 4.75, head="FLAGGED REFERRALS ENDING IN AN EMPTY VISIT · % · PILOT TEAMS VS CONTROL", head_color=CYAN)
bars = [("Today", "2026 base", F["gate"][0], RED), ("Pilot gate", "20% drop", F["gate"][1], MUT), ("Expected", "35% drop", F["gate"][2], CYAN), ("Upside", "50% drop", F["gate"][3], GREEN)]
base = 5.85; maxh = 3.0; bx = 0.75; bw = 1.3; gap = 0.42
for i, (lab, lab2, v, col) in enumerate(bars):
    x = bx + i * (bw + gap); h = maxh * v / F["gate"][0]
    rect(s, x, base - h, bw, h, col)
    text(s, x - 0.1, base - h - 0.36, bw + 0.2, 0.34, [{"runs": [R(f"{v:.1f}%", size=12, bold=True, color=col)], "align": "c"}], anchor="bottom")
    text(s, x - 0.15, base + 0.04, bw + 0.3, 0.5, [{"runs": [R(lab, size=9, bold=True, color=TXT)], "align": "c"}, {"runs": [R(lab2, size=8, color=MUT)], "align": "c"}])
line(s, 0.6, base, 7.45, base, LINE2, 1)
# right column
stat(s, 7.75, 1.9, 5.28, 1.05, f"{NET} a year", f"of officer and desk capacity freed; P10-P90 {RNG}; no budget line moves", color=GREEN, num_size=20, top=GREEN)
stat(s, 7.75, 3.05, 5.28, 1.05, f"{NC} codes", f"{FLG} of phone referrals checked; {CGT} of the empty visits reached", color=CYAN, num_size=20, top=CYAN)
stat(s, 7.75, 4.2, 5.28, 1.05, "Day 120", "the gate: all seven lines true, or the card comes off and the fields stay", color=AMBER, num_size=20, top=AMBER)
text(s, 7.75, 5.4, 5.28, 1.2, [[R("You're all caught up.", size=14, bold=True, color=TXT)], [R("Thank you. Questions?", size=11, color=MUT)]])
concept_strip(s, [("S2 · DECIDE AGAIN AT THE GATE", S2), ("S9 · MEASURES BEFORE LAUNCH", S9), ("BRIEF · Q&A IS MARKED", BR)])
# Mayor Knack, peeking over the bottom edge at the last stop, eyes on the bars (placeholder drawn from shapes until a photo is supplied)
lib3.XF = False
cx = 11.45; SKIN = "E8B88E"; HAIR = "3B2A1E"; OV = MSO_SHAPE.OVAL
rect(s, 9.95, 6.62, 3.4, 0.9, BG0)                                                       # clear the last tab and page number behind him
rect(s, cx - 1.0, 6.66, 2.0, 1.5, HAIR, shape=OV)                                        # hair
rect(s, cx - 1.06, 7.0, 0.2, 0.42, SKIN, shape=OV); rect(s, cx + 0.86, 7.0, 0.2, 0.42, SKIN, shape=OV)   # ears
rect(s, cx - 0.88, 6.84, 1.76, 2.1, SKIN, shape=OV)                                      # face, running off the bottom edge
for ex in (cx - 0.5, cx + 0.14):
    b = rect(s, ex - 0.03, 6.96, 0.42, 0.055, HAIR, shape=MSO_SHAPE.ROUNDED_RECTANGLE); b.rotation = -9 if ex < cx else 9   # raised brows
    rect(s, ex, 7.09, 0.36, 0.26, WHITE, shape=OV)                                       # eye
    rect(s, ex + 0.05, 7.1, 0.16, 0.16, "1B1B1B", shape=OV)                              # pupil, looking up and left at the bars
    rect(s, ex + 0.08, 7.12, 0.05, 0.05, WHITE, shape=OV)
for hx in (cx - 1.62, cx + 1.14):                                                        # fingers over the edge
    for k in range(4):
        rect(s, hx + k * 0.125, 7.3 - (0.03 if k in (1, 2) else 0), 0.115, 0.3, SKIN, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
text(s, 8.2, 6.31, 4.68, 0.22, [{"runs": [R("PLACEHOLDER FOR MAYOR KNACK  ·  SWAP IN A PHOTO (SEE NOTES)", size=6.5, bold=True, color=AMBER)], "align": "r"}], anchor="middle")
notes(s, f"Closing slide after the ask. The bars are the gate arithmetic from Appendix A5: {BASE} today, {G1} at the gate, {G2} expected, {G3} upside. The head at the bottom edge is a placeholder for Mayor Knack watching the bars fall; to swap in a photo, delete the drawn shapes, insert a head-and-shoulders picture, crop it so only the top of the head and the eyes show, and rest it on the bottom edge at the right. Take questions here; the appendix follows for the numbers.")
lib3.XF = True

# =====================================================================
# APPENDIX
# =====================================================================
DIV[4] = divider(d, 4, "For the questions: how the score is built, the codes behind it, the ten-year check, the Monte Carlo inputs, the pilot length, the political game, the concept map and the sources.", "05 · APPENDIX")
s = raw_slide(d, count=False)
console(d, s, "APPENDIX · INDEX", True, "APPENDIX")
lib3.CUR["section"] = 4
text(s, 0.5, 0.84, 12.3, 0.3, [[R("05 APPENDIX", size=10, bold=True, color=EDM_L)]])
text(s, 0.5, 1.04, 12.3, 0.6, [[R("Appendix", size=20, bold=True, color=TXT)]])
ax_items = [("A1", "How the risk score is built"), ("A2", "The codes behind the empty visits"), ("A3", "Ten-year check of the score"), ("A4", "Monte Carlo inputs and sensitivity"),
            ("A5", "How long the pilot must run"), ("A6", "The political game: players, goals, moves"), ("A7", "Every course concept, and the design choice it changed"), ("A8", "Sources")]
AX_SQ = []
for i, (lab, name) in enumerate(ax_items):
    col = i // 4; row = i % 4
    x = 0.9 + col * 6.1; y = 2.05 + row * 1.05
    sq = rect(s, x, y, 0.72, 0.72, EDM)
    text(s, x, y, 0.72, 0.72, [{"runs": [R(lab, size=15, bold=True, color=WHITE)], "align": "c"}], anchor="middle", shape=sq, margin=(0, 0, 0, 0))
    tb = text(s, x + 0.95, y, 4.9, 0.72, [[R(name, size=13, bold=True, color=TXT)]], anchor="middle")
    AX_SQ.append((sq, tb, lab))
tabbar(s, 4)
footer(s, "")
notes(s, "Appendix index. Each square is a link to that appendix slide.")
APP = "APPENDIX"
s = new_slide(d, "APPENDIX A1 · HOW THE RISK SCORE IS BUILT", appendix=True, page_label="A1", foot=f"{OD}. Scripts in the project folder: final-presentation/assets/app311/figs.py (every figure in this deck), edmonton-311-analysis/scripts/hist.py (ten-year check), s1c_no_duplicates.py, a1-a4.py (Route Check). Duplicate requests left out.")
headline(s, "APPENDIX A1", ["The score is a shrunk ratio per code, computed from fields the City already publishes."])
panel(s, 0.3, 1.9, 6.2, 4.75, head="DEFINITIONS", head_color=CYAN)
text(s, 0.42, 2.22, 5.95, 4.4, [[R("Code = service area + category + description: 1,930 phone codes in 2025. The team's October deck counted 1,917 on its own definition; the slides keep that figure.", size=8.5, color=TXT)],
                                {"runs": [R("Empty field outcome = closure label in {Does Not Meet Bylaw Offence Standards, Assessed - No Action Required, Unable to Locate Animal, Location Not Found, Unable to Contact Complainant}." + f" The last two ({F['noproof25']:,} of {F['WV25']:,} in 2025) do not prove an officer attended.", size=8.5, color=TXT)], "before": 4},
                                {"runs": [R("Wasted desk outcome = {311 Redirecting to Other Business Area (a bounce), Non-City Service or Location, Reported on same day}." + f" Left out: the three Duplicate Request labels and File Already under Investigation ({F['dup25']:,} in 2025; {F['dup26']:,} in 2026 to Nov 6), because the City is already working on duplicates.", size=8.5, color=TXT)], "before": 4},
                                {"runs": [R("Left out: Parking \"Vehicle Gone Upon Arrival\" (4,886 in 2025) because it depends on dispatch speed (9.7% when closed within an hour vs 44.2% at 3-12 hours), not on intake.", size=8.5, color=TXT)], "before": 4},
                                {"runs": [R(f"Score = (empty + prior mean x 10) / (referrals + 10), separately for field and desk outcomes, then summed. Prior means 2025: field {F['prior_wv']:.1f}%, desk {F['prior_wd']:.1f}%.", size=8.5, color=TXT)], "before": 4},
                                {"runs": [R("Refresh: weekly, rolling 12 months. New codes: amber for 90 days, then scored. Three years of history did no better than one (AUC within 0.01).", size=8.5, color=TXT)], "before": 4},
                                {"runs": [R("Route Check lives inside Referral Check: bounces sit in the desk term, so the October design is a special case of this one.", size=8.5, color=TXT)], "before": 4}])
rows = [["CUT-OFF", "CODES", "2026 REFERRALS FLAGGED", "EMPTY VISITS CAUGHT", "DESK WASTE CAUGHT", "WASTE RATE IN FLAGGED SET"]]
for c_ in F["curve"]:
    if c_["th"] < 0.09:
        continue
    lab_ = f"> {c_['th']:.0%}" + (" (chosen)" if abs(c_["th"] - F["cut"]) < 1e-9 else " (red line)" if abs(c_["th"] - F["red"]) < 1e-9 else "")
    rows.append([lab_, f"{c_['codes']}", f"{c_['flag']:.1f}%", f"{c_['caught']:.1f}%", f"{c_['desk']:.1f}%", f"{c_['prec']:.1f}%"])
table(s, 6.65, 1.9, 6.38, 3.0, rows, colw=[1.1, 0.7, 1.25, 1.15, 1.05, 1.13], sizes=[8, 8, 8, 8, 8, 8], bold_first_col=True, row_h=0.33, fills={(3, None): AMBER_D})
text(s, 6.65, 5.0, 6.38, 1.6, [[R(f"Base rates, 2026 to Nov 6: {F['wv_rate26']:.1f}% of phone referrals ended in an empty field visit, {F['wd_rate26']:.1f}% in a wasted desk outcome, {ANY} in either. 2025: {F['WV25']:,} field, {F['WD25']:,} desk, of {F['N25']:,} referrals.", size=8.5, color=MUT)],
                               {"runs": [R("Precision reads: a red code at 30%+ means three in ten of its referrals end in some wasted outcome; the card says so in words.", size=8.5, color=MUT)], "before": 4},
                               {"runs": [R(f"The 15% line ({F15['codes']} codes, {F15['flag']:.0f}% of calls, {F15['caught']:.0f}% of empty visits, about {K(F15['mc']['net'])}) was considered. The team kept the 20% line it had set before duplicates were taken out, so the threshold did not move with the result.", size=8.5, color=MUT)], "before": 4}])

s = new_slide(d, "APPENDIX A2 · THE CODES BEHIND THE EMPTY VISITS", appendix=True, page_label="A2", foot=f"{OD}, phone referrals, Jan 1 to Nov 6, 2026. Flagged set = {NC} codes above 20% 2025 risk. Duplicate requests left out.")
headline(s, "APPENDIX A2", [f"Ten codes carry {F['top10_share']:.0f}% of the flagged empty visits, and three areas carry three in four."])
pic(s, "topcodes.png", 0.3, 1.9, 7.6)
rows = [["AREA", "FLAGGED REFERRALS", "EMPTY VISITS", "SHARE OF FLAGGED EMPTY VISITS"]] + [[a_, f"{n_:,}", f"{w_:,}", f"{sh_:.0f}%"] for a_, n_, w_, sh_ in F["areas"]]
table(s, 8.05, 1.9, 4.98, 3.2, rows, colw=[2.2, 0.95, 0.85, 0.98], sizes=[7.8, 8, 8, 8], bold_first_col=True, row_h=0.36)
text(s, 8.05, 5.2, 4.98, 1.4, [[R(f"Why the question changed: the flagged codes are complaints where an officer must judge a standard (untidy property, noise, parking on private property, business licences, zoning), not assets with an ambiguous owner. Municipal Enforcement, Peace Officers and Parking Enforcement are the three pilot areas ({F['pilot_share']:.0f}% of flagged empty visits). Roadway Maintenance (snow) is seasonal and depends on timing; it joins in phase two. Just under the line and still green: weed complaints (18.5% in 2025) and snow on walk (16.1%).", size=8.5, color=MUT)]])

s = new_slide(d, "APPENDIX A3 · TEN-YEAR CHECK OF THE SCORE", appendix=True, page_label="A3", foot="City of Edmonton yearly 311 datasets 2016-2022 (distinct Row ID) and the current dataset 2023-2026. The deck's score (field and desk ratios, duplicates left out) is trained on the prior year and tested on the year shown; flag = 20% risk. Script: edmonton-311-analysis/scripts/hist.py; table: empty_visit_backtest_2017_2026.csv. The bounce-only lookup from October scored AUC 0.82 to 0.93 over the same years (stability_backtest_2017_2026.csv).")
headline(s, "APPENDIX A3", [f"The same lookup has ranked the next year's empty visits in each of ten years (AUC {HMIN:.2f} to {HMAX:.2f}). 2026 is the weakest of the ten."])
rows = [["YEAR TESTED", "PHONE REFERRALS", "EMPTY VISITS", "RATE", "AUC, PRIOR YEAR'S SCORE", "CODES OVER 20%", "REFERRALS FLAGGED", "EMPTY VISITS CAUGHT"]]
for h_ in reversed(HIST):
    rows.append(["2026 (to Nov 6)" if h_["year"] == 2026 else str(h_["year"]), f"{h_['n']:,}", f"{h_['wv']:,}", f"{h_['wv_rate']:.1f}%", f"{h_['auc_deck_score_visits']:.2f}", f"{h_['codes']}", f"{h_['flag']:.1f}%", f"{h_['caught']:.0f}%"])
table(s, 0.3, 1.9, 8.4, 4.3, rows, colw=[1.3, 1.15, 0.95, 0.7, 1.3, 0.95, 1.05, 1.0], sizes=[8] * 8, bold_first_col=True, row_h=0.38)
panel(s, 8.85, 1.9, 4.18, 4.3, head="WHAT THE HISTORY ADDS", head_color=CYAN)
text(s, 8.97, 2.22, 3.95, 3.9, [[R(f"The ratio is not fitted to one odd year. Scored with the year before, it ranked empty visits with AUC {HMIN:.2f} to {HMAX:.2f} in every year from 2017 to 2026.", size=8.3, color=TXT)],
                                {"runs": [R(f"2026 is the weakest year. At the same 20% line the rule would have caught {HIST[-4]['caught']:.0f}%, {HIST[-3]['caught']:.0f}% and {HIST[-2]['caught']:.0f}% of empty visits in 2023, 2024 and 2025, against {HIST[-1]['caught']:.0f}% in 2026. The deck leads with 2026 because that test was specified before it was scored; the other nine years are a later check.", size=8.3, color=TXT)], "before": 6},
                                {"runs": [R("Before 2022 fewer codes crossed 20% and the rule flagged 4% to 7% of calls. Closure labels changed over the decade (Unable to Contact Complainant first appears in 2022), so the count tracks recording as much as conduct.", size=8.3, color=TXT)], "before": 6},
                                {"runs": [R("Phone volume fell by two thirds (1.83M phone tickets in 2016 to 0.67M in 2025) while phone codes grew from 1,701 to 1,930: less practice per code each year, which is the Kahneman and Klein condition eroding.", size=8.3, color=TXT)], "before": 6},
                                {"runs": [R("One year of history is enough: three years changed the AUC by less than 0.01.", size=8.3, color=TXT)], "before": 6}])

s = new_slide(d, "APPENDIX A4 · MONTE CARLO INPUTS AND SENSITIVITY", appendix=True, page_label="A4", foot="Triangular distributions (min / most likely / max), 50,000 draws, seed 20261110, independent draws. Volumes annualised from Jan 1 to Nov 6, 2026 (x 12 / 10.2). Six questions for reviewing an analysis: Session 2.")
headline(s, "APPENDIX A4", ["Every input is a range with a source or a flag; the one that moves the answer most is ours."])
rows = [["INPUT", "MIN / LIKELY / MAX", "SOURCE OR STATUS"],
        ["Empty field visits a year in flagged codes", f"{FVY} (counted)", "Open data, 2026 annualised"],
        ["Wasted desk closures a year in flagged codes", f"{F['FD']:,.0f} (counted)", "Open data, 2026 annualised; duplicates left out"],
        ["Flagged referrals a year", f"{FLY} (counted)", "Open data, 2026 annualised"],
        ["Cost of a field visit", "$22 / $84 / $280", "Team's Oct 26 stake model ranges; no City figure"],
        ["Desk time per closure", "5 / 10 / 20 min at $36.93 / $41.99 / $52.09 an hour", "CSU 52 collective agreement rates"],
        ["Share of flagged empty visits avoided by the check", "20% / 35% / 50%", f"ASSUMED; the pilot measures it; break-even {BE}"],
        ["Agent time per flagged call (20 s)", "$0.30 / $1.02 / $1.02", "Agent-only to average cost per contact ($16.29 per contact, $14.66M budget / 900K contacts)"],
        ["311 re-handling share on desk waste", "25% x $16.29", "Team judgment"]]
table(s, 0.3, 1.9, 7.6, 3.9, rows, colw=[2.6, 2.3, 2.7], sizes=[8, 8, 7.6], bold_first_col=True, row_h=0.42)
panel(s, 8.05, 1.9, 4.98, 3.9, head="SIX QUESTIONS FOR REVIEWING THIS ANALYSIS", head_color=CYAN)
text(s, 8.17, 2.22, 4.75, 3.55, [[R("Is this the decision we face? Yes: the pick on a phone referral, as in October, with its consequence widened.", size=8, color=TXT)],
                                 {"runs": [R("What is missing, overlapping, dependent? Vehicle Gone and duplicate requests are left out; bounces are counted once, in the desk row.", size=8, color=TXT)], "before": 4},
                                 {"runs": [R("Observed vs estimated? Volumes observed; costs are team ranges; the avoided share is assumed.", size=8, color=TXT)], "before": 4},
                                 {"runs": [R("Does it account for what averages hide? Rates are per code; the pilot is judged inside flagged codes.", size=8, color=TXT)], "before": 4},
                                 {"runs": [R(f"What flips it? Avoided share under {BE}, or a cost per empty visit under about ${F['be_visit']:.0f}. Neither is plausible; both are tested.", size=8, color=TXT)], "before": 4},
                                 {"runs": [R("What could we lose that the numbers leave out? Agent trust if the card is noise; area goodwill if the rate is published as a league table.", size=8, color=TXT)], "before": 4}])
text(s, 0.3, 5.9, 12.7, 0.7, [[R(f"Results: net mean {NET}; median {MED}; P10 {P10}; P90 {P90}; no draw below zero. Gross {GROSS}; check cost {COST}. Halve visit cost: {K(F['sens_halve'])}. Every check priced at $1.02: {K(F['sens_ask102'])}. Desk row left out: {K(F['sens_nodesk'])}. Red codes only (30% line): {K(F['mc_red']['net'])} (P10-P90 {K(F['mc_red']['p10'])}-{K(F['mc_red']['p90'])}). With duplicates counted, the earlier figure was $375K.", size=8.5, color=MUT)]])

s = new_slide(d, "APPENDIX A5 · HOW LONG THE PILOT MUST RUN", appendix=True, page_label="A5", foot=f"Two-proportion test, 80% power, 5% two-sided significance; baseline {BASE} of flagged referrals ending in an empty visit; about {PM} flagged phone referrals a month at the 20% cut-off, split 50/50 by team-week. Clustering by team-week adds a design effect: treat the figures as minimums.")
headline(s, "APPENDIX A5", ["Because the outcome is common (more than one in four flagged referrals), the pilot reads out in weeks, not quarters."])
rows = [["DROP TO DETECT", "FLAGGED REFERRALS PER ARM", "MONTHS OF PILOT (50/50 SPLIT)"],
        [f"20% relative ({BASE} to {G1})", f"{F['pw20']['n']:,.0f}", f"{F['pw20']['months']:.1f}"], [f"35% relative ({BASE} to {G2})", f"{F['pw35']['n']:,.0f}", f"{F['pw35']['months']:.1f}"],
        [f"Red codes only, 20% drop ({F['pw_red20']['p1']:.1f}% to {F['pw_red20']['p2']:.1f}%)", f"{F['pw_red20']['n']:,.0f}", f"{F['pw_red20']['months']:.1f}"], ["For comparison, Route Check (bounces, 7.0% base), 30% drop", "about 2,000", "3.6"]]
table(s, 0.3, 1.9, 7.6, 2.3, rows, colw=[3.6, 2.0, 2.0], sizes=[8.5, 8.5, 8.5], bold_first_col=True, row_h=0.4)
text(s, 0.3, 4.4, 7.6, 2.0, [[R("Design: half the teams see the card in a given week, chosen at random by team-week; the other half is the control. Both halves log the two answers only when the card is shown, so the control measures today's routine. The gate decision is set at day 120 (60 days of pilot) to allow for clustering and for the areas' closure lag (most field outcomes close within three weeks).", size=8.5, color=TXT)]])
panel(s, 8.05, 1.9, 4.98, 4.5, head="GATE ARITHMETIC", head_color=CYAN)
text(s, 8.17, 2.22, 4.75, 4.1, [[R(f"Baseline inside flagged codes: {BASE} empty field visits ({F['wv_flag']:,} of {F['n_flag']:,} in 2026 to Nov 6).", size=8.5, color=TXT)],
                                {"runs": [R(f"Gate: {G1} or lower in pilot teams while control stays near {F['p1']:.0f}%.", size=8.5, color=TXT)], "before": 5},
                                {"runs": [R(f"Expected: {G2} (35% avoided). Upside: {G3} (50%).", size=8.5, color=TXT)], "before": 5},
                                {"runs": [R(f"Dollar read-across at the gate: 20% avoided is about {K(F['net20'])} a year; 35% is {K(F['net35'])}; 50% is about {K(F['net50'])}.", size=8.5, color=TXT)], "before": 5},
                                {"runs": [R(f"Read-out: about {F['pw20']['n']:,.0f} flagged referrals in each arm is about one month of pilot calls at {PM} a month; add about three weeks for those visits to close.", size=8.5, color=TXT)], "before": 5}])

s = new_slide(d, "APPENDIX A6 · THE POLITICAL GAME · PLAYERS, GOALS, MOVES", appendix=True, page_label="A6", foot="Session 4: who are the players, what are their goals, what actions can they take, which maximise their benefit, what are they likely to do. CSD03148 (Sep 2, 2026); OCA 2023; CSU 52 collective agreement Art. 11.03 (technological change). 'At stake' cells are hypotheses to test in the day 1-30 interviews, not findings.")
headline(s, "APPENDIX A6", ["Who must say yes, in what order, and what each stands to lose."])
rows = [["PLAYER", "MEASURED ON TODAY", "GOAL", "MOVES OPEN", "WHAT IS AT STAKE (HYPOTHESIS)", "LIKELY MOVE, AND OUR ANSWER"],
        ["311 and Customer Access", "98.7% resolved on initial contact; 120-s answer", "Fewer repeat calls; a defensible scorecard", "Approve the pilot; publish or not", "A new line on its own scorecard that can go down", "Approves if the measure is paired and framed as capacity: it is"],
        ["Receiving areas (3 pilot)", "Closed within timelines (81%); audit compliance", "Officers on real work; control of outcome labels", "Write the questions; record reasons; sign or stall", "A published empty-visit rate read as an audit of officers", "Stall unless they own the questions and the queue: they do"],
        ["Agents and CSU 52", "Answer speed; Art. 11.03 on technological change", "No hidden ranking; no job loss; less rework", "Accept, bargain, grieve", "20 s per flagged call; a digest that could become a performance file", "Accept with coaching-only terms and a paused clock, agreed in writing first"],
        ["CRM owner / IT", "Uptime; 2030 replacement scope", "No scope creep on a dying system", "Add two fields, or export instead", "Effort on a platform being replaced", "Two fields, or exports in the shadow phase; every field a 2030 requirement"],
        ["Council and Auditor", "Closures, duplicates, compliance (July 2025 motion)", "Residents served; audit findings closed", "Ask for a routing measure", "A number that was never reported before", "Welcome a measure that is already in open data"],
        ["Residents", "Nothing", "One call, the right outcome, a reason", "Call again or give up", "Being talked out of a real problem", "The consent rule: a referral on request, always"]]
table(s, 0.3, 1.9, 12.73, 4.6, rows, colw=[1.7, 2.0, 2.0, 1.9, 2.5, 2.63], sizes=[8, 7.5, 7.5, 7.5, 7.5, 7.5], bold_first_col=True, row_h=0.62)

# concept map (two slides)
cm = [["SESSION · CONCEPT", "WHERE", "THE DESIGN CHOICE IT CHANGED"],
      ["S1 · AI as prediction machine; three kinds of system and their questions", "6", "A learned ratio plus an explicit rule, no generative step in phase one; the labelling question answered on the slide"],
      ["S1 · Four agent questions (access, change, stop, correct)", "8", "Read-only access, no caller text, a kill switch to green, a joint fix queue"],
      ["S1 · Three elements of agency; Organizations as Algorithms", "7, 8", "Authority stays with the agent; accountability with the area; data categories named as choices"],
      ["S1 · Northfield Credit Union", "8", "The interface and the metric shape the outcome: no pre-selected answer, no throughput target"],
      ["S1 · Assistant, analyst, coach; Mollick's rules; Zuboff vs Davenport", "16, 8", "AI used in three roles; the human keeps the knowledge by asking the question"],
      ["S2 · Problem tree, MECE, explanation as hypothesis", "4", "Branches by stage of one call; the agent is one leaf of nine"],
      ["S2 · Profit tree that reconciles; EV; mix effect; sensitivity", "5", "Capacity case with ranges; judge inside flagged codes; break-even stated"],
      ["S2 · Decision tree threshold; option value of waiting; staged options; premortem; six questions", "6, 10, 13, 15, A4", "2% floor, 20% cut-off; cost of waiting for 2030 stated; pilot as the small option; four failure stories"],
      ["S3 · System 1 / 2; attention needs one concrete question", "4, 6, 10", f"One question, one call in {ONEIN}, clock paused"],
      ["S3 · Kahneman and Klein: feedback for intuition", "10, 12", "Closure reason back to the agent within a day"],
      ["S3 · Ten biases; situation before tendency; heuristic vs bias; prompt framing; ethics test", "11, 16", "Answer-first card, paired measures, our own biases declared"]]
s = new_slide(d, "APPENDIX A7 · EVERY COURSE CONCEPT, AND THE DESIGN CHOICE IT CHANGED (1 OF 2)", appendix=True, page_label="A7a", foot="A concept earns its place only if it changed a design choice (Group Project brief: not a tour of the syllabus).")
headline(s, "APPENDIX A7", ["Sessions 1 to 3: each concept, where it appears, and what it changed."])
table(s, 0.3, 1.9, 12.73, 4.7, cm, colw=[5.2, 1.1, 6.43], sizes=[8, 8, 8], bold_first_col=True, row_h=0.4)
cm2 = [["SESSION · CONCEPT", "WHERE", "THE DESIGN CHOICE IT CHANGED"],
       ["S4 · The political game; where you stand; mirror imaging; sedimented assumptions", "10, A6", "Areas write the questions and co-own the queue; asks ordered 311, areas, union"],
       ["S4 · Strategic foresight (now to future, future to now); data limits; advisers who know your answer", "13, 9, 16", "Every field a 2030 requirement; what the data cannot show said first; test specified before scoring"],
       ["S5 · Garneau: disaggregate; what the data structurally cannot show", "5, 9, 12", "Per-code rates; the gaps listed; the 90-day set built to close them"],
       ["S6 · Data is built; inventory columns; a metric constructed slightly wrong; SBS reply-not-fix", "12, 14", "Required closure reason; label audits; re-contact paired with the primary measure"],
       ["S7 · Ostensive / performative / artifact; McGarry; Ironstone tacit work; dashboard-sim questions", "3, 7, 13", "The algorithm as a new artifact; co-design with senior agents; what the system makes invisible"],
       ["S8 · Direct AI, don't prompt it (Sloan and Glaser 2026)", "16", "Roles assigned to AI; loss-first and gain-first runs compared"],
       ["S9 · Proxy drift; values wither; measures before launch; Robodebt burden of proof", "8, 14", "Zero declined referrals; consent rule; guardrails never targets"],
       ["S10 · What to refuse to automate", "8", "Closing, declining, deciding an offence, hazard routing: never automated"],
       ["Brief · Five-part test; grain size; not already doing it; one concrete situation", "2, 3, 15", "Caller 7; the pick, not intake; checked against the City's July 2026 app AI and script search"],
       ["Consulting standard · takeaway titles; base case; within control vs needs others; risks beside forecast", "all, 13, 14, 15", "Every title a sentence; 90 days split by authority; upside and downside shown"]]
s = new_slide(d, "APPENDIX A7 · EVERY COURSE CONCEPT, AND THE DESIGN CHOICE IT CHANGED (2 OF 2)", appendix=True, page_label="A7b", foot="Sessions 8 to 10 entries follow the syllabus; the team will update them after those sessions (Nov 16, 23, 30).")
headline(s, "APPENDIX A7 (CONTINUED)", ["Sessions 4 to 10, the brief and the consulting standard."])
table(s, 0.3, 1.9, 12.73, 4.4, cm2, colw=[5.2, 1.1, 6.43], sizes=[8, 8, 8], bold_first_col=True, row_h=0.42)

s = new_slide(d, "APPENDIX A8 · SOURCES", appendix=True, page_label="A8", foot="Full references in the team's Oct 26 deck appendices and the Nov 1 research report (Appendix D).")
headline(s, "APPENDIX A8", ["Sources."])
src = ["City of Edmonton, 311 Requests open data (q7ua-agfg), accessed Nov 6-11, 2026, and yearly datasets 2016-2022. https://data.edmonton.ca/d/q7ua-agfg",
       "City of Edmonton, CSD03148 (Sep 2, 2026) and Attachments 1-2; Office of the City Auditor, City's Response to 311 Requests (Nov 2023); FCS02139 (Nov 30, 2023).",
       "City of Edmonton, Generative Artificial Intelligence Standard (Jul 25, 2024; s. 3.2 Jul 29, 2025); Administrative Standard on Privacy Impact Assessments (May 13, 2026); CSU 52 collective agreement 2024-2027, Art. 11.03.",
       "City of Edmonton operating budget: 311 and Customer Access $14.66M (2026). Toronto 311 cost per call $11-16 (Global News, Jan 19, 2024).",
       "Winnipeg 311 budget presentation (Dec 9, 2025) p. 6; Madrid SyRCI-IA (Interoperable Europe); Amsterdam Signalen (algoritmes.overheid.nl, gm0363); Dallas Auditor 311 SLA audit (Apr 2026); Denver Auditor (Aug 2025) and Council record 26-1373; Toronto, Simplifying the 311 Intake Experience (Apr 30, 2026).",
       "Glaser, V. L. (2026a) Analytic Trees; (2026b) The Psychological Perspective; Session 1 and 4 decks. Glaser, Sloan and Gehman (2024) Organizations as Algorithms, JMS 61(6). Glaser, Sloan and Knight (2025) FFI Practitioner. Sloan and Glaser (2026) Stop Prompting AI, MIT SMR.",
       "Kahneman and Klein (2009) Am. Psychologist 64(6); Klein (2007) HBR; Feldman and Pentland (2003) ASQ 48(1); Lindebaum, Glaser, Moser and Ashraf (2022) MIT SMR; Mollick (2024) Co-Intelligence; Tversky and Kahneman (1974, 1981); Moore and Healy (2008); Allison (2016).",
       "Green, B. (2022) The flaws of policies requiring human oversight of government algorithms; Bucinca et al. (2021) To trust or to think; Alon-Barkat and Busuioc (2023) Human-AI interactions in public sector decision making.",
       "Team materials: Strategic Analytics Initiative deck (Oct 26, 2026); Team research report (Nov 1, 2026); Final presentation plan (Nov 10, 2026); analysis scripts and tables in the project folder."]
text(s, 0.3, 1.9, 12.73, 4.7, [{"runs": [R(t, size=9.5, color=TXT)], "after": 6} for t in src])

out = "/tmp/claude-0/sc/build/v3.pptx"
# wire the app-style navigation now that every slide exists
for a_, b_, i in AG_ROWS:
    for sh in (a_, b_):
        sh.click_action.target_slide = DIV[i]
for sq, tb, lab in AX_SQ:
    tgt = lib3.APPX.get(lab) or lib3.APPX.get(lab + "a")
    sq.click_action.target_slide = tgt; tb.click_action.target_slide = tgt
print("nav links", link_nav(d, DIV, HOME))
d.save(out)
embed_fonts(out)
print("saved", out, d.page, len(d.prs.slides._sldIdLst))
