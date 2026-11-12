#!/usr/bin/env bash
# Rebuilds the Referral Check deck in the Edmonton 311 app style (the "V6" deck of Nov 11, 2026) from the project folder.
# The scripts keep their working files under /tmp/claude-0/sc; this script recreates that layout, then builds.
# Needs: python3 with python-pptx, pandas, numpy, scipy, matplotlib, pillow.
set -euo pipefail
A=/mnt/project-files/final-presentation/assets/app311
E=/mnt/project-files/edmonton-311-analysis
W=/tmp/claude-0/sc
mkdir -p $W/build/img3 $W/nd $W/hist $W/tpl/x/ppt/fonts /root/.fonts/qs
cp $A/build3.py $A/lib3.py $A/charts3.py $A/figs.py $W/build/
cp $A/fonts/*.fntdata $W/tpl/x/ppt/fonts/          # the template's embedded Quattrocento Sans, copied into the deck
cp $A/fonts/*.ttf /root/.fonts/qs/                 # the same font as TTF, for text measuring and charts
fc-cache -f >/dev/null 2>&1 || true
cp $E/hist/agg_*.json $W/hist/                     # 2016-2022 phone referrals by code and closure label (yearly open datasets)
cp $E/scripts/hist.py $E/scripts/load23.py $W/hist/
# phone referrals 2023-2026 from the team's six-part export (each loader reads 3.5M rows; a few minutes)
[ -f $W/nd/p.pkl ]    || (cd $W/nd && python3 $E/scripts/s1c_load_from_csv.py)
[ -f $W/nd/p24.pkl ]  || (cd $W/nd && python3 $E/scripts/load24.py)
[ -f $W/hist/p23.pkl ] || python3 $W/hist/load23.py
python3 $W/hist/hist.py > $W/hist/hist_out.txt     # ten-year check, writes empty_visit_backtest_2017_2026.csv
cd $W/build
python3 figs.py 0.20 0.30                          # prints every figure on the slides (amber line 20%, red line 30%)
python3 charts3.py                                 # charts into img3/
python3 build3.py                                  # deck at /tmp/claude-0/sc/build/v3.pptx
echo "built $W/build/v3.pptx"
