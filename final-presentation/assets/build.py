import sys
sys.path.insert(0, "/tmp/claude-0/-home-user/792c5072-ff21-5e30-8643-ca6c4b8a353c/scratchpad/build")
from lib import *

d = Deck()
DUR = [45, 60, 75, 75, 60, 75, 75, 60, 75, 60, 60, 75, 60, 45]
START = [sum(DUR[:i]) for i in range(len(DUR))]
OD = "311 Requests open data (q7ua-agfg), pulled Nov 7, 2026"

# =====================================================================
# 1 COVER
# =====================================================================
s = d.prs.slides.add_slide(d.blank); d.page += 1
s.background.fill.solid(); s.background.fill.fore_color.rgb = rgb(NAVY2)
callbar(s, 'Mon Dec 7, 9:05 · Caller 4 · "The garbage can by the park on our corner is overflowing again."', 0, label="INCOMING CALL")
kicker(s, 0.6, 0.95, 8, "SEM 620 · SOLUTION PROPOSAL · CLIENT: 311 AND CUSTOMER ACCESS", color=YELLOW)
text(s, 0.6, 1.3, 7.6, 1.9, [{"runs": [R("Same call. Same code.", size=44, bold=True, color=WHITE)], "line": 0.9},
                             {"runs": [R("This time, the screen speaks up.", size=44, bold=True, color=YELLOW)], "line": 0.9}])
text(s, 0.6, 3.45, 7.3, 2.4, [
    {"runs": [R("Route Check", size=15, bold=True, color=YELLOW), R(" is a 20-second check on the ", size=15, color=WHITE),
              R("6% of phone referrals", size=15, bold=True, color=WHITE), R(" most likely to land in the wrong area, and a loop that sends every miss back to someone who can fix it.", size=15, color=WHITE)], "after": 10},
    {"runs": [R("Tested on 2026 tickets it never saw, it flags 1 in 16 referrals and catches ", size=15, color=WHITE),
              R("41% of bounces", size=15, bold=True, color=YELLOW), R(". The agent keeps the final pick.", size=15, color=WHITE)], "after": 10},
    {"runs": [R("Today: what it does, what data it needs, who has to change, and the first 90 days.", size=13, color="C2D3E0")]},
])
# illustrative screen
rrect(s, 8.75, 0.95, 4.0, 5.55, WHITE, radius=0.06)
text(s, 8.95, 1.05, 3.6, 0.25, [[R("SERVICE CODE", size=8, bold=True, color=SLATE, spc=150), R("      ILLUSTRATIVE SCREEN", size=7, bold=True, color=ORANGE, spc=100)]])
rrect(s, 8.95, 1.35, 3.6, 0.36, "F3F7FA", LINE, radius=0.2)
text(s, 9.05, 1.37, 3.4, 0.32, [[R("garbage can|", size=11, color=NAVY, font="Consolas")]], anchor="middle")
text(s, 8.95, 1.76, 3.6, 0.22, [[R("4 codes · 3 descriptions · 4 owners", size=8, color=SLATE)]])
rows = [("GARBAGE:Can Needs Emptying", "Parks", "3.8%", ORANGE), ("Overflowing Garbage Can", "Transit", "0.5%", GREEN),
        ("311 - Empty Existing Garbage Can", "Facility Maintenance", "40%", RED), ("GARBAGE:Can Needs Emptying", "River Valley Operations", "0.2%", GREEN)]
yy = 2.02
for i, (c, a, r, col) in enumerate(rows):
    picked = i == 2
    rrect(s, 8.95, yy, 3.6, 0.5 if not picked else 1.55, "FFF4F4" if picked else WHITE, RED if picked else LINE, lw=1.5 if picked else 0.75, radius=0.08)
    text(s, 9.05, yy + 0.03, 2.6, 0.24, [[R(c, size=9, bold=True, color=NAVY, font="Consolas")]])
    text(s, 9.05, yy + 0.25, 2.4, 0.2, [[R(a, size=8, color=SLATE)]])
    text(s, 11.55, yy + 0.05, 0.95, 0.4, [{"runs": [R("risk ", size=7, color=SLATE), R(r, size=10, bold=True, color=col)], "align": "r"}])
    if picked:
        rect(s, 9.05, yy + 0.5, 3.4, 0.008, "F0B8BB")
        text(s, 9.05, yy + 0.55, 3.4, 0.95, [
            {"runs": [R("● RED · CHECK OWNER FIRST", size=8, bold=True, color=RED, spc=100)], "after": 2},
            {"runs": [R("Bounced 50 of 116 times last year. Ask: ", size=8.5, color=NAVY), R('"Is the can in the park, at a bus stop, or outside a City building?"', size=8.5, bold=True, color=NAVY)]}])
        yy += 1.6
    else:
        yy += 0.56
text(s, 8.95, 6.12, 3.6, 0.35, [[R("Risk = each code's 2025 phone-referral bounce rate, shrunk for small samples (2026 test, Appendix A1).", size=7, color=SLATE)]])
text(s, 0.6, 6.3, 7.5, 0.3, [[R("Rick Auger · Lauren Lonsberry · Nav Sekhon · Curtis Middleton", size=11, color=WHITE)]])
text(s, 0.6, 6.6, 7.5, 0.3, [[R("December 7, 2026", size=10, color="C2D3E0")]])
notes(s, """COVER (about 45 s). Presenter: Curtis.
Open with Caller 4 again, the same call from October: the garbage can by the park, the agent types "garbage can", four codes come up. In October the agent picked the Facility Maintenance code and the ticket bounced 1.6 days later. Today the same pick turns red on the screen, and the agent asks one question before the ticket routes.
Risk numbers on the screen: shrunk 2025 phone-referral bounce rates from the code risk table (edmonton-311-analysis/code_risk_table_2025.csv). "311 - Empty Existing Garbage Can": 50 bounces on 116 phone referrals in 2025 (shrunk rate 40%). Other can codes, same table: Parks "GARBAGE:Can Needs Emptying" 11 of 283 (3.8%, amber); Transit "Overflowing Garbage Can" 1 of 192 (0.5%, green); River Valley Operations 0 of 23 (0.2% after shrinkage, green).
Headline numbers: 2026 test period Jan 1 to Nov 6, 2026, 179,139 phone referrals, 1,930 bounces. Flagging codes above 2% shows a prompt on 6.4% of referrals and catches 41% of bounces (800 of 1,930).
Line to land: we are not replacing the agent; we are telling the agent which picks are risky and telling the system which codes are broken.""")

# =====================================================================
# 2 THE ASK (answer first)
# =====================================================================
s = new_slide(d, "Mon 9:05 · Caller 4 is on the line · before the agent picks: our recommendation", START[1],
              foot=f"1 {OD}; Appendix A1-A2. 2 Using the October deck's decision tree ($1.02 per ask; asking halves wrong owners; $36.11 per bounce), annualised from 10.2 months of 2026. 3 Resident-days in the wrong queue avoided, range across tier settings. 4 CSD03148 (Sep 2, 2026): CRM end of life 2030.")
kicker(s, 0.5, 0.65, 8, "OUR RECOMMENDATION")
title(s, ["Approve a ", ("90-day start for Route Check", ), " inside the current CRM, then decide on phase two by day 180 on evidence, not on belief"])
cols = [
    ("WHAT IT IS", BLUE, [
        [R("A risk score on the code the agent picks, shown ", size=12), R("only on risky codes", size=12, bold=True), R(".", size=12)],
        [R("A daily bounce digest for team leads and a weekly code-fix queue with the owning areas.", size=12)],
        [R("It never routes a ticket by itself.", size=12, bold=True)]]),
    ("WHAT IT WILL DO", GREEN, [
        [R("Catch about ", size=12), R("4 in 10 bounces", size=12, bold=True), R(" before they happen, prompting on 1 in 16 referrals.", size=12), R("¹", size=12)],
        [R("Spare residents about ", size=12), R("1,200 to 2,900 days", size=12, bold=True), R(" a year in the wrong queue.", size=12), R("³", size=12)],
        [R("Build the routing record the 2030 CRM will need.", size=12), R("⁴", size=12)]]),
    ("WHAT IT WILL NOT DO", RED, [
        [R("Save real money. City savings are about ", size=12), R("$7K to $17K a year", size=12, bold=True), R(", roughly the agent time it costs.", size=12), R("²", size=12)],
        [R("Catch the other 6 in 10 bounces, or the misroutes areas fix quietly.", size=12)],
        [R("Replace agents, or judge them one by one.", size=12)]]),
]
for i, (h, c, paras) in enumerate(cols):
    x = 0.5 + i * 4.15
    card(s, x, 1.85, 3.95, 2.75, head=h, head_color=c, top=c, body=[{"runs": p, "after": 7} for p in paras])
# the ask band
rrect(s, 0.5, 4.8, 12.35, 1.1, NAVY, radius=0.08)
text(s, 0.7, 4.88, 2.2, 0.3, [[R("WHAT WE ASK TODAY", size=9.5, bold=True, color=YELLOW, spc=150)]])
asks = [("Data", "Read access to the CRM's reassignment log and first-code field"), ("People", "A 311 analyst, half-time, for 120 days; team leads for the digest"),
        ("Partners", "CSU 52 and three area program coordinators in co-design"), ("Decision", "An early look at day 120; go / no-go by day 180 against the gate on slide 13")]
for i, (a, b) in enumerate(asks):
    x = 0.7 + i * 3.05
    text(s, x, 5.18, 2.9, 0.7, [{"runs": [R(a + "  ", size=11, bold=True, color=YELLOW), R(b, size=10.5, color=WHITE)]}])
person(s, "lauren", 0.5, 6.05, 6.05, 0.85, "The dollars are small, so we will not sell this as savings. We sell it as residents' days and a record the City does not have.", qsize=10.5)
person(s, "rick", 6.8, 6.05, 6.05, 0.85, "Nothing here moves authority away from the agent or the areas. It gives the hand-off an owner.", qsize=10.5)
notes(s, """THE ASK, ANSWER FIRST (about 60 s). Presenter: Curtis.
Consultants lead with the recommendation. Say the ask in one sentence: approve the first 90 days inside the current CRM; take an early look at day 120; decide on phase two by day 180.
Why not decide at day 90: prompts only go live on day 61. Detecting a 30% drop needs about 3.6 months of pilot (80% power; Appendix A4), so the full gate lands near day 180. At day 120 (two months of pilot) we can stop for harm or go early if the drop is 40% or more. We say this up front so nobody expects proof at day 90.
Be honest about money: using the October decision tree (a 20-second ask valued at $1.02, asking halves the chance of a wrong owner, a bounce costs $36.11 with expected field visits), Route Check saves about $7K to $17K a year gross, against $3K to $14K of agent time. It is roughly break-even in City dollars. The case is residents' days (about 1,200 to 2,900 a year), hazard tickets, the learning loop, and the 2030 CRM replacement.
Resource ask (the analyst half-time and team-lead time) is our assumption, not a costed estimate; scope it with 311 in days 1 to 30.
ASSUMPTION TO CONFIRM: that the CRM can show a prompt and log an override by configuration rather than new development. If it cannot, phase one becomes a paper prompt list on the agent's second screen.""")

