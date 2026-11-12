import duckdb, pandas as pd, numpy as np, re
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
con=duckdb.connect('data/311.duckdb')
STOP=set('311 the a of and or to for in on request general inquiry policy callback no other minor - : / required'.split())
def norm(s):
  s=str(s or "").lower(); s=re.sub(r'^[a-z ]{2,12}:\s*','',s); s=re.sub(r'^311\s*-?\s*','',s)
  toks=[t for t in re.findall(r'[a-z]+',s) if t not in STOP and len(t)>2]
  return frozenset(t[:-1] if t.endswith('s') and len(t)>4 else t for t in toks)
codes=con.execute("select area, cat, descr, code, count(*) n, sum(bounced) b from p where yr in (2025) and descr is not null group by all").df()
codes['tok']=codes.descr.map(norm)
# sibling: another code from a different area with token Jaccard >= 0.5 (and nonempty)
recs=codes.to_dict('records'); sib={}
for i,a in enumerate(recs):
  s=[]
  for j,c in enumerate(recs):
    if i==j or a['area']==c['area'] or not a['tok'] or not c['tok']: continue
    J=len(a['tok']&c['tok'])/len(a['tok']|c['tok'])
    if J>=0.5: s.append(c['code'])
  sib[a['code']]=s
codes['n_sib']=codes.code.map(lambda c: len(sib[c]))
codes['has_sib']=codes.n_sib>0
g=codes.groupby('has_sib')[['n','b']].sum(); g['rate%']=100*g.b/g.n; g['codes']=codes.groupby('has_sib').size()
print('2025 phone referrals by sibling ambiguity\n',g)
print(codes[codes.has_sib].sort_values('b',ascending=False).head(20)[['code','n','b','n_sib']].to_string())
pd.DataFrame([(c,'; '.join(s)) for c,s in sib.items() if s],columns=['code','siblings']).to_csv('out/sibling_codes_2025.csv',index=False)
# ticket-level model: features from 2025, test on 2026
a0,b0,mu=__import__('pickle').load(open('out/prior.pkl','rb'))
codes['eb']=(codes.b+a0)/(codes.n+a0+b0)
# app bounce rate for same code (cross-channel)
app=con.execute(f"""select area||' | '||cat||' | '||descr code, count(*) an, sum((sd='311 Redirecting to Other Business Area')::int) ab from t2 where ch='Mobile App' and rt='Referral' and yr=2025 group by 1""").df()
app['app_eb']=(app.ab+a0)/(app.an+a0+b0)
area=con.execute("select area, count(*) an_, sum(bounced) ab_ from p where yr=2025 group by 1").df(); area['area_rate']=(area.ab_+1)/(area.an_+100)
te=con.execute("select code, area, bounced from p where yr=2026").df()
X=te.merge(codes[['code','eb','n','n_sib']],on='code',how='left').merge(app[['code','app_eb']],on='code',how='left').merge(area[['area','area_rate']],on='area',how='left')
X['new_code']=X.eb.isna().astype(int); X['eb']=X.eb.fillna(mu); X['n']=X.n.fillna(0); X['n_sib']=X.n_sib.fillna(0); X['app_eb']=X.app_eb.fillna(mu); X['area_rate']=X.area_rate.fillna(mu)
print('AUC eb only 2026:',roc_auc_score(X.bounced,X.eb))
F=['eb','logn','has_sib','app_eb','area_rate','new_code']
X['logn']=np.log1p(X.n); X['has_sib']=(X.n_sib>0).astype(int)
# train LR on 2025 tickets with features from 2024 to avoid leakage
codes24=con.execute("select area, code, count(*) n, sum(bounced) b from p where yr=2024 group by all").df(); codes24['eb']=(codes24.b+a0)/(codes24.n+a0+b0)
app24=con.execute(f"""select area||' | '||cat||' | '||descr code, count(*) an, sum((sd='311 Redirecting to Other Business Area')::int) ab from t2 where ch='Mobile App' and rt='Referral' and yr=2024 group by 1""").df(); app24['app_eb']=(app24.ab+a0)/(app24.an+a0+b0)
area24=con.execute("select area, count(*) an_, sum(bounced) ab_ from p where yr=2024 group by 1").df(); area24['area_rate']=(area24.ab_+1)/(area24.an_+100)
tr=con.execute("select code, area, bounced from p where yr=2025").df()
T=tr.merge(codes24[['code','eb','n']],on='code',how='left').merge(app24[['code','app_eb']],on='code',how='left').merge(area24[['area','area_rate']],on='area',how='left')
T['new_code']=T.eb.isna().astype(int); T['eb']=T.eb.fillna(mu); T['n']=T.n.fillna(0); T['app_eb']=T.app_eb.fillna(mu); T['area_rate']=T.area_rate.fillna(mu); T['logn']=np.log1p(T.n)
T['has_sib']=T.code.map(lambda c: int(len(sib.get(c,[]))>0))
lr=LogisticRegression(max_iter=1000,class_weight=None).fit(T[F],T.bounced)
pr=lr.predict_proba(X[F])[:,1]
print('AUC LR (train 2025 w/ 2024 feats, test 2026 w/ 2025 feats):',roc_auc_score(X.bounced,pr))
print(dict(zip(F,lr.coef_[0].round(3))))
# top-k capture
X['pr']=pr
for k in [0.01,0.02,0.05,0.10,0.20]:
  cut=X.pr.quantile(1-k); f=X[X.pr>=cut]
  print(f'top {k:.0%} tickets: capture {f.bounced.sum()/X.bounced.sum():.1%}, precision {f.bounced.mean():.2%}')
# 2026 bounces from codes unseen in 2025, and areas new
print('2026 bounces on codes not seen in 2025 phone:',X[X.new_code==1].bounced.sum(), 'of', X.bounced.sum())
