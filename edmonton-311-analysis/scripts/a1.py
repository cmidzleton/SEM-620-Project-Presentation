import duckdb, pandas as pd, numpy as np
con=duckdb.connect('data/311.duckdb')
B="'311 Redirecting to Other Business Area'"
con.execute("""create or replace table p as select *, coalesce(area,'?')||' | '||coalesce(cat,'?')||' | '||coalesce(descr,'?') code, coalesce(sd='311 Redirecting to Other Business Area',false)::int bounced, coalesce(sd='Non-City Service or Location',false)::int noncity from t2 where ch='Phone Call' and rt='Referral'""")
d=con.execute("""select code, area, descr, yr, count(*) n, sum(bounced) b from p group by all""").df()
# monthly phone referral bounce rate
m=con.execute("""select date_trunc('month',dc) m, count(*) n, sum(bounced) b, 100.0*sum(bounced)/count(*) r from p group by 1 order by 1""").df()
print(m.to_string())
# train 2025, test 2026
tr=d[d.yr==2025].groupby(['code','area','descr'],as_index=False)[['n','b']].sum()
te=d[d.yr==2026].groupby(['code'],as_index=False)[['n','b']].sum().rename(columns={'n':'n26','b':'b26'})
# empirical bayes beta prior via method of moments on codes with n>=20
x=tr[tr.n>=20]; r=x.b/x.n; mu=(x.b.sum()/x.n.sum()); var=np.average((r-mu)**2,weights=x.n)
# beta-binomial MoM approx
k=max(mu*(1-mu)/max(var - mu*(1-mu)/x.n.mean(),1e-6)-1,1)
a0,b0=mu*k,(1-mu)*k
print('prior mean',mu,'strength',k)
tr['eb']=(tr.b+a0)/(tr.n+a0+b0)
mg=te.merge(tr,on='code',how='left')
mg['eb']=mg.eb.fillna(mu)
tot_n=mg.n26.sum(); tot_b=mg.b26.sum()
print('2026 phone referrals',tot_n,'bounces',tot_b,'codes',len(mg))
rows=[]
for th in [0.005,0.01,0.02,0.03,0.056,0.08,0.1,0.2]:
  f=mg[mg.eb>th]
  rows.append(dict(th=th,codes=len(f),tickets_flagged=f.n26.sum(),pct_tix=100*f.n26.sum()/tot_n,bounces_caught=f.b26.sum(),pct_b=100*f.b26.sum()/tot_b,prec=100*f.b26.sum()/max(f.n26.sum(),1)))
print(pd.DataFrame(rows).to_string())
mg.sort_values('eb',ascending=False).head(30)[['code','n','b','eb','n26','b26']].to_csv('out/top_risk_codes.csv',index=False)
print(mg.sort_values('eb',ascending=False).head(25)[['code','n','b','eb','n26','b26']].to_string())
tr.to_csv('out/code_eb_2025.csv',index=False)
import pickle; pickle.dump((a0,b0,mu),open('out/prior.pkl','wb'))