# =====================================================================
# 3 THE DECISION, REFINED
# =====================================================================
s = new_slide(d, "Mon 9:05 · the agent searches \"garbage can\" · what decision are we really improving?", START[2],
              foot=f"1 October deck, slide 4. 2 {OD}: 2026 phone referrals Jan 1-Nov 6 (179,139; 1,930 bounces); 2025 phone-referral bounces by code. 3 Glaser, Analytic Trees p. 20 (threshold); October deck slide 11. 4 Glaser, The Psychological Perspective 3.3; The Reassembly of Agency 1.1.")
kicker(s, 0.5, 0.65, 8, "THE CORE ANALYTIC DECISION · RESTATED AND REFINED")
title(s, ["Our diagnosis moved: the pick is ", ("usually right", ), ". The gap is knowing ", ("which picks are risky", ), ", and hearing about the misses"])
# left: october
card(s, 0.5, 1.85, 3.6, 3.05, head="OCTOBER", head_color=SLATE, body=[
    {"runs": [R("Which service code does a new 311 phone or web ticket get?", size=14, bold=True)], "after": 10},
    {"runs": [R("One agent, one pick, 1,917 codes, 665,225 times a year.", size=11.5, color=SLATE)], "after": 6},
    {"runs": [R("We showed that a wrong code costs residents days, and that nothing tells the agent.", size=11.5, color=SLATE)]}])
arrow(s, 4.2, 3.15, 0.45, 0.45, ORANGE)
# right: two linked decisions
rrect(s, 4.75, 1.85, 8.1, 3.05, WHITE, radius=0.04)
rect(s, 4.75, 1.85, 8.1, 0.06, RED)
text(s, 4.95, 1.98, 7.5, 0.27, [[R("DECEMBER · TWO LINKED DECISIONS", size=9.5, bold=True, color=RED, spc=150)]])
for i, (num, who, q, detail) in enumerate([
    ("1", "PER TICKET · LIVE · THE AGENT", "Route on the code I picked, or check who owns it first?",
     "Asking pays only when a code's bounce chance is above 5.6% (the October decision tree). Today nothing tells the agent that chance."),
    ("2", "PER CODE · WEEKLY · 311 WITH THE OWNING AREA", "Keep, reword, merge or retire this code?",
     "A code that keeps bouncing is a code-set problem, not an agent problem. Today no one owns that fix.")]):
    x = 4.95 + i * 3.95
    c = rect(s, x, 2.36, 0.42, 0.42, NAVY, shape=MSO_SHAPE.OVAL)
    text(s, x, 2.36, 0.42, 0.42, [{"runs": [R(num, size=14, bold=True, color=WHITE)], "align": "c"}], anchor="middle", shape=c, margin=(0, 0, 0, 0))
    text(s, x + 0.52, 2.33, 3.2, 0.5, [[R(who, size=8.5, bold=True, color=BLUE, spc=100)]])
    text(s, x, 2.88, 3.75, 0.85, [[R(q, size=14, bold=True)]])
    text(s, x, 3.72, 3.75, 1.1, [[R(detail, size=11, color=SLATE)]])
# evidence strip
stats = [("98.9%", "of 2026 phone referrals did not bounce", "VERIFIED"), ("37%", "of 2025 phone-referral bounces sit on just 10 codes", "VERIFIED"),
         ("233 of 1,116", "referral codes bounced at all in 2025", "VERIFIED"), ("50 of 116", "bounced on the picked can code, 2025", "VERIFIED")]
for i, (n, t, lab) in enumerate(stats):
    x = 0.5 + i * 3.1
    rrect(s, x, 5.05, 2.95, 0.95, WHITE, radius=0.08)
    text(s, x + 0.15, 5.1, 2.7, 0.45, [[R(n, size=20, bold=True, color=NAVY)]])
    text(s, x + 0.15, 5.52, 2.7, 0.45, [[R(t, size=9.5, color=SLATE)]])
person(s, "lauren", 0.5, 6.1, 4.0, 0.85, "Concentrated misses mean a targeted check beats a check on every call.", "RATIONAL", qsize=10)
person(s, "nav", 4.67, 6.1, 4.0, 0.85, "Agents can't learn from a miss they never hear about.", "PSYCHOLOGICAL", qsize=10)
person(s, "rick", 8.84, 6.1, 4.0, 0.85, "311 picks the code; areas own the result. Decision 2 gives the hand-off an owner.", "POLITICAL", qsize=10)
notes(s, """THE DECISION, REFINED (about 75 s). Presenter: Lauren.
In October we framed the decision as "which service code does a new ticket get". The data moved us. Most picks are right: 98.9% of 2026 phone referrals did not bounce. The misses are concentrated: the top 10 codes carry 37% of 2025 phone-referral bounces, the top 25 carry 54%, and only 233 of 1,116 referral codes bounced at all.
So the decision worth supporting is not "pick the code for the agent". It is two linked decisions:
1. Per ticket, live, by the agent: route now, or spend about 20 seconds checking ownership first. Our October decision tree said asking pays only when the code's bounce probability is above about 5.6%. The agent has no way to know that probability today. Route Check supplies it.
2. Per code, weekly, by 311 with the owning area: keep, reword, merge or retire the code. This is the LEARN step that was missing in October (Reassembly six activities).
Course link: decision tree threshold (Analytic Trees p. 20); feedback (Psych. Perspective 3.3; Kahneman and Klein 2009); authority vs accountability (Reassembly 1.1).""")

# =====================================================================
# 4 THE SYSTEM ON ONE PAGE
# =====================================================================
s = new_slide(d, "Mon 9:06 · the agent picks a code · Route Check scores it before the ticket routes", START[3],
              foot="1 Risk table: each code's bounce rate over the last 12 months, shrunk toward the average for small samples (empirical Bayes); refreshed weekly. 2 Sibling map: codes with overlapping wording owned by another area; draft of 301 codes from 2025 (sibling_codes_2025.csv). 3 Six activities: Glaser, The Reassembly of Agency s. 1.3.")
kicker(s, 0.5, 0.65, 8, "THE PROPOSED ALGORITHMIC ROUTINE · ROUTE CHECK")
title(s, ["Route Check ", ("takes in the agent's pick", ), ", puts out a prompt only when the pick is risky, and ", ("sends every miss back", ), " to someone who can fix it"])
# columns: TAKES IN -> SCORES -> PUTS OUT -> WHO ACTS
colx = [0.5, 3.55, 6.45, 9.75]
heads = ["TAKES IN", "SCORES", "PUTS OUT", "WHO ACTS"]
for x, h in zip(colx, heads):
    kicker(s, x, 1.8, 2.8, h, color=NAVY, size=9.5)
ins = [("The code the agent picked", "on every phone referral"), ("Code risk table", "12-month bounce rate per code, weekly¹"),
       ("Sibling map", "look-alike codes owned elsewhere²"), ("Phase two: address and notes", "asset layers; agent's typed words")]
for i, (a, b) in enumerate(ins):
    y = 2.1 + i * 0.66
    rrect(s, 0.5, y, 2.7, 0.58, WHITE if i < 3 else "EEF3F7", LINE if i == 3 else None, radius=0.1)
    text(s, 0.62, y + 0.04, 2.5, 0.52, [{"runs": [R(a, size=10.5, bold=True, color=NAVY if i < 3 else SLATE)]}, {"runs": [R(b, size=8.5, color=SLATE)]}])
arrow(s, 3.25, 3.0, 0.25, 0.35)
rrect(s, 3.55, 2.1, 2.6, 2.6, NAVY, radius=0.06)
text(s, 3.7, 2.2, 2.35, 2.45, [
    {"runs": [R("A lookup, not a black box", size=12.5, bold=True, color=YELLOW)], "after": 6},
    {"runs": [R("risk = (bounces + prior) ÷ (referrals + prior)", size=9.5, color=WHITE, font="Consolas")], "after": 6},
    {"runs": [R("Explainable in one sentence: ", size=10, color="C2D3E0"), R('"This code bounced 50 of 116 times last year."', size=10, bold=True, color=WHITE)], "after": 6},
    {"runs": [R("New codes start amber for 90 days.", size=10, color="C2D3E0")]}])
arrow(s, 6.18, 3.0, 0.25, 0.35)
tiers = [("GREEN · under 2%", "~94% of referrals", "Nothing shown. Route as today.", GREEN, LGREEN),
         ("AMBER · 2% to 5.6%", "~5%", "Show the look-alike codes and who owns each. One click to confirm or switch.", ORANGE, LORANGE),
         ("RED · above 5.6%", "~1%", "Ask one ownership question, then pick.", RED, LRED)]
for i, (a, b, c, col, f) in enumerate(tiers):
    y = 2.1 + i * 0.88
    rrect(s, 6.45, y, 3.0, 0.8, f, col, lw=1.25, radius=0.1)
    text(s, 6.55, y + 0.03, 2.85, 0.75, [{"runs": [R(a, size=9, bold=True, color=col, spc=80), R("  " + b, size=8.5, color=SLATE)]}, {"runs": [R(c, size=9.5, color=NAVY)]}])
arrow(s, 9.48, 3.0, 0.25, 0.35)
rrect(s, 9.75, 2.1, 3.1, 2.6, WHITE, radius=0.06)
text(s, 9.9, 2.18, 2.85, 2.5, [
    {"runs": [R("The agent", size=12.5, bold=True)], "after": 2},
    {"runs": [R("hears the caller, answers the prompt, keeps the final pick. Overrides take one click and are logged.", size=10, color=SLATE)], "after": 8},
    {"runs": [R("No auto-routing", size=12.5, bold=True, color=RED)], "after": 2},
    {"runs": [R("Only the agent hears the caller. A wrong automatic route would have no one to catch it.", size=10, color=SLATE)]}])
# learn loop band
rrect(s, 0.5, 4.88, 12.35, 1.95, "EAF1F6", MID, lw=1, radius=0.06)
text(s, 0.7, 4.95, 6, 0.28, [[R("THE LOOP · WHAT HAPPENS AFTER A MISS", size=9.5, bold=True, color=MID, spc=150)]])
loop = [("A bounce", "The receiving area closes it \"311 Redirecting\"", "DAY 0-3"), ("Daily digest", "Team lead sees their team's bounces; coaching only", "NEXT DAY"),
        ("Weekly fix queue", "311 and the owning area keep, reword, merge or retire codes above 5.6%", "WEEKLY"),
        ("Weekly refresh", "311 analytics recomputes the risk table; watches drift", "WEEKLY")]
