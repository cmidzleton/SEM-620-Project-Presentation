# Referral Check re-run with duplicates excluded (Nov 11, 2026)

Curtis (Nov 11): duplicates out of the savings, because the City is already working on them.
Source: 311 Requests open data (q7ua-agfg), team six-part export (Nov 7, 2026), phone referrals, deduplicated by Row ID.
Scripts: s1c.py (`with` / `without` duplicates, 20%/30% cut-offs), s1d.py (without, 15%/25% cut-offs). Baseline reproduced exactly (191,521 / 12,583 / 7,815; net $375K).

Excluded as duplicates: "Duplicate Request Exists", "Duplicate Request", "Duplicate Request - See Related Ticket in Details", and "File Already under Investigation" (an existing file, so functionally a duplicate). 6,249 phone referrals in 2025, 5,100 in 2026 to Nov 6.
Desk waste kept: 311 Redirecting (bounce), Non-City Service or Location, Reported on same day.

- Wasted share of phone referrals without duplicates: 7.4% (2025), 7.3% (2026). Empty field visits unchanged: 5.9% (2026), 10,609.
- Same 20% cut-off without duplicates: 84 codes, 10.7% of calls, 50% of empty visits, net $287K (P10-P90 $130K-$477K). Duplicates had inflated the scores.
- Chosen cut-off re-set to 15% to keep reach: 142 codes, 17.1% of 2026 phone referrals, 63.7% of empty visits (6,759 of 10,609); 25.0% of flagged referrals end in waste; empty-visit rate in flagged set 22.1% (gate baseline).
- Monte Carlo (same inputs, seed 20261110): net mean $359K, median $331K, P10-P90 $160K-$601K, no draw below zero. Gross $387K (field $383K = 2,783 visits x $137.5; desk $5K = 367 x $12.55). Check cost $28K (36,049 flagged calls/yr x $0.78). Break-even 2.5% avoided. Halve visit cost $180K; agent-only pricing $376K; desk row out $354K.
- Red tier at 25%: 52 codes, 8.8% of calls, 43.9% of empty visits, net $251K if only red were checked. Tiers: green 82.9%, amber 8.3%, red 8.8%.
- Flagged empty visits by area: Municipal Enforcement 42%, Peace Officers 21%, Roadway Maintenance 21%, Parking 8% (three pilot areas = 71%).
- Untidy Property score 29.9% without duplicates (40.5% with): red at the 25% line. 1,350 of 4,877 (28%) empty.
- Pilot power: ~3,000 flagged calls/month, 20% relative drop (22.1% -> 17.7%) needs ~1,280 per arm, ~0.85 months; day-120 gate still fine.

## Decision (Curtis, Nov 11, 2026): lead with the 20% line, $287K
Net mean $287K (median $265K, P10-P90 $130K-$477K); gross $304K (field $301K = 2,193 visits x $137; desk $3K); check $17K (22,459 flagged calls/yr). 84 codes, 10.7% of calls, 50.2% of empty visits (5,326 of 10,609), 30.7% waste in flagged set, baseline 27.9%, ~1,870 flagged/month, 20% drop reads out in ~1 month (~950 per arm). Tiers: green 89.3%, amber 6.5%, red (>30%) 4.2% / 28.1% of empty visits. Break-even 2.0%. Pilot areas ME 39%, PO 27%, Parking 10% = 76%. Untidy Property score 29.9% = amber. Day-90 set ~3,700 logged; gate 3,500+ labelled.
Empty-visit score AUC (ticket level, prior-year rate, ties half): 0.862 (2026), 0.888 (2025), 0.915 (2024); 0.86-0.92 every year 2017-2026 (empty_visit_backtest_2017_2026.csv). An earlier line here said 0.82/0.84/0.88; that came from a faulty calculation and is withdrawn.
