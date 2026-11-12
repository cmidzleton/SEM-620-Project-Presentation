import duckdb, pandas as pd, numpy as np
con=duckdb.connect('data/311.duckdb',read_only=True)
VISIT=["Does Not Meet Bylaw Offence Standards","Assessed-No Action Required","Unable to Locate Animal","Location Not Found","Unable to Contact Complainant"]
v="','".join(VISIT)
c=con.execute(f"""select yr, coalesce(area,'?')||' | '||coalesce(cat,'?')||' | '||coalesce(descr,'?') code, sum(n) n, coalesce(sum(n) filter (where sd in ('{v}')),0) b from agg where ch='Phone Call' and rt='Referral' and yr between 2016 and 2026 group by all""").df()
def auc(s,n,b):
  d=pd.DataFrame({'s':s,'p':b,'q':n-b}).groupby('s').sum().sort_index(); cq=d.q.cumsum()-d.q
  return (d.p*(cq+0.5*d.q)).sum()/(d.p.sum()*d.q.sum())
print(c.groupby('yr')[['n','b']].sum().assign(rate=lambda x: (100*x.b/x.n).round(2)))
for Y in range(2017,2027):
  tr=c[c.yr==Y-1].groupby('code')[['n','b']].sum(); mu=tr.b.sum()/tr.n.sum(); r=(tr.b+mu*10)/(tr.n+10)
  te=c[c.yr==Y]; s=te.code.map(r).fillna(mu).values
  flag=s>0.2
  print(Y, 'AUC',round(auc(s,te.n.values,te.b.values),3), 'flag>20% calls',round(te.n[flag].sum()/te.n.sum()*100,1),'caught',round(te.b[flag].sum()/te.b.sum()*100,1))
p=con.execute(f"select code, count(*) n, sum((sd in ('{v}'))::int) b from p where yr=2025 and descr='Complaint Registered - Untidy Property' group by 1").df(); print(p)
