import duckdb, pandas as pd, numpy as np
con=duckdb.connect('data/311.duckdb')
q=lambda s: con.execute(s).df()
# feedback latency: phone bounces 2025-2026, hours from created to closed
print(q("""select yr, count(*) n, median(epoch(dcl-dc)/86400) med_days, avg((epoch(dcl-dc)<=86400)::int) within1d, avg((epoch(dcl-dc)<=3*86400)::int) within3d, avg((epoch(dcl-dc)>7*86400)::int) over7d, sum(epoch(dcl-dc)/86400) days_sum from p where bounced=1 and dcl is not null group by 1 order by 1""").to_string())
# re-route reconstruction: for each phone bounce with nid, is there a new ticket (any channel, referral) created within [close-1h, close+72h] in same nid, different area, same cat OR desc shares a word?
con.execute("create or replace table bnc as select row_id, dc, dcl, nid, area, cat, descr, yr from p where bounced=1 and nid is not null and dcl is not null and yr>=2025")
con.execute("create or replace table cand as select row_id, dc, nid, area, cat, descr from t2 where yr>=2025 and nid is not null")
def match(shift_days):
  return q(f"""select count(distinct b.row_id) m from bnc b join cand c on c.nid=b.nid and c.area<>b.area
  and c.dc between b.dcl - interval 1 hour + to_days({shift_days}) and b.dcl + interval 72 hour + to_days({shift_days})
  and (c.cat=b.cat or regexp_extract(lower(b.descr),'(can|sign|graffiti|tree|light|signal|parking|fence|grass|bench|garbage|litter|pothole|snow|sidewalk|playground|path|trail)')<>'' and regexp_extract(lower(b.descr),'(can|sign|graffiti|tree|light|signal|parking|fence|grass|bench|garbage|litter|pothole|snow|sidewalk|playground|path|trail)')=regexp_extract(lower(c.descr),'(can|sign|graffiti|tree|light|signal|parking|fence|grass|bench|garbage|litter|pothole|snow|sidewalk|playground|path|trail)'))""").m[0]
nb=q("select count(*) n from bnc").n[0]
real=match(0); placebo=np.mean([match(s) for s in (14,28,-14)])
print('bounces with nid',nb,'matched',real,f'{real/nb:.1%}','placebo',placebo,f'{placebo/nb:.1%}')
# also: share of bounces with a same-nid same-category ticket in another area within 72h of CREATION (sign that resident/311 re-filed)
# where do bounces go? for the can code, matched successor areas
print(q("""select c.area, count(distinct b.row_id) n from bnc b join cand c on c.nid=b.nid and c.area<>b.area and c.dc between b.dcl - interval 1 hour and b.dcl + interval 72 hour and c.cat=b.cat group by 1 order by 2 desc limit 10""").to_string())
# neighbourhood coverage among phone referrals
print(q("select yr, avg((nid is null)::int) miss from p group by 1 order by 1").to_string())
# sibling owner by neighbourhood: garbage can family
can=q("""select yr, nid, area, coalesce(sd='311 Redirecting to Other Business Area',false)::int b from t2 where rt='Referral' and nid is not null and yr>=2024
 and descr in ('GARBAGE:Can Needs Emptying','Overflowing Garbage Can','311 - Empty Existing Garbage Can')""")
ok=can[can.b==0]
tr=ok[ok.yr<=2025].groupby(['nid','area']).size().unstack(fill_value=0)
own=tr.idxmax(axis=1); share=tr.max(axis=1)/tr.sum(axis=1)
te=can[(can.yr==2026)]
te=te.assign(pred=te.nid.map(own))
cov=te.pred.notna().mean()
okte=te[te.b==0]; acc=(okte.pred==okte.area)[okte.pred.notna()].mean()
base=(okte.area==ok[ok.yr<=2025].area.value_counts().idxmax()).mean()
print(f'can family 2026: tickets {len(te)}, nbhd known coverage {cov:.1%}, owner-by-neighbourhood accuracy on kept tickets {acc:.1%} vs majority-area baseline {base:.1%}')
bt=te[te.b==1]; print('2026 can-family bounces',len(bt),'where neighbourhood model disagreed with picked area', (bt.pred.notna() & (bt.pred!=bt.area)).sum())
print('median owner share per nbhd',share.median(), 'nbhds',len(share))