for i, (a, b, c) in enumerate(loop):
    x = 0.7 + i * 3.05
    rrect(s, x, 5.3, 2.7, 1.35, WHITE, radius=0.08)
    text(s, x + 0.12, 5.35, 2.5, 1.25, [{"runs": [R(c, size=7.5, bold=True, color=ORANGE, spc=100)]}, {"runs": [R(a, size=11.5, bold=True)]}, {"runs": [R(b, size=9.5, color=SLATE)]}])
    if i < 3:
        arrow(s, x + 2.74, 5.82, 0.27, 0.3, MID)
text(s, 7.2, 4.95, 5.5, 0.28, [{"runs": [R("Fills the two gaps from October: AUTHORIZE and LEARN³", size=9, bold=True, color=RED)], "align": "r"}])
notes(s, """THE SYSTEM ON ONE PAGE (about 75 s). Presenter: Curtis or Lauren.
Walk it left to right, then the loop.
Takes in: the code the agent picked; the code risk table (each code's bounce rate over the last 12 months, shrunk toward the average for rare codes, recomputed weekly from CRM closures); the sibling map (codes with overlapping wording owned by another area; our draft has 301 codes). Phase two adds the ticket address matched to asset layers, and the agent's typed notes.
Scores: a lookup. We tried a logistic regression with more features; it did worse out of time (AUC 0.69 vs 0.82). Simple wins and is explainable.
Puts out: green (nothing shown, about 94% of referrals), amber (look-alike codes and owners, one click, about 5%), red (one ownership question, about 1%). The 5.6% red cut is the October decision tree's break-even.
Who acts: the agent, always. Route Check never routes a ticket.
The loop: a bounce goes to the team lead in a daily digest (45% of 2025 phone bounces closed within 1 day, 63% within 3, so most arrive while the call is remembered); codes that stay above 5.6% go to a weekly fix queue run by 311 with the owning area; 311 analytics refreshes the table weekly.
Course link: Reassembly six activities (notice, record, propose, AUTHORIZE, carry out, LEARN); October showed AUTHORIZE and LEARN were missing.""")

# =====================================================================
# 5 WHAT THE AGENT SEES
# =====================================================================
s = new_slide(d, "Mon 9:06 · the screen turns red · the agent asks one question", START[4],
              foot=f"1 {OD}: tier shares of 2026 phone referrals using 2025 risk scores. 2 October deck slide 11: asking pays when p > 2 x $1.02 / $36.11 = 5.6%. 3 Glaser, The Psychological Perspective 3.2. 4 Our proposed refinement, to test in shadow mode: 61 of 91 red codes had fewer than 20 referrals in 2025.")
kicker(s, 0.5, 0.65, 8, "WHAT THE AGENT SEES · THREE TIERS")
title(s, ["The prompt ", ("interrupts the fast pick only where it is likely wrong", ), ": nothing on 94% of referrals, one click or one question on the rest"])
tiers = [
    ("GREEN", "Risk under 2%", "93.6%", "of 2026 phone referrals", "Nothing appears. The agent routes as today, at today's speed.", GREEN, LGREEN, "Prune City Tree · Forestry · 1.7%"),
    ("AMBER", "Risk 2% to 5.6%", "5.2%", "of referrals · 24% of bounces", "The look-alike codes appear with their owners. One click confirms or switches.", ORANGE, LORANGE, "LITTER:Road · Roadway · 5.0% → siblings shown"),
    ("RED", "Risk above 5.6%", "1.2%", "of referrals · 18% of bounces", "One ownership question appears. The agent asks, then picks.", RED, LRED, '"Is it in the park, at a bus stop, or by a City building?"'),
]
for i, (t, rule, share, sub, what, col, f, ex) in enumerate(tiers):
    x = 0.5 + i * 4.15
    rrect(s, x, 1.85, 3.95, 3.25, f, col, lw=1.5, radius=0.05)
    text(s, x + 0.2, 1.95, 3.6, 0.3, [[R(t, size=13, bold=True, color=col, spc=200), R("   " + rule, size=10, color=SLATE)]])
    text(s, x + 0.2, 2.3, 3.6, 0.6, [[R(share, size=30, bold=True, color=NAVY)]])
    text(s, x + 0.2, 2.92, 3.6, 0.3, [[R(sub, size=9.5, color=SLATE)]])
    text(s, x + 0.2, 3.3, 3.6, 0.9, [[R(what, size=12)]])
    rrect(s, x + 0.2, 4.3, 3.55, 0.62, WHITE, radius=0.12)
    text(s, x + 0.3, 4.32, 3.35, 0.58, [[R("EXAMPLE  ", size=7, bold=True, color=col, spc=100), R(ex, size=9, color=NAVY)]], anchor="middle")
# rules
card(s, 0.5, 5.25, 7.45, 1.65, head="RULES THAT KEEP IT HONEST", body=[
    {"runs": [R("Cut-offs come from the analysis, not taste: ", size=10.5, bold=True), R("red starts at 5.6%, the October decision tree's break-even.²", size=10.5)], "after": 3},
    {"runs": [R("New codes start amber for 90 days: ", size=10.5, bold=True), R("8% of 2026 bounces came from codes unseen in 2025.", size=10.5)], "after": 3},
    {"runs": [R("Small samples cap at amber: ", size=10.5, bold=True), R("one bounce on five tickets should not trigger a question.⁴", size=10.5)]}])
person(s, "nav", 8.15, 5.25, 4.7, 1.65, "A prompt on every call becomes wallpaper and I stop reading it. A prompt on one call in sixteen tells me something is different about this one. That's when my slow thinking should switch on.³", "PSYCHOLOGICAL", qsize=10.5)
notes(s, """WHAT THE AGENT SEES (about 60 s). Presenter: Nav.
Tier shares are on 2026 phone referrals (Jan 1 to Nov 6), scored with 2025 risk: green 93.6%, amber 5.2% (catches 459 of 1,930 bounces, 24%), red 1.2% (catches 341, 18%). Amber plus red: 6.4% flagged, 41% caught; bounce rate inside the flagged set 7.0% vs 1.08% overall.
Examples: Prune City Tree (Forestry) 1,069 referrals, 18 bounces in 2025, green. LITTER:Road (Roadway Maintenance) 2,089 referrals, 104 bounces, 5.0%, amber, the single biggest bounce code. The red question is the can example from the cover.
Psychology: System 1 produces "garbage can" and a can code; System 2 "can examine an impression, and it can also defend one" (Psych. Perspective 3.2, p. 5). The prompt is rare on purpose so it switches System 2 on where the evidence says the first impression is often wrong. Too many prompts trains agents to click through them (automation bias / alert fatigue; Parasuraman and Manzey 2010).
Small-sample cap: this is OUR refinement and is not in the backtest. 61 of the 91 codes that score red had fewer than 20 phone referrals in 2025, so one bounce can make a rare code red. We cap those at amber and test the effect in shadow mode.""")

# =====================================================================
# 6 EVIDENCE
# =====================================================================
s = new_slide(d, "Mon 9:06 · would the red flag have been right? · ten years of tickets say yes", START[5],
              foot=f"1 {OD}; 2016-2022 from the City's yearly 311 datasets (deduplicated by Row ID). Each year scored only with the year before (out-of-time test). AUC: chance a random bounced ticket scores above a random non-bounced one (0.5 = coin flip). 2 Appendix A2.")
kicker(s, 0.5, 0.65, 8, "DOES IT WORK? · BACKTEST ON TICKETS THE SCORE NEVER SAW")
title(s, ["Last year's code bounce rates rank next year's tickets well ", ("every year since 2017", ), "; a fancier model did worse"])
# chart AUC
cd = CategoryChartData()
yrs = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"]
auc = [0.861, 0.907, 0.902, 0.903, 0.920, 0.911, 0.932, 0.932, 0.895, 0.818]
cd.categories = yrs
cd.add_series("AUC, scored with prior year", auc)
rrect(s, 0.5, 1.85, 6.6, 4.2, WHITE, radius=0.04)
text(s, 0.7, 1.95, 6.2, 0.3, [[R("HOW WELL THE SCORE RANKS NEXT YEAR'S TICKETS (AUC)¹", size=9.5, bold=True, color=BLUE, spc=120)]])
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.65), Inches(2.25), Inches(6.3), Inches(3.3), cd)
ch = gf.chart
ch.has_legend = False
ch.has_title = False
va = ch.value_axis; va.minimum_scale = 0.5; va.maximum_scale = 1.0; va.major_unit = 0.1
va.has_major_gridlines = True; va.major_gridlines.format.line.color.rgb = rgb("E3EAF0")
va.tick_labels.font.size = Pt(9); va.tick_labels.font.color.rgb = rgb(SLATE); va.tick_labels.number_format = '0.0'; va.tick_labels.number_format_is_linked = False
va.format.line.fill.background()
ca = ch.category_axis; ca.tick_labels.font.size = Pt(9); ca.tick_labels.font.color.rgb = rgb(SLATE)
pl = ch.plots[0]; pl.gap_width = 60
pl.has_data_labels = True; dl = pl.data_labels; dl.font.size = Pt(8.5); dl.font.color.rgb = rgb(NAVY); dl.number_format = '0.00'; dl.number_format_is_linked = False; dl.position = XL_LABEL_POSITION.OUTSIDE_END
ser = pl.series[0]
for i, pt in enumerate(ser.points):
    pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(RED if i == 9 else MID)
text(s, 0.7, 5.55, 6.3, 0.45, [[R("2026 is the weakest year because eight areas began recording bounces; 0.82 is still strong. Three years of history did no better than one.", size=9, color=SLATE)]])
# right: flag table
text(s, 7.35, 1.85, 5.5, 0.3, [[R("WHERE TO SET THE FLAG · 2026 TEST", size=9.5, bold=True, color=BLUE, spc=100)]])
table(s, 7.35, 2.2, 5.5, 1.9, [
    ["Flag codes with risk", "Referrals flagged", "Bounces caught", "Bounce rate if flagged"],
    ["above 5.6% (red only)", "1.2%", "18%", "16.2%"],
    [[R("above 2% (red + amber)", bold=True)], [R("6.4%", bold=True)], [R("41%", bold=True, color=RED)], [R("7.0%", bold=True)]],
    ["above 1%", "12.0%", "50%", "4.4%"],
    ["no flag (today)", "0%", "0%", "1.08% overall"]],
    colw=[1.75, 1.15, 1.15, 1.45], sizes=[9.5, 9.5, 9.5, 9.5], fills={(2, None): "FFF4E8"}, row_h=0.36)
card(s, 7.35, 4.25, 5.5, 1.8, head="WHAT WE TRIED THAT DID NOT HELP", head_color=SLATE, body=[
    {"runs": [R("More features: ", size=10.5, bold=True), R("a regression adding app bounce rate, area and sibling flags scored AUC 0.69 out of time, worse than the lookup's 0.82.", size=10.5)], "after": 4},
    {"runs": [R("Neighbourhood: ", size=10.5, bold=True), R("predicting the can owner from neighbourhood was right 62.8% of the time vs 63.9% for always guessing the biggest area.", size=10.5)], "after": 4},
    {"runs": [R("Longer history: ", size=10.5, bold=True), R("three years of data matched one year within 0.01 AUC.", size=10.5)]}])
