"""Referral Check final deck, painting / whiteboard-sketch variant.
Content mirrors final-presentation/content/referral-check-slide-text.txt (the futuristic deck); layout follows
the T5 whiteboard template (grid canvas, highlight titles, sticky notes, sketch boxes), painted.
Run: python3 build_painting.py  ->  final-presentation/Referral-Check-painting-deck.pptx"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plib import *

OUT = "/mnt/project-files/final-presentation/Referral-Check-painting-deck.pptx"
OD = "311 Requests open data (q7ua-agfg), 2023 to Nov 6, 2026, re-run on the team's six-part export"
d = Deck()

# =====================================================================
# 1 COVER
# =====================================================================
s = d.prs.slides.add_slide(d.blank); d.page += 1
pic(s, "canvas", 0, 0, 13.333, 7.5)
pic(s, "splat_yellow", 10.9, -0.35, 2.6, 2.6, rot=20)
pic(s, "splat_blue", 12.0, 6.15, 1.1, 1.1)
text(s, 0.7, 0.55, 9, 0.35, [[R("CITY OF EDMONTON  ·  311 AND CUSTOMER ACCESS  ·  EXECUTIVE BRIEFING", 11, True, BLUE, BODY_SB)]])
pic(s, "brush_yellow", 0.45, 1.25, 7.6, 1.45, rot=-1.2)
text(s, 0.7, 1.12, 8, 1.6, [[R("Referral Check", 60, True, INK, HAND)]], anchor="middle")
text(s, 0.75, 2.95, 7.4, 1.3, [{"runs": [R("One small decision, one simple algorithm: before a 311 referral goes out, a 20-second check on the one in ten that end with nothing for the City to do.", 18, False, INK, BODY)], "line": 1.05}])
sticky(s, 0.75, 4.45, 3.3, 1.55, "mint", -1.5, [
    {"runs": [R("$375K a year", 24, True, INK, HAND)], "after": 0},
    {"runs": [R("of field and desk capacity freed (mean; P10-P90 $171K-$622K). Capacity, not cash.", 10.5, False, INK)]}])
sticky(s, 4.35, 4.5, 3.3, 1.5, "pink", 1.2, [
    {"runs": [R("Agent keeps the call", 19, True, INK, HAND)], "after": 0},
    {"runs": [R("The algorithm never refuses a referral. The caller can always insist.", 10.5, False, INK)]}])
pic(s, "palette", 8.55, 2.15, 4.1, 2.95, rot=-8)
sticky(s, 8.9, 4.75, 3.6, 1.75, "yellow", 2.0, [
    {"runs": [R("Team 2", 17, True, INK, HAND)], "align": "c", "after": 0},
    {"runs": [R("Lauren Lonsberry · Nav Sekhon", 11, False, INK)], "align": "c"},
    {"runs": [R("Rick Auger · Curtis Middleton", 11, False, INK)], "align": "c"},
    {"runs": [R("Session 11 · Mon Dec 7, 2026 · 15 min + Q&A", 9, False, GREY)], "align": "c"}], anchor="middle")
text(s, 0.75, 6.3, 11.5, 0.5, [[R("Dollar figures: mean of 50,000 Monte Carlo draws on the team's cost ranges, trained on 2025 tickets and tested on 2026. The share of empty visits the check avoids (35%) is our assumption; the pilot measures it.", 8.5, False, GREY)]])
footer(s)
notes(s, "Cover. Open on the decision, not the agenda: one 311 agent, one code, 20 seconds, and whether a City officer drives across town. Referral Check is the algorithm that sits between the pick and the referral. Say up front: capacity, not cash; the 35% is ours to test.\n\nDesign note: painting variant of the Referral Check deck, built in the whiteboard-sketch style of the T5 template (grid canvas, highlight titles, sticky notes). Handwriting font is Segoe Print (as in the template); body text Segoe UI.")

# =====================================================================
# 2 CALLER 7
# =====================================================================
s = base(d, "The decision, as it happens",
         ["One pick on one call decides whether an officer drives out. ", ("12,583 times in 2025 the officer arrived and found nothing to act on.",)],
         src=OD + ". Caller 7 is illustrative; every code, count and closure label is real. Empty field outcome = Does Not Meet Bylaw Offence Standards, Assessed - No Action Required, Unable to Locate Animal, Location Not Found, Unable to Contact Complainant. 2026 to Nov 6: 179,139 referrals, 10,609 empty visits.")
def timeline(s, y, label, color, steps, lcolor):
    brush_label(s, 0.6, y - 0.05, label, 14, color, w=3.2)
    hand_line(s, 0.7, y + 0.78, 8.55, y + 0.78, INK, 2, arrow=True)
    n = len(steps); gap = 7.7 / n
    for i, (when, what, col) in enumerate(steps):
        cx = 0.75 + i * gap
        rect(s, cx + 0.05, y + 0.66, 0.24, 0.24, PAPER, RED, 1.75, shape=MSO_SHAPE.OVAL)
        text(s, cx - 0.05, y + 0.33, 1.4, 0.3, [[R(when, 11, True, BLUE, HAND)]])
        sticky(s, cx - 0.08, y + 0.98, gap - 0.1, 1.22, col, (-1.2 if i % 2 else 1.0), [[R(what, 8.5, False, INK)]], pad=0.1, shadow=False)
timeline(s, 1.8, "Today: the call as it runs", "pink", [
    ("Tue 10:12", 'Caller 7: "The yard next door is full of junk again."', "cream"),
    ("10:13", "Agent searches \"untidy\", picks Untidy Property, refers to Municipal Enforcement (120-s target).", "cream"),
    ("Thu", "A peace officer drives out. Ordinary household items; nothing meets the bylaw standard.", "cream"),
    ("Thu", "Closed: Does Not Meet Bylaw Offence Standards. 1,350 of 4,877 such referrals in 2026 (28%).", "pink"),
    ("Later", "Nothing goes back to the agent. The scorecard counts it resolved on first contact.", "pink")], RED)
timeline(s, 3.98, "With Referral Check: +20 s", "mint", [
    ("10:12", "Same call, same words.", "cream"),
    ("10:13", "Same code. Screen shows RED: 28% of these end with nothing to act on, plus two questions written by Municipal Enforcement.", "mint"),
    ("10:13", '"Visible from the street? More than household items?" "Just bins and a bike." Agent gives the bylaw info; caller can still insist.', "mint"),
    ("Thu", "No officer dispatched. Had it gone out, the closure reason would return to the agent within a day.", "cream"),
    ("Weekly", "The code's risk updates. Codes that stay red go to a fix queue 311 reviews with the area.", "cream")], GREEN)
stats = [("1 in 17", "phone referrals ends in an empty field visit (5.9%, 2026)", "yellow", -1.5),
         ("1 in 10", "ends in any wasted outcome, desk or field (10.1%)", "pink", 1.2),
         ("150 codes", "carry 65% of the empty visits, on 18% of calls", "mint", -0.8),
         ("$375K / yr", "capacity freed, mean; P10-P90 $171K-$622K", "yellow", 1.6)]
for i, (big, small, col, rot) in enumerate(stats):
    yy = 1.85 + i * 1.12
    sticky(s, 9.0, yy, 3.75, 0.98, col, rot, [{"runs": [R(big, 19, True, INK, HAND)], "after": 0}, {"runs": [R(small, 9, False, INK)]}], pad=0.12)
concepts(s, ["Brief · one concrete situation", "S7 · routine as performed", "S3 · feedback links action to result"])
notes(s, "The hook. Caller 4 told you about bounces in October; Caller 7 is the bigger cost. Illustrative dialogue; real code (Complaint Registered - Untidy Property), real counts. The screening questions are examples of what the area would write; the area owns them. Key line: the caller can always insist on a referral. The algorithm never says no.")

# =====================================================================
# 3 DECISION RESTATED
# =====================================================================
s = base(d, "The core decision, refined",
         ["Same 20-second pick as October. The refinement: ", ("the code chooses whether the work goes out, not only where.",)],
         src=OD + ". October figures from the team's Oct 26 Strategic Analytics Initiative deck. Five-part test and grain-size rule: SEM 620 Group Project brief; McGarry (ready-mix dispatcher) is the brief's benchmark. OCA 2023; CSD03148.")
sticky(s, 0.6, 1.95, 3.6, 1.95, "cream", -1.2, [
    {"runs": [R("OCTOBER · DIAGNOSIS", 9, True, GREY, BODY_SB)], "after": 2},
    {"runs": [R("Which service code does a new 311 phone ticket get?", 14, True, INK, HAND)], "after": 3},
    {"runs": [R("1 of 1,917 codes. 1,062 phone-referral bounces in 2025, about $100K a year; 98.9% land first time.", 9, False, INK)]}])
blue_arrow(s, 4.35, 2.75, 0.5, 0.32)
sticky(s, 5.0, 1.95, 3.9, 1.95, "yellow", 1.0, [
    {"runs": [R("DECEMBER · WHAT WE DESIGN FOR", 9, True, GREY, BODY_SB)], "after": 2},
    {"runs": [R("On each phone referral: route on the code as picked, or check first whether it should go out at all?", 13, True, INK, HAND)], "after": 3},
    {"runs": [R("1,062 bounced; 12,583 went out and found nothing.", 9, False, INK)]}])
red_circle(s, 4.85, 1.75, 4.25, 2.35, 2.25)
yy = 4.25
brush_label(s, 0.6, yy - 0.05, "Why the diagnosis moved", 14, "blue", w=3.3)
for i, (h, b) in enumerate([("1  The pick is right for routing", "98.9% of 2026 phone referrals did not bounce. Fixing bounces alone frees $7K-$17K a year."),
                            ("2  The bigger loss: referrals that should not go", "5.9% end in an empty field visit; 10.1% in some wasted outcome. A visit costs far more than a bounce."),
                            ("3  Grain size", "One agent, one code, 20 seconds, 190,000 times a year. McGarry's board was replaced; this agent is not.")]):
    text(s, 0.6, yy + 0.45 + i * 0.6, 8.4, 0.6, [{"runs": [R(h + ":  ", 10.5, True, INK, BODY_SB), R(b, 10, False, INK)]}])
table(s, 9.2, 1.95, [1.25, 2.4], [
    ["Five-part test", "Finding"],
    ["Who, how often", "A 311 agent, live, once per phone referral: 191,521 in 2025"],
    ["Inputs now", "Caller's words, code search, 900 area scripts, experience. Nothing shows how a code usually ends"],
    ["Options", "Resolve on the call, refer under one of 1,917 codes, or ask one more question first"],
    ["Bad instance x frequency", "Empty visit $22/$84/$280 x 12,583 a year; bounce $36 x 1,062"],
    ["Could an algorithm?", "Not the pick: only the agent hears the caller. A lookup can say how often this code ends with nothing"]],
    [0.35, 0.62, 0.8, 0.8, 0.8, 0.95], size=8.5)
concepts(s, ["Brief · five-part test", "Brief · grain size", "S7 · McGarry benchmark", "S2 · is this the decision we face?"])
notes(s, "Restate, then refine. The October decision stands; the diagnosis moved because the open data showed the pick is almost always right for routing, while one referral in ten ends with nothing for the City to do. Name the change openly: October's alternatives slide ranked complaint-intake screening sixth; the data moved it up.")

# =====================================================================
# 4 PROBLEM TREE
# =====================================================================
s = base(d, "Problem tree",
         ["Empty referrals start before the call, are picked during it, and ", ("after it no one is told, so no one learns.",)],
         src="Problem tree after Glaser, Analytic Trees pp. 5-10: root sentence with a result and a puzzle, branches MECE by stage of one call, evidence on every leaf. " + OD + "; OCA 2023 pp. 3, 16, 19, 20; CSD03148 (Sep 2, 2026) p. 2, Att. 2.")
wobble_box(s, 0.55, 2.85, 2.6, 2.0, INK, 2.25, seed=4)
text(s, 0.65, 2.9, 2.4, 1.9, [{"runs": [R("ROOT QUESTION", 8, True, GREY, BODY_SB)], "after": 2},
                               {"runs": [R("Why do one in ten phone referrals end with nothing for the City to do, and why does no one learn from them?", 11.5, True, INK, HAND)]}], anchor="middle")
sticky(s, 0.55, 5.05, 2.65, 1.1, "pink", -1.0, [{"runs": [R("Assumed, stated: ", 8.5, True, INK, BODY_SB), R("an empty visit is treated as avoidable at intake. Some are not: the condition changed, or the officer could not see it.", 8, False, INK)]}], pad=0.1)
branches = [("BEFORE THE CALL · the code set", "blue", [("Codes name an owner, not a standard", "Bylaw criteria live in 900 area scripts; the code carries none.", "VERIFIED"),
                                                   ("Ownership follows the asset", "One garbage can, four codes, four owners.", "VERIFIED"),
                                                   ("Risk is invisible", "No published rate per code. Untidy Property 28% empty; average 5.9%.", "VERIFIED")]),
            ("DURING THE CALL · the pick", "yellow", [("Words don't say if the standard is met", "\"Junk in the yard\" fits the code; whether an officer can act is a second question nobody asks.", "INFERRED"),
                                              ("Speed is what is measured", "120-second answer target; script AI framed around shorter calls.", "VERIFIED"),
                                              ("System 1 picks, System 2 defends", "A familiar phrase calls up a familiar code; the search confirms it.", "HYPOTHESIS")]),
            ("AFTER THE CALL · no learning", "pink", [("No count on the scorecard", "\"Resolved on Initial Contact\" 98.7% counts an empty visit as resolved.", "ABSENCE"),
                                             ("No word back", "No process we found returns the closure reason to the agent.", "ABSENCE"),
                                             ("Labels built differently by area", "Eight areas began recording bounces only in 2026.", "VERIFIED")])]
for bi, (bl, col, leaves) in enumerate(branches):
    by = 1.95 + bi * 1.45
    hand_line(s, 3.15, 3.85, 3.65, by + 0.55, INK, 1.75)
    hand_line(s, 5.55, by + 0.55, 6.0, by + 0.55, BLUE, 1.25)
    wobble_box(s, 3.65, by + 0.25, 1.9, 0.6, BLUE, 1.75, seed=10 + bi)
    text(s, 3.7, by + 0.27, 1.8, 0.56, [[R(bl, 9, True, BLUE, BODY_SB)]], anchor="middle")
    for li, (h, b, ev) in enumerate(leaves):
        lx = 6.0 + li * 2.3
        sticky(s, lx, by, 2.15, 1.25, col, (-1.0, 0.8, -0.5)[li], [
            {"runs": [R(h, 9, True, INK, BODY_SB)], "after": 1},
            {"runs": [R(b, 8, False, INK)], "after": 1},
            {"runs": [R(ev, 7, True, RED if ev in ("ABSENCE", "HYPOTHESIS") else GREEN, BODY_SB)]}], pad=0.09, shadow=False)
red_circle(s, 5.85, 4.75, 4.85, 1.5, 2.25)
concepts(s, ["S2 · problem tree", "S2 · MECE by stage", "S2 · explanation as hypothesis", "S3 · System 1 / 2", "S6 · metric built slightly wrong"])
notes(s, "The October problem tree, widened from bounces to every referral that ends with nothing to do. Root is a sentence with a result and a puzzle. Branches are MECE by stage of one call. Each leaf carries its evidence grade. Three real events each land in exactly one branch: garbage-can bounce (before), untidy yard with no offence (during), the 2026 bounce rise with 39% from new recording (after). The design answers one leaf per branch: show the risk (before), ask the standard (during), send the reason back (after).")

# =====================================================================
# 5 PROFIT TREE
# =====================================================================
s = base(d, "Profit tree",
         ["Checking the 150 riskiest codes frees ", ("about $375K a year of officer and desk time.",), " Capacity, not cash: no budget line moves."],
         src="Profit tree after Glaser, Analytic Trees Fig 2.1: each box is the sum or product of the boxes to its right. Triangular inputs: field visit $22/$84/$280 and desk time 5/10/20 min at $36.93-$52.09/h (team's Oct 26 ranges, CSU 52 rates); avoided share 20/35/50% (assumed); check 20 s at $0.30-$1.02. 50,000 draws, seed 20261110. 2026 volumes annualised x 12/10.2.")
def node(x, y, w, h, label, big, small, col, rot=0):
    sticky(s, x, y, w, h, col, rot, [{"runs": [R(label, 8, True, GREY, BODY_SB)], "after": 0},
                                     {"runs": [R(big, 17, True, INK, HAND)], "after": 0},
                                     {"runs": [R(small, 8, False, INK)]}], pad=0.1)
node(0.55, 3.05, 2.35, 1.5, "NET CAPACITY FREED / YR", "$375K", "mean; P10-P90 $171K-$622K; every draw above zero", "yellow", -1.0)
node(3.35, 1.95, 2.2, 1.3, "GROSS TIME FREED", "$405K", "field + desk work avoided", "mint", 0.8)
node(3.35, 4.45, 2.2, 1.3, "COST OF THE CHECK", "-$30K", "38,245 flagged calls x $0.78 (20 s)", "pink", -0.8)
node(6.0, 1.75, 2.15, 1.25, "FIELD VISITS AVOIDED", "$389K", "2,835 visits x $137", "mint", -0.6)
node(6.0, 3.2, 2.15, 1.15, "DESK WORK AVOIDED", "$16K", "1,195 closures x $12.60", "mint", 0.6)
node(8.6, 1.95, 1.35, 1.2, "VISITS REACHED", "8,100", "65% of empty visits", "cream", 0.8)
node(10.1, 1.95, 1.25, 1.2, "x AVOIDED", "35%", "assumed 20-50%", "pink", -0.8)
node(11.5, 1.95, 1.3, 1.2, "x COST / VISIT", "$137", "$22-$280 + desk", "cream", 0.5)
for (x1, y1, x2, y2) in [(2.9, 3.8, 3.35, 2.6), (2.9, 3.8, 3.35, 5.1), (5.55, 2.6, 6.0, 2.35), (5.55, 2.6, 6.0, 3.75), (8.15, 2.4, 8.6, 2.5)]:
    hand_line(s, x1, y1, x2, y2, INK, 1.5)
red_circle(s, 9.95, 1.8, 1.55, 1.5, 2.0)
text(s, 9.75, 3.3, 2.2, 0.35, [[R("the number the pilot tests", 10, True, RED, HAND)]])
sticky(s, 6.0, 4.6, 3.3, 1.5, "blue", -0.8, [{"runs": [R("Mix effect", 13, True, INK, HAND)], "after": 1},
    {"runs": [R("The City-wide rate (5.9%) hides codes at 28%, 43%, 62%. Judge the pilot inside flagged codes, never on the average.", 8.5, False, INK)]}], pad=0.12)
sticky(s, 9.55, 3.75, 3.25, 2.35, "yellow", 1.0, [{"runs": [R("Sensitivity", 13, True, INK, HAND)], "after": 1},
    {"runs": [R("Break-even if the check avoids only 2.6% of flagged empty visits. Halve the visit cost: $190K. Agent-time pricing only: $355K. Desk closures out: $360K.", 8.5, False, INK)], "after": 3},
    {"runs": [R("Left out: residents' days in the wrong queue (16,987 in 2025 on bounces alone) and delayed hazard tickets. October's $100K bounce stake sits inside the desk row.", 8, False, GREY)]}], pad=0.12)
concepts(s, ["S2 · profit tree reconciles", "S2 · EV is not a forecast", "S2 · mix effect", "S2 · sensitivity", "Deck std · units, source, assumptions"])
notes(s, "The stake as a profit tree: children multiply to the parent, the tree reconciles to $375K. Every input is a range with a source or a stated assumption; the one that matters most, the 35% avoided, is ours, and the pilot measures it. Say 'capacity, not cash' before anyone asks: officers freed for calls that need them; no budget line moves and no position is cut. Spread is wide because visit cost is wide ($22 to $280). Median $347K.")

# =====================================================================
# 6 THE ALGORITHM
# =====================================================================
s = base(d, "The algorithm, simple on purpose",
         ["One number per code: how often it ended with nothing last year. ", ("A rule turns it into three colours; the agent does the rest.",)],
         src="Risk score: last 12 months' empty outcomes per referral for the code, shrunk toward the City average with a prior of about 10 tickets (empirical Bayes), refreshed weekly. Trained on 2025, tested on Jan-Nov 2026. Shares of 2026 phone referrals: green 81.9%, amber 6.6%, red 11.5%. Threshold: $1.02 / (35% x $137) = 2.2%. " + OD + ".")
wobble_box(s, 0.6, 1.95, 6.2, 1.85, BLUE, 2.0, seed=21)
text(s, 0.75, 2.0, 5.9, 0.3, [[R("THE WHOLE MODEL, IN ONE SENTENCE", 8.5, True, BLUE, BODY_SB)]])
text(s, 0.75, 2.28, 5.9, 0.55, [[R("risk(code) = (empty outcomes + 10 x 5.9%) / (referrals + 10)", 15, True, INK, HAND)]], anchor="middle")
text(s, 0.75, 2.85, 5.9, 0.9, [[R("Last 12 months of closed phone referrals, refreshed weekly. \"This code ended with nothing 1,350 of 4,877 times last year\" is the whole explanation an agent needs. Rare codes are pulled toward the average; new codes sit amber for 90 days.", 9, False, INK)]])
table(s, 0.6, 4.0, [1.45, 1.75, 3.0], [
    ["Kind of system (S1)", "In Referral Check", "The question it raises, and our answer"],
    ["Learns a pattern", "The ratio per code, from past closures", "How were examples labelled? By the area's closure reason. Build a required reason field; audit a sample."],
    ["Applies a rule", "20% / 30% cut-offs; amber for new codes", "Who set the conditions? 311 with the pilot areas and CSU 52; reviewed at the gate."],
    ["Generates content", "Nothing in phase one", "Faithful to source? Not triggered until phase two, under the City's Generative AI Standard."]],
    [0.32, 0.62, 0.55, 0.62], size=8.3)
tiers = [("GREEN", "risk under 20%", "82% of referrals", "Nothing. Route as today.", "ROUTE", "mint", GREEN),
         ("AMBER", "risk 20% to 30%", "7%", "The code's rate and the area's screening questions; one click to confirm.", "CONFIRM OR SWITCH", "yellow", "B8860B"),
         ("RED", "risk over 30%", "11% of referrals, 65% of empty visits", "Rate, two screening questions, and alternatives (information, self-serve, report again).", "ASK, THEN DECIDE", "pink", RED)]
for i, (nm, rule, share, sees, does, col, ink) in enumerate(tiers):
    x = 7.15 + i * 1.95
    sticky(s, x, 1.95, 1.8, 2.6, col, (-1.2, 0.6, 1.4)[i], [
        {"runs": [R(nm, 16, True, ink, HAND)], "after": 0},
        {"runs": [R(rule, 8.5, True, INK, BODY_SB)], "after": 0},
        {"runs": [R(share, 8, False, GREY)], "after": 4},
        {"runs": [R(sees, 8.5, False, INK)], "after": 4},
        {"runs": [R(does, 8, True, BLUE, BODY_SB)]}], pad=0.11)
sticky(s, 7.15, 4.75, 5.65, 1.4, "cream", -0.5, [
    {"runs": [R("Why 20%, when the decision tree says 2%?", 12, True, INK, HAND)], "after": 1},
    {"runs": [R("Rolled back, a 20-second check pays above about 2% risk: most referrals. But a prompt on every second call becomes wallpaper. The cut-off is set by the agent's attention, not the arithmetic: flag one call in five and still reach 65% of empty visits.", 8.5, False, INK)]}], pad=0.12)
concepts(s, ["S1 · three kinds of system", "S1 · how examples were labelled", "S2 · decision-tree threshold", "S3 · attention needs one question"])
notes(s, "The algorithm is deliberately the simplest thing that works: a shrunk ratio per code, a rule, three colours. Session 1's three kinds of system each raise a question; answer all three on the slide. The rational threshold (2%) and the psychological constraint (attention) disagree; the design sides with attention and says so. A logistic model with more features did worse out of time (AUC 0.69 vs 0.82 on bounces).")

# =====================================================================
# 7 THE ROUTINE (swim lane)
# =====================================================================
s = base(d, "The routine: who does what",
         ["Four actors, one new artifact. ", ("The algorithm scores; the agent asks; the area closes with a reason; the reason comes back.",)],
         src="Routine decomposed after Feldman and Pentland (2003): ostensive, performative, artifacts. Ironstone Ready-Mix (Session 7): the scheduling system removed the afternoon readiness calls nobody had written down. OCA 2023 p. 19: agents are expected to ask clarifying questions.")
cols = ["The pick (20 s)", "The check (+20 s)", "After (days)", "Learn (weekly)"]
lanes = [("Resident", "pink", ['"The yard next door is full of junk." Gives the address.', "Answers two questions. Can always insist on a referral.", "Hears the outcome with the reason (phase 2).", ""]),
         ("311 agent", "yellow", ["Searches the code list under a 120-s target; picks Untidy Property.", "Reads the tier; asks the area's two questions; refers with answers attached, or informs. Final call stays here.", "Sees the closure reason in a daily digest to the team lead. Coaching only.", ""]),
         ("Referral Check", "blue", ["Looks up the code's risk and tier. In: code, risk table, screening set.", "Out: tier, rate, questions, alternatives. Logs tier, answers, choice.", "", "Recomputes every ratio; drift alerts; codes that stay red go to the fix queue."]),
         ("Receiving area", "mint", ["", "Receives the ticket with the two answers attached.", "Officer attends; closes with a required reason (one of five).", "Owns the questions and the fix queue with 311: retire, merge, reword."])]
lx, cw, lh = 2.05, 2.7, 0.79
for ci, c in enumerate(cols):
    brush_label(s, lx + ci * cw + 0.1, 1.85, c, 12, ("yellow", "pink", "mint", "blue")[ci], w=2.2)
for li, (who, col, cells) in enumerate(lanes):
    y = 2.3 + li * lh
    wobble_box(s, 0.55, y + 0.05, 1.4, lh - 0.12, INK, 1.5, seed=30 + li)
    text(s, 0.6, y + 0.05, 1.3, lh - 0.12, [{"runs": [R(who, 12, True, INK, HAND)], "align": "c"}], anchor="middle")
    for ci, c in enumerate(cells):
        if c:
            sticky(s, lx + ci * cw, y + 0.04, cw - 0.15, lh - 0.1, col, (0.6 if (ci + li) % 2 else -0.6), [[R(c, 8, False, INK)]], pad=0.07, shadow=False)
y0 = 5.95 - 0.35
for i, (h, b, col) in enumerate([("Ostensive: the steps as understood", "Find the right code; resolve or refer. Unchanged. We add one step inside it: on risky codes, ask the standard first.", "cream"),
                                 ("Performative: as carried out", "Search, pick the first fit, refer. Judgment moves: \"can an officer act?\" moves from the curb on Thursday to the line on Tuesday.", "cream"),
                                 ("Artifacts: old and new", "Old: code list, 900 scripts, status field. New: tier on screen, screening card, required closure reason, fix queue. Ironstone: first ask senior agents what they already ask.", "cream")]):
    pass
for i, (h, b) in enumerate([("Ostensive", "Find the right code; resolve or refer. Unchanged, plus one step on risky codes: ask the standard first."),
                            ("Performative", "\"Can an officer act?\" moves from the curb on Thursday to the line on Tuesday. The pick itself does not move."),
                            ("Artifacts", "New: tier on screen, screening card, required closure reason, fix queue. Ironstone: ask senior agents what they already ask.")]):
    text(s, 0.55 + i * 4.15, 5.55, 4.0, 0.72, [{"runs": [R(h + ": ", 9, True, BLUE, BODY_SB), R(b, 8.5, False, INK)]}])
concepts(s, ["S7 · ostensive / performative / artifact", "S7 · Ironstone tacit work", "S7 · where judgment moves", "Brief · in, out, who acts", "S1 · agency in the assemblage"])
notes(s, "The brief's four questions in one picture: what goes in (the code, the risk table, the area's screening set), what comes out (tier, rate, questions, alternatives, a log), who acts (agent decides, area closes with a reason, 311 and the area run the fix queue), and the loop back. Session 7 decomposition at the bottom: the ostensive routine barely changes; the performative one gains one question; the artifacts are where the algorithm lives. Ironstone: co-design with senior agents so we do not pave over what they already ask.")

# =====================================================================
# 8 AUTOMATE VS PERSON + WHEN WRONG
# =====================================================================
s = base(d, "Automate vs leave to a person",
         ["Automate the counting and the reminder. ", ("Never the decision to refer, close or decline:",), " those stay with people who can be asked why."],
         src="Three elements of agency and the four agent questions: Session 1; Northfield Credit Union case. Robodebt and proxy drift: Session 9, Lindebaum et al. (2022). Refusals: Session 10. Green (2022): oversight people cannot perform is not oversight; Bucinca et al. (2021): answer-first designs cut over-reliance.")
table(s, 0.55, 1.9, [1.75, 1.55, 1.65, 2.25], [
    ["Step", "Automated?", "A person", "Why"],
    ["Score and tier every pick", "Yes: one ratio, one rule, weekly", "Sets thresholds; reviews at gate", "Counting is what machines do well; the cut-off is a value choice"],
    ["Show the screening questions", "Yes: on amber and red", "Area writes; agent asks", "Only the agent hears the caller (Northfield)"],
    ["Refer, inform or switch code", "No", "The agent, every time; override logged", "Authority stays where the information is"],
    ["Close a ticket / declare no offence", "No, ever", "The receiving area", "Accountability sits with whoever must explain it"],
    ["Retire, merge, reword a code", "Queue yes, decision no", "311 knowledge team + area", "Political, not statistical"],
    ["Coach an agent", "No: digest is material", "Team lead", "Feedback works from a person the agent trusts; agreed with CSU 52"]],
    [0.33, 0.48, 0.42, 0.45, 0.45, 0.42, 0.5], size=8.3)
sticky(s, 0.55, 5.1, 7.2, 0.95, "blue", -0.4, [{"runs": [R("Four agent questions:  ", 9, True, INK, BODY_SB),
    R("Access: code and closure tables; no caller notes, no names. Change: nothing; it displays and logs. Stop: falls back to green if override rate passes 80%, recording drops, or it is down. Correct: weekly fix queue; agents can flag a wrong tier.", 8.3, False, INK)]}], pad=0.1)
brush_label(s, 8.1, 1.85, "When it is wrong", 15, "pink", w=2.6)
wrong = [("False alarm", "Red flag on a real offence: 20-40 s and one click. 80% overridden = noise, goes green.", "yellow"),
         ("Missed one", "Green code sends an officer to nothing: same as today, but the reason returns within a day.", "mint"),
         ("Drift", "An area changes how it closes tickets. Judge the pilot only against its control.", "yellow"),
         ("Rubber stamp", "Acceptance over 95%: audit a sample. Questions, never a pre-selected outcome.", "mint"),
         ("Turned into a gate", "Robodebt: a proxy becomes a reason to refuse service. Rule: never declines; caller can insist; \"declined without consent\" must read zero.", "pink")]
for i, (h, b, col) in enumerate(wrong):
    cx = 8.1 + (i % 2) * 2.4 if i < 4 else 8.1
    cy = 2.4 + (i // 2) * 1.25
    w = 2.3 if i < 4 else 4.7
    sticky(s, cx, cy, w, 1.13, col, (-1.2, 1.0, 0.8, -1.0, -0.5)[i], [{"runs": [R(h, 11, True, INK, HAND)], "after": 0}, {"runs": [R(b, 7.8, False, INK)]}], pad=0.09)
concepts(s, ["S1 · three elements of agency", "S1 · four agent questions", "S1 · Northfield", "S10 · refuse to automate", "S9 · Robodebt"])
notes(s, "Be explicit, as the brief asks. Influence: the card changes what gets asked. Decision authority: agent recommends and executes the referral; area approves the outcome; 311 and the area revise codes. Accountability: whoever must explain the result keeps the decision. Zuboff's worry is answered by keeping the ask with the agent and returning the outcome to them; Davenport's promise is kept to the counting. Robodebt is the Q&A trap: say the refusal rule before anyone asks.")

# =====================================================================
# 9 EVIDENCE
# =====================================================================
s = base(d, "Evidence: 2025 predicts 2026",
         ["Last year's ratio picks this year's empty visits: ", ("18% of calls, 65% of the waste.",), " The same score has ranked bounces every year since 2016."],
         src=OD + ". Score trained on 2025 closures only, tested on 179,139 phone referrals Jan 1-Nov 6, 2026 (10,609 empty visits). Bounce AUC by year from yearly datasets 2016-2022 and current dataset 2023-2026. Peers: Winnipeg 311 budget presentation (Dec 9, 2025) p. 6; Madrid SyRCI-IA.")
# coverage chart (hand-drawn)
cx0, cy0, cw0, ch0 = 0.9, 2.15, 5.6, 3.3
wobble_box(s, 0.6, 1.95, 6.3, 4.15, INK, 1.5, seed=41)
text(s, 0.75, 2.0, 6.0, 0.3, [[R("SHARE OF 2026 EMPTY VISITS CAUGHT vs SHARE OF CALLS FLAGGED", 8, True, GREY, BODY_SB)]])
pts = [(0, 0), (4.1, 18.9), (9.0, 43.0), (11.5, 47.4), (13.6, 53.6), (18.1, 64.9), (26.5, 76.1), (35.9, 83.5), (100, 100)]
ox, oy, sw, sh = 1.15, 5.55, 5.4, 3.1   # origin and scale (x 0-50%, y 0-100%)
hand_line(s, ox, oy, ox + sw, oy, INK, 1.5); hand_line(s, ox, oy, ox, oy - sh, INK, 1.5)
def P(px, py): return ox + min(px, 50) / 50 * sw, oy - py / 100 * sh
prev = None
for (px, py) in pts:
    if px > 50: px, py = 50, 90
    q = P(px, py)
    if prev: hand_line(s, prev[0], prev[1], q[0], q[1], BLUE, 3.0)
    prev = q
hand_line(s, *P(0, 0), *P(50, 50), GREY, 1.0, dash=True)
text(s, P(38, 42)[0], P(38, 42)[1], 1.6, 0.3, [[R("random flags", 8, False, GREY, BODY)]])
fx, fy = P(18.1, 64.9)
red_circle(s, fx - 0.22, fy - 0.22, 0.44, 0.44, 2.25)
text(s, fx + 0.3, fy + 0.15, 2.6, 0.6, [[R("20% cut-off: 18% of calls, 65% of empty visits", 10, True, RED, HAND)]])
for v in (0, 10, 20, 30, 40, 50):
    text(s, P(v, 0)[0] - 0.25, oy + 0.03, 0.5, 0.22, [{"runs": [R(f"{v}%", 7.5, False, GREY)], "align": "c"}])
for v in (0, 50, 100):
    text(s, ox - 0.5, P(0, v)[1] - 0.11, 0.45, 0.22, [{"runs": [R(f"{v}%", 7.5, False, GREY)], "align": "r"}])
text(s, ox, oy + 0.22, sw, 0.25, [{"runs": [R("calls flagged", 8, False, GREY)], "align": "c"}])
stats = [("0.82", "AUC on 2026 bounces, lookup; a logistic model with more features: 0.69", "yellow"),
         ("30%", "of flagged referrals end in waste, vs 10% of all referrals", "mint"),
         ("r 0.74", "code rate 2024 vs 2025 (402 codes with 30+ referrals)", "pink"),
         ("8%", "of 2026 bounces on codes new since 2025: hence amber for new codes", "yellow")]
for i, (b, t, col) in enumerate(stats):
    sticky(s, 7.2 + (i % 2) * 2.85, 1.95 + (i // 2) * 1.3, 2.7, 1.15, col, (-1.0, 1.0, 0.7, -0.8)[i], [{"runs": [R(b, 20, True, INK, HAND)], "after": 0}, {"runs": [R(t, 8.3, False, INK)]}], pad=0.1)
sticky(s, 7.2, 4.65, 5.55, 1.5, "cream", -0.4, [{"runs": [R("What this data cannot show, said before anyone asks", 11, True, INK, HAND)], "after": 1},
    {"runs": [R("Why the officer found nothing. Whether the first code differed from the final one (no re-route link). Which agent picked. Quiet misroutes. Peers measure what we cannot: Winnipeg publishes returns due to agent error (1.62%, 2024); Madrid's units validated 79% of 38,221 AI routings. The 90-day data set closes these gaps.", 8.2, False, INK)]}], pad=0.12)
concepts(s, ["S3 · overfitting: test on unseen cases", "S5 · disaggregate", "S4 · data limits", "S4 · advisers who know your answer"])
notes(s, "Evidence slide. The test was specified before the 2026 data was scored: trained on 2025, scored on 2026, so the overfitting trap is addressed. The coverage curve is the design choice made visible: pick any point; we picked 18% of calls for 65% of empty visits. Curve points (cut-off: calls flagged, empty visits caught): 50%: 4.1%, 18.9%; 40%: 9.0%, 43.0%; 30%: 11.5%, 47.4%; 25%: 13.6%, 53.6%; 20%: 18.1%, 64.9%; 15%: 26.5%, 76.1%; 10%: 35.9%, 83.5%. Ten years of the bounce score show the ratio is not fitted to one odd year; 2026 is weakest because eight areas started recording.")

# =====================================================================
# 10 THREE LENSES
# =====================================================================
s = base(d, "The lens: three portraits",
         ["Each lens changes one design choice: ", ("rational sets the floor, psychological sets the cut-off, political sets the order of asking.",)],
         src="Rational: Glaser, Analytic Trees (threshold p. 20; option value of waiting; loss beside the average p. 21). Psychological: Glaser, The Psychological Perspective (3.2, 3.3, 3.6); Kahneman and Klein (2009). Political: Session 4 (the political game; Allison; mirror imaging; sedimented assumptions; strategic foresight). CSD03148 p. 2; OCA 2023 p. 20.")
lenses = [("lauren", "Logical Lauren · rational", "\"The arithmetic says check almost everything. I set the floor, not the ceiling.\"", "yellow",
           [("Expected value", "A 20-s check pays above ~2% risk; $375K a year across 150 codes. An average, not a forecast."),
            ("Loss beside the average", "P10 $171K; no draw negative. The loss is 20 s on 38,000 calls and a prompt agents stop reading."),
            ("Option value of waiting", "Waiting for the 2030 CRM costs ~$1.1M of capacity and arrives with no labelled data."),
            ("Staged options", "The pilot is the small option; phases two and three only if the gate passes.")]),
          ("nav", "Neuro Nav · psychological", "\"Agents don't need to be more careful. They need one concrete question and to hear how it turned out.\"", "pink",
           [("Attention", "One question on one call in five; the clock pauses on flagged calls."),
            ("Feedback for intuition", "Kahneman and Klein: no feedback, no expertise. The digest returns the reason in a day."),
            ("Anchoring", "Rate and questions, never a pre-selected answer."),
            ("Gain, loss, reference point", "Reference point is speed. Name the loss (20 s); frame the gain (no officer sent to nothing).")]),
          ("rick", "Ruling Rick · political", "\"The ratio is harmless. Publishing it is political: it shows the areas' closures for the first time.\"", "mint",
           [("The players", "311 owns the pick; areas own the labels; CSU 52 represents agents; Council never asked about misroutes."),
            ("Where you stand", "An area may read an empty-visit rate as an audit of its officers. So the area writes the questions."),
            ("Sedimented assumption", "\"98.7% resolved on initial contact\" repeated since 2023. Nobody is lying; nobody is counting."),
            ("Strategic foresight", "The 2030 CRM inherits whatever labels exist; every pilot field is a requirement for it.")])]
for i, (who, nm, quote, col, pts_) in enumerate(lenses):
    x = 0.55 + i * 4.2
    portrait(s, who, x, 1.85, 1.15)
    text(s, x + 1.25, 1.88, 2.85, 0.35, [[R(nm, 12, True, INK, HAND)]])
    text(s, x + 1.25, 2.22, 2.85, 0.8, [[R(quote, 9, False, BLUE, BODY, True)]])
    paras = []
    for h, b in pts_:
        paras.append({"runs": [R(h + ": ", 10, True, INK, BODY_SB), R(b, 9.8, False, INK)], "after": 6})
    sticky(s, x, 3.1, 3.95, 3.0, col, (-0.8, 0.7, -0.6)[i], paras, pad=0.13)
concepts(s, ["S2 · EV, option value, loss", "S3 · attention, feedback, anchoring, framing", "S4 · players, where you sit, foresight"])
notes(s, "The three characters from October assess the proposal. Rational: EV, loss beside the average, option value of waiting, staged options. Psychological: attention needs a concrete question (3.2), feedback for intuition (3.3, Kahneman and Klein), anchoring, gain/loss framing (3.6), and the ethics test: we use what we know about agents to help them see the 20 seconds, never to hide it. Political: the game's five questions (full table in Appendix A6), where you stand, mirror imaging, sedimentation, foresight both directions. Each lens changes a design choice; say which.")

# =====================================================================
# 11 BIASES
# =====================================================================
s = base(d, "Biases: situation first",
         ["Ten biases from the course, each with the situation first and the design choice that answers it. ", ("Four of them are ours.",)],
         src="Biases as taught in Session 3 (Glaser, The Psychological Perspective; Tversky and Kahneman 1974, 1981; Nickerson 1998; Moore and Healy 2008; Kahneman and Tversky 1979; Arkes and Blumer 1985; Fazio et al. 2015; MacGarvie and McElheran 2018). Method rule: what happened, then the tendency, then what is neglected.")
table(s, 0.55, 1.85, [1.3, 2.6, 2.75], [
    ["Bias", "What happens", "What the design does"],
    ["Availability", "A memorable empty visit (or real offence) stands in for how often each happens", "The ratio counts every case; the card shows the rate, not an anecdote"],
    ["Confirmation", "System 2 searches the list to confirm the code System 1 offered", "Questions ask the other way round: what would make this not an offence?"],
    ["Anchoring", "A ranked suggestion on screen becomes the answer", "No pre-selected outcome; the agent records answers and decides"],
    ["Overconfidence", "\"99% land correctly\" reads as \"the pick is fine\"", "Report precision per code (28%, 43%, 62%), never a City average"],
    ["Framing", "\"98.7% resolved\" vs \"1 in 10 referrals ends with nothing\"", "The scorecard carries both lines"],
    ["Loss aversion", "Agents' reference point is the clock; areas' is control of closures", "Pause the clock on flagged calls; areas co-own the queue"],
    ["Sunk cost", "\"Wait for the 2030 CRM\"; \"we already built script search\"", "A lookup and a card; every field doubles as a CRM requirement"],
    ["Jumping to conclusions", "\"Agents are careless\" is a coherent story", "The tree names nine causes; the agent is one leaf"],
    ["Illusory truth", "\"Efficiently routed\" repeated in reports since 2023", "Put a measured rate beside the repeated phrase"],
    ["Overfitting", "A model that explains 2025 perfectly", "Trained 2025, tested 2026; one ratio (AUC 0.82 vs 0.69)"]],
    [0.3] + [0.395] * 10, size=7.9)
ours = [("Confirmation", "We went looking for a bigger dollar case after bounces came in at $7K-$17K. Test: score specified before scoring 2026. It held.", "yellow"),
        ("Overconfidence", "The 35% avoided share has no source: a team judgment, range 20-50%. The case holds down to 2.6%.", "mint"),
        ("Prompt framing", "Asking AI for \"the most savings\" produces savings. We asked the loss side separately: who pays, who could be refused.", "pink"),
        ("Heuristic or bias?", "\"Untidy yard = untidy code\" is a useful shortcut. It becomes a bias only with no feedback. We change the condition, not the person.", "blue")]
brush_label(s, 7.35, 1.82, "Our own, declared", 14, "yellow", w=2.8)
for i, (h, b, col) in enumerate(ours):
    sticky(s, 7.35 + (i % 2) * 2.8, 2.35 + (i // 2) * 1.9, 2.65, 1.75, col, (-1.5, 1.2, 1.0, -1.3)[i], [{"runs": [R(h, 13, True, INK, HAND)], "after": 2}, {"runs": [R(b, 9.5, False, INK)]}], pad=0.13)
concepts(s, ["S3 · ten biases", "S3 · situation, tendency, neglected", "S3 · heuristic vs bias", "S3 · prompt framing"])
notes(s, "Each row follows the method rule: the situation, then the tendency, then what is neglected, then the design answer. Keep the agents out of the dock: the biases live in the system (no feedback, a speed clock, a label built by the area). Own ours in the room before the examiner finds them: confirmation (we wanted a dollar case), overconfidence (35%), framing of our own prompts.")

# =====================================================================
# 12 DATA + 90-DAY DATA SET
# =====================================================================
s = base(d, "Data: constructed, then leveraged",
         ["The ratio needs fields the City already has. ", ("Learning needs a data set that does not exist yet: we build it in the first 90 days.",)],
         src="Inventory columns after the Session 6 exercise (Scandinavian Building Services, Ivey W35309). SBS lesson: the 10-1-24 figure measured the reply, not the fix. Session 1: how the examples were labelled. Volumes: about 3,200 flagged phone referrals a month at the 20% cut-off (2026 pace).")
table(s, 0.55, 1.85, [1.85, 1.25, 1.45, 1.85], [
    ["Data", "Have it?", "Used for", "Who must change"],
    ["Code, area, channel, referral type, closure label, dates", "Yes, public", "The ratio, tiers, backtest", "No one"],
    ["Ticket address, agent ID, handle time", "In the CRM (inferred)", "Digest, handle-time guardrail", "CRM owner: data agreement"],
    ["Closure reason, consistent across areas", "Partly (8 areas from 2026)", "The label every ratio learns from", "Areas: required reason"],
    ["Screening answers on flagged calls", "No", "90-day set; answer-level risk", "Agents: two fields; CSU 52"],
    ["Agent's choice after the card", "No", "Override rate, consent guardrail", "Comes free with the card"],
    ["Link from referral to final code (re-route)", "No; can't be rebuilt", "Was the picked code right?", "Area clerks: one field"],
    ["Accuracy of codes on resolved calls (473,564)", "No", "Replaces the stake's biggest unknown", "311 QA: ~200 calls/month"]],
    [0.32, 0.42, 0.42, 0.42, 0.42, 0.38, 0.42, 0.42], size=8)
sticky(s, 0.55, 5.25, 6.4, 0.92, "pink", -0.4, [{"runs": [R("Data is built. ", 9, True, INK, BODY_SB), R("The label is the area's verdict, written under its own incentives. An empty-visit rate alone rewards closing \"no action\" less often, so every rate is paired with resident re-contact within 30 days and labels are audited by sample.", 8.2, False, INK)]}], pad=0.1)
# 90-day data set panel
pic(s, "wash_cream", 7.2, 1.8, 5.65, 4.45)
brush_label(s, 7.45, 1.92, "The 90-day data set", 16, "yellow", w=3.2)
text(s, 7.45, 2.5, 5.2, 0.85, [{"runs": [R("Built so the algorithm can learn to code correctly. One row per flagged phone referral, from day 31: ", 8.8, True, INK, BODY_SB),
    R("code picked · tier and rate shown · two answers · agent's choice · caller insisted · days to closure · closure reason · reassigned to (final code) · re-contact within 30 days", 8.5, False, INK)]}])
sticky(s, 7.45, 3.45, 2.5, 1.45, "yellow", -1.2, [{"runs": [R("Size by day 90", 11, True, INK, HAND)], "after": 0},
    {"runs": [R("~6,400 flagged referrals logged; ~4,800 with a closure reason; ~1,000 empty visits labelled.", 8.2, False, INK)]}], pad=0.1)
sticky(s, 10.15, 3.45, 2.5, 1.45, "mint", 1.0, [{"runs": [R("Rules for the set", 11, True, INK, HAND)], "after": 0},
    {"runs": [R("No caller names or notes. Agent ID held by QA only. Held out by time. Every field a 2030 CRM requirement.", 8.2, False, INK)]}], pad=0.1)
text(s, 7.45, 5.0, 5.2, 1.2, [{"runs": [R("What it lets the algorithm learn:", 9, True, BLUE, BODY_SB)], "after": 2}] +
     bullets(["Whether the two answers predict an empty visit better than the code alone.", "Whether picked and final code differ: the City's first ground truth for \"coded correctly\".", "Which codes are confusing vs which standards are unclear: two different fixes."], 8.3, gap=1, mark="✓", mcolor=GREEN))
concepts(s, ["S6 · data is built", "S6 · inventory columns", "S6 · SBS reply is not fix", "S1 · how examples were labelled", "S5 · what it cannot show"])
notes(s, "This is the 30% criterion. Left: the inventory in the Session 6 columns, with the behaviour change each gap needs. Right: the data set the City does not have and the pilot creates: one row per flagged call with the answers, the agent's choice, the outcome and the re-route. By day 90 it is large enough to re-estimate pilot codes from their own closures and to test whether answers beat codes. Labels are the area's verdict: audit them, pair them with re-contact.")

# =====================================================================
# 13 PLAN
# =====================================================================
s = base(d, "How we roll it out",
         ["Ninety days inside 311's own authority, three areas, half the teams. ", ("Phase two is bought only if the gate passes.",)],
         src="Split after the course's consulting-deck standard (USPS 2010): within 311's authority vs needs others. Pilot by team-week randomisation; at ~3,200 flagged calls a month a 20% relative drop reads out in about six weeks (80% power, 5% two-sided; clustering makes this a minimum). Generative AI Standard (Jul 2024) and Privacy Impact Assessment standard (May 2026) apply from phase two.")
hand_line(s, 0.6, 2.75, 12.7, 2.75, INK, 2.25, arrow=True)
phases = [("Days 1-30 · build, no screen change", 0.6, [
              ("311", "Re-run backtest on internal closures; pick pilot areas: Municipal Enforcement, Peace Officers, Parking (3 of 4 flagged empty visits).", "yellow"),
              ("Agents + CSU 52", "Co-design the card with senior agents. In writing: coaching only, no ranking.", "yellow"),
              ("Needs others", "CRM data agreement; required closure reason + reassignment field; areas write two questions.", "pink")]),
          ("Days 31-60 · shadow mode", 4.65, [
              ("311", "Score every pick, show nothing. Confirm 18% flagged and the mix matches the backtest.", "mint"),
              ("Data set starts", "Log tier, outcome, reason, re-route for every flagged referral. Digest and fix queue begin.", "mint"),
              ("Needs others", "Areas close with a reason on 80%+ of flagged referrals, or the pilot waits.", "pink")]),
          ("Days 61-90 · pilot", 8.7, [
              ("311", "Card on for half the teams by team-week at random; the other half is the control. Clock paused on flagged calls.", "blue"),
              ("Data set fills", "Two answers and the agent's choice on every flagged call; QA samples 200 resolved calls a month.", "blue"),
              ("Needs others", "Weekly fix queue with the three areas. Union walkthrough at day 75.", "pink")])]
for lbl, x, items in phases:
    rect(s, x + 1.7, 2.63, 0.25, 0.25, PAPER, RED, 2.0, shape=MSO_SHAPE.OVAL)
    brush_label(s, x + 0.05, 1.85, lbl, 12, "yellow", w=3.6)
    for j, (h, b, col) in enumerate(items):
        sticky(s, x, 3.0 + j * 0.86, 3.85, 0.78, col, (-0.6, 0.5, -0.4)[j], [{"runs": [R(h + ": ", 8.5, True, INK, BODY_SB), R(b, 8, False, INK)]}], pad=0.08, shadow=False)
sticky(s, 0.6, 5.62, 12.2, 0.6, "cream", 0, [{"runs": [R("Phase two · months 5-12, if the gate passes: ", 8.6, True, INK, BODY_SB),
    R("all teams and areas; retrain on the 90-day set; text suggestion on the agent's notes (top three codes, never pre-selected), 85% top-three offline first.  ", 8.2, False, INK),
    R("Phase three · 2027 on: ", 8.6, True, INK, BODY_SB), R("every pilot field becomes a 2030 CRM requirement; shared app/web intake only if the phone pilot passes. No automatic routing.", 8.2, False, INK)]}], pad=0.08, shadow=False)
concepts(s, ["Deck std · within control vs needs others", "S4 · strategic foresight", "S2 · staged options", "S10 · governance"])
notes(s, "Ninety days in three columns, each split into what 311 controls and what needs others. Phase two is where the AI assistant from the team's plan enters, gated and in shadow first, reusing the City's July 2026 app AI, under the Generative AI Standard's human-review rule and a privacy impact assessment. Phase three carries the CRM requirements and the platform option with its start condition. Full automatic routing is not on the roadmap.")

# =====================================================================
# 14 GATE + MEASURES
# =====================================================================
s = base(d, "How we know it works",
         ["One primary measure, paired with the thing it could corrupt. ", ("Handle time is a guardrail, never a target.",)],
         src="Measures chosen before launch (Session 9: proxies drift; values wither when nothing measures them). Base case: 21.2% of flagged referrals ended in an empty visit in 2026. Weekly City-wide bounce rates ran 0.79% to 2.05% (Apr-Oct 2026), so the City-wide average cannot be the test.")
gate = ["Empty-visit rate on flagged codes, pilot vs control: down 20%+", "Referrals a caller wanted and did not get: zero",
        "Handle time on flagged calls: +15 s or less; 120-s target met", "Override rate between 20% and 80%",
        "Closure reason on 80%+ of flagged referrals, all three areas", "Data set: 5,000+ labelled flagged calls",
        "Three areas and CSU 52 sign the phase-two scope"]
pic(s, "wash_yellow", 0.55, 1.85, 4.3, 4.35)
text(s, 0.75, 1.95, 3.9, 0.4, [[R("The gate · day 120 · all must be true", 13, True, INK, HAND)]])
for i, g in enumerate(gate):
    wobble_box(s, 0.8, 2.47 + i * 0.52, 0.22, 0.22, INK, 1.25, jitter=0.012, seed=60 + i)
    text(s, 1.12, 2.35 + i * 0.52, 3.6, 0.38, [[R(g, 9, False, INK)]], anchor="middle")
table(s, 5.15, 1.85, [2.3, 0.95, 1.05, 0.85, 2.5], [
    ["Measure", "Baseline", "Target", "Type", "What it could reward by mistake"],
    ["Empty-visit rate on flagged codes, pilot vs control", "21.2%", "-20% at gate; -35% expected", "Primary", "Areas closing \"no action\" less on paper: paired with re-contact"],
    ["Resident re-contact within 30 days", "measure in shadow", "no rise", "Resident", "Catches a check that talks residents out of real problems"],
    ["Referrals wanted and not given", "none", "zero", "Guardrail", "The algorithm becoming a gate (Robodebt)"],
    ["Days in the wrong queue per bounce", "2.0 days", "down", "Resident", "Kept from October: bounces matter for hazards"],
    ["Closure reason back within 24 h", "none", "90%", "Learning", "A digest nobody opens: track opens"],
    ["Handle time on flagged calls", "from 311", "+15 s max", "Guardrail", "A target here recreates the speed incentive"],
    ["Override rate", "none", "20-80%", "Guardrail", "Below 20% rubber stamp; above 80% noise"]],
    [0.32, 0.52, 0.42, 0.42, 0.42, 0.42, 0.42, 0.42], size=7.9)
sticky(s, 5.15, 5.25, 7.65, 0.95, "pink", -0.3, [{"runs": [R("What would change our minds: ", 9, True, INK, BODY_SB),
    R("shadow flags 30%+ of calls (raise the cut-off); re-contact rises (stop, redesign the questions); control falls too (recording change, extend); handle time +15 s (cut to one question). Values we refuse to trade: no resident refused a referral, no agent ranked.", 8.2, False, INK)]}], pad=0.1)
concepts(s, ["S9 · proxy drift, values wither", "S9 · measures before launch", "S6 · every measure rewards something", "S2 · what flips it"])
notes(s, "Session 9 applied to ourselves. The primary measure (empty-visit rate on flagged codes) could be gamed by areas closing differently, so it is paired with resident re-contact. The Robodebt guardrail is explicit: referrals a caller wanted and did not get must be zero. Handle time stays a guardrail, not a target, or the routine recreates the speed incentive the problem tree found. 'What would change our minds' pre-empts the Q&A. The gate reads out at day 120 (60 days of pilot) to allow for clustering and closure lag.")

# =====================================================================
# 15 THE ASK + PREMORTEM
# =====================================================================
s = base(d, "The ask",
         ["Approve a 90-day pilot in three areas, and ", ("decide again at day 120",), " with the numbers on the previous slide."],
         src="Premortem after Klein (2007). Peers: Amsterdam Signalen (algoritmes.overheid.nl gm0363); Winnipeg 311 budget presentation (Dec 9, 2025) p. 6; Madrid SyRCI-IA (Interoperable Europe); Denver Council record 26-1373, Auditor Aug 2025. One-time cost is a team estimate with no City quote.")
asks = [("1 · Approve the pilot", "150 codes above 20% risk, three areas, half the teams. One-time configuration est. $10K-$150K (assumed, no City quote); running ~$30K/yr of agent time, inside the $375K it frees.", "yellow"),
        ("2 · Sign the data agreement", "Two CRM fields (closure reason, reassignment) in Municipal Enforcement, Peace Officers, Parking, and 311 access to internal closures.", "mint"),
        ("3 · Set terms with CSU 52", "Coaching only, no ranking, clock paused on flagged calls, walkthrough at day 75. Agreed before any agent sees a card.", "pink")]
for i, (h, b, col) in enumerate(asks):
    sticky(s, 0.55 + i * 2.15, 1.9, 2.0, 2.45, col, (-1.5, 1.0, -0.8)[i], [{"runs": [R(h, 11.5, True, INK, HAND)], "after": 2}, {"runs": [R(b, 8.8, False, INK)]}], pad=0.11)
brush_label(s, 7.15, 1.85, "Premortem: Dec 2027, it failed. Why?", 13, "pink", w=4.9)
pm = [("The rate fell on paper", "Areas closed fewer as \"no action\". Answer: paired re-contact, label audits."),
      ("Agents clicked through", "Override sat at 5%. Answer: 20-80% guardrail, one question, team-lead coaching."),
      ("The signal drowned", "Two areas changed recording. Answer: judge vs control, by area."),
      ("A reason not on the tree", "CRM vendor can't add fields before 2028. Answer: shadow and data set run on exports.")]
for i, (h, b) in enumerate(pm):
    sticky(s, 7.15 + (i % 2) * 2.85, 2.4 + (i // 2) * 1.05, 2.7, 0.95, ("cream", "cream", "cream", "red")[i], (0.8, -0.8, -0.6, 0.9)[i], [{"runs": [R(h, 10, True, INK, HAND)], "after": 0}, {"runs": [R(b, 7.8, False, INK)]}], pad=0.08, shadow=False)
text(s, 0.55, 4.55, 6.2, 1.6, [{"runs": [R("Upside and downside, beside the forecast", 11, True, INK, HAND)], "after": 2},
    {"runs": [R("Upside: ", 8.8, True, GREEN, BODY_SB), R("P90 $622K; answer-level risk in phase two reaches the 35% of empty visits in green codes; residents hear the reason.", 8.5, False, INK)], "after": 2},
    {"runs": [R("Downside: ", 8.8, True, RED, BODY_SB), R("P10 $171K; 20 s on 38,000 calls a year; a published rate the areas resent. Nothing is hard to undo: turn the card off and the fields stay useful.", 8.5, False, INK)]}])
text(s, 7.15, 4.6, 5.7, 1.6, [{"runs": [R("What other cities teach", 11, True, INK, HAND)], "after": 2}] + bullets([
    [R("Winnipeg ", 8.3, True, INK, BODY_SB), R("publishes returns due to agent error (1.62%, 2024): measuring misroutes is normal.", 8.2)],
    [R("Madrid: ", 8.3, True, INK, BODY_SB), R("receiving units validated 79% of 38,221 AI routings; rejections retrain.", 8.2)],
    [R("Amsterdam ", 8.3, True, INK, BODY_SB), R("(Signalen, since 2022): under 40% confidence goes to a human desk.", 8.2)],
    [R("Denver: ", 8.3, True, INK, BODY_SB), R("chatbot paired with cuts; Council voted 9-3 against. Ours cuts no position.", 8.2)]], gap=1))
concepts(s, ["S2 · premortem", "S2 · staged options", "Deck std · risks beside forecast", "S4 · who says yes, in order", "Brief · not already doing it"])
notes(s, "Close on the decision the room can take today. Three asks, in the order the political game requires: 311 approves, the CRM owner and three areas sign, the union agrees the terms. Premortem (Klein): four failure stories, each with the answer already in the design; the fourth is the reason not on the tree. Upside and downside beside the forecast. Peers: measuring misroutes is ordinary (Winnipeg); humans validate AI routing (Madrid); tools paired with cuts fail politically (Denver).")

# =====================================================================
# 16 AI PROCESS REFLECTION
# =====================================================================
s = base(d, "AI Process Reflection",
         ["How we worked with AI, the two moves that changed the analysis, ", ("and where the AI was wrong.",)],
         src="Sloan and Glaser (2026), Stop Prompting AI, Start Directing It; Glaser, Sloan and Knight (2025): assistant, analyst, coach; Mollick (2024); AI Literacy Exercise brief. All analysis and final writing are the team's own; every figure re-derived from the open data by a team member.")
quads = [("Tools, and the task each did", "yellow", [
            "Analyst: Claude with Python and DuckDB over 3.5M open-data rows (backtest, ten-year check, Monte Carlo); re-runnable scripts in the project folder.",
            "Assistant: first drafts of slide text and the deck build script; the team rewrote every slide.",
            "Coach: AI played the skeptical 311 director and the CSU 52 rep before team meetings.",
            "Fact-checkers: agents checked the Nov 1 report: 610 rows, 369 verified, 208 corrected, 25 unverified, 8 wrong."]),
         ("Two crux moves", "mint", [
            "The AI argued against our own AI idea: training labels are agents' own picks, errors included. The suggester became a gated phase two behind a human-built data set.",
            "\"Give me the most savings\" moved the decision: bounces alone came back at $7K-$17K; the larger loss was 12,583 empty visits, so the card's question became \"does it meet the standard?\"."]),
         ("How we validated", "blue", [
            "Two independent pulls (City API and the team's CSV export); counts matched.",
            "Trained on one year, tested on the next; a richer model that scored better in-sample was dropped.",
            "Every figure sourced or labelled assumed; uncheckable citations dropped.",
            "Framing test: gain-first vs loss-first; loss-first produced the refusal rule."]),
         ("Where the AI was wrong", "pink", [
            "Counted 1,930 phone codes vs our 1,917: a definition difference, footnoted.",
            "Proposed the 35% avoided share with no source: kept only as a labelled assumption.",
            "First pilot design needed 3.6 months; a power calculation on the right outcome cut it to six weeks.",
            "Drafted fluent prose that read as ours: we rewrote and kept a change log."])]
for i, (h, col, items) in enumerate(quads):
    x = 0.55 + (i % 2) * 6.2; y = 1.85 + (i // 2) * 2.2
    sticky(s, x, y, 5.95, 2.05, col, (-0.6, 0.5, 0.4, -0.5)[i], [{"runs": [R(h, 13.5, True, INK, HAND)], "after": 2}] + bullets(items, 9.6, gap=3), pad=0.14)
concepts(s, ["S8 · direct, don't prompt", "S1 · assistant / analyst / coach", "S1 · human in the loop", "S3 · prompt framing"])
notes(s, "Draft only: the team must write this slide in its own voice and with its own log. The four quadrants follow the brief: tools by kind of task, one or two crux moves, how outputs were validated, and what happened when the AI was wrong. 'A reflection that reports only successes has not been written honestly.' The figures in the fact-check line come from the Nov 1 team report.")

# =====================================================================
# APPENDIX
# =====================================================================
s = d.prs.slides.add_slide(d.blank); d.page += 1
pic(s, "canvas", 0, 0, 13.333, 7.5)
pic(s, "brush_yellow2", 2.2, 3.0, 9.0, 1.3, rot=-0.8)
text(s, 2.2, 2.95, 9.0, 1.35, [{"runs": [R("Backup", 40, True, INK, HAND)], "align": "c"}], anchor="middle")
text(s, 2.2, 4.45, 9.0, 0.5, [{"runs": [R("A1 risk score · A2 codes · A3 ten-year check · A4 Monte Carlo · A5 pilot length · A6 political game · A7 concept map · A8 sources", 11, False, GREY)], "align": "c"}])
footer(s); page_badge(s, d.page)

def appx(code, title, src=None):
    return base(d, "Appendix " + code, title, src=src, kcolor="blue", tsize=18)

# A1
s = appx("A1", "The score is a shrunk ratio per code, computed from fields the City already publishes.",
         OD + ". Scripts: edmonton-311-analysis/scripts/s1b.py (Referral Check), a1-a4.py (Route Check), code_risk_table_2025.csv.")
text(s, 0.55, 1.75, 5.6, 4.4, bullets([
    [R("Code ", 9, True, INK, BODY_SB), R("= service area + category + description (1,930 phone codes in 2025).", 9)],
    [R("Empty field outcome ", 9, True, INK, BODY_SB), R("= Does Not Meet Bylaw Offence Standards, Assessed - No Action Required, Unable to Locate Animal, Location Not Found, Unable to Contact Complainant.", 9)],
    [R("Wasted desk outcome ", 9, True, INK, BODY_SB), R("= 311 Redirecting to Other Business Area (bounce), Non-City Service or Location, Duplicate Request (three labels), File Already under Investigation, Reported on same day.", 9)],
    [R("Left out: ", 9, True, INK, BODY_SB), R("Parking \"Vehicle Gone Upon Arrival\" (4,886 in 2025): depends on dispatch speed (9.7% if closed within an hour vs 44.2% at 3-12 h), not intake.", 9)],
    [R("Score ", 9, True, INK, BODY_SB), R("= (empty + prior mean x 10) / (referrals + 10), for field and desk separately, then summed. Prior means 2025: field 6.6%, desk 4.1%.", 9)],
    [R("Refresh ", 9, True, INK, BODY_SB), R("weekly, rolling 12 months; new codes amber for 90 days. Three years of history did no better than one.", 9)],
    [R("Route Check lives inside Referral Check: ", 9, True, INK, BODY_SB), R("the bounce ratio is one of the two terms.", 9)]], gap=4))
table(s, 6.5, 1.75, [1.3, 0.7, 1.15, 1.2, 1.0], [
    ["Cut-off", "Codes", "Calls flagged", "Empty visits caught", "Waste rate in set"],
    ["> 10%", "425", "35.9%", "83.5%", "22.1%"], ["> 15%", "215", "26.5%", "76.1%", "26.8%"],
    ["> 20% (chosen)", "150", "18.1%", "64.9%", "30.1%"], ["> 25%", "99", "13.6%", "53.6%", "32.0%"],
    ["> 30%", "72", "11.5%", "47.4%", "34.0%"], ["> 40%", "34", "9.0%", "43.0%", "38.1%"], ["> 50%", "14", "4.1%", "18.9%", "38.5%"]],
    [0.45] + [0.36] * 7, size=9)
red_circle(s, 6.4, 1.75 + 0.45 + 2 * 0.36 - 0.04, 5.55, 0.44, 1.75)
text(s, 6.5, 5.15, 5.4, 0.9, [[R("Base rates, 2026 to Nov 6: 5.9% of phone referrals ended in an empty field visit, 4.2% in a wasted desk outcome, 10.1% in either. 2025: 12,583 field, 7,815 desk, of 191,521 referrals.", 8.8, False, INK)]])

# A2
s = appx("A2", "Ten codes carry most of the flagged empty visits, and three areas carry three in four.",
         OD + ", phone referrals, Jan 1 to Nov 6, 2026. Flagged set = 150 codes above 20% 2025 risk.")
table(s, 0.55, 1.8, [4.2, 1.6, 1.4, 1.8], [
    ["Area", "Flagged referrals", "Empty visits", "Share of flagged empty visits"],
    ["Community Standards - Municipal Enforcement", "10,937", "2,812", "41%"], ["Roadway Maintenance", "10,808", "1,519", "22%"],
    ["Community Standards - Peace Officers", "3,218", "1,446", "21%"], ["Parking Enforcement", "2,385", "625", "9%"],
    ["Animal Control", "2,210", "225", "3%"], ["Park Rangers", "1,560", "123", "2%"], ["All other", "1,390", "135", "2%"]],
    [0.45] + [0.4] * 7, size=10)
sticky(s, 9.85, 1.8, 2.95, 3.3, "yellow", 1.2, [{"runs": [R("Why the question changed", 12, True, INK, HAND)], "after": 2},
    {"runs": [R("The flagged codes are complaints where an officer must judge a standard (untidy, noise, weeds, parking on private property), not assets with an ambiguous owner. Municipal Enforcement, Peace Officers and Parking are the pilot areas. Roadway Maintenance is seasonal and joins in phase two.", 10.5, False, INK)]}], pad=0.14)

# A3
s = appx("A3", "The same lookup has ranked next year's bounces every year since 2016; the step-ups track recording, not coding.",
         "City of Edmonton yearly 311 datasets 2016-2022 (deduplicated by Row ID) and the current dataset 2023-2026. Score trained on the prior year, tested on the year shown; flag = 2% bounce risk.")
rows = [["Year", "Phone referrals", "Bounces", "Rate", "Areas recording", "AUC (prior yr)", "Caught at 2%", "On new codes"],
        ["2026 (to Nov 6)", "179,139", "1,930", "1.08%", "31", "0.82", "41%", "8.4%"], ["2025", "191,521", "1,062", "0.55%", "24", "0.90", "56%", "1.2%"],
        ["2024", "188,003", "874", "0.46%", "20", "0.93", "64%", "7.6%"], ["2023", "193,077", "1,062", "0.55%", "23", "0.93", "58%", "1.4%"],
        ["2022", "223,944", "1,205", "0.54%", "20", "0.91", "43%", "2.7%"], ["2021", "225,435", "584", "0.26%", "17", "0.92", "33%", "22.1%"],
        ["2020", "200,313", "562", "0.28%", "17", "0.90", "36%", "2.1%"], ["2019", "254,693", "566", "0.22%", "19", "0.90", "44%", "4.4%"],
        ["2018", "261,243", "649", "0.25%", "14", "0.91", "35%", "20.5%"], ["2017", "259,028", "585", "0.23%", "20", "0.86", "28%", "6.2%"]]
table(s, 0.55, 1.75, [1.45, 1.15, 0.85, 0.75, 1.0, 1.0, 0.95, 0.95], rows, [0.45] + [0.33] * 10, size=9)
sticky(s, 9.0, 1.75, 3.8, 4.1, "mint", -1.0, [{"runs": [R("What the history adds", 12, True, INK, HAND)], "after": 2}] + bullets([
    "The bounce rate stepped up in 2022 and 2026; both line up with more areas recording (all-channel bounces 2,162 in 2021 to 4,515 in 2022).",
    "Phone volume fell by two thirds (1.83M in 2016 to 0.67M in 2025) while phone codes grew from 1,701 to 1,930: less practice per code, the Kahneman and Klein condition eroding.",
    "One-year rolling history is enough and adapts faster."], 9.6, gap=5), pad=0.14)

# A4
s = appx("A4", "Every input is a range with a source or a flag; the one that moves the answer most is ours.",
         "Triangular distributions (min / most likely / max), 50,000 draws, seed 20261110, independent draws. Volumes annualised from Jan 1 to Nov 6, 2026 (x 12 / 10.2). Six questions for reviewing an analysis: Session 2.")
table(s, 0.55, 1.75, [2.9, 1.9, 2.4], [
    ["Input", "Min / likely / max", "Source or status"],
    ["Empty field visits a year, flagged codes", "8,100 (counted)", "Open data, 2026 annualised"],
    ["Wasted desk closures a year, flagged codes", "3,414 (counted)", "Open data, 2026 annualised"],
    ["Flagged referrals a year", "38,245 (counted)", "Open data, 2026 annualised"],
    ["Cost of a field visit", "$22 / $84 / $280", "Team's Oct 26 ranges; no City figure"],
    ["Desk time per closure", "5 / 10 / 20 min at $36.93-$52.09/h", "CSU 52 collective agreement rates"],
    ["Share of flagged empty visits avoided", "20% / 35% / 50%", "ASSUMED; pilot measures it; break-even 2.6%"],
    ["Agent time per flagged call (20 s)", "$0.30 / $1.02 / $1.02", "Agent-only to avg cost per contact ($16.29)"],
    ["311 re-handling share on desk waste", "25% x $16.29", "Team judgment"]],
    [0.4] + [0.42] * 8, size=8.6)
sticky(s, 8.0, 1.75, 4.8, 4.3, "cream", 0.6, [{"runs": [R("Six questions for this analysis", 12, True, INK, HAND)], "after": 2}] + bullets([
    "Is this the decision we face? Yes: the pick on a phone referral, consequence widened.",
    "Missing, overlapping? Vehicle Gone left out; bounces sit inside desk waste, so October's $100K is not added twice.",
    "Observed vs estimated? Volumes observed; costs are ranges; avoided share assumed.",
    "What averages hide? Rates per code; pilot judged inside flagged codes.",
    "What flips it? Avoided share under 2.6%, or a visit under ~$10.",
    "What could we lose? Agent trust if the card is noise; area goodwill if the rate becomes a league table."], 9, gap=3) +
    [{"runs": [R("Net mean $375K; median $347K; P10 $171K; P90 $622K; no draw below zero. At 30% cut-off: $276K.", 8.3, True, BLUE, BODY_SB)], "before": 3}], pad=0.14)

# A5
s = appx("A5", "Because the outcome is common (one in five flagged referrals), the pilot reads out in weeks, not quarters.",
         "Two-proportion test, 80% power, 5% two-sided; baseline 21.2% of flagged referrals ending in an empty visit; ~3,200 flagged phone referrals a month at the 20% cut-off, split 50/50 by team-week. Clustering adds a design effect: treat as minimums.")
table(s, 0.55, 1.8, [3.6, 2.0, 2.0], [
    ["Drop to detect", "Flagged referrals per arm", "Months of pilot (50/50)"],
    ["20% relative (21.2% to 17.0%)", "1,347", "0.85"], ["35% relative (21.2% to 13.8%)", "408", "0.26"],
    ["At the 30% cut-off, 20% drop (24.5% to 19.6%)", "1,120", "1.1"], ["Route Check (bounces, 7.0% base), 30% drop", "about 2,000", "3.6"]],
    [0.45] + [0.45] * 4, size=10)
text(s, 0.55, 4.3, 7.6, 1.7, [[R("Design: half the teams see the card in a given week, chosen at random by team-week; the other half is the control. Both log answers only when the card shows, so the control measures today's routine. The gate is set at day 120 (60 days of pilot) to allow for clustering and the areas' closure lag (most field outcomes close within three weeks).", 9.5, False, INK)]])
sticky(s, 8.7, 1.8, 4.1, 3.6, "yellow", -1.0, [{"runs": [R("Gate arithmetic", 13, True, INK, HAND)], "after": 2}] + bullets([
    "Baseline inside flagged codes: 21.2% empty visits (6,885 of 32,508, 2026 to Nov 6).",
    "Gate: 17.0% or lower in pilot teams while control stays near 21%.",
    "Expected: 13.8% (35% avoided). Upside: 10.6% (50%).",
    "Read-across: 20% avoided ~ $200K/yr; 35% = $375K; 50% ~ $550K."], 10.5, gap=5), pad=0.15)

# A6
s = appx("A6", "Who must say yes, in what order, and what each stands to lose.",
         "Session 4: players, goals, actions, best moves, likely moves. CSD03148 (Sep 2, 2026); OCA 2023; CSU 52 collective agreement Art. 11.03 (technological change). 'At stake' cells are hypotheses to test in the day 1-30 interviews, not findings.")
table(s, 0.55, 1.75, [1.75, 1.9, 1.85, 2.4, 4.3], [
    ["Player", "Measured on today", "Goal", "At stake (hypothesis)", "Likely move, and our answer"],
    ["311 and Customer Access", "98.7% resolved on first contact; 120-s answer", "Fewer repeat calls; defensible scorecard", "A new scorecard line that can go down", "Approves if the measure is paired and framed as capacity: it is"],
    ["Receiving areas (3 pilot)", "Closed within timelines (81%)", "Officers on real work; control of labels", "Empty-visit rate read as an audit of officers", "Stall unless they own the questions and the queue: they do"],
    ["Agents and CSU 52", "Answer speed; Art. 11.03", "No hidden ranking; no job loss", "20 s per flagged call; a digest that becomes a file", "Accept with coaching-only terms and a paused clock, agreed in writing first"],
    ["CRM owner / IT", "Uptime; 2030 replacement scope", "No scope creep on a dying system", "Effort on a platform being replaced", "Two fields, or exports in shadow; every field a 2030 requirement"],
    ["Council and Auditor", "Closures, duplicates, compliance", "Residents served; findings closed", "A number never reported before", "Welcome a measure already in open data"],
    ["Residents", "Nothing", "One call, right outcome, a reason", "Being talked out of a real problem", "The consent rule: a referral on request, always"]],
    [0.45] + [0.62] * 6, size=8.6)

# A7 concept map (one slide, condensed)
s = appx("A7", "Every course concept earned its place by changing a design choice, not by touring the syllabus.",
         "Group Project brief: concepts should be appropriate and insightful, not a tour. Sessions 8-10 follow the syllabus; the team updates them after Nov 16, 23 and 30.")
cm = [["Session · concept", "Slide", "The design choice it changed"],
      ["S1 · three kinds of system; four agent questions; agency; Northfield", "6, 8", "A learned ratio plus a rule; read-only access, kill switch; authority with the agent, accountability with the area"],
      ["S2 · problem, profit and decision trees; EV; mix; sensitivity; premortem", "4, 5, 6, 15", "Tree by stage of call; capacity case with ranges; 2% floor, 20% cut-off; four failure stories"],
      ["S3 · System 1/2; Kahneman and Klein; ten biases; framing", "4, 10, 11", "One question, one call in five; reason back in a day; answer-first card; our biases declared"],
      ["S4 · political game; where you stand; foresight", "10, A6", "Areas write questions and co-own the queue; every field a 2030 CRM requirement"],
      ["S5 · Garneau: disaggregate; what data cannot show", "5, 9, 12", "Per-code rates; gaps listed; the 90-day set built to close them"],
      ["S6 · data is built; inventory; metric built slightly wrong", "12, 14", "Required closure reason; label audits; re-contact paired with the primary measure"],
      ["S7 · ostensive / performative / artifact; McGarry; Ironstone", "3, 7, 13", "The algorithm as a new artifact; co-design with senior agents"],
      ["S8-S10 · direct AI; proxy drift and Robodebt; what to refuse", "8, 14, 16", "Roles assigned to AI; zero declined referrals; closing, declining and hazards never automated"],
      ["Brief and deck standard · five-part test; takeaway titles; risks beside forecast", "all", "Caller 7; the pick, not intake; 90 days split by authority"]]
table(s, 0.55, 1.75, [4.4, 1.2, 6.6], cm, [0.4] + [0.43] * 9, size=8.6)

# A8 sources
s = appx("A8", "Sources.", None)
srcs = ["City of Edmonton, 311 Requests open data (q7ua-agfg), accessed Nov 6-10, 2026, and yearly datasets 2016-2022. https://data.edmonton.ca/d/q7ua-agfg",
        "City of Edmonton, CSD03148 (Sep 2, 2026) and Attachments 1-2; Office of the City Auditor, City's Response to 311 Requests (Nov 2023); FCS02139 (Nov 30, 2023).",
        "City of Edmonton, Generative Artificial Intelligence Standard (Jul 25, 2024; s. 3.2 Jul 29, 2025); Administrative Standard on Privacy Impact Assessments (May 13, 2026); CSU 52 collective agreement 2024-2027, Art. 11.03.",
        "City of Edmonton operating budget: 311 and Customer Access $14.66M (2026). Toronto 311 cost per call $11-16 (Global News, Jan 19, 2024).",
        "Winnipeg 311 budget presentation (Dec 9, 2025) p. 6; Madrid SyRCI-IA (Interoperable Europe); Amsterdam Signalen (algoritmes.overheid.nl, gm0363); Dallas Auditor 311 SLA audit (Apr 2026); Denver Auditor (Aug 2025) and Council record 26-1373; Toronto, Simplifying the 311 Intake Experience (Apr 30, 2026).",
        "Glaser, V. L. (2026a) Analytic Trees; (2026b) The Psychological Perspective; Session 1 and 4 decks. Glaser, Sloan and Gehman (2024) Organizations as Algorithms, JMS 61(6). Glaser, Sloan and Knight (2025) FFI Practitioner. Sloan and Glaser (2026) Stop Prompting AI, MIT SMR.",
        "Kahneman and Klein (2009) Am. Psychologist 64(6); Klein (2007) HBR; Feldman and Pentland (2003) ASQ 48(1); Lindebaum, Glaser, Moser and Ashraf (2022) MIT SMR; Mollick (2024) Co-Intelligence; Tversky and Kahneman (1974, 1981); Moore and Healy (2008); Allison (2016).",
        "Green, B. (2022) The flaws of policies requiring human oversight of government algorithms; Bucinca et al. (2021) To trust or to think; Alon-Barkat and Busuioc (2023) Human-AI interactions in public sector decision making.",
        "Team materials: Strategic Analytics Initiative deck (Oct 26, 2026); team research report (Nov 1, 2026); final presentation plan (Nov 10, 2026); analysis scripts and tables in the project folder."]
text(s, 0.55, 1.6, 12.2, 5.0, bullets(srcs, 9.5, gap=5))

d.save(OUT)
print("saved", OUT, d.page, "slides")
