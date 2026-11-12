# Part 2 of build_t2.py (exec'd from it): slides 9-25.

# ---------------------------------------------------------------- 9 DATA INVENTORY
s = new_slide(prs, pill='REFERRED', pill_style='yellow', chap=3, context='Thu · the area closes the ticket · what record?',
    kicker='DATA · SESSION 6: DATA IS BUILT · STRUCTURED VS UNSTRUCTURED, REAL-TIME VS BATCH',
    title='The ratio runs on data the City has; learning needs **one new habit per player**',
    source='Inventory columns after the Session 6 exercise (Scandinavian Building Services, Ivey W35309). Open data fields: data.edmonton.ca/d/q7ua-agfg. CRM fields not in open data are inferred, to confirm with 311. Eight areas began recording bounces in 2026 (team analysis).',
    notes='8:00-9:00. This is the 30% criterion. Left: what exists, its form, and who has to change a habit for the missing pieces to exist. The ratio needs nothing new: code, area, closure label and dates are already public. Learning needs three things nobody records today: a consistent closure reason, the agent’s two answers, and the link from the code picked to the code that finally owned the ticket. Then the trap: the label is the area’s own verdict. An empty-visit rate on its own rewards areas for closing “no action” less often, whatever happened at the curb. So we pair it with resident re-contact.')
rows = [['Code, area, closure label, dates', 'Public open data', 'No one'],
        ['Address, agent ID, handle time', 'In the CRM, not public', 'CRM owner: data agreement'],
        ['Closure reason, same in every area', 'Partly: 8 areas began in 2026', 'Areas: a required reason'],
        ['Two screening answers', 'Does not exist', 'Agents: two fields (CSU 52)'],
        ['First code → final code link', 'Does not exist', 'Dispatch clerks: one field']]
forms = [('STRUCTURED', 'BATCH'), ('STRUCTURED', 'REAL-TIME'), ('STRUCTURED', 'BATCH'), ('STRUCTURED', 'REAL-TIME'), ('STRUCTURED', 'BATCH')]
yend = table(s, 0.6, 2.3, [3.3, 2.7, 2.85], rows, header_row=['DATA', 'TODAY', 'WHO CHANGES'], row_h=0.6, size=12, first_size=12.5)
for i, (a, b) in enumerate(forms):
    tb(s, 0.68, 2.64 + i * 0.6 + 0.38, 3.2, 0.2, f'{a} · {b}', size=7, color=RED, font=MONO, bold=True, spc=30)
rect(s, 9.75, 2.3, 2.98, 3.4, fill=DARK)
mono_label(s, 9.95, 2.45, 2.6, 'THE ONE NEW FIELD', color=YEL, size=9)
tb(s, 9.95, 2.8, 2.6, 0.9, '“Why was there nothing to act on?”', size=17, bold=True, color=WHITE, font=HEAD)
line(s, 9.95, 3.8, 12.5, 3.8, color=GREY, dash=DASH.DASH)
tb(s, 9.95, 3.9, 2.6, 0.75, 'One of five reasons, required on every closure in the three pilot areas', size=11, color=LINE)
mono_label(s, 9.95, 4.75, 2.6, 'FILLED BY', color=YEL, size=9)
tb(s, 9.95, 5.0, 2.6, 0.6, 'The officer who closes the ticket', size=11.5, bold=True, color=WHITE)
rect(s, 0.6, 5.85, 12.13, 0.45, fill=PINK)
tb(s, 0.8, 5.85, 11.8, 0.45, '**A measure built slightly wrong:** an empty-visit rate alone rewards areas for closing “no action” less often. Pair it with re-contact.',
   anchor='m', size=11.5, color=TXT)

# ---------------------------------------------------------------- 10 90-DAY DATA SET
s = new_slide(prs, pill='REFERRED', pill_style='yellow', chap=3, context='Days 31-90 · the data set fills',
    kicker='DATA · CONSTRUCTED, THEN LEVERAGED · SESSION 1: HOW WERE THE EXAMPLES LABELLED?',
    title='The first 90 days build the **labelled data set** the City has never had',
    source='Volumes: about 1,870 flagged phone referrals a month at the 20% cut-off (2026 pace, duplicates excluded); logged from day 31; closure reason expected on about three in four by day 90 (most field outcomes close within three weeks). Session 1: data structure is a choice; Session 5: what the data cannot show.',
    notes='9:00-10:00. One row per flagged call, from day 31. By day 90 about 3,700 rows, about 2,800 with a closure reason, about 800 labelled empty visits. That is enough to re-estimate every pilot code from its own closures, and to test whether the two answers predict an empty visit better than the code alone. It also gives the City its first ground truth for whether the code picked was the right code. Rules: no names or notes, agent ID with QA only, held out by time, every field written as a requirement for the 2030 CRM.')
mono_label(s, 0.6, 2.3, 8, 'ONE ROW PER FLAGGED PHONE REFERRAL, FROM DAY 31', color=DARK, size=9.5)
fields = ['code picked', 'tier + rate shown', 'answer 1', 'answer 2', 'agent’s choice', 'caller insisted', 'closure reason', 'final code', 're-contact 30 d']
x = 0.6
for i, f in enumerate(fields):
    w = 0.22 + 0.085 * len(f)
    fl = RED if f in ('answer 1', 'answer 2', 'agent’s choice', 'caller insisted', 'final code') else DARK
    rect(s, x, 2.62, w, 0.38, fill=fl)
    tb(s, x, 2.62, w, 0.38, f, anchor='m', align=PP_ALIGN.CENTER, size=9.5, color=WHITE, font=MONO, bold=True)
    x += w + 0.07
tb(s, 0.6, 3.05, 9, 0.25, 'Red = new, recorded for the first time. Dark = exists today.', size=9, color=GREY)
rect(s, 0.6, 3.45, 3.6, 2.85, fill=DARK)
mono_label(s, 0.8, 3.58, 3.2, 'SIZE BY DAY 90', color=YEL, size=9)
for i, (a, b) in enumerate([('~3,700', 'flagged calls logged'), ('~2,800', 'with a closure reason'), ('~800', 'empty visits labelled')]):
    y = 3.92 + i * 0.75
    tb(s, 0.8, y, 1.6, 0.5, a, size=22, bold=True, color=(YEL if i == 2 else WHITE), font=HEAD, anchor='m')
    tb(s, 2.35, y, 1.8, 0.5, b, size=11, color=LINE, anchor='m')
