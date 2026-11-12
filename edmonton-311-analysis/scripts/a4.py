import duckdb, pandas as pd, numpy as np, math
con=duckdb.connect('data/311.duckdb'); q=lambda s: con.execute(s).df()
# concentration of 2025 phone referral bounces by code
c=q("select code, area, count(*) n, sum(bounced) b from p where yr=2025 group by all order by b desc")
c['cum']=c.b.cumsum()/c.b.sum()
for k in [10,25,50,100]: print(f'top {k} codes = {c.cum.iloc[k-1]:.1%} of 2025 phone referral bounces')
print('codes with >=1 bounce',(c.b>0).sum(),'of',len(c))
# by receiving area
a=q("select area, count(*) n, sum(bounced) b, 100.0*sum(bounced)/count(*) r from p where yr=2025 group by 1 order by b desc limit 12"); print(a.to_string())
# weekly baseline for SPC: always-recording 2026 Apr-Oct
w=q("select date_trunc('week',dc) wk, count(*) n, sum(bounced) b from p where dc>='2026-04-06' and dc<'2026-11-02' group by 1 order by 1")
pbar=w.b.sum()/w.n.sum(); nbar=w.n.mean()
print(f'weekly phone referral bounce rate Apr-Oct 2026: pbar={pbar:.3%}, n/wk={nbar:.0f}, 3-sigma UCL={pbar+3*math.sqrt(pbar*(1-pbar)/nbar):.3%} LCL={max(0,pbar-3*math.sqrt(pbar*(1-pbar)/nbar)):.3%}, weeks={len(w)}')
print('weekly min/max', (w.b/w.n).min(), (w.b/w.n).max())
# power: two-proportion, flagged codes baseline p1 at eb>2% threshold (precision 7.0%), detect 30% and 50% reduction
from math import sqrt
def n_per_arm(p1,p2,za=1.96,zb=0.8416):
  pb=(p1+p2)/2; return ((za*sqrt(2*pb*(1-pb))+zb*sqrt(p1*(1-p1)+p2*(1-p2)))**2)/(p1-p2)**2
for p1,lab,vol in [(0.0701,'flag tier eb>2%',11408/10.2),(0.1624,'flag tier eb>5.6%',2100/10.2)]:
  for red in [0.3,0.5]:
    n=n_per_arm(p1,p1*(1-red)); print(f'{lab}: base {p1:.1%}, detect -{red:.0%}: {n:.0f} tickets/arm -> {2*n/vol:.1f} months at {vol:.0f} flagged/month (50/50 split)')
# EV of 'ask first' using deck tree: cost $1.02/ask, halves wrong owners, bounce -$36.11
for th,flags,caught in [(0.02,11408,800),(0.056,2100,341)]:
  ann=12/10.2
  print(f'th {th}: annual flags {flags*ann:.0f}, bounces avoided {caught/2*ann:.0f}, $ saved {caught/2*36.11*ann:,.0f}, ask cost {flags*1.02*ann:,.0f} (agent-time-only {flags*0.30*ann:,.0f}), resident days avoided ~{caught/2*ann*q("select avg(epoch(dcl-dc)/86400) d from p where bounced=1 and yr=2026").d[0]:.0f}')
