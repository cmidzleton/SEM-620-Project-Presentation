import duckdb, pandas as pd, numpy as np
con=duckdb.connect('data/311.duckdb',read_only=True)
VISIT=["Does Not Meet Bylaw Offence Standards","Vehicle Gone Upon Arrival","Assessed-No Action Required","Unable to Locate Animal","Location Not Found","Unable to Contact Complainant"]
DESK=["311 Redirecting to Other Business Area","Non-City Service or Location","Duplicate Request Exists","Duplicate Request","Duplicate Request - See Related Ticket in Details","File Already under Investigation","Reported on same day - must submit after 10pm"]
v="','".join(VISIT); d="','".join(DESK)
df=con.execute(f"""select yr, code, count(*) n, sum((sd in ('{v}'))::int) wv, sum((sd in ('{d}'))::int) wd from p where yr in (2025,2026) group by all""").df()
for y in (2025,2026):
  s=df[df.yr==y]; print(y,'referrals',s.n.sum(),'wasted-visit',s.wv.sum(),'wasted-desk',s.wd.sum())
tr=df[df.yr==2025].set_index('code'); te=df[df.yr==2026].set_index('code')
res={}
for col in ('wv','wd'):
  mu=tr[col].sum()/tr.n.sum(); k=10; a0,b0=mu*k,(1-mu)*k
  rate=(tr[col]+a0)/(tr.n+a0+b0)
  te['s_'+col]=te.index.map(lambda c: rate.get(c,mu)).astype(float)
  print(col,'base rate',round(mu,4))
te['w']=te.wv+te.wd
# flag: code expected wasted rate (visit+desk) above thresholds
te['s']=te.s_wv+te.s_wd
out=[]
for th in [0.10,0.20,0.30,0.40]:
  f=te[te.s>th]
  out.append(dict(th=th,codes=len(f),flag_pct=round(100*f.n.sum()/te.n.sum(),1),flagged=int(f.n.sum()),visit_caught=int(f.wv.sum()),visit_pct=round(100*f.wv.sum()/te.wv.sum(),1),desk_caught=int(f.wd.sum()),prec=round(100*f.w.sum()/f.n.sum(),1)))
print(pd.DataFrame(out).to_string())
months=10.2; ann=12/months
rng=np.random.default_rng(20261110); N=50000
tri=lambda a,m,b: rng.triangular(a,m,b,N)
for th in [0.20,0.30]:
  f=te[te.s>th]; FV=f.wv.sum()*ann; FD=f.wd.sum()*ann; FL=f.n.sum()*ann
  visit=tri(22,84,280); desk=tri(5,10,20)/60*tri(36.93,41.99,52.09)
  avoid=tri(0.2,0.35,0.5)      # share of flagged wasted referrals avoided by the intake check
  ask=tri(0.30,1.02,1.02)      # agent time per flagged call (deck: $0.30 agent-only, $1.02 avg contact)
  sav=FV*avoid*(visit+desk)+FD*avoid*(desk+16.29*0.25)
  cost=FL*ask
  net=sav-cost
  q=lambda x: f"${np.mean(x)/1e3:,.0f}K (P10-P90 ${np.percentile(x,10)/1e3:,.0f}K-${np.percentile(x,90)/1e3:,.0f}K)"
  print(f'th {th}: flagged/yr {FL:,.0f}; wasted visits in flagged/yr {FV:,.0f}; gross {q(sav)}; ask cost {q(cost)}; net {q(net)}; P(net<0)={np.mean(net<0):.1%}')
# top flagged codes for th .3
print(te[te.s>0.3].sort_values('wv',ascending=False).head(12)[['n','wv','wd','s']].to_string())