card(s, 4.45, 3.45, 4.5, 2.85)
mono_label(s, 4.65, 3.58, 4, 'WHAT IT LETS THE ALGORITHM LEARN', color=RED, size=9)
for i, t in enumerate(['Do the two answers predict an empty visit better than the code alone?',
                       'Did the picked code differ from the final one? The first ground truth for “coded right”',
                       'Which codes confuse, and which standards are unclear: two different fixes']):
    y = 3.9 + i * 0.78
    tb(s, 4.65, y, 0.35, 0.4, str(i + 1), size=18, bold=True, color=RED, font=HEAD)
    tb(s, 5.05, y, 3.75, 0.75, t, size=11.5, color=TXT)
card(s, 9.2, 3.45, 3.53, 2.85, fill=PALE, line_c=PALE)
mono_label(s, 9.4, 3.58, 3, 'RULES FOR THE SET', color=DARK, size=9)
bullet_list(s, 9.4, 3.9, 3.2, ['No caller names or notes', 'Agent ID held by 311 QA only', 'Held out by time before training', 'Every field a 2030 CRM requirement'],
            size=11.5, sq=DARK, gap=0.55, h=0.5)

# ---------------------------------------------------------------- 11 LAUREN
s = new_slide(prs, pill='REFERRED', pill_style='yellow', chap=4, context='The shift debrief · Lauren’s tally',
    kicker='LOGICAL LAUREN HAS THE FLOOR · RATIONAL LENS · SESSION 2',
    title='The rational lens sets the floor: the check pays **above about 2% risk**',
    source='Glaser, Analytic Trees (decision-tree threshold p. 20; loss beside the average p. 21; option value of waiting). Monte Carlo: 50,000 draws on team ranges, duplicates excluded (Appendix A3). Resident days: 2025 phone bounces, team analysis of open data. Characters are composites from the October deck.',
    notes='10:00-10:50. Lauren is the October character for the rational lens. Expected value: rolled back, a 20-second check pays above about 2% risk. That gives $287K a year on average, and it is an average, not a forecast. Loss beside the average: P10 is $130K and no draw is negative; the real loss is 20 seconds on 22,000 calls and a prompt agents might stop reading. Option value of waiting: waiting for the 2030 CRM costs about three years of freed capacity, around $0.86M, and arrives with no labelled data. The pilot is the small staged option.')
persona(s, 0.6, 2.25, 12.13, 'LL', 'Logical Lauren', 'RATIONAL', 'Voiced by Lauren Lonsberry',
        'The arithmetic says check almost everything. I set the floor, not the ceiling.')
boxes = [('EXPECTED VALUE', '$287K / yr', 'mean of 50,000 draws; an average, not a forecast'),
         ('LOSS BESIDE THE AVERAGE', '$130K at P10', 'no draw below zero; the real loss is 20 s on 22,000 calls'),
         ('OPTION VALUE OF WAITING', '~$0.86M', 'three years of capacity lost waiting for the 2030 CRM'),
         ('STAGED OPTIONS', '90 days', 'phases two and three bought only if the gate passes')]
