import pandas as pd, numpy as np, sys
p=pd.read_pickle('p.pkl'); p['sd']=p['Status Detail']
VISIT=["Does Not Meet Bylaw Offence Standards","Assessed-No Action Required","Unable to Locate Animal","Location Not Found","Unable to Contact Complainant"]
DUP=["Duplicate Request Exists","Duplicate Request","Duplicate Request - See Related Ticket in Details"]
FAUI=["File Already under Investigation"]
BASE_DESK=["311 Redirecting to Other Business Area","Non-City Service or Location","Reported on same day - must submit after 10pm"]
def run(desk,label):
    p['wv']=p.sd.isin(VISIT).astype(int); p['wd']=p.sd.isin(desk).astype(int)
    df=p.groupby(['yr','code']).agg(n=('wv','size'),wv=('wv','sum'),wd=('wd','sum')).reset_index()
    tr=df[df.yr==2025].set_index('code'); te=df[df.yr==2026].set_index('code').copy()
    for col in ('wv','wd'):
        mu=tr[col].sum()/tr.n.sum(); k=10; a0,b0=mu*k,(1-mu)*k
        rate=(tr[col]+a0)/(tr.n+a0+b0)
        te['s_'+col]=te.index.map(lambda c: rate.get(c,mu)).astype(float)
    te['s']=te.s_wv+te.s_wd; te['w']=te.wv+te.wd
    print(f"\n=== {label}: 2026 wasted-visit {te.wv.sum()}, wasted-desk {te.wd.sum()}")
    ann=12/10.2
    for th in [0.20,0.30]:
        f=te[te.s>th]
        rng=np.random.default_rng(20261110); N=50000
        tri=lambda a,m,b: rng.triangular(a,m,b,N)
        FV=f.wv.sum()*ann; FD=f.wd.sum()*ann; FL=f.n.sum()*ann
        visit=tri(22,84,280); desk=tri(5,10,20)/60*tri(36.93,41.99,52.09)
        avoid=tri(0.2,0.35,0.5); ask=tri(0.30,1.02,1.02)
        sav=FV*avoid*(visit+desk)+FD*avoid*(desk+16.29*0.25); cost=FL*ask; net=sav-cost
        q=lambda x: f"${np.mean(x)/1e3:,.0f}K (P10-P90 ${np.percentile(x,10)/1e3:,.0f}K-${np.percentile(x,90)/1e3:,.0f}K)"
        # break-even avoid share at means
        be=np.mean(cost)/np.mean((FV*(visit+desk)+FD*(desk+16.29*0.25)))
        print(f"th>{th:.0%}: codes {len(f)}, flagged {100*f.n.sum()/te.n.sum():.1f}% of 2026 phone referrals ({int(f.n.sum())}), wasted visits caught {100*f.wv.sum()/te.wv.sum():.1f}% ({int(f.wv.sum())}), desk caught {int(f.wd.sum())}, precision {100*f.w.sum()/f.n.sum():.1f}%")
        print(f"   flagged/yr {FL:,.0f}; gross {q(sav)}; cost {q(cost)}; net {q(net)}; P(net<0) {np.mean(net<0):.1%}; break-even avoided {be:.1%}")
run(BASE_DESK+DUP+FAUI,"ORIGINAL (with duplicates)")
run(BASE_DESK+FAUI,"NO DUPLICATES (keep File Already under Investigation)")
run(BASE_DESK,"NO DUPLICATES, NO 'File Already under Investigation'")
