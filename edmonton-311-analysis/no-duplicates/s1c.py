import duckdb, pandas as pd, numpy as np, sys
con=duckdb.connect('311.duckdb',read_only=True)
VISIT=["Does Not Meet Bylaw Offence Standards","Assessed-No Action Required","Unable to Locate Animal","Location Not Found","Unable to Contact Complainant"]
DUPS=["Duplicate Request Exists","Duplicate Request","Duplicate Request - See Related Ticket in Details","File Already under Investigation"]
DESK_ALL=["311 Redirecting to Other Business Area","Non-City Service or Location","Reported on same day - must submit after 10pm"]+DUPS
mode=sys.argv[1]
DESK=DESK_ALL if mode=='with' else [x for x in DESK_ALL if x not in DUPS]
v="','".join(VISIT); d="','".join(DESK); u="','".join(DUPS)
df=con.execute(f"""select yr, code, any_value(area) area, count(*) n, sum((sd in ('{v}'))::int) wv, sum((sd in ('{d}'))::int) wd, sum((sd in ('{u}'))::int) wu from p where yr in (2025,2026) group by yr, code""").df()
for y in (2025,2026):
  s=df[df.yr==y]; print(y,'referrals',s.n.sum(),'visit',s.wv.sum(),'desk',s.wd.sum(),'dups',s.wu.sum(),
     'rates',round(100*s.wv.sum()/s.n.sum(),2),round(100*s.wd.sum()/s.n.sum(),2),round(100*(s.wv.sum()+s.wd.sum())/s.n.sum(),2))
tr=df[df.yr==2025].set_index('code'); te=df[df.yr==2026].set_index('code').copy()
for col in ('wv','wd'):
  mu=tr[col].sum()/tr.n.sum(); k=10; a0=mu*k
  rate=(tr[col]+a0)/(tr.n+k)
  te['s_'+col]=te.index.map(lambda c: rate.get(c,mu)).astype(float)
  print(col,'prior',round(mu,4))
te['w']=te.wv+te.wd; te['s']=te.s_wv+te.s_wd
out=[]
for th in [0.10,0.15,0.20,0.25,0.30,0.40,0.50]:
  f=te[te.s>th]
  out.append(dict(th=th,codes=len(f),flag_pct=round(100*f.n.sum()/te.n.sum(),1),flagged=int(f.n.sum()),visit_caught=int(f.wv.sum()),visit_pct=round(100*f.wv.sum()/te.wv.sum(),1),desk_pct=round(100*f.wd.sum()/max(te.wd.sum(),1),1),prec=round(100*f.w.sum()/f.n.sum(),1),empty_rate=round(100*f.wv.sum()/f.n.sum(),1)))
print(pd.DataFrame(out).to_string())
print('tiers green/amber/red', [round(100*te[m].n.sum()/te.n.sum(),1) for m in (te.s<=0.2,(te.s>0.2)&(te.s<=0.3),te.s>0.3)])
months=10.2; ann=12/months
rng=np.random.default_rng(20261110); N=50000
tri=lambda a,m,b: rng.triangular(a,m,b,N)
for th in [0.20,0.30]:
  f=te[te.s>th]; FV=f.wv.sum()*ann; FD=f.wd.sum()*ann; FL=f.n.sum()*ann
  visit=tri(22,84,280); desk=tri(5,10,20)/60*tri(36.93,41.99,52.09)
  avoid=tri(0.2,0.35,0.5); ask=tri(0.30,1.02,1.02)
  fv=FV*avoid*(visit+desk); fd=FD*avoid*(desk+16.29*0.25)
  sav=fv+fd; cost=FL*ask; net=sav-cost
  q=lambda x: f"mean {np.mean(x)/1e3:,.0f}K med {np.median(x)/1e3:,.0f}K P10 {np.percentile(x,10)/1e3:,.0f}K P90 {np.percentile(x,90)/1e3:,.0f}K"
  print(f'th {th}: flagged/yr {FL:,.0f} visits/yr {FV:,.0f} desk/yr {FD:,.0f} | fieldsav {np.mean(fv)/1e3:.0f}K desksav {np.mean(fd)/1e3:.0f}K | gross {q(sav)} | cost {np.mean(cost)/1e3:.0f}K | net {q(net)} | P<0 {np.mean(net<0):.2%}')
  # break-even avoided share
  per_visit=np.mean(visit+desk); per_desk=np.mean(desk+16.29*0.25); be=np.mean(cost)/(FV*per_visit+FD*per_desk)
  print('  break-even avoided', round(100*be,2),'%  visits avoided', round(FV*.35), 'desk avoided', round(FD*.35), 'cost/visit', round(per_visit,1), 'per desk', round(per_desk,2),'ask mean',round(np.mean(ask),2))
  # sensitivity: halve visit cost
  sav2=FV*avoid*(visit/2+desk)+fd; print('  halve visit cost net', round(np.mean(sav2-cost)/1e3),'K; agent-only', round(np.mean(sav-FL*0.30)/1e3),'K; desk out', round(np.mean(fv-cost)/1e3),'K')
f=te[te.s>0.2]
a=f.groupby('area')[['n','wv']].sum().sort_values('wv',ascending=False); a['share']=(100*a.wv/a.wv.sum()).round(0); print(a.head(8).to_string())
print('gate baseline: empty visits in flagged', int(f.wv.sum()),'of',int(f.n.sum()), round(100*f.wv.sum()/f.n.sum(),1),'% ; per month flagged', round(f.n.sum()/months))
print('untidy', te.loc[[c for c in te.index if 'Untidy' in c],['n','wv','wd','s']].to_string())
