import duckdb, pandas as pd, numpy as np
con=duckdb.connect('data/311.duckdb')
con.execute("""create or replace table agg as
select try_cast(year as int) yr, interaction_channel ch, referral_type rt, service_area area, service_category cat, service_description descr, status_detail sd, try_cast(nd as bigint) n from read_csv('hagg/*.csv',header=true,all_varchar=true)
union all select yr, ch, rt, area, cat, descr, sd, count(*) from h group by all""")
B='311 Redirecting to Other Business Area'
y=con.execute(f"""select yr, sum(n) total, sum(n) filter (where ch='Phone Call') phone, sum(n) filter (where ch='Phone Call' and rt='Referral') pref,
 sum(n) filter (where ch='Phone Call' and rt='Referral' and sd='{B}') pb, sum(n) filter (where sd='{B}') allb,
 count(distinct area) filter (where ch='Phone Call' and rt='Referral' and sd='{B}') areas_rec,
 count(distinct coalesce(area,'')||cat||descr) filter (where ch='Phone Call') phone_codes
 from agg where yr between 2016 and 2026 group by 1 order by 1""").df()
y['rate%']=100*y.pb/y.pref
print(y.to_string())
y.to_csv('out/yearly_2016_2026.csv',index=False)
c=con.execute(f"""select yr, coalesce(area,'?')||' | '||coalesce(cat,'?')||' | '||coalesce(descr,'?') code, sum(n) n, sum(n) filter (where sd='{B}') b from agg where ch='Phone Call' and rt='Referral' and yr between 2016 and 2026 group by all""").df().fillna({'b':0})
a0,b0=0.0051*9.6,(1-0.0051)*9.6
def auc_grouped(score,n,b):
  # AUC from grouped: positives b, negatives n-b, ties half
  d=pd.DataFrame({'s':score,'p':b,'q':n-b}).groupby('s').sum().sort_index()
  cq=d.q.cumsum()-d.q; P=d.p.sum(); Q=d.q.sum()
  return ((d.p*(cq+0.5*d.q)).sum())/(P*Q)
rows=[]
for Y in range(2017,2027):
  for k in (1,3):
    tr=c[(c.yr<Y)&(c.yr>=Y-k)].groupby('code')[['n','b']].sum()
    te=c[c.yr==Y].set_index('code')
    tr_rate=(tr.b+a0)/(tr.n+a0+b0)
    s=te.index.map(lambda x: tr_rate.get(x, a0/(a0+b0)))
    te=te.assign(s=np.array(s,dtype=float))
    new=~te.index.isin(tr.index)
    flag=te.s>0.02
    rows.append(dict(test_year=Y,train_years=k,auc=round(auc_grouped(te.s.values,te.n.values,te.b.values),3),
      bounces=int(te.b.sum()),pct_flagged=round(100*te.n[flag].sum()/te.n.sum(),1),pct_caught=round(100*te.b[flag].sum()/max(te.b.sum(),1),1),
      new_code_share_b=round(100*te.b[new].sum()/max(te.b.sum(),1),1)))
r=pd.DataFrame(rows); print(r.to_string()); r.to_csv('out/stability_backtest_2017_2026.csv',index=False)
# persistence of top codes
top=c[c.yr<=2025].groupby(['code','yr'])[['n','b']].sum().reset_index()
cans=c[c.code.str.contains('Empty Existing Garbage Can|Request New Garbage Can|Parking Lot \\| 311 Parking Lot|SIGNS:Sign Required')].pivot_table(index='code',columns='yr',values=['b','n'],aggfunc='sum')
print(cans.fillna(0).astype(int).to_string())
