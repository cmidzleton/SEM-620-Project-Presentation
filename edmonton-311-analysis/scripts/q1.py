import duckdb
con=duckdb.connect('data/311.duckdb')
def q(s):
  print('>>',s[:150]);
  for r in con.execute(s).fetchall(): print(r)
q("select count(distinct area||'|'||cat||'|'||descr), count(distinct cat||'|'||descr), count(distinct descr) from t2 where yr=2025 and ch='Phone Call'")
q("select rt, count(*), avg((nid is null)::int) from t2 where yr=2025 group by 1")
q("select ch, count(*) filter (where rt='Referral') ref, count(*) filter (where sd='311 Redirecting to Other Business Area') b from t2 where yr=2025 group by 1")
q("select rt, count(*) from t2 where yr=2025 and ch='Phone Call' and sd='311 Redirecting to Other Business Area' group by 1")
q("select descr, cat, area, count(*) n from t2 where yr=2025 and ch='Phone Call' and lower(descr) like '%garbage can%' or (yr=2025 and ch='Phone Call' and lower(descr) like '%can needs%') group by all order by n desc")
q("select max(dc) from t2")
