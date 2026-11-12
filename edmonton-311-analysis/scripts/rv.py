import duckdb, pandas as pd, numpy as np, math
con=duckdb.connect('data/311.duckdb',read_only=True)
VISIT=["Does Not Meet Bylaw Offence Standards","Assessed-No Action Required","Unable to Locate Animal","Location Not Found","Unable to Contact Complainant"]
DESK=["311 Redirecting to Other Business Area","Non-City Service or Location","Reported on same day - must submit after 10pm"]
v="','".join(VISIT); d="','".join(DESK)
print(con.execute("select sd, count(*) from p where yr=2026 and descr='Complaint Registered - Untidy Property' group by 1 order by 2 desc limit 8").fetchall())
print(con.execute(f"select yr, count(*), sum((sd in ('{v}'))::int), sum((sd='Does Not Meet Bylaw Offence Standards')::int), sum((sd='Unable to Contact Complainant')::int), sum((sd in ('{d}'))::int) from p where yr in (2025,2026) group by 1").fetchall())
df=con.execute(f"select yr, code, area, count(*) n, sum((sd in ('{v}'))::int) wv, sum((sd in ('{d}'))::int) wd from p where yr in (2025,2026) group by all").df()
tr=df[df.yr==2025].groupby('code')[['n','wv','wd']].sum(); te=df[df.yr==2026].copy()
for c in ('wv','wd'):
  mu=tr[c].sum()/tr.n.sum(); a0,b0=mu*10,(1-mu)*10; r=(tr[c]+a0)/(tr.n+a0+b0)
  te['s_'+c]=te.code.map(r).fillna(mu); print(c,'prior',round(mu,4))
te['s']=te.s_wv+te.s_wd
N=te.n.sum(); WV=te.wv.sum()
for th in (0.2,0.3):
  f=te[te.s>th]; print(f'>{th}: codes {f.code.nunique()}, flagged {f.n.sum()} ({f.n.sum()/N:.1%}), visits {f.wv.sum()} of {WV} ({f.wv.sum()/WV:.1%}), visit-rate in set {f.wv.sum()/f.n.sum():.1%}, waste rate {(f.wv.sum()+f.wd.sum())/f.n.sum():.1%}')
f=te[te.s>0.2]; a=f.groupby('area')[['n','wv']].sum().sort_values('wv',ascending=False); a['share']=a.wv/a.wv.sum(); print(a.head(8))
print('base 2026 visit rate',WV/N,'waste rate',(WV+te.wd.sum())/N)
red=te[te.s>0.3]; amb=te[(te.s>0.2)&(te.s<=0.3)]; print('red share calls',red.n.sum()/N,'visits',red.wv.sum()/WV,'amber calls',amb.n.sum()/N)
# power
def npa(p1,p2,za=1.96,zb=0.8416):
  pb=(p1+p2)/2; return ((za*math.sqrt(2*pb*(1-pb))+zb*math.sqrt(p1*(1-p1)+p2*(1-p2)))**2)/(p1-p2)**2
p1=f.wv.sum()/f.n.sum(); vol=f.n.sum()/10.2
for red_ in (0.2,0.35):
  n=npa(p1,p1*(1-red_)); print(f'power: base {p1:.1%} -{red_:.0%}: {n:.0f}/arm, {2*n/vol:.2f} months at {vol:.0f}/month')