person(s, "lauren", 0.5, 6.15, 12.35, 0.78, "41% caught means 59% missed. Route Check is triage, not a cure. That is why the loop on slide 4 matters as much as the prompt.", "RATIONAL", qsize=10.5)
notes(s, """EVIDENCE (about 75 s). Presenter: Lauren.
Method: for each test year, every code's bounce rate is computed from the year before only, shrunk toward the average (beta prior, mean 0.51%, weight about 10 tickets), then used to rank that year's phone referrals. AUC is the chance that a randomly chosen bounced ticket scores higher than a randomly chosen non-bounced one. 0.5 is a coin flip.
Results (stability_backtest_2017_2026.csv): 2017 0.86, 2018 0.91, 2019 0.90, 2020 0.90, 2021 0.92, 2022 0.91, 2023 0.93, 2024 0.93, 2025 0.90, 2026 0.82. Share of bounces caught at a 2% flag ranges 28% to 64% by year.
Why 2026 is weaker: eight areas that rarely recorded bounces began in 2026, and 8% of 2026 bounces were on codes unseen in 2025.
Flag table (2026 test): above 5.6% flags 2,100 tickets (1.2%) and catches 341 bounces (18%); above 2% flags 11,408 (6.4%) and catches 800 (41%); above 1% flags 21,560 (12%) and catches 956 (50%).
Dead ends we report on purpose: the richer model (AUC 0.69) and neighbourhood owner prediction (62.8% vs 63.9% baseline). Course link: overfitting (Psych. Perspective; Session 3), and "start simple".
Caveat: the label is a recorded bounce. Quiet misroutes and wrong answers on resolved calls are not in it. Slide 9 covers how to build a better label.""")

# =====================================================================
# 7 AUTOMATE VS HUMAN
# =====================================================================
s = new_slide(d, "Mon 9:06 · the agent overrides the prompt · who decides what?", START[6],
              foot="1 Glaser, The Reassembly of Agency (SEM 620, 2026), s. 1.1 and Session 1: who can access, change, stop and correct an agent. 2 Northfield Credit Union case (Session 1): a score with a 1-in-20 override, judged by a throughput metric. 3 Ironstone case (Session 7). 4 Glaser, Sloan and Knight (2025): AI as assistant, analyst, coach.")
kicker(s, 0.5, 0.65, 8, "WHAT WE AUTOMATE · WHAT WE LEAVE TO PEOPLE · AND WHY")
title(s, ["Automate ", ("the counting and the reminding", ), "; leave ", ("the pick, the code fixes and the coaching", ), " to people who hear the caller and own the outcome"])
table(s, 0.5, 1.85, 7.6, 3.55, [
    ["Automate", "Leave to a person", "Why"],
    ["Score every pick; choose the tier; show look-alike codes", "The final code (agent)", "Only the agent hears the caller. An automatic wrong route has no one to catch it, and Hashemi (2022) shows text models still miss about 1 in 6."],
    ["Build the daily digest and the weekly fix queue", "Retiring, merging or rewording codes (311 + area)", "Areas already sign off scripts. Changing the code set moves work between budgets: a political choice, not a statistical one."],
    ["Weekly refresh; drift and recording alerts", "Coaching (team lead)", "Feedback changes behaviour when it comes from a person the agent trusts, not from a dashboard."],
    ["Log every override with the outcome", "Whether the pilot continues (311 director)", "Someone accountable must be able to stop it."]],
    colw=[2.35, 2.05, 3.2], sizes=[10, 10, 9.5], row_h=0.6)
# four questions
rrect(s, 8.3, 1.85, 4.55, 3.55, WHITE, radius=0.04)
text(s, 8.45, 1.95, 4.3, 0.3, [[R("THE FOUR QUESTIONS FOR ANY AGENT¹", size=9.5, bold=True, color=BLUE, spc=120)]])
qs = [("ACCESS", "Agents see why a code is flagged; team leads see only their own team's bounces."),
      ("CHANGE", "Cut-offs and the sibling map change only through the weekly fix queue, with area sign-off."),
      ("STOP", "The 311 director can switch it off; it switches off by itself if handle time rises more than 10 s."),
      ("CORRECT", "One-click override, logged; overrides that turn out right lower the code's score.")]
for i, (a, b) in enumerate(qs):
    y = 2.3 + i * 0.75
    text(s, 8.45, y, 1.0, 0.3, [[R(a, size=9, bold=True, color=RED, spc=100)]])
    text(s, 9.45, y, 3.3, 0.72, [[R(b, size=10)]])
person(s, "rick", 0.5, 5.55, 4.05, 1.35, "Northfield's override was allowed on paper, but a throughput metric made it costly. We judge handle time by team, never by agent, and no one is marked down for an override.²", "POLITICAL", qsize=9.5)
person(s, "nav", 4.67, 5.55, 4.05, 1.35, "When Ironstone replaced Wes Harlan, his tacit calls went with him. Agents know that cans at transit centres are ETS. The override log and fix queue capture that.³", "PSYCHOLOGICAL", qsize=9.5)
person(s, "lauren", 8.84, 5.55, 4.01, 1.35, "Route Check is an analyst, not a decider: it adds evidence to the agent's pick. Phase two adds an assistant that suggests three codes.⁴", "RATIONAL", qsize=9.5)
notes(s, """AUTOMATE VS LEAVE TO PEOPLE (about 75 s). Presenter: Rick.
The rubric asks us to be explicit. Automate what machines do well and people do badly: counting bounces per code, remembering which codes are risky, assembling a digest, spotting drift. Leave to people what needs hearing the caller (the pick), trading off work between budgets (code fixes), trust (coaching) and accountability (stopping the pilot).
Why not auto-route: the best published text classifier for 311 requests reached a bit over 83% accuracy (Hashemi 2022). On 665,225 phone tickets, a 17% error rate would be far worse than today's recorded 1% bounce rate on referrals, and no one would hear the caller to catch it. The City's own app AI has no published accuracy.
Four agent questions (Session 1, Reassembly): access, change, stop, correct, answered on the slide.
Northfield (Session 1 case): a score plus a 1-in-20 override; the throughput metric quietly made overriding expensive. Our guardrail: handle time measured at team level, overrides never penalised, agreed in writing with CSU 52.
Ironstone (Session 7): tacit readiness knowledge was lost when the system replaced the dispatcher. We keep the agent's knowledge in the loop: override reasons feed the sibling map and the fix queue.
Assistant / analyst / coach (Glaser, Sloan and Knight 2025): Route Check is the analyst; humans do the coaching; phase two's text suggestions are the assistant.""")

# =====================================================================
# 8 WHEN IT IS WRONG
# =====================================================================
s = new_slide(d, "Tue · the prompt was wrong · what happens next?", START[7],
              foot=f"1 {OD}: 39% of the 2026 rise in phone bounces came from eight areas that began recording (October deck slide 7). 2 Klein (2007), Performing a project premortem, HBR. 3 Lindebaum et al. (2022), as assigned in SEM 620 Session 9; Robodebt simulation. 4 Parasuraman and Manzey (2010), Human Factors 52(3).")
