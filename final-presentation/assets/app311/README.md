# Referral Check deck, Edmonton 311 app style

Built Nov 11, 2026 for the SEM 620 final presentation (Dec 7, 2026). Delivered as `V6 Referral-Check-311-app-deck.pptx`.

## What is here

| File | What it does |
| --- | --- |
| `figs.py` | Computes every figure on the slides from the team's six-part export of 311 Requests open data (q7ua-agfg). `figures(cut, red)` returns one dictionary. Duplicate-type closures are left out. |
| `charts3.py` | Draws the five charts from that dictionary into `img3/`. |
| `lib3.py` | Slide library: template look (T2 Contrarian Thesis), app header, bus tab bar, push transitions, clickable navigation, font embedding. |
| `build3.py` | The deck itself: 17 core slides, agenda, five section dividers, appendix index, A1 to A8. Text reads its numbers from `figs.py`. |
| `fonts/` | Quattrocento Sans as the template embeds it (`.fntdata`) and as TTF. |
| `template-T2_Contrarian_Thesis.pptx` | The template Curtis supplied. |
| `setup.sh` | Recreates the working layout under `/tmp/claude-0/sc` and rebuilds the deck. |

Related: `edmonton-311-analysis/scripts/hist.py` (ten-year check of the score), `hist_pull.py` (pulls 2016 to 2022 from the yearly open datasets), `edmonton-311-analysis/hist/agg_*.json` (the pulled counts), `edmonton-311-analysis/empty_visit_backtest_2017_2026.csv` (the result).

## Decisions baked in

- Duplicates are out of every figure (Curtis, Nov 11): the three Duplicate Request labels and File Already under Investigation.
- The cut-off stays at 20% (Curtis chose this on Nov 11 over a 15% line). To see another cut-off, run `python3 figs.py 0.15 0.25`.
- Headline at 20%: 84 codes, 10.7% of phone referrals flagged, 50.2% of empty visits caught, net $287K a year (P10 to P90 $130K to $477K).

## Still open

- The closing slide shows a drawn placeholder for Mayor Knack. Swap in a photo (the notes on that slide say how).
- The blue (0057B8) approximates the City's brand blue; edmonton.ca could not be reached from the build session to confirm the hex.
- The AI Process Reflection slide is a draft the team must rewrite in its own voice.
