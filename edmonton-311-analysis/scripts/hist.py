"""Year-by-year out-of-time check of the empty-visit score: train on year Y-1, test on year Y, 2017 to 2026.
2016-2022 from the City's yearly 311 datasets (aggregated by SoQL, distinct row_id); 2023-2026 from the team's six-part export."""
import json, pandas as pd, numpy as np
VISIT = ["Does Not Meet Bylaw Offence Standards", "Assessed-No Action Required", "Unable to Locate Animal", "Location Not Found", "Unable to Contact Complainant"]
DESK = ["311 Redirecting to Other Business Area", "Non-City Service or Location", "Reported on same day - must submit after 10pm"]
rows = []
for y in range(2016, 2023):
    for x in json.load(open(f"/tmp/claude-0/sc/hist/agg_{y}.json")):
        a, c, d = x.get("service_area"), x.get("service_category"), x.get("service_description")
        code = f"{a} | {c} | {d}" if (a and c and d) else None
        rows.append((int(x["year"]), code, x.get("status_detail"), int(x["n"])))
h = pd.DataFrame(rows, columns=["yr", "code", "sd", "n"])
parts = [pd.read_pickle("/tmp/claude-0/sc/hist/p23.pkl"), pd.read_pickle("/tmp/claude-0/sc/nd/p24.pkl"), pd.read_pickle("/tmp/claude-0/sc/nd/p.pkl")]
p = pd.concat(parts); p["sd"] = p["Status Detail"]
m = p.groupby(["yr", "code", "sd"], dropna=False).size().reset_index(name="n")
a = pd.concat([h, m[["yr", "code", "sd", "n"]]])
a["wv"] = a.n.where(a.sd.isin(VISIT), 0); a["wd"] = a.n.where(a.sd.isin(DESK), 0)
c = a.groupby(["yr", "code"], dropna=False)[["n", "wv", "wd"]].sum().reset_index()
print(c.groupby("yr")[["n", "wv", "wd"]].sum().assign(wv_rate=lambda x: (100 * x.wv / x.n).round(2), wd_rate=lambda x: (100 * x.wd / x.n).round(2)).to_string())
print(a[a.sd.isin(VISIT)].pivot_table(index="sd", columns="yr", values="n", aggfunc="sum").fillna(0).astype(int).to_string())

def auc(s, n, b):
    d = pd.DataFrame({"s": s, "p": b, "q": n - b}).groupby("s").sum().sort_index(); cq = d.q.cumsum() - d.q
    return (d.p * (cq + 0.5 * d.q)).sum() / (d.p.sum() * d.q.sum())

out = []
for Y in range(2017, 2027):
    tr = c[c.yr == Y - 1].dropna(subset=["code"]).set_index("code"); te = c[c.yr == Y].copy()
    N_tr = c[c.yr == Y - 1].n.sum()
    mu_v = c[c.yr == Y - 1].wv.sum() / N_tr; mu_d = c[c.yr == Y - 1].wd.sum() / N_tr
    rv = (tr.wv + mu_v * 10) / (tr.n + 10); rd = (tr.wd + mu_d * 10) / (tr.n + 10)
    sv = te.code.map(rv).fillna(mu_v).values; sd_ = te.code.map(rd).fillna(mu_d).values
    s = sv + sd_
    fl = s > 0.20; flv = sv > 0.20
    out.append(dict(year=Y, auc_field_score=round(auc(sv, te.n.values, te.wv.values), 3), auc_deck_score_visits=round(auc(s, te.n.values, te.wv.values), 3),
                    auc_deck_score_anywaste=round(auc(s, te.n.values, (te.wv + te.wd).values), 3),
                    flag=round(100 * te.n[fl].sum() / te.n.sum(), 1), caught=round(100 * te.wv[fl].sum() / te.wv.sum(), 1), codes=int(fl.sum()),
                    flag_fieldonly=round(100 * te.n[flv].sum() / te.n.sum(), 1), caught_fieldonly=round(100 * te.wv[flv].sum() / te.wv.sum(), 1),
                    n=int(te.n.sum()), wv=int(te.wv.sum()), wv_rate=round(100 * te.wv.sum() / te.n.sum(), 2)))
r = pd.DataFrame(out); print(r.to_string()); r.to_csv("/tmp/claude-0/sc/hist/empty_visit_backtest_2017_2026.csv", index=False)

# one year of history against three (deck score, empty visits as the outcome)
k3 = []
for Y in range(2019, 2027):
    res = {}
    for k in (1, 3):
        trn = c[(c.yr < Y) & (c.yr >= Y - k)]
        tr = trn.dropna(subset=["code"]).groupby("code")[["n", "wv", "wd"]].sum(); te = c[c.yr == Y]
        mu_v = trn.wv.sum() / trn.n.sum(); mu_d = trn.wd.sum() / trn.n.sum()
        s = te.code.map((tr.wv + mu_v * 10) / (tr.n + 10)).fillna(mu_v).values + te.code.map((tr.wd + mu_d * 10) / (tr.n + 10)).fillna(mu_d).values
        res[k] = round(auc(s, te.n.values, te.wv.values), 3)
    k3.append((Y, res[1], res[3]))
print("AUC one year vs three years of history:", k3, "max gap", max(abs(a_ - b_) for _, a_, b_ in k3))