kicker(s, 0.5, 0.65, 8, "WHEN IT IS WRONG · A PREMORTEM²")
title(s, ["It is December 2027 and Route Check has failed. ", ("Here are the six likeliest reasons", ), ", and what we built in for each"])
fails = [
    ("FALSE ALARM", "A green-tier pick gets flagged", "Costs about 20 seconds. One-click override; the override and its outcome feed the next refresh.", "Override rate by code", GREEN),
    ("MISSED BOUNCE", "6 in 10 bounces are on unflagged codes", "Same as today, except the bounce now reaches the team lead next day and the code enters the fix queue.", "Bounces returned within 24 h", ORANGE),
    ("DRIFT", "An area starts or stops recording bounces¹", "Track the recording rate per area; judge the pilot only on areas that always recorded.", "Recording rate by area", ORANGE),
    ("RUBBER-STAMPING", "Agents click through every prompt⁴", "If agents accept more than 95%, audit a sample. If they override more than 80%, the tier is noise: retune it.", "Override rate 20% to 80%", RED),
    ("SURVEILLANCE", "The digest becomes a ranking of agents", "Written agreement with CSU 52: team-level data, coaching only, no individual targets.", "Grievances; agent survey", RED),
    ("PROXY DRIFT", "Areas stop recording bounces to look good³", "Never make bounces an area target. Pair them with a QA sample of 200 resolved calls a month and a re-route log.", "QA sample vs bounce trend", RED),
]
for i, (h, what, resp, watch, col) in enumerate(fails):
    x = 0.5 + (i % 3) * 4.15; y = 1.85 + (i // 3) * 2.15
    rrect(s, x, y, 3.95, 2.0, WHITE, radius=0.05)
    rect(s, x, y, 0.07, 2.0, col)
    text(s, x + 0.22, y + 0.1, 3.6, 1.85, [
        {"runs": [R(h, size=9.5, bold=True, color=col, spc=150)], "after": 2},
        {"runs": [R(what, size=13.5, bold=True)], "after": 6},
        {"runs": [R(resp, size=11.5, color=NAVY)], "after": 6},
        {"runs": [R("WATCH  ", size=8, bold=True, color=SLATE, spc=100), R(watch, size=10, color=SLATE)]}])
person(s, "rick", 0.5, 6.15, 12.35, 0.78, "The most dangerous failure is the quiet one: once a bounce count is on a scorecard, someone has a reason to stop recording bounces. Robodebt is what a trusted proxy looks like when no one checks it.", "POLITICAL", qsize=10.5)
notes(s, """WHEN IT IS WRONG (about 60 s). Presenter: Rick or Nav.
Framed as a premortem (Klein 2007; Session 2): imagine it failed, then list why. Six failure modes and the guardrail for each.
False alarm: 20 seconds of agent time; override logged. Missed bounce: same as today but now it comes back through the digest and fix queue. Drift: 39% of the 2026 rise in phone bounces was eight areas starting to record, so we track recording per area and evaluate only on always-recording areas. Rubber-stamping: automation bias (Parasuraman and Manzey 2010); acceptance above 95% triggers an audit, override above 80% means the tier is noise. Surveillance: CSU 52 agreement, team-level only. Proxy drift: the bounce is a proxy for a misroute; if bounces become an area KPI, areas can stop recording them (Goodhart; Session 9 Robodebt simulation and Lindebaum et al. 2022 on values withering under algorithmic rule). We pair the bounce count with an independent QA sample and a logged re-route link.
The worst case is not a wrong prompt; it is a trusted number that has stopped meaning what it used to.""")

# =====================================================================
# 9 DATA
# =====================================================================
s = new_slide(d, "Wed · the area closes the ticket · what record does that leave?", START[8],
              foot=f"1 {OD}: 26 columns; no address, no agent, no free text; neighbourhood centroid only, missing on 38% of 2026 phone referrals. 2 Inferred from OCA (2023) and CSD03148; to confirm with 311. 3 Matching bounces to a later ticket nearby found 19.3% vs 16.8% by chance. 4 Parks (gdd9-eqv9), ETS GTFS stops (4vt2-8zrq).")
kicker(s, 0.5, 0.65, 8, "HOW DATA WOULD BE CONSTRUCTED AND LEVERAGED")
title(s, ["Public data is enough to build version one. The learning loop needs ", ("five records nobody keeps yet", ), ", and small new habits from agents, area staff and 311"])
G, A, Rr = GREEN, ORANGE, RED
rows = [
    ["Data", "Status today", "Used for", "Who has to change"],
    ["Code, area, channel, closure label, created and closed times", [R("EXISTS · public¹", bold=True, color=G)], "Risk table, backtest, tiers", "No one"],
    ["Ticket address, agent ID, handle time, typed notes", [R("EXISTS · inside CRM²", bold=True, color=G)], "Digest by team; phase-two owner hints and text model", "311: a data agreement"],
    ["Parks and transit stop locations", [R("EXISTS · public⁴", bold=True, color=G)], "Red-tier question: whose asset is at this address?", "No one"],
    ["Link from a bounced ticket to its re-route (first code, final code)", [R("MISSING · cannot rebuild³", bold=True, color=Rr)], "The label every later model learns from", "Area staff: log the code it should have been"],
    ["A closure reason recorded the same way in every area", [R("PARTIAL · 8 areas began 2026", bold=True, color=A)], "A fair comparison across areas", "Area staff: one required field"],
    ["Sibling map of look-alike codes", [R("DRAFT · 301 codes", bold=True, color=A)], "Amber prompt", "311 knowledge staff and areas confirm it"],
    ["Code accuracy on calls resolved on the phone (473,564 in 2025)", [R("MISSING", bold=True, color=Rr)], "The stake's biggest assumption", "311 QA: code a sample of 200 a month"],
    ["Override log: prompt shown, agent's choice, outcome", [R("MISSING · comes with Route Check", bold=True, color=Rr)], "Trust, drift, retuning", "Agents: one click"],
]
table(s, 0.5, 1.85, 8.65, 4.3, rows, colw=[2.9, 1.95, 2.0, 1.8], sizes=[9.5, 8.5, 9, 9], row_h=0.46)
card(s, 9.35, 1.85, 3.5, 2.6, head="DATA IS BUILT, NOT FOUND", head_color=BLUE, body=[
    {"runs": [R("Today the only routing signal is a closure label set by the receiving area, and only when it chooses to use it.", size=10.5)], "after": 6},
    {"runs": [R("The City's headline, 98.7% resolved on initial contact, measures the call, not the route: the same trap as the 10-1-24 reply target in the SBS case.", size=10.5)]}])
card(s, 9.35, 4.6, 3.5, 1.55, head="LEVERAGE", head_color=GREEN, body=[
    {"runs": [R("Every row in red is also a requirement for the 2030 CRM. Building them now gives the new system three years of clean routing labels on day one.", size=10.5)]}])
person(s, "nav", 0.5, 6.25, 12.35, 0.7, "The re-route link is the one that matters most: it turns a bounce from \"not mine\" into \"it should have been this code\", which is something an agent, and a model, can learn from.", "PSYCHOLOGICAL", qsize=10.5)
notes(s, """DATA (about 75 s). Presenter: Nav or Lauren.
What exists publicly (311 Requests, 26 columns): code (service area + category + description), channel, referral type, closure label, created and closed timestamps, neighbourhood and ward. No address, no agent ID, no free text; neighbourhood is a centroid and is missing on 38% of 2026 phone referrals.
What exists inside the CRM (inferred, to confirm): ticket address, agent ID, handle time, typed notes.
What does not exist: (1) a link from a bounced ticket to its re-route. We tried to rebuild it by matching each bounce to a later ticket in the same neighbourhood, another area, within 72 hours: 19.3% matched vs 16.8% by chance, so it cannot be rebuilt; it must be logged. (2) Consistent bounce recording: eight areas only began in 2026. (3) The sibling map: our draft from wording overlap has 301 codes; codes with a look-alike owned elsewhere bounced at 0.76% vs 0.48% (1.6x). (4) Accuracy on resolved calls: a QA sample of about 200 a month would replace the stake's biggest assumption. (5) The override log, which Route Check creates.
Who changes behaviour: area staff (one required field: closure reason, and the code it should have been); agents (one click); 311 QA (a monthly sample); knowledge staff with areas (confirm siblings).
Course link: Session 6, data is constructed; a metric built slightly wrong rewards the wrong behaviour (SBS Ivey case W35309: the 10-1-24 target measured the reply, not the fix). 98.7% "resolved on initial contact" is the 311 version.""")

# =====================================================================
# 10 THE CASE
# =====================================================================
s = new_slide(d, "Thu · Caller 4 does not call again · what was that worth?", START[9],
              foot="1 Using the October decision tree: $1.02 per 20-second ask; asking halves wrong owners; $36.11 per bounce incl. expected field visits; annualised from 10.2 months of 2026. 2 October deck slide 14: 231 hazard-type phone bounces, 2,915 days in the wrong queue, 2025. Alberta MGA s. 532. 3 CSD03148 (Sep 2, 2026).")
kicker(s, 0.5, 0.65, 8, "THE BUSINESS CASE · HONEST ABOUT THE DOLLARS")
title(s, ["In City dollars Route Check is ", ("roughly break-even", ), ". It is worth doing for residents' time, hazard tickets, and the 2030 CRM"])
card(s, 0.5, 1.85, 4.0, 2.55, head="CITY DOLLARS · A YEAR¹", head_color=SLATE, top=SLATE, body=[
    {"runs": [R("$7K to $17K", size=26, bold=True)], "after": 0},
    {"runs": [R("gross savings from fewer bounces", size=10.5, color=SLATE)], "after": 8},
    {"runs": [R("$3K to $14K", size=20, bold=True, color=SLATE)], "after": 0},
    {"runs": [R("agent time spent on prompts", size=10.5, color=SLATE)]}])
card(s, 4.67, 1.85, 4.0, 2.55, head="RESIDENTS · A YEAR", head_color=GREEN, top=GREEN, body=[
    {"runs": [R("1,200 to 2,900", size=26, bold=True)], "after": 0},
    {"runs": [R("days not spent in the wrong queue", size=10.5, color=SLATE)], "after": 8},
    {"runs": [R("2,915 days", size=20, bold=True, color=RED)], "after": 0},
    {"runs": [R("hazard tickets sat misrouted in 2025: roads, sidewalks, signals²", size=10.5, color=SLATE)]}])
card(s, 8.84, 1.85, 4.0, 2.55, head="THE 2030 CRM · OPTION VALUE", head_color=BLUE, top=BLUE, body=[
    {"runs": [R("3 years", size=26, bold=True)], "after": 0},
    {"runs": [R("of routing labels ready when the CRM is replaced³", size=10.5, color=SLATE)], "after": 8},
    {"runs": [R("Waiting is not free: every year without a re-route link is a year of labels the new system can never train on.", size=10.5)]}])
# future->now strip
rrect(s, 0.5, 4.55, 12.35, 1.45, WHITE, radius=0.05)
text(s, 0.7, 4.62, 8, 0.28, [[R("WORKING BACK FROM 2030 · FUTURE → NOW", size=9.5, bold=True, color=BLUE, spc=150)]])
steps = [("2026-27", "Route Check pilot; re-route log and closure reason in the busiest areas"), ("2027-28", "All teams; text suggestions on agent notes; routing measure reported to Council"),
         ("2029", "CRM replacement specification written from three years of logged routing data"), ("2030", "New CRM routes with tested, City-owned data and an agent override already trusted")]
for i, (a, b) in enumerate(steps):
    x = 0.7 + i * 3.05
    text(s, x, 4.95, 2.6, 1.0, [{"runs": [R(a, size=12, bold=True, color=NAVY)]}, {"runs": [R(b, size=9.5, color=SLATE)]}])
    if i < 3:
        arrow(s, x + 2.72, 5.08, 0.25, 0.25, LINE)
person(s, "lauren", 0.5, 6.12, 6.05, 0.82, "Put the potential loss beside the average: a 0.5% bounce rate hides a 40% code, and 9% of bounces waited over a month.", "RATIONAL", qsize=10)
person(s, "rick", 6.8, 6.12, 6.05, 0.82, "Council asked about closures and duplicates. A routing measure next to 98.7% answers a question they will ask next.", "POLITICAL", qsize=10)
notes(s, """THE CASE (about 60 s). Presenter: Lauren.
City dollars: applying the October decision tree to the 2026 flagged set gives about $7K to $17K a year of avoided bounce cost, against $3K to $14K of agent time on prompts. Do not sell ROI. The October stake was about $100K a year in total; Route Check can only touch the part tied to flagged codes.
Residents: about 1,200 to 2,900 days a year not spent in the wrong queue (range across tier settings). Hazards: in 2025, 231 hazard-type phone bounces spent 2,915 days in the wrong queue (roads, sidewalks, signals and lights, potholes, signs). Alberta's Municipal Government Act s. 532 ties road-hazard liability to whether the City knew or should have known; whether a misrouted ticket counts as notice is a legal question we do not price.
2030 CRM: CSD03148 says the CRM reaches end of life in 2030. Option value (Session 2) usually favours waiting; here waiting destroys information, because labels not logged now cannot be recovered later.
Strategic foresight, Future to Now (Session 4): start from a 2030 CRM that routes on City-owned, tested data, and work back to what must start in 2026.
Loss beside the average: Analytic Trees p. 21.""")

# =====================================================================
# 11 POLITICS
# =====================================================================
s = new_slide(d, "Thu · the shift debrief · who has to say yes?", START[10],
              foot="1 Allison and Zelikow (1999), as used in the Session 4 debrief: where you stand depends on where you sit. 2 OCA (2023) p. 20: program coordinators sign off script content. 3 CSD03148 p. 2: business areas assume full ownership after routing. Stakes are our hypotheses, to test in co-design (not interviews held).")
kicker(s, 0.5, 0.65, 8, "INTEGRATION · THE POLITICAL GAME¹")
title(s, ["Every player gets something they already care about and ", ("no one loses authority", ), "; the union and the areas join on day one"])
rows = [
    ["Player", "Measured on today", "What they fear", "What Route Check gives them", "Our move"],
    ["311 agents (CSU 52)", "Answer speed; resolved on first contact", "Being replaced or ranked", "Fewer repeat calls; a reason behind each prompt; final say", "Co-design prompts; written coaching-only agreement"],
    ["311 team leads", "Team service levels", "More reporting work", "A daily digest that does the counting", "Digest fits in a 10-minute huddle"],
    ["311 director", "98.7% resolved on initial contact; 120 s answer", "Longer calls; a new bad-news number", "A routing measure they control before Council asks", "Guardrail: +10 s handle time stops the pilot"],
    ["Area program coordinators²", "Their own timeliness; script sign-off", "Blame for bounces; more tickets", "Fewer wrong tickets in their queue; a say in the code set", "Co-own the fix queue; no area bounce target"],
    ["Council / City Manager", "Complaints; duplicate tickets; audits", "Another IT project", "Evidence before money; a CRM requirement list", "Report the measure next to 98.7% from phase two"],
]
table(s, 0.5, 1.85, 12.35, 3.75, rows, colw=[1.85, 2.3, 2.0, 3.2, 3.0], sizes=[9.5, 9, 9, 9, 9], bold_first_col=True, row_h=0.6)
person(s, "rick", 0.5, 5.75, 6.05, 1.15, "Authority over the code stays with 311 and accountability for the work stays with the areas.³ What changes is that a miss now has an owner: the weekly fix queue, run by both.", "POLITICAL", qsize=10)
person(s, "nav", 6.8, 5.75, 6.05, 1.15, "If agents hear \"AI\" and \"accuracy\" first, they'll hear \"replacement\". Start with the can code they already know bounces, and with their own override stories.", "PSYCHOLOGICAL", qsize=10)
notes(s, """POLITICS (about 60 s). Presenter: Rick.
Vern's political game (Session 4): players, goals, actions, payoffs, likely moves. "Where you stand depends on where you sit."
Agents and CSU 52: measured on answer speed and first-contact resolution; fear replacement or individual ranking. Route Check keeps the final pick with the agent, explains every prompt, and the digest is coaching-only by written agreement.
Team leads: a daily digest that counts for them; designed to fit a 10-minute huddle.
311 director: the headline is 98.7% resolved on initial contact (CSD03148). A routing measure is a new number that could look bad; the counter-argument is that controlling it before Council asks is better than being asked.
Area program coordinators: they sign off scripts (OCA 2023 p. 20) and own the work after routing (CSD03148 p. 2). They fear blame for bounces. We give them co-ownership of the fix queue and refuse to make bounces an area target (that would invite proxy drift, slide 8).
Council: the July 2, 2025 motion asked about closures, duplicates and compliance. A routing measure next to 98.7% is the answer to the next question.
All "fears" are hypotheses (mirror imaging warning, Session 4). City outreach got no substantive answers as of Oct 22, 2026; co-design in days 1 to 30 is where these get tested.""")

# =====================================================================
# 12 90 DAYS
# =====================================================================
s = new_slide(d, "Thu · the plan · the first 90 days", START[11],
              foot=f"1 {OD}: \"311 - Empty Existing Garbage Can\" 50 + \"311 - Request New Garbage Can\" 35 = 85 of 1,062 phone-referral bounces in 2025. 2 Randomised by team-week so the comparison is fair. 3 Appendix A4: about 1,100 flagged tickets a month.")
kicker(s, 0.5, 0.65, 8, "PHASED IMPLEMENTATION · THE FIRST 90 DAYS")
title(s, ["Fix the worst codes first, run in ", ("shadow mode", ), " before anyone sees a prompt, then pilot on half the floor ", ("against a control", )])
phases = [
    ("DAYS 1-30", "Fix and build", "No model on screen", BLUE, [
        "Data agreement; pull the CRM reassignment log and agent IDs",
        "Re-run the backtest on internal data",
        "Quick win: review the two Facility Maintenance can codes with the areas: 8% of 2025 phone-referral bounces¹",
        "Co-design prompts with agents and CSU 52; sign the coaching-only agreement"]),
    ("DAYS 31-60", "Shadow mode", "Score all, show none", ORANGE, [
        "Check that the flagged share matches the backtest (about 6%)",
        "Start the daily digest to team leads",
        "Start the weekly fix queue with three areas: Roadway, Parks, Facility Maintenance",
        "Areas add a required closure reason and \"should have been\" code"]),
    ("DAYS 61-90", "Pilot", "Prompts on, half the teams", RED, [
        "Amber and red prompts on for half the teams; the rest are the control²",
        "Monthly QA sample of 200 resolved calls begins",
        "Weekly guardrail check: handle time, override rate",
        "Pilot runs to day 180 unless the day-120 look settles it³"]),
]
for i, (d1, h, sub, col, items) in enumerate(phases):
    x = 0.5 + i * 4.15
    rrect(s, x, 1.85, 3.95, 4.1, WHITE, radius=0.04)
    rect(s, x, 1.85, 3.95, 0.75, col)
    text(s, x + 0.2, 1.9, 3.6, 0.7, [{"runs": [R(d1, size=10, bold=True, color=WHITE, spc=150)]}, {"runs": [R(h, size=16, bold=True, color=WHITE), R("   " + sub, size=9.5, color=WHITE)]}])
    text(s, x + 0.2, 2.75, 3.6, 3.15, [{"runs": [R("●  ", size=8, color=col), R(it, size=10.5)], "after": 7} for it in items])
rrect(s, 0.5, 6.05, 12.35, 0.88, NAVY, radius=0.08)
text(s, 0.7, 6.1, 12, 0.8, [{"runs": [R("DAY 120 EARLY LOOK · DAY 180 GO / NO-GO  ", size=10, bold=True, color=YELLOW, spc=150), R("Two months of pilot can show a 40% drop; a 30% drop needs about 3.6 months. At day 120 we stop for harm or go early on a big effect. Otherwise the gate meets at day 180, and a no-go is a real option.", size=11, color=WHITE)]}], anchor="middle")
notes(s, """FIRST 90 DAYS (about 75 s). Presenter: Curtis.
Days 1-30, fix and build: data agreement with 311; pull the internal reassignment log and agent IDs; re-run the backtest on internal data (it may change the picture, which is the point). Quick win that needs no model: the two Facility Maintenance garbage-can codes alone were 85 of 1,062 phone-referral bounces in 2025 (8%); review them with Facility Maintenance, Parks and Transit. Co-design prompts with agents and CSU 52.
Days 31-60, shadow mode: score every pick, show nothing; confirm the flagged share matches the backtest; start the digest and the weekly fix queue with the three areas that carry the most bounces; areas add a required closure reason.
Days 61-90, pilot: prompts on for half the teams, randomised by team-week; the other half is the control; QA sample begins.
Power: at about 1,100 flagged tickets a month split 50/50 (about 550 per arm), the pilot detects a 50% drop in about 1.2 months, a 40% drop in about 1.9 months, and a 30% drop in about 3.6 months (80% power, 5% significance, two-proportion test; randomising by team-week adds a design effect, so treat these as minimums). Prompts go live on day 61, so day 120 is an early look (stop for harm, or go early on a 40%+ drop) and the full gate is near day 180.
Course link: what has to be true before phase two (brief); option value of waiting (Session 2) is used deliberately here: 30 extra days buys a real answer.""")

# =====================================================================
# 13 GATE + SCORECARD
# =====================================================================
s = new_slide(d, "Thu · the debrief · how will we know it worked?", START[12],
              foot=f"1 {OD}: flagged-code bounce rate 7.0% in 2026; median 2.0 days per phone bounce, 2026. 2 Weekly phone-referral bounce rate ran 0.79% to 2.05% between April and October 2026. 3 Hashemi (2022) reports over 83% top-one accuracy on 311 descriptions; our 85% top-three gate is our assumption.")
kicker(s, 0.5, 0.65, 8, "WHAT HAS TO BE TRUE BEFORE PHASE TWO · HOW THE CITY KNOWS IT WORKS")
title(s, ["Phase two starts only if bounces fall on flagged codes ", ("without slowing calls", ), ", agents trust the prompt, and the areas are logging re-routes"])
rrect(s, 0.5, 1.85, 5.2, 4.25, WHITE, radius=0.04)
rect(s, 0.5, 1.85, 5.2, 0.06, RED)
text(s, 0.7, 1.97, 4.9, 0.3, [[R("THE GATE · ALL SIX BY DAY 180", size=9.5, bold=True, color=RED, spc=150)]])
gates = ["Bounce rate on flagged codes down 30% or more vs control", "Average handle time up 10 seconds or less; 120 s answer target still met",
         "Override rate between 20% and 80%", "Re-route log live in areas receiving 80% of referrals",
         "Text model reaches 85% top-three accuracy on agent notes, offline³", "CSU 52 and area sign-off to expand"]
for i, g in enumerate(gates):
    y = 2.35 + i * 0.6
    c = rect(s, 0.7, y + 0.03, 0.3, 0.3, NAVY, shape=MSO_SHAPE.OVAL)
    text(s, 0.7, y + 0.03, 0.3, 0.3, [{"runs": [R(str(i + 1), size=9, bold=True, color=WHITE)], "align": "c"}], anchor="middle", shape=c, margin=(0, 0, 0, 0))
    text(s, 1.12, y, 4.45, 0.58, [[R(g, size=10.5)]])
text(s, 5.9, 1.85, 7, 0.3, [[R("THE SCORECARD¹", size=9.5, bold=True, color=BLUE, spc=150)]])
table(s, 5.9, 2.18, 6.95, 3.15, [
    ["Measure", "Baseline", "Target", "Type"],
    ["Bounce rate on flagged codes, pilot vs control", "7.0%", "down 30%+", [R("Primary", bold=True, color=RED)]],
    ["Median days in the wrong queue per bounce", "2.0 days", "down", [R("Primary · residents", bold=True, color=RED)]],
    ["Bounces returned to the team within 24 hours", "none today", "90%", [R("Learning loop", bold=True, color=BLUE)]],
    ["Codes cleared from the fix queue per quarter", "none today", "rising", [R("Learning loop", bold=True, color=BLUE)]],
    ["Average handle time", "today", "+10 s or less", [R("Guardrail", bold=True, color=ORANGE)]],
    ["Override rate", "none today", "20% to 80%", [R("Guardrail", bold=True, color=ORANGE)]],
    ["Bounce recording rate by area", "varies", "stable", [R("Data health", bold=True, color=GREEN)]]],
    colw=[3.0, 1.15, 1.25, 1.55], sizes=[9.5, 9.5, 9.5, 9], row_h=0.39)
rrect(s, 5.9, 5.45, 6.95, 0.65, LRED, RED, radius=0.1)
text(s, 6.05, 5.47, 6.7, 0.62, [[R("Do not judge it on the City-wide bounce rate. ", size=10.5, bold=True, color=RED), R("Weekly rates swing from 0.79% to 2.05% with season and recording; that noise would swamp the effect.²", size=10.5)]], anchor="middle")
text(s, 0.5, 6.2, 12.35, 0.7, [{"runs": [R("AFTER THE GATE  ", size=9.5, bold=True, color=NAVY, spc=150),
    R("Phase two (months 7-12): all teams; address-to-asset owner hints on red; text suggestions of the top three codes from the agent's notes, reusing the app's July 2026 AI, still a suggestion.  ", size=10.5),
    R("Phase three (2028-30): ", size=10.5, bold=True), R("routing measure reported to Council; data requirements written into the CRM replacement.", size=10.5)]}])
notes(s, """GATE AND SCORECARD (about 60 s). Presenter: Lauren or Curtis.
The brief asks: what has to be true before phase two, and how would the organisation know it is working.
Gate (all six by day 180; early look at day 120): flagged-code bounce rate down 30%+ vs control; handle time up no more than 10 seconds and the 120-second answer standard still met; override rate 20-80% (between rubber-stamping and ignoring); re-route log live in areas receiving 80% of referrals; phase-two text model at 85%+ top-three accuracy on agent notes offline (our assumption; Hashemi 2022 reports over 83% top-one accuracy on resident descriptions); CSU 52 and area sign-off.
Scorecard: two primary measures (flagged-code bounce rate vs control; median days in the wrong queue, the resident measure), two learning-loop measures, two guardrails, one data-health measure. Baselines from 2026 open data: 7.0% bounce rate in the flagged set; 2.0 median days per phone bounce.
Do not judge on the City-wide rate: weekly phone-referral bounce rates ran 0.79% to 2.05% between April and October 2026 (mean 1.33%).
Phase two and three as on the slide. Course link: Session 6 metric construction; Session 9 proxy drift (data-health row).""")

# =====================================================================
# 14 CLOSE
# =====================================================================
s = d.prs.slides.add_slide(d.blank); d.page += 1
s.background.fill.solid(); s.background.fill.fore_color.rgb = rgb(NAVY2)
callbar(s, "Call ended · Caller 4's can was emptied Tuesday · no second call", START[13], label="CALL ENDED", pill=SLATE)
footer(s, d.page, "Illustrative story; codes and rates real (311 Requests open data, 2025). Sources: Appendix A6.", lc="C2D3E0")
kicker(s, 0.6, 0.75, 8, "THE SHIFT DEBRIEF · WHAT WE PROPOSE", color=YELLOW)
text(s, 0.6, 1.05, 12.2, 1.2, [{"runs": [R("One check on the risky 6%, one loop for every miss, ", size=30, bold=True, color=WHITE), R("and the agent still makes the call", size=30, bold=True, color=YELLOW)], "line": 0.95}])
tl = [("MON 9:06", "The can code turns red. The agent asks: park, bus stop or City building?"), ("MON 9:07", "\"The bus shelter.\" The agent switches to the Transit code."),
      ("TUE", "Transit empties the can. Ticket closed, resolved."), ("THU", "No second call. The can code is on the fix queue.")]
for i, (a, b) in enumerate(tl):
    x = 0.6 + i * 3.08
    rrect(s, x, 2.45, 2.9, 1.25, "24496E", radius=0.08)
    text(s, x + 0.15, 2.52, 2.65, 1.15, [{"runs": [R(a, size=10, bold=True, color=YELLOW, spc=100)]}, {"runs": [R(b, size=11, color=WHITE)]}])
for i, (who, line) in enumerate([("lauren", "It costs about what it saves in City dollars. It is worth it for residents' days and for the data the 2030 CRM needs."),
                                 ("nav", "Agents finally hear about their misses, the next day, from a person they trust."),
                                 ("rick", "Nobody loses authority. A miss now has an owner, and the union is in the room.")]):
    person(s, who, 0.6 + i * 4.1, 3.95, 3.95, 1.25, line, qsize=10.5)
rrect(s, 0.6, 5.4, 12.15, 1.45, WHITE, radius=0.06)
text(s, 0.8, 5.48, 4, 0.3, [[R("DECISION REQUESTED TODAY", size=9.5, bold=True, color=RED, spc=150)]])
text(s, 0.8, 5.8, 11.8, 1.0, [{"runs": [R("Approve days 1-30: ", size=15, bold=True), R("a data agreement, a half-time analyst, and co-design with CSU 52 and three areas. ", size=15),
                                         R("Nothing reaches an agent's screen until shadow mode confirms the backtest.", size=15, bold=True, color=RED)]}])
notes(s, """CLOSE (about 45 s). Presenter: Curtis.
Close the story: Monday 9:06 the can code turns red; the agent asks one question; the caller says the bus shelter; the agent switches to the Transit code; Transit empties it Tuesday; no second call Thursday; the can code is on the fix queue. Illustrative, but the codes and rates are real.
Each character gives one line. Then the decision: approve days 1-30 only. It is low-risk because nothing reaches an agent's screen until shadow mode confirms the backtest on the City's own data.
Then open Q&A. Q&A prep sheet is in the project folder.""")

# =====================================================================
# APPENDIX
# =====================================================================
s = new_slide(d, "Appendix A1 · How the risk score is built", appendix=True, page_label="A1",
              foot=f"{OD}; scripts in edmonton-311-analysis/scripts (load.py, a1-a4.py, h1.py). Shrinkage: empirical Bayes with a beta prior fitted to 2025 phone referrals.")
kicker(s, 0.5, 0.65, 8, "APPENDIX A1 · METHOD")
title(s, ["The score is one ratio per code, shrunk so rare codes are not judged on one or two tickets"], size=22)
card(s, 0.5, 1.7, 6.1, 5.2, head="DEFINITIONS", body=[
    {"runs": [R("Bounce: ", size=11, bold=True), R("a ticket closed \"311 Redirecting to Other Business Area\".", size=11)], "after": 5},
    {"runs": [R("Code: ", size=11, bold=True), R("service area + category + description. We count 1,930 phone codes in 2025; the October deck counted 1,917 (definition difference, e.g. blank descriptions).", size=11)], "after": 5},
    {"runs": [R("Population: ", size=11, bold=True), R("phone tickets of type Referral, where 94% of phone bounces sit.", size=11)], "after": 5},
    {"runs": [R("Score: ", size=11, bold=True), R("(bounces + a) ÷ (referrals + a + b); prior mean 0.51%, weight about 10 tickets.", size=11)], "after": 5},
    {"runs": [R("Test: ", size=11, bold=True), R("fit on 2025, test on Jan 1-Nov 6, 2026 only; repeated for every year 2017-2026 using the prior year.", size=11)], "after": 5},
    {"runs": [R("Data: ", size=11, bold=True), R("3,531,392 tickets (2023 to Nov 6, 2026) from the live dataset; 2016-2022 from the City's yearly 311 files, deduplicated by Row ID (the 2017 file lists most rows twice).", size=11)]}])
card(s, 6.8, 1.7, 6.05, 2.5, head="KNOWN WEAKNESS WE FOUND IN REVIEW", head_color=RED, top=RED, body=[
    {"runs": [R("A prior weight of about 10 tickets is light: a code with 1 bounce on 5 tickets scores 7.2%, which is red. 61 of the 91 red codes had fewer than 20 referrals in 2025.", size=10.5)], "after": 5},
    {"runs": [R("Fix to test in shadow mode: cap codes under 20 referrals at amber, or raise the prior weight. The 91 red codes together carry 2,579 referrals and 395 bounces (15%).", size=10.5)]}])
card(s, 6.8, 4.35, 6.05, 2.55, head="WHAT THE LABEL CANNOT SEE", head_color=SLATE, body=[
    {"runs": [R("Quiet misroutes fixed inside an area, and wrong answers on 473,564 phone-resolved calls (2025), leave no record. The score learns only from recorded bounces.", size=10.5)], "after": 5},
    {"runs": [R("Recording changes move the label: all-channel bounces jumped from 2,162 (2021) to 4,515 (2022) and again in 2026 as more areas recorded (17 areas in 2021, 31 in 2026).", size=10.5)]}])
notes(s, "APPENDIX A1. Method and known weaknesses. Use in Q&A for 'how does the score work' and 'isn't one bounce enough to make a code red?'.")

s = new_slide(d, "Appendix A2 · Ten-year backtest", appendix=True, page_label="A2", foot=f"{OD}; yearly_2016_2026.csv and stability_backtest_2017_2026.csv in edmonton-311-analysis/.")
kicker(s, 0.5, 0.65, 8, "APPENDIX A2 · STABILITY, 2016-2026")
title(s, ["The score has held for ten years; the bounce rate stepped up twice, both times when more areas began recording"], size=22)
rows = [["Year", "Phone tickets", "Phone referrals", "Phone-referral bounces", "Bounce rate", "Areas recording", "Phone codes", "AUC (prior year)", "Caught at 2% flag"]]
data = [("2016", "1,831,720", "207,617", "580", "0.28%", "17", "1,701", "--", "--"), ("2017", "1,832,041", "259,028", "585", "0.23%", "20", "1,738", "0.86", "28%"),
        ("2018", "1,691,830", "261,243", "649", "0.25%", "14", "1,766", "0.91", "35%"), ("2019", "1,470,990", "254,693", "566", "0.22%", "19", "1,828", "0.90", "44%"),
        ("2020", "935,051", "200,313", "562", "0.28%", "17", "1,881", "0.90", "36%"), ("2021", "938,844", "225,435", "584", "0.26%", "17", "1,990", "0.92", "33%"),
        ("2022", "816,788", "223,944", "1,205", "0.54%", "20", "1,967", "0.91", "43%"), ("2023", "734,419", "193,077", "1,062", "0.55%", "23", "2,020", "0.93", "58%"),
        ("2024", "704,535", "188,003", "874", "0.46%", "20", "2,025", "0.93", "64%"), ("2025", "665,227", "191,521", "1,062", "0.55%", "24", "1,930", "0.90", "56%"),
        ("2026*", "557,353", "179,139", "1,930", "1.08%", "31", "1,954", "0.82", "41%")]
rows += [list(r) for r in data]
table(s, 0.5, 1.7, 12.35, 4.6, rows, colw=[0.8, 1.45, 1.45, 1.6, 1.2, 1.4, 1.25, 1.6, 1.6], sizes=[10] * 9, bold_first_col=True, row_h=0.36)
text(s, 0.5, 6.4, 12.35, 0.5, [[R("* 2026 to Nov 6. Phone volume fell by about two thirds from 2016 to 2025 while phone codes grew from 1,701 to 1,930: fewer calls spread over more codes means less practice per code.", size=10, color=SLATE)]])
notes(s, "APPENDIX A2. Full ten-year table.")

s = new_slide(d, "Appendix A3 · The codes behind the bounces", appendix=True, page_label="A3", foot=f"{OD}; code_risk_table_2025.csv. Tier from the shrunk 2025 rate.")
kicker(s, 0.5, 0.65, 8, "APPENDIX A3 · TOP CODES BY 2025 PHONE-REFERRAL BOUNCES")
title(s, ["Ten codes carry 37% of bounces; three of the top five belong to Facility Maintenance"], size=22)
top = [("Roadway Maintenance", "LITTER:Road", "2,089", "104", "5.0%", "amber"), ("Roadway Maintenance", "Callback Request", "1,655", "57", "3.4%", "amber"),
       ("Facility Maintenance", "311 - Empty Existing Garbage Can", "116", "50", "39.8%", "red"), ("Facility Maintenance", "311 - Request New Garbage Can", "59", "35", "51.1%", "red"),
       ("Facility Maintenance", "311 Parking Lot", "135", "30", "20.8%", "red"), ("Parks", "GENERAL COMMENT: COE Parks Services", "392", "27", "6.7%", "red"),
       ("Traffic", "General Comments Traffic Services", "1,802", "27", "1.5%", "green"), ("Roadway Maintenance", "General Comments Roadway Maintenance", "679", "26", "3.8%", "amber"),
       ("Forestry", "Prune City Tree", "1,069", "18", "1.7%", "green"), ("Roadway Maintenance", "LITTER:Boulevard Litter", "408", "17", "4.1%", "amber"),
       ("Parks", "GARBAGE:Other", "267", "16", "5.8%", "red"), ("Parks", "SIGNS:Sign Required", "34", "14", "32.2%", "red")]
tc = {"red": RED, "amber": ORANGE, "green": GREEN}
rows = [["Area", "Description", "Referrals", "Bounces", "Risk score", "Tier"]] + [[a, b, c, e, f, [R(t.upper(), bold=True, color=tc[t])]] for a, b, c, e, f, t in top]
table(s, 0.5, 1.7, 8.6, 5.0, rows, colw=[2.0, 3.4, 0.9, 0.85, 0.85, 0.6], sizes=[9.5, 9.5, 9.5, 9.5, 9.5, 8.5], row_h=0.38)
card(s, 9.3, 1.7, 3.55, 5.0, head="READING THE TABLE", body=[
    {"runs": [R("Two kinds of problem show up.", size=11, bold=True)], "after": 5},
    {"runs": [R("Look-alike codes ", size=10.5, bold=True), R("(the can codes, parking lot): the wording fits several owners. Fix in the code set and with a red question.", size=10.5)], "after": 5},
    {"runs": [R("Catch-all codes ", size=10.5, bold=True), R("(General Comments, Callback Request): high volume, low rate, used when nothing else fits. Fix by splitting or scripting, through the fix queue.", size=10.5)], "after": 5},
    {"runs": [R("Tiers: ", size=10.5, bold=True), R("956 green, 68 amber, 91 red codes in 2025.", size=10.5)]}])
notes(s, "APPENDIX A3. Top codes by 2025 phone-referral bounces, with tiers.")

s = new_slide(d, "Appendix A4 · How long the pilot must run", appendix=True, page_label="A4", foot="Two-proportion test, 80% power, 5% two-sided significance, baseline 7.0% bounce rate in the flagged set, about 1,100 flagged tickets a month split 50/50; prompts live from day 61. Team-week randomisation adds a design effect: treat as minimums.")
kicker(s, 0.5, 0.65, 8, "APPENDIX A4 · PILOT POWER AND MEASUREMENT")
title(s, ["A 30% drop needs about 3.6 months of pilot to show, so the gate sits near day 180; the City-wide rate is too noisy to judge on"], size=22)
table(s, 0.5, 1.7, 6.0, 1.95, [["Effect to detect", "Months of pilot needed", "Implication"],
                              ["50% drop (7.0% → 3.5%)", "about 1.2", "Visible by day 120"],
                              ["40% drop (7.0% → 4.2%)", "about 1.9", "Day-120 early look"],
                              ["30% drop (7.0% → 4.9%)", "about 3.6", "Full gate near day 180"],
                              ["Under 20%", "much longer", "Treat as no effect"]], colw=[2.0, 1.7, 2.3], sizes=[10.5, 10.5, 10], row_h=0.38)
card(s, 6.7, 1.7, 6.15, 1.8, head="WHY RANDOMISE BY TEAM-WEEK", body=[
    {"runs": [R("Seasons and recording changes move bounce rates week to week. Splitting teams at random, and switching weekly, keeps both arms exposed to the same weather, areas and codes.", size=10.5)]}])
card(s, 0.5, 3.7, 12.35, 2.2, head="WHY NOT THE CITY-WIDE BOUNCE RATE", head_color=RED, body=[
    {"runs": [R("Weekly phone-referral bounce rates ran from 0.79% to 2.05% between April and October 2026 (mean 1.33%). Route Check works on 6% of referrals; even a large effect on them moves the City-wide rate by less than the week-to-week noise. ", size=11), R("Judge it on the flagged codes, against the control.", size=11, bold=True)]}])
notes(s, "APPENDIX A4. Pilot power; source: analysis doc (power calculation by the analysis thread). Re-run with internal data in days 1-30.")

s = new_slide(d, "Appendix A5 · Course concepts behind each design choice", appendix=True, page_label="A5", foot="SEM 620 readings and cases (Glaser 2026); Feldman and Pentland (2003) ASQ 48(1); Kahneman and Klein (2009); Klein (2007); Parasuraman and Manzey (2010); Lindebaum et al. (2022); Glaser, Sloan and Gehman (2024); Glaser, Sloan and Knight (2025).")
kicker(s, 0.5, 0.65, 8, "APPENDIX A5 · COURSE CONCEPTS")
title(s, ["Every design choice traces to a concept we used in October, so the solution follows from the diagnosis"], size=22)
rows = [["Design choice", "Concept", "Session / source", "Slide"],
        ["Red tier at 5.6%", "Decision tree threshold, solved right to left", "S2 · Analytic Trees p. 20", "5"],
        ["Shrunk per-code rates; flagged-code measure", "Look inside the average; mix effect", "S2 · Analytic Trees p. 13", "6, 13"],
        ["Prompt on only 6% of picks", "System 1 / System 2; automation bias", "S3 · Psych. Perspective 3.2; Parasuraman & Manzey", "5"],
        ["Daily digest, next day", "Intuition needs timely feedback", "S3 · 3.3; Kahneman & Klein 2009", "4"],
        ["Agent keeps the final pick; four questions", "Reassembly of agency; access, change, stop, correct", "S1 · Reassembly 1.1, 1.7", "7"],
        ["Northfield guardrail; Ironstone override log", "Score + override; tacit knowledge lost to systems", "S1, S7 cases", "7"],
        ["Route Check as artifact; fix queue as routine", "Ostensive, performative, artifact", "S7 · Feldman & Pentland 2003", "4"],
        ["Fix queue co-owned with areas", "Political game; where you stand depends on where you sit", "S4 · Allison", "11"],
        ["Five missing records; re-route link", "Data is constructed; metric built slightly wrong", "S6 · SBS Ivey case", "9"],
        ["No area bounce target; QA sample", "Proxy drift; values withering under algorithms", "S9 · Robodebt; Lindebaum et al.", "8"],
        ["Premortem of six failures", "Premortem", "S2 · Klein 2007", "8"],
        ["Working back from the 2030 CRM", "Strategic foresight (Future → Now); option value", "S4, S2", "10"]]
table(s, 0.5, 1.7, 12.35, 5.2, rows, colw=[3.6, 4.0, 3.75, 1.0], sizes=[9.5, 9.5, 9, 9.5], row_h=0.38)
notes(s, "APPENDIX A5. Concept map. Check session numbers against the SEM 620 Course Concepts reference page before presenting; S8-S10 concepts were syllabus-only when this was drafted.")

s = new_slide(d, "Appendix A6 · How we used AI · and sources", appendix=True, page_label="A6", foot="Full AI process reflection submitted separately.")
kicker(s, 0.5, 0.65, 8, "APPENDIX A6 · AI PROCESS (SUMMARY) AND SOURCES")
title(s, ["AI pulled and tested 3.5 million tickets in hours; people chose the decision, caught its errors, and own every claim"], size=22)
card(s, 0.5, 1.7, 5.4, 5.2, head="AI PROCESS · SUMMARY", body=[
    {"runs": [R("Tools: ", size=10.5, bold=True), R("Claude (Anthropic) in Claude Code projects: separate threads for data analysis, course-concept reference, and deck drafting.", size=10.5)], "after": 5},
    {"runs": [R("What AI did well: ", size=10.5, bold=True), R("pulled the full open dataset, ran out-of-time backtests, and told us the dollar case was weak.", size=10.5)], "after": 5},
    {"runs": [R("What review caught: ", size=10.5, bold=True), R("a second AI pass found light shrinkage making one-bounce codes red, and a code-count mismatch (1,930 vs 1,917). Team to verify.", size=10.5)], "after": 5},
    {"runs": [R("What AI could not do: ", size=10.5, bold=True), R("talk to 311 agents or area staff. Every stake on slide 11 is a hypothesis.", size=10.5)], "after": 5},
    {"runs": [R("Rules: ", size=10.5, bold=True), R("public data only; no City or personal data entered; the team rewrites all final text before submission.", size=10.5)]}])
srcs = [
    "City of Edmonton. 311 Requests open data (q7ua-agfg). data.edmonton.ca/d/q7ua-agfg, accessed Nov 7, 2026; yearly 311 datasets 2016-2022.",
    "City of Edmonton. Parks (gdd9-eqv9); ETS GTFS Stops (4vt2-8zrq). Open data, accessed Nov 7, 2026.",
    "City of Edmonton (2026). 311 Service Experience, CSD03148, Executive Committee, Sep 2, 2026.",
    "Office of the City Auditor (2023). City's Response to 311 Requests, Nov 14, 2023.",
    "Hashemi, M. (2022). Automatic type detection of 311 service requests. Applied Artificial Intelligence 36(1). doi.org/10.1080/08839514.2022.2073717",
    "Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise. American Psychologist 64(6), 515-526.",
    "Parasuraman, R., & Manzey, D. (2010). Complacency and bias in human use of automation. Human Factors 52(3), 381-410. pubmed.ncbi.nlm.nih.gov/21077562",
    "Feldman, M. S., & Pentland, B. T. (2003). Reconceptualizing organizational routines. ASQ 48(1), 94-118. doi.org/10.2307/3556620",
    "Klein, G. (2007). Performing a project premortem. Harvard Business Review 85(9).",
    "Brynjolfsson, E., Li, D., & Raymond, L. (2023). Generative AI at Work. NBER w31161. nber.org/papers/w31161",
    "Glaser, V. L. (2026). The Reassembly of Agency; The Psychological Perspective; Analytic Trees; SEM 620 session slides and cases.",
    "Alberta, Municipal Government Act, RSA 2000, c M-26, s. 532. October 26, 2026 team deck, Appendix H, for all other sources.",
]
card(s, 6.1, 1.7, 6.75, 5.2, head="SOURCES", body=[{"runs": [R(x, size=8.5)], "after": 3} for x in srcs])
notes(s, "APPENDIX A6. AI summary and sources. The full AI process reflection is a separate deliverable (10% of the mark). The team must rewrite all final text in its own words (syllabus).")

d.save(sys.argv[1])
print("slides", d.page)