for i, (a, b, c) in enumerate(boxes):
    x = 0.6 + (i % 2) * 4.3
    y = 3.2 + (i // 2) * 1.35
    card(s, x, y, 4.1, 1.2)
    mono_label(s, x + 0.15, y + 0.1, 3.8, a, color=RED, size=8.5)
    tb(s, x + 0.15, y + 0.36, 3.8, 0.45, b, size=20, bold=True, color=DARK, font=HEAD, anchor='m')
    tb(s, x + 0.15, y + 0.82, 3.8, 0.35, c, size=10, color=GREY)
rect(s, 9.25, 3.2, 3.48, 2.55, fill=DARK)
mono_label(s, 9.45, 3.33, 3.1, 'WHAT DOLLARS LEAVE OUT', color=YEL, size=9)
tb(s, 9.45, 3.65, 3.1, 0.5, '16,987', size=24, bold=True, color=WHITE, font=HEAD, anchor='m')
tb(s, 9.45, 4.15, 3.1, 0.45, 'resident days in the wrong queue (2025 phone bounces)', size=10.5, color=LINE)
tb(s, 9.45, 4.7, 3.1, 0.9, 'Officers’ time for the calls that need them, and hazards not delayed', size=11, color=WHITE)
rect(s, 0.6, 5.95, 12.13, 0.38, fill=PALE)
tb(s, 0.8, 5.95, 11.8, 0.38, '**Sensitivity:** break-even at 2.0% avoided · halve the visit cost: $145K · agent-time pricing only: $297K',
   anchor='m', size=11.5, color=TXT)

# ---------------------------------------------------------------- 12 NAV
s = new_slide(prs, pill='REFERRED', pill_style='yellow', chap=4, context='The shift debrief · Nav on the floor',
    kicker='NEURO NAV HAS THE FLOOR · PSYCHOLOGICAL LENS · SESSION 3',
    title='The psychological lens sets the cut-off: **one question, about one call in nine**',
    source='Glaser, The Psychological Perspective (3.2 attention needs one concrete question; 3.3 feedback; 3.6 reference point); Kahneman and Klein (2009), conditions for intuitive expertise; Bucinca et al. (2021) on answer-first designs. Characters are composites.',
    notes='10:50-11:40. Nav: agents do not need to be more careful; they need one concrete question and to hear how it turned out. Each risk on the left has a design answer on the right. Attention: one question on about one call in nine, and the 120-second clock pauses on flagged calls. Feedback: Kahneman and Klein say intuition needs feedback that links action to result, and today none comes back. Anchoring: the card shows the rate and the questions, never a pre-selected answer. Reference point: agents feel the 20 seconds as a loss, so frame the gain and agree coaching-only terms.')
persona(s, 0.6, 2.25, 12.13, 'NN', 'Neuro Nav', 'PSYCHOLOGICAL', 'Voiced by Nav Sekhon',
        'Agents don’t need to be more careful. They need one concrete question, and to hear how it turned out.')
mono_label(s, 2.4, 3.15, 4, 'RISK', color=RED, size=9)
mono_label(s, 7.6, 3.15, 4, 'DESIGN RESPONSE', color=DARK, size=9)
nrows = [('Attention', '3.2', '“Be careful” does nothing on a 120-s clock', 'One question; clock paused on flagged calls'),
         ('Feedback', '3.3', 'No closure reason ever reaches the agent', 'Reason back to the agent within a day'),
         ('Anchoring', '3.2', 'A suggested outcome becomes the answer', 'Rate and questions, never a pre-selected answer'),
         ('Reference point', '3.6', 'Agents feel the 20 seconds as a loss', 'Frame the gain; coaching only, in writing')]
for i, (a, sec, r, d) in enumerate(nrows):
    y = 3.45 + i * 0.66
    card(s, 0.6, y, 6.6, 0.56)
    tb(s, 0.75, y, 1.9, 0.56, a, anchor='m', size=12.5, bold=True, color=DARK, font=HEAD)
    tag(s, 2.6, y + 0.17, 'S3 · ' + sec, color=DARK, size=7)
    tb(s, 3.45, y, 3.7, 0.56, r, anchor='m', size=11, color=TXT)
    line(s, 7.22, y + 0.28, 7.55, y + 0.28, color=DARK, w=1, arrow=True)
    rect(s, 7.6, y, 5.13, 0.56, fill=DARK)
    tb(s, 7.75, y, 4.9, 0.56, d, anchor='m', size=11.5, bold=True, color=WHITE)
tb(s, 0.6, 6.05, 12, 0.3, '**Bottom line:** the bias lives in the conditions (no feedback, a speed clock), not in the agent. Change the conditions.', size=12, color=TXT)

# ---------------------------------------------------------------- 13 RICK
s = new_slide(prs, pill='REFERRED', pill_style='yellow', chap=4, context='The shift debrief · who must agree',
    kicker='RULING RICK HAS THE FLOOR · POLITICAL LENS · SESSION 4',
    title='The political lens sets the order: **four parties say yes, in turn**',
    source='Session 4: the political game (players, goals, moves); Allison, where you stand depends on where you sit; mirror imaging; strategic foresight. CSD03148 (Sep 2, 2026) p. 2: areas assume ownership after routing. OCA 2023 p. 20: areas sign off scripts. CSU 52 collective agreement 2024-2027, Art. 11.03 (technological change). Stakes are hypotheses to test in days 1-30.',
    notes='11:40-12:30. Rick: the ratio is harmless; publishing it is political, because it makes the areas’ closures visible for the first time. An area may read a published empty-visit rate as an audit of its officers, so do not mirror-image and assume they want it counted. That is why the areas write the screening questions and co-own the fix queue. The order of asking: 311 approves, the three areas and the CRM owner sign, CSU 52 agrees the terms before any agent sees a card. Council gets a routing measure it never had.')
persona(s, 0.6, 2.25, 7.4, 'RR', 'Ruling Rick', 'POLITICAL', 'Voiced by Rick Auger',
        'The ratio is harmless. Publishing it is political: it makes the areas’ closures visible.')
rect(s, 8.2, 2.25, 4.53, 0.72, fill=DARK)
mono_label(s, 8.35, 2.32, 3, 'WHERE YOU STAND', color=YEL, size=8.5)
tag(s, 11.55, 2.32, 'HYPOTHESIS', color=YEL, size=6.5)
tb(s, 8.35, 2.57, 4.3, 0.38, 'Areas may read the rate as an audit of officers', size=11, color=WHITE, bold=True)
stairs = [('1', '311 management', 'Approve the 90-day pilot', 'NOW', GRN),
          ('2', 'Three pilot areas', 'Write the questions; require a closure reason', 'DAYS 1-30', GRN),
          ('3', 'CRM owner', 'Two fields, or exports in shadow', 'DAYS 1-30', GRN),
          ('4', 'CSU 52', 'Coaching only; clock paused; no ranking', 'BEFORE ANY CARD', DARK)]
for i, (n, who, ask, when, f) in enumerate(stairs):
    x = 0.6 + i * 3.07
    top = 5.25 - i * 0.38
    mono_label(s, x, top - 0.78, 2.9, 'WE ASK', color=RED, size=8)
    tb(s, x, top - 0.55, 2.9, 0.5, ask, size=11.5, bold=True, color=DARK)
    rect(s, x, top, 2.92, 6.3 - top, fill=f)
    tb(s, x + 0.12, top + 0.1, 0.4, 0.4, n, size=16, bold=True, color=YEL, font=HEAD)
    tb(s, x + 0.45, top + 0.1, 2.4, 0.4, who, size=13.5, bold=True, color=WHITE, font=HEAD)
    tb(s, x + 0.45, top + 0.45, 2.4, 0.25, when, size=8, bold=True, color=YEL, font=MONO)

# ---------------------------------------------------------------- 14 BIASES
s = new_slide(prs, pill='REFERRED', pill_style='yellow', chap=4, context='Wed · the team chat · why didn’t we catch it?',
    kicker='BIASES · SESSION 3: SAY WHAT HAPPENED, THEN THE TENDENCY, THEN WHAT IS NEGLECTED',
    title='Name the situation before the bias; **two of the biases are ours**',
    source='Glaser, The Psychological Perspective; Tversky and Kahneman (1974, 1981); Nickerson (1998); Moore and Healy (2008); Arkes and Blumer (1985); Fazio et al. (2015). Method rule: a heuristic is a shortcut; a bias is a systematic distortion under particular conditions.',
    notes='12:30-13:10. Each row is a situation first, then the bias, then what the design does. Keep agents out of the dock: the biases live in the system. Then own ours before the examiner finds them. Confirmation: after the bounce case came in at $7K to $17K, we went looking for a bigger dollar case and found one, so we specified the test before scoring 2026. Overconfidence: the 35% avoided has no source. And when we took duplicates out, the case fell from $375K to $287K. We kept the 20% line we had set before, rather than move it to win the number back. Say that openly.')
brows = [['Availability', 'One memorable empty visit stands in for the rate', 'Card shows the code’s rate, not an anecdote'],
         ['Confirmation', 'The code list is searched to confirm the first fit', 'Questions ask what would make it not an offence'],
         ['Anchoring', 'A suggestion on screen becomes the answer', 'No pre-selected outcome'],
         ['Overconfidence', '“99% land correctly” reads as “the pick is fine”', 'Report per code (30%, not 5.9%), never one average'],
         ['Framing', '“98.7% resolved” vs “1 in 17 visits finds nothing”', 'Scorecard carries both lines'],
         ['Sunk cost', '“Wait for the 2030 CRM”', 'Every pilot field doubles as a CRM requirement']]
table(s, 0.6, 2.25, [1.85, 3.55, 3.15], brows, header_row=['BIAS', 'WHAT HAPPENS', 'WHAT THE DESIGN DOES'], row_h=0.5, size=10.5, first_size=11.5)
rect(s, 9.4, 2.25, 3.33, 4.05, fill=DARK)
mono_label(s, 9.6, 2.38, 3, 'OURS, DECLARED BEFORE Q&A', color=YEL, size=8.5)
tb(s, 9.6, 2.7, 3.0, 0.3, 'Confirmation', size=13, bold=True, color=WHITE, font=HEAD)
tb(s, 9.6, 3.0, 3.0, 0.95, 'We hunted for a bigger dollar case than $7K-$17K. Test fixed before scoring 2026; it held.', size=10, color=LINE)
tb(s, 9.6, 3.95, 3.0, 0.3, 'Overconfidence', size=13, bold=True, color=WHITE, font=HEAD)
tb(s, 9.6, 4.25, 3.0, 0.95, 'The 35% avoided has no source. The case holds down to 2.0%; the pilot measures it.', size=10, color=LINE)
tb(s, 9.6, 5.2, 3.0, 1.05, '**Duplicates out:** the case fell from $375K to $287K. We kept the 20% line rather than move it to win the number back.', size=10, color=WHITE, hi=YEL)

# ---------------------------------------------------------------- 15 PLAN
s = new_slide(prs, pill='REFERRED', pill_style='yellow', chap=4, context='Day 1 to 90 · data before AI',
    kicker='THE PLAN · FIRST 90 DAYS, THE GATE, AND TWO LATER PHASES',
    title='Ninety days inside 311’s authority; **a numeric gate** guards phase two',
    source='Within control vs needs others: course consulting-deck standard. Pilot by team-week randomisation, half the teams. At ~1,870 flagged calls a month, a 20% relative drop (27.9% to 22.3%) reads out in about a month at 80% power (Appendix A4); clustering makes this a minimum. Generative AI Standard (Jul 2024) and Privacy Impact Assessment standard (May 2026) apply from phase two.',
    notes='13:10-14:00. Days 1-30 build with no screen change: re-run the backtest on internal closures, co-design the card with senior agents, the areas write their two questions, the data agreement and the CSU 52 terms. Days 31-60 shadow mode: score every pick, show nothing, start the data set. Days 61-90: the card goes on for half the teams, chosen by team-week. The gate at day 120: every line must be true. Phase two adds all areas, retrains on the 90-day set, and only then tests the text suggestion on agent notes. Phase three writes every field into the 2030 CRM. Full automatic routing is not on the roadmap.')
line(s, 0.6, 2.75, 12.73, 2.75, color=DARK, w=1.25)
rect(s, 0.6, 2.67, 0.16, 0.16, fill=RED)
mono_label(s, 0.6, 2.3, 3.5, 'DAYS 1-90 · NO AI', color=RED, size=9)
rect(s, 6.08, 2.62, 0.26, 0.26, fill=BG, line=RED, lw=1.5, rot=45)
mono_label(s, 8.95, 2.3, 2, 'AFTER THE GATE', color=DARK, size=8.5)
rect(s, 8.95, 2.69, 0.12, 0.12, fill=DARK)
mono_label(s, 10.95, 2.3, 2, '2027 ON', color=DARK, size=8.5)
rect(s, 10.95, 2.69, 0.12, 0.12, fill=DARK)
tb(s, 0.6, 3.0, 4.8, 0.35, 'Phase 1 · build, shadow, pilot', size=14, bold=True, color=DARK, font=HEAD)
prow = [('1-30', 'Re-run backtest on internal closures', '311'), ('1-30', 'Co-design the card with senior agents', '311 + AGENTS'),
        ('1-30', 'Areas write two questions; reason field', 'AREAS'), ('1-30', 'Data agreement; CSU 52 terms', 'CRM + CSU 52'),
        ('31-60', 'Shadow: score every pick, show nothing', '311'), ('61-90', 'Card on for half the teams', '311 + LEADS')]
for i, (d, t, o) in enumerate(prow):
    y = 3.42 + i * 0.44
    tb(s, 0.6, y, 0.6, 0.4, d, anchor='m', size=8.5, color=GREY, font=MONO, bold=True)
    tb(s, 1.2, y, 3.2, 0.4, t, anchor='m', size=11, color=TXT)
    tb(s, 4.3, y, 1.25, 0.4, o, anchor='m', size=7.5, color=RED, font=MONO, bold=True, align=PP_ALIGN.RIGHT)
    line(s, 0.6, y + 0.42, 5.55, y + 0.42, color=LINE, w=0.5)
card(s, 5.75, 3.0, 3.0, 3.3, line_c=RED, lw=1.25)
mono_label(s, 5.9, 3.08, 2.8, 'GATE · DAY 120 · ALL TRUE', color=RED, size=8.5)
gates = ['Empty visits, flagged codes: down 20%+ vs control', 'Refused without consent: zero', 'Handle time: +15 s or less',
         'Override rate 20% to 80%', 'Closure reason on 80%+', '3,500+ labelled flagged calls', 'Areas + CSU 52 sign phase 2']
for i, g in enumerate(gates):
    y = 3.4 + i * 0.4
    rect(s, 5.9, y + 0.1, 0.11, 0.11, fill=RED)
    tb(s, 6.1, y, 2.6, 0.4, g, anchor='m', size=10, color=TXT)
tb(s, 8.95, 3.0, 1.85, 0.35, 'Phase 2', size=14, bold=True, color=DARK, font=HEAD)
for i, t in enumerate(['All teams, all areas', 'Retrain on the 90-day set', 'Text suggestion on notes, in shadow first']):
    rect(s, 8.95, 3.42 + i * 0.95, 1.85, 0.85, fill=PALE)
    tb(s, 9.05, 3.42 + i * 0.95, 1.7, 0.85, t, anchor='m', size=11, bold=True, color=DARK)
tb(s, 10.95, 3.0, 1.8, 0.35, 'Phase 3', size=14, bold=True, color=DARK, font=HEAD)
for i, t in enumerate(['Fields become 2030 CRM requirements', 'Resident hears the closure reason', 'No full auto-routing']):
    rect(s, 10.95, 3.42 + i * 0.95, 1.78, 0.85, fill=PALE)
    tb(s, 11.05, 3.42 + i * 0.95, 1.63, 0.85, t, anchor='m', size=11, bold=True, color=DARK)

# ---------------------------------------------------------------- 16 MEASURES
s = new_slide(prs, pill='REFERRED', pill_style='yellow', chap=4, context='Day 90 on · how the City knows',
    kicker='HOW THE CITY WOULD KNOW · EACH MEASURE PAIRED WITH WHAT IT COULD REWARD BY MISTAKE',
    title='Pair every measure with **a check against gaming it**',
    source=f'{OD}, duplicates excluded: 27.9% of flagged referrals ended in an empty visit (5,326 of 19,090, Jan 1-Nov 6, 2026). Session 9: proxies drift from what they stand for; measures chosen before launch; Robodebt and the burden of proof. Weekly City-wide phone bounce rates ran 0.79% to 2.05%, Apr-Oct 2026.',
    notes='14:00-14:30. One primary measure, three guardrails, each paired with what it could reward by mistake. The primary, the empty-visit rate on flagged codes, could fall on paper if areas close differently, so it is paired with resident re-contact within 30 days. Refused-without-consent is the Robodebt guardrail and must read zero. Handle time and override rate are guardrails, never targets. And never judge on the City-wide average: weekly bounce rates swung from 0.79% to 2.05% this year.')
mcards = [('Empty visits, flagged codes', '27.9%', 'phone, 2026 · gate 22.3%', 'Closing “no action” less, on paper', 'Re-contact within 30 days'),
          ('Refused without consent', '0', 'must stay at zero', 'The check becoming a gate', '“Caller insisted” logged'),
          ('Handle time, flagged calls', '+15 s', 'maximum added', 'Skipping the questions', 'Answers recorded rate'),
          ('Override rate', '20-80%', 'healthy band', 'Rubber stamp or noise', 'Monthly sample audit')]
for i, (h, v, sub, rew, chk) in enumerate(mcards):
    x = 0.6 + i * 3.07
    card(s, x, 2.3, 2.92, 3.15)
    tb(s, x + 0.15, 2.38, 2.65, 0.5, h, size=12, bold=True, color=DARK, font=HEAD)
    tb(s, x + 0.15, 2.95, 2.65, 0.55, v, size=26, bold=True, color=(RED if i == 1 else DARK), font=HEAD, anchor='m')
    tb(s, x + 0.15, 3.5, 2.65, 0.25, sub, size=8.5, color=GREY, font=MONO)
    rect(s, x, 3.85, 2.92, 0.8, fill=PINK)
    mono_label(s, x + 0.15, 3.9, 2.6, 'COULD REWARD', color=RED, size=8)
    tb(s, x + 0.15, 4.15, 2.65, 0.48, rew, size=10.5, color=RED)
    mono_label(s, x + 0.15, 4.75, 2.6, 'CHECK', color=DARK, size=8)
    tb(s, x + 0.15, 5.0, 2.65, 0.42, chk, size=11, bold=True, color=DARK)
rect(s, 0.6, 5.65, 12.13, 0.55, fill=DARK)
tb(s, 0.8, 5.65, 1.2, 0.55, 'CAUTION', anchor='m', size=9, bold=True, color=YEL, font=MONO)
tb(s, 2.0, 5.65, 10.6, 0.55, 'Judge the pilot against its control group, never the City-wide average.', anchor='m', size=14, bold=True, color=WHITE, font=HEAD)

# ---------------------------------------------------------------- 17 ASK (dark)
s = new_slide(prs, dark=True, pill='REFERRED', pill_style='yellow', chap=5, context='Today · the decision we ask for',
    kicker='RECOMMENDATION · THE DECISION WE ASK THE EXECUTIVE TEAM TO MAKE TODAY',
    title='Approve a 90-day pilot in three areas; **decide again at day 120**',
    source='One-time configuration is a team estimate with no City quote. Running cost: ~22,000 flagged calls a year x $0.78 of agent time. Pilot areas: Municipal Enforcement, Peace Officers, Parking (3 of every 4 flagged empty visits, 2026). Caller 7 illustrative.',
    notes='14:30-15:00. Close on the decision the room can take today. Three asks, in the order the political game requires. Approve the pilot on the 84 codes above 20% risk, in three areas, half the teams. Sign the data agreement for two CRM fields. Set the terms with CSU 52 before any agent sees a card. Not asked today: automatic routing or an AI writing codes. The measure we would bring back: Caller 7’s officer, free on Thursday for a call that needs one.')
asks = [('01', 'Approve the pilot', ['84 codes, three areas, half the teams', 'One-time $10K-$150K', 'Running ~$17K of agent time'], 'ASSUMPTION'),
        ('02', 'Sign the data agreement', ['Closure reason + reassignment fields', 'In the three pilot areas', 'Exports if the CRM can’t'], None),
        ('03', 'Set terms with CSU 52', ['Coaching only, no ranking', 'Clock paused on flagged calls', 'Walkthrough at day 75'], None)]
for i, (n, h, items, t) in enumerate(asks):
    x = 0.6 + i * 3.15
    rect(s, x, 2.3, 3.0, 2.95, fill=GRN)
    tb(s, x + 0.2, 2.42, 1, 0.5, n, size=24, bold=True, color=YEL, font=HEAD)
    if t:
        tag(s, x + 1.75, 2.5, t, color=YEL, size=7)
    tb(s, x + 0.2, 3.0, 2.7, 0.4, h, size=15, bold=True, color=WHITE, font=HEAD)
    bullet_list(s, x + 0.2, 3.5, 2.7, items, size=11.5, color=WHITE, sq=YEL, gap=0.5, h=0.48)
card(s, 10.1, 2.3, 2.63, 2.95, fill=DARK, line_c=WHITE)
mono_label(s, 10.28, 2.42, 2.3, 'NOT ASKED TODAY', color=YEL, size=9)
tb(s, 10.28, 2.75, 2.3, 1.1, 'Automatic routing, or an AI that writes codes', size=13.5, bold=True, color=WHITE, font=HEAD)
tb(s, 10.28, 3.9, 2.3, 0.5, 'Phase two, only if the gate passes', size=10.5, color=LINE)
for i, ini in enumerate(['LL', 'NN', 'RR']):
    rect(s, 10.28 + i * 0.62, 4.55, 0.52, 0.45, fill=BG)
    tb(s, 10.28 + i * 0.62, 4.55, 0.52, 0.45, ini, anchor='m', align=PP_ALIGN.CENTER, size=10.5, bold=True, color=DARK, font=HEAD)
rect(s, 0.6, 5.5, 12.13, 0.62, fill=BG)
rect(s, 0.52, 5.73, 0.16, 0.16, fill=DARK, shape=MSO_SHAPE.OVAL)
rect(s, 12.65, 5.73, 0.16, 0.16, fill=DARK, shape=MSO_SHAPE.OVAL)
tb(s, 0.85, 5.5, 2.0, 0.62, 'TICKET · CALLER 7', anchor='m', size=9, bold=True, color=GREY, font=MONO)
tb(s, 2.9, 5.5, 9.7, 0.62, 'Caller 7’s officer, **free on Thursday** for a call that needs one, is the measure we bring back.', anchor='m', size=14, bold=True, color=DARK, font=HEAD)

# ---------------------------------------------------------------- 18 AI REFLECTION placeholder
s = new_slide(prs, pill='PLACEHOLDER', pill_style='dark', chap=5, context='Behind the deck · how we used AI',
    kicker='AI PROCESS REFLECTION',
    title='PLACEHOLDER: headline to be written by the team member who owns this slide',
    source='TO CONFIRM by the slide owner. The syllabus requires the final writing to be the team’s own.',
    notes='Placeholder. The team member who owns this slide writes it in their own words, from the team’s own log: tools and what each did, one or two crux moves, when the AI was wrong, and how outputs were validated. Material the team can draw on: the AI argued against our own AI idea (training labels are agents’ own picks); “give me the most savings” moved the decision; the 35% avoided share was proposed with no source and kept only as a labelled assumption; the duplicates call came from Curtis, not the AI, and cut the case at the old cut-off.')
rect(s, 0.6, 2.25, 12.13, 0.38, fill=RED)
tb(s, 0.8, 2.25, 8, 0.38, 'PLACEHOLDER · TO BE WRITTEN BY A TEAM MEMBER', anchor='m', size=9.5, bold=True, color=WHITE, font=MONO)
for i, (h, d) in enumerate([('Tools and agents', 'Which tools were used, and for what.'), ('Crux moves', 'One or two crux moves.'),
                            ('When AI was wrong', 'What we did when AI was wrong.'), ('How we validated', 'How we validated what AI produced.')]):
    x = 0.6 + i * 3.07
    card(s, x, 2.85, 2.92, 3.35, line_c=GREY, dash=DASH.DASH)
    tb(s, x + 0.15, 2.95, 1, 0.35, f'0{i + 1}', size=12, bold=True, color=RED, font=MONO)
    tb(s, x + 0.15, 3.3, 2.65, 0.35, h, size=13, bold=True, color=DARK, font=HEAD)
    tb(s, x + 0.15, 3.68, 2.65, 0.5, d, size=10, italic=True, color=GREY)
    tb(s, x + 0.15, 5.85, 2.65, 0.25, 'To be written by a team member.', size=8, color=GREY, font=MONO)

# ---------------------------------------------------------------- APPENDIX
def appx(code, context, kicker, title, source):
    return new_slide(prs, pill='APPENDIX', pill_style='dark', chap=5, context=f'{code} · {context}', kicker=kicker, title=title,
                     source=source, notes='Appendix only; not presented.', title_size=24)

s = appx('A1', 'how the risk score is built', 'APPENDIX A1 · THE SCORE AND THE CUT-OFF',
    'The score is a shrunk ratio per code; **duplicates are out**, and the 20% line stays',
    f'{OD}; team six-part export, deduplicated by Row ID. Scripts: edmonton-311-analysis/no-duplicates/s1c.py, s1d.py. Bounce AUC by year: yearly datasets 2016-2022 and current set (stability_backtest_2017_2026.csv).')
tb(s, 0.6, 2.35, 5.4, 4.2, [
    ('DEFINITIONS', {'font': MONO, 'size': 9, 'bold': True, 'color': RED, 'space_after': 4}),
    ('**Code** = service area + category + description.', {'space_after': 5}),
    ('**Empty field visit** = Does Not Meet Bylaw Offence Standards; Assessed-No Action Required; Unable to Locate Animal; Location Not Found; Unable to Contact Complainant.', {'space_after': 5}),
    ('**Desk waste** = 311 Redirecting (a bounce); Non-City Service or Location; Reported on same day.', {'space_after': 5}),
    ('**Left out:** three Duplicate Request labels and File Already under Investigation (5,100 in 2026; the City is already working on duplicates); Parking Vehicle Gone Upon Arrival (depends on dispatch speed).', {'space_after': 5}),
    ('**Score** = (wasted + 10 × prior) / (referrals + 10), field and desk, summed. Priors 2025: 6.6% and 0.8%. Weekly, rolling 12 months; new codes amber 90 days.', {'space_after': 5}),
    ('**Route Check lives inside it:** the bounce ratio is one term. Its AUC on next year’s bounces was 0.82-0.93 every year since 2017; the empty-visit score scores 0.86-0.92 on next year’s empty visits, every year 2017-2026.', {}),
], size=10.5, color=TXT)
crow = [['>10%', '222', '25.7%', '76.4%', '20.2%'], ['>15%', '142', '17.1%', '63.7%', '25.0%'], ['>20% (chosen)', '84', '10.7%', '50.2%', '30.7%'],
        ['>25%', '52', '8.8%', '43.9%', '32.0%'], ['>30% (red)', '35', '4.2%', '28.1%', '42.5%'], ['>50%', '6', '0.7%', '7.3%', '64.7%']]
table(s, 6.3, 2.35, [1.55, 0.8, 1.25, 1.3, 1.53], crow, header_row=['CUT-OFF', 'CODES', 'CALLS FLAGGED', 'EMPTY VISITS', 'WASTE IN FLAGGED'], row_h=0.42, size=11, first_size=11)
tb(s, 6.3, 5.3, 6.4, 1.0, ['2026 to Nov 6: 179,139 phone referrals; 5.9% empty field visit, 1.4% desk waste, 7.3% either.',
    'With duplicates left in, the 20% line flagged 150 codes for $375K. Without them, the same line flags 84 codes for $287K (P10-P90 $130K-$477K). The line was set before duplicates came out and was not moved.'], size=10, color=TXT, space_after=4)

s = appx('A2', 'the codes behind the empty visits', 'APPENDIX A2 · WHERE THE FLAGGED EMPTY VISITS SIT',
    'Three pilot areas hold **three in four** flagged empty visits',
    f'{OD}, Jan 1-Nov 6, 2026; flagged set = 84 codes above 20% 2025 risk, duplicates excluded.')
arows = [['Community Standards - Municipal Enforcement', '6,196', '2,055', '39%'], ['Community Standards - Peace Officers', '3,218', '1,446', '27%'],
         ['Roadway Maintenance', '3,524', '817', '15%'], ['Parking Enforcement', '1,448', '550', '10%'], ['Animal Control', '2,210', '225', '4%'],
         ['Park Rangers', '1,560', '123', '2%'], ['All other', '934', '110', '2%']]
table(s, 0.6, 2.35, [5.0, 2.35, 2.0, 2.0], arows, header_row=['AREA', 'FLAGGED REFERRALS', 'EMPTY VISITS', 'SHARE'], row_h=0.4, size=12, first_size=12)
tb(s, 0.6, 5.6, 12, 0.6, 'Why the card asks about the standard, not the owner: the flagged codes are complaints where an officer judges a standard (untidy, noise, weeds, private parking). Roadway Maintenance (snow) is seasonal and timing-driven; it joins in phase two.', size=11, color=TXT)

s = appx('A3', 'Monte Carlo inputs and sensitivity', 'APPENDIX A3 · MONTE CARLO INPUTS',
    'Every input is a range with a source or a flag; **the one that moves the answer most is ours**',
    'Triangular distributions (min / likely / max), 50,000 draws, seed 20261110. Volumes annualised from Jan 1-Nov 6, 2026 (x 12/10.2). Budget: 311 and Customer Access $14.66M / ~900K contacts = $16.29 per contact (City of Edmonton operating budget). Six questions for reviewing an analysis: Session 2.')
mrows = [['Empty field visits a year, flagged codes', '6,266 (counted)', 'Open data, duplicates excluded'], ['Desk waste a year, flagged codes', '632 (counted)', 'Bounces, non-City, same-day'],
         ['Flagged calls a year', '22,459 (counted)', 'Open data'], ['Cost of a field visit', '$22 / $84 / $280', 'Team Oct 26 ranges; no City figure'],
         ['Desk time per closure', '5 / 10 / 20 min', 'CSU 52 rates $36.93-$52.09/h'], ['Share of empty visits avoided', '20% / 35% / 50%', '**ASSUMED**; pilot measures it'],
         ['Agent time per flagged call', '$0.30 / $1.02 / $1.02', 'Agent-only to average contact cost']]
table(s, 0.6, 2.35, [3.9, 2.2, 3.1], mrows, header_row=['INPUT', 'MIN / LIKELY / MAX', 'SOURCE OR STATUS'], row_h=0.44, size=11, first_size=11)
rect(s, 10.0, 2.35, 2.73, 3.7, fill=DARK)
mono_label(s, 10.15, 2.47, 2.5, 'RESULTS', color=YEL, size=9)
tb(s, 10.15, 2.8, 2.45, 3.2, ['Net mean **$287K**', 'Median $265K', 'P10 $130K · P90 $477K', 'No draw below zero', 'Gross $304K; check $17K',
    'Halve visit cost: $145K', 'Agent-only: $297K', 'Red tier only (30%): $163K', 'Break-even: 2.0% avoided'], size=10.5, color=WHITE, hi=YEL, space_after=3)

s = appx('A4', 'how long the pilot must run', 'APPENDIX A4 · PILOT LENGTH',
    'Because one flagged referral in five ends empty, **the pilot reads out in weeks**',
    'Two-proportion test, 80% power, 5% two-sided; baseline 27.9% (5,326 of 19,090 flagged phone referrals, 2026, duplicates excluded); ~1,870 flagged referrals a month split 50/50 by team-week. Clustering adds a design effect: treat as minimums.')
prow2 = [['20% relative (27.9% → 22.3%)', '~950', '~1.0'], ['35% relative (27.9% → 18.1%)', '~290', '~0.3'],
         ['Route Check, bounces, 30% drop (for comparison)', '~2,000', '~3.6']]
table(s, 0.6, 2.35, [5.6, 2.6, 2.6], prow2, header_row=['DROP TO DETECT', 'PER ARM', 'MONTHS OF PILOT'], row_h=0.5, size=12, first_size=12)
tb(s, 0.6, 4.3, 11.5, 1.6, ['Design: half the teams see the card in a given week, chosen at random by team-week; the other half is the control.',
    'The gate sits at day 120 (60 days of pilot) to allow for clustering and the areas’ closure lag (most field outcomes close within three weeks).',
    'Dollar read-across at the gate: 20% avoided is about $160K a year; 35% is $287K; 50% is about $415K (scaled from the Monte Carlo).'], size=11.5, color=TXT, space_after=6)

s = appx('A5', 'what other cities show', 'APPENDIX A5 · PEER CITIES',
    'No city has published a measured drop in misroutes; **Edmonton would be early, not late**',
    'Team peer-city research, Nov 11, 2026 (edmonton-311-analysis/peer-cities/). Links: council.nyc.gov/data/311-agency; algoritmes.overheid.nl (Amsterdam gm0363 Signalen); Dallas City Auditor 311 SLA audit (Apr 2026); San Diego audit 22-009 (Jun 2022); toronto.ca backgroundfile-287175 (Apr 30, 2026); Denver Auditor statement (2025).')
prow3 = [['New York (2018)', '24.8% of complaints closed “Did Not Observe”, 18.7% “No Action”; 0.8% “Wrong Agency”', 'Empty visits dwarf misroutes'],
         ['Amsterdam (since 2022)', 'Model suggests a category; under 40% confidence goes to a human desk; corrections retrain it', 'Closest human-in-the-loop precedent'],
         ['Dallas (Apr 2026)', 'About 5% of requests transferred; 45% with no reason on file', 'Record a reason on every transfer'],
         ['San Diego (2022)', 'Auditors recommended screening low-priority code complaints before an inspector goes out', 'Same idea as the check'],
         ['Toronto (Apr 2026)', 'Intake redesign to cut misrouting; 600+ codes; no baseline or results yet', 'A Canadian peer working on it now'],
         ['Denver (2025)', 'Misroutes from inconsistent agent tools; 311 has no authority over agencies', 'Same authority split as Edmonton']]
table(s, 0.6, 2.35, [2.3, 6.4, 3.43], prow3, header_row=['CITY', 'WHAT WAS FOUND', 'LESSON FOR EDMONTON'], row_h=0.55, size=10.5, first_size=11)

s = appx('A6', 'every course concept, and what it changed', 'APPENDIX A6 · COURSE CONCEPTS',
    'Each concept earns its place by **changing a design choice**',
    'Group Project brief: concepts should change the work, not tour the syllabus. Sessions 8-10 entries follow the syllabus and will be updated after those sessions.')
crows = [['S1 · Three kinds of system; four agent questions; agency', '5, 7', 'Ratio + rule, no generative step; read-only, kill switch, agent decides'],
         ['S2 · Problem tree, profit tree, decision tree, premortem', '3, 4, 5, 11', 'MECE by stage; reconciling $287K; 2% floor; staged options'],
         ['S3 · Attention, feedback, anchoring, biases', '12, 14', 'One question; reason back in a day; no pre-selected answer'],
         ['S4 · Political game, where you stand, foresight', '13, 15', 'Areas write the questions; asks in order; 2030 CRM requirements'],
         ['S5 · Disaggregate; what data cannot show', '8, 16', 'Per-code rates; gaps said first; judge vs control'],
         ['S6 · Data is built; metric slightly wrong', '9, 10', 'Required reason; 90-day labelled set; re-contact pairing'],
         ['S7 · Ostensive / performative / artifact; Ironstone', '6', 'Card as new artifact; co-design with senior agents'],
         ['S8-S10 · Direct AI; proxy drift; what to refuse', '7, 16, 18', 'Zero refused referrals; guardrails not targets; never auto-decline']]
table(s, 0.6, 2.35, [4.6, 1.3, 6.23], crows, header_row=['SESSION · CONCEPT', 'SLIDES', 'THE DESIGN CHOICE IT CHANGED'], row_h=0.47, size=10.5, first_size=10.5, first_font=BODY)

s = appx('A7', 'sources', 'APPENDIX A7 · SOURCES',
    'Every number traces to open data, a City document, or **a labelled assumption**',
    'Full October source list: Team 2 SAI deck, Appendix H.')
tb(s, 0.6, 2.35, 5.9, 4.2, [
    ('DATA AND CITY DOCUMENTS', {'font': MONO, 'size': 9, 'bold': True, 'color': RED, 'space_after': 4}),
    ('City of Edmonton, 311 Requests open data (q7ua-agfg), data.edmonton.ca/d/q7ua-agfg, export Nov 7, 2026; yearly datasets 2016-2022.', {'space_after': 4}),
    ('City of Edmonton, CSD03148, 311 Service Experience (Sep 2, 2026) and Att. 1-2.', {'space_after': 4}),
    ('Office of the City Auditor (2023). City’s Response to 311 Requests (Nov 14, 2023).', {'space_after': 4}),
    ('City of Edmonton, Generative AI Standard (Jul 25, 2024); Privacy Impact Assessment standard (May 13, 2026); 2026 operating budget, 311 and Customer Access $14.66M.', {'space_after': 4}),
    ('CSU 52 collective agreement 2024-2027, Art. 11.03.', {'space_after': 4}),
    ('Team 2 (2026, Oct 26). Strategic Analytics Initiative deck, SEM 620.', {}),
], size=11, color=TXT)
line(s, 6.66, 2.4, 6.66, 6.1, color=LINE)
tb(s, 6.9, 2.35, 5.8, 4.2, [
    ('COURSE READINGS', {'font': MONO, 'size': 9, 'bold': True, 'color': RED, 'space_after': 4}),
    ('Glaser, V. L. (2026). The Reassembly of Agency; Analytic Trees; The Psychological Perspective. SEM 620, University of Alberta.', {'space_after': 4}),
    ('SEM 620 Sessions 4-7 slides; Group Project brief (2026).', {'space_after': 4}),
    ('Feldman and Pentland (2003); Kahneman and Klein (2009); Klein (2007) premortem; Bucinca et al. (2021).', {'space_after': 8}),
    ('PEER CITIES', {'font': MONO, 'size': 9, 'bold': True, 'color': RED, 'space_after': 4}),
    ('NYC Council 311 agency analysis; Amsterdam Signalen (algoritmes.overheid.nl gm0363); Dallas City Auditor (Apr 2026); San Diego audits 22-009, 23-004; City of Toronto (Apr 30, 2026); Denver Auditor (2025). Full links: Appendix A5 and the team’s peer-city file.', {}),
], size=10, color=TXT)
