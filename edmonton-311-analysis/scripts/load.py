import duckdb,sys
con=duckdb.connect('data/311.duckdb')
con.execute("""create or replace table t as select *, year(date_created::timestamp) yr from read_csv('data/y*.csv', header=true, all_varchar=true)""")
con.execute("""create or replace table t2 as select row_id, date_created::timestamp dc, try_cast(date_closed as timestamp) dcl, request_status st, status_detail sd, service_category cat, service_description descr, interaction_channel ch, service_area area, referral_type rt, neighbourhood_id nid, ward, year(date_created::timestamp) yr from t""")
con.execute("drop table t")
print(con.execute("select count(*), count(distinct row_id) from t2").fetchall())
for q in ["select rt,count(*) from t2 where yr=2025 group by 1 order by 2 desc",
"select sd,count(*) from t2 where yr=2025 group by 1 order by 2 desc limit 40",
"select st,count(*) from t2 group by 1",
"select count(*) filter (where nid is null)*1.0/count(*), count(*) filter (where dcl is null and st='Closed') from t2"]:
  print(q);[print(r) for r in con.execute(q).fetchall()]
